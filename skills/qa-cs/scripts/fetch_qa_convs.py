#!/usr/bin/env python3
"""
Fetch random conversations from Crisp for QA review.
Usage: python3 fetch_qa_convs.py --operator-id <ID> --month <YYYY-MM> --count 20
Output: /tmp/qa_convs_<operator_id>_<month>.json
"""

import argparse
import base64
import datetime
import json
import os
import random
import time
import requests
from pathlib import Path

# Load credentials
ENV_PATH = Path(__file__).parent.parent.parent.parent.parent / "crispchat" / ".env"
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

KEY = os.environ.get("CRISP_API_KEY", "60053ee7-54a7-4426-b0c7-66fc7eadee5a")
SECRET = os.environ.get("CRISP_API_SECRET", "72f3cd4146cea1ac60ab5164f5e143fc35e3bd6280313fb961527067f92c5e31")
WEBSITE_ID = "72a663b0-4cda-4e3b-8878-426bdd79364c"

auth = base64.b64encode(f"{KEY}:{SECRET}".encode()).decode()
HEADERS = {"Authorization": f"Basic {auth}", "X-Crisp-Tier": "plugin"}
TZ7 = datetime.timezone(datetime.timedelta(hours=7))


def get_month_range(month_str):
    """Return (start_ms, end_ms) for a YYYY-MM month in GMT+7."""
    year, month = map(int, month_str.split("-"))
    start = datetime.datetime(year, month, 1, 0, 0, 0, tzinfo=TZ7)
    if month == 12:
        end = datetime.datetime(year + 1, 1, 1, 0, 0, 0, tzinfo=TZ7)
    else:
        end = datetime.datetime(year, month + 1, 1, 0, 0, 0, tzinfo=TZ7)
    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)


def fetch_conversations(operator_id, start_ms, end_ms):
    """Fetch all conversations for operator in the given time range."""
    all_convs = []
    page = 1
    while page <= 20:
        r = requests.get(
            f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversations/{page}",
            headers=HEADERS,
            params={"filter_assigned_operator_id": operator_id}
        )
        convs = r.json().get("data", [])
        if not convs:
            break
        added = 0
        for c in convs:
            upd = c.get("updated_at", 0)
            if start_ms <= upd < end_ms:
                all_convs.append(c)
                added += 1
        if convs[-1].get("updated_at", 0) < start_ms:
            break
        page += 1
        time.sleep(0.3)
    return all_convs


def fetch_messages(session_id):
    """Fetch all messages for a conversation."""
    r = requests.get(
        f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversation/{session_id}/messages",
        headers=HEADERS
    )
    return r.json().get("data", [])


def format_messages(msgs):
    """Format messages for QA review."""
    result = []
    for m in sorted(msgs, key=lambda x: x.get("timestamp", 0)):
        ts = datetime.datetime.fromtimestamp(
            m.get("timestamp", 0) / 1000, tz=TZ7
        ).strftime("%Y-%m-%d %H:%M")
        frm = m.get("from", "?")
        content = m.get("content", "")
        if isinstance(content, dict):
            content = json.dumps(content, ensure_ascii=False)
        result.append({"time": ts, "from": frm, "content": str(content)[:500]})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--operator-id", required=True)
    parser.add_argument("--month", required=True, help="YYYY-MM")
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()

    start_ms, end_ms = get_month_range(args.month)
    print(f"Fetching conversations for {args.month}...")

    convs = fetch_conversations(args.operator_id, start_ms, end_ms)
    print(f"Found {len(convs)} conversations")

    # Random sample
    if len(convs) > args.count:
        sample = random.sample(convs, args.count)
    else:
        sample = convs
    print(f"Sampling {len(sample)} conversations for QA")

    # Fetch messages for each
    results = []
    for i, conv in enumerate(sample):
        sid = conv["session_id"]
        visitor = conv.get("meta", {}).get("nickname", "Unknown")
        email = conv.get("meta", {}).get("email", "")
        upd = datetime.datetime.fromtimestamp(
            conv.get("updated_at", 0) / 1000, tz=TZ7
        ).strftime("%Y-%m-%d %H:%M")

        msgs = fetch_messages(sid)
        formatted = format_messages(msgs)

        results.append({
            "index": i + 1,
            "session_id": sid,
            "visitor": visitor,
            "email": email,
            "updated_at": upd,
            "url": f"https://app.crisp.chat/website/{WEBSITE_ID}/inbox/{sid}/",
            "message_count": len(formatted),
            "messages": formatted
        })
        print(f"  [{i+1}/{len(sample)}] {visitor} — {len(formatted)} messages")
        time.sleep(0.2)

    # Save
    out_path = f"/tmp/qa_convs_{args.operator_id}_{args.month}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved to {out_path}")
    return out_path


if __name__ == "__main__":
    main()
