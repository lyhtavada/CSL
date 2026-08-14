#!/usr/bin/env python3
"""
Weekly auto-fill for VanCT's 1-month PIP tracker (Google Sheet "Overview" tab).
Pulls 3 data-backed metrics for the CURRENT challenge week (Mon of that week ->
run time) and writes them into the matching Tuần-N column:

  - SLA / first response time  <- BigQuery avada_cs.crisp_chats (agentEmail=vanct)
  - DFY task completion        <- Avada Ticket API (dueDateDone=true, creator=VanCT)
  - Check-in muộn              <- Admin API /shifts + /shifts/:id/checks
    (raw check-in data, NOT the same as the "approved" Penalty log — no API
    access to that endpoint was found; flagged in the written value)

The other 3 criteria (Ticket Follow-up, Team Participation, Internal
Communication) are qualitative — Liz fills those columns by hand.

Usage:
  .venv-crisp/bin/python skills/vanct-pip-tracker/scripts/fill_weekly.py
"""
import os
import sys
import json
import time
import urllib.request
import datetime as dt

ROOT = os.path.expanduser("~/CSL")
sys.path.insert(0, ROOT)

from gapi.client import sheets as gsheets  # noqa: E402

SHEET_ID = "1-KrG3RlFaSLDGKVJWWm3nK-Ow48lHuiwSUanBYlg_zI"
VN = dt.timezone(dt.timedelta(hours=7))
VANCT_EMAIL = "vanct@avadagroup.com"

# Challenge weeks (Mon->Sun), fixed — VanCT resumed trực on 2026-08-17.
WEEKS = [
    (dt.date(2026, 8, 17), dt.date(2026, 8, 23)),
    (dt.date(2026, 8, 24), dt.date(2026, 8, 30)),
    (dt.date(2026, 8, 31), dt.date(2026, 9, 6)),
    (dt.date(2026, 9, 7), dt.date(2026, 9, 13)),
]
WEEK_COL = ["E", "F", "G", "H"]

ROW_SLA_10P = 6
ROW_SLA_30P = 7
ROW_DFY_BASE = 9  # +week_idx -> row for that week's DFY target
ROW_CHECKIN_10P = 16
ROW_CHECKIN_20P = 17


def load_env():
    env = {}
    with open(os.path.join(ROOT, ".env")) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            v = v.strip()
            if v and v[0] in "\"'" and v[-1] == v[0]:
                v = v[1:-1]
            env[k.strip()] = v
    return env


def parse_iso(t):
    return dt.datetime.fromisoformat(t.replace("Z", "+00:00"))


def api_get(env, path, retries=3):
    base = env["AVD_API_BASE"]
    tok = env["AVD_TOKEN"]
    req = urllib.request.Request(f"{base}{path}", headers={"Authorization": f"Bearer {tok}"})
    last = None
    for attempt in range(retries):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise last


def week_index_for(today):
    for i, (s, e) in enumerate(WEEKS):
        if s <= today <= e:
            return i
    return None


def norm_name(disp):
    if not disp:
        return None
    s = disp.strip().lower()
    return s[:-6] if s.endswith("_avada") else s


def fetch_dfy_count(env, week_start, week_end_capped):
    import requests

    url = "https://avada-ts-a9cb0.web.app/api/external/tickets/by-date"
    headers = {"X-API-Key": env["AVD_TICKET_API_KEY"]}
    params = {
        "startDate": week_start.isoformat(),
        "endDate": week_end_capped.isoformat(),
        "appName": "JOY Loyalty",
    }
    r = requests.get(url, params=params, headers=headers, timeout=60)
    r.raise_for_status()
    tickets = r.json()["data"]["tickets"]

    count = 0
    for t in tickets:
        if not t.get("subject", "").startswith("[DFY]"):
            continue
        if t.get("dueDateDone") is not True:
            continue
        if t.get("tsStatus") == "sale_request":
            continue
        creator = next((m for m in t.get("members", []) if m.get("isCreate")), None) or t.get("memberUpdate")
        disp = creator.get("displayName") if creator else None
        if norm_name(disp) != "audrey":
            continue
        count += 1
    return count


def fetch_sla(env, week_start, week_end_capped):
    from google.cloud import bigquery
    from google.oauth2 import service_account

    key = env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n")
    info = {
        "type": "service_account",
        "project_id": "avada-crm",
        "private_key_id": env["BQ_SA_PRIVATE_KEY_ID"],
        "private_key": key,
        "client_email": env["BQ_SA_CLIENT_EMAIL"],
        "token_uri": "https://oauth2.googleapis.com/token",
    }
    creds = service_account.Credentials.from_service_account_info(
        info,
        scopes=["https://www.googleapis.com/auth/bigquery", "https://www.googleapis.com/auth/cloud-platform"],
    )
    client = bigquery.Client(credentials=creds, project="avada-crm")

    start_ts = dt.datetime.combine(week_start, dt.time(0, 0), tzinfo=VN).astimezone(dt.timezone.utc)
    end_ts = dt.datetime.combine(week_end_capped, dt.time(23, 59, 59), tzinfo=VN).astimezone(dt.timezone.utc)

    q = """
    WITH visitor_first AS (
      SELECT session_id, MIN(timestamp) AS first_visitor_ts
      FROM `avada-crm.avada_cs.crisp_chats`
      WHERE fromType = 'user'
      GROUP BY session_id
    ),
    agent_first AS (
      SELECT session_id, MIN(timestamp) AS first_agent_ts
      FROM `avada-crm.avada_cs.crisp_chats`
      WHERE agentEmail = @email AND fromType = 'operator'
      GROUP BY session_id
    )
    SELECT
      TIMESTAMP_DIFF(a.first_agent_ts, v.first_visitor_ts, MINUTE) AS response_min
    FROM visitor_first v
    JOIN agent_first a USING(session_id)
    WHERE a.first_agent_ts > v.first_visitor_ts
      AND a.first_agent_ts BETWEEN @start_ts AND @end_ts
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("email", "STRING", VANCT_EMAIL),
            bigquery.ScalarQueryParameter("start_ts", "TIMESTAMP", start_ts),
            bigquery.ScalarQueryParameter("end_ts", "TIMESTAMP", end_ts),
        ]
    )
    rows = [r.response_min for r in client.query(q, job_config=job_config).result()]
    total = len(rows)
    if total == 0:
        return None, 0, 0
    within10 = sum(1 for m in rows if m <= 10)
    over30 = sum(1 for m in rows if m > 30)
    pct = round(within10 / total * 100)
    return pct, total, over30


def fetch_checkin(env, week_start, week_end_capped):
    shifts = api_get(env, f"/shifts?start={week_start.isoformat()}&end={week_end_capped.isoformat()}").get("data", [])
    late10 = 0
    late20 = 0
    for sh in shifts:
        g2 = [c for c in sh.get("cs", []) if "G2" in (c.get("groupLabel") or "")]
        if not any(c["email"] == VANCT_EMAIL for c in g2):
            continue
        st = parse_iso(sh["start"])
        checks = api_get(env, f"/shifts/{sh['id']}/checks").get("data", [])
        ci = next((c for c in checks if c["email"] == VANCT_EMAIL and c["type"] == "checkin"), None)
        if not ci:
            continue
        m = (parse_iso(ci["createdAt"]) - st).total_seconds() / 60
        if m > 10:
            late10 += 1
        if m > 20:
            late20 += 1
    return late10, late20


def main():
    env = load_env()
    today = dt.datetime.now(VN).date()
    idx = week_index_for(today)
    if idx is None:
        print(f"Today {today} is outside the 4-week challenge window (2026-08-17 -> 2026-09-13) — nothing to fill.")
        return

    week_start, week_end = WEEKS[idx]
    week_end_capped = min(today, week_end)
    col = WEEK_COL[idx]

    dfy_count = fetch_dfy_count(env, week_start, week_end_capped)
    sla_pct, sla_total, sla_over30 = fetch_sla(env, week_start, week_end_capped)
    late10, late20 = fetch_checkin(env, week_start, week_end_capped)

    sla_pct_str = f"{sla_pct}% ≤10p ({sla_total} case)" if sla_pct is not None else "0 case (chưa có data tuần này)"
    sla_over30_str = f"{sla_over30} case >30p"
    dfy_str = f"{dfy_count} ticket dueDateDone"
    checkin_str = f"{late10} lần muộn >10p (raw check-in, chưa qua duyệt penalty log)"
    checkin_ss11b_str = f"{late20} lần >20p (~SS11b)" if late20 else "0 lần >20p"

    svc = gsheets()
    updates = [
        {"range": f"Overview!{col}{ROW_SLA_10P}", "values": [[sla_pct_str]]},
        {"range": f"Overview!{col}{ROW_SLA_30P}", "values": [[sla_over30_str]]},
        {"range": f"Overview!{col}{ROW_DFY_BASE + idx}", "values": [[dfy_str]]},
        {"range": f"Overview!{col}{ROW_CHECKIN_10P}", "values": [[checkin_str]]},
        {"range": f"Overview!{col}{ROW_CHECKIN_20P}", "values": [[checkin_ss11b_str]]},
    ]
    svc.spreadsheets().values().batchUpdate(
        spreadsheetId=SHEET_ID, body={"valueInputOption": "USER_ENTERED", "data": updates}
    ).execute()

    print(
        f"Week {idx + 1} ({week_start}–{week_end_capped}) written to column {col}:\n"
        f"  SLA: {sla_pct_str} | {sla_over30_str}\n"
        f"  DFY: {dfy_str}\n"
        f"  Check-in: {checkin_str} | {checkin_ss11b_str}"
    )


if __name__ == "__main__":
    main()
