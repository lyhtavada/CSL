---
name: dfy-tracker
description: Generate a MONTHLY DFY KPI tracker report for Joy (or Chatty). Pulls only open tickets, groups by CS, shows ticket link, created date, status, task completion, tags, and an auto-calculated Point column based on scoring tags. This is the monthly KPI scoring report — for the weekly monitoring report (Overview + adopt rate, no points), use /dfy-weekly.
version: 1.2.0
---

# DFY Tracker Skill (Monthly KPI)

Generate a **monthly DFY KPI** tracker from Avada Ticket API, grouped by CS, with Point scoring.

> **Weekly vs monthly:** This skill is for **monthly KPI** (Point column for scoring CS performance). For the **weekly monitoring** report (Overview block with adopt rate %, breakdown without points), use `/dfy-weekly` instead.

## Trigger

When Liz says `/dfy-tracker` or asks to "pull DFY tickets", "tạo DFY tracker", "xem DFY tháng X", "DFY KPI tháng".
(For "DFY tuần này" / weekly → use `/dfy-weekly`.)

## Parameters

Liz can specify:
- **App:** `joy` (default) or `chatty`
- **Period:** `month` (e.g. `tháng 5`, `2026-05`) — first to last day of the month
- **Filter:** exclude Liz's own tickets without tags (default: on)

If not specified, default to **last month**, **Joy**.

## Steps

### 1. Determine date range

- **Month:** first to last day of the specified month (default: last month)
- (Weekly ranges are handled by `/dfy-weekly`, not here.)

### 2. Fetch tickets from API

```
GET https://avada-ts-a9cb0.web.app/api/external/tickets/by-date
Headers: X-API-Key: {AVD_TICKET_API_KEY}
Params: startDate, endDate, appName ("JOY Loyalty" or "Chatty")
```

Filter:
- `subject.startsWith("[DFY]")`
- **Only open tickets** — exclude closed/resolved tickets (`ticketStatus !== "closed"`)

### 3. Fetch tags

```
GET https://avada-ts-a9cb0.web.app/api/external/tags
```

Map `tagIds` on each ticket to tag names.

### 4. Determine CS (creator)

Use `members[].isCreate === true` → `displayName`. Fallback to `memberUpdate.displayName`.

### 5. Filter

- Exclude Liz's tickets (`liz_avada`) that have no tags (test tickets)
- Exclude tickets with `tsStatus = "sale_request"`

### 6. Group by CS and generate markdown table

```markdown
## {CS Name} ({n} tickets)

| Date | Ticket | Store | Status | Tasks | Tags | Point |
|------|--------|-------|--------|-------|------|-------|
| 2026-05-22 | [JOY-...](link) | store.myshopify.com | In progress | 15/16 | DFY-1, DFY-video | 90 |
| 2026-05-23 | [JOY-...](link) | store2.myshopify.com | In progress | 8/12 | DFY-coupon-images | 5 |
| **Total** | | | | | | **95** |
```

- **Status:** `In progress` (only open tickets are fetched; closed tickets are excluded in step 2)
- **Tasks:** `{completed}/{total}`
- **Tags:** comma-separated tag names from `tagIds`
- **Point:** auto-calculated — sum the point value of every scoring tag on the ticket (see **Point rules** below). A ticket can have multiple scoring tags → cộng dồn. Tags không có điểm = 0.

### Point rules

| Tag | Point |
|-----|-------|
| DFY-1 | 60 |
| DFY-coupon-images | 5 |
| DFY-tier-banner | 10 |
| DFY-tier-icon | 10 |
| DFY-video | 30 |

All other tags (`DFY-adopted`, `DFY-no-adopt`, `DFY-following-up`, `review-yes`) = 0 point.

Ví dụ: ticket có `DFY-1` + `DFY-video` → Point = 60 + 30 = **90**.

Add a **Total** row per CS summing the Point column.

### 7. Save file

- Joy: `reports/dfy/joy/joy-dfy-{YYYY-MM}.md` (month) or `joy-dfy-{YYYY-W##}.md` (week)
- Chatty: `reports/dfy/chatty/chatty-dfy-{YYYY-MM}.md`

## Tag reference

| Tag | Meaning | Point |
|-----|---------|-------|
| DFY-1 | Level đạt được | 60 |
| DFY-adopted | MC giữ lại widget sau follow-up | 0 |
| DFY-coupon-images | DFY làm coupon images | 5 |
| DFY-following-up | Đang chờ follow-up | 0 |
| DFY-no-adopt | MC không adopt | 0 |
| DFY-tier-banner | DFY làm tier banner | 10 |
| DFY-tier-icon | DFY làm tier icon | 10 |
| DFY-video | Có quay video kết quả | 30 |
| review-yes | Convert được review từ DFY flow | 0 |

## Output

Print summary first:
```
App: Joy | Period: 2026-05 | Total: 60 tickets (open only) | CS: 12 | Total points: 1240
Saved: reports/dfy/joy/joy-dfy-2026-05.md
```

Then show per-CS breakdown (ticket count + total points only, not full table — too long for chat):
```
- Mai: 8 tickets | 320 pts
- Hương: 6 tickets | 210 pts
...
```
