"""Shared helpers for slack-personal scripts — all act AS Liz's own Slack account
(user token, not a bot), scoped to whatever Liz can already see/do herself.
"""
import json
import os
import urllib.parse
import urllib.request

ENV_PATH = "/Users/avada/CSL/.env"
SELF_USER_ID = "U02GT4PC6RH"  # Liz's own Slack user id (from auth.test)


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


SELF_DM_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".self_dm_cache")


def find_self_dm_channel():
    """Find Liz's own "Saved Messages" DM channel id, caching it locally since
    it requires paginating through every im channel (~280+) to find.
    """
    if os.path.exists(SELF_DM_CACHE):
        with open(SELF_DM_CACHE) as f:
            cached = f.read().strip()
            if cached:
                return cached

    cursor = None
    found = None
    while True:
        params = {"types": "im", "limit": 200}
        if cursor:
            params["cursor"] = cursor
        data = slack_call("conversations.list", params)
        for c in data["channels"]:
            if c.get("user") == SELF_USER_ID:
                found = c["id"]
                break
        if found:
            break
        cursor = data.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    if not found:
        raise SystemExit("Could not find self-DM channel for Liz's account")

    with open(SELF_DM_CACHE, "w") as f:
        f.write(found)
    return found


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
