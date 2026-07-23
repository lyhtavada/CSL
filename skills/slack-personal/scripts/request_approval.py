#!/usr/bin/env python3
"""Post a draft message into Liz's own "Saved Messages" self-DM for approval,
before actually sending it anywhere as her account.

Flow:
  1. request_approval.py --channel <target> --text "..." [--thread-ts ...]
     -> posts the draft into Liz's self-DM, prints the approval ts
  2. Liz reviews in Slack, reacts with :white_check_mark: on that draft message
  3. check_approval.py --ts <approval_ts>  -> confirms she approved
  4. send_message.py ... --send            -> actually posts to the real target

Usage:
  python3 request_approval.py --channel C0XXXXX --text "..." [--thread-ts 169...]
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import slack_call, find_self_dm_channel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", required=True, help="Real target channel/DM id the message would go to")
    ap.add_argument("--thread-ts", help="Real target thread ts, if replying in-thread")
    ap.add_argument("--text", required=True, help="Draft message text")
    args = ap.parse_args()

    self_dm = find_self_dm_channel()

    preview = (
        f":memo: *Draft to review* — target: `{args.channel}`"
        + (f" (thread `{args.thread_ts}`)" if args.thread_ts else "")
        + f"\n\n{args.text}\n\n_React :white_check_mark: here to approve sending as-is._"
    )

    data = slack_call("chat.postMessage", {"channel": self_dm, "text": preview}, http_method="POST")
    print(f"Posted draft to self-DM ({self_dm}). approval_ts={data['ts']}")
    print("Waiting for Liz to react ✅ on that message in Slack, then run check_approval.py")


if __name__ == "__main__":
    main()
