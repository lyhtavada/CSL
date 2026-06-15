#!/usr/bin/env python3
"""
Pull the full list of tickets created for one app within a date window, so the
weekly bulletin can cluster TOP ISSUES from tickets (not from chats).

Returns each ticket's subject + description + priority + status so the caller can
read the asks and cluster them into 3-5 themes. [dfy] tickets are EXCLUDED by
default (they already have their own row in §2; they are not support issues).

Window is INCLUSIVE [start, end] in local time (Asia/Bangkok, +07).

Usage:
  python3 fetch_tickets.py --app chatty --start 2026-06-01 --end 2026-06-07 --json
  python3 fetch_tickets.py --app joy    --start 2026-06-01 --end 2026-06-07 --include-dfy --json

App → Ticket appName:
  chatty → "Chatty"
  joy    → "JOY Loyalty"
"""
import os, json, argparse
import requests
from dotenv import load_dotenv

ENV_PATH = "/Users/avada/CSL/.env"
TICKET_BASE = "https://avada-ts-a9cb0.web.app/api/external"

APP_CFG = {
    "chatty": {"ticket_app": "Chatty"},
    "joy":    {"ticket_app": "JOY Loyalty"},
}


def fetch_tickets(app_name, start, end, key):
    r = requests.get(
        f"{TICKET_BASE}/tickets/by-date",
        headers={"X-API-Key": key},
        params={"startDate": start, "endDate": end, "appName": app_name},
        timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", {}).get("tickets", [])


def slim(t):
    """Keep only the fields needed to read + cluster an issue."""
    return {
        "subject": (t.get("subject") or "").strip(),
        "description": (t.get("description") or "").strip(),
        "priority": t.get("priority"),
        "status": t.get("ticketStatus"),
        "ticketNumber": t.get("ticketNumber"),
        "shortUrl": t.get("shortUrl"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, choices=["chatty", "joy"])
    ap.add_argument("--start", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--include-dfy", action="store_true",
                    help="keep [dfy] tickets (default: excluded)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    load_dotenv(ENV_PATH)
    key = os.environ["AVD_TICKET_API_KEY"]

    tks = fetch_tickets(APP_CFG[a.app]["ticket_app"], a.start, a.end, key)
    if not a.include_dfy:
        tks = [t for t in tks
               if not (t.get("subject", "").strip().lower().startswith("[dfy]"))]
    rows = [slim(t) for t in tks]

    out = {"app": a.app, "start": a.start, "end": a.end,
           "count": len(rows), "tickets": rows}

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"{a.app} {a.start}–{a.end}: {len(rows)} tickets (dfy excluded={not a.include_dfy})")
        for r in rows:
            print(f"  #{r['ticketNumber']} [{r['priority']}] {r['subject']}")


if __name__ == "__main__":
    main()
