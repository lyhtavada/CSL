---
name: dfy-weekly
description: Generate a WEEKLY DFY ticket tracker report for Joy (or Chatty). Week runs Friday→Thursday. Shows an Overview block (tickets created, open, adopted, no-adopt, following-up, adopt rate %) plus a per-CS breakdown table with ticket link, created date, store, status, task completion, and tags. NO Point column (weekly is for monitoring, not KPI scoring — use /dfy-tracker for monthly KPI with points).
version: 1.0.0
---

# DFY Weekly Skill

Generate a weekly DFY monitoring report from Avada Ticket API, grouped by CS.

This is the **weekly monitoring** report. For **monthly KPI scoring (with Point column)**, use `/dfy-tracker` instead.

## Trigger

When Liz says `/dfy-weekly`, "DFY tuần này", "DFY weekly", "report DFY theo tuần".

## Parameters

Liz can specify:
- **App:** `joy` (default) or `chatty`
- **Week:** which week (default: current week). Week runs **Friday → Thursday**.
  - Liz can also pass an explicit range, e.g. `29/5 → 4/6` or `2026-05-29 → 2026-06-04`.

If not specified, default to **current week (Fri→Thu)**, **Joy**.

## Steps

### 1. Determine date range

- Week = **Friday → Thursday** (7 days).
- "Current week" = the most recent Friday up to today's Thursday.
- If Liz gives an explicit range, use it verbatim.

### 2. Fetch tickets from API

```
GET https://avada-ts-a9cb0.web.app/api/external/tickets/by-date
Headers: X-API-Key: {AVD_TICKET_API_KEY}   # from CSL/.env
Params: startDate, endDate, appName ("JOY Loyalty" or "Chatty")
```

Response shape: `data.tickets` is the array, `data.total` is the count.

### 3. Fetch tags

```
GET https://avada-ts-a9cb0.web.app/api/external/tags
```

Response shape: `data` is the array of `{id, name, ...}`. Build a `tagId → name` map.
Only the 9 known DFY tags are relevant (see Tag reference). **Drop any tagId not in the DFY tag set** from the Tags column (avoids leaking unrelated internal tag IDs).

### 4. Identify DFY tickets

`subject.strip().lower().startsWith("[dfy]")`.

### 5. Determine CS (creator)

Use `members[].isCreate === true` → `displayName`. Fallback to `memberUpdate.displayName`.

### 6. Filter (for the breakdown + adopted/no-adopt/following counts)

- **Open only:** exclude `ticketStatus === "closed"`.
- Exclude `tsStatus === "sale_request"`.
- Exclude `liz_avada` tickets that have no tags (test tickets).

### 7. Compute Overview

- **Tickets tạo trong tuần** = total DFY tickets created in the range (BEFORE open-only filter — counts closed too). This is the denominator for adopt rate.
- **Open (đang theo dõi)** = count after the open-only filter (step 6).
- **Adopted** = tickets (in the filtered set) tagged `DFY-adopted`.
- **No-adopt** = tickets tagged `DFY-no-adopt`.
- **Following-up** = tickets tagged `DFY-following-up`.
- **Tỉ lệ adopt** = `adopted / tickets tạo trong tuần` (rounded to whole %). Show the fraction inline, e.g. `22%  _(adopted 5 / tickets tạo trong tuần 23)_`.
- **CS tham gia** = number of distinct CS creators in the filtered set.

### 8. Breakdown table per CS — NO Point column

Group the filtered (open) tickets by CS, sort CS by ticket count desc, rows by createdAt asc.

```markdown
## {CS Name} ({n} tickets)

| Date | Ticket | Store | Status | Tasks | Tags |
|------|--------|-------|--------|-------|------|
| 2026-05-29 | [JOY-260529-uXXGdw](https://avada-ts-a9cb0.web.app/t/JOY-260529-uXXGdw) | store.myshopify.com | done_for_you | 18/22 | DFY-1 |
```

- **Ticket link:** `https://avada-ts-a9cb0.web.app` + `shortUrl` (e.g. `/t/JOY-...`).
- **Store:** `store[0].domain`.
- **Status:** `tsStatus` (fallback `ticketStatus`).
- **Tasks:** `{completed}/{total}` from `tasks[]`.
- **Tags:** comma-separated DFY tag names only.
- **No Total/Point row** — weekly report does not score points.

### 9. Save file

- Joy: `reports/dfy/joy/joy-dfy-{YYYY-W##}.md` (ISO week number)
- Chatty: `reports/dfy/chatty/chatty-dfy-{YYYY-W##}.md`

Use the ISO week of the range's end (Thursday) for `W##`.

## Report format

```markdown
# Joy DFY Tracker — Week {start} → {end}

_App: JOY Loyalty | Period: {start} → {end}_

## Overview

- **Tickets tạo trong tuần:** 23
- **Open (đang theo dõi):** 15
- **Adopted:** 5
- **No-adopt:** 0
- **Following-up:** 2
- **Tỉ lệ adopt:** 22%  _(adopted 5 / tickets tạo trong tuần 23)_
- **CS tham gia:** 5

## {CS Name} ({n} tickets)
... breakdown tables ...
```

## Tag reference (DFY tag set)

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

(Weekly report shows tags for context but does NOT compute points. Points live in `/dfy-tracker` monthly.)

## Output (chat summary)

Print summary first, then per-CS counts:
```
App: Joy | Week: 2026-05-29 → 2026-06-04 | Created: 23 | Open: 15 | Adopted: 5 | No-adopt: 0 | Adopt rate: 22%
Saved: reports/dfy/joy/joy-dfy-2026-W23.md

- sonny_avada: 5 tickets
- alyssa_avada: 4 tickets
...
```
