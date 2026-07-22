#!/usr/bin/env python3
"""
Check-in/checkout status for Team G2 over one full calendar day (00:00–24:00
VN time), for the daily CS report. Reuses shift_status() from cs-daily/lib
(same Admin API /shifts + /shifts/:id/checks source) rather than duplicating it.

Default target day = yesterday (VN).

Usage:
  python3 fetch_checkin.py --json                # yesterday (VN)
  python3 fetch_checkin.py --date 2026-07-21 --json
"""
import os, sys, json, argparse, datetime as dt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "cs-daily", "lib"))
from common import load_env, VN  # noqa: E402
from render import shift_status  # noqa: E402


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

    win_start = day.replace(hour=0, minute=0, second=0, microsecond=0)
    win_end = win_start + dt.timedelta(days=1)
    start_date = win_start.strftime("%Y-%m-%d")
    end_date = win_end.strftime("%Y-%m-%d")

    env = load_env()
    late, miss_in, miss_out = shift_status(env, win_start, win_end, start_date, end_date)

    out = {
        "date": start_date,
        "late": [{"nick": n, "shift": t, "minutes": m} for n, t, m in
                 sorted(late, key=lambda x: -x[2])],
        "missCheckin": [{"nick": n, "shift": t} for n, t in miss_in],
        "missCheckout": [{"nick": n, "shift": t} for n, t in miss_out],
        "allOk": not (late or miss_in or miss_out),
    }

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"{out['date']}: late={len(late)} miss_in={len(miss_in)} "
              f"miss_out={len(miss_out)}")


if __name__ == "__main__":
    main()
