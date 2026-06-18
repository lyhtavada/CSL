#!/usr/bin/env python3
"""
fetch_ts_elite.py — TS Elite usage cho CS weekly report (team G2, theo app).

TS Elite = agent CS dùng để investigate case (agent.avada-ts.site). Mỗi "chat" = 1
cuộc hội thoại CS hỏi agent. Report cho team G2 biết: tuần qua ai dùng nhiều / ít,
và những câu hay được hỏi (cluster từ title chat).

Nguồn: GET /api/v1/chats?from=&to=&app=&page= (auth: X-API-Key = TS_ELITE_API_KEY).
  - from/to LỌC theo ngày createdAt (inclusive). app LỌC theo app slug.
  - pageSize cap 100 → paginate tới hết totalPages.
  - mỗi chat: {id, title, createdAt, app, _user, _userEmail, messageCount}.
    title = câu hỏi mở đầu của chat → dùng làm "câu hay được hỏi".

Chỉ tính CS thuộc TEAM G2 (đọc từ ~/CSL/_identity/team-g2.md, map theo email).
CSL (Liz) loại khỏi usage. Người G2 không có chat nào trong kỳ vẫn liệt kê (count 0,
flag "chưa dùng") để Liz thấy ai chưa onboard tool.

App slug ở TS Elite: Chatty = "chatty", Joy = "joy" (+ "joy-subscriptions" gộp vào Joy).

Usage:
  fetch_ts_elite.py <app> <from> <to> [--compare]   # app = chatty|joy ; date = YYYY-MM-DD (Mon..Sun)
  fetch_ts_elite.py chatty 2026-06-09 2026-06-15 --compare
  # --compare: tự pull tuần trước (lùi 7 ngày) vào key "prevWeek" để tính ▲▼.
Output: JSON ra stdout.
"""
import json
import os
import sys
import urllib.request
import urllib.parse
from collections import Counter, defaultdict

ENV_PATH = os.path.expanduser("~/CSL/.env")
TEAM_PATH = os.path.expanduser("~/CSL/_identity/team-g2.md")

# App slug ở TS Elite gộp vào "app" của report. Joy gồm cả joy-subscriptions.
APP_SLUGS = {"chatty": ["chatty"], "joy": ["joy", "joy-subscriptions"]}


def env(key):
    for line in open(ENV_PATH):
        line = line.strip()
        if line.startswith(key + "="):
            return line.split("=", 1)[1].strip()
    sys.exit(f"ERROR: {key} missing in {ENV_PATH}")


def team_g2():
    """Parse team-g2.md → list of dicts {user, display, nick, app, role}.
    user = local-part của email (= _user ở TS Elite). CSL bị loại."""
    members = []
    try:
        lines = open(TEAM_PATH).read().splitlines()
    except FileNotFoundError:
        return members
    header = None
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if set(cells) == {"---"} or all(set(c) <= {"-", ":"} for c in cells):
            continue
        row = dict(zip(header, cells))
        email = (row.get("Email") or "").lower()
        role = (row.get("Role") or "").lower()
        if "@" not in email or role == "csl":   # loại CSL (Liz)
            continue
        members.append({
            "user": email.split("@")[0],
            "display": row.get("Tên hiển thị") or row.get("Nickname (KPI)") or email,
            "nick": row.get("Nickname (KPI)") or "",
            "app": row.get("App") or "",
            "state": row.get("State") or "",
        })
    return members


def get_json(base, key, path):
    req = urllib.request.Request(base + path)
    req.add_header("X-API-Key", key)
    req.add_header("User-Agent", "cs-weekly/1.0")
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())


def fetch_chats(base, key, frm, to, app_slug):
    """Pull all chats trong [frm,to] cho 1 app slug, paginate hết."""
    rows, page = [], 1
    while True:
        q = urllib.parse.urlencode({"from": frm, "to": to, "app": app_slug,
                                    "page": page, "pageSize": 100})
        d = get_json(base, key, f"/api/v1/chats?{q}")
        rows += d.get("chats", [])
        total_pages = d.get("totalPages") or 1
        if page >= total_pages or not d.get("chats"):
            break
        page += 1
    return rows


def prev_week(frm, to):
    """Mon→Sun ngay trước [frm,to]: lùi đúng 7 ngày cả 2 mốc."""
    from datetime import date, timedelta
    f = date.fromisoformat(frm) - timedelta(days=7)
    t = date.fromisoformat(to) - timedelta(days=7)
    return f.isoformat(), t.isoformat()


def collect(app, frm, to):
    base = env("TS_ELITE_API_URL").rstrip("/")
    key = env("TS_ELITE_API_KEY")
    members = team_g2()
    g2_users = {m["user"]: m for m in members}

    # Pull chats cho mọi slug thuộc app, gộp lại
    chats = []
    for slug in APP_SLUGS.get(app, [app]):
        chats += fetch_chats(base, key, frm, to, slug)

    # Lọc chats của team G2
    g2_chats = [c for c in chats if (c.get("_user") or "") in g2_users]

    per_user = Counter(c["_user"] for c in g2_chats)
    titles_by_user = defaultdict(list)
    for c in g2_chats:
        t = (c.get("title") or "").strip()
        if t:
            titles_by_user[c["_user"]].append(t)

    # Bảng usage: mọi member G2 (kể cả 0) — top desc, ai 0 = chưa dùng
    usage = []
    for m in members:
        n = per_user.get(m["user"], 0)
        usage.append({
            "user": m["user"], "display": m["display"], "nick": m["nick"],
            "app": m["app"], "state": m["state"], "chats": n,
        })
    usage.sort(key=lambda x: (-x["chats"], x["display"]))

    active = [u for u in usage if u["chats"] > 0]
    inactive = [u for u in usage if u["chats"] == 0]

    out = {
        "app": app,
        "range": {"from": frm, "to": to},
        "totalChatsG2": len(g2_chats),
        "activeCount": len(active),
        "memberCount": len(usage),
        "top": active[:5],                              # top 5 dùng nhiều
        "least": [u for u in active[-3:]][::-1],        # 3 người dùng ít nhất (vẫn >0)
        "inactive": [{"display": u["display"], "user": u["user"]} for u in inactive],
        "usage": usage,                                 # full bảng để render
        # Câu hay được hỏi: gom tất cả title G2, lấy nguyên văn (cluster do model làm ở SKILL)
        "questions": [c.get("title", "").strip() for c in g2_chats if c.get("title")],
    }
    return out


def main():
    args = [a for a in sys.argv[1:] if a != "--compare"]
    compare = "--compare" in sys.argv
    if len(args) != 3:
        sys.exit("usage: fetch_ts_elite.py <chatty|joy> <from YYYY-MM-DD> <to YYYY-MM-DD> [--compare]")
    app, frm, to = args[0].lower(), args[1], args[2]

    out = collect(app, frm, to)
    if compare:
        pf, pt = prev_week(frm, to)
        prev = collect(app, pf, pt)
        out["prevWeek"] = {
            "range": {"from": pf, "to": pt},
            "totalChatsG2": prev["totalChatsG2"],
            "activeCount": prev["activeCount"],
        }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
