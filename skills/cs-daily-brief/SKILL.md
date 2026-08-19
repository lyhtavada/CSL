---
name: cs-daily-brief
description: Daily CS report posted to #cs-2-daily — conversation volume per app (Joy/Chatty/Wishlist) for the previous 24h, Team G2 check-in/checkout (late/miss), AI-created tickets with no progress, and tickets created for Liz with a summary of what each is about — all over a rolling 08:30-to-08:30 window. Runs in exception mode: short on a quiet day, expands only for what needs Liz, full report in a thread.
---

# /cs-daily-brief

Runs each morning at **8:45**, reports on a rolling 24h window **08:30 VN the
previous day to 08:30 VN today** — e.g. running on the 22nd reports on the
window 21st 08:30 -> 22nd 08:30. The window is intentionally aligned to this
job's own run time (not midnight-midnight) so it ends just minutes before the
report is sent — minimal lag, vs. a midnight-aligned calendar day where
activity between 00:00-08:45 wouldn't surface until the *following* day's
report (changed 2026-07-31 per Liz's request). Posts one Slack message to the
**#cs-2-daily channel** (`C0B8042TXQ9`), sent with Liz's name/avatar
(live-fetched, matches the `/cs-weekly`+`/dfy-weekly-chatty` convention for
team-channel posts) — not a private DM. 4 sections. Evolved from the
original `/ticket-watch` (folded in conversation volume + attendance, then
moved from DM to team channel, then added tickets created for Liz); section
③ was originally a neglected/stale-ticket watch and was replaced 2026-07-31
with an AI-ticket section per Liz's request (assignee-based stale tracking
dropped in favor of "what did the bot actually resolve into a ticket").

## Exception mode (2026-08-11)

The brief used to print all 4 sections in full every morning. It now posts a
**short message** and expands only the sections that actually fired; the full
4-section report goes out as a **thread reply** under it, so nothing is lost
but the channel stays scannable. #cs-2-daily is Liz's own tracking channel,
not a team broadcast, so there is no team-visibility cost to shortening it.

Rules live in `cron/thresholds.json` (Liz edits it directly, no code change);
`scripts/evaluate.py` runs all 4 fetchers, applies them, and returns
`quiet` / `sanity` / `flags`. The fetchers stay pure data — every threshold is
in the JSON, every rule is in evaluate.py.

| Section | Fires when | Otherwise |
|---|---|---|
| ① Volume | never — always one line of numbers | (no baseline, no history needed) |
| ② Checkin | late **≥10 min**, miss checkin, or miss checkout | `✅ OK` |
| ③ AI ticket | `tsStatus` ∈ {pending, doing} **and** `dueDateDone is not True` | `✅ Không có` |
| ③b DFY chưa nhận | `tsStatus` = `done_for_you` **and** `memberIds` vẫn chỉ có `ai-agent-2` (chưa ai thật assign) | `✅ Không có` |
| ④ Ticket Liz | any ticket created for her | `Không có` |

**Why ① has no anomaly rule:** three of Liz's four rules are absolute, so only
volume would have needed a trailing baseline — and that meant a history file
plus a 14-day backfill for one soft signal. Dropped; volume is just shown.

**Sanity over silence.** The failure mode this design has to survive is a
broken pipeline looking exactly like a calm day. `evaluate.py` therefore
treats an all-zeros result (total conversations 0, or all three bots at 0
handled) as *suspected breakage*, forces `quiet=false`, and the message leads
with ⚠️ instead of reporting calm. A fetcher exiting non-zero aborts the run
with nothing sent.

**Tuning if ③ gets noisy:** widen the skip list or drop the `dueDateDone`
condition in `thresholds.json`. A 14-day probe put the rate at ~0.5
tickets/day, but that measured *current* status on old tickets; checked at
08:45 the morning after creation the real rate is higher, since tickets TS
hasn't picked up yet still sit in pending/doing. Expect to retune.

## Sections

**① Tổng quan conversation** — count of **real merchant conversations** per app
active in the window: Joy, Chatty, Wishlist + total. `scripts/fetch_conversations.py`,
BigQuery `avada-crm.avada_cs.crisp_chats`, app split via `APP_SEGMENTS` in
`skills/_shared/chat_count.py`. Uses `chat_count_window()` (the time-of-day-aware
sibling of `chat_count_active()`, added 2026-07-31 so this report's 08:30-08:30
window doesn't have to align to midnight like `/cs-weekly` + `/count-chats` do) —
same merchant-anchored / ≥2-msgs / internal-traffic-excluded filters, counting
conversations **active** in the window (≥1 merchant message in it, full
conversation may span outside it) rather than ones that *started* in it — the
right semantic for a daily activity pulse, and it avoids undercounting chats
that cross the window boundary. This means a single ongoing conversation can
legitimately be counted in 2 consecutive reports — expected, not a bug.

**② Checkin/checkout (Team G2)** — late (>5 min) checkins, missed checkins,
missed checkouts for the window. `scripts/fetch_checkin.py`, via
`shift_status()` in `scripts/_common.py` (Admin API `/shifts` +
`/shifts/:id/checks`, `$AVD_TOKEN`/`$AVD_API_BASE`, roster included in the
same file).

**③ Chat AI đã tạo ticket** — per app bot (Joyce/Joy, Ivy/Chatty,
Wendy/Wishlist): how many chats it handled in the window, and which of those
chats it turned into a ticket. `scripts/fetch_ai_tickets.py`, two sources
joined by app:
- **Handled count** — BigQuery `avada_cs.crisp_chats`: distinct sessions
  with an operator message in the window where `agentEmail IS NULL` (a bot
  message, not a human CS reply) and `userNickname` matches the bot's own
  Crisp display name. Confirmed live (2026-07-31) that nickname alone is an
  unambiguous per-app filter — Ivy only appears under `app_chatty` segments,
  Joyce under `app_joy`, Wendy under `app_wishlist` — so no segments join is
  needed.
- **AI-created tickets** — Ticket API `/tickets/by-date`: tickets created in
  the window whose `members[]` has an entry with `isCreate: true` and
  `memberId == "ai-agent-2"` (the same AI agent id is shared across all 3
  apps in the ticket system — it's the ticket's own `appName` that maps it
  back to Joyce/Ivy/Wendy for display, not a per-app bot identity in the
  ticket data). `by-date`'s `endDate` is exclusive (confirmed live
  2026-07-31 — a bug where same-day start/end silently returned zero rows),
  so the script queries a 1-day-widened superset and filters precisely on
  `createdAt` itself. Customer display name is `store[0].shopName` (fallback
  domain, then "Khách") since the Ticket API has no Crisp nickname field;
  the chat link comes straight from the ticket's own `chatLink`.

Like ①, ② and ④, this section is scoped to the window (not a live snapshot).

Since 2026-08-11 the fetcher also carries the ticket's **progress fields** so
`evaluate.py` can flag AI tickets nobody has moved. Three things were
confirmed against 486 live tickets and are easy to get wrong:

- **`dueDate` is a timestamp, not a flag** — present on every ticket and
  always exactly `createdAt + 2 days`, auto-set at creation. A "dueDate is
  false" filter can never fire. It carries no signal at all.
- **`dueDateDone` is the real completion flag**, and "not done" shows up as
  the key being **absent** (140/486), not as `False` (1/486). The test must be
  `is not True`.
- **`ticketStatus` is only open/closed** — the working state is `tsStatus`
  (waiting_customer, done, done_for_you, dev_done, dev_fixing, pending, doing,
  onb, sale_request, feature_request, customization, waiting_permission,
  billing).

Also from that probe: **all 75 AI-created tickets in 14 days were Chatty** —
Joyce and Wendy created none, so empty joy/wishlist blocks are real, not a
bug. Worth revisiting whether those two bots create tickets under a different
member id.

**③b (added 2026-08-19, Liz's request)** — a separate condition from ③,
checked on the same ticket data: `tsStatus == "done_for_you"` (the bot marked
the DFY setup itself complete) **and** `memberIds` is still exactly
`["ai-agent-2"]` — meaning no human CS/TS has ever been added to the ticket.
A bot-completed DFY ticket nobody picked up is invisible to ③ since
`done_for_you` isn't in `flagTsStatus`, so this catches it separately.
Example: `CHAT-260818-7p3UjQ`, flagged by Liz 2026-08-19. Toggle off via
`aiTickets.flagDfyUnassigned` in `thresholds.json`.

**④ Ticket tạo cho Liz trong ngày** — tickets created in the window where
Liz is a member (`scripts/fetch_liz_tickets.py`, matches any member whose
`displayName` contains "liz" case-insensitive — covers both "Liz" and
"liz_avada" seen live). Separate from ③: this is "what landed on her in the
window", not a staleness check.

Each one gets a **1-2 sentence Vietnamese summary** built from three sources
together: `subject`, the full `description` (now kept untruncated), and the
actual chat transcript via `scripts/fetch_chat_transcripts.py`. The transcript
matters most for `[DFY]` tickets, whose description is a generic checklist
template and says nothing case-specific.

## How it runs

```
python3 skills/cs-daily-brief/scripts/evaluate.py --date <target> --json > /tmp/cs_daily_eval.json
python3 skills/cs-daily-brief/scripts/fetch_chat_transcripts.py --from-json /tmp/cs_daily_eval.json --json
```
`evaluate.py` runs the 4 fetchers itself — one command instead of five, and
the sanity checks can't be skipped. Compose the short Vietnamese message (see
`cron/prompt.txt` for the exact three shapes: broken / quiet / có việc),
live-fetch Liz's name+avatar via `users.info`, send via
`../qa-weekly/scripts/send_dm.py` to channel `C0B8042TXQ9` with `--out` to
capture the message `ts`, then post the full report as a thread reply using
`thread_ts`. (`send_dm.py` gained optional `thread_ts` + `--out` for this;
both are backwards-compatible, so /qa-weekly, /cs-weekly and
/dfy-weekly-chatty are unaffected.)

The individual fetchers still run standalone with `--date <target> --json` if
you want to inspect one section by hand.

## Manual run

```
bash skills/cs-daily-brief/cron/run-cs-daily-brief.sh
```
To see the verdict without sending anything:
```
python3 skills/cs-daily-brief/scripts/evaluate.py --date <target>
```

## Cron

Daily 8:45 local (reports on the rolling 08:30-08:30 window) —
`cron/run-cs-daily-brief.sh`, installed via `cron/install.sh`.
