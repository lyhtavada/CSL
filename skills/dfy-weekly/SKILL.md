---
name: dfy-weekly
description: Generate a WEEKLY DFY ticket tracker report for Joy (or Chatty). Week runs Friday→Thursday. Publishes a new Notion sub-page (newest on top) under the "Joy DFY Weekly" page — NOT a repo file. Shows a 3-line Overview (số ticket, adopted, ticket không có tag adopted) plus a per-CS breakdown table with ticket link, created date, store, task completion, and tags. NO Point column (weekly is for monitoring, not KPI scoring — use /dfy-tracker for monthly KPI with points).
version: 2.0.0
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

### 7. Compute Overview (with week-over-week compare)

The Overview compares **this week vs the previous Fri→Thu week**. Fetch the previous week too: run the same fetch + filter (steps 2-6) for the 7 days immediately before the current range (e.g. current `30/05→05/06` → previous `23/05→29/05`).

Compute for BOTH weeks: `Số ticket` (filtered open set), `Adopted` (DFY-adopted), `Adopted %` = adopted / số ticket, `Không tag adopted` = số ticket − adopted.

Then render 3 lines, each showing the delta vs last week:

- **Tổng ticket:** `{this}` `{▲ +N / ▼ -N / = 0}` _(tuần trước {prev})_
- **Adopted:** `{this} ({this_pct}%)` `{▲ +N% / ▼ -N% / = 0%}` _(tuần trước {prev}, {prev_pct}%)_ — delta is on the **percentage** (this_pct − prev_pct).
- **Ticket không có tag adopted:** `{this}` `{▲ +N / ▼ -N / = 0}` _(tuần trước {prev})_

Arrow rule: `▲` when up, `▼` when down, `=` when unchanged. Note `▲` on "không tag adopted" is bad, but keep the arrow purely directional — don't recolor by good/bad.

### 8. Breakdown table per CS — NO Point column

Group the filtered (open) tickets by CS, sort CS by ticket count desc, rows by createdAt asc.

```markdown
## {CS Name} ({n} tickets)

| Date | Ticket | Store | Tasks | Tags |
|------|--------|-------|-------|------|
| 2026-05-29 | [JOY-260529-uXXGdw](https://avada-ts-a9cb0.web.app/t/JOY-260529-uXXGdw) | store.myshopify.com | 18/22 | DFY-1 |
```

- **Ticket link:** `https://avada-ts-a9cb0.web.app` + `shortUrl` (e.g. `/t/JOY-...`).
- **Store:** `store[0].domain`.
- **Tasks:** `{completed}/{total}` from `tasks[]`.
- **Tags:** comma-separated DFY tag names only. Tag IDs live in `ticket.tagIds` (array) — map via `/api/external/tags`. Drop any tagId not in the 9-tag DFY set.
- **No Status column** — DFY tickets are all `tsStatus=done_for_you`, so the column adds no signal.
- **No Total/Point row** — weekly report does not score points.

### 9. Push to Notion (NOT a file)

The weekly report is published as a **new Notion sub-page**, newest on top — it is NOT saved to the repo and NOT committed to git.

1. Build the markdown report (see Report format below) and write it to a temp file, e.g. `/tmp/joy-dfy-{YYYY-W##}.md`.
2. Push it as a sub-page under the parent page:

```
python3 skills/dfy-weekly/scripts/push_notion.py \
  --parent 36fb0da449f1808d8b3df436c87f7345 \
  --title "Joy DFY - {DD/MM} → {DD/MM}" \
  --md /tmp/joy-dfy-{YYYY-W##}.md
```

- **Parent page** (Joy DFY Weekly): `36fb0da449f1808d8b3df436c87f7345`
- The script sets `position: page_start` → **the new sub-page lands at the TOP** of the parent (newest first). Don't change this.
- **Title** must be `Joy DFY - {start} → {end}` with the Fri→Thu date range (e.g. `Joy DFY - 30/05 → 05/06`).
- The first line of the markdown is the `#` H1; it duplicates the title inside the page body, which is fine.

## Report format

```markdown
# Joy DFY - {start} → {end}

## Overview

- **Tổng ticket:** 14 ▼ -11 _(tuần trước 25)_
- **Adopted:** 8 (57%) ▼ -15% _(tuần trước 18, 72%)_
- **Ticket không có tag adopted:** 6 ▼ -1 _(tuần trước 7)_

## {CS Name} ({n} tickets)
... breakdown tables ...

---

## Note

_(Liz điền — feedback khi review với CS)_
```

- The **Note** section is always the LAST block, after the per-CS breakdown, separated by a `---` divider. Leave the placeholder `_(Liz điền — feedback khi review với CS)_` so Liz fills it in Notion when reviewing with the team.
- See step 7 for how each Overview line + its ▲▼ delta is computed.

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

Print the Notion URL first, then headline numbers + per-CS counts:
```
App: Joy | Week: 2026-05-29 → 2026-06-04 | Số ticket: 18 | Adopted: 5 | Không tag adopted: 13
Notion: https://www.notion.so/...   (new sub-page, top of "Joy DFY - Weekly")

- sonny_avada: 5 tickets
- alyssa_avada: 4 tickets
...
```
