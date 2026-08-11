#!/usr/bin/env python3
"""
fetch_bot_qa.py — Bot performance metrics cho CS weekly report (Joyce/Joy + Ivy/Chatty).

Trả 2 nhóm (output JSON: {handle, qa, [prevWeek]}):
  HANDLE (vận hành) — từ GET /api/obs/metrics?agent=<id>&from=&to= (dashboard "chỉ số vận hành")
  + GET /api/obs/sessions (cùng range) để tự tính take-only. Report 2 chỉ số song song:
    - aiResolvedPct  = kpi.aiResolvedPct của API = ai_resolved/ai_replied.
      ĐO CHẤT LƯỢNG BOT. Khớp đúng số dashboard cs2 nên đối chiếu được.
    - takeOnlyPct    = % session bot chạy trọn mà CS không phải đụng tay
      = (session không human_active, không escalated, không no_ai, bot có reply)/ai_replied.
      ĐO TẢI NHÂN SỰ. Cùng mẫu số ai_replied để so trực tiếp với aiResolvedPct.
    - unclearGapPct  = takeOnlyPct − aiResolvedPct = vùng merchant im lặng, không rõ
      có được giúp không. Phình ra = bot nói nhiều mà không chốt được vấn đề.
    - aiReplyCoveragePct / humanTakeoverPct / escalationRatePct (lấy thẳng kpi)
    - sessions / inbound / botReplies (volume)
  QA (chất lượng) — verify/correction do human CS làm:
    - verifyCoveragePct / correctionRatePct (từ /api/obs/metrics)
    - verifiedInWeek / correctionsInWeek (đếm row có created_at trong tuần)
    - topVerifiers (top 3, parse note "Verified by X" từ /api/reviews)
    - topCorrectors (top 3, created_by email từ /api/corrections)

Creds đọc từ ~/CSL/.env: CS2_API_URL + CS2_API_TOKEN.
Map email -> tên hiển thị đọc từ ~/CSL/_identity/team-g2.md.

Usage:
  fetch_bot_qa.py <app> <from> <to> [--compare]   # app = chatty|joy|wishlist ; date = YYYY-MM-DD (Mon..Sun)
  fetch_bot_qa.py chatty 2026-06-09 2026-06-15 --compare
  # --compare: tự pull tuần trước (lùi 7 ngày) vào key "prevWeek" để tính ▲▼.
Output: JSON ra stdout.
"""
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
from collections import Counter

ENV_PATH = os.path.expanduser("~/CSL/.env")
TEAM_PATH = os.path.expanduser("~/CSL/_identity/team-g2.md")
APP_AGENTS = {
    "chatty": "chatty-agent",
    "joy": "joy-loyalty-agent",
    "wishlist": "wishlist-agent",
}


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


def get(base, tok, path, tries=4):
    """GET + retry: /api/obs/sessions phải phân trang nên hay timeout lẻ tẻ."""
    for i in range(tries):
        try:
            req = urllib.request.Request(base + path)
            req.add_header("Authorization", f"Bearer {tok}")
            req.add_header("User-Agent", "cs-weekly/1.0")
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(3 * (i + 1))


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


def session_rows(base, tok, agent, frm, to):
    """Mọi session trong range, mỗi row có cờ escalated / human_active / no_ai.
    Endpoint bỏ qua filter param nên phải kéo hết rồi tự lọc."""
    rows, page = [], 1
    while True:
        q = urllib.parse.urlencode({"agent": agent, "from": frm, "to": to,
                                    "page": page, "pageSize": 50})
        d = get(base, tok, f"/api/obs/sessions?{q}")
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

    total = sess.get("total") or 0
    ai_replied = sess.get("ai_replied") or 0

    # Hai chỉ số song song, trả lời hai câu hỏi khác nhau (Liz chốt 2026-08-11):
    #   aiResolvedPct → chất lượng bot   | takeOnlyPct → tải nhân sự
    #
    # Công thức cũ (total − human_active)/total đã BỎ vì thổi phồng ~15 điểm: nó
    # đếm cả session bot đã escalate (CS xử qua ticket/email nên human_active vẫn
    # false — Chatty 57 ca, Joy 17 ca tuần 03–09/08) lẫn session no_ai (bot không
    # chạy) vào tử số. Nó cũng chia cho total trong khi API chia cho ai_replied,
    # nên lệch dashboard cs2 ở cả tử lẫn mẫu.
    #
    # takeOnlyPct dùng CHUNG mẫu số ai_replied với aiResolvedPct để 2 số so trực
    # tiếp được. Nó là CẬN TRÊN, không phải ước lượng đúng: session merchant im
    # lặng sau khi bot nudge vẫn được tính (tuần 03–09/08: 54% session trong bucket
    # này của Ivy kết thúc bằng câu bỏ ngỏ kiểu "Still there?" không ai trả lời).
    rows = session_rows(base, tok, agent, frm, to)
    take_only = [r for r in rows
                 if not r.get("human_active")
                 and not r.get("escalated")
                 and not r.get("no_ai")
                 and (r.get("bot_reply_count") or 0) > 0]
    take_only_pct = round(len(take_only) / ai_replied * 100, 1) if ai_replied else None
    ai_resolved_pct = k.get("aiResolvedPct")
    gap = (round(take_only_pct - ai_resolved_pct, 1)
           if take_only_pct is not None and ai_resolved_pct is not None else None)

    review_sessions = fetch_all(base, tok, "reviews", agent)
    corrections = fetch_all(base, tok, "corrections", agent)

    # /api/reviews groups by session_id: each row's own created_at/note live
    # nested per-review inside row["reviews"], NOT on the row itself.
    reviews = [rv for row in review_sessions for rv in row.get("reviews", [])]

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
            "aiResolvedPct": ai_resolved_pct,       # API — chất lượng bot, khớp dashboard
            "takeOnlyPct": take_only_pct,           # tự tính — CS không phải đụng tay
            "unclearGapPct": gap,                   # vùng merchant im lặng, không rõ kết quả
            "takeOnlySessions": len(take_only),
            "aiReplied": ai_replied,
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
        sys.exit("usage: fetch_bot_qa.py <chatty|joy|wishlist> <from YYYY-MM-DD> <to YYYY-MM-DD> [--compare]")
    app, frm, to = args[0].lower(), args[1], args[2]

    out = collect(app, frm, to)
    if compare:
        pf, pt = prev_week(frm, to)
        out["prevWeek"] = collect(app, pf, pt)
        out["prevWeek"]["range"] = {"from": pf, "to": pt}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
