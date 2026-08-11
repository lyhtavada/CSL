#!/usr/bin/env python3
"""
Pull full Crisp transcripts for a set of chat links, so the daily brief can
say what each of Liz's tickets is actually about (section ④ = title +
description + a summary of how the chat went).

Same source and query as /read-crisp (BigQuery `avada_cs.crisp_chats`, not the
Crisp API — that caps at ~40 messages). Packaged as a script instead of
hand-written per run because the daily brief runs headless: one deterministic
command beats re-deriving BigQuery auth in a cron prompt every morning.

Takes chat links (or bare session ids) on argv or via --from-json, which reads
evaluate.py's output and pulls every chatLink under flags.lizTickets.

Usage:
  python3 fetch_chat_transcripts.py --from-json /tmp/eval.json --json
  python3 fetch_chat_transcripts.py "https://app.crisp.chat/.../session_abc..." --json
"""
import os, sys, re, json, argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load_env, bq_client  # noqa: E402

SESSION_RE = re.compile(r"(session_[0-9a-f\-]+)", re.I)

# Long chats blow up the brief's context for no gain — the tail is what says
# how the case actually ended up.
MAX_MSGS = 60
MAX_CHARS = 1200


def session_id(s):
    m = SESSION_RE.search(s or "")
    return m.group(1) if m else None


def fetch(client, ids):
    q = """
    SELECT session_id, timestamp, fromType, content, agentEmail,
           customerNickname, userNickname
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE session_id IN UNNEST(@ids)
    ORDER BY session_id, timestamp ASC
    """
    from google.cloud import bigquery
    job = bigquery.QueryJobConfig(query_parameters=[
        bigquery.ArrayQueryParameter("ids", "STRING", ids)])

    out = {i: [] for i in ids}
    for r in client.query(q, job_config=job).result():
        if r.fromType == "operator":
            who = r.userNickname or ("CS" if r.agentEmail else "Bot")
        else:
            who = r.customerNickname or "Merchant"
        out[r.session_id].append({
            "at": r.timestamp.isoformat() if r.timestamp else None,
            "from": r.fromType,
            "who": who,
            "isBot": r.fromType == "operator" and not r.agentEmail,
            "text": (r.content or "")[:MAX_CHARS],
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("links", nargs="*", help="chat links or session ids")
    ap.add_argument("--from-json", help="evaluate.py output — reads flags.lizTickets[].chatLink")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    raw = list(a.links)
    if a.from_json:
        with open(a.from_json) as f:
            ev = json.load(f)
        raw += [t.get("chatLink") for t in ev.get("flags", {}).get("lizTickets", [])]

    ids, seen = [], set()
    for s in raw:
        sid = session_id(s)
        if sid and sid not in seen:
            seen.add(sid)
            ids.append(sid)

    if not ids:
        print(json.dumps({"count": 0, "chats": {}}, ensure_ascii=False))
        return

    msgs = fetch(bq_client(load_env()), ids)
    chats = {}
    for sid in ids:
        m = msgs.get(sid, [])
        chats[sid] = {
            "sessionId": sid,
            "messageCount": len(m),
            "truncated": len(m) > MAX_MSGS,
            # Keep the tail — the outcome matters more than the greeting.
            "messages": m[-MAX_MSGS:],
        }

    out = {"count": len(chats), "chats": chats}
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        for sid, c in chats.items():
            print(f"{sid}: {c['messageCount']} msgs"
                  f"{' (truncated)' if c['truncated'] else ''}")


if __name__ == "__main__":
    main()
