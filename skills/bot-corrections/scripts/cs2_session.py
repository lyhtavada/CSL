#!/usr/bin/env python3
"""
cs2_session.py — thin client to pull a full conversation trace from CS v2, for
tracing WHY the bot answered a correction wrong (not just the isolated
question/original_response/corrected_response triplet from /api/corrections).

Route (confirmed 2026-08-21, probing cs2.avada.net):
  GET /api/obs/session/{session_id}
    -> {"conversation": {...session metadata...}, "messages": [
         {id, direction, content, trace, debug, escalation, by, received_at, ...}
       ]}

`trace` / `debug` / `escalation` per-message fields are the key signal for
telling a SYSTEM bug (retrieval picked wrong doc, tool call failed, router
sent to wrong flow, prompt/instruction bug) apart from a KB-content gap.
They are `null` on backfilled/imported messages but populated on real-time
agent turns.

Auth: same as kb_api.py / fetch_corrections.py — Authorization: Bearer
<CS2_API_TOKEN> + User-Agent, creds from ~/CSL/.env.

Usage:
  python3 cs2_session.py <session_id>          # pretty JSON to stdout
"""
import json
import os
import sys
import urllib.request

ENV_PATH = os.path.expanduser("~/CSL/.env")


def load_creds():
    url = token = None
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("CS2_API_URL="):
                    url = line.split("=", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("CS2_API_TOKEN="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        sys.exit(f"ERROR: {ENV_PATH} not found")
    if not url or not token:
        sys.exit("ERROR: CS2_API_URL / CS2_API_TOKEN missing in ~/CSL/.env")
    return url.rstrip("/"), token


def get_session(session_id, base=None, token=None):
    if base is None or token is None:
        base, token = load_creds()
    url = f"{base}/api/obs/session/{session_id}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "bot-corrections/1.0",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: cs2_session.py <session_id>")
    print(json.dumps(get_session(sys.argv[1]), indent=2, ensure_ascii=False))
