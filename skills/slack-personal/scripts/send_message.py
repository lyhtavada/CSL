#!/usr/bin/env python3
"""Send a message AS Liz's real Slack account into a channel/DM she is already a
member of. There is no im:write scope on this token, so it CANNOT open a brand
new DM with someone Liz has never messaged — only post into existing channels/DMs.

SAFETY: dry-run by default. Liz must review the rendered text before --send.

Usage:
  python3 send_message.py --channel C0XXXXX --text "..." [--thread-ts 169...]      # dry-run
  python3 send_message.py --channel C0XXXXX --text "..." --send
  python3 send_message.py --link "https://avadaio.slack.com/archives/C0XXXXX/p..." --text "..." --send
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import slack_call, parse_slack_link


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", help="Channel or DM id")
    ap.add_argument("--link", help="Slack link to reply in-thread instead of --channel/--thread-ts")
    ap.add_argument("--thread-ts", help="Reply in this thread (optional)")
    ap.add_argument("--text", required=True, help="Message text (Slack mrkdwn)")
    ap.add_argument("--send", action="store_true", help="Actually send. Omit for dry-run preview.")
    args = ap.parse_args()

    channel_id = args.channel
    thread_ts = args.thread_ts
    if args.link:
        channel_id, _ts, thread_ts = parse_slack_link(args.link)

    if not channel_id:
        print("Provide --channel or --link", file=sys.stderr)
        sys.exit(1)

    print("--- DRY RUN PREVIEW ---" if not args.send else "--- SENDING ---")
    print(f"channel: {channel_id}")
    if thread_ts:
        print(f"thread_ts: {thread_ts}")
    print(f"text:\n{args.text}")

    if not args.send:
        print("\n(dry-run — pass --send to actually post as Liz)")
        return

    payload = {"channel": channel_id, "text": args.text}
    if thread_ts:
        payload["thread_ts"] = thread_ts

    data = slack_call("chat.postMessage", payload, http_method="POST")
    print(f"\nSent. ts={data['ts']}")


if __name__ == "__main__":
    main()
