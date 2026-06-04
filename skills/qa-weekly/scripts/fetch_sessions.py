#!/usr/bin/env python3
"""
Fetch Crisp sessions for a given week from the Public Admin API, group by CS,
filter to Team G2 members, sample up to 30 per CS.

Usage:
  python3 fetch_sessions.py --start 2026-05-26 --end 2026-06-01 \
      --out /tmp/qa_weekly_sessions.json [--sample 30]

Output JSON shape:
  {
    "period": {"start": "...", "end": "...", "iso_week": "2026-W22"},
    "by_cs": {
      "Hazel": {
        "slack_id": "U09FYACFH2T", "email": "hienpt@avadagroup.com",
        "total": 47, "sampled": 30,
        "sessions": [{"session_id": "...", "website_id": "...",
                      "shopifyDomain": "...", "customerEmail": "...",
                      "createdAt": "...", "segments": [...]}, ...]
      }, ...
    }
  }
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.request

API_BASE = "https://us-central1-avada-crm.cloudfunctions.net/publicAdminApi/api"

# Joy + Chatty retention website. Team G2 handles these.
# We do NOT hard-filter on website here — we keep all apps a G2 CS handled,
# since the rubric covers both Joy and Chatty.

TEAM_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                         "_identity", "team-g2.md")


def load_env(path):
    """Minimal .env loader (KEY=VALUE, ignores quotes/comments)."""
    env = {}
    if not os.path.exists(path):
        return env
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def load_team_roster(path):
    """Parse team-g2.md markdown table → {nickname: {slack_id, email, name, app}}.

    Maps the Crisp 'Tên hiển thị' (display name = agentUser.nickname in
    crispSessions) to Slack ID + email.
    """
    roster = {}
    if not os.path.exists(path):
        print(f"WARN: roster not found at {path}", file=sys.stderr)
        return roster
    with open(path) as f:
        for line in f:
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # Header / separator rows
            if len(cells) < 11 or cells[0] in ("#", "") or set(cells[0]) <= {"-"}:
                continue
            # Columns: # | Tên | Role | App | State | Nickname(KPI) | Slack ID |
            #          Trello | Tên hiển thị | Email | ...
            try:
                slack_id = cells[6]
                display = cells[8]   # "Tên hiển thị" = Crisp nickname
                email = cells[9]
                app = cells[3]
                name = cells[1]
            except IndexError:
                continue
            if not display or not slack_id.startswith("U"):
                continue
            roster[display] = {
                "slack_id": slack_id,
                "email": email,
                "name": name,
                "app": app,
            }
    return roster


def iso_week(date_str):
    d = dt.date.fromisoformat(date_str)
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def _fetch_range(token, start, end, limit=3000):
    """Single /crispSessions call for a [start, end) date range.

    NOTE: the API's `page`/`cursor` params are ignored server-side — only
    `limit` is honored (caps ~2000/call). So we never paginate a single call;
    instead the caller chunks the week into day-sized ranges (see
    fetch_sessions) so each call stays under the cap.
    """
    url = (f"{API_BASE}/crispSessions?start={start}&end={end}&limit={limit}")
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode()).get("data", [])


def fetch_sessions(token, start, end):
    """Fetch all sessions in [start, end] by querying one day at a time and
    merging (dedup by session_id). Day chunks keep each call under the
    server-side ~2000-record cap so nothing is silently dropped."""
    all_sessions = []
    seen = set()
    d0 = dt.date.fromisoformat(start)
    d1 = dt.date.fromisoformat(end)
    day = d0
    while day <= d1:
        nxt = day + dt.timedelta(days=1)
        try:
            batch = _fetch_range(token, day.isoformat(), nxt.isoformat())
        except Exception as e:
            print(f"ERROR fetching {day}: {e}", file=sys.stderr)
            batch = []
        kept = 0
        for s in batch:
            sid = s.get("session_id")
            if sid and sid not in seen:
                seen.add(sid)
                all_sessions.append(s)
                kept += 1
        if len(batch) >= 2000:
            print(f"WARN: {day} hit {len(batch)} records — may be capped, "
                  f"some sessions could be missing", file=sys.stderr)
        print(f"  {day}: {kept} new ({len(batch)} returned)", file=sys.stderr)
        day = nxt
    return all_sessions


def sample(lst, n, seed):
    """Deterministic sample of n items (no Math.random equivalent needed —
    stable across reruns for the same week)."""
    if len(lst) <= n:
        return lst
    # Stable stride sampling, seeded by week so reruns match.
    step = len(lst) / n
    return [lst[int(i * step)] for i in range(n)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD (Monday)")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD (Sunday)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--sample", type=int, default=30)
    ap.add_argument("--env", default=os.path.join(
        os.path.dirname(__file__), "..", "..", "..", ".env"))
    args = ap.parse_args()

    env = load_env(args.env)
    token = env.get("AVD_TOKEN") or os.environ.get("AVD_TOKEN")
    if not token:
        print("ERROR: AVD_TOKEN not found in .env or environment",
              file=sys.stderr)
        sys.exit(1)

    roster = load_team_roster(TEAM_FILE)
    if not roster:
        print("ERROR: empty roster — cannot map CS to Slack", file=sys.stderr)
        sys.exit(1)

    sessions = fetch_sessions(token, args.start, args.end)
    print(f"Fetched {len(sessions)} unique sessions for {args.start}..{args.end}",
          file=sys.stderr)

    by_cs = {}
    for s in sessions:
        nick = (s.get("agentUser") or {}).get("nickname")
        if not nick or nick not in roster:
            continue  # skip AI-bot/unassigned and non-G2 agents
        by_cs.setdefault(nick, []).append({
            "session_id": s.get("session_id"),
            "website_id": s.get("website_id"),
            "shopifyDomain": s.get("shopifyDomain"),
            "customerEmail": s.get("customerEmail"),
            "createdAt": s.get("createdAt"),
            "segments": s.get("segments", []),
        })

    out = {
        "period": {"start": args.start, "end": args.end,
                   "iso_week": iso_week(args.start)},
        "by_cs": {},
    }
    for nick, sess in sorted(by_cs.items()):
        info = roster[nick]
        sampled = sample(sess, args.sample, seed=args.start)
        out["by_cs"][nick] = {
            "slack_id": info["slack_id"],
            "email": info["email"],
            "name": info["name"],
            "app": info["app"],
            "total": len(sess),
            "sampled": len(sampled),
            "sessions": sampled,
        }

    with open(args.out, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(out['by_cs'])} CS → {args.out}", file=sys.stderr)
    for nick, d in out["by_cs"].items():
        print(f"  {nick}: {d['sampled']}/{d['total']} chats", file=sys.stderr)


if __name__ == "__main__":
    main()
