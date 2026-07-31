#!/usr/bin/env python3
"""
Pull JOY Loyalty onboarding tickets (subject prefix `[ONB]`) for the weekly CS
bulletin's "Onboarding tickets" section.

The Ticket API's `/tickets/by-date` filters on createdAt, so a single call only
sees tickets CREATED in [start, end] — it can't surface older still-open backlog.
To also flag stuck backlog we additionally pull a LOOKBACK window (default 90
days ending at `end`) and take the current-state snapshot of every open [ONB]
ticket in it (status + checklist completion), independent of when it was created.

Checklist = the ticket's `tasks` array (10 standard onboarding steps: Launch
date, Detail program, Earning/Redeeming rule, VIP tier setup, Referral setup,
Guest→Member, Migration/Import, Test full loop, Widget customize, Switch live).

Window is INCLUSIVE [start, end] in local time (Asia/Bangkok, +07).

Usage:
  python3 fetch_onboarding.py --start 2026-07-21 --end 2026-07-27 --json
  python3 fetch_onboarding.py --start 2026-07-21 --end 2026-07-27 --compare --json
"""
import os, json, argparse, datetime
import requests
from dotenv import load_dotenv

ENV_PATH = "/Users/avada/CSL/.env"
TICKET_BASE = "https://avada-ts-a9cb0.web.app/api/external"
TICKET_APP = "JOY Loyalty"
LOOKBACK_DAYS = 90
STUCK_DAYS = 14  # open + created this long ago -> flag as delayed


def fetch(start, end, key):
    r = requests.get(
        f"{TICKET_BASE}/tickets/by-date",
        headers={"X-API-Key": key},
        params={"startDate": start, "endDate": end, "appName": TICKET_APP},
        timeout=60,
    )
    r.raise_for_status()
    tks = r.json().get("data", {}).get("tickets", [])
    return [t for t in tks if t.get("subject", "").strip().startswith("[ONB]")]


def checklist(t):
    tasks = t.get("tasks") or []
    done = sum(1 for x in tasks if x.get("completed"))
    total = len(tasks)
    return done, total


def store_domain(t):
    domains = t.get("storeDomains") or []
    if domains:
        return domains[0]
    return t.get("subject", "").replace("[ONB]", "").strip()


def cs_name(t):
    members = t.get("members") or []
    return members[0].get("displayName") if members else None


def slim(t, today):
    done, total = checklist(t)
    created = t.get("createdAt", "")
    days_open = None
    if created:
        try:
            created_dt = datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))
            days_open = (today - created_dt.date()).days
        except ValueError:
            pass
    return {
        "ticketNumber": t.get("ticketNumber"),
        "ticketId": t.get("ticketId"),
        "shortUrl": t.get("shortUrl"),
        "store": store_domain(t),
        "cs": cs_name(t),
        "status": t.get("ticketStatus"),
        "done": done,
        "total": total,
        "pct": round(done / total * 100) if total else 0,
        "createdAt": created,
        "daysOpen": days_open,
    }


def window(app_key, start, end, today):
    onb = fetch(start, end, app_key)
    new_count = len(onb)

    lookback_start = (datetime.date.fromisoformat(end) -
                       datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()
    backlog = fetch(lookback_start, end, app_key)

    open_tks = [t for t in backlog if t.get("ticketStatus") == "open"]
    open_rows = [slim(t, today) for t in open_tks]
    open_rows.sort(key=lambda r: r["createdAt"])

    golive = [t for t in backlog
              if t.get("ticketStatus") == "closed"
              and start <= (t.get("updatedAt") or "")[:10] <= end]

    avg_pct = round(sum(r["pct"] for r in open_rows) / len(open_rows)) if open_rows else 0
    delayed = [r for r in open_rows if (r["daysOpen"] or 0) > STUCK_DAYS]

    return {
        "new_count": new_count,
        "open_count": len(open_rows),
        "golive_count": len(golive),
        "avg_checklist_pct": avg_pct,
        "open_tickets": open_rows,
        "delayed": delayed,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--compare", action="store_true", help="also pull the prior Mon-Sun window")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    load_dotenv(ENV_PATH)
    key = os.environ["AVD_TICKET_API_KEY"]
    today = datetime.date.fromisoformat(a.end)

    out = {"app": "joy", "start": a.start, "end": a.end}
    out.update(window(key, a.start, a.end, today))

    if a.compare:
        span = (datetime.date.fromisoformat(a.end) - datetime.date.fromisoformat(a.start)).days + 1
        prev_end = datetime.date.fromisoformat(a.start) - datetime.timedelta(days=1)
        prev_start = prev_end - datetime.timedelta(days=span - 1)
        prev = window(key, prev_start.isoformat(), prev_end.isoformat(), prev_end)
        out["prevWeek"] = {"new_count": prev["new_count"]}

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"joy onboarding {a.start}-{a.end}: new={out['new_count']} "
              f"open={out['open_count']} golive={out['golive_count']} "
              f"avg_checklist={out['avg_checklist_pct']}%")
        for r in out["open_tickets"]:
            flag = " ⚠️" if (r["daysOpen"] or 0) > STUCK_DAYS else ""
            print(f"  {r['store']} — {r['done']}/{r['total']} ({r['cs']}, "
                  f"{r['daysOpen']}d open){flag}")


if __name__ == "__main__":
    main()
