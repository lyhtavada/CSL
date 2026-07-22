---
name: cs-daily-brief
description: Daily CS report DM'd to Liz — conversation volume per app (Joy/Chatty/Wishlist) for the previous full day, Team G2 check-in/checkout (late/miss), and neglected-ticket watch (stale/DFY-stuck, VIP, per-CS breakdown).
---

# /cs-daily-brief

Runs each morning, reports on the **previous full calendar day** (00:00–24:00
VN) — e.g. running on the 22nd reports on the 21st. Sends one Slack DM to
Liz with 3 sections. Evolved from the original `/ticket-watch` (now section
③) after Liz asked to fold in conversation volume + attendance.

## Sections

**① Tổng quan conversation** — count of Crisp conversations per app for the
target day: Joy, Chatty, Wishlist + total. `scripts/fetch_conversations.py`,
BigQuery `avada-crm.avada_cs.crisp_chats`, app split by `segments` LIKE
`%app_joy%` / `%app_chatty%`|`%app_faqs%` / `%app_wishlist%`.

**② Checkin/checkout (Team G2)** — late (>5 min) checkins, missed checkins,
missed checkouts for the target day. `scripts/fetch_checkin.py`, reuses
`shift_status()` from `../cs-daily/lib/render.py` (Admin API `/shifts` +
`/shifts/:id/checks`, `$AVD_TOKEN`/`$AVD_API_BASE`, roster in
`../cs-daily/lib/common.py`) — not duplicated.

**③ Ticket watch** — neglected open tickets across all 3 apps, unchanged from
the original `/ticket-watch` design. `scripts/fetch_stale.py`:
- `stale_no_update`: regular ticket (excludes `[DFY]`/`[ONB]`), open ≥1 day,
  no update since created OR still `tsStatus=pending`/unclaimed.
- `dfy_stuck`: `[DFY]`/`[ONB]` ticket, open ≥2 days, incomplete `tasks[]`
  item with no update since.
- Day-over-day dedup via `state/seen.json` — new tickets shown in full,
  carryover backlog just counted.
- VIP tickets (`isVip` — `appPlan` not free/basic) always listed in full.
- `assigneeBreakdown` — top 8 CS by count of currently flagged tickets
  (bot members excluded).

This section is a live snapshot ("tickets currently neglected as of now"),
not bound to the target day like ① and ② are.

## How it runs

```
python3 skills/cs-daily-brief/scripts/fetch_conversations.py --date <target> --json
python3 skills/cs-daily-brief/scripts/fetch_checkin.py --date <target> --json
python3 skills/cs-daily-brief/scripts/fetch_stale.py --json
```
Compose one Vietnamese Slack message (see `cron/prompt.txt` for exact shape),
send via `../qa-weekly/scripts/send_dm.py` to Liz's Slack id `U02GT4PC6RH`.

## Manual run

```
bash skills/cs-daily-brief/cron/run-cs-daily-brief.sh
```
or run the 3 fetch scripts individually and compose by hand.

## Cron

Daily 10:00 local (reports on the previous full day) —
`cron/run-cs-daily-brief.sh`, installed via `cron/install.sh`.
