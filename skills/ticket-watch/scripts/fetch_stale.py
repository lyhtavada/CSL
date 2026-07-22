#!/usr/bin/env python3
"""
Pull open tickets across all 3 apps Liz owns (Chatty, JOY Loyalty, Wishlist)
and flag ones that look neglected, so /ticket-watch can DM her a daily report.

Flags (a ticket can carry more than one):
  stale_no_update   ticketStatus=open AND no update (updatedAt) in >= --stale-days
  pending_unclaimed tsStatus=pending AND created >= 24h ago (nobody has claimed it)
  dfy_stuck         has a tasks[] checklist with an incomplete item AND
                     no update in >= --stale-days (DFY progress stalled)
  sla_breach        priority in {urgent,high} AND still open past the
                     resolution-target window from kb/cs-process/shared-cs-process/
                     priority-matrix.md (urgent=P0: 24h, high=P1: 5 days)

Window: pulls tickets created in the last --window-days (default 60) — a ticket
open longer than that without being closed is assumed rare enough to not need
covering here; widen --window-days if needed.

Usage:
  python3 fetch_stale.py --stale-days 2 --json
  python3 fetch_stale.py --stale-days 2 --window-days 90 --json
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

SLA_RESOLUTION_HOURS = {
    "urgent": 24,       # P0
    "high": 24 * 5,     # P1
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


def flag_ticket(t, now, stale_days):
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

    if since_update is not None and since_update >= stale_days * 24:
        flags.append("stale_no_update")

    if t.get("tsStatus") == "pending" and age_hours >= 24:
        flags.append("pending_unclaimed")

    tasks = t.get("tasks") or []
    if tasks and any(not task.get("completed") for task in tasks) \
            and since_update is not None and since_update >= stale_days * 24:
        flags.append("dfy_stuck")

    priority = t.get("priority")
    sla_h = SLA_RESOLUTION_HOURS.get(priority)
    if sla_h and age_hours >= sla_h:
        flags.append("sla_breach")

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
    ap.add_argument("--stale-days", type=float, default=2)
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
            flags = flag_ticket(t, now, a.stale_days)
            if flags:
                counts[app_key]["flagged"] += 1
                flagged.append(slim(t, app_key, flags, now))

    flagged.sort(key=lambda x: x["sinceUpdateDays"] or 0, reverse=True)

    out = {
        "generatedAt": now.isoformat(),
        "staleDays": a.stale_days,
        "windowDays": a.window_days,
        "counts": counts,
        "flaggedCount": len(flagged),
        "tickets": flagged,
    }

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"Flagged {len(flagged)} tickets across {list(APPS.keys())}")
        for t in flagged:
            print(f"  [{t['app']}] #{t['ticketNumber']} {t['flags']} "
                  f"({t['sinceUpdateDays']}d since update) — {t['subject'][:60]}")


if __name__ == "__main__":
    main()
