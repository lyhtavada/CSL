#!/usr/bin/env python3
"""
Count Crisp conversations per app (Joy, Chatty, Wishlist) for a rolling 24h
window, 08:30 VN to 08:30 VN the next day, for the daily CS report — aligned
to the 08:45 cron run so the window ends just before the report is sent
(minimal lag), instead of a midnight-aligned calendar day.

Default target day = yesterday (VN) — e.g. run today (22nd) to report on the
window 21st 08:30 -> 22nd 08:30.

Usage:
  python3 fetch_conversations.py --json                # yesterday 08:30 -> today 08:30 (VN)
  python3 fetch_conversations.py --date 2026-07-21 --json
"""
import os, sys, json, argparse, datetime as dt

sys.path.insert(0, os.path.dirname(__file__))
from _common import load_env, bq_client, VN  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_shared"))
from chat_count import chat_count_window, APP_SEGMENTS, LOOKAROUND_DAYS  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYY-MM-DD (VN calendar day, window starts 08:30 this day) — default yesterday")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.date:
        day = dt.datetime.strptime(a.date, "%Y-%m-%d").replace(tzinfo=VN)
    else:
        day = (dt.datetime.now(VN) - dt.timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0)

    start = day.replace(hour=8, minute=30, second=0, microsecond=0)
    end = start + dt.timedelta(days=1)

    env = load_env()
    client = bq_client(env)
    # Same "real conversation" filters as /cs-weekly + /count-chats (merchant-
    # anchored, >=2 msgs, internal traffic excluded) but using chat_count_window()
    # — counts conversations ACTIVE in this window (not just ones that started
    # in it), matching this report's original "sessions touched" intent. See
    # skills/_shared/chat_count.py docstring for why chat_count() (start-anchored)
    # would systematically undercount at daily granularity.
    win_start = start.strftime("%Y-%m-%d %H:%M:%S+07")
    win_end_excl = end.strftime("%Y-%m-%d %H:%M:%S+07")
    fetch_start = (start - dt.timedelta(days=LOOKAROUND_DAYS)).strftime("%Y-%m-%d %H:%M:%S+07")
    fetch_end = (end + dt.timedelta(days=LOOKAROUND_DAYS)).strftime("%Y-%m-%d %H:%M:%S+07")
    counts = {
        app: chat_count_window(client, segs, win_start, win_end_excl, fetch_start, fetch_end)
        for app, segs in APP_SEGMENTS.items()
    }

    out = {
        "date": start.strftime("%Y-%m-%d"),
        "startVn": start.strftime("%d/%m/%Y %H:%M"),
        "endVn": end.strftime("%d/%m/%Y %H:%M"),
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
