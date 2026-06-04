#!/usr/bin/env python3
"""
Fetch the sessions each in-house CS actually handled in a given week, from
BigQuery (NOT the Crisp `assigned` field — that only marks one owner per
session and misses 70-90% of the chats a CS really touched).

A session counts for CS X in week W if X sent >= MIN_MSGS operator messages
*within* week W (so a chat a CS only greeted/handed-off doesn't count, and a
chat is attributed to the week the CS actually worked it — even if the customer
first wrote in an earlier week).

Sampling: up to --sample per CS, biased toward longer chats (more CS messages
in-week = a real case handled, not a one-liner).

Usage:
  python3 fetch_sessions.py --start 2026-05-26 --end 2026-06-01 \
      --out /tmp/qa_weekly_sessions.json --sample 30 --only-type in-house

Output JSON shape (same as before, so downstream scripts are unchanged):
  {"period": {...}, "by_cs": {"Hazel": {slack_id, email, name, app, type,
                              total, sampled, sessions:[{session_id, ...}]}}}
"""
import argparse
import datetime as dt
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore")

from google.cloud import bigquery
from google.oauth2 import service_account

TABLE = "avada-crm.avada_cs.crisp_chats"
MIN_MSGS = 3  # CS must send >= this many in-week to "own" the chat

TEAM_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                         "_identity", "team-g2.md")


def load_env(path):
    env = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def bq_client(env):
    key = (env.get("BQ_SA_PRIVATE_KEY") or "").replace("\\n", "\n")
    creds = service_account.Credentials.from_service_account_info({
        "type": "service_account", "project_id": "avada-crm",
        "private_key": key, "client_email": env.get("BQ_SA_CLIENT_EMAIL"),
        "token_uri": "https://oauth2.googleapis.com/token",
    })
    return bigquery.Client(project="avada-crm", credentials=creds)


def load_team_roster(path):
    """Parse team-g2.md → {email_lower: {nickname, slack_id, email, name, app,
    type}}. Keyed by email since we attribute via agentEmail from BigQuery."""
    roster = {}
    if not os.path.exists(path):
        print(f"WARN: roster not found at {path}", file=sys.stderr)
        return roster
    with open(path) as f:
        for line in f:
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 10 or cells[0] in ("#", "") or set(cells[0]) <= {"-"}:
                continue
            try:
                slack_id = cells[6]
                display = cells[8]      # Crisp nickname
                email = cells[9]
                app = cells[3]
                name = cells[1]
                cs_type = cells[13] if len(cells) > 13 else ""
            except IndexError:
                continue
            if not email or "@" not in email:
                continue
            roster[email.lower()] = {
                "nickname": display, "slack_id": slack_id, "email": email,
                "name": name, "app": app, "type": cs_type,
            }
    return roster


def iso_week(date_str):
    d = dt.date.fromisoformat(date_str)
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def fetch_by_cs(client, emails, start, end):
    """For each email, return the sessions where that CS sent >= MIN_MSGS
    operator messages within [start, end). Biased sample order = most in-week
    CS messages first (longer/real cases). Also pulls session metadata."""
    # end is inclusive day → query through end+1 day
    end_excl = (dt.date.fromisoformat(end) + dt.timedelta(days=1)).isoformat()
    q = f"""
    WITH in_week AS (
      SELECT agentEmail, session_id, COUNT(*) AS cs_msgs
      FROM `{TABLE}`
      WHERE timestamp >= @start AND timestamp < @end
        AND fromType = 'operator'
        AND LOWER(agentEmail) IN UNNEST(@emails)
      GROUP BY agentEmail, session_id
      HAVING cs_msgs >= {MIN_MSGS}
    ),
    meta AS (
      SELECT session_id,
             ANY_VALUE(website_id) website_id,
             ANY_VALUE(shopifyDomain) shopifyDomain,
             ANY_VALUE(customerEmail) customerEmail,
             ANY_VALUE(segments) segments
      FROM `{TABLE}`
      WHERE session_id IN (SELECT session_id FROM in_week)
      GROUP BY session_id
    )
    SELECT w.agentEmail, w.session_id, w.cs_msgs,
           m.website_id, m.shopifyDomain, m.customerEmail, m.segments
    FROM in_week w JOIN meta m USING (session_id)
    ORDER BY w.agentEmail, w.cs_msgs DESC
    """
    job = client.query(q, job_config=bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("start", "TIMESTAMP", start),
            bigquery.ScalarQueryParameter("end", "TIMESTAMP", end_excl),
            bigquery.ArrayQueryParameter("emails", "STRING",
                                         [e.lower() for e in emails]),
        ]))
    by_email = {}
    for r in job:
        seg = r["segments"]
        try:
            seg = json.loads(seg) if isinstance(seg, str) else (seg or [])
        except Exception:
            seg = []
        by_email.setdefault(r["agentEmail"].lower(), []).append({
            "session_id": r["session_id"],
            "website_id": r["website_id"],
            "shopifyDomain": r["shopifyDomain"],
            "customerEmail": r["customerEmail"],
            "segments": seg,
            "cs_msgs": r["cs_msgs"],
        })
    return by_email


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD (Monday)")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD (Sunday)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--sample", type=int, default=30)
    ap.add_argument("--exclude", default="")
    ap.add_argument("--only-type", default="")
    ap.add_argument("--env", default=os.path.join(
        os.path.dirname(__file__), "..", "..", "..", ".env"))
    args = ap.parse_args()

    env = load_env(args.env)
    roster = load_team_roster(TEAM_FILE)
    if not roster:
        print("ERROR: empty roster", file=sys.stderr)
        sys.exit(1)

    exclude = {x.strip().lower() for x in args.exclude.split(",") if x.strip()}
    only_type = args.only_type.strip().lower()

    # Which CS to fetch: filter roster by type + exclude
    targets = {}
    for email, info in roster.items():
        if only_type and info.get("type", "").lower() != only_type:
            continue
        if info["nickname"].lower() in exclude or info["name"].lower() in exclude:
            continue
        if info.get("type", "").lower() == "csl":
            continue  # never grade the CSL
        targets[email] = info
    if not targets:
        print("ERROR: no target CS after filtering", file=sys.stderr)
        sys.exit(1)

    client = bq_client(env)
    by_email = fetch_by_cs(client, list(targets.keys()), args.start, args.end)

    out = {"period": {"start": args.start, "end": args.end,
                      "iso_week": iso_week(args.start)},
           "by_cs": {}}
    for email, info in targets.items():
        sess = by_email.get(email, [])
        # already ordered by cs_msgs DESC → take top N (longest/real cases)
        sampled = sess[:args.sample]
        nick = info["nickname"]
        out["by_cs"][nick] = {
            "slack_id": info["slack_id"], "email": info["email"],
            "name": info["name"], "app": info["app"], "type": info["type"],
            "total": len(sess), "sampled": len(sampled), "sessions": sampled,
        }

    with open(args.out, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(out['by_cs'])} CS → {args.out}", file=sys.stderr)
    for nick, d in sorted(out["by_cs"].items()):
        print(f"  {nick}: {d['sampled']}/{d['total']} chats "
              f"(>= {MIN_MSGS} msg in-week)", file=sys.stderr)


if __name__ == "__main__":
    main()
