#!/usr/bin/env python3
"""
Fetch random conversations from Crisp for QA review.
Usage: python3 fetch_crisp_convs.py --operator <operator_name> --month <YYYY-MM> --count <n>

Operators (Crisp name → user_id):
  Jade     (PhuongNT): 52215a15-bf11-43da-950c-558fc353f2fd
  Andy     (AnhBD):    faedcc02-a989-46e3-b480-6a353c3ae5f2
  Hazel    (HienPT):   7af44c09-37f2-4092-82ad-28a0aa0ba6c1
  Cody     (ChauHM):   c6a1cc08-b989-403a-8ed1-cb22ecf3ba80
  Mirra    (MinhBT):   561d38f8-7fd6-49c6-ab76-ffed1fb2dab8
  Phoebe   (PhuongTTM):b258e2c0-ed4d-4f2d-853d-f79f46364f5c
  Megan    (TrangNTH): 83ae9b4d-8ab5-481f-a9e1-dd5f3934ea94
  Hana     (HangHM):   (Joy - TBD)
  Audrey   (VanCT):    (Joy - TBD)
  Alyssa   (LyPK):     (Joy - TBD)
  Sonny    (HuyTC):    (Joy - TBD)
"""

import requests, base64, datetime, json, random, argparse, sys, time, os
from dotenv import dotenv_values

_env = dotenv_values(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
KEY = _env["CRISP_API_KEY"]
SECRET = _env["CRISP_API_SECRET"]
WEBSITE_ID = _env["CRISP_WEBSITE_RETENTION"]

OPERATORS = {
    "jade":   "52215a15-bf11-43da-950c-558fc353f2fd",
    "andy":   "faedcc02-a989-46e3-b480-6a353c3ae5f2",
    "hazel":  "7af44c09-37f2-4092-82ad-28a0aa0ba6c1",
    "cody":   "c6a1cc08-b989-403a-8ed1-cb22ecf3ba80",
    "mirra":  "561d38f8-7fd6-49c6-ab76-ffed1fb2dab8",
    "phoebe": "b258e2c0-ed4d-4f2d-853d-f79f46364f5c",
    "megan":  "83ae9b4d-8ab5-481f-a9e1-dd5f3934ea94",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--operator", required=True, help="Operator name (e.g. jade, andy)")
    parser.add_argument("--month", required=True, help="Month YYYY-MM (e.g. 2026-03)")
    parser.add_argument("--count", type=int, default=20, help="Number of conversations to sample")
    parser.add_argument("--output", default=None, help="Output JSON file path")
    args = parser.parse_args()

    op_name = args.operator.lower()
    if op_name not in OPERATORS:
        print(f"Unknown operator: {op_name}. Available: {', '.join(OPERATORS.keys())}")
        sys.exit(1)

    op_id = OPERATORS[op_name]
    year, month = map(int, args.month.split("-"))
    TZ7 = datetime.timezone(datetime.timedelta(hours=7))
    start_dt = datetime.datetime(year, month, 1, 0, 0, 0, tzinfo=TZ7)
    if month == 12:
        end_dt = datetime.datetime(year + 1, 1, 1, 0, 0, 0, tzinfo=TZ7)
    else:
        end_dt = datetime.datetime(year, month + 1, 1, 0, 0, 0, tzinfo=TZ7)

    start_ms = int(start_dt.timestamp() * 1000)
    end_ms = int(end_dt.timestamp() * 1000)
    print(f"Fetching {args.count} conversations for {op_name} in {args.month}...")

    auth = base64.b64encode(f"{KEY}:{SECRET}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}", "X-Crisp-Tier": "plugin"}

    all_convs = []
    page = 1
    while page <= 20:
        r = requests.get(
            f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversations/{page}",
            headers=headers,
            params={"filter_assigned_operator_id": op_id}
        )
        convs = r.json().get("data", [])
        if not convs:
            break
        for c in convs:
            upd = c.get("updated_at", 0)
            if start_ms <= upd < end_ms:
                all_convs.append(c)
        if convs[-1].get("updated_at", 0) < start_ms:
            break
        page += 1
        time.sleep(0.3)

    print(f"Found {len(all_convs)} conversations in {args.month}")

    if len(all_convs) <= args.count:
        sampled = all_convs
    else:
        sampled = random.sample(all_convs, args.count)

    # Fetch messages for each conversation
    results = []
    for i, conv in enumerate(sampled):
        sid = conv["session_id"]
        visitor = conv.get("meta", {}).get("nickname", "Unknown")
        r2 = requests.get(
            f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversation/{sid}/messages",
            headers=headers
        )
        msgs = r2.json().get("data", [])
        # Format messages
        formatted = []
        for m in sorted(msgs, key=lambda x: x.get("timestamp", 0)):
            ts = datetime.datetime.fromtimestamp(m.get("timestamp", 0)/1000, tz=TZ7)
            formatted.append({
                "time": ts.strftime("%H:%M"),
                "from": m.get("from", "?"),
                "type": m.get("type", "?"),
                "content": str(m.get("content", ""))[:500]
            })

        results.append({
            "index": i + 1,
            "session_id": sid,
            "visitor": visitor,
            "url": f"https://app.crisp.chat/website/{WEBSITE_ID}/inbox/{sid}/",
            "updated_at": conv.get("updated_at"),
            "messages": formatted
        })
        time.sleep(0.2)
        if (i + 1) % 5 == 0:
            print(f"  Fetched {i+1}/{len(sampled)} conversations...")

    output = {
        "operator": op_name,
        "month": args.month,
        "total_in_month": len(all_convs),
        "sampled": len(results),
        "conversations": results
    }

    outfile = args.output or f"qa_{op_name}_{args.month}.json"
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nSaved to {outfile}")
    print(f"Total conversations in month: {len(all_convs)}")
    print(f"Sampled: {len(results)}")

if __name__ == "__main__":
    main()
