---
name: kb-test
description: >
  Generate test questions from a recent KB change (kb-sync patch, or any
  described change), batch-run them against the live bot (Joyce/Ivy) via
  /api/chat, then Betty reads every answer against the source-of-truth and
  reports verdict + suggestion. Use right after a kb-sync push, or any time
  Liz wants to sanity-check what the bot is actually saying on a topic.
---

# /kb-test — generate test questions, run them live, Betty judges

Closes the loop on a KB patch: don't just trust that push+reindex worked —
ask the bot the questions a merchant would ask and read what it says.

Keyword pass/fail is deliberately **not** built into the runner script.
A correct answer can be phrased many ways, and a wrong one can still contain
the "right" keyword — judging requires actually reading the reply, which is
Betty's job, not a grep.

## Inputs

- **app** — `chatty` (Ivy) or `joy` (Joyce) or `wishlist` (Wendy). Ask if not given.
- **context** — what changed and needs testing. Usually one of:
  - The payload/summary from a just-finished `/kb-sync` run (files touched +
    what OUTDATED/GAP items were patched)
  - A specific KB file or topic Liz names directly
  - A list of questions Liz already wrote herself (skip straight to Run)

## Flow

### 1. Generate test questions (judgment — you do this)

For each patched item, write 1-2 test questions **in merchant phrasing**, not
KB phrasing — don't quote the KB's own wording back at it, ask the way a real
merchant would in chat. Cover:

- **Every OUTDATED fix** — a question that would have surfaced the *old wrong
  answer* before the patch. This is the highest-value test: if the bot still
  gives the stale fact, the patch didn't take.
- **High-value GAP/PARTIAL additions** — a question the bot previously had no
  good answer for.
- **1-2 rephrasings of the trickiest item** — different wording of the same
  fact, to catch retrieval fragility (a chunk can be correct but only surface
  for certain phrasings — this has happened before, see
  `references/retrieval-fragility-note.md` if present, or just note it fresh).

Write questions to a JSON file (array of strings, or `{"id","question"}`
objects if you want stable labels): `/tmp/kb-test/<app>-<date>-questions.json`.

Aim for **5-15 questions** — enough to cover every patched fact once, without
turning this into an exhaustive regression suite.

### 2. Run (mechanical)
```
cd ~/CSL/skills/kb-test/scripts
python3 run_tests.py <app> /tmp/kb-test/<app>-<date>-questions.json /tmp/kb-test/<app>-<date>-results.json
```
This POSTs each question to `/api/chat` for the live agent and dumps raw
`{id, question, reply, sources_count, duration_ms}` per question — no
verdict yet.

### 3. Judge (judgment — you do this)

Read every reply against the source-of-truth (the patched KB content, or the
mined-FAQ answer if this isn't a kb-sync follow-up). For each question decide:

- **PASS** — states the current-correct fact, no stale/wrong claim.
- **FAIL** — repeats the old wrong fact, or gives a materially incomplete/
  misleading answer.
- **PARTIAL** — correct on the core fact but missing a caveat that matters
  (plan gating, a condition, an escalation trigger).

If something FAILs, don't just flag it — form a hypothesis: is the KB content
itself still wrong (re-check the live file), is it a retrieval/chunking issue
(content is right but doesn't surface for that phrasing — try a rephrase to
confirm), or is it a model reasoning slip on top of correct retrieved content?
State which one in the suggestion.

### 4. Report

Table: **# | Question | AI's answer (trimmed to the load-bearing sentence(s)) |
Verdict | Betty's suggestion**. Suggestions should be concrete and actionable,
e.g.:
- "OK, no action"
- "KB content is right — retrieval issue with this phrasing, re-test after next reindex / consider adding this phrasing as a synonym in the KB file"
- "KB still wrong at `kb/reference/x.md` line N — needs another patch"
- "Bot is factually right but the answer is confusing/verbose — consider tightening the KB source"

Then a one-line overall score (e.g. "8/10 PASS, 2 need follow-up") and ask
Liz whether to act on the follow-ups now or log them for next week's kb-sync.

## Notes
- Results files under `/tmp/kb-test/` are scratch — don't commit them. If
  Liz wants a persistent record, write the final markdown report to
  `reports/analysis/kb-test-<app>-<date>.md` only on request.
- `run_tests.py` reuses `../../kb-sync/scripts/kb_api.py` for creds and the
  `/api/chat` client (`chat(base, token, agent, message)`).
- The bot always opens with a scripted greeting ("Hi! I'm Joyce...") — that's
  cosmetic, judge the substance after it.
- If every question in a batch comes back with `sources_count: 0` or a
  generic non-answer, suspect the agent id or that reindex is still running
  rather than a content problem — check before judging individual answers as
  FAIL.
