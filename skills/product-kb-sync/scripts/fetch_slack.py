#!/usr/bin/env python3
"""
fetch_slack.py — pull new messages from the shared product-release channel
since this app's last processed ts, using Liz's own Slack account (reuses
slack-personal's _common.py — same auth, same account).

Usage:
  python3 fetch_slack.py <app>              # since state's last_slack_ts
  python3 fetch_slack.py <app> --limit 20    # bounded fallback when last_slack_ts is null (first run)

Does NOT update state — caller updates state only after the diff step
actually completes, so a crash mid-run doesn't silently drop a week's posts.
Prints JSON: {messages: [{ts, user, text}], latest_ts: "..."}
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "..", "..", "slack-personal", "scripts"))
from _common import slack_call

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
import state


def fetch_since(channel_id, since_ts, limit):
    params = {"channel": channel_id, "limit": limit}
    if since_ts:
        params["oldest"] = since_ts
    data = slack_call("conversations.history", params)
    # Slack returns newest-first; oldest excludes the `since_ts` message itself.
    return list(reversed(data["messages"]))


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: fetch_slack.py <app> [--limit N]")
    app = sys.argv[1].lower()
    if app not in config.APPS:
        sys.exit(f"unknown app '{app}' (use: {', '.join(config.APPS)})")

    limit = 20
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    app_state = state.get_app_state(app)
    since_ts = app_state.get("last_slack_ts")

    messages = fetch_since(config.RELEASE_CHANNEL_ID, since_ts, limit)

    out = {
        "app": app,
        "channel": config.RELEASE_CHANNEL_ID,
        "since_ts": since_ts,
        "messages": [{"ts": m.get("ts"), "user": m.get("user"), "text": m.get("text", "")} for m in messages],
        "latest_ts": messages[-1]["ts"] if messages else since_ts,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
