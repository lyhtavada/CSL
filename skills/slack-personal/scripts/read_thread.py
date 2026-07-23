#!/usr/bin/env python3
"""Read a Slack thread/channel/DM as Liz's own account (sees anything Liz can see,
including private DMs the Avada bot tokens cannot read).

Usage:
  python3 read_thread.py --link "https://avadaio.slack.com/archives/C0XXXXX/p1234567890123456"
  python3 read_thread.py --channel C0XXXXX --ts 1234567890.123456
  python3 read_thread.py --channel D0XXXXX --limit 50          # plain channel/DM history, no thread
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import slack_call, parse_slack_link


def fetch_user_names(user_ids):
    names = {}
    for uid in user_ids:
        try:
            data = slack_call("users.info", {"user": uid})
            profile = data["user"]
            names[uid] = profile.get("real_name") or profile.get("name") or uid
        except SystemExit:
            names[uid] = uid
    return names


def print_messages(messages):
    user_ids = sorted({m.get("user") for m in messages if m.get("user")})
    names = fetch_user_names(user_ids)
    for m in messages:
        who = names.get(m.get("user"), m.get("username", "?"))
        text = m.get("text", "")
        print(f"[{m.get('ts')}] {who}: {text}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--link", help="Slack message/thread URL")
    ap.add_argument("--channel", help="Channel or DM id (with --ts, or standalone for recent history)")
    ap.add_argument("--ts", help="Thread ts (use with --channel)")
    ap.add_argument("--limit", type=int, default=30, help="Messages to fetch when no thread ts given")
    args = ap.parse_args()

    if args.link:
        channel_id, _ts, thread_ts = parse_slack_link(args.link)
    elif args.channel and args.ts:
        channel_id, thread_ts = args.channel, args.ts
    elif args.channel:
        channel_id, thread_ts = args.channel, None
    else:
        print("Provide --link, or --channel [--ts]", file=sys.stderr)
        sys.exit(1)

    if thread_ts:
        data = slack_call("conversations.replies", {"channel": channel_id, "ts": thread_ts, "limit": 200})
    else:
        data = slack_call("conversations.history", {"channel": channel_id, "limit": args.limit})

    print_messages(data["messages"])


if __name__ == "__main__":
    main()
