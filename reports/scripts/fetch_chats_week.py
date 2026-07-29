#!/usr/bin/env python3
"""
Weekly "real conversation" chat count (Chatty + Joy) for the CEO Weekly report,
using the SAME counting logic as /cs-weekly (skills/_shared/chat_count.py) —
so the number here always matches the per-app CS Weekly Notion report, instead
of being regex-parsed back out of that report's text.

Usage:
  python3 fetch_chats_week.py --start 2026-07-20 --end 2026-07-26 [--out /tmp/chats.json]

Output JSON: {"chatty": N, "joy": N}
"""
import argparse, json, os, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT / "skills" / "_shared"))
from chat_count import chat_count, APP_SEGMENTS  # noqa: E402


def load_env():
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")


def bq_client():
    from google.oauth2 import service_account
    from google.cloud import bigquery

    env = os.environ
    creds = service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "project_id": "avada-crm",
            "private_key_id": env["BQ_SA_PRIVATE_KEY_ID"],
            "private_key": env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n"),
            "client_email": env["BQ_SA_CLIENT_EMAIL"],
            "token_uri": "https://oauth2.googleapis.com/token",
        },
        scopes=["https://www.googleapis.com/auth/bigquery"],
    )
    return bigquery.Client(project="avada-crm", credentials=creds)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD (Monday)")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD (Sunday)")
    ap.add_argument("--out")
    a = ap.parse_args()

    load_env()
    client = bq_client()
    result = {app: chat_count(client, APP_SEGMENTS[app], a.start, a.end)
              for app in ("chatty", "joy")}

    blob = json.dumps(result, ensure_ascii=False, indent=2)
    if a.out:
        with open(a.out, "w") as f:
            f.write(blob)
        print(f"Wrote {a.out}", file=sys.stderr)
    else:
        print(blob)


if __name__ == "__main__":
    main()
