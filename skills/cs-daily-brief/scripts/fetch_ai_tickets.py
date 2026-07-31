#!/usr/bin/env python3
"""
Chats handled by the app AI bot (Ivy/Joyce/Wendy) on one full calendar day
(00:00-24:00 VN time), and which of those chats got a ticket created by the
bot itself — for the daily CS report (section replacing the old ticket-watch).

Two data sources, joined by app:
  - BigQuery `avada_cs.crisp_chats`: distinct sessions with an operator
    message from the bot that day (agentEmail IS NULL identifies a bot
    message; userNickname is the bot's own Crisp display name — confirmed
    live 2026-07-31: Ivy only appears under segments containing "app_chatty",
    Joyce under "app_joy", Wendy under "app_wishlist" — so nickname alone is
    an unambiguous per-app bot filter, no segments join needed).
  - Ticket API `/tickets/by-date`: tickets created that day whose creating
    member (`isCreate: true`) is the AI agent (`memberId == "ai-agent-2"`,
    displayName "TS AI Agent 2 (Team 2)" — confirmed live, same agent id
    shared across all 3 apps; the ticket's own `appName` is what maps it back
    to Ivy/Joyce/Wendy for display, not the member identity).

Customer display name comes from the ticket's `store[0].shopName` (fallback
to domain, then "Khách") — the Ticket API has no Crisp nickname field, and
chatLink already carries the session_id straight from Crisp so no BigQuery
join is needed to get the chat link itself.

Usage:
  python3 fetch_ai_tickets.py --json                # yesterday (VN)
  python3 fetch_ai_tickets.py --date 2026-07-30 --json
"""
import os, sys, json, argparse, datetime as dt
import requests
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(__file__))
from _common import load_env, bq_client, VN  # noqa: E402

ENV_PATH = "/Users/avada/CSL/.env"
TICKET_BASE = "https://avada-ts-a9cb0.web.app/api/external"

# app_key -> (Ticket API appName, Crisp bot nickname)
APPS = {
    "joy": ("JOY Loyalty", "Joyce"),
    "chatty": ("Chatty", "Ivy"),
    "wishlist": ("Wishlist", "Wendy"),
}

AI_MEMBER_ID = "ai-agent-2"


def fetch_handled_counts(client, day_str):
    """Distinct sessions with >=1 bot operator message that day, per bot nickname."""
    nick_list = [nick for _, nick in APPS.values()]
    q = """
    SELECT userNickname, COUNT(DISTINCT session_id) AS n
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE fromType = 'operator' AND agentEmail IS NULL
      AND userNickname IN UNNEST(@nicks)
      AND timestamp >= TIMESTAMP(@start)
      AND timestamp <  TIMESTAMP(@end)
    GROUP BY userNickname
    """
    from google.cloud import bigquery
    start = f"{day_str} 00:00:00+07"
    end_excl = (dt.datetime.strptime(day_str, "%Y-%m-%d").date()
                + dt.timedelta(days=1)).isoformat() + " 00:00:00+07"
    job = bigquery.QueryJobConfig(query_parameters=[
        bigquery.ArrayQueryParameter("nicks", "STRING", nick_list),
        bigquery.ScalarQueryParameter("start", "STRING", start),
        bigquery.ScalarQueryParameter("end", "STRING", end_excl),
    ])
    counts = {nick: 0 for nick in nick_list}
    for r in client.query(q, job_config=job).result():
        counts[r.userNickname] = r.n
    return counts


def fetch_tickets(app_name, start, end, key):
    r = requests.get(
        f"{TICKET_BASE}/tickets/by-date",
        headers={"X-API-Key": key},
        params={"startDate": start, "endDate": end, "appName": app_name},
        timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", {}).get("tickets", [])


def is_ai_created(members):
    return any(m.get("isCreate") and m.get("memberId") == AI_MEMBER_ID
               for m in (members or []))


def customer_name(t):
    store = (t.get("store") or [{}])[0]
    return store.get("shopName") or store.get("domain") or "Khách"


def slim_ticket(t, app_key):
    return {
        "app": app_key,
        "ticketNumber": t.get("ticketNumber"),
        "customer": customer_name(t),
        "chatLink": t.get("chatLink"),
        "ticketUrl": "https://avada-ts-a9cb0.web.app" + t["shortUrl"] if t.get("shortUrl") else None,
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
    start = day.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + dt.timedelta(days=1)
    day_str = start.strftime("%Y-%m-%d")

    env = load_env()
    bq = bq_client(env)
    handled = fetch_handled_counts(bq, day_str)

    load_dotenv(ENV_PATH)
    key = os.environ["AVD_TICKET_API_KEY"]

    apps_out = {}
    for app_key, (app_name, nick) in APPS.items():
        tickets = []
        for t in fetch_tickets(app_name, day_str, day_str, key):
            created = t.get("createdAt")
            if not created:
                continue
            created_dt = dt.datetime.fromisoformat(created.replace("Z", "+00:00"))
            if not (start <= created_dt < end):
                continue
            if is_ai_created(t.get("members")):
                tickets.append(slim_ticket(t, app_key))
        apps_out[app_key] = {
            "bot": nick,
            "handledCount": handled.get(nick, 0),
            "ticketCount": len(tickets),
            "tickets": tickets,
        }

    out = {"date": day_str, "apps": apps_out}

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        for app_key, d in apps_out.items():
            print(f"{d['bot']} ({app_key}): handled={d['handledCount']} tickets={d['ticketCount']}")
            for t in d["tickets"]:
                print(f"  {t['customer']} — {t['ticketUrl']}")


if __name__ == "__main__":
    main()
