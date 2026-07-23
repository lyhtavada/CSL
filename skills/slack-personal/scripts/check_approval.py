#!/usr/bin/env python3
"""Check whether Liz approved a draft posted by request_approval.py, by looking
for a white_check_mark reaction (from Liz herself) on that message in her self-DM.

Usage:
  python3 check_approval.py --ts 1690000000.123456
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import slack_call, find_self_dm_channel, SELF_USER_ID


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ts", required=True, help="approval_ts printed by request_approval.py")
    args = ap.parse_args()

    self_dm = find_self_dm_channel()
    data = slack_call("reactions.get", {"channel": self_dm, "timestamp": args.ts})
    reactions = data.get("message", {}).get("reactions", [])

    approved = any(
        r["name"] in ("white_check_mark", "heavy_check_mark", "+1")
        and SELF_USER_ID in r.get("users", [])
        for r in reactions
    )

    print("APPROVED" if approved else "NOT YET APPROVED")
    sys.exit(0 if approved else 1)


if __name__ == "__main__":
    main()
