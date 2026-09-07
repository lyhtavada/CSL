#!/usr/bin/env python3
"""
Ad-hoc App Store review count, broken down by month, for any date range.

Reuses the validated crawler in skills/cs-weekly/scripts/fetch_reviews.py
(sort_by=newest + real pagination — see that file's docstring for why the
other two URL patterns silently drop or duplicate reviews). This script does
NOT re-implement scraping; it only adds month-bucketing on top so Liz can ask
"reviews tháng 5,6,7,8" without doing the date math or a manual scan through
the Shopify App Store listing (unreliable to eyeball — edited reviews can
reorder mid-listing, see memory count_reviews_listing_vs_bigquery.md).

Usage:
  python3 run.py --app chatty --start 2026-05-01 --end 2026-08-31
  python3 run.py --app chatty --months 5,6,7,8 --year 2026
  python3 run.py --app joy --month 2026-07
  python3 run.py --app chatty --months 5,6,7,8 --year 2026 --json
"""
import sys
import json
import argparse
import datetime
import calendar
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "cs-weekly" / "scripts"))
from fetch_reviews import fetch  # noqa: E402

SLUGS = {"chatty": "chatty", "joy": "joyio"}


def month_bounds(year, month):
    last = calendar.monthrange(year, month)[1]
    return datetime.date(year, month, 1), datetime.date(year, month, last)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, choices=sorted(SLUGS))
    ap.add_argument("--start", help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", help="YYYY-MM-DD inclusive")
    ap.add_argument("--month", help="YYYY-MM, single calendar month")
    ap.add_argument("--months", help="comma list of month numbers, e.g. 5,6,7,8 (needs --year)")
    ap.add_argument("--year", type=int, default=datetime.date.today().year)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.month:
        y, m = map(int, a.month.split("-"))
        start, end = month_bounds(y, m)
    elif a.months:
        months = [int(x) for x in a.months.split(",")]
        start = month_bounds(a.year, min(months))[0]
        end = month_bounds(a.year, max(months))[1]
    elif a.start and a.end:
        start = datetime.datetime.strptime(a.start, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(a.end, "%Y-%m-%d").date()
    else:
        ap.error("need --start/--end, --month, or --months (+ --year)")

    slug = SLUGS[a.app]
    rows = fetch(slug, start, end)
    inwin = [(d, r, n) for d, r, n in rows if start <= d <= end]

    buckets = {}
    for d, r, n in inwin:
        key = f"{d.year}-{d.month:02d}"
        b = buckets.setdefault(key, {"count": 0, "ratings": []})
        b["count"] += 1
        if r:
            b["ratings"].append(r)

    result = {
        "app": a.app,
        "start": str(start),
        "end": str(end),
        "total": len(inwin),
        "by_month": {
            k: {
                "count": v["count"],
                "avg": round(sum(v["ratings"]) / len(v["ratings"]), 2) if v["ratings"] else None,
            }
            for k, v in sorted(buckets.items())
        },
    }

    if a.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{a.app} reviews {result['start']}..{result['end']} — total {result['total']}")
        for k, v in result["by_month"].items():
            avg = f"avg {v['avg']}★" if v["avg"] else "avg n/a"
            print(f"  {k}: {v['count']}  ({avg})")


if __name__ == "__main__":
    main()
