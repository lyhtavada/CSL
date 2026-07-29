#!/usr/bin/env python3
"""
Fetch weekly DFY numbers (Mon-Sun) for Chatty + Joy, for the CEO Weekly report.

Lean version of skills/dfy-monthly/scripts/fetch_dfy.py: same DFY-tag set +
review/install logic, but by an arbitrary date range instead of a calendar
month, and without per-CS breakdown / insights / no-adopt comment fetching
(not needed for a 1-line-per-app CEO summary).

Usage:
  python3 fetch_dfy_week.py --start 2026-07-13 --end 2026-07-19 [--out /tmp/dfy_week.json]

Output JSON: {"chatty": {...}, "joy": {...}}, each:
  {"total": N, "adopted": N, "adopt_pct": N,
   "review": {"count": N, "pct": N},
   "install": {"count": N, "pct": N}}
"""
import argparse, json, re, sys, urllib.request, urllib.parse
from pathlib import Path

BASE = "https://avada-ts-a9cb0.web.app"
ROOT = Path(__file__).parent.parent.parent

APP_NAME = {"chatty": "Chatty", "joy": "JOY Loyalty"}
INSTALL_APP_ID = {"chatty": "avadaFaq", "joy": "joy"}
REVIEW_SEGMENTS = {
    "chatty": ["review_yes_chatty", "rv_yes_chatty", "review_yes_faq"],
    "joy": ["review_yes_joy"],
}
DFY_SET = {
    "DFY-1", "DFY-adopted", "DFY-coupon-images", "DFY-following-up", "DFY-new",
    "DFY-no-adopt", "DFY-tier-banner", "DFY-tier-icon", "DFY-video",
    "ai agent", "chatbox", "proactive",
}
SESSION_RE = re.compile(r"session_([a-f0-9-]+)")


def load_env():
    env = {}
    for line in open(ROOT / ".env"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k] = v.strip().strip('"').strip("'")
    return env


def api_get(path, key, params=None, retries=2):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-API-Key": key})
    last_err = None
    for _ in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
    raise last_err


def tag_map(key):
    data = api_get("/api/external/tags", key)
    arr = data.get("data", data)
    if isinstance(arr, dict):
        arr = arr.get("tags", arr)
    return {(tg.get("id") or tg.get("_id") or tg.get("tagId")): (tg.get("name") or tg.get("title")) for tg in arr}


def names(t, id2name):
    return [x for x in (id2name.get(i) for i in (t.get("tagIds") or [])) if x]


def creator(t):
    m = [x for x in t.get("members", []) if x.get("isCreate")] or t.get("members", [])[:1]
    return (m[0].get("username") or m[0].get("displayName") or "?") if m else "?"


def session_id_from_chatlink(chat_link):
    if not chat_link:
        return None
    m = SESSION_RE.search(chat_link)
    return m.group(1) if m else None


def bq_client(env):
    from google.oauth2 import service_account
    from google.cloud import bigquery
    creds = service_account.Credentials.from_service_account_info({
        "type": "service_account",
        "client_email": env["BQ_SA_CLIENT_EMAIL"],
        "private_key": env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n"),
        "token_uri": "https://oauth2.googleapis.com/token",
    }, scopes=["https://www.googleapis.com/auth/bigquery"])
    return bigquery.Client(project="avada-crm", credentials=creds)


def fetch_reviewed(client, session_ids, domains, since, segments):
    if not session_ids and not domains:
        return set(), set()
    from google.cloud import bigquery as bq
    seg_clause = " OR ".join(f"LOWER(segments) LIKE '%{s}%'" for s in segments)
    q = f"""
    SELECT DISTINCT session_id,
           REGEXP_REPLACE(REGEXP_REPLACE(LOWER(shopifyDomain), r'^https?://', ''), r'/$', '') AS domain
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE ({seg_clause})
      AND timestamp >= @since
      AND (session_id IN UNNEST(@session_ids)
           OR REGEXP_REPLACE(REGEXP_REPLACE(LOWER(shopifyDomain), r'^https?://', ''), r'/$', '') IN UNNEST(@domains))
    """
    job = client.query(q, job_config=bq.QueryJobConfig(query_parameters=[
        bq.ScalarQueryParameter("since", "TIMESTAMP", since),
        bq.ArrayQueryParameter("session_ids", "STRING", list(session_ids) or [""]),
        bq.ArrayQueryParameter("domains", "STRING", [d.lower() for d in domains] or [""]),
    ]))
    rev_sessions, rev_domains = set(), set()
    for row in job.result():
        if row.session_id:
            rev_sessions.add(row.session_id)
        if row.domain:
            rev_domains.add(row.domain)
    return rev_sessions, rev_domains


def fetch_installs(client, app_id, start, end):
    from google.cloud import bigquery as bq
    q = """
    SELECT SUM(unique_shops) AS installs
    FROM `avada-crm.avada_product_dash.dash_daily_installs`
    WHERE app_id = @app_id AND day BETWEEN @start AND @end
    """
    job = client.query(q, job_config=bq.QueryJobConfig(query_parameters=[
        bq.ScalarQueryParameter("app_id", "STRING", app_id),
        bq.ScalarQueryParameter("start", "DATE", start),
        bq.ScalarQueryParameter("end", "DATE", end),
    ]))
    for row in job.result():
        return row.installs or 0
    return 0


def ticket_reviewed(t, rev_sessions, rev_domains):
    sess = session_id_from_chatlink(t.get("chatLink"))
    domain = (t.get("store") or [{}])[0].get("domain", "").lower()
    return (sess and sess in rev_sessions) or (domain and domain in rev_domains)


def fetch_app(app, start, end, key, bq, env):
    id2name = tag_map(key)
    resp = api_get("/api/external/tickets/by-date", key,
                    {"startDate": start, "endDate": end, "appName": APP_NAME[app]})
    tickets = resp.get("data", {}).get("tickets", [])

    dfy = [t for t in tickets if set(names(t, id2name)) & DFY_SET]
    op = [t for t in dfy
          if t.get("ticketStatus") != "closed"
          and t.get("tsStatus") != "sale_request"
          and not (creator(t) == "?" and not names(t, id2name))]

    total = len(op)
    adopted = sum(1 for t in op if "DFY-adopted" in names(t, id2name))
    adopt_pct = round(100 * adopted / total) if total else 0

    session_ids = {s for s in (session_id_from_chatlink(t.get("chatLink")) for t in op) if s}
    domains = {(t.get("store") or [{}])[0].get("domain", "") for t in op}
    domains.discard("")
    rev_sessions, rev_domains = fetch_reviewed(bq, session_ids, domains, f"{start} 00:00:00", REVIEW_SEGMENTS[app])
    review_n = sum(1 for t in op if ticket_reviewed(t, rev_sessions, rev_domains))
    review_pct = round(100 * review_n / total) if total else 0

    installs = fetch_installs(bq, INSTALL_APP_ID[app], start, end)
    install_pct = round(100 * total / installs, 2) if installs else 0

    return {
        "total": total, "adopted": adopted, "adopt_pct": adopt_pct,
        "review": {"count": review_n, "pct": review_pct},
        "install": {"count": installs, "pct": install_pct},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD (Monday)")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD (Sunday)")
    ap.add_argument("--out")
    a = ap.parse_args()

    env = load_env()
    key = env["AVD_TICKET_API_KEY"]
    bq = bq_client(env)

    result = {app: fetch_app(app, a.start, a.end, key, bq, env) for app in ("chatty", "joy")}

    blob = json.dumps(result, ensure_ascii=False, indent=2)
    if a.out:
        with open(a.out, "w") as f:
            f.write(blob)
        print(f"Wrote {a.out}", file=sys.stderr)
    else:
        print(blob)


if __name__ == "__main__":
    main()
