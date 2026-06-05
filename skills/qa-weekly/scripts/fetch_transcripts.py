#!/usr/bin/env python3
"""
Fetch full chat transcripts from BigQuery for a list of session IDs and
write a clean, readable transcript file the grading subagent can read.

Usage:
  python3 fetch_transcripts.py --sessions-file /tmp/qa_weekly_sessions.json \
      --cs Hazel --out /tmp/qa_transcripts_Hazel.txt

  # or pass session ids directly (comma separated):
  python3 fetch_transcripts.py --session-ids session_a,session_b \
      --out /tmp/t.txt

Reads BQ service-account creds from CSL/.env (BQ_SA_CLIENT_EMAIL,
BQ_SA_PRIVATE_KEY). Table: avada-crm.avada_cs.crisp_chats (flat — one row per
message).
"""
import argparse
import json
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")  # silence py3.9 EOL / urllib3 noise

from google.cloud import bigquery
from google.oauth2 import service_account

TABLE = "avada-crm.avada_cs.crisp_chats"

# Segment tags meaning "this chat ALREADY has a review" → CS không cần xin nữa.
# Joy: review_yes_joy · Chatty (segment app_faqs/app_chatty, tên cũ FAQ app):
# review_yes_chatty / rv_yes_chatty / review_yes_faq. (Confirmed on BQ 2026-06-05.)
# KHÔNG tính g2_potential_review / video_potential — đó là *tiềm năng*, chưa review.
REVIEW_DONE_TAGS = (
    "review_yes_joy",
    "review_yes_chatty",
    "rv_yes_chatty",
    "review_yes_faq",
)


def review_status(segments):
    """'done' nếu chat đã có review (loại khỏi mẫu xin), else 'open'."""
    blob = " ".join(segments or []).lower() if isinstance(segments, list) \
        else str(segments or "").lower()
    return "done" if any(t in blob for t in REVIEW_DONE_TAGS) else "open"


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


def bq_client(env):
    key = (env.get("BQ_SA_PRIVATE_KEY") or "").replace("\\n", "\n")
    info = {
        "type": "service_account",
        "project_id": "avada-crm",
        "private_key": key,
        "client_email": env.get("BQ_SA_CLIENT_EMAIL"),
        "token_uri": "https://oauth2.googleapis.com/token",
    }
    creds = service_account.Credentials.from_service_account_info(info)
    return bigquery.Client(project="avada-crm", credentials=creds)


def fetch(client, session_ids):
    """Return {session_id: [msg, ...]} ordered by time."""
    q = f"""
    SELECT session_id, timestamp, fromType, type, content,
           userNickname, agentEmail, customerNickname, shopifyDomain,
           conversationState
    FROM `{TABLE}`
    WHERE session_id IN UNNEST(@sids)
      AND type IN ('text', 'note', 'file', 'picker', 'field')
    ORDER BY session_id, timestamp ASC
    """
    job = client.query(q, job_config=bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ArrayQueryParameter("sids", "STRING", session_ids)]))
    convs = {}
    for r in job:
        convs.setdefault(r["session_id"], []).append({
            "ts": str(r["timestamp"]),
            "from": r["fromType"],
            "content": r["content"] or "",
            "agent": r["agentEmail"],
            "nick": r["userNickname"],
            "customer": r["customerNickname"],
            "shop": r["shopifyDomain"],
            "state": r["conversationState"],
        })
    return convs


_IMG_JSON = re.compile(r'\{[^{}]*"(?:url|name|type)"\s*:[^{}]*\}')
_LONG_URL = re.compile(r'https?://storage\.crisp\.chat/\S+')
_ANY_LONG_URL = re.compile(r'https?://\S{60,}')


def clean_content(text):
    """Strip heavy junk the grader can't use: image/file JSON blobs and long
    storage URLs. Keeps the message readable, cuts ~25% of transcript size."""
    if not text:
        return text
    # image/file attachment messages → placeholder
    if _IMG_JSON.search(text):
        t = _IMG_JSON.sub("[hình ảnh/file]", text)
    else:
        t = text
    # bare crisp storage URLs → placeholder
    t = _LONG_URL.sub("[link ảnh]", t)
    # any other very long URL → trimmed (keep domain for context)
    t = _ANY_LONG_URL.sub(lambda m: m.group(0)[:50] + "…", t)
    return t.strip()


def render(convs, session_meta):
    """Render transcripts as readable text, numbered, with metadata header."""
    out = []
    for i, (sid, msgs) in enumerate(convs.items(), 1):
        meta = session_meta.get(sid, {})
        shop = (msgs[0]["shop"] if msgs else None) or meta.get("shopifyDomain", "?")
        state = msgs[0]["state"] if msgs else "?"
        out.append(f"\n{'='*70}")
        out.append(f"CHAT #{i}  |  session: {sid}")
        rv = meta.get("review_status", "open")
        rv_txt = ("ĐÃ CÓ review (không cần xin)" if rv == "done"
                  else "chưa có review")
        out.append(f"Shop: {shop}  |  State: {state}  |  "
                   f"App: {meta.get('app_seg','?')}  |  Review: {rv_txt}")
        out.append("=" * 70)
        for m in msgs:
            who = m["from"]
            if who == "operator":
                label = f"CS ({m['nick'] or m['agent'] or 'agent'})"
            elif who == "user":
                label = f"Customer ({m['customer'] or 'KH'})"
            else:
                label = who or "?"
            ts = m["ts"][11:19] if len(m["ts"]) > 19 else m["ts"]  # HH:MM:SS
            content = clean_content(m["content"].replace("\n", " ").strip())
            if content:
                out.append(f"[{ts}] {label}: {content}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions-file", help="output of fetch_sessions.py")
    ap.add_argument("--cs", help="CS nickname to pull from sessions-file")
    ap.add_argument("--session-ids", help="comma-separated session ids")
    ap.add_argument("--out", required=True)
    ap.add_argument("--env", default=os.path.join(
        os.path.dirname(__file__), "..", "..", "..", ".env"))
    args = ap.parse_args()

    env = load_env(args.env)
    session_ids, session_meta = [], {}

    if args.sessions_file and args.cs:
        data = json.load(open(args.sessions_file))
        cs = data["by_cs"].get(args.cs)
        if not cs:
            print(f"ERROR: CS '{args.cs}' not in sessions file", file=sys.stderr)
            sys.exit(1)
        for s in cs["sessions"]:
            sid = s["session_id"]
            session_ids.append(sid)
            segs = s.get("segments", [])
            app = "Joy" if any("joy" in x for x in segs) else (
                "Chatty" if any("chatty" in x for x in segs) else "?")
            session_meta[sid] = {"shopifyDomain": s.get("shopifyDomain"),
                                 "app_seg": app,
                                 "website_id": s.get("website_id"),
                                 "customerEmail": s.get("customerEmail")}
    elif args.session_ids:
        session_ids = [s.strip() for s in args.session_ids.split(",") if s.strip()]
    else:
        print("ERROR: need --sessions-file+--cs or --session-ids",
              file=sys.stderr)
        sys.exit(1)

    if not session_ids:
        print("ERROR: no session ids", file=sys.stderr)
        sys.exit(1)

    client = bq_client(env)
    convs = fetch(client, session_ids)
    # Preserve the sampled order even if BQ returns a subset
    ordered = {sid: convs[sid] for sid in session_ids if sid in convs}
    text = render(ordered, session_meta)

    header = (f"QA TRANSCRIPTS — CS: {args.cs or '(adhoc)'}\n"
              f"Sessions requested: {len(session_ids)} | "
              f"with messages: {len(ordered)}\n")
    with open(args.out, "w") as f:
        f.write(header + text)
    print(f"Wrote {len(ordered)}/{len(session_ids)} transcripts → {args.out}",
          file=sys.stderr)

    # Sidecar: chat index for the DM "Chat đã QA" links.
    # {chat_no, customer, crisp_url} — built in the same sampled order so
    # chat #N in the transcript matches chat #N here.
    index = []
    for i, sid in enumerate([s for s in session_ids if s in ordered], 1):
        msgs = ordered[sid]
        meta = session_meta.get(sid, {})
        # customer display: nickname > email > "Khách"
        cust = next((m["customer"] for m in msgs if m.get("customer")), None)
        wid = meta.get("website_id") or (
            "72a663b0-4cda-4e3b-8878-426bdd79364c")
        index.append({
            "chat_no": i,
            "session_id": sid,
            "customer": cust or meta.get("customerEmail") or "Khách",
            "crisp_url": f"https://app.crisp.chat/website/{wid}/inbox/{sid}",
        })
    idx_path = args.out.rsplit(".", 1)[0] + "_index.json"
    with open(idx_path, "w") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"Wrote chat index ({len(index)}) → {idx_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
