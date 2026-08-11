#!/usr/bin/env python3
"""
Send Slack messages (DM or channel) via the Avada bot. Originally built for
QA weekly DMs; also reused by /cs-daily-brief to post to a channel.

SAFETY: only sends what's in the approved payload file. Run ONLY after Liz
has reviewed. Supports --dry-run (default) — must pass --send to actually DM.

Payload file (JSON):
  {
    "week": "2026-W22",
    "sender": {                              // optional — post appears as Liz
      "username": "Ly (Liz)",
      "icon_url": "https://avatars.slack-edge.com/.../512.png"
    },
    "messages": [
      {"cs": "Hazel", "slack_id": "U09FYACFH2T",              // DM: user id (U...)
       "text": "*QA Tuần W22 — Hazel* ...markdown..."},
      {"cs": "cs-2-daily", "slack_id": "C0B8042TXQ9",         // or a channel id (C...)
       "text": "..."},
      {"cs": "cs-2-daily-detail", "slack_id": "C0B8042TXQ9",  // reply in a thread
       "thread_ts": "1754899200.123456", "text": "..."},
      ...
    ]
  }

`--out <path>` writes the send results as JSON — [{cs, ok, ts, channel,
error}] — so a caller can grab the parent message's `ts` and post a follow-up
into its thread (used by /cs-daily-brief to hang the full report off the
short summary). `ts` is the FIRST chunk's timestamp when a long message gets
split, so the thread always hangs off the top of the message.

Usage:
  python3 send_dm.py --payload /tmp/qa_dm_payload.json            # dry-run
  python3 send_dm.py --payload /tmp/qa_dm_payload.json --send     # real send
  python3 send_dm.py --payload ... --send --only Hazel,Andy       # subset
  python3 send_dm.py --payload ... --send --out /tmp/result.json  # capture ts
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


def _post_one(token, slack_id, text, sender=None, thread_ts=None):
    msg = {"channel": slack_id, "text": text,
           "unfurl_links": False, "unfurl_media": False}
    if thread_ts:
        msg["thread_ts"] = thread_ts
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


def post_dm(token, slack_id, text, sender=None, thread_ts=None):
    """Send a DM, splitting long text into multiple sequential messages.

    Returns the result of the LAST chunk (or the first failure), with
    `_first_ts` added — the ts of the FIRST chunk, which is the one a thread
    should hang off when a long message got split. A long report is delivered
    as several DMs in order, each labelled (part N/M).
    """
    chunks = split_message(text)
    total = len(chunks)
    last, first_ts = None, None
    for i, chunk in enumerate(chunks, 1):
        body = chunk if total == 1 else f"{chunk}\n\n_(phần {i}/{total})_"
        last = _post_one(token, slack_id, body, sender, thread_ts)
        if not last.get("ok"):
            return last  # stop on first failure
        if first_ts is None:
            first_ts = last.get("ts")
    if last is not None:
        last["_first_ts"] = first_ts
    return last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--payload", required=True)
    ap.add_argument("--send", action="store_true",
                    help="actually send (default is dry-run)")
    ap.add_argument("--only", help="comma-separated CS names to send to")
    ap.add_argument("--out", help="write send results (incl. message ts) as JSON")
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
    results = []
    for m in msgs:
        cs = m.get("cs")
        sid = m.get("slack_id")
        thread_ts = m.get("thread_ts")
        if only and cs not in only:
            skipped += 1
            continue
        if not sid or not sid.startswith(("U", "C")):
            print(f"  ✗ {cs}: invalid slack_id ({sid}) — SKIP")
            results.append({"cs": cs, "ok": False, "error": f"invalid slack_id {sid}"})
            failed += 1
            continue
        preview = m["text"].split("\n")[0][:70]
        nparts = len(split_message(m["text"]))
        if not args.send:
            parts_note = f" [{nparts} phần]" if nparts > 1 else ""
            thread_note = " [thread reply]" if thread_ts else ""
            print(f"  • {cs} → {sid}{parts_note}{thread_note}: {preview}…")
            results.append({"cs": cs, "ok": True, "dryRun": True})
            sent += 1
            continue
        try:
            res = post_dm(token, sid, m["text"], sender, thread_ts)
            if res.get("ok"):
                ts = res.get("_first_ts") or res.get("ts")
                where = "thread" if thread_ts else "DM"
                print(f"  ✓ {cs} → {where} sent ({res.get('channel')}) ts={ts}")
                results.append({"cs": cs, "ok": True, "ts": ts,
                                "channel": res.get("channel")})
                sent += 1
            else:
                print(f"  ✗ {cs}: Slack error — {res.get('error')}")
                results.append({"cs": cs, "ok": False, "error": res.get("error")})
                failed += 1
        except Exception as e:
            print(f"  ✗ {cs}: {e}")
            results.append({"cs": cs, "ok": False, "error": str(e)})
            failed += 1

    if args.out:
        with open(args.out, "w") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nresults → {args.out}")

    print(f"\n{mode} done — {sent} sent, {skipped} skipped, {failed} failed")
    if not args.send:
        print("\n(dry-run — pass --send to actually deliver)")


if __name__ == "__main__":
    main()
