#!/usr/bin/env python3
"""
Fetch real Crisp chat conversations from BigQuery for FAQ mining.

Usage:
  python3 fetch_chats.py --segment app_joy --days 7 --output /tmp/joy_convs.json
  # Chatty spans two segments — pass both (comma-separated), they are OR'd:
  python3 fetch_chats.py --segment app_chatty,app_faqs --days 7 --output /tmp/chatty_convs.json

Output JSON: list of {session_id, messages: [{role, text}]} ordered by recency.
A session matching multiple segments is returned once (grouped by session_id).
Credentials are loaded from /Users/avada/CSL/.env (BQ_SA_* vars).

Notes:
- The MCP BigQuery tool CANNOT query avada_cs.crisp_chats directly (app-scoped).
  This script uses the churn-prediction service account with full bigquery scope.
- 'role' is normalized: fromType='user' -> 'Customer', else -> 'Agent'.
"""

import argparse, json, sys, warnings
warnings.filterwarnings("ignore")

from dotenv import dotenv_values
from google.oauth2 import service_account
from google.cloud import bigquery

ENV_PATH = "/Users/avada/CSL/.env"


def get_client():
    env = dotenv_values(ENV_PATH)
    key_data = {
        "type": "service_account",
        "project_id": "avada-crm",
        "private_key_id": env["BQ_SA_PRIVATE_KEY_ID"],
        "private_key": env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n"),
        "client_email": env["BQ_SA_CLIENT_EMAIL"],
        "token_uri": "https://oauth2.googleapis.com/token",
    }
    credentials = service_account.Credentials.from_service_account_info(
        key_data,
        scopes=[
            "https://www.googleapis.com/auth/bigquery",
            "https://www.googleapis.com/auth/cloud-platform",
        ],
    )
    return bigquery.Client(project="avada-crm", credentials=credentials)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--segment", required=True, help="Crisp segment(s), comma-separated. e.g. app_joy OR app_chatty,app_faqs")
    p.add_argument("--days", type=int, default=7, help="Look-back window in days (default 7)")
    p.add_argument("--output", required=True, help="Output JSON path")
    p.add_argument("--min-len", type=int, default=2, help="Drop messages shorter than this many chars")
    args = p.parse_args()

    client = get_client()

    segments = [s.strip() for s in args.segment.split(",") if s.strip()]
    # OR the segments together: a session in ANY of them qualifies.
    seg_clause = " OR ".join(f"segments LIKE @seg{i}" for i in range(len(segments)))
    params = [bigquery.ScalarQueryParameter("days", "INT64", args.days)]
    for i, seg in enumerate(segments):
        params.append(bigquery.ScalarQueryParameter(f"seg{i}", "STRING", f"%{seg}%"))

    sql = f"""
    SELECT
      session_id,
      ARRAY_AGG(STRUCT(timestamp, fromType, content) ORDER BY timestamp) AS messages
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE ({seg_clause})
      AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL @days DAY)
      AND type = 'text'
      AND content IS NOT NULL
      AND TRIM(content) != ''
    GROUP BY session_id
    ORDER BY MIN(timestamp) DESC
    """
    job_config = bigquery.QueryJobConfig(query_parameters=params)

    rows = list(client.query(sql, job_config=job_config).result())

    conversations = []
    total_msgs = 0
    for row in rows:
        msgs = []
        for m in row.messages:
            role = "Customer" if m["fromType"] == "user" else "Agent"
            text = str(m["content"]).strip()
            if text and len(text) > args.min_len:
                msgs.append({"role": role, "text": text})
        if msgs:
            conversations.append({"session_id": row.session_id, "messages": msgs})
            total_msgs += len(msgs)

    with open(args.output, "w") as f:
        json.dump(conversations, f, ensure_ascii=False, indent=2, default=str)

    user_msgs = sum(
        1 for c in conversations for m in c["messages"] if m["role"] == "Customer"
    )
    print(f"Segment(s):     {', '.join(segments)}")
    print(f"Window:         last {args.days} days")
    print(f"Sessions:       {len(conversations)}")
    print(f"Total messages: {total_msgs}")
    print(f"Customer msgs:  {user_msgs}")
    print(f"Saved to:       {args.output}")


if __name__ == "__main__":
    main()
