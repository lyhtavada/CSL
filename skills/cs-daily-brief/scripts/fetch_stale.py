#!/usr/bin/env python3
"""
Pull open tickets across all 3 apps Liz owns (Chatty, JOY Loyalty, Wishlist)
and flag ones that look neglected, so /ticket-watch can DM her a daily report.

A ticket is skipped entirely (no flags) if `dueDateDone` is true or
`tsStatus == "done"` — that's the "Done" checkmark on the ticket header,
which can stay true while `ticketStatus` itself is still "open" (API lag).

Flags (a ticket can carry more than one):
  stale_no_update   regular (non-DFY/ONB) ticket, ticketStatus=open, age >=
                     --stale-days (default 1) AND (no update since created OR
                     still tsStatus=pending / unclaimed)
  dfy_stuck         [DFY]/[ONB] project ticket, ticketStatus=open, has an
                     incomplete tasks[] item, AND the checklist's completed
                     count hasn't grown in >= --dfy-stale-days (checklist
                     progress itself is tracked per-ticket in state/seen.json
                     under "taskProgress", NOT the ticket's `updatedAt` —
                     `updatedAt` lags/changes for reasons unrelated to the
                     checklist, e.g. viewer read receipt, so an actively
                     worked ticket (3/5 tasks done) was getting flagged the
                     same as a truly untouched one (0/5) whenever
                     `updatedAt` happened to sit still (Liz-reported false
                     positive, 2026-07-23). Every task checked off resets
                     that ticket's stall clock to `now`; first sighting of a
                     ticket seeds the clock at its `createdAt`.

Window: pulls tickets created in the last --window-days (default 60) — a ticket
open longer than that without being closed is assumed rare enough to not need
covering here; widen --window-days if needed.

VIP tier: a ticket is VIP if its `appPlan` is anything other than a free/basic
plan — plan naming has drifted across years per app (e.g. "pro_3_2026",
"advanced_2025", "shopify_plus", "enterprise"...) so this is a coarse "paid
tier at Pro-and-above" heuristic, not an exact plan lookup. Adjust
NON_VIP_PLANS below if it misclassifies something.

Usage:
  python3 fetch_stale.py --json
  python3 fetch_stale.py --stale-days 1 --dfy-stale-days 2 --json
"""
import os, json, argparse
from collections import Counter
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

NON_VIP_PLANS = {None, "free", "basic", "affiliate"}


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


def flag_ticket(t, now, stale_days, dfy_stale_days, task_key, prev_task_progress, next_task_progress):
    flags = []
    status = t.get("ticketStatus")
    if status != "open":
        return flags

    # `dueDateDone` is the "Done" quick-action checkmark shown on the ticket
    # header — merchant-facing work is finished even though `ticketStatus`
    # can lag behind and still say "open" (confirmed live: JOY-260612-PTUnBC
    # has dueDateDone=true, tsStatus=done_for_you, ticketStatus=open — Liz
    # flagged this as a false positive). tsStatus=="done" is the same signal
    # from the other status dropdown.
    if t.get("dueDateDone") is True or t.get("tsStatus") == "done":
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

    if project:
        tasks = t.get("tasks") or []
        tasks_done = sum(1 for task in tasks if task.get("completed"))
        prior = prev_task_progress.get(task_key) or {}
        prior_done = prior.get("tasksDone", 0)
        prior_progress_at = parse_dt(prior.get("progressAt")) or created

        # Any checklist item ticked off since we last looked resets the
        # stall clock — that's real forward progress, not a stuck ticket.
        progress_at = now if tasks_done > prior_done else prior_progress_at
        next_task_progress[task_key] = {"tasksDone": tasks_done, "progressAt": progress_at.isoformat()}

        stalled_hours = (now - progress_at).total_seconds() / 3600
        if tasks and tasks_done < len(tasks) and stalled_hours >= dfy_stale_days * 24:
            flags.append("dfy_stuck")

    return flags


def slim(t, app_key, flags, now):
    created = parse_dt(t.get("createdAt"))
    updated = parse_dt(t.get("updatedAt")) or created
    plan = t.get("appPlan")
    assignees = [m.get("displayName") for m in (t.get("members") or []) if m.get("displayName")]
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
        "assignees": assignees or ["(chưa gán)"],
        "store": (t.get("store") or [{}])[0].get("domain"),
        "appPlan": plan,
        "isVip": plan not in NON_VIP_PLANS,
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

    # Load state up front (not just the carryover dedup below) — dfy_stuck
    # needs yesterday's per-ticket checklist progress to tell "still stuck"
    # apart from "just made progress".
    state_path = os.path.abspath(STATE_PATH)
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    prev_state = {}
    if os.path.exists(state_path):
        try:
            prev_state = json.load(open(state_path))
        except (json.JSONDecodeError, OSError):
            prev_state = {}
    prev_seen = prev_state.get("tickets", {})
    prev_task_progress = prev_state.get("taskProgress", {})
    next_task_progress = {}

    flagged = []
    counts = {}
    for app_key, app_name in APPS.items():
        tickets = fetch_tickets(app_name, start, end, key)
        counts[app_key] = {"total": len(tickets), "open": 0, "flagged": 0}
        for t in tickets:
            if t.get("ticketStatus") == "open":
                counts[app_key]["open"] += 1
            task_key = f"{app_key}:{t.get('ticketNumber')}"
            flags = flag_ticket(t, now, a.stale_days, a.dfy_stale_days,
                                 task_key, prev_task_progress, next_task_progress)
            if flags:
                counts[app_key]["flagged"] += 1
                flagged.append(slim(t, app_key, flags, now))

    flagged.sort(key=lambda x: x["sinceUpdateDays"] or 0, reverse=True)

    # Breakdown by CS phụ trách — accountability view (who currently owns the
    # most neglected tickets), computed over ALL currently flagged tickets
    # (new + carryover), not just today's new ones.
    assignee_counter = Counter()
    for t in flagged:
        for name in t["assignees"]:
            if "AI Agent" in name or "Bot" in name:
                continue  # bot members aren't accountable CS owners
            assignee_counter[name] += 1
    assignee_breakdown = [{"name": n, "count": c}
                           for n, c in assignee_counter.most_common()]

    # VIP (Pro+/Plus/Enterprise) tickets always get surfaced in full, not
    # summarized — a stale VIP ticket matters more than a stale Free one.
    vip_tickets = [t for t in flagged if t["isVip"]]

    # Day-over-day dedup: a ticket already reported yesterday and still open
    # today is "carryover" (summarized, not re-listed in full) — only tickets
    # that just crossed a threshold since the last run are "new" and get
    # listed in detail. Keeps the daily DM short instead of repeating the
    # same backlog every day.
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

    json.dump({"generatedAt": now.isoformat(), "tickets": next_seen,
               "taskProgress": next_task_progress},
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
        "assigneeBreakdown": assignee_breakdown,
        "vipCount": len(vip_tickets),
        "vipTickets": vip_tickets,
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
