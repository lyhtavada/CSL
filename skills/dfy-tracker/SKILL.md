---
name: dfy-tracker
description: Generate a MONTHLY DFY KPI tracker report for Joy (or Chatty). Pulls only open tickets, groups by CS, shows ticket link, created date, status, task completion, tags, and an auto-calculated Point column based on scoring tags. This is the monthly KPI scoring report — for the weekly monitoring report (Overview + adopt rate, no points), use /dfy-weekly. Runs automatically on the 2nd of each month (launchd) for last month's Joy tickets.
version: 1.3.0
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

### 4. Determine CS (creator) and map to KPI nickname

Use `members[].isCreate === true` → `displayName`. Fallback to `memberUpdate.displayName`.

Then **map the CS to their KPI nickname** (the abbreviated name used for KPI, e.g. `VanCT`, `HangHM`). The report and grouping must use the **nickname**, not the raw `displayName`/`trello username`.

Map via the `trello username` the API returns (or `displayName` as fallback):

| trello username | displayName | Nickname (KPI) |
|---|---|---|
| liz_avada | Liz | LyHT |
| hana_avada | Hana | HangHM |
| audrey_avada | Audrey | VanCT |
| alyssa_avada | Alyssa | LyPK |
| sonny_avada | Sonny | HuyTC |
| alicia_avada | Alicia | AnhLN |
| rosie_avada | Rosie | ThaoLTT |
| jade_avada | Jade | PhuongNT |
| mirra_avada | Mirra | MinhBT |
| andy_avada | Andy | AnhBD |
| hazel_avada | Hazel | HienPT |
| megan_avada | Megan | TrangNTH |
| cody_avada | Cody | ChauHM |
| phoebe_avada | Phoebe | PhuongTTM |
| linda1_avada | Linda | LinhTLK |

> Source of truth: `_identity/team-g2.md` (columns "Nickname (KPI)" + "Trello username"). If a new CS appears in the API but not in this table, fall back to the raw `displayName` and flag it in the output so the table here can be updated.

### 5. Filter

- Exclude Liz's tickets (`liz_avada`) that have no tags (test tickets)
- Exclude tickets with `tsStatus = "sale_request"`

### 6. Group by CS (nickname) and generate markdown table

Group by the **KPI nickname** from step 4.

```markdown
## {Nickname} ({n} tickets)

| Date | Ticket | Store | Status | Tasks | Tags | Point |
|------|--------|-------|--------|-------|------|-------|
| 2026-05-22 | [JOY-...](link) | store.myshopify.com | In progress | 15/16 | DFY-1, DFY-video | 125 |
| 2026-05-23 | [JOY-...](link) | store2.myshopify.com | In progress | 8/12 | DFY-coupon-images | 5 |
| **Total** | | | | | | **130** |
```

- **Status:** `In progress` (only open tickets are fetched; closed tickets are excluded in step 2)
- **Tasks:** `{completed}/{total}`
- **Tags:** comma-separated tag names from `tagIds`
- **Point:** auto-calculated — Required (`DFY-1` = 75) + Recommended (coupon/banner/icon cộng dồn, **trần 25p**) + Video (`DFY-video` = 50). A ticket can have multiple scoring tags → cộng dồn theo nhóm (xem **Point rules** below). Tags không có điểm = 0.

### Point rules

Điểm chia theo 3 nhóm:
- **Required: 75p** — tag `DFY-1` (level đạt được). Đây là phần bắt buộc.
- **Recommended: tổng trần 25p** — bonus, cộng dồn các tag dưới đây (tối đa 25p):
  - `DFY-coupon-images` = 5
  - `DFY-tier-banner` = 10
  - `DFY-tier-icon` = 10
- **Video: 50p** — tag `DFY-video`.

| Tag | Nhóm | Point |
|-----|------|-------|
| DFY-1 | Required | 75 |
| DFY-coupon-images | Recommended | 5 |
| DFY-tier-banner | Recommended | 10 |
| DFY-tier-icon | Recommended | 10 |
| DFY-video | Video | 50 |

All other tags (`DFY-adopted`, `DFY-no-adopt`, `DFY-following-up`, `review-yes`) = 0 point.

Recommended cộng dồn nhưng **trần 25p** (nếu có cả 3 tag = 5+10+10 = 25, đúng trần).

Ví dụ: ticket có `DFY-1` + `DFY-video` → Point = 75 + 50 = **125**.
Ví dụ: ticket có `DFY-1` + `DFY-coupon-images` + `DFY-tier-banner` + `DFY-tier-icon` → 75 + 25 = **100**.

Add a **Total** row per CS summing the Point column.

### 7. Save file

- Joy: `reports/dfy/joy/joy-dfy-{YYYY-MM}.md` (month) or `joy-dfy-{YYYY-W##}.md` (week)
- Chatty: `reports/dfy/chatty/chatty-dfy-{YYYY-MM}.md`

## Tag reference

| Tag | Meaning | Nhóm | Point |
|-----|---------|------|-------|
| DFY-1 | Level đạt được | Required | 75 |
| DFY-adopted | MC giữ lại widget sau follow-up | — | 0 |
| DFY-coupon-images | DFY làm coupon images | Recommended | 5 |
| DFY-following-up | Đang chờ follow-up | — | 0 |
| DFY-no-adopt | MC không adopt | — | 0 |
| DFY-tier-banner | DFY làm tier banner | Recommended | 10 |
| DFY-tier-icon | DFY làm tier icon | Recommended | 10 |
| DFY-video | Có quay video kết quả | Video | 50 |
| review-yes | Convert được review từ DFY flow | — | 0 |

> Recommended (coupon + banner + icon) cộng dồn nhưng **trần 25p**.

## Output

Print summary first:
```
App: Joy | Period: 2026-05 | Total: 60 tickets (open only) | CS: 12 | Total points: 1240
Saved: reports/dfy/joy/joy-dfy-2026-05.md
```

Then show per-CS breakdown by **nickname** (ticket count + total points only, not full table — too long for chat):
```
- VanCT: 8 tickets | 320 pts
- HangHM: 6 tickets | 210 pts
...
```

## Automated monthly run (launchd)

This skill runs automatically on the **2nd of each month at 15:00** local time via launchd (`com.avada.dfy-tracker-monthly`), generating the report for **last month's Joy tickets** and committing it.

- Cron source: `skills/dfy-tracker/cron/` (plist + `run-monthly.sh` + `prompt.txt` + `install.sh`)
- Install once (Liz runs in Terminal): `bash ~/CSL/skills/dfy-tracker/cron/install.sh`
- Log: `/tmp/dfy-tracker-monthly.log`
- **Machine off on the 2nd?** launchd skips the run (no catch-up). Run it manually the next day: `bash ~/CSL/skills/dfy-tracker/cron/run-monthly.sh`
