---
name: kb-sync
description: >
  Sync a weekly mined-FAQ file against the live CS v2 knowledge base (Chatty/Ivy
  or Joy), produce a diff (COVERED / OUTDATED / GAP / PARTIAL), draft patches to
  the existing KB files, then — after Liz approves — push to v2 and reindex.
  Use when Liz says "kb-sync", "đồng bộ KB", "so KB với FAQ tuần này", or after
  /mine-chat-faqs produces a new file.
---

# /kb-sync — Weekly FAQ → KB v2 sync

Takes the latest mined-FAQ file (real customer questions + answers) and brings the
**live CS v2 knowledge base** of the AI agent up to date with it. Diff first, Liz
approves, then push + reindex.

## Inputs

- **app** — `chatty` (agent `chatty-agent` / Ivy), `joy` (agent `joy-loyalty-agent`), or `wishlist` (agent `wishlist-agent` / Wendy — still `enabled:false`, pre-launch as of 2026-07-22; KB uses the `reference`/`case` schema, not the old flat `faq` Q:/A: format — match that when patching).
  Ask if not given. Default: do `chatty` first.
- **FAQ file** — newest in `~/CSL/reports/weekly-faqs/<app>/`
  (output of `/mine-chat-faqs`). Liz can override with an explicit path.

## The v2 KB API (confirmed)

Base + token in `~/CSL/.env` → `CS2_API_URL`, `CS2_API_TOKEN`. Auth `Bearer`.
- `GET  /api/kb/files?agent=<id>` — list files
- `GET  /api/kb/file?agent=<id>&path=<p>` — read `{content}`
- `POST /api/kb/file` body `{agent,path,content}` — write 1 file (auto git commit)
- `POST /api/kb/reindex` body `{agent}` — re-embed so the agent uses new content
  (returns `{ok,chunks,partial}`; `partial:false` = full success)

> Writes go through the helper scripts. The reindex step is what makes the agent
> actually use the new content — never skip it after a successful push.

## Flow

### 1. Prep (mechanical)
```
cd ~/CSL/skills/kb-sync/scripts
python3 prep.py <app>            # or: prep.py <app> --faq <path>
```
Downloads all KB files to `/tmp/kb-sync/<app>/` (paths flattened with `__`) and
prints a manifest: the FAQ file used, agent id, and the full KB file list.

### 2. Diff (judgment — you do this)
Read the mined-FAQ file fully, then for **each FAQ** find the matching KB file(s)
in the cache (grep `/tmp/kb-sync/<app>/` by topic/keyword) and classify:

- **COVERED** — KB already has equivalent, accurate, current content → no action.
- **OUTDATED** — KB covers it but a fact contradicts the fresher mined answer.
  Quote the stale line + the correct line.
- **GAP** — KB has no equivalent → name the file it should go into.
- **PARTIAL** — KB covers part, missing a sub-point → name file + the sub-point.

Mined FAQs are the **fresher signal** (real chats this week). When they contradict
the KB on a concrete fact (address, limit, plan rule, retention), the mined fact wins.
Verify every candidate discrepancy against the actual cached file — never assume.

Output a summary table (Q# | topic | KB file | verdict) + the OUTDATED / GAP /
PARTIAL detail, and a short priority list ranked by mined frequency (high-freq first).

For a large batch, use the Agent tool to parallelize the read-heavy compare
(see `references/diff-prompt.md`), then review its findings yourself.

### 3. Draft patches → build payloads
For each OUTDATED/GAP/PARTIAL item, build the **full new file content** (not a
fragment): start from the cached file, insert/replace at a real anchor heading,
match the KB's existing voice (`## Heading`, frontmatter `tags`). Prefer adding a
new `## Section` over rewriting; for OUTDATED facts, edit in place.

**For `kb/case/*.md` specifically, write each scenario to this template** (learned
from blog-agent's `kb/reference/billing.md`, applied to Chatty/Joy billing-refund
rewrites on 2026-08-22 — this is now the default bar, not optional polish):

- **One `## Heading` = one concrete situation**, phrased from the merchant's
  side (`## Merchant wants to cancel`, not `## Resolution Steps`). Chunking is
  per-heading, so a generic/repeated heading (`## Resolution Steps` reused
  across 5 unrelated cases in one file) produces chunks with no topic signal —
  this was a real bug found in Joy's old `kb/case/billing.md`. Never reuse a
  heading string across scenarios in the same file.
- **`**Symptom phrasings (any of):**`** right under the heading — 4-6 natural
  ways a merchant might actually phrase it. This isn't a keyword whitelist
  (retrieval is semantic embedding, not exact match) — it enriches the
  chunk's embedding to catch more phrasing angles.
- **Scripted reply as a blockquote** (`> ...`), not just an internal
  instruction — the bot should be able to use it close to verbatim. When a
  reply needs multiple beats in one turn, split with `<<<SPLIT>>>` on its own
  line (bridge renders each as a separate bubble).
- **When you need evidence before acting** (screenshot, confirmation), use the
  `Step 1 → WAIT for reply → Step 2` pattern explicitly — write "→ **WAIT for
  ...**" so the bot doesn't escalate before it has what the team needs.
- **End with the real tag**, not a placeholder — `` `<escalate reason="..."/>` ``
  (confirm the exact tag/attribute the target agent actually uses — Chatty and
  Joy both use `<escalate reason="...">`, but check `persona/*.md` and
  `flows/*.md` per app before assuming). Put a real, specific `reason` (what
  was collected, not just the case name) — it's the handoff note a human
  reads, not a label.
- **`**❌ Do NOT:**` bullet list** closing the scenario — the specific wrong
  moves for that case (promise a number, argue, self-approve, imply auto-fix).
  This is what stops the bot from improvising outside its authority.
- A reusable line (e.g. the screenshot-request template) can live once near
  the top of the file and be referenced by later scenarios — don't repeat the
  same paragraph in every case.

This template is for `kb/case/*.md` (bot-facing scripted scenarios).
`kb/faq/*.md` and `kb/reference/*.md` follow their own, lighter templates:

**`kb/faq/*.md`** — plain factual Q&A, no scenario/escalation logic:
- Literal `Q: <question>` / `A: <answer>` pairs, one blank line between pairs,
  no `## Heading` wrapper needed (this is blog-agent's format — see
  `kb/faq/general.md` on the `blog-agent` — and it's the simpler, more literal
  cousin of Chatty/Joy's current `kb/faq/*.md`, which mix in `## Heading` +
  bold-question-as-lead-in prose; either is fine, just match what the target
  file already does — see step 3's opening rule).
- Each `A:` should be a **complete, standalone answer** — same "no relying on
  a sibling section" rule as case files, since FAQ files also chunk per Q/A
  or per heading.
- No `<escalate>` tags, no "Symptom phrasings", no Do NOT list — FAQ is pure
  fact, not a scenario the bot has to navigate. If an item actually needs
  judgment/escalation, it belongs in `kb/case/`, not `kb/faq/`.

**`kb/reference/*.md`** — longer internal/CS-process docs (playbooks, pricing
tables, eligibility criteria, routing rules) — not primarily bot scripts, but
still often retrieved directly by the bot, so the same rules apply where relevant:
- `## Heading` per topic, same self-contained-per-heading rule as case files.
- Tables are fine and often clearer than prose for plan/pricing/eligibility
  data (see blog-agent's `kb/reference/pricing.md` and `billing.md`).
- **Any FAQ-style sub-section inside a reference file** (a short factual Q
  answered in a couple sentences) should still get a **scripted blockquote
  reply** — not just an internal instruction — so the bot can use it near-
  verbatim. Example: "Common Billing Questions" in Joy's
  `kb/reference/billing-refund.md`.
- **Any escalation instruction** inside a reference file must use the real
  tag (`` `<escalate reason="..."/>` ``), never prose like "escalate to the
  team" or a placeholder like "Append escalate tag here" — same rule as case
  files above.
- Reference files can and should hold things case files shouldn't: internal
  routing/ownership notes (who handles what), eligibility criteria, and
  process steps aimed at a human CS agent reading it directly, not just RAG
  chunks for the bot.

Write a payloads file = JSON array of `{agent, path, content}`:
```
reports/analysis/kb-sync-<app>-<YYYY-MM-DD>-payloads.json
```
(Use a Python script like the build steps in `references/build-example.py`. Assert
each anchor exists before replacing so a moved heading fails loudly, not silently.)

### 4. Review gate — STOP and show Liz
Print the diff summary + the list of files that will change + new section titles.
**Wait for Liz's approval.** Do not push before she says go. (Headless/cron runs
stop here and notify her — see Cron below.)

### 5. Push + reindex (after approval)
```
cd ~/CSL/skills/kb-sync/scripts
python3 push_kb.py ../../../reports/analysis/kb-sync-<app>-<date>-payloads.json
```
POSTs each file (auto git commit), then reindexes once. Re-runnable (idempotent).
Each write is a git commit in the content repo → revertable.

> If Claude is blocked by the permission classifier from POSTing to production,
> hand Liz the one-liner to run in Terminal instead:
> `python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>`

### 6. Verify
Re-GET the changed files and confirm the new content is present and any stale
string is gone. Confirm the reindex returned `partial:false`. Report what changed.

## Notes
- Do NOT save KB content into the CSL repo — KB lives in v2. The audit trail is
  the git history on the v2 side (push auto-commits there).
- Payload files (`reports/analysis/kb-sync-*-payloads.json`) are temporary: built
  → reviewed → pushed. They are gitignored (never committed) and `push_kb.py`
  deletes each one after a successful push. Pass `--keep` to retain it.
- KB layout (Chatty only has `flows/`; Joy/Wishlist don't): `flows/` = bot's live
  routing scripts (YAML `triggers` + action tags `<ticket>`/`<escalate>`/
  `<consult_ts>`, matched deterministically by keyword), `kb/case/` = deeper
  reference for a case type, `kb/faq/` = customer-facing answers, `kb/reference/`
  = internal CS guidance, `persona/` = identity (rarely touch).
- **Where to patch a finding (flow vs case/faq/reference):** default to
  `kb/case`, `kb/faq`, or `kb/reference` — that's where nearly everything from
  `/bot-corrections` and `/mine-chat-faqs` belongs (factual/knowledge fixes).
  Only also patch a `flows/*.md` file when BOTH: (1) the finding is about what
  **system action** the bot should take (create a ticket, escalate, or consult
  TS) rather than just what it should say, AND (2) an existing flow already
  covers that topic — add the new root-cause/exception to its causes list or
  "Never create a ticket when" section. Do not create a brand-new flow file for
  a routine correction/mined-FAQ finding — a new flow is only worth it when the
  bot can actually execute the action itself for a recurring request pattern,
  and its trigger keywords don't collide with the existing flows. When a topic
  has both a matching flow and a case file, patch both — the flow controls
  what the bot does, the case is what RAG retrieves for detail, and patching
  only the case still leaves the flow ignorant of the new known-cause.
- Both apps: run the flow once per app. Reindex is per-agent.
