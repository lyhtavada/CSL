---
name: vanct-pip-tracker
description: Weekly auto-fill for VanCT's 1-month performance improvement tracker (Google Sheet). Pulls SLA/response time (BigQuery crisp_chats), DFY task completion (Avada Ticket API), and check-in muộn (Admin shifts API) for the current challenge week and writes them into the "Overview" tab. Runs every Friday 09:00 via launchd.
version: 1.0.0
---

# VanCT PIP Tracker (Weekly)

Context: VanCT (Joy CS, in-house fulltime) is on a **4-week performance
challenge** (2026-08-17 → 2026-09-13, resumed trực từ 17/08 sau nghỉ 3 tuần)
following a team conversation about SLA, DFY completion, follow-up, team
participation, and internal communication issues, plus repeated late
check-ins. Tracker sheet:
https://docs.google.com/spreadsheets/d/1-KrG3RlFaSLDGKVJWWm3nK-Ow48lHuiwSUanBYlg_zI/edit

The sheet has **one tab, "Overview"** — a flat table where each target is its
own row (grouped/merged by criterion), and 4 columns (Tuần 1–4) hold weekly
actuals. Only **3 of the 6 criteria have a data source** and are auto-filled:

| Criterion | Source | Row(s) |
|---|---|---|
| SLA / Response Time | BigQuery `avada-crm.avada_cs.crisp_chats` | 6 (≤10p %), 7 (>30p count) |
| DFY Task Completion | Avada Ticket API `/api/external/tickets/by-date` | 9–12 (one row per challenge week — only the matching week's row+column gets filled) |
| Check-in muộn | Admin API `/shifts` + `/shifts/:id/checks` | 16 (>10p count), 17 (>20p count, ~SS11b proxy) |

The other 3 (Ticket Follow-up row 8, Team Participation rows 13–14, Internal
Communication row 15) are **qualitative — Liz fills by hand**, no API/log
exists for "leader had to follow up" or "missed a Slack message".

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
  `dueDate` = createdAt + 2 days, a ticket created right before the Friday
  run may not show `dueDateDone=true` yet even if VanCT is on track — this is
  a rolling/partial-week snapshot, not a final count until the week is over.

## Weekly run (launchd)

Runs every **Friday at 09:00** local time (`com.avada.vanct-pip-tracker-weekly`),
computing metrics for **Monday of the current challenge week through the run
time** (a partial-week snapshot, since Friday morning is before the week ends
Sunday) and writing them into that week's column.

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
