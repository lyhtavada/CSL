---
name: ticket-watch
description: Daily scan of open tickets (Chatty, Joy Loyalty, Joy Wishlist) for ones that look neglected — no update in 2+ days, unclaimed >24h, DFY checklist stalled, or P0/P1 past SLA — DM'd to Liz.
---

# /ticket-watch

Daily hygiene check across all 3 apps Liz owns. Pulls open tickets from the
Avada Ticket API, flags ones that look neglected, and DMs Liz a short report
via Slack — new issues in detail, older backlog as a summary count (not
re-listed every day).

## Flags

| Flag | Applies to | Rule |
|---|---|---|
| `stale_no_update` | Regular tickets (excludes `[DFY]`/`[ONB]` — tracked separately by `/dfy-tracker`) | Open, age ≥1 day, AND (no update since created OR still `tsStatus=pending`/unclaimed) |
| `dfy_stuck` | `[DFY]`/`[ONB]` project tickets | Open, age ≥2 days, AND has an incomplete `tasks[]` item with no update since |

## How it runs

1. `scripts/fetch_stale.py --json` (stale-days=1, dfy-stale-days=2 by default)
   — pulls tickets (window: last 60 days by `createdAt`), applies flags, and
   diffs against `state/seen.json` from the previous run to split **new**
   (just crossed a threshold — full detail) vs **carryover** (already
   reported, still open — summarized count only). Updates `state/seen.json`
   for the next run.
2. Compose a Vietnamese Slack message: per new/urgent ticket show subject,
   ticket link (`ticketUrl`), chat link (`chatLink`), and current status
   (`tsStatus`/progress) — then a one-line summary of carryover counts by
   app/flag.
3. Send via `../qa-weekly/scripts/send_dm.py` (reused, not duplicated) to
   Liz's Slack id `U02GT4PC6RH` — payload has one message, no `sender`
   override needed since it's a bot DM straight to her, not impersonation.

## Manual run

```
python3 skills/ticket-watch/scripts/fetch_stale.py --json > /tmp/ticket_watch.json
```
Then read the JSON, compose the DM text, write a payload file, and run
`send_dm.py --payload ... --send`.

## Cron

Daily 10:00 local — `cron/run-ticket-watch.sh`, installed via `cron/install.sh`.

## Suggested, not built (Liz can request)

- **Breakdown by CS phụ trách** — ticket API has `members[]`, could group
  stale tickets by who owns them → accountability view instead of a flat list.
- **VIP/Pro+Plus tier weighting** — surface stale tickets from Pro/Plus
  merchants above Free-tier ones, tying into the Chatty Proactive Care segment
  data.
