#!/usr/bin/env python3
"""
Pull open tickets across all 3 apps Liz owns (Chatty, JOY Loyalty, Wishlist)
and flag ones that look neglected, so /ticket-watch can DM her a daily report.

Flags (a ticket can carry more than one):
  stale_no_update   regular (non-DFY/ONB) ticket, ticketStatus=open, age >=
                     --stale-days (default 1) AND (no update since created OR
                     still tsStatus=pending / unclaimed)
  dfy_stuck         [DFY]/[ONB] project ticket, ticketStatus=open, age >=
                     --dfy-stale-days (default 2) AND has an incomplete
                     tasks[] item with no update since (checklist stalled)

Window: pulls tickets created in the last --window-days (default 60) — a ticket
open longer than that without being closed is assumed rare enough to not need
covering here; widen --window-days if needed.

Usage:
  python3 fetch_stale.py --json
  python3 fetch_stale.py --stale-days 1 --dfy-stale-days 2 --json
"""
import os, json, argparse
from datetime import datetime, timedelta, timezone
import requests
from dotenv import load_dotenv

ENV_PATH = "/Users/avada/CSL/.env"
TICKET_BASE = "https://avada-ts-a9cb0.web.app/api/external"
STATE_PATH = os.path.join(os.path.dirname(__file__), "..", "state", "seen.json")

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


def parse_dt(s):
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def is_project_ticket(subject):
    """[DFY] / [ONB] tickets are ongoing multi-week projects tracked separately
    by /dfy-tracker, /dfy-weekly, /dfy-monthly — staying 'open' for a while is
    normal for them, so they're excluded from the generic staleness flag and
    only checked via dfy_stuck (checklist literally stalled)."""
    s = (subject or "").strip().lower()
    return s.startswith("[dfy]") or s.startswith("[onb]")


def flag_ticket(t, now, stale_days, dfy_stale_days):
    flags = []
    status = t.get("ticketStatus")
    if status != "open":
        return flags

    created = parse_dt(t.get("createdAt"))
    updated = parse_dt(t.get("updatedAt")) or created
    if not created:
        return flags

    since_update = (now - updated).total_seconds() / 3600 if updated else None
    age_hours = (now - created).total_seconds() / 3600
    project = is_project_ticket(t.get("subject"))

    if not project and age_hours >= stale_days * 24:
        no_update = since_update is not None and since_update >= stale_days * 24
        unclaimed = t.get("tsStatus") == "pending"
        if no_update or unclaimed:
            flags.append("stale_no_update")

    if project and age_hours >= dfy_stale_days * 24:
        tasks = t.get("tasks") or []
        stalled = since_update is not None and since_update >= dfy_stale_days * 24
        if tasks and any(not task.get("completed") for task in tasks) and stalled:
            flags.append("dfy_stuck")

    return flags


def slim(t, app_key, flags, now):
    created = parse_dt(t.get("createdAt"))
    updated = parse_dt(t.get("updatedAt")) or created
    return {
        "app": app_key,
        "ticketNumber": t.get("ticketNumber"),
        "ticketId": t.get("ticketId"),
        "subject": (t.get("subject") or "").strip()[:200],
        "priority": t.get("priority"),
        "tsStatus": t.get("tsStatus"),
        "ticketStatus": t.get("ticketStatus"),
        "createdAt": t.get("createdAt"),
        "updatedAt": t.get("updatedAt"),
        "ageDays": round((now - created).total_seconds() / 86400, 1) if created else None,
        "sinceUpdateDays": round((now - updated).total_seconds() / 86400, 1) if updated else None,
        "assignees": [m.get("displayName") for m in (t.get("members") or [])],
        "store": (t.get("store") or [{}])[0].get("domain"),
        "ticketUrl": "https://avada-ts-a9cb0.web.app" + t["shortUrl"] if t.get("shortUrl") else None,
        "chatLink": t.get("chatLink"),
        "tasks": t.get("tasks") or [],
        "flags": flags,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stale-days", type=float, default=1)
    ap.add_argument("--dfy-stale-days", type=float, default=2)
    ap.add_argument("--window-days", type=int, default=60)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    load_dotenv(ENV_PATH)
    key = os.environ["AVD_TICKET_API_KEY"]

    now = datetime.now(timezone.utc)
    start = (now - timedelta(days=a.window_days)).strftime("%Y-%m-%d")
    end = now.strftime("%Y-%m-%d")

    flagged = []
    counts = {}
    for app_key, app_name in APPS.items():
        tickets = fetch_tickets(app_name, start, end, key)
        counts[app_key] = {"total": len(tickets), "open": 0, "flagged": 0}
        for t in tickets:
            if t.get("ticketStatus") == "open":
                counts[app_key]["open"] += 1
            flags = flag_ticket(t, now, a.stale_days, a.dfy_stale_days)
            if flags:
                counts[app_key]["flagged"] += 1
                flagged.append(slim(t, app_key, flags, now))

    flagged.sort(key=lambda x: x["sinceUpdateDays"] or 0, reverse=True)

    # Day-over-day dedup: a ticket already reported yesterday and still open
    # today is "carryover" (summarized, not re-listed in full) — only tickets
    # that just crossed a threshold since the last run are "new" and get
    # listed in detail. Keeps the daily DM short instead of repeating the
    # same backlog every day.
    state_path = os.path.abspath(STATE_PATH)
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    prev_seen = {}
    if os.path.exists(state_path):
        try:
            prev_seen = json.load(open(state_path)).get("tickets", {})
        except (json.JSONDecodeError, OSError):
            prev_seen = {}

    new_items, carryover_items = [], []
    next_seen = {}
    for t in flagged:
        key = f"{t['app']}:{t['ticketNumber']}"
        prior = prev_seen.get(key)
        first_flagged = prior.get("firstFlaggedAt") if prior else now.isoformat()
        next_seen[key] = {"firstFlaggedAt": first_flagged, "flags": t["flags"]}
        t["firstFlaggedAt"] = first_flagged
        if prior:
            carryover_items.append(t)
        else:
            new_items.append(t)

    json.dump({"generatedAt": now.isoformat(), "tickets": next_seen},
               open(state_path, "w"), ensure_ascii=False, indent=2)

    out = {
        "generatedAt": now.isoformat(),
        "staleDays": a.stale_days,
        "dfyStaleDays": a.dfy_stale_days,
        "windowDays": a.window_days,
        "counts": counts,
        "flaggedCount": len(flagged),
        "newCount": len(new_items),
        "carryoverCount": len(carryover_items),
        "newTickets": new_items,
        "carryoverTickets": carryover_items,
    }

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"Flagged {len(flagged)} tickets ({len(new_items)} new, "
              f"{len(carryover_items)} carryover) across {list(APPS.keys())}")
        for t in new_items:
            print(f"  NEW [{t['app']}] #{t['ticketNumber']} {t['flags']} "
                  f"({t['sinceUpdateDays']}d since update) — {t['subject'][:60]}")


if __name__ == "__main__":
    main()
