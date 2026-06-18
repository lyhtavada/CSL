---
name: cs-weekly
description: Generate the weekly CS bulletin for the CS team of an app (Chatty or Joy) to read and stay on top of the week. Period = Monday→Sunday of LAST week. Pulls tickets created (Ticket API), chats (BigQuery crisp_chats), DFY created, and App Store reviews (Shopify, sort_by=newest) — each compared vs the prior week — then clusters top issues from tickets (Ticket API, [dfy] excluded), scans the #product-release Slack channel for releases, publishes a team-facing report as a new sub-page at the TOP of the app's Notion page (title includes the date range), and posts a TL;DR digest (as Liz, with a Notion button) to the app's CS Slack channel. Coaching + recognition sections are left for Liz to fill/review. Use when Liz says "/cs-weekly", "CS weekly", "report tuần cho team", or it runs via cron Mon 9AM.
version: 1.4.0
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
Sunday end date (`W##`) — used in the Notion sub-page title and the temp filename.

### 2. Pull metrics (per app) — with `--compare` for ▲▼

```bash
python3 skills/cs-weekly/scripts/fetch_metrics.py --app {chatty|joy} --start {start} --end {end} --compare --json
```
`--compare` returns BOTH `this_week` and `prev_week` (the prior Mon→Sun window) so you
can compute ▲▼ for §2 — **the comparison data is re-pulled live from source, not read
from an old file** (reports live in Notion only). Each block has `tickets_created`,
`dfy_created`, `chats`. Sources: Ticket API (`AVD_TICKET_API_KEY`), BigQuery
`avada_cs.crisp_chats` (Chatty = segments `app_chatty,app_faqs`; Joy = `app_joy`).

**`chats` = conversations, sessionized — NOT DISTINCT session_id.** Crisp keeps one
session_id per visitor forever, so a merchant returning across the week stays one
session_id; counting distinct sessions under-counts real volume (~40% low on Chatty,
~70% on Joy in a sample week). The script splits a session_id into a new conversation
whenever there's a silence gap ≥ `GAP_HOURS` (default **6h**, set in `fetch_metrics.py`).
6h = long enough not to split a chat still awaiting a reply, short enough to catch a
genuine return. Retune via `GAP_HOURS` if needed.

### 3. Pull App Store reviews (per app) — with `--compare`

```bash
python3 skills/cs-weekly/scripts/fetch_reviews.py --slug {joyio|chatty} --start {start} --end {end} --compare --json
```
`--compare` returns `this_week` + `prev_week`. Slugs: Joy = `joyio`, Chatty = `chatty`.
Each block has `count`, `avg`, `distribution`, `low_reviews` (≤3★ — call these out).
The script uses `?sort_by=newest&page=N` and takes the FIRST date/rating per block —
do NOT change this (see the script header for the 3 bugs this avoids).

### 4. Cluster top issues from tickets

Top issues come from **tickets** (Ticket API), NOT chats. Run for EACH app (chatty + joy):
```bash
python3 skills/cs-weekly/scripts/fetch_tickets.py --app {chatty|joy} --start {start} --end {end} --json
```
Returns each ticket's `subject` + `description` + `priority` + `status` for the period.
`[dfy]` tickets are **excluded by default** (they have their own row in §2 and aren't
support issues) — pass `--include-dfy` only if Liz wants them counted.

Read the subjects + descriptions, cluster the asks into 3-5 themes, rank by volume,
and for each give a 1-line "cách xử lý" + KB pointer. The `[bug]` subject prefix marks
bug reports — flag any bug reported repeatedly (→ Known bugs in §4 of the report).

(Chat volume is still pulled in §2 as a metric via `fetch_metrics.py` — only the
top-issue clustering moved from chats to tickets.)

### 4b. Pull Bot performance metrics (Joyce/Joy + Ivy/Chatty)

Hiệu quả của AI bot tuần qua — **Handle** (vận hành: bot xử được bao nhiêu) +
**QA** (chất lượng: human CS verify/correct). Từ "chỉ số vận hành" dashboard on
`cs2.avada.net`. Run for EACH app, **with `--compare`** (tự pull tuần trước cho ▲▼):
```bash
python3 skills/cs-weekly/scripts/fetch_bot_qa.py {chatty|joy} {start} {end} --compare > /tmp/{app}-botqa-{YYYY-W##}.json
```
Returns `handle`, `qa`, and (with `--compare`) `prevWeek` (same shape, prior Mon→Sun):
- **`handle`** — pulled live from `GET /api/obs/metrics?agent=<id>&from=&to=` (same
  numbers as the dashboard cards):
  - `resolveRatePct` = **% session bot tự xử, human KHÔNG nhảy vào** =
    `(sessions.total − sessions.human_active)/total` (cách A, Liz chốt 2026-06-18). Số chủ đạo.
  - `aiReplyCoveragePct` / `humanTakeoverPct` / `escalationRatePct` — bổ trợ (lấy thẳng từ kpi).
  - `sessions` / `inbound` / `botReplies` — volume.
- **`qa`** — `verifyCoveragePct` / `correctionRatePct` /
  `verifiedInWeek` / `correctionsInWeek` / `botReplies`, plus `topVerifiers` /
  `topCorrectors` = **top 3 of THIS WEEK** (lọc `created_at`): verifiers từ
  `/api/reviews` (parse `note` "Verified by X"), correctors từ `/api/corrections`
  (`created_by` email). Emails → display names via `_identity/team-g2.md`.

Agent ids: Chatty = `chatty-agent` (bot **Ivy**), Joy = `joy-loyalty-agent` (bot
**Joyce**). Auth: `CS2_API_URL` + `CS2_API_TOKEN` from `.env`.

Fill the report's **🤖 Bot performance section** (right after TL;DR) — Handle table +
QA table, mỗi metric có cột tuần trước (▲▼) từ `prevWeek`. **If `qa.verifyCoveragePct`
< 30%** → add the ⚠️ "verify coverage thấp" line. If a top-list is empty →
`_(chưa có lượt nào tuần này)_`.

### 4c. Pull TS Elite usage (team G2 dùng agent investigate ntn)

**TS Elite** (`agent.avada-ts.site`) = agent CS dùng để investigate case. Mỗi "chat" =
1 cuộc CS hỏi agent. Report cho team G2 thấy **ai dùng nhiều / ít, ai chưa dùng, và
những câu hay được hỏi**. Run for EACH app, **with `--compare`**:
```bash
python3 skills/cs-weekly/scripts/fetch_ts_elite.py {chatty|joy} {start} {end} --compare > /tmp/{app}-tselite-{YYYY-W##}.json
```
Source: `GET /api/v1/chats?from=&to=&app=&page=` (auth `X-API-Key: TS_ELITE_API_KEY`
from `.env`). `from`/`to` lọc theo `createdAt` (inclusive), `app` lọc theo slug
(Joy gộp cả `joy-subscriptions`). Chỉ tính CS thuộc **team G2** (`_user` = local-part
email, map từ `_identity/team-g2.md`), CSL (Liz) loại. Returns:
- **`totalChatsG2`** / `activeCount` / `memberCount` — volume + bao nhiêu CS active.
- **`top`** (5 dùng nhiều nhất) / **`least`** (3 active ít nhất, vẫn >0) /
  **`inactive`** (CS G2 **chưa dùng lần nào** tuần này — flag để Liz nhắc onboard).
- **`questions`** — list nguyên văn `title` mọi chat G2 (= câu hỏi mở đầu). **Đọc và
  cluster thành 3-5 chủ đề hay hỏi nhất** (gộp các "investigate Crisp chat: <url>" =
  1 nhóm "tra cứu Crisp", "check ticket" = 1 nhóm…). Bỏ URL trần khi hiển thị.
- **`prevWeek`** (`--compare`) — `totalChatsG2` + `activeCount` tuần trước cho ▲▼.

Fill the report's **🛠 TS Elite usage section** (sau Top issues). Top table + ai chưa
dùng + 3-5 câu/chủ đề hay hỏi. **If `inactive` không rỗng** → liệt kê tên, gợi ý Liz
nhắc. Nếu `totalChatsG2` = 0 (cả team chưa đụng) → ẩn section, ghi 1 dòng TL;DR.

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

### 5b. Low reviews (≤3★) → link the bad-review thread

ONLY if step 3 found a review **≤3★** in the period. The Slack group `G019ZF7GM7H` is an
auto-feed of reviews that need attention (one message per review: `[App name] Review
by {store} published {date} ...`). For each low review:
```python
requests.get("https://slack.com/api/conversations.history",
  headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN_AVADA}"},  # same token as release channel
  params={"channel":"G019ZF7GM7H","oldest":<start ts>,"latest":<end+2d ts>,"limit":100})
```
Match a message by **app name in the `[...]` prefix + the published date ≈ the review
date** (feed posts may lag the review by a day → widen the window a couple days).
On match → `chat.getPermalink` and attach the thread link next to that review in the
report's §2 "⚠️ Review cần lưu ý" line. If no match (the feed doesn't carry every review, only
flagged ones) → keep the review note but say `_(không thấy trong feed bad-review)_`,
do NOT fabricate a link. 4★ and above do NOT trigger this scan.

### 6. Write the report

Use `reports/weekly-cs/TEMPLATE.md`. Fill the report's §1–4 + the §6-win from data.
Leave the report's §5 (Coaching) and the Shoutout/Focus lines for Liz to review —
these need her judgment; write `_(Liz điền)_` placeholders, but you MAY pre-fill a
process reminder if a repeated bug/issue warrants it.

**Do NOT add an H1 title / Period line / intro quote at the top** — the Notion
sub-page title already carries app + week + date range. The body starts straight at
`## ⚡ TL;DR` (the template already omits these; `push_notion.py` also strips any
leading H1/Period block as a safety net).

Write the filled report to a TEMP file (not committed to the repo — reports live in
Notion only):
- Chatty: `/tmp/chatty-cs-weekly-{YYYY-W##}.md`
- Joy:    `/tmp/joy-cs-weekly-{YYYY-W##}.md`

Keep it ~1 screen. Hide any sub-block with nothing new.

### 7. Push to Notion (one sub-page per week)

Each report becomes a NEW sub-page under the app's parent Notion page:
```bash
python3 skills/cs-weekly/scripts/push_notion.py \
  --parent {PARENT_PAGE_ID} \
  --title "{App} CS Weekly — W## ({DD–DD/MM/YYYY})" \
  --md /tmp/{app}-cs-weekly-{YYYY-W##}.md
```
- **Parent page IDs** (Notion integration already shared with these pages):
  - Chatty: `37bb0da449f180729d79fcfc6d43c35a` ("Chatty CS Weekly")
  - Joy:    `37bb0da449f18054b553c00929e711cb` ("Joy CS Weekly")
- **Title MUST include the date range** (Liz's rule), format:
  `Chatty CS Weekly — W23 (01–07/06/2026)`.
- **New sub-page lands at the TOP** of the parent (the script sends
  `position: page_start`) so the newest report is always first — no scrolling down
  as reports accumulate.
- Auth: `NOTION_API_KEY` from `.env`. The script parses the markdown into Notion
  blocks (headings, table, lists, quote, divider, inline bold/italic/code/links),
  strips any redundant leading H1/Period header, and prints the new page URL.

The script prints the new page URL — capture it for step 8.

### 8. Notify the CS Slack channel (after Notion push)

For each app, post a digest to its CS channel via the Avada bot: the TL;DR + a button
to the Notion report.
```bash
python3 skills/cs-weekly/scripts/notify_slack.py \
  --channel {CHANNEL_ID} \
  --title "{App} CS Weekly — W## ({DD–DD/MM/YYYY})" \
  --tldr "{the §1 TL;DR text from the report}" \
  --botqa-file /tmp/{app}-botqa-{YYYY-W##}.json \
  --notion-url {the URL printed by push_notion.py in step 7}
```
- **`--botqa-file`** (the JSON from step 4b) adds a "🤖 Bot performance tuần này" block
  to the Slack digest — Handle (resolve rate + AI coverage + human takeover +
  escalation + volume, with ▲▼ vs last week) + QA (verify coverage / correction rate /
  + top verify + top correction), ⚠️ flag if verify coverage < 30%.
- **CS channel IDs:**
  - Chatty: `C07LZNWEUUD`   (`chatty-cs`)
  - Joy:    `C07MSUX0VPA`   (`joy-faqs`)
- Auth: `SLACK_BOT_TOKEN_AVADA` (bot = `avada_bot`). The bot must be a member of the
  channel — if posting fails with `not_in_channel`, invite `@avada_bot` there once.
  (Both channels already have the bot.)
- **Posts AS LIZ** — `--as-user` is ON by default: the script live-fetches Liz's
  profile (`U02GT4PC6RH`) and posts with her name + avatar. Slack still shows a small
  "APP" tag (unavoidable with a bot token). Pass `--no-as-user` to post as plain bot.
- The title should match the Notion sub-page title (app + week + date range).
- Sends Block Kit: header + TL;DR + "📄 Xem full trên Notion" button.
- To preview layout safely, post to Liz's DM: `--channel U02GT4PC6RH`.

Print the Notion page URL(s), the Slack post confirmation, and the headline numbers
(tickets / chats / DFY / reviews) for each app. Do NOT commit anything to git — there
is no .md file in the repo.

## Report sections (TEMPLATE.md)

1. **TL;DR** — 2-3 sentences from the data: lead with the §2 numbers + the hottest
   ticket-based theme/bug of the week. Do NOT phrase it as "merchant vào hỏi…" (that's
   the old chat framing) — chat is only a count metric now.
1b. **🤖 Bot performance** (right after TL;DR) — **Handle** (resolve rate + AI coverage
   + human takeover + escalation + volume) and **QA** (verify coverage / correction
   rate + top 3 verify + top 3 correction), each vs last week (▲▼). From
   step 4b's JSON (`--compare`). ⚠️ flag if verify coverage < 30%. This whole block also
   goes into the Slack digest.
2. **📊 Tình hình support** — table: tickets / chats / DFY / reviews, vs last week (▲▼).
   Get "tuần trước" from the `--compare` flag's `prev_week` block (re-pulled live from
   source) — there is no .md file in the repo to read. Show ▲▼ % for tickets/chats,
   ▲▼ count for reviews.
3. **🔥 Top issues** — 3-5 themes from tickets (Ticket API, `[dfy]` excluded), each with a fix/KB pointer.
4. **🆕 Cập nhật sản phẩm & policy** — releases from #product-release + known bugs open.
5. **💡 Coaching & lưu ý** — Liz reviews/fills.
6. **🌟 Ghi nhận & tinh thần** — win (auto, e.g. review streak) + Liz's shoutout/focus.

## Notes / gotchas

- **Period is Mon→Sun of LAST week**, not a rolling 7-day window.
- **Reviews:** ALWAYS `sort_by=newest`. App Store's default page order is NOT by
  date, so any early-stop on a non-sorted feed silently drops reviews.
- **Slack channels** both open ONLY with `SLACK_BOT_TOKEN_AVADA`:
  release feed `C07RNAY9ZC6` (§5) and bad-review feed `G019ZF7GM7H` (§5b).
- **Bad-review scan triggers only for ≤3★** (Liz's rule). The feed is sparse
  (not every review) — no match ≠ error; just note it and skip the link.
- Chatty has no DFY program yet → `dfy_created` is 0; keep the row but it's expected.
- This is team-facing: tone clear and encouraging, language Vietnamese (per workspace
  default for internal team content), short.
- **Output is Notion-only** — one sub-page per week under the app's parent page
  (Chatty/Joy IDs in §7). No .md in the repo, no git commit. Title MUST carry the
  date range. `NOTION_API_KEY` from `.env`; integration is already shared with both
  parent pages (re-share if push 404s). Notion API, not MCP — survives headless cron.
- **Slack digest (step 8)** runs AFTER the Notion push and links to it — Notion is the
  source of truth, Slack is just the ping. Posts AS LIZ (name + avatar) via the Avada
  bot to `chatty-cs` (`C07LZNWEUUD`) / `joy-faqs` (`C07MSUX0VPA`). If the Notion
  push fails, skip the Slack post for that app (don't ping a broken link).
