---
name: product-kb-sync
description: >
  Proactively sync CS v2 knowledge base with product changes BEFORE merchants
  ask about them — pulls the weekly product-release Slack post + a GitLab diff
  on label/nav/feature-doc files, drafts patches, Liz approves, then push +
  reindex (reuses kb-sync's push mechanism). Complements /kb-sync and
  /bot-corrections, which are reactive (they fix KB gaps already exposed by
  a real merchant question). Use when Liz says "product-kb-sync", "cập nhật
  KB theo release", or after a new post appears in the shared product-release
  Slack channel.
---

# /product-kb-sync — proactive KB sync from product changes

Two source-of-truth signals, per app, feed into the same patch → review →
push flow as `/kb-sync`:

- **A — Slack** (`config.RELEASE_CHANNEL_ID`, shared by all 3 apps): weekly
  human-written release notes. Already has merchant-facing meaning attached —
  the writer chose what's worth telling CS. Highest-confidence signal.
- **B1 — GitLab feature docs** (per-app path in `config.py`): curated prose,
  engineering-voiced. Good for understanding *why*/*how* a feature works in
  depth, but needs rewriting before it can go into a support KB file directly.
  **Does not exist for Wishlist** — skip B1 for that app.
- **B2 — GitLab label/nav files** (per-app paths in `config.py`): raw diff of
  the actual copy/nav that ships. Catches changes nobody wrote a release note
  for (menu renames, label tweaks). Zero narrative — a diff, not a reason.

## Inputs
- `app` — `chatty` | `joy` | `wishlist`. Ask if not given.
  Wishlist is low priority: agent (Wendy) is `enabled:false`/pre-launch.

## Flow

### 1. Fetch signals (mechanical)
```
cd ~/CSL/skills/product-kb-sync/scripts
python3 fetch_slack.py <app>              # new messages since state's last_slack_ts
python3 fetch_gitlab.py <app>             # diff since state's last_gitlab_commit
```
Neither script updates state — that happens only in step 6, after the diff
this run actually produces has been used. A crash mid-run should not silently
drop a week's signal.

`fetch_slack.py` reads the **shared** channel — every run for every app sees
every message (Chatty posts and Joy posts land in the same channel). Filter
by content, not by channel.

### 2. Read + classify (judgment — you do this)
Read the Slack messages and the GitLab diffs fetched above.

- For B2 diffs on a noisy path (`appMenu.js` for Joy, `AppFullLayout.js` for
  Chatty — see `notes` field per app in `config.py`): first decide if the
  diff is even a copy/nav change or just unrelated logic/refactor. Discard
  non-copy diffs before treating them as a signal.
- For each surviving item (from A or filtered B2, plus B1 as supporting
  context), classify against the live KB the same way `/kb-sync` does:
  **COVERED / OUTDATED / GAP / PARTIAL**. Use `~/CSL/skills/kb-sync/scripts/
  prep.py <app>` to cache the live KB first — reuse it, don't re-fetch.

### 3. Draft patches
For each OUTDATED/GAP/PARTIAL item:
- **GAP** (brand-new feature) → write it as a feature-doc-style description
  (what/where/how/conditions), not a guessed Q&A. RAG retrieval matches on
  meaning, not exact merchant phrasing, so a clear description is enough —
  don't invent questions nobody has asked yet.
- **OUTDATED** (existing feature's behavior changed) → find and edit the
  actual KB file describing the old behavior. Never just append a new
  section next to stale info — that leaves two conflicting facts in the KB.
- **Always English**, even though the Slack source is Vietnamese — hard rule,
  see memory `feedback_kb_files_english_only`.
- **Every `## Heading` must stand alone** for retrieval — write each section
  so it's answerable on its own, don't rely on context from a sibling
  section (chunking is per-heading).
- Default target: `kb/case/` or `kb/faq/`. Only touch `flows/*.md` when the
  change is about a **system action** (ticket/escalate/consult_ts) AND a
  matching flow already exists — see `flow_vs_case_patch_rule` in memory.
- Build the same payloads format as `/kb-sync`:
  `reports/analysis/product-kb-sync-<app>-<date>-payloads.json`,
  array of `{agent, path, content}` (full file content per entry).

### 4. Review gate — STOP and show Liz
Print: which Slack items and which GitLab paths were used, the
COVERED/OUTDATED/GAP/PARTIAL table, and the files that will change.
**Wait for approval.** Cron runs stop here and notify her (see Cron below).

### 5. Push + reindex (after approval)
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>
```
Reuse `kb-sync`'s script directly — do not duplicate it here.

### 6. Verify — run `/kb-test`
There is no real merchant question to validate against (that's the whole
point of this being proactive), so this step is not optional the way it is
for `/kb-sync`. Write a few plausible merchant-phrased test questions for
whatever was just patched, run them through `/kb-test`, confirm retrieval
picks up the new content correctly.

### 7. Update state
Only after 5+6 succeed:
```python
import state
state.update_app_state("<app>",
    last_slack_ts=<latest_ts from step 1's fetch_slack.py output>,
    gitlab_commits={"<project>": "<to_sha from fetch_gitlab.py output>"})
```
If Liz doesn't approve anything this run (nothing worth patching), still
advance the state — otherwise the next run re-surfaces the same already-
reviewed-and-rejected items.

## Notes
- `config.py` — per-app repo paths (B1/B2) and Slack channel id. Look here
  first; paths are NOT uniform across apps, don't assume symmetry.
- `state/last_sync.json` — committed to the repo (small, needed across runs,
  unlike kb-sync's gitignored temp payloads). Don't hand-edit without reason;
  editing it forward skips signal, editing it backward re-surfaces old signal.
- Wishlist has no B1 source and is low priority (pre-launch agent) — expect
  to mostly skip it until Wendy actually launches.
- GitLab access: `glab api`, read-only, per `gitlab_avada_repos.md` memory —
  never anything beyond GET.
