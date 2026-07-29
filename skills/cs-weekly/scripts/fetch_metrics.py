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
import os, sys, json, argparse, datetime
import requests
from dotenv import load_dotenv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_shared"))
from chat_count import chat_count as _chat_count, APP_SEGMENTS  # noqa: E402

ENV_PATH = "/Users/avada/CSL/.env"
TICKET_BASE = "https://avada-ts-a9cb0.web.app/api/external"

APP_CFG = {
    "chatty": {"ticket_app": "Chatty", "segments": APP_SEGMENTS["chatty"]},
    "joy":    {"ticket_app": "JOY Loyalty", "segments": APP_SEGMENTS["joy"]},
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


# "Real conversation" counting logic (merchant-anchored, >=2 msgs, internal
# traffic excluded, boundary-safe) lives in skills/_shared/chat_count.py — shared
# with the ad-hoc /count-chats skill so both stay in sync. See that module's
# docstring for the full rationale and validation numbers.
def _bq_client():
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


def chat_count(segments, start, end):
    return _chat_count(_bq_client(), segments, start, end)


def metrics_for(cfg, start, end, key):
    tickets, dfy = ticket_counts(cfg["ticket_app"], start, end, key)
    chats = chat_count(cfg["segments"], start, end)
    return {"start": start, "end": end,
            "tickets_created": tickets, "dfy_created": dfy, "chats": chats}


def prev_week(start, end):
    """The Mon→Sun window immediately before [start, end]."""
    d = datetime.timedelta(days=7)
    s = (datetime.datetime.strptime(start, "%Y-%m-%d").date() - d).isoformat()
    e = (datetime.datetime.strptime(end, "%Y-%m-%d").date() - d).isoformat()
    return s, e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, choices=["chatty", "joy"])
    ap.add_argument("--start", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--compare", action="store_true",
                    help="also pull the prior Mon→Sun week for ▲▼ comparison")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    load_dotenv(ENV_PATH)
    cfg = APP_CFG[a.app]
    key = os.environ["AVD_TICKET_API_KEY"]

    this = metrics_for(cfg, a.start, a.end, key)
    out = {"app": a.app, "this_week": this}

    if a.compare:
        ps, pe = prev_week(a.start, a.end)
        out["prev_week"] = metrics_for(cfg, ps, pe, key)

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        t = this
        print(f"{a.app} {t['start']}–{t['end']}: "
              f"tickets={t['tickets_created']} dfy={t['dfy_created']} chats={t['chats']}")
        if a.compare:
            p = out["prev_week"]
            print(f"  prev {p['start']}–{p['end']}: "
                  f"tickets={p['tickets_created']} dfy={p['dfy_created']} chats={p['chats']}")


if __name__ == "__main__":
    main()
