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

- **app** — `chatty` (agent `chatty-agent` / Ivy) or `joy` (agent `joy-loyalty-agent`).
  Ask if not given. Default: do `chatty` first.
- **FAQ file** — newest in `~/claw-weebhook-crisp-chat/Liz/faq_from_chats/<app>/`
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
- Do NOT save KB content into the CSL repo — KB lives in v2. Only the payloads +
  diff report land in `reports/analysis/` as an audit trail.
- `case/` = how-to-handle flows, `faq/` = customer-facing answers, `reference/` =
  internal CS guidance, `persona/` = identity (rarely touch). Put content where it fits.
- Both apps: run the flow once per app. Reindex is per-agent.
