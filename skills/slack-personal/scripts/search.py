#!/usr/bin/env python3
"""Search across everything Liz's Slack account can see (channels/DMs/groups),
using search:read scope. Bot tokens cannot do this — no search scope granted.

Usage:
  python3 search.py "refund policy" --count 20
  python3 search.py "from:@someone keyword"     # Slack search modifiers work
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import slack_call


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--count", type=int, default=20)
    args = ap.parse_args()

    data = slack_call("search.messages", {"query": args.query, "count": args.count})
    matches = data["messages"]["matches"]

    if not matches:
        print("No results.")
        return

    for m in matches:
        channel = m.get("channel", {}).get("name", m.get("channel", {}).get("id", "?"))
        user = m.get("username") or m.get("user", "?")
        print(f"[#{channel}] {user}: {m.get('text')}")
        print(f"  {m.get('permalink')}\n")


if __name__ == "__main__":
    main()
