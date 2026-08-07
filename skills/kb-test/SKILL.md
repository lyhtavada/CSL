---
name: kb-test
description: >
  Generate test questions from a recent KB change (kb-sync patch, or any
  described change), batch-run them against the live bot (Joyce/Ivy) through
  the real pipeline via a local sim-crisp process (falls back to /api/chat
  if sim isn't set up), then Betty reads every answer against the
  source-of-truth and reports verdict + suggestion. Use right after a
  kb-sync push, or any time Liz wants to sanity-check what the bot is
  actually saying on a topic.
---

# /kb-test — generate test questions, run them live, Betty judges

Closes the loop on a KB patch: don't just trust that push+reindex worked —
ask the bot the questions a merchant would ask and read what it says.

Keyword pass/fail is deliberately **not** built into the runner script.
A correct answer can be phrased many ways, and a wrong one can still contain
the "right" keyword — judging requires actually reading the reply, which is
Betty's job, not a grep.

## Sim mode (default) vs. direct mode

Two ways to run step 2:

- **Sim mode (`run_tests_sim.py`, default)** — sends questions through the
  REAL bridge pipeline (webhook -> gate -> worker -> `process.ts` -> agent)
  against a local sim-crisp process. Catches things a raw API call can't:
  multi-turn context, the `human_active` gate, greeting behavior. See
  `docs/sim-crisp.md` in the bridge repo
  (`avada/cs-team/avada-cs-ai-agent-crisp-chat`, cloned locally at
  `~/avada-cs-ai-agent-crisp-chat`) for how the sim works.
- **Direct mode (`run_tests.py`, fallback)** — calls `/api/chat` directly.
  Faster/cheaper, single-turn only, skips gates. Use when the sim bridge
  isn't set up yet, or for a quick one-off sanity check.

**One-time sim setup** (skip if already done):
```
tailscale up   # must reach prod Postgres via HAProxy
cp skills/kb-test/scripts/sim.env.example ~/avada-cs-ai-agent-crisp-chat/.env.sim
# fill in DATABASE_URL password, ANTHROPIC_API_KEY, a random CRISP_WEBHOOK_SECRET
```
`run_tests_sim.py` auto-starts the sim process if it isn't already running
(via `start_sim.sh`); you can also start it manually first. It shares prod
Postgres (agents/KB/personas) but only ever writes rows under
`website_id='sim-crisp'` — no real merchant data touched. If auth fails
(403), the reused `CS2_API_TOKEN` may lack `console.chat` permission — ask
for a token that has it.

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

Write questions to a JSON file: `/tmp/kb-test/<app>-<date>-questions.json`.
Array of items — a plain string or `{"id","question"}` for single-turn, or
`{"id","turns":["...","..."]}` for a multi-turn case (only meaningful in sim
mode; direct mode only sends `turns[0]`).

Aim for **5-15 questions** — enough to cover every patched fact once, without
turning this into an exhaustive regression suite. Use a multi-turn case
specifically when a patched fact only matters as a follow-up (e.g. "what if
I'm past the 30-day window" after a refund-policy question) or to test the
gate (a `turns` entry sent `"as":"human"` isn't supported by the JSON format
yet — for that, test manually via the curl examples in `docs/sim-crisp.md`).

### 2. Run (mechanical)
```
cd ~/CSL/skills/kb-test/scripts
python3 run_tests_sim.py <app> /tmp/kb-test/<app>-<date>-questions.json /tmp/kb-test/<app>-<date>-results.json
```
Runs each question through the real pipeline via sim-crisp and dumps raw
`{id, turns:[{question, reply, status, suppress_reason, timed_out}], final_reply}`
per item — no verdict yet. Falls back to `run_tests.py` (same call
signature, `/api/chat`) if sim isn't set up.

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
- `run_tests_sim.py` uses `sim_client.py` (this dir) — creds are
  `CS2_API_TOKEN` (reused as sim bearer token) + `SIM_BASE_URL` from
  `~/CSL/.env`. `run_tests.py` (direct mode) reuses
  `../../kb-sync/scripts/kb_api.py` for the `/api/chat` client instead.
- The bot always opens with a scripted greeting ("Hi! I'm Joyce...") — that's
  cosmetic, judge the substance after it.
- Sim mode: each question runs in its own throwaway session (cleaned up
  after), so a bare `status`/`timed_out` on a result is worth checking before
  judging content — a stuck pipeline (agent disabled, gate misroute) looks
  different from a wrong-but-delivered answer. Direct mode: if every question
  in a batch comes back with `sources_count: 0` or a generic non-answer,
  suspect the agent id or that reindex is still running rather than a
  content problem.
