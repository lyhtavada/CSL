---
name: count-reviews
description: Ad-hoc App Store review count for Chatty or Joy, broken down by month, for any date range. Use when Liz asks "đếm review tháng X", "review Chatty mấy tháng gần đây", "list review theo tháng" — a number that isn't already in a scheduled report.
version: 1.0.0
---

# /count-reviews

Ad-hoc review-count lookup, bucketed by calendar month. Wraps the validated
crawler in `skills/cs-weekly/scripts/fetch_reviews.py` (same script `/cs-weekly`
uses for its §2 review numbers) — a number pulled here always matches what
the weekly report would show for the same window.

## Why not just eyeball the App Store listing or query BigQuery ad-hoc

- **Manually paging `apps.shopify.com/{slug}/reviews` and reading it**: looks
  fine but is unreliable to hand-count. An edited review can jump position in
  the "newest" sort, which shifts what shows up on which page — you'll miss
  or double count near page boundaries. Confirmed 2026-09-07: manual count
  came in ~20-30% under the real number for Chatty May-Aug 2026.
- **Ad-hoc BigQuery/analytic-MCP query on `shopify_reviews`**: numbers came
  out *higher* than the true App Store listing in the same 2026-09-07 check —
  don't trust it either without cross-checking. `fetch_reviews.py` scrapes
  the live listing directly (regex on `data-review-content-id` blocks, first
  date/rating in each block = the review's own, not a reply's), which is what
  `/cs-weekly` has been validated against for months — treat it as
  source-of-truth for review counts, not the MCP tool.

## Usage

```bash
python3 skills/count-reviews/scripts/run.py --app chatty --start 2026-05-01 --end 2026-08-31
python3 skills/count-reviews/scripts/run.py --app chatty --months 5,6,7,8 --year 2026
python3 skills/count-reviews/scripts/run.py --app joy --month 2026-07
python3 skills/count-reviews/scripts/run.py --app chatty --months 5,6,7,8 --year 2026 --json
```

- `--app`: `chatty` | `joy` (app slugs `chatty` / `joyio` internally — Wishlist
  not supported yet, no confirmed App Store slug on file)
- Date range: `--start`/`--end` (inclusive), or `--month YYYY-MM` (one
  calendar month), or `--months 5,6,7,8` + `--year` (shorthand for a list of
  months, no date math needed)
- Output: total for the window + a per-month `{count, avg rating}` breakdown
- `--json` for structured output when composing into another report

## When Liz asks for a review count

Run the script and report the numbers — no need to re-derive the method each
time. If a number looks off vs. something she remembers from BigQuery or
eyeballing the listing, point to the "Why not" section above rather than
re-litigating it.
