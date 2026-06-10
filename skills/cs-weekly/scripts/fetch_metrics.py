#!/usr/bin/env python3
"""
Pull weekly CS metrics for one app within an explicit date window:
  - tickets created   (Avada Ticket API)
  - DFY created       (subject startsWith [dfy])
  - chats             (BigQuery avada_cs.crisp_chats, by Crisp segment)

Window is INCLUSIVE [start, end] in local time (Asia/Bangkok, +07).

Usage:
  python3 fetch_metrics.py --app chatty --start 2026-06-01 --end 2026-06-07
  python3 fetch_metrics.py --app joy    --start 2026-06-01 --end 2026-06-07 --json

App → (Ticket appName, Crisp segments):
  chatty → "Chatty",       segments app_chatty + app_faqs
  joy    → "JOY Loyalty",  segment  app_joy
"""
import os, json, argparse, datetime
import requests
from dotenv import load_dotenv

ENV_PATH = "/Users/avada/CSL/.env"
TICKET_BASE = "https://avada-ts-a9cb0.web.app/api/external"

APP_CFG = {
    "chatty": {"ticket_app": "Chatty", "segments": ["app_chatty", "app_faqs"]},
    "joy":    {"ticket_app": "JOY Loyalty", "segments": ["app_joy"]},
}


def ticket_counts(app_name, start, end, key):
    r = requests.get(
        f"{TICKET_BASE}/tickets/by-date",
        headers={"X-API-Key": key},
        params={"startDate": start, "endDate": end, "appName": app_name},
        timeout=60,
    )
    r.raise_for_status()
    d = r.json().get("data", {})
    tks = d.get("tickets", [])
    total = d.get("total", len(tks))
    dfy = sum(1 for t in tks if t.get("subject", "").strip().lower().startswith("[dfy]"))
    return total, dfy


def chat_count(segments, start, end):
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
    client = bigquery.Client(project="avada-crm", credentials=creds)

    seg_clause = " OR ".join(f"segments LIKE @s{i}" for i in range(len(segments)))
    params = [
        bigquery.ScalarQueryParameter(f"s{i}", "STRING", f"%{s}%")
        for i, s in enumerate(segments)
    ]
    # end is inclusive → query strictly before end+1 day at 00:00 +07
    end_excl = (datetime.datetime.strptime(end, "%Y-%m-%d").date()
                + datetime.timedelta(days=1)).isoformat()
    sql = f"""
    SELECT COUNT(DISTINCT session_id) AS n
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE ({seg_clause})
      AND timestamp >= TIMESTAMP("{start} 00:00:00+07")
      AND timestamp <  TIMESTAMP("{end_excl} 00:00:00+07")
      AND type = 'text' AND content IS NOT NULL AND TRIM(content) != ''
    """
    job = bigquery.QueryJobConfig(query_parameters=params)
    return list(client.query(sql, job_config=job).result())[0].n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, choices=["chatty", "joy"])
    ap.add_argument("--start", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    load_dotenv(ENV_PATH)
    cfg = APP_CFG[a.app]
    key = os.environ["AVD_TICKET_API_KEY"]

    tickets, dfy = ticket_counts(cfg["ticket_app"], a.start, a.end, key)
    chats = chat_count(cfg["segments"], a.start, a.end)

    out = {
        "app": a.app,
        "start": a.start,
        "end": a.end,
        "tickets_created": tickets,
        "dfy_created": dfy,
        "chats": chats,
    }
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"{a.app} {a.start}–{a.end}: tickets={tickets} dfy={dfy} chats={chats}")


if __name__ == "__main__":
    main()
