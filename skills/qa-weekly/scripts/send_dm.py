#!/usr/bin/env python3
"""
Send QA weekly reports as Slack DMs via the Avada bot.

SAFETY: only sends what's in the approved payload file. Run ONLY after Liz
has reviewed. Supports --dry-run (default) — must pass --send to actually DM.

Payload file (JSON):
  {
    "week": "2026-W22",
    "sender": {                              // optional — DM appears as Liz
      "username": "Ly (Liz)",
      "icon_url": "https://avatars.slack-edge.com/.../512.png"
    },
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

# Slack truncates long `text` silently. Keep each chunk well under the limit
# and split at line boundaries so markdown/sentences don't break mid-way.
MAX_CHARS = 2800


def split_message(text, limit=MAX_CHARS):
    """Split a long message into <=limit-char chunks at line boundaries.

    Never breaks a line in the middle. A single line longer than `limit`
    (rare) is hard-split as a last resort.
    """
    if len(text) <= limit:
        return [text]
    chunks, cur = [], ""
    for line in text.split("\n"):
        # +1 for the newline we'll re-add
        if cur and len(cur) + 1 + len(line) > limit:
            chunks.append(cur)
            cur = ""
        if len(line) > limit:
            # single line too long — flush, then hard-split it
            if cur:
                chunks.append(cur)
                cur = ""
            for i in range(0, len(line), limit):
                chunks.append(line[i:i + limit])
            continue
        cur = line if not cur else cur + "\n" + line
    if cur:
        chunks.append(cur)
    return chunks


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


def _post_one(token, slack_id, text, sender=None):
    msg = {"channel": slack_id, "text": text,
           "unfurl_links": False, "unfurl_media": False}
    if sender:
        # Requires chat:write.customize scope (Avada bot has it).
        # Note: Slack still shows an APP badge next to the name — unavoidable.
        if sender.get("username"):
            msg["username"] = sender["username"]
        if sender.get("icon_url"):
            msg["icon_url"] = sender["icon_url"]
    body = json.dumps(msg).encode()
    req = urllib.request.Request(
        SLACK_API, data=body, method="POST",
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def post_dm(token, slack_id, text, sender=None):
    """Send a DM, splitting long text into multiple sequential messages.

    Returns the result of the LAST chunk (or the first failure). A long
    report is delivered as several DMs in order, each labelled (part N/M).
    """
    chunks = split_message(text)
    total = len(chunks)
    last = None
    for i, chunk in enumerate(chunks, 1):
        body = chunk if total == 1 else f"{chunk}\n\n_(phần {i}/{total})_"
        last = _post_one(token, slack_id, body, sender)
        if not last.get("ok"):
            return last  # stop on first failure
    return last


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
    sender = payload.get("sender")
    only = set(s.strip() for s in args.only.split(",")) if args.only else None

    mode = "SEND" if args.send else "DRY-RUN"
    as_who = sender.get("username") if sender else "avada_bot (default)"
    print(f"[{mode}] Week {payload.get('week')} — {len(msgs)} messages "
          f"— gửi dưới tên: {as_who}\n")

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
        nparts = len(split_message(m["text"]))
        if not args.send:
            parts_note = f" [{nparts} phần]" if nparts > 1 else ""
            print(f"  • {cs} → {sid}{parts_note}: {preview}…")
            sent += 1
            continue
        try:
            res = post_dm(token, sid, m["text"], sender)
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
