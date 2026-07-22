---
name: cs-daily-brief
description: Daily CS report posted to #cs-2-daily — conversation volume per app (Joy/Chatty/Wishlist) for the previous full day, Team G2 check-in/checkout (late/miss), neglected-ticket watch (stale/DFY-stuck, VIP, per-CS breakdown), and tickets created for Liz that day.
---

# /cs-daily-brief

Runs each morning, reports on the **previous full calendar day** (00:00–24:00
VN) — e.g. running on the 22nd reports on the 21st. Posts one Slack message
to the **#cs-2-daily channel** (`C0B8042TXQ9`), sent with Liz's name/avatar
(live-fetched, matches the `/cs-weekly`+`/dfy-monthly` convention for
team-channel posts) — not a private DM. 4 sections. Evolved from the
original `/ticket-watch` (now section ③) after Liz asked to fold in
conversation volume + attendance, then to post to the team channel instead
of DM'ing her, then to add tickets created for her.

## Sections

**① Tổng quan conversation** — count of Crisp conversations per app for the
target day: Joy, Chatty, Wishlist + total. `scripts/fetch_conversations.py`,
BigQuery `avada-crm.avada_cs.crisp_chats`, app split by `segments` LIKE
`%app_joy%` / `%app_chatty%`|`%app_faqs%` / `%app_wishlist%`.

**② Checkin/checkout (Team G2)** — late (>5 min) checkins, missed checkins,
missed checkouts for the target day. `scripts/fetch_checkin.py`, via
`shift_status()` in `scripts/_common.py` (Admin API `/shifts` +
`/shifts/:id/checks`, `$AVD_TOKEN`/`$AVD_API_BASE`, roster included in the
same file).

**③ Ticket watch** — neglected open tickets across all 3 apps, unchanged from
the original `/ticket-watch` design. `scripts/fetch_stale.py`:
- Skipped entirely if `dueDateDone` is true or `tsStatus=="done"` — the
  "Done" checkmark on the ticket header, which can be true while
  `ticketStatus` itself still says "open" (API lag; confirmed on a real
  ticket Liz flagged as a false positive).
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
not bound to the target day like ①, ② and ④ are.

**④ Ticket tạo cho Liz trong ngày** — tickets created on the target day where
Liz is a member (`scripts/fetch_liz_tickets.py`, matches any member whose
`displayName` contains "liz" case-insensitive — covers both "Liz" and
"liz_avada" seen live). Separate from ③: this is "what landed on her that
day", not a staleness check.

## How it runs

```
python3 skills/cs-daily-brief/scripts/fetch_conversations.py --date <target> --json
python3 skills/cs-daily-brief/scripts/fetch_checkin.py --date <target> --json
python3 skills/cs-daily-brief/scripts/fetch_stale.py --json
python3 skills/cs-daily-brief/scripts/fetch_liz_tickets.py --date <target> --json
```
Compose one Vietnamese Slack message (see `cron/prompt.txt` for exact shape),
live-fetch Liz's name/avatar via `users.info`, then send via
`../qa-weekly/scripts/send_dm.py` targeting channel `C0B8042TXQ9`
(`chat.postMessage`'s `channel` field takes a channel ID the same way it
takes a user ID — same script, no code change) with the `sender` override.

## Manual run

```
bash skills/cs-daily-brief/cron/run-cs-daily-brief.sh
```
or run the 3 fetch scripts individually and compose by hand.

## Cron

Daily 10:00 local (reports on the previous full day) —
`cron/run-cs-daily-brief.sh`, installed via `cron/install.sh`.
