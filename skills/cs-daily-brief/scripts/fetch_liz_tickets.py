#!/usr/bin/env python3
"""
Tickets created for Liz (she's in members[]) in a rolling 24h window, 08:30
VN to 08:30 VN the next day (aligned to the 08:45 cron run), across all 3
apps — for the daily CS report.

Matches any member whose displayName contains "liz" (case-insensitive) —
covers both "Liz" and "liz_avada" name variants seen live in the API.

Default target day = yesterday (VN).

Usage:
  python3 fetch_liz_tickets.py --json                # yesterday 08:30 -> today 08:30 (VN)
  python3 fetch_liz_tickets.py --date 2026-07-21 --json
"""
import os, json, argparse, datetime as dt
import requests
from dotenv import load_dotenv

ENV_PATH = "/Users/avada/CSL/.env"
TICKET_BASE = "https://avada-ts-a9cb0.web.app/api/external"
VN = dt.timezone(dt.timedelta(hours=7))

APPS = {
    "chatty": "Chatty",
    "joy": "JOY Loyalty",
    "wishlist": "Wishlist",
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


def is_liz(members):
    return any("liz" in (m.get("displayName") or "").lower() for m in members)


def slim(t, app_key):
    return {
        "app": app_key,
        "ticketNumber": t.get("ticketNumber"),
        "subject": (t.get("subject") or "").strip()[:200],
        # Full description — the daily brief summarises each of Liz's tickets
        # from title + description + the chat itself, so keep it untruncated
        # (AI-created tickets carry a well-structured problem/store/plan blob).
        "description": (t.get("description") or "").strip(),
        "priority": t.get("priority"),
        "tsStatus": t.get("tsStatus"),
        "ticketStatus": t.get("ticketStatus"),
        "createdAt": t.get("createdAt"),
        "store": (t.get("store") or [{}])[0].get("domain"),
        "ticketUrl": "https://avada-ts-a9cb0.web.app" + t["shortUrl"] if t.get("shortUrl") else None,
        "chatLink": t.get("chatLink"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYY-MM-DD (VN calendar day) — default yesterday")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.date:
        day = dt.datetime.strptime(a.date, "%Y-%m-%d").replace(tzinfo=VN)
    else:
        day = (dt.datetime.now(VN) - dt.timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0)
    start = day.replace(hour=8, minute=30, second=0, microsecond=0)
    end = start + dt.timedelta(days=1)

    load_dotenv(ENV_PATH)
    key = os.environ["AVD_TICKET_API_KEY"]

    start_str, end_str = start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")
    tickets = []
    for app_key, app_name in APPS.items():
        for t in fetch_tickets(app_name, start_str, end_str, key):
            created = t.get("createdAt")
            if not created:
                continue
            created_dt = dt.datetime.fromisoformat(created.replace("Z", "+00:00"))
            if not (start <= created_dt < end):
                continue  # by-date filters by day, not exact window — narrow it
            if is_liz(t.get("members") or []):
                tickets.append(slim(t, app_key))

    tickets.sort(key=lambda x: x["createdAt"])

    out = {
        "date": start.strftime("%Y-%m-%d"),
        "count": len(tickets),
        "tickets": tickets,
    }

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"{out['date']}: {len(tickets)} ticket(s) tạo cho Liz")
        for t in tickets:
            print(f"  [{t['app']}] #{t['ticketNumber']} — {t['subject'][:60]}")


if __name__ == "__main__":
    main()
