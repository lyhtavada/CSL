---
name: qa-weekly
description: Weekly QA review of in-house Team G2 CS chats. Pulls each CS's real chats for the week from BigQuery (by agentEmail, ≥3 msgs in-week), samples up to 30, fans out one Sonnet grader per CS scoring on the 3-axis rubric (Mindset / Knowledge / Skill), writes per-CS reports + a team summary, then DMs each CS as Liz via the Avada bot — only after Liz approves. Use when Liz says "/qa-weekly", "QA tuần này", "chấm QA tuần cho team".
---

# QA Weekly Skill

Run a coaching-focused weekly QA pass for Team G2 and DM each CS a personal report.

This is **coaching, not penalty** — different from the monthly QA (`playbooks/qa-policy.md`).
Scoring follows `playbooks/qa-weekly-rubric.md`.

## Scoring model (3 axes)

Each chat is scored on 3 independent axes summing to 100:
- **🧠 Mindset (0–34):** ownership, empathy, proactive, effort to satisfy the customer
- **📚 Knowledge (0–33):** correct advice, verified against the agent KB (pricing table is embedded in the workflow prompt; other claims → read KB)
- **🛠️ Skill (0–33):** clarity, right flow, no comms errors

Weekly score = mean of per-chat scores. Labels: 90+ Xuất sắc · 80–89 Tốt · 70–79 Đạt · <70 Cần coaching. A technically-correct-but-cold CS loses ⅓ at Mindset; a caring + accurate CS with minor typos still scores high — by design.

**Language note:** Crisp has live-translate, so replying in the customer's language is NOT a strength (never praise "đa ngôn ngữ"). Only flag when the customer writes in one language and the CS replies in a *different* one → KN3 (Skill deduction).

## When to use

Liz says `/qa-weekly`, "QA tuần này / tuần trước", "chấm QA tuần cho team".

## Lịch tự chạy

Tự chạy **Thứ 2, 14:00** qua launchd (`com.avada.qa-weekly`, plist ở
`~/Library/LaunchAgents/`, runner `cron/run-weekly.sh` + `cron/prompt.txt`).
Cron chấm tuần vừa kết thúc + tạo report, rồi **gửi toàn bộ kết quả cho Liz duyệt
qua Slack DM** — KHÔNG tự DM cho CS. Liz review xong, ra lệnh thì mới gửi CS
(`send_dm.py --send`). Log: `/tmp/qa-weekly.log`.

## Parameters

- **Period** (default: **last completed week**, Mon–Sun):
  - no arg → last completed week
  - "tuần này" → current week Mon → today
  - "2026-W22" or a date → that ISO week
- **App:** both Joy + Chatty (default). Roster is Team G2 only (`_identity/team-g2.md`).
- **Sample:** 30 chats/CS (`--sample`).

## Flow (fan-out via Workflow — runs in background)

The heavy lifting (grading 9 in-house CS × up to 30 chats) is done by a
**Workflow** that fans out one grading subagent per CS, in parallel. Main thread
only fetches data, kicks off the workflow, and assembles the result.

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

**Source = BigQuery, NOT the Crisp `assigned` field.** The API's `agentUser`
only marks ONE owner per session and misses 70-90% of the chats a CS actually
worked (multiple CS touch one chat across shifts). Instead we query
`avada-crm.avada_cs.crisp_chats` by `agentEmail`:

- A session counts for CS X in week W **only if X sent ≥3 operator messages
  within week W**. This (a) attributes the chat to the week the CS actually
  worked it — even if the customer first wrote earlier — and (b) drops chats a
  CS only greeted/handed-off (1-2 lines).
- Sample = top 30 by in-week CS-message count (longest/real cases first).
- CS mapped via `agentEmail` → `_identity/team-g2.md`; `--only-type in-house`
  filters by the "Loại" column; CSL never graded.

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

Run the workflow `skills/qa-weekly/qa-weekly.workflow.js`. One **Sonnet** subagent
per CS reads that CS's transcript + the rubric and returns structured JSON:
`score`, `axis_avg` (mindset/knowledge/skill), `overall` (nhận xét chung),
`strengths`, `improvements` (with quotes + action), `severe_flags`,
`chats_reviewed` + `excluded`. Runs in background; reports when all CS are done.

Pass `args` as a **plain array of CS nicknames**, e.g. `["Hana","Andy",...]`.
The script builds `/tmp/qa_tx_<name>.txt` paths itself.

**Run in batches of 4–5 CS**, not all 9 at once — 9 graders over 30-chat
transcripts can hit the subscription usage limit. Save each batch's results,
then run the next; retry any CS that fails.

Operational gotchas:
- **Don't type in the session while a workflow is running** — it interrupts the
  in-flight subagents (they fail with "Request interrupted").
- The grader is told to score **every** chat (chats_reviewed + excluded = N). If
  a CS comes back with far fewer reviewed than its transcript has, re-grade it.
- **Quirk:** the runtime may deliver `args` as a JSON *string* — the script
  `JSON.parse`s it. If a run returns `{results:[]}` with "No CS to grade", check
  the args shape in the workflow log.
- Subagent uses Sonnet (`model:'sonnet'`), not Opus — keeps quota/cost down.

### Step 5 — Compare to last week (main thread)

For each CS, read last week's report in
`reports/qa-weekly/qa-weekly-<YYYY-W(##-1)>/` if it exists. Compute score delta,
repeated error codes, and fixed error codes. First week → "Tuần đầu, chưa có dữ
liệu so sánh."

### Step 6 — Write reports + team summary

One folder per week — `reports/qa-weekly/qa-weekly-<YYYY-Www>/`:
- Per CS: `qa-weekly-<CS>-<YYYY-Www>.md` — score + 3-axis breakdown,
  **📝 Nhận xét chung** (direct/"thẳng thắn" tone, calls the CS "bạn", never
  "em"), strengths, improvements (quote + action), vs-last-week.
- Team summary for Liz: `qa-weekly-summary-<YYYY-Www>.md` — score table with
  per-axis averages, who needs coaching, severe/KB-verify flags.

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
- Severe findings (KN8 rude, QT11 ignored customer, KT1 wrong info, live-store
  mistakes) → **flag in the summary for Liz to review individually**, never auto-send.
- **KB may be outdated.** If a CS's claim contradicts the KB, don't auto-blame —
  it may be the KB that's wrong (e.g. Joy Starter free-orders was 150 in KB but
  actually 250; team-member count differs between two KB files). Flag for Liz to
  verify the KB first.
- A finding must quote the chat as evidence. No evidence → don't report it.
- Score only the target CS's messages, not handoff colleagues'.

## Files

- Rubric: `playbooks/qa-weekly-rubric.md`
- Roster (CS → Slack ID): `_identity/team-g2.md`
- Scripts: `skills/qa-weekly/scripts/`
- Workflow: `skills/qa-weekly/qa-weekly.workflow.js`
- Output: `reports/qa-weekly/`
