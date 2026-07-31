---
name: cs-daily-brief
description: Daily CS report posted to #cs-2-daily — conversation volume per app (Joy/Chatty/Wishlist) for the previous full day, Team G2 check-in/checkout (late/miss), chats the app AI bot (Joyce/Ivy/Wendy) took that day and which ones it turned into a ticket, and tickets created for Liz that day.
---

# /cs-daily-brief

Runs each morning at **8:45**, reports on the **previous full calendar day** (00:00–24:00
VN) — e.g. running on the 22nd reports on the 21st. Posts one Slack message
to the **#cs-2-daily channel** (`C0B8042TXQ9`), sent with Liz's name/avatar
(live-fetched, matches the `/cs-weekly`+`/dfy-monthly` convention for
team-channel posts) — not a private DM. 4 sections. Evolved from the
original `/ticket-watch` (folded in conversation volume + attendance, then
moved from DM to team channel, then added tickets created for Liz); section
③ was originally a neglected/stale-ticket watch and was replaced 2026-07-31
with an AI-ticket section per Liz's request (assignee-based stale tracking
dropped in favor of "what did the bot actually resolve into a ticket").

## Sections

**① Tổng quan conversation** — count of **real merchant conversations** per app
active on the target day: Joy, Chatty, Wishlist + total. `scripts/fetch_conversations.py`,
BigQuery `avada-crm.avada_cs.crisp_chats`, app split via `APP_SEGMENTS` in
`skills/_shared/chat_count.py`. Uses `chat_count_active()` (not `chat_count()`) —
same merchant-anchored / ≥2-msgs / internal-traffic-excluded filters as
`/cs-weekly` + `/count-chats`, but counts conversations **active** that day
(≥1 merchant message that day, full conversation may span into adjacent days)
rather than ones that *started* that day — the right semantic for a daily
activity pulse, and it avoids undercounting chats that cross midnight. This
means a single ongoing conversation can legitimately be counted on 2
consecutive days — expected, not a bug.

**② Checkin/checkout (Team G2)** — late (>5 min) checkins, missed checkins,
missed checkouts for the target day. `scripts/fetch_checkin.py`, via
`shift_status()` in `scripts/_common.py` (Admin API `/shifts` +
`/shifts/:id/checks`, `$AVD_TOKEN`/`$AVD_API_BASE`, roster included in the
same file).

**③ Chat AI đã tạo ticket** — per app bot (Joyce/Joy, Ivy/Chatty,
Wendy/Wishlist): how many chats it handled that day, and which of those
chats it turned into a ticket. `scripts/fetch_ai_tickets.py`, two sources
joined by app:
- **Handled count** — BigQuery `avada_cs.crisp_chats`: distinct sessions
  with an operator message that day where `agentEmail IS NULL` (a bot
  message, not a human CS reply) and `userNickname` matches the bot's own
  Crisp display name. Confirmed live (2026-07-31) that nickname alone is an
  unambiguous per-app filter — Ivy only appears under `app_chatty` segments,
  Joyce under `app_joy`, Wendy under `app_wishlist` — so no segments join is
  needed.
- **AI-created tickets** — Ticket API `/tickets/by-date`: tickets created
  that day whose `members[]` has an entry with `isCreate: true` and
  `memberId == "ai-agent-2"` (the same AI agent id is shared across all 3
  apps in the ticket system — it's the ticket's own `appName` that maps it
  back to Joyce/Ivy/Wendy for display, not a per-app bot identity in the
  ticket data). Customer display name is `store[0].shopName` (fallback
  domain, then "Khách") since the Ticket API has no Crisp nickname field;
  the chat link comes straight from the ticket's own `chatLink`.

Like ①, ② and ④, this section is scoped to the target day (not a live
snapshot).

**④ Ticket tạo cho Liz trong ngày** — tickets created on the target day where
Liz is a member (`scripts/fetch_liz_tickets.py`, matches any member whose
`displayName` contains "liz" case-insensitive — covers both "Liz" and
"liz_avada" seen live). Separate from ③: this is "what landed on her that
day", not a staleness check.

## How it runs

```
python3 skills/cs-daily-brief/scripts/fetch_conversations.py --date <target> --json
python3 skills/cs-daily-brief/scripts/fetch_checkin.py --date <target> --json
python3 skills/cs-daily-brief/scripts/fetch_ai_tickets.py --date <target> --json
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

Daily 8:45 local (reports on the previous full day) —
`cron/run-cs-daily-brief.sh`, installed via `cron/install.sh`.
