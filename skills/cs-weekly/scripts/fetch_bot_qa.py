#!/usr/bin/env python3
"""
fetch_bot_qa.py — Bot QA metrics cho CS weekly report (Joyce/Joy + Ivy/Chatty).

Lấy 2 nhóm số trên dashboard "chỉ số vận hành" CS v2 (cs2.avada.net):
  1) KPI tổng (verify coverage %, correction rate %, verify đúng %, reply bot)
     -> GET /api/obs/metrics?agent=<id>&from=&to=
  2) Top 3 người verify + top 3 người correction TRONG TUẦN (lọc created_at)
     -> GET /api/reviews?agent=<id>      (người verify = parse note "Verified by X")
     -> GET /api/corrections?agent=<id>  (người làm = created_by email -> tên)

Creds đọc từ ~/CSL/.env: CS2_API_URL + CS2_API_TOKEN.
Map email -> tên hiển thị đọc từ ~/CSL/_identity/team-g2.md.

Usage:
  fetch_bot_qa.py <app> <from> <to>      # app = chatty|joy ; date = YYYY-MM-DD (Mon..Sun)
  fetch_bot_qa.py chatty 2026-06-09 2026-06-15
Output: JSON ra stdout.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.parse
from collections import Counter

ENV_PATH = os.path.expanduser("~/CSL/.env")
TEAM_PATH = os.path.expanduser("~/CSL/_identity/team-g2.md")
APP_AGENTS = {"chatty": "chatty-agent", "joy": "joy-loyalty-agent"}


def env(key):
    for line in open(ENV_PATH):
        line = line.strip()
        if line.startswith(key + "="):
            return line.split("=", 1)[1].strip()
    sys.exit(f"ERROR: {key} missing in {ENV_PATH}")


def email_to_name():
    """Parse team-g2.md table: column 'Tên hiển thị' + 'Email'."""
    out = {}
    try:
        lines = open(TEAM_PATH).read().splitlines()
    except FileNotFoundError:
        return out
    header = None
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            try:
                i_name = header.index("Tên hiển thị")
                i_email = header.index("Email")
            except ValueError:
                return out
            continue
        if len(cells) <= max(i_name, i_email):
            continue
        email = cells[i_email].lower()
        name = cells[i_name]
        if "@" in email and name and name != "—":
            out[email] = name
    return out


def get(base, tok, path):
    req = urllib.request.Request(base + path)
    req.add_header("Authorization", f"Bearer {tok}")
    req.add_header("User-Agent", "cs-weekly/1.0")
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())


def fetch_all(base, tok, endpoint, agent):
    rows, page = [], 1
    while True:
        q = urllib.parse.urlencode({"agent": agent, "page": page})
        d = get(base, tok, f"/api/{endpoint}?{q}")
        rows += d.get("rows", [])
        if len(rows) >= d.get("total", 0) or not d.get("rows"):
            break
        page += 1
    return rows


def in_week(created_at, frm, to):
    # created_at "2026-06-18T07:55:59.600Z" -> date part; inclusive [frm, to]
    if not created_at:
        return False
    d = created_at[:10]
    return frm <= d <= to


def clean_name(s):
    """Strip ' via TS Elite' suffix and surrounding whitespace."""
    return re.sub(r"\s*via\s+TS\s+Elite\s*$", "", s, flags=re.I).strip()


def display_name(name, email, e2n):
    """Prefer team-g2 mapping by email; fall back to cleaned literal name."""
    if email:
        hit = e2n.get(email.strip().lower())
        if hit:
            return hit
    name = clean_name(name or "")
    # drop service tokens / auto reviewers
    if not name or name.startswith("token:") or "@" in name or name == "answer-guard":
        return None
    return name


def verifier_name(r, e2n):
    note = r.get("note") or ""
    m = re.search(r"Verified by\s*([^<]*?)\s*<([^>]+)>", note)
    if m:
        return display_name(m.group(1), m.group(2), e2n)
    m = re.search(r"Verified by\s*(.+)$", note)
    if m:
        return display_name(m.group(1), None, e2n)
    return None  # answer-guard / auto / no human


def prev_week(frm, to):
    """Mon→Sun ngay trước [frm,to]: lùi đúng 7 ngày cả 2 mốc (không cần Date.now)."""
    from datetime import date, timedelta
    f = date.fromisoformat(frm) - timedelta(days=7)
    t = date.fromisoformat(to) - timedelta(days=7)
    return f.isoformat(), t.isoformat()


def collect(app, frm, to):
    agent = APP_AGENTS.get(app, app)
    base, tok = env("CS2_API_URL").rstrip("/"), env("CS2_API_TOKEN")
    e2n = email_to_name()

    kpi = get(base, tok, f"/api/obs/metrics?agent={agent}&from={frm}&to={to}")
    k = kpi.get("kpi", {})
    sess = kpi.get("sessions", {})
    msgs = kpi.get("messages", {})

    # Bot resolve rate = session bot tự xử, human KHÔNG nhảy vào (cách A, Liz chốt).
    total = sess.get("total") or 0
    human = sess.get("human_active") or 0
    resolve_pct = round((total - human) / total * 100, 1) if total else None

    reviews = fetch_all(base, tok, "reviews", agent)
    corrections = fetch_all(base, tok, "corrections", agent)

    rv_week = [r for r in reviews if in_week(r.get("created_at"), frm, to)]
    cr_week = [c for c in corrections if in_week(c.get("created_at"), frm, to)]

    top_verify = Counter(n for r in rv_week if (n := verifier_name(r, e2n)))
    top_correct = Counter(
        n for c in cr_week
        if (n := display_name(c.get("created_by") or "", c.get("created_by"), e2n))
    )

    out = {
        "app": app,
        "agent": agent,
        "range": {"from": frm, "to": to},
        "handle": {
            "resolveRatePct": resolve_pct,          # session bot tự xử, human không vào
            "aiReplyCoveragePct": k.get("aiReplyCoveragePct"),
            "humanTakeoverPct": k.get("humanTakeoverPct"),
            "escalationRatePct": k.get("escalationRatePct"),
            "sessions": total,
            "inbound": msgs.get("inbound"),
            "botReplies": sess.get("bot_replies"),
        },
        "qa": {
            "verifyCoveragePct": k.get("verifyCoveragePct"),
            "correctionRatePct": k.get("correctionRatePct"),
            "verifiedInWeek": len(rv_week),
            "correctionsInWeek": len(cr_week),
            "botReplies": sess.get("bot_replies"),
            "topVerifiers": [{"name": n, "count": c} for n, c in top_verify.most_common(3)],
            "topCorrectors": [{"name": n, "count": c} for n, c in top_correct.most_common(3)],
        },
    }
    return out


def main():
    args = [a for a in sys.argv[1:] if a != "--compare"]
    compare = "--compare" in sys.argv
    if len(args) != 3:
        sys.exit("usage: fetch_bot_qa.py <chatty|joy> <from YYYY-MM-DD> <to YYYY-MM-DD> [--compare]")
    app, frm, to = args[0].lower(), args[1], args[2]

    out = collect(app, frm, to)
    if compare:
        pf, pt = prev_week(frm, to)
        out["prevWeek"] = collect(app, pf, pt)
        out["prevWeek"]["range"] = {"from": pf, "to": pt}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
