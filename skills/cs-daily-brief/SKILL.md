---
name: ticket-watch
description: Daily scan of open tickets (Chatty, Joy Loyalty, Joy Wishlist) for ones that look neglected — no update in 1+ day (2+ for DFY/ONB) — with CS-owner breakdown and VIP highlighting, DM'd to Liz.
---

# /ticket-watch

Daily hygiene check across all 3 apps Liz owns. Pulls open tickets from the
Avada Ticket API, flags ones that look neglected, and DMs Liz a short report
via Slack — new issues in detail, older backlog as a summary count (not
re-listed every day), plus a per-CS ownership breakdown and always-shown VIP
tickets.

## Flags

| Flag | Applies to | Rule |
|---|---|---|
| `stale_no_update` | Regular tickets (excludes `[DFY]`/`[ONB]` — tracked separately by `/dfy-tracker`) | Open, age ≥1 day, AND (no update since created OR still `tsStatus=pending`/unclaimed) |
| `dfy_stuck` | `[DFY]`/`[ONB]` project tickets | Open, age ≥2 days, AND has an incomplete `tasks[]` item with no update since |

## Breakdowns (always included, not just new/carryover)

- **VIP tier** (`isVip` in output) — a ticket is VIP if `appPlan` isn't a
  free/basic plan (`NON_VIP_PLANS` in `fetch_stale.py`; plan naming drifts
  across years per app, so this is a coarse heuristic — adjust that set if it
  misclassifies). VIP tickets are always listed in full in the DM (never just
  summarized as a count), separate from the new/carryover split.
- **CS breakdown** (`assigneeBreakdown` in output) — count of currently
  flagged tickets per assignee (`members[].displayName`), across new +
  carryover, bot members (`AI Agent`/`Bot` in name) excluded. Snapshot of who
  currently owns the most neglected tickets.

## How it runs

1. `scripts/fetch_stale.py --json` (stale-days=1, dfy-stale-days=2 by default)
   — pulls tickets (window: last 60 days by `createdAt`), applies flags, and
   diffs against `state/seen.json` from the previous run to split **new**
   (just crossed a threshold — full detail) vs **carryover** (already
   reported, still open — summarized count only). Updates `state/seen.json`
   for the next run.
2. Compose a Vietnamese Slack message in 3 sections: ① new tickets (grouped
   by app, link/chat/progress per ticket) + carryover count, ② all VIP
   tickets in full, ③ CS ownership breakdown (top 8).
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
