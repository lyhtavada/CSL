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
from _common import load_env, bq_client, to_utc_str, VN  # noqa: E402


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
    us, ue = to_utc_str(start), to_utc_str(end)

    env = load_env()
    client = bq_client(env)
    # Joy = app_joy ; Chatty = app_chatty OR app_faqs (legacy) ; Wishlist = app_wishlist
    q = f"""
    SELECT
      CASE WHEN ANY_VALUE(segments) LIKE '%app_joy%' THEN 'joy'
           WHEN ANY_VALUE(segments) LIKE '%app_chatty%' OR ANY_VALUE(segments) LIKE '%app_faqs%' THEN 'chatty'
           WHEN ANY_VALUE(segments) LIKE '%app_wishlist%' THEN 'wishlist' END AS app,
      session_id
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE timestamp >= TIMESTAMP('{us}') AND timestamp < TIMESTAMP('{ue}')
    GROUP BY session_id
    HAVING app IS NOT NULL
    """
    counts = {"joy": 0, "chatty": 0, "wishlist": 0}
    for r in client.query(q):
        counts[r.app] += 1

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
