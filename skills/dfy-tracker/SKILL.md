---
name: dfy-tracker
description: Generate a DFY ticket tracker report for Joy (or Chatty) by week or month. Groups by CS, shows ticket link, created date, status, task completion, tags (adopted/no-adopt/etc), and a Point column for manual entry.
version: 1.0.0
---

# DFY Tracker Skill

Generate a DFY ticket tracker from Avada Ticket API, grouped by CS.

## Trigger

When Liz says `/dfy-tracker` or asks to "pull DFY tickets", "tạo DFY tracker", "xem DFY tháng X", "DFY tuần này".

## Parameters

Liz can specify:
- **App:** `joy` (default) or `chatty`
- **Period:** `week` (current or last week) or `month` (e.g. `tháng 5`, `2026-05`)
- **Filter:** exclude Liz's own tickets without tags (default: on)

If not specified, default to **last month**, **Joy**.

## Steps

### 1. Determine date range

- **Week:** Mon–Sun of the specified or last week
- **Month:** first to last day of the specified month

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
| 2026-05-22 | [JOY-...](link) | store.myshopify.com | Done | 15/16 | DFY-adopted | |
```

- **Status:** `In progress` (only open tickets are fetched; closed tickets are excluded in step 2)
- **Tasks:** `{completed}/{total}`
- **Tags:** comma-separated tag names from `tagIds`
- **Point:** empty — Liz fills manually

### 7. Save file

- Joy: `reports/dfy/joy/joy-dfy-{YYYY-MM}.md` (month) or `joy-dfy-{YYYY-W##}.md` (week)
- Chatty: `reports/dfy/chatty/chatty-dfy-{YYYY-MM}.md`

## Tag reference

| Tag | Meaning |
|-----|---------|
| DFY-1 | Level đạt được |
| DFY-adopted | MC giữ lại widget sau follow-up |
| DFY-coupon-images | DFY làm coupon images |
| DFY-following-up | Đang chờ follow-up |
| DFY-no-adopt | MC không adopt |
| DFY-tier-banner | DFY làm tier banner |
| DFY-tier-icon | DFY làm tier icon |
| DFY-video | Có quay video kết quả |
| review-yes | Convert được review từ DFY flow |

## Output

Print summary first:
```
App: Joy | Period: 2026-05 | Total: 60 tickets | CS: 12
Saved: reports/dfy/joy/joy-dfy-2026-05.md
```

Then show per-CS breakdown (ticket count only, not full table — too long for chat).
