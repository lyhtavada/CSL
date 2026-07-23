"""Shared helpers for slack-personal scripts — all act AS Liz's own Slack account
(user token, not a bot), scoped to whatever Liz can already see/do herself.
"""
import json
import os
import urllib.parse
import urllib.request

ENV_PATH = "/Users/avada/CSL/.env"


def load_token():
    with open(ENV_PATH) as f:
        for line in f:
            if line.startswith("SLACK_USER_TOKEN="):
                token = line.strip().split("=", 1)[1]
                if not token:
                    raise SystemExit("SLACK_USER_TOKEN is empty in .env — paste the xoxp- token first.")
                return token
    raise SystemExit("SLACK_USER_TOKEN not found in .env")


def slack_call(method, params, http_method="GET"):
    token = load_token()
    url = f"https://slack.com/api/{method}"
    headers = {"Authorization": f"Bearer {token}"}

    if http_method == "GET":
        url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers=headers)
    else:
        headers["Content-Type"] = "application/json; charset=utf-8"
        req = urllib.request.Request(
            url, data=json.dumps(params).encode(), headers=headers, method="POST"
        )

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())

    if not data.get("ok"):
        raise SystemExit(f"Slack API error ({method}): {data.get('error')}")
    return data


def parse_slack_link(url):
    """Extract channel_id and message ts from a Slack message/thread URL.

    Handles both:
      https://avadaio.slack.com/archives/C0XXXXX/p1234567890123456
      https://avadaio.slack.com/archives/C0XXXXX/p1234567890123456?thread_ts=...
    """
    parts = urllib.parse.urlparse(url)
    segments = [s for s in parts.path.split("/") if s]
    if "archives" not in segments:
        raise SystemExit(f"Not a Slack archives link: {url}")
    idx = segments.index("archives")
    channel_id = segments[idx + 1]
    p_ts = segments[idx + 2]  # e.g. p1234567890123456
    if not p_ts.startswith("p"):
        raise SystemExit(f"Could not parse message ts from link: {url}")
    raw = p_ts[1:]
    ts = f"{raw[:-6]}.{raw[-6:]}"

    qs = urllib.parse.parse_qs(parts.query)
    thread_ts = qs.get("thread_ts", [None])[0] or ts
    return channel_id, ts, thread_ts
