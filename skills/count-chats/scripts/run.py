#!/usr/bin/env python3
"""
Ad-hoc "real conversation" count for one or all apps over any date range.
Uses the shared counting logic in skills/_shared/chat_count.py — same method
as /cs-weekly's fetch_metrics.py, so numbers here always match the weekly report.

Usage:
  python3 run.py --app chatty --start 2026-07-20 --end 2026-07-26
  python3 run.py --app all --month 2026-07
  python3 run.py --app joy --week 2026-07-20          # Mon of the target week
  python3 run.py --app chatty --start 2026-07-01 --end 2026-07-26 --json
"""
import os, sys, json, argparse, datetime, calendar

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_shared"))
from chat_count import chat_count, APP_SEGMENTS  # noqa: E402

ENV_PATH = "/Users/avada/CSL/.env"


def load_env():
    from dotenv import load_dotenv
    load_dotenv(ENV_PATH)


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


def month_range(ym):
    y, m = map(int, ym.split("-"))
    last = calendar.monthrange(y, m)[1]
    return f"{y:04d}-{m:02d}-01", f"{y:04d}-{m:02d}-{last:02d}"


def week_range(any_date):
    d = datetime.datetime.strptime(any_date, "%Y-%m-%d").date()
    mon = d - datetime.timedelta(days=d.weekday())
    sun = mon + datetime.timedelta(days=6)
    return mon.isoformat(), sun.isoformat()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, choices=["chatty", "joy", "wishlist", "all"])
    ap.add_argument("--start", help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", help="YYYY-MM-DD inclusive")
    ap.add_argument("--month", help="YYYY-MM shortcut (full calendar month)")
    ap.add_argument("--week", help="any YYYY-MM-DD shortcut (its Mon->Sun week)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.month:
        start, end = month_range(a.month)
    elif a.week:
        start, end = week_range(a.week)
    elif a.start and a.end:
        start, end = a.start, a.end
    else:
        ap.error("need --start/--end, --month, or --week")

    load_env()
    client = bq_client()

    apps = ["chatty", "joy", "wishlist"] if a.app == "all" else [a.app]
    out = {"start": start, "end": end, "counts": {}}
    for app in apps:
        out["counts"][app] = chat_count(client, APP_SEGMENTS[app], start, end)
    out["total"] = sum(out["counts"].values())

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"{start} -> {end}")
        for app, n in out["counts"].items():
            print(f"  {app}: {n}")
        if len(apps) > 1:
            print(f"  total: {out['total']}")


if __name__ == "__main__":
    main()
