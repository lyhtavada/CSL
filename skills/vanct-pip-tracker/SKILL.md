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

**Pass/fail bar (set 2026-08-15):** Criteria 1, 2, 4, 5, 6 (SLA, Ticket
Follow-up, Team Participation, Internal Communication, Check-in muộn) are
basic job requirements — must hit **100%, zero errors**, no partial credit.
Criteria 3 (DFY) and 7 (ONB) are flexible/lenient — Liz's read is these
depend on merchant situation, not purely on VanCT's effort.

The sheet has **one tab, "Overview"** — a flat table where each target is its
own row (grouped/merged by criterion), and 4 columns (Tuần 1–4) hold weekly
actuals. **7 criteria total; 4 of them have a data source** and are
auto-filled:

| Criterion | Source | Row(s) |
|---|---|---|
| SLA / Response Time | BigQuery `avada-crm.avada_cs.crisp_chats` | 6 (≤10p %), 7 (>30p count) |
| DFY Task Completion | Avada Ticket API `/api/external/tickets/by-date` | 9–12 (ticket count, one row per challenge week — only the matching week's row+column gets filled), 13 (avg % checklist tasks done per dueDateDone ticket), 14 (% tickets with a resolved follow-up tag) |
| ONB Task (flow mới) | Avada Ticket API, subject starts `[ONB]` | 20 |
| Check-in muộn | Admin API `/shifts` + `/shifts/:id/checks` | 18 (>10p count), 19 (>20p count, ~SS11b proxy) |

The other 3 (Ticket Follow-up row 8, Team Participation rows 15–16, Internal
Communication row 17) are **qualitative — Liz fills by hand**, no API/log
exists for "leader had to follow up" or "missed a Slack message".

Added 2026-08-14, after the team launched a new Joy onboarding flow: Liz
wants VanCT to create ≥1 `[ONB]` ticket/week for a new merchant (criterion
#7), plus deeper DFY tracking beyond the raw dueDateDone count — how much of
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
- **SLA metric** = time between a session's first `fromType='user'` message
  and VanCT's first `fromType='operator'` reply (`agentEmail = vanct@avadagroup.com`),
  for sessions where that first reply falls inside the week's window. It is a
  simplification — it does not account for cases where another CS also
  touched the same session.
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

- Script: `skills/vanct-pip-tracker/scripts/fill_weekly.py` — no LLM step,
  pure Python (BigQuery + REST + Sheets API), run directly via `.venv-crisp/bin/python`.
- Cron source: `skills/vanct-pip-tracker/cron/` (plist + `run-weekly.sh` + `install.sh`)
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
