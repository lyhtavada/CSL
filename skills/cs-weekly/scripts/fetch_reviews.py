#!/usr/bin/env python3
"""
Crawl Shopify App Store reviews for a given app within a date window.

WHY sort_by=newest (learned the hard way, 2026-06-10):
  - `?page=N` plain      → NOT sorted by date; this month's reviews are scattered
                           across many pages → early-stop misses them.
  - `?sort_by=most_recent&page=N` → Shopify ignores page, redirects to page 1
                           → you re-crawl page 1 and miss everything else.
  - `?sort_by=newest&page=N`  → TRUE date-descending + real pagination. Safe to
                           stop once a page's oldest date is before `start`.

Each review block (split on `data-review-content-id`) may contain TWO dates:
the review date AND the merchant's reply date. Always take the FIRST date/rating
in the block (the review's own).

Usage:
  python3 fetch_reviews.py --slug joyio  --start 2026-06-01 --end 2026-06-07
  python3 fetch_reviews.py --slug chatty --start 2026-06-01 --end 2026-06-07 --json

App slugs: Joy = joyio, Chatty = chatty
"""
import re, json, argparse, datetime, urllib.request

UA = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
DATE_RE = re.compile(r"([A-Z][a-z]{2,8} \d{1,2}, 20\d\d)")
STAR_RE = re.compile(r"(\d) out of 5 stars")


def fetch(slug, start, end, max_pages=40):
    rows = []  # (date, rating)
    for page in range(1, max_pages + 1):
        url = f"https://apps.shopify.com/{slug}/reviews?sort_by=newest&page={page}"
        req = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30)
        # If Shopify redirected us off the requested page, there are no more pages.
        if f"page={page}" not in req.geturl() and page > 1:
            break
        html = req.read().decode("utf-8", "ignore")
        blocks = re.split(r"data-review-content-id", html)[1:]
        if not blocks:
            break
        page_min = None
        for b in blocks:
            ds = DATE_RE.findall(b)
            rs = STAR_RE.findall(b)
            if not ds:
                continue
            d = datetime.datetime.strptime(ds[0], "%B %d, %Y").date()  # FIRST = review date
            r = int(rs[0]) if rs else None                            # FIRST = review rating
            page_min = d if page_min is None else min(page_min, d)
            rows.append((d, r))
        # newest-first → once the whole page predates the window, we're done.
        if page_min and page_min < start:
            break
    return rows


def summarize(slug, start, end):
    rows = fetch(slug, start, end)
    inwin = [(d, r) for d, r in rows if start <= d <= end]
    n = len(inwin)
    avg = round(sum(r for _, r in inwin if r) / n, 2) if n else 0.0
    dist = {}
    for _, r in inwin:
        dist[r] = dist.get(r, 0) + 1
    low = [{"date": str(d), "rating": r} for d, r in inwin if r and r <= 3]
    return {
        "start": str(start),
        "end": str(end),
        "count": n,
        "avg": avg,
        "distribution": {str(k): v for k, v in sorted(dist.items(), reverse=True)},
        "low_reviews": low,
        "reviews": [{"date": str(d), "rating": r} for d, r in sorted(inwin, reverse=True)],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="joyio (Joy) or chatty (Chatty)")
    ap.add_argument("--start", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--compare", action="store_true",
                    help="also pull the prior Mon→Sun week for ▲▼ comparison")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    start = datetime.datetime.strptime(a.start, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(a.end, "%Y-%m-%d").date()

    this = summarize(a.slug, start, end)
    out = {"slug": a.slug, "this_week": this}
    if a.compare:
        d = datetime.timedelta(days=7)
        out["prev_week"] = summarize(a.slug, start - d, end - d)

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        t = this
        print(f"{a.slug}: {t['count']} reviews {t['start']}–{t['end']} | avg {t['avg']}★ | dist {t['distribution']}")
        if t["low_reviews"]:
            print(f"  ⚠️ low (≤3★): {t['low_reviews']}")
        if a.compare:
            p = out["prev_week"]
            print(f"  prev: {p['count']} reviews {p['start']}–{p['end']} | avg {p['avg']}★")


if __name__ == "__main__":
    main()
