---
name: dfy-monthly
description: Generate a MONTHLY DFY report for Chatty for leadership (PM + anh Sam) — pulls open DFY tickets for a month, splits them into Inbound (no `proactive` tag) vs Proactive (has `proactive` tag) with adopt rate per group, auto-computes insights (video→adopt, AI-completion→adopt, Chatbox coverage, timing, automatic review rate via BigQuery, DFY tickets/app installs ratio, per-CS quality), reads CS comments on non-adopted tickets so Betty can categorize no-adopt reasons by hand, publishes a Notion sub-page (newest on top) under "Chatty DFY Reports", and posts a Block Kit Slack digest to the Chatty CS channel AS Liz with a "Xem full trên Notion" button. NO Point column — this is the leadership monitoring report, not KPI scoring (use /dfy-tracker for points). Chatty only. Runs automatically on the 2nd of each month at 10:00 (the cron prompt does the reason-categorization reading step too, since it runs headless Claude Code, not a bare script).
version: 1.1.0
---

# DFY Monthly Skill (Chatty — leadership report)

Generate a **monthly DFY report for Chatty** aimed at PM + anh Sam: adopt rate split by
channel (Inbound vs Proactive) + auto insights → Notion sub-page + Slack digest as Liz.

> **This is the leadership/monitoring report — NO points.** For the KPI scoring report
> (Point column per CS), use `/dfy-tracker`. For the weekly Fri→Thu monitoring, use
> `/dfy-weekly`. This skill = monthly, no points, sent to the CS channel as Liz.

## Trigger

When Liz says `/dfy-monthly`, "report DFY tháng", "DFY monthly Chatty", "tổng hợp DFY
Chatty tháng X".

## Parameters

- **App:** `chatty` only (Joy uses `/dfy-tracker` / `/dfy-weekly`; add here later if needed).
- **Month:** `YYYY-MM` (default: last month).
- **Mode:**
  - `--draft` (default when run by hand): fetch + build + **push Notion** + **DM Liz** the
    digest to preview. Does NOT post to the channel.
  - `--send`: also post the digest to the Chatty CS channel as Liz.
  - The **cron run posts straight to the channel** (see below) — no draft.

## Config (hard-coded, confirmed 2026-07-07)

| Thing | Value |
|-------|-------|
| Notion parent page ("Chatty DFY Reports") | `37ab0da449f180b5bd78e3253071269c` |
| Chatty CS Slack channel | `C0B62UJRGSJ` |
| Liz Slack user ID | `U02GT4PC6RH` |
| Ticket API key | `.env` `AVD_TICKET_API_KEY` |
| Notion API key | `.env` `NOTION_API_KEY` |
| Slack bot token (Avada bot) | `.env` `SLACK_BOT_TOKEN_AVADA` |

## Steps

Mostly scripted, with one manual reading step (1.5) where Betty categorizes no-adopt
reasons from free-text CS comments.

### 1. Fetch + analyze

```
python3 skills/dfy-monthly/scripts/fetch_dfy.py --app chatty --month {YYYY-MM} --out /tmp/dfy.json
```

- Pulls `GET /api/external/tickets/by-date` (appName `Chatty`) for the whole month.
- **DFY ticket** = has any tag in the DFY set (`DFY-*`, `ai agent`, `chatbox`, `proactive`).
- Keeps **open only** (`ticketStatus != closed`), drops `tsStatus=sale_request` and Liz's
  untagged test tickets.
- **Splits by `proactive` tag:** 🟢 Proactive (has it) vs 🔵 Inbound (doesn't) → adopt rate
  (`DFY-adopted / count`) for each group + overall.
- Maps CS → KPI nickname (`_identity/team-g2.md`). The Ticket API returns `username=None`
  and the handle in `displayName` with mixed casing — the script matches case-insensitively.
- Computes insights: video→adopt, AI-Agent-completion→adopt, Chatbox coverage, timing
  (which week of the month tickets cluster in), per-CS adopt/video rate.
- **Review rate (automatic, no manual tag):** matches each ticket's `chatLink` session_id
  (fallback: store domain + time) against `avada_cs.crisp_chats` for a
  `review_yes_chatty`/`rv_yes_chatty`/`review_yes_faq` segment. `insights.review` =
  `{count, total, pct}`.
- **DFY tickets / app installs this month:** `insights.dfy_per_install` compares this
  month's DFY ticket count against Chatty's new installs
  (`avada_product_dash.dash_daily_installs`, `app_id=avadaFaq`).
- **`no_adopt_raw`:** for every non-adopted ticket, pulls CS comments via
  `/api/external/tickets/{internal id}/actions` (filtered to `type=commentTicket` — must
  use the ticket's internal `id`, NOT the human `ticketId` like `CHAT-260629-...`, or the
  API returns an empty action list). This is raw text, not yet categorized.

### 1.5. Read no-adopt comments and categorize reasons (Betty, by hand)

Read `no_adopt_raw` from the JSON (each entry: ticket_id, store, cs, comments[]) and
group into reason buckets by hand — this is free-text Vietnamese CS notes, not
keyword-matched. Write the buckets to a small JSON, e.g.:

```json
{"buckets": [
  {"label": "Khách không phản hồi follow-up", "count": 7},
  {"label": "Setup phía khách chưa xong (chưa embed widget / enable AI Agent)", "count": 5}
]}
```

Save as `/tmp/reasons.json`. A ticket can land in more than one bucket — don't force
mutual exclusivity. Re-derive buckets fresh each month; don't reuse last month's labels
verbatim, patterns can shift.

### 2. Build the Notion body

```
python3 skills/dfy-monthly/scripts/build_report.py --in /tmp/dfy.json \
  --reasons /tmp/reasons.json --out /tmp/dfy.md
```

Body starts at `## Overview` (no H1). Order: Overview (now includes ⭐ review rate and
📈 DFY/install) → 💡 Insight & đề xuất → 🔵 Inbound table → 🟢 Proactive table →
❌ Lý do không adopt → Note (Liz fills in). `--reasons` is optional — omit it and the
section just shows a placeholder telling the reader it wasn't categorized yet.

### 3. Push to Notion (newest on top)

```
python3 skills/dfy-monthly/scripts/push_notion.py \
  --parent 37ab0da449f180b5bd78e3253071269c \
  --title "Chatty DFY - Tháng {M}/{YYYY}" \
  --md /tmp/dfy.md
```

- **Newest on top:** the script uses `position: page_start` → the new sub-page lands at
  the TOP of "Chatty DFY Reports". Don't change this — Liz wants the latest report first.
- Title format: `Chatty DFY - Tháng {M}/{YYYY}` (e.g. `Chatty DFY - Tháng 6/2026`).
- Capture the returned URL for the Slack button.

### 4. Post the Slack digest as Liz

```
# draft (default): DM Liz to preview
python3 skills/dfy-monthly/scripts/notify_slack.py --in /tmp/dfy.json --notion-url {URL} --dm

# send: post to the Chatty CS channel
python3 skills/dfy-monthly/scripts/notify_slack.py --in /tmp/dfy.json --notion-url {URL}
```

- Posts via the Avada bot with `username` + `icon_url` overridden to **Liz's** Slack
  identity (still shows a small "APP" tag — unavoidable with a bot token).
- **Block Kit:** header → tổng quan → tách kênh → 💡 điểm đáng chú ý → theo CS → context
  → primary button "📗 Xem full trên Notion" → footer context.
- **Slack highlights = video + review-yes only.** The Chatbox insight is intentionally
  kept OUT of the Slack digest (per Liz) but stays in the Notion Insight section.
- **Does NOT tag anyone** (`@channel` / individuals) — monthly report, no ping needed.

## Cleanup when re-running

If you re-push a report for the same month (e.g. after an edit), **archive the old
sub-page** so the parent doesn't accumulate duplicates:

```
PATCH https://api.notion.com/v1/pages/{old_page_id}  body {"archived": true}
```

(Notion-Version `2022-06-28`, `Authorization: Bearer {NOTION_API_KEY}`.)

## Output (chat summary)

```
App: Chatty | Month: 2026-06 | 27 DFY tickets | adopt 52%
  🔵 Inbound 22 (64%) · 🟢 Proactive 5 (0%)
Notion: https://app.notion.com/p/...
Slack: posted to C0B62UJRGSJ as Liz   (or: DM preview sent to Liz)
```

## Automated monthly run (launchd)

Runs on the **2nd of each month at 10:00** local time (`com.avada.dfy-monthly`),
generating **last month's** Chatty DFY report and **posting straight to the Chatty CS
channel** as Liz (not a draft).

- Cron source: `skills/dfy-monthly/cron/` (plist + `run-monthly.sh` + `prompt.txt` + `install.sh`)
- Install once (Liz runs in Terminal): `bash ~/CSL/skills/dfy-monthly/cron/install.sh`
- Log: `/tmp/dfy-monthly.log`
- **Machine off on the 2nd?** launchd skips (no catch-up). Run manually:
  `bash ~/CSL/skills/dfy-monthly/cron/run-monthly.sh`
- Note: `/dfy-tracker` also runs on the 2nd (15:00, KPI file). Different time + different
  output, so they don't collide.
```
