#!/usr/bin/env python3
"""
fetch_corrections.py — pull bot corrections (câu bot trả bị human CS sửa) từ CS v2
cho 1 hoặc nhiều app, lọc theo cửa sổ tuần, group theo topic, map người sửa → tên,
rồi build report markdown để Liz dùng update data cho bot.

Nguồn: GET /api/corrections?agent=<id>&page=N  (cs2.avada.net)
  rows[]: id, question, original_response, corrected_response, context, tags,
          status, created_by (email), created_at (ISO), source_session_id, ...

Auth: Authorization: Bearer <CS2_API_TOKEN>  (super_admin) + User-Agent header.
Creds đọc từ ~/CSL/.env (CS2_API_URL, CS2_API_TOKEN).

Cửa sổ mặc định = tuần TRƯỚC trọn vẹn (Mon 00:00 → Sun 23:59:59 local).
Lọc theo created_at (lúc correction được tạo).

Usage:
  python3 fetch_corrections.py                       # cả Joy + Chatty, tuần trước
  python3 fetch_corrections.py --apps joy            # chỉ Joy
  python3 fetch_corrections.py --start 2026-06-16 --end 2026-06-22
  python3 fetch_corrections.py --out reports/bot-corrections   # thư mục output

In ra danh sách đường dẫn file đã ghi (1 dòng / app).
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

ENV_PATH = os.path.expanduser("~/CSL/.env")
REPO = os.path.expanduser("~/CSL")
TEAM_FILE = os.path.join(REPO, "_identity", "team-g2.md")

APP_AGENTS = {
    "joy": ("joy-loyalty-agent", "Joyce"),
    "chatty": ("chatty-agent", "Ivy"),
}


def load_creds():
    url = token = None
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("CS2_API_URL="):
                    url = line.split("=", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("CS2_API_TOKEN="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        sys.exit(f"ERROR: {ENV_PATH} not found")
    if not url or not token:
        sys.exit("ERROR: CS2_API_URL / CS2_API_TOKEN missing in ~/CSL/.env")
    return url.rstrip("/"), token


def load_email_map():
    """email (lowercase) -> tên hiển thị, parse từ team-g2.md."""
    m = {}
    try:
        text = Path(TEAM_FILE).read_text(encoding="utf-8")
    except FileNotFoundError:
        return m
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # cột: ... | Tên hiển thị | Email | ...  (header có 'Email')
        for c in cells:
            em = c.lower()
            if "@" in em and "." in em:
                # tên hiển thị nằm ngay TRƯỚC cột email
                idx = cells.index(c)
                if idx > 0:
                    m[em] = cells[idx - 1]
    return m


def display_name(email, email_map):
    if not email:
        return "—"
    return email_map.get(email.lower(), email)


_EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def editor_of(row, email_map):
    """Người sửa thật: created_by nếu là email; nếu là token (vd 'token:Avada CS
    Team') thì parse email trong context ('...Submitted via TS Elite by <email>')."""
    cb = (row.get("created_by") or "").strip()
    if "@" in cb and not cb.lower().startswith("token:"):
        return display_name(cb, email_map)
    ctx = row.get("context") or ""
    m = _EMAIL_RE.search(ctx)
    if m:
        return display_name(m.group(0), email_map)
    # bỏ tiền tố token: cho gọn
    return cb.split(":", 1)[1].strip() if cb.lower().startswith("token:") else (cb or "—")


def fetch_all_corrections(base, token, agent):
    rows = []
    page = 1
    while True:
        url = f"{base}/api/corrections?agent={agent}&page={page}"
        req = urllib.request.Request(
            url,
            headers={"Authorization": f"Bearer {token}", "User-Agent": "bot-corrections/1.0"},
        )
        d = json.load(urllib.request.urlopen(req, timeout=60))
        batch = d.get("rows", [])
        rows.extend(batch)
        total = d.get("total", len(rows))
        page_size = d.get("pageSize", 20)
        if len(rows) >= total or not batch:
            break
        page += 1
        if page > 200:
            break
    return rows


def parse_iso(s):
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        d = dt.datetime.fromisoformat(s)
    except ValueError:
        return None
    # về local naive để so với window naive
    if d.tzinfo is not None:
        d = d.astimezone().replace(tzinfo=None)
    return d


def last_week_window():
    """Mon 00:00 → Sun 23:59:59 của tuần trước (local)."""
    today = dt.date.today()
    monday_this = today - dt.timedelta(days=today.weekday())
    start = monday_this - dt.timedelta(days=7)
    end = start + dt.timedelta(days=6)
    start_dt = dt.datetime.combine(start, dt.time.min)
    end_dt = dt.datetime.combine(end, dt.time.max)
    return start_dt, end_dt


# tag nguồn (kênh submit) — KHÔNG phải topic nội dung, bỏ qua khi gom nhóm
SOURCE_TAGS = {"ts-elite", "crisp", "slack", "manual", "api"}


def topic_of(row):
    """Topic gom nhóm: ưu tiên tag nội dung, fallback heuristic theo từ khóa câu hỏi."""
    tags = row.get("tags")
    tag_list = []
    if isinstance(tags, list):
        tag_list = [str(t).strip().lower() for t in tags if str(t).strip()]
    elif isinstance(tags, str) and tags.strip():
        tag_list = [t.strip().lower() for t in tags.split(",") if t.strip()]
    for t in tag_list:
        if t not in SOURCE_TAGS and not t.startswith("src:") and not t.startswith("source:"):
            return t
    q = (row.get("question") or "").lower()
    buckets = [
        ("pricing/plan", ["price", "pricing", "plan", "cost", "billing", "charge", "refund", "upgrade", "downgrade"]),
        ("points/earning", ["point", "earn", "reward", "redeem", "vip", "tier"]),
        ("setup/config", ["setup", "set up", "configure", "install", "enable", "turn on", "settings"]),
        ("loyalty page/widget", ["loyalty page", "widget", "launcher", "on-site", "display", "theme"]),
        ("referral", ["referral", "refer", "invite"]),
        ("integration", ["integrat", "klaviyo", "shopify", "pos", "email", "api"]),
        ("chat/inbox", ["chat", "inbox", "message", "live chat", "agent", "reply"]),
    ]
    for name, kws in buckets:
        if any(k in q for k in kws):
            return name
    return "khác"


def short(s, n=600):
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def build_report(app, agent, bot_name, rows, start_dt, end_dt, email_map):
    win = [r for r in rows if (d := parse_iso(r.get("created_at"))) and start_dt <= d <= end_dt]
    win.sort(key=lambda r: r.get("created_at") or "")

    groups = defaultdict(list)
    for r in win:
        groups[topic_of(r)].append(r)

    by_person = defaultdict(int)
    for r in win:
        by_person[editor_of(r, email_map)] += 1

    period = f"{start_dt.date():%d/%m/%Y} → {end_dt.date():%d/%m/%Y}"
    L = []
    L.append(f"# Bot Corrections — {bot_name} ({app.capitalize()})")
    L.append("")
    L.append(f"**Tuần:** {period}  ·  **Tổng correction:** {len(win)}")
    L.append("")
    L.append("> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.")
    L.append("")

    # ---- TL;DR theo topic ----
    L.append("## 📌 Tóm tắt theo topic")
    L.append("")
    if not win:
        L.append("_Không có correction nào trong tuần._")
        L.append("")
    else:
        for topic, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            L.append(f"### {topic} — {len(items)} câu")
            for r in items[:3]:
                q = short(r.get("question"), 140).replace("\n", " ")
                L.append(f"- {q}")
            if len(items) > 3:
                L.append(f"- … +{len(items) - 3} câu khác (xem chi tiết bên dưới)")
            L.append("")
        # người sửa
        ppl = ", ".join(f"{n} ({c})" for n, c in sorted(by_person.items(), key=lambda kv: -kv[1]))
        L.append(f"**Người sửa:** {ppl}")
        L.append("")

    # ---- Full list ----
    L.append("---")
    L.append("")
    L.append("## 📋 Chi tiết từng correction")
    L.append("")
    if not win:
        L.append("_(trống)_")
    for i, r in enumerate(win, 1):
        who = editor_of(r, email_map)
        when = (parse_iso(r.get("created_at")) or dt.datetime.min).strftime("%d/%m %H:%M")
        topic = topic_of(r)
        sess = r.get("source_session_id") or ""
        L.append(f"### {i}. [{topic}] — {who} · {when}")
        L.append("")
        L.append(f"**Q:** {short(r.get('question'), 400)}")
        L.append("")
        L.append("**Bot trả (sai/thiếu):**")
        L.append("")
        L.append("```")
        L.append(short(r.get("original_response"), 1200))
        L.append("```")
        L.append("")
        L.append("**CS sửa thành:**")
        L.append("")
        L.append("```")
        L.append(short(r.get("corrected_response"), 1200))
        L.append("```")
        ctx = (r.get("context") or "").strip()
        if ctx:
            L.append("")
            L.append(f"**Context:** {short(ctx, 300)}")
        if sess:
            L.append("")
            L.append(f"_session: `{sess}`_")
        L.append("")
    return "\n".join(L), len(win)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apps", nargs="+", default=["joy", "chatty"], help="joy chatty (mặc định cả 2)")
    ap.add_argument("--start", help="YYYY-MM-DD (mặc định = thứ 2 tuần trước)")
    ap.add_argument("--end", help="YYYY-MM-DD (mặc định = chủ nhật tuần trước)")
    ap.add_argument("--out", default=os.path.join(REPO, "reports", "bot-corrections"))
    args = ap.parse_args()

    if args.start and args.end:
        start_dt = dt.datetime.combine(dt.date.fromisoformat(args.start), dt.time.min)
        end_dt = dt.datetime.combine(dt.date.fromisoformat(args.end), dt.time.max)
    else:
        start_dt, end_dt = last_week_window()

    base, token = load_creds()
    email_map = load_email_map()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    week_tag = f"{start_dt.date():%Y-%m-%d}"
    written = []
    for app in args.apps:
        app = app.lower().strip()
        if app not in APP_AGENTS:
            print(f"SKIP unknown app: {app}", file=sys.stderr)
            continue
        agent, bot_name = APP_AGENTS[app]
        rows = fetch_all_corrections(base, token, agent)
        md, n = build_report(app, agent, bot_name, rows, start_dt, end_dt, email_map)
        path = out_dir / f"{app}-corrections-{week_tag}.md"
        path.write_text(md, encoding="utf-8")
        written.append(str(path))
        print(f"{app}: {n} correction(s) → {path}")

    return written


if __name__ == "__main__":
    main()
