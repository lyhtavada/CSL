---
name: cs-weekly
description: Generate the weekly CS bulletin for the CS team of an app (Chatty or Joy) to read and stay on top of the week. Period = Monday→Sunday of LAST week. Pulls tickets created (Ticket API), chats (BigQuery crisp_chats), DFY created, App Store reviews (Shopify, sort_by=newest), and (Joy only) onboarding tickets ([ONB] prefix, 10-step checklist) — each compared vs the prior week — then clusters top issues from tickets (Ticket API, [dfy] excluded), scans the #product-release Slack channel for releases, publishes a team-facing report as a new sub-page at the TOP of the app's Notion page (title includes the date range), and posts a TL;DR digest (as Liz, with a Notion button) to the app's CS Slack channel. Coaching + recognition sections are left for Liz to fill/review. Use when Liz says "/cs-weekly", "CS weekly", "report tuần cho team", or it runs via cron Mon 9AM.
version: 1.7.0
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

**`chats` = real merchant conversations — NOT DISTINCT session_id.** Logic lives in
`skills/_shared/chat_count.py` (shared with `/count-chats`, full rationale + validation
numbers in its docstring): sessionize on merchant (`fromType='user'`) text messages only
— a silence gap ≥ 6h starts a new conversation, operator messages never start/reset one
— then only count conversations with ≥2 merchant messages (excludes CS-initiated chats
and "click-a-CTA-then-go-silent" chats), excluding Avada-internal test traffic
(`@avada*` emails), with a lookback window so a conversation spanning a report-period
boundary isn't double-counted. Retune via `chat_count()`'s `gap_hours`/`min_user_msgs`
args if needed.

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

Read the subjects + descriptions, cluster the asks into 3-5 themes. For EACH theme,
**actually count** how many of the pulled tickets belong to it — do not eyeball or
estimate ("~1/3", "phần lớn") from a skim. A theme's ticket must genuinely be about
that issue (e.g. "AI trả lời sai/bịa thông tin" = the ticket reports a wrong/invented
answer — NOT any ticket that merely mentions "AI", like a pricing question or a
"train AI" request). State the real count as `{n}/{total non-dfy}` in the report, not
a fraction guess. Rank themes by this count.

For each theme, list ticket links as proof: `https://avada-ts-a9cb0.web.app` +
`shortUrl` (e.g. `https://avada-ts-a9cb0.web.app/t/CHAT-260718-tp3nJq`), using
`ticketNumber` as the link text. If a theme has ≤3 tickets, link all of them; if more,
link 3 representative ones and note `(+n khác)` — never drop the true count to fit.

For each theme, also give a 1-line "cách xử lý" + KB pointer. The `[bug]` subject
prefix marks bug reports — flag any bug reported repeatedly (→ Known bugs in §4 of
the report).

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
- **`handle`** — từ `GET /api/obs/metrics?agent=<id>&from=&to=` + `GET /api/obs/sessions`
  (cùng range). **Report 2 chỉ số song song** (Liz chốt 2026-08-11) — chúng trả lời 2
  câu hỏi khác nhau, đừng gộp thành một:
  - `aiResolvedPct` = `kpi.aiResolvedPct` của API = `ai_resolved/ai_replied`.
    **Đo chất lượng bot.** Khớp đúng con số dashboard cs2 nên team/anh Sam đối chiếu được.
  - `takeOnlyPct` = **% session bot chạy trọn mà CS không phải đụng tay** = (session
    không `human_active`, không `escalated`, không `no_ai`, `bot_reply_count`>0) /
    `ai_replied`. **Đo tải nhân sự** — dùng cho quyết định headcount. Cùng mẫu số
    `ai_replied` để so trực tiếp với `aiResolvedPct`. Đây là **cận trên**: session
    merchant im lặng sau khi bot nudge vẫn được tính.
  - `unclearGapPct` = `takeOnlyPct − aiResolvedPct` = vùng merchant im lặng, không rõ
    có được giúp không. Khoảng này phình ra = bot nói nhiều mà không chốt được vấn đề.
  - `aiReplyCoveragePct` / `humanTakeoverPct` / `escalationRatePct` — bổ trợ (lấy thẳng từ kpi).
  - `sessions` / `aiReplied` / `takeOnlySessions` / `inbound` / `botReplies` — volume.
  - ⚠️ Công thức cũ `(total − human_active)/total` đã **bỏ** (2026-08-11): nó đếm cả
    session bot đã escalate (CS xử qua ticket nên `human_active` vẫn false) lẫn session
    `no_ai` vào tử số → thổi phồng ~15 điểm và lệch dashboard ở cả tử lẫn mẫu. Số cũ
    trong report trước 08/2026 KHÔNG so sánh trực tiếp được với số mới.
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

Fill the report's **🛠 TS Elite usage section** (gần cuối, ngay trước "Lưu ý tuần
này"). Top table + ai chưa dùng + 3-5 câu/chủ đề hay hỏi. **If `inactive` không rỗng**
→ liệt kê tên, gợi ý Liz nhắc. Nếu `totalChatsG2` = 0 (cả team chưa đụng) → ẩn section,
ghi 1 dòng TL;DR. **Notion-only** — KHÔNG đưa vào Slack digest (step 8 không nhận file này).

### 4d. Pull Onboarding tickets (Joy only)

Joy has a dedicated onboarding flow tracked as tickets with subject prefix
`[ONB]` and a 10-step checklist (`tasks`). Run **only for Joy**, with `--compare`:
```bash
python3 skills/cs-weekly/scripts/fetch_onboarding.py --start {start} --end {end} --compare --json > /tmp/joy-onboarding-{YYYY-W##}.json
```
Returns `new_count` (created in period), `open_count` / `golive_count` (current
snapshot of a 90-day lookback — `open_count` = still open regardless of when
created, `golive_count` = closed within the period), `avg_checklist_pct` (avg
% done across open tickets), `open_tickets` (full list: store, CS, done/total,
daysOpen), `delayed` (open tickets >14 days old — flag these), and
`prevWeek.new_count` (for ▲▼).

Fill the report's **🚀 Onboarding tickets tuần này** section (Joy only, after
§2). If both `new_count` and `open_count` are 0 → hide the section. Chatty has
no onboarding-ticket flow — skip this step entirely for Chatty.

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

Use `reports/weekly-cs/TEMPLATE.md`. Fill the report's §1–4b from data. Leave the
final "💡 Lưu ý tuần này" section for Liz to review — write `_(Liz điền)_` placeholders,
but you MAY pre-fill a process reminder if a repeated bug/issue warrants it.

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
  --onboarding-file /tmp/joy-onboarding-{YYYY-W##}.json \
  --notion-url {the URL printed by push_notion.py in step 7}
```
- **`--botqa-file`** (the JSON from step 4b) adds a "🤖 Bot performance tuần này" block
  to the Slack digest — Handle (AI resolved + CS không phải đụng tay + gap + AI coverage
  + human takeover + escalation + volume, with ▲▼ vs last week) + QA (verify coverage /
  correction rate / + top verify + top correction), ⚠️ flag if verify coverage < 30%.
- **`--onboarding-file`** (the JSON from step 4d, **Joy only** — omit this flag
  for Chatty) adds a "🚀 Onboarding tickets tuần này" block: new/open/go-live
  counts + avg checklist % + up to 5 delayed (>14d) tickets. Hidden automatically
  if the week has no onboarding tickets (new or backlog).
- **CS channel IDs:**
  - Chatty: `C07LZNWEUUD`   (`chatty-cs`)
  - Joy:    `C07MSUX0VPA` (`joy-faqs`, private)
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
1b. **🤖 Bot performance** (right after TL;DR) — **Handle** (AI resolved + CS không phải
   đụng tay + AI coverage + human takeover + escalation + volume) and **QA** (verify
   coverage / correction rate + top 3 verify + top 3 correction), each vs last week (▲▼). From
   step 4b's JSON (`--compare`). ⚠️ flag if verify coverage < 30%. This whole block also
   goes into the Slack digest.
2. **📊 Tình hình support** — table: tickets / chats / DFY / reviews, vs last week (▲▼).
   Get "tuần trước" from the `--compare` flag's `prev_week` block (re-pulled live from
   source) — there is no .md file in the repo to read. Show ▲▼ % for tickets/chats,
   ▲▼ count for reviews.
2b. **🚀 Onboarding tickets** (Joy only, right after §2) — new/open/go-live counts vs
   last week (▲▼ on new), avg checklist %, table of open tickets, delayed (>14d) flag.
   From step 4d's JSON (`--compare`). Hidden if the week has no onboarding tickets
   (new or backlog). This block also goes into the Slack digest (Joy only).
3. **🔥 Top issues** — 3-5 themes from tickets (Ticket API, `[dfy]` excluded), each with
   a real counted `{n}/{total}` (not a guessed fraction), a fix/KB pointer, and 2-3
   proof ticket links (`https://avada-ts-a9cb0.web.app` + `shortUrl`).
4. **🆕 Cập nhật sản phẩm & policy** — releases from #product-release + known bugs open.
4b. **🛠 TS Elite usage** (gần cuối, trước "Lưu ý tuần này") — team G2 dùng agent
   investigate: total + active/members vs last week (▲▼), top 5 user, ai chưa dùng
   (⚠️), 3-5 chủ đề hay hỏi (cluster từ `questions`). From step 4c's JSON
   (`--compare`). **Notion-only**, KHÔNG vào Slack digest.
5. **💡 Lưu ý tuần này** — last section. Liz reviews/fills; you may pre-fill a process
   reminder if a repeated bug/issue warrants it.

## Notes / gotchas

- **Period is Mon→Sun of LAST week**, not a rolling 7-day window.
- **Reviews:** ALWAYS `sort_by=newest`. App Store's default page order is NOT by
  date, so any early-stop on a non-sorted feed silently drops reviews.
- **Slack channels** both open ONLY with `SLACK_BOT_TOKEN_AVADA`:
  release feed `C07RNAY9ZC6` (§5) and bad-review feed `G019ZF7GM7H` (§5b).
- **Bad-review scan triggers only for ≤3★** (Liz's rule). The feed is sparse
  (not every review) — no match ≠ error; just note it and skip the link.
- Chatty has no DFY program yet → `dfy_created` is 0; keep the row but it's expected.
- Chatty has no onboarding-ticket flow (`[ONB]`) → skip step 4d and the §2b section
  entirely for Chatty (don't show a 0 row).
- This is team-facing: tone clear and encouraging, language Vietnamese (per workspace
  default for internal team content), short.
- **Output is Notion-only** — one sub-page per week under the app's parent page
  (Chatty/Joy IDs in §7). No .md in the repo, no git commit. Title MUST carry the
  date range. `NOTION_API_KEY` from `.env`; integration is already shared with both
  parent pages (re-share if push 404s). Notion API, not MCP — survives headless cron.
- **Slack digest (step 8)** runs AFTER the Notion push and links to it — Notion is the
  source of truth, Slack is just the ping. Posts AS LIZ (name + avatar) via the Avada
  bot to `chatty-cs` (`C07LZNWEUUD`) / `joy-faqs` (`C07MSUX0VPA`, Joy). If the Notion
  push fails, skip the Slack post for that app (don't ping a broken link). Bot must
  be a member of the channel — invite `@avada_bot` if posting fails with
  `not_in_channel`.
