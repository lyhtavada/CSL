---
name: vanct-pip-tracker
description: Weekly auto-fill for VanCT's 1-month performance improvement tracker (Google Sheet). Pulls SLA/response time (BigQuery crisp_chats), DFY task completion + ONB tickets (Avada Ticket API), and check-in muộn (Admin shifts API) for the week that just ended and writes them into the "Overview" tab. Runs every Monday 11:00 via launchd.
version: 1.1.0
---

# VanCT PIP Tracker (Weekly)

Context: VanCT (Joy CS, in-house fulltime) is on a **4-week performance
challenge** (2026-08-17 → 2026-09-13, resumed trực từ 17/08 sau nghỉ 3 tuần)
following a team conversation about SLA, DFY completion, follow-up, team
participation, and internal communication issues, plus repeated late
check-ins. Tracker sheet:
https://docs.google.com/spreadsheets/d/1-KrG3RlFaSLDGKVJWWm3nK-Ow48lHuiwSUanBYlg_zI/edit

Row 2 ("Bối cảnh:") was deleted 2026-08-15 — Liz dropped the free-text
context blurb, keeping just row 1 (title) and the "Kỳ thử thách:" row before
the header row. **This shifted every row below up by 1** — if you're
resuming from an older version of this doc or a stale memory, the row
numbers below are the current ones; anything referencing the pre-2026-08-15
numbering is off by one.

**Pass/fail bar (set 2026-08-15, all in ONE merged cell, row 22 —
`Ngưỡng đạt/không đạt: ...`, referenced by criterion number only, no full
names):** Criteria **1, 3, 5, 6, 7** (SLA, Ticket Follow-up, Team
Participation, Internal Communication, Check-in muộn) are basic job
requirements — must hit **100%, zero errors**, no partial credit. Criteria
**4, 8** (DFY, ONB) are flexible/lenient — depend on merchant situation, not
purely on VanCT's effort. Criterion **2** (Product Knowledge) — a wrong
answer is serious and should trend to 0, but judge it with context (hard
case / new topic), not a strict pass/fail like the others.

The sheet has **one tab, "Overview"** — a flat table where each target is its
own row (grouped/merged by criterion), and 4 columns (Tuần 1–4) hold weekly
actuals. **8 criteria total; 5 of them have a data source** and are
auto-filled:

| # | Criterion | Source | Row(s) |
|---|---|---|---|
| 1 | SLA / Response Time | BigQuery `avada-crm.avada_cs.crisp_chats` | 5 (first-msg ≤2p %), 6 (ongoing-msg ≤10p %) |
| 2 | Product Knowledge | **LLM step** (headless Claude), reuses `/qa-weekly`'s Knowledge axis, verified against live Joy KB on cs2.avada.net | 7 |
| 4 | DFY Task Completion | Avada Ticket API `/api/external/tickets/by-date` | 9–12 (ticket count, one row per challenge week — only the matching week's row+column gets filled), 13 (avg % checklist tasks done per dueDateDone ticket, within the 48h SLA), 14 (% tickets with a follow-up tag) |
| 7 | Check-in muộn | Admin API `/shifts` + `/shifts/:id/checks` | 19 (single row since 2026-08-15 — the SS11b >20p breakout row was dropped; if late20 > 0 it's appended as a suffix inside the same cell text instead) |
| 8 | ONB Task (flow mới) | Avada Ticket API, subject starts `[ONB]` | 20 |

The other 3 (Ticket Follow-up row 8, Team Participation rows 15–17, Internal
Communication row 18) are **qualitative — Liz fills by hand**, no API/log
exists for "leader had to follow up" or "missed a Slack message". Team
Participation is 3 rows as of 2026-08-15: 100% meeting attendance, ≥1h
advance notice to leader if can't attend, and react/respond to relevant
announcements within 24h.

**Product Knowledge (criterion #2) is not a pure data pull** — it needs an
LLM to actually read VanCT's chat transcripts and judge whether what she
told merchants matches the live KB, so it can't live in `fill_weekly.py`.
It runs as a separate headless-Claude step (`prompt_knowledge_check.txt`),
reusing `skills/qa-weekly/scripts/fetch_sessions.py` +
`fetch_transcripts.py` + `fetch_kb.py` to pull VanCT's week and the relevant
Joy KB docs, then grading for factual errors only (not tone/process — those
are separate criteria) and writing the error count + a one-line note per
error straight into row 7 of the matching week's column. The sheet's target
cell text was shortened 2026-08-15 to just "0 lỗi kiến thức sai/tuần trong
chat" (dropped the "chấm bằng KB cs2.avada.net..." explainer as redundant
with this doc) — **the cron prompt still grades against the KB exactly as
before**, only the sheet's displayed target text got shorter.

Added 2026-08-14, after the team launched a new Joy onboarding flow: Liz
wants VanCT to create ≥1 `[ONB]` ticket/week for a new merchant (criterion
#8), plus deeper DFY tracking beyond the raw dueDateDone count — how much of
each ticket's checklist actually got done, and whether merchant follow-up
was closed out (tagged `DFY-adopted`/`DFY-no-adopt`) rather than left hanging
on `DFY-following-up`.

## Important caveats

- **Check-in muộn is NOT the same as the "Penalty log" (approved/disapproved)
  admin UI Liz showed via screenshot.** That page's backend
  (`/shifts/penalties` or similar) returned 401 with the current API token —
  no programmatic access found. This script instead computes lateness
  directly from raw check-in timestamps (`/shifts/:id/checks`), which is a
  reasonable proxy but will not exactly match the approved-only Penalty log
  count. The written value says "raw check-in, chưa qua duyệt penalty log" —
  Liz should still glance at the Penalty log for the official approved count
  before the end-of-challenge decision.
- **SLA target changed 2026-08-15**: now two separate bars — first message of
  a new case ≤**2 phút**, ongoing messages within an already-open case ≤**10
  phút**. `fetch_sla()` pulls every session where VanCT replied at least once
  in the window, walks the full user/operator message sequence per session,
  and for each user message finds the *next* operator reply — only counted
  if that reply is from VanCT (`agentEmail = vanct@avadagroup.com`) and lands
  inside the week's window. The session's 1st user message → "first message"
  bucket (target ≤2p); every later user message → "ongoing" bucket (target
  ≤10p). If a different CS replies first (handover), that gap isn't counted
  against VanCT. Doesn't distinguish message `type` (text vs note/event) —
  a directional metric, not exact.
- **DFY count** = tickets with `subject` starting `[DFY]`, `appName="JOY Loyalty"`,
  `dueDateDone=true`, creator=VanCT (`displayName` normalizes to `audrey`/`Audrey`),
  `tsStatus != "sale_request"`, created within the week's date range. Since
  `dueDate` = createdAt + 2 days, a ticket created right at the end of the
  week could in theory still flip to `dueDateDone=true` a day or two after
  the Monday run — a small lag, but the run happens a full week after the
  week started so almost all of it has already settled by then.
- **Follow-up target changed 2026-08-15**: `DFY-following-up` now also counts
  as "có tag rõ ràng" (not just `DFY-adopted`/`DFY-no-adopt`) — the bar is
  "has a tracked follow-up status at all", not "fully resolved".
- **DFY ticket-count target changed 2026-08-15**: flat numbers, not a
  ticket/week rate — Tuần 1: 2 ticket, Tuần 2–4: 3 ticket/tuần each.

## Weekly run (launchd)

Runs every **Monday at 11:00** local time (`com.avada.vanct-pip-tracker-weekly`),
reporting the **full week that just ended** (Mon→Sun) and writing it into
that week's column. The first run that produces data is the Monday right
after Tuần 1 ends (i.e. 2026-08-24, reporting 17–23/08) — running on
2026-08-17 itself has nothing to report yet and is a no-op.

`run-weekly.sh` does two steps:
1. `fill_weekly.py` — pure Python (BigQuery + REST + Sheets API), no LLM,
   fills SLA / DFY / ONB / check-in muộn.
2. `prompt_knowledge_check.txt` via headless `claude -p` — reads VanCT's
   chats for the week and grades Product Knowledge against the live KB
   (cs2.avada.net, same source `/qa-weekly` uses), writes directly to row 7.

- Cron source: `skills/vanct-pip-tracker/cron/` (plist + `run-weekly.sh` + `prompt_knowledge_check.txt` + `install.sh`)
- Install once (Liz runs in Terminal): `bash ~/CSL/skills/vanct-pip-tracker/cron/install.sh`
- Log: `/tmp/vanct-pip-tracker-weekly.log`
- After the challenge ends (2026-09-13), unload the job: `bash ~/CSL/skills/vanct-pip-tracker/cron/install.sh --remove`

## Manual run

```
.venv-crisp/bin/python skills/vanct-pip-tracker/scripts/fill_weekly.py
```

Auto-detects the current week from today's date against the fixed WEEKS list
in the script; does nothing (prints a message) if today is outside
2026-08-17 → 2026-09-13.
