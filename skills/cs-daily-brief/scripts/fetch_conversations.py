#!/usr/bin/env python3
"""
Count Crisp conversations per app (Joy, Chatty, Wishlist) for one full
calendar day (00:00–24:00 VN time), for the daily CS report.

Default target day = yesterday (VN) — e.g. run today (22nd) to report on the
21st's full 24h.

Usage:
  python3 fetch_conversations.py --json                # yesterday (VN)
  python3 fetch_conversations.py --date 2026-07-21 --json
"""
import os, sys, json, argparse, datetime as dt

sys.path.insert(0, os.path.dirname(__file__))
from _common import load_env, bq_client, VN  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_shared"))
from chat_count import chat_count_active, APP_SEGMENTS  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYY-MM-DD (VN calendar day) — default yesterday")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.date:
        day = dt.datetime.strptime(a.date, "%Y-%m-%d").replace(tzinfo=VN)
    else:
        day = (dt.datetime.now(VN) - dt.timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0)

    start = day.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + dt.timedelta(days=1)
    day_str = start.strftime("%Y-%m-%d")

    env = load_env()
    client = bq_client(env)
    # Same "real conversation" filters as /cs-weekly + /count-chats (merchant-
    # anchored, >=2 msgs, internal traffic excluded) but using chat_count_active()
    # — counts conversations ACTIVE this day (not just ones that started today),
    # matching this report's original "sessions touched today" intent. See
    # skills/_shared/chat_count.py docstring for why chat_count() (start-anchored)
    # would systematically undercount at daily granularity.
    counts = {
        app: chat_count_active(client, segs, day_str, day_str)
        for app, segs in APP_SEGMENTS.items()
    }

    out = {
        "date": start.strftime("%Y-%m-%d"),
        "startVn": start.strftime("%d/%m/%Y 00:00"),
        "endVn": (end - dt.timedelta(seconds=1)).strftime("%d/%m/%Y 23:59"),
        "counts": counts,
        "total": sum(counts.values()),
    }

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"{out['date']}: total={out['total']} joy={counts['joy']} "
              f"chatty={counts['chatty']} wishlist={counts['wishlist']}")


if __name__ == "__main__":
    main()
