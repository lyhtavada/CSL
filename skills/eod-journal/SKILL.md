---
name: eod-journal
description: Generate an end-of-day journal entry summarizing what Liz worked on today, from conversation history. Use when Liz says "/eod-journal", "journal", "ghi nhật ký hôm nay", "tổng kết ngày", "log ngày hôm nay". Role-agnostic — adapted from a personal daily-log skill (journal), kept mostly as-is since it doesn't depend on sales-specific data.
---

# End-of-Day Journal

Generate a short end-of-day entry from what actually happened in conversation today. This is a reflection log, not a plan — complements `/today` (which plans the day ahead) rather than duplicating it.

## Difference from the original version
The source skill read a separate hand-maintained activity log file (`~/second-brain/journal/logs/YYYY-MM-DD.log`) fed by a Telegram bot. This workspace has no such log — instead, scan today's conversation history directly (same source `/today` already uses) and derive the entry from what was actually done, not a pre-written log.

## Step 1: Gather today's activity

Scan today's conversation(s) for concrete actions: skills run, accounts worked on, decisions made, tickets handled, content drafted. Be specific — brand/account names, what was decided, what's still open.

## Step 2: Check for an existing entry

Check `reports/journal/YYYY-MM-DD.md`. If it exists (re-run same day), only add what's new — don't duplicate or rewrite existing content.

## Step 3: Write the entry

```
# Journal — YYYY-MM-DD (<day name>)

## What I did today
- [3-5 bullets, specific: names, accounts, outcomes]

## Wins
- [meetings booked, deals advanced, issues resolved, tools shipped]

## Blockers / open
- [anything unresolved or waiting on someone else]

## Learned
- [1-2 genuine insights, only if there's something real — don't pad]
```

**Light days (fewer than 3 real activities):** collapse "What I did" and "Wins" into one section, drop "Blockers" if empty. Don't pad to fill the template — a short honest entry beats a padded generic one.

Write in first person, direct and specific — not "worked on outreach and prospecting" but "drafted the upsell email for Cool-Vita after their VIP-tier ticket, waiting on Liz's review."

## Step 4: Save

Write to `reports/journal/YYYY-MM-DD.md`. No git push required — this repo already auto-syncs (per the `auto-sync` commits visible in git log).
