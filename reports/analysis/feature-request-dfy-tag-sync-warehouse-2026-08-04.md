# Feature Request: Sync DFY ticket tags into the analytics warehouse

**Requested by:** Liz (CS Leader)
**Date:** 2026-08-04
**App:** Chatty (avadaFaq) — same gap likely applies to Joy
**Priority:** Needed to unblock a CS custom analytics view

## Problem

CS wants to build a custom dashboard view on `analytics.avada.net` for the Chatty DFY (Done For You) program — volume, turnaround time, and **adopt rate** trended weekly/monthly with WoW/MoM comparisons.

The BigQuery-backed analytics tools (`cs.tickets` / `cs.ticket_breakdown`, reading `avada_cs.tickets`) already expose everything except adopt rate: `ts_status`, `ticket_status`, `priority`, `created_at`, `due_date`, `done_at`, `resolution_duration_minutes`, `member_names`, `shop_domain`.

What's missing: **ticket tags** (`DFY-adopted`, `DFY-no-adopt`, `DFY-video`, `proactive`, `DFY-feedback`, etc.). These tags exist today, but only on the **Avada Ticket API** (Trello-backed, `avada-ts-a9cb0.web.app/api/external/tickets/...`) — they are not present in any column of `avada_cs.tickets` or any other table the analytics warehouse exposes to CS-role users. Adopt rate = `% of DFY tickets tagged DFY-adopted`, so without tags in the warehouse, adopt rate cannot be computed inside a custom view at all.

Today CS gets adopt rate via a separate weekly script (`fetch_dfy.py`) that calls the Ticket API directly and posts a Notion report — it works, but it's a one-off script, not a self-serve dashboard, and can't live inside `analytics.avada.net` alongside the rest of CS's metrics.

## Request

Sync ticket tags (tag IDs + tag names) from the Avada Ticket API into the warehouse, joinable to `avada_cs.tickets` by `ticket_id`/`id`.

Suggested shape — either works for CS's purposes:
- **Option A (preferred):** an `avada_cs.ticket_tags` table, one row per `(ticket_id, tag_name)` pair, refreshed on the same cadence as `avada_cs.tickets`.
- **Option B:** an array/repeated `tags` column added directly onto `avada_cs.tickets`.

Source of truth for tags: `GET /api/external/tickets/by-date` (and per-ticket `GET /api/external/tickets/{id}`) on `avada-ts-a9cb0.web.app`, field `tagIds` on each ticket, resolved against `GET /api/external/tags` for tag names. This is the same data source the existing `fetch_dfy.py` script pulls from — happy to share the script/logic as reference.

## Why this matters

- Adopt rate is the single most important DFY KPI for Chatty CS — without it, a "DFY custom view" on the main analytics dashboard is materially incomplete.
- Once tags are queryable in BigQuery, CS can build one self-serve view (trend + WoW/MoM deltas, no manual script run) instead of relying on a scheduled report script.
- Same gap likely blocks similar dashboards for Joy DFY down the line.

## Acceptance criteria

- [ ] Ticket tags queryable in the warehouse, joinable to `avada_cs.tickets` on ticket ID
- [ ] Covers at minimum: `DFY-adopted`, `DFY-no-adopt`, `DFY-video`, `proactive`, `DFY-feedback`, `verified-by-csl`
- [ ] Refreshed at least daily (matching `avada_cs.tickets` freshness)
- [ ] CS-role (`avadaFaq` scope) analytics MCP users can read the new table/column via the existing semantic tools or a documented query pattern

## Contact

Liz (CS Leader) — can provide ticket ID examples and the reference script (`fetch_dfy.py`) on request.
