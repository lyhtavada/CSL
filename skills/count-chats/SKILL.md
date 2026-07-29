---
name: count-chats
description: Ad-hoc count of real merchant conversations (Chatty/Joy/Wishlist) for any date range, week, or month — using the same validated counting method as /cs-weekly. Use when Liz asks "đếm chat tuần/tháng này", "conversation volume tháng X", or wants a number that isn't already in a scheduled report.
version: 1.0.0
---

# /count-chats

Ad-hoc chat-volume lookup. Wraps the shared counting logic in
`skills/_shared/chat_count.py` — the same method `/cs-weekly`'s
`fetch_metrics.py` uses, so a number pulled here always matches the weekly
report for the same range.

## What counts as a "conversation"

Not `COUNT(DISTINCT session_id)` — Crisp keeps one `session_id` per visitor
forever, so that undercounts real volume. Not a raw message-gap count either
— that overcounts (CS-initiated chats, single CTA-click-then-silence chats).
The method (full rationale + validation numbers in `chat_count.py`'s
docstring):

1. Sessionize on **merchant messages only** (`fromType='user'`, `type='text'`,
   non-empty) — a silence gap ≥ 6h starts a new conversation. Operator/bot
   messages never start or reset one.
2. Keep only conversations with **≥2 merchant messages** — drops CS-initiated
   chats (0 merchant msgs) and "clicked a CTA, bot replied, merchant went
   silent" chats (1 merchant msg).
3. Exclude Avada-internal test traffic (`customerEmail` on an `@avada*`
   domain).
4. Lookback window before the report start so a conversation spanning a
   period boundary isn't double-counted.

## Usage

```bash
python3 skills/count-chats/scripts/run.py --app chatty --start 2026-07-01 --end 2026-07-26
python3 skills/count-chats/scripts/run.py --app all --month 2026-07
python3 skills/count-chats/scripts/run.py --app joy --week 2026-07-20   # its Mon->Sun week
python3 skills/count-chats/scripts/run.py --app chatty --start 2026-07-01 --end 2026-07-26 --json
```

- `--app`: `chatty` | `joy` | `wishlist` | `all`
- Date range: `--start`/`--end` (inclusive), or `--month YYYY-MM` (full
  calendar month), or `--week YYYY-MM-DD` (any date → its Mon→Sun week)
- `--json` for structured output when composing into another report

## When Liz asks for a chat count

Run the script directly and report the number(s) — no need to re-derive the
method or re-litigate the definition each time. If she asks "why is this
different from what I remember", point to the 4 conditions above.
