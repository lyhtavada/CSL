#!/usr/bin/env python3
"""
Send QA weekly reports as Slack DMs via the Avada bot.

SAFETY: only sends what's in the approved payload file. Run ONLY after Liz
has reviewed. Supports --dry-run (default) — must pass --send to actually DM.

Payload file (JSON):
  {
    "week": "2026-W22",
    "messages": [
      {"cs": "Hazel", "slack_id": "U09FYACFH2T",
       "text": "*QA Tuần W22 — Hazel* ...markdown..."},
      ...
    ]
  }

Usage:
  python3 send_dm.py --payload /tmp/qa_dm_payload.json            # dry-run
  python3 send_dm.py --payload /tmp/qa_dm_payload.json --send     # real send
  python3 send_dm.py --payload ... --send --only Hazel,Andy       # subset
"""
import argparse
import json
import os
import sys
import urllib.request

SLACK_API = "https://slack.com/api/chat.postMessage"


def load_env(path):
    env = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def post_dm(token, slack_id, text):
    body = json.dumps({"channel": slack_id, "text": text,
                       "unfurl_links": False, "unfurl_media": False}).encode()
    req = urllib.request.Request(
        SLACK_API, data=body, method="POST",
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--payload", required=True)
    ap.add_argument("--send", action="store_true",
                    help="actually send (default is dry-run)")
    ap.add_argument("--only", help="comma-separated CS names to send to")
    ap.add_argument("--env", default=os.path.join(
        os.path.dirname(__file__), "..", "..", "..", ".env"))
    args = ap.parse_args()

    env = load_env(args.env)
    token = env.get("SLACK_BOT_TOKEN_AVADA") or os.environ.get(
        "SLACK_BOT_TOKEN_AVADA")
    if not token:
        print("ERROR: SLACK_BOT_TOKEN_AVADA not found", file=sys.stderr)
        sys.exit(1)

    payload = json.load(open(args.payload))
    msgs = payload.get("messages", [])
    only = set(s.strip() for s in args.only.split(",")) if args.only else None

    mode = "SEND" if args.send else "DRY-RUN"
    print(f"[{mode}] Week {payload.get('week')} — {len(msgs)} messages\n")

    sent, skipped, failed = 0, 0, 0
    for m in msgs:
        cs = m.get("cs")
        sid = m.get("slack_id")
        if only and cs not in only:
            skipped += 1
            continue
        if not sid or not sid.startswith("U"):
            print(f"  ✗ {cs}: invalid slack_id ({sid}) — SKIP")
            failed += 1
            continue
        preview = m["text"].split("\n")[0][:70]
        if not args.send:
            print(f"  • {cs} → {sid}: {preview}…")
            sent += 1
            continue
        try:
            res = post_dm(token, sid, m["text"])
            if res.get("ok"):
                print(f"  ✓ {cs} → DM sent ({res.get('channel')})")
                sent += 1
            else:
                print(f"  ✗ {cs}: Slack error — {res.get('error')}")
                failed += 1
        except Exception as e:
            print(f"  ✗ {cs}: {e}")
            failed += 1

    print(f"\n{mode} done — {sent} sent, {skipped} skipped, {failed} failed")
    if not args.send:
        print("\n(dry-run — pass --send to actually deliver)")


if __name__ == "__main__":
    main()
