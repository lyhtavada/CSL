---
name: cs-weekly
description: Generate the weekly CS bulletin for the CS team of an app (Chatty or Joy) to read and stay on top of the week. Period = Monday→Sunday of LAST week. Pulls tickets created (Ticket API), chats (BigQuery crisp_chats), DFY created, and App Store reviews (Shopify, sort_by=newest), then clusters top issues from chats, scans the #product-release Slack channel for releases in the period, and writes a team-facing report. Coaching + recognition sections are left for Liz to fill/review. Use when Liz says "/cs-weekly", "CS weekly", "report tuần cho team", or it runs via cron Mon 9AM.
version: 1.0.0
---

# CS Weekly Skill

Generate a **team-facing weekly bulletin** for the CS team of one app, so agents can read 2 minutes and know the week's situation + what to watch when supporting merchants.

This is DIFFERENT from:
- `/weekly` — internal G2 leadership report for the Monday meeting.
- `/dfy-weekly` — DFY ticket monitoring only.

## Trigger

When Liz says `/cs-weekly`, "CS weekly", "report tuần cho team CS", or via cron (Mon 9AM).

## Parameters

- **App:** `chatty` or `joy`. If Liz doesn't specify, generate **both**.
- **Period:** default = **Monday → Sunday of LAST week** (the week that just ended).
  - Compute from today: last Sunday = most recent Sunday before today; Monday = that Sunday − 6 days.
  - e.g. run on Mon 2026-06-10 → period 2026-06-01 (Mon) → 2026-06-07 (Sun).
  - Liz may pass an explicit range.

## Steps

### 1. Determine period (Mon→Sun of last week)

Compute `start` (Monday) and `end` (Sunday) as YYYY-MM-DD. Note the ISO week of the
Sunday end date for the filename (`W##`).

### 2. Pull metrics (per app)

```bash
python3 skills/cs-weekly/scripts/fetch_metrics.py --app {chatty|joy} --start {start} --end {end} --json
```
Returns `tickets_created`, `dfy_created`, `chats`. Sources: Ticket API
(`AVD_TICKET_API_KEY`), BigQuery `avada_cs.crisp_chats` (Chatty = segments
`app_chatty,app_faqs`; Joy = `app_joy`).

### 3. Pull App Store reviews (per app)

```bash
python3 skills/cs-weekly/scripts/fetch_reviews.py --slug {joyio|chatty} --start {start} --end {end} --json
```
Slugs: Joy = `joyio`, Chatty = `chatty`. Returns `count`, `avg`, `distribution`,
`low_reviews` (≤3★ — call these out in the report). The script uses
`?sort_by=newest&page=N` and takes the FIRST date/rating per block — do NOT change
this (see the script header for the 3 bugs this avoids).

### 4. Cluster top issues from chats

Fetch the period's chats and read the first customer message per session:
```bash
python3 skills/mine-chat-faqs/scripts/fetch_chats.py --segment {app_chatty,app_faqs | app_joy} --days {N} --output /tmp/{app}_week.json
```
`fetch_chats.py` only takes `--days` (look-back from today), so pass enough days to
cover the period, then read the JSON. Cluster the asks into 3-5 themes, rank by
volume, and for each give a 1-line "cách xử lý" + KB pointer. Flag any bug merchants
report repeatedly (→ Known bugs in §4 of the report).

### 5. Scan #product-release for releases in the period

Read Slack channel `C07RNAY9ZC6` for messages within [start, end]. **Use token
`SLACK_BOT_TOKEN_AVADA`** (other bot tokens get `not_in_channel`):
```python
requests.get("https://slack.com/api/conversations.history",
  headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN_AVADA}"},
  params={"channel":"C07RNAY9ZC6","oldest":<start ts>,"latest":<end+1 ts>,"limit":50})
```
Keep only releases relevant to the report's app. For each, get a permalink via
`chat.getPermalink` and link it. If none → omit the release sub-block. Write 1 line
per release on what it means for support ("when merchant asks X → now they can Y").

### 6. Write the report

Use `reports/weekly-cs/TEMPLATE.md`. Fill §1–4 + §6-win from data. Leave §5 (Coaching)
and the Shoutout/Focus lines for Liz to review — these need her judgment; write
`_(Liz điền)_` placeholders, but you MAY pre-fill a process reminder if a repeated
bug/issue warrants it.

Save to:
- Chatty: `reports/weekly-cs/chatty/chatty-cs-weekly-{YYYY-W##}.md`
- Joy:    `reports/weekly-cs/joy/joy-cs-weekly-{YYYY-W##}.md`

Keep it ~1 screen. Hide any sub-block with nothing new.

### 7. Commit

`git add` the report(s) and commit: `cs-weekly: auto report {YYYY-W##}`.
Print the saved path(s) + the headline numbers.

## Report sections (TEMPLATE.md)

1. **TL;DR** — 2-3 sentences from the data.
2. **📊 Tình hình support** — table: tickets / chats / DFY / reviews, vs last week (▲▼).
   Last week's baseline: read the previous week's report file if it exists.
3. **🔥 Top issues** — 3-5 themes from chats, each with a fix/KB pointer.
4. **🆕 Cập nhật sản phẩm & policy** — releases from #product-release + known bugs open.
5. **💡 Coaching & lưu ý** — Liz reviews/fills.
6. **🌟 Ghi nhận & tinh thần** — win (auto, e.g. review streak) + Liz's shoutout/focus.

## Notes / gotchas

- **Period is Mon→Sun of LAST week**, not a rolling 7-day window.
- **Reviews:** ALWAYS `sort_by=newest`. App Store's default page order is NOT by
  date, so any early-stop on a non-sorted feed silently drops reviews.
- **Slack release channel** `C07RNAY9ZC6` only opens with `SLACK_BOT_TOKEN_AVADA`.
- Chatty has no DFY program yet → `dfy_created` is 0; keep the row but it's expected.
- This is team-facing: tone clear and encouraging, language Vietnamese (per workspace
  default for internal team content), short.
