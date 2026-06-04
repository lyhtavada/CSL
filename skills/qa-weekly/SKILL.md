---
name: qa-weekly
description: Weekly QA review of CS chats for Team G2. Fetches a week of Crisp sessions per CS from the Public Admin API, samples up to 30, pulls full transcripts from BigQuery, grades each CS against the weekly rubric (score + strengths + improvements with quotes, vs last week), then DMs each CS via the Avada bot after Liz approves. Use when Liz says "/qa-weekly", "QA tuần này", "chấm QA tuần cho team".
---

# QA Weekly Skill

Run a coaching-focused weekly QA pass for Team G2 and DM each CS a personal report.

This is **coaching, not penalty** — different from the monthly QA (`playbooks/qa-policy.md`).
Scoring follows `playbooks/qa-weekly-rubric.md`.

## When to use

Liz says `/qa-weekly`, "QA tuần này / tuần trước", "chấm QA tuần cho team".

## Parameters

- **Period** (default: **last completed week**, Mon–Sun):
  - no arg → last completed week
  - "tuần này" → current week Mon → today
  - "2026-W22" or a date → that ISO week
- **App:** both Joy + Chatty (default). Roster is Team G2 only (`_identity/team-g2.md`).
- **Sample:** 30 chats/CS (`--sample`).

## Flow (fan-out via Workflow — runs in background)

The heavy lifting (grading ~15 CS × up to 30 chats) is done by a **Workflow**
that fans out one grading subagent per CS, in parallel. Main thread only
fetches data, kicks off the workflow, and assembles the result.

### Step 1 — Resolve the week

Compute Mon–Sun for the target week. Default = last completed week.
Derive `iso_week` (e.g. `2026-W22`) and the previous week tag for comparison.

### Step 2 — Fetch sessions (main thread)

```bash
python3 skills/qa-weekly/scripts/fetch_sessions.py \
  --start <MON> --end <SUN> \
  --out /tmp/qa_weekly_sessions.json --sample 30 \
  --only-type in-house
```

**Only QA in-house CS** (`--only-type in-house`) — remote/CTV are not graded
weekly. The "Loại" column in `_identity/team-g2.md` marks each CS as
`in-house` / `remote` / `csl`. To change who's graded, edit that column — no
code change. (Liz the CSL is `csl` and never in `in-house`, so she's excluded
automatically; no need for `--exclude Liz`.)

Current in-house (9): Hana, Audrey, Alyssa, Jade, Sonny, Andy, Hazel, Phoebe, Linda.

Groups all sessions by `agentUser.nickname`, keeps only Team G2 members
(mapped to Slack ID + email via `_identity/team-g2.md`), drops AI-bot /
unassigned chats, samples ≤30 per CS. Queries **one day at a time** because the
API's `page`/`cursor` params are ignored — only `limit` works (~2000 cap/call).

### Step 3 — Fetch transcripts per CS (main thread)

For each CS in the sessions file:

```bash
python3 skills/qa-weekly/scripts/fetch_transcripts.py \
  --sessions-file /tmp/qa_weekly_sessions.json --cs <Name> \
  --out /tmp/qa_tx_<Name>.txt
```

Pulls full message-level transcripts from BigQuery
`avada-crm.avada_cs.crisp_chats`. **Note:** a session may contain messages from
several CS (handoffs across shifts) — the grader must score ONLY the target
CS's own messages.

### Step 4 — Grade (Workflow fan-out)

Run the workflow `skills/qa-weekly/qa-weekly.workflow.js`. One subagent per CS:
reads that CS's transcript file + the rubric, returns structured JSON
(score, label distribution, strengths with chat refs, improvements with quotes).
Workflow runs in background and reports once when ALL CS are done.

Pass `args` as a **plain array of CS nicknames**, e.g.
`["Alicia","Andy",...]`. The script builds `/tmp/qa_tx_<name>.txt` paths itself
and reads app/chat-count from each transcript. **Quirk:** the runtime may deliver
`args` as a JSON *string*, not a parsed array — the script handles both
(`JSON.parse` if string). If a run returns `{results:[]}` with log
"No CS to grade", check the args shape in the workflow output log.

### Step 5 — Compare to last week (main thread)

For each CS, read last week's report in `reports/qa-weekly/` if it exists.
Compute score delta, repeated error codes, and fixed error codes. First week →
"Tuần đầu, chưa có dữ liệu so sánh."

### Step 6 — Write reports + team summary

- Per CS: `reports/qa-weekly/qa-weekly-<CS>-<YYYY-Www>.md`
- Team summary for Liz: `reports/qa-weekly/qa-weekly-summary-<YYYY-Www>.md`
  (score table, who needs coaching, flagged severe issues)

### Step 7 — Liz reviews, then DM

1. Build DM payload `/tmp/qa_dm_payload.json` (`{week, messages:[{cs, slack_id, text}]}`)
   using the DM format in the rubric (§5).
2. **Show Liz the full team summary + each DM text. Wait for explicit approval.**
3. Dry-run first:
   ```bash
   python3 skills/qa-weekly/scripts/send_dm.py --payload /tmp/qa_dm_payload.json
   ```
4. On Liz's OK, send for real:
   ```bash
   python3 skills/qa-weekly/scripts/send_dm.py --payload /tmp/qa_dm_payload.json --send
   ```

## Safety rules

- **Never DM without Liz's explicit approval** (Step 7.2).
- Severe findings (KN8 rude, QT11 ignored customer, KT1 wrong info) → **flag in
  the summary for Liz to review individually**, never auto-send.
- A finding must quote the chat as evidence. No evidence → don't report it.
- Score only the target CS's messages, not handoff colleagues'.

## Files

- Rubric: `playbooks/qa-weekly-rubric.md`
- Roster (CS → Slack ID): `_identity/team-g2.md`
- Scripts: `skills/qa-weekly/scripts/`
- Workflow: `skills/qa-weekly/qa-weekly.workflow.js`
- Output: `reports/qa-weekly/`
