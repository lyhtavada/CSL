#!/usr/bin/env python3
"""Add an emoji reaction to a message, as Liz's own account.

Usage:
  python3 react.py --link "https://avadaio.slack.com/archives/C0XXXXX/p1234567890123456" --emoji white_check_mark
  python3 react.py --channel C0XXXXX --ts 1234567890.123456 --emoji eyes
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import slack_call, parse_slack_link


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--link", help="Slack message URL")
    ap.add_argument("--channel", help="Channel id (use with --ts)")
    ap.add_argument("--ts", help="Message ts (use with --channel)")
    ap.add_argument("--emoji", required=True, help="Emoji name without colons, e.g. white_check_mark")
    args = ap.parse_args()

    if args.link:
        channel_id, ts, _thread_ts = parse_slack_link(args.link)
    elif args.channel and args.ts:
        channel_id, ts = args.channel, args.ts
    else:
        print("Provide --link, or --channel and --ts", file=sys.stderr)
        sys.exit(1)

    slack_call(
        "reactions.add",
        {"channel": channel_id, "timestamp": ts, "name": args.emoji},
        http_method="POST",
    )
    print(f"Reacted :{args.emoji}: on {channel_id} {ts}")


if __name__ == "__main__":
    main()
