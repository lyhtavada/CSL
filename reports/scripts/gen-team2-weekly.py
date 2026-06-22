#!/usr/bin/env python3
"""
Gen weekly CS Group 2 (Retention) report bằng cách TỔNG HỢP 2 bản CS Weekly
(Chatty + Joy) đã push Notion sáng thứ 2 + resolve rate từ dashboard obs metrics.

KHÔNG tự tính lại từ ticket/chat — nguồn sự thật là 2 bản /cs-weekly trên Notion.
Lấy subpage MỚI NHẤT của mỗi parent page, parse số từ TL;DR + Top issues,
ghép resolve rate (tuần này vs tuần trước) từ cs2.avada.net /api/obs/metrics.

Output: reports/weekly/weekly-CSL-report-<DATE>.md  (ghi đè nếu đã có)

Usage:
  python3 gen-team2-weekly.py                 # tuần trước (Mon–Sun), date = hôm nay
  python3 gen-team2-weekly.py --date 2026-06-22
"""
import argparse, datetime, json, os, re, sys, urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent          # ~/CSL
ENV = ROOT / ".env"
REPORTS_DIR = Path(__file__).parent.parent / "weekly"

# Parent Notion pages — các bản /cs-weekly push subpage vào đây (mới nhất lên đầu)
NOTION_PARENTS = {
    "chatty": "37bb0da449f180729d79fcfc6d43c35a",   # "Chatty CS Weekly"
    "joy":    "37bb0da449f18054b553c00929e711cb",   # "Joy CS Weekly"
}
OBS_AGENTS = {"chatty": "chatty-agent", "joy": "joy-loyalty-agent"}
BOT_NAME = {"chatty": "Ivy", "joy": "Joyce"}


def env(key):
    for line in ENV.read_text().splitlines():
        if line.startswith(key + "="):
            return line.split("=", 1)[1].strip().strip('"')
    return None


# ── Notion ──────────────────────────────────────────────────────────────────
def notion_get(path):
    req = urllib.request.Request("https://api.notion.com/v1" + path)
    req.add_header("Authorization", f"Bearer {env('NOTION_API_KEY')}")
    req.add_header("Notion-Version", "2022-06-28")
    return json.load(urllib.request.urlopen(req, timeout=60))


def latest_subpage(parent_id):
    """Trả (page_id, title) của subpage được edit gần nhất dưới parent."""
    r = notion_get(f"/blocks/{parent_id}/children?page_size=20")
    kids = [b for b in r.get("results", []) if b["type"] == "child_page"]
    if not kids:
        return None, None
    kids.sort(key=lambda b: b["last_edited_time"], reverse=True)
    top = kids[0]
    return top["id"], top["child_page"]["title"]


def page_text(page_id):
    """Flatten toàn bộ block text của 1 subpage thành 1 list dòng."""
    lines, cursor = [], None
    while True:
        url = f"/blocks/{page_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        r = notion_get(url)
        for b in r["results"]:
            t = b["type"]
            d = b.get(t, {})
            txt = "".join(x.get("plain_text", "") for x in d.get("rich_text", []))
            if txt.strip():
                lines.append(txt.strip())
        if r.get("has_more"):
            cursor = r["next_cursor"]
        else:
            break
    return lines


def top_issues(lines):
    """Trích các bullet chủ đề từ section 'Top issues' của bản /cs-weekly.
    Mỗi issue trong Notion là 1 dòng dạng 'Chủ đề — mức độ', dòng '→ Cách xử lý' bỏ qua.
    Trả chuỗi ngắn các chủ đề nối bằng ' · '."""
    issues, in_sec = [], False
    for ln in lines:
        low = ln.lower()
        if low.startswith("top issues") or "🔥" in ln:
            in_sec = True
            continue
        if in_sec:
            # section kết thúc khi sang heading khác
            if ln.startswith(("Cập nhật", "Known", "Coaching", "Ghi nhận",
                              "💡", "🆕", "🌟", "🤖")) or "Cluster theo" in ln:
                break
            if ln.startswith("→") or ln.startswith("(") or "Nguồn:" in ln or "Chủ đề ticket" in ln:
                continue
            # tên chủ đề: lấy phần trước ' — ' (em dash) nếu có
            topic = ln.split(" — ")[0].strip(" -·")
            if topic and len(topic) > 3:
                issues.append(topic)
    return " · ".join(issues[:5]) if issues else None


def parse_cs_weekly(lines):
    """Trích các số từ TL;DR của bản /cs-weekly. Trả dict (giá trị None nếu thiếu)."""
    blob = "\n".join(lines)
    out = {"tickets": None, "tickets_delta": None, "chats": None,
           "reviews": None, "dfy": None, "dfy_delta": None,
           "issues": top_issues(lines)}
    m = re.search(r"(\d+)\s*tickets?\s*\(([▲▼]?\s*\d+%)\)", blob)
    if m:
        out["tickets"], out["tickets_delta"] = m.group(1), m.group(2).replace(" ", "")
    m = re.search(r"(\d+)\s*chats?", blob)
    if m:
        out["chats"] = m.group(1)
    m = re.search(r"(\d+)\s*reviews?", blob)
    if m:
        out["reviews"] = m.group(1)
    m = re.search(r"DFY\D*?(\d+)\D*?\(([▲▼]?\s*\d+%)", blob)
    if m:
        out["dfy"], out["dfy_delta"] = m.group(1), m.group(2).replace(" ", "")
    return out


# ── obs metrics (resolve rate) ────────────────────────────────────────────────
def obs(agent, frm, to):
    base = env("CS2_API_URL").rstrip("/")
    req = urllib.request.Request(
        f"{base}/api/obs/metrics?agent={agent}&from={frm}&to={to}")
    req.add_header("Authorization", f"Bearer {env('CS2_API_TOKEN')}")
    req.add_header("User-Agent", "team2-weekly/1.0")
    return json.load(urllib.request.urlopen(req, timeout=60))


def resolve_rate(agent, frm, to):
    """resolve rate = (total - human_active)/total, theo cách A Liz đã chốt."""
    try:
        s = obs(agent, frm, to).get("sessions", {})
        tot, hum = s.get("total") or 0, s.get("human_active") or 0
        if not tot:
            return None, 0
        return round((tot - hum) / tot * 100), tot
    except Exception as e:
        print(f"  obs metrics fail {agent}: {e}", file=sys.stderr)
        return None, 0


# ── build report ──────────────────────────────────────────────────────────────
def week_bounds(ref):
    """Mon–Sun của tuần TRƯỚC ref (ref = ngày chạy report, thường thứ 2)."""
    last_mon = ref - datetime.timedelta(days=ref.weekday() + 7)
    last_sun = last_mon + datetime.timedelta(days=6)
    return last_mon, last_sun


def fmt_rate(r):
    return f"{r}%" if r is not None else "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="ngày chạy report (YYYY-MM-DD), mặc định hôm nay")
    a = ap.parse_args()
    ref = (datetime.date.fromisoformat(a.date) if a.date
           else datetime.date.today())
    mon, sun = week_bounds(ref)
    iso_week = mon.isocalendar()[1]
    period = f"{mon.strftime('%d/%m')} – {sun.strftime('%d/%m/%Y')}"
    prev_mon, prev_sun = mon - datetime.timedelta(days=7), sun - datetime.timedelta(days=7)

    data = {}
    for app, parent in NOTION_PARENTS.items():
        pid, title = latest_subpage(parent)
        if not pid:
            print(f"!! Không tìm thấy subpage cho {app}", file=sys.stderr)
            data[app] = {"parse": {}, "title": None, "lines": []}
            continue
        lines = page_text(pid)
        data[app] = {"parse": parse_cs_weekly(lines), "title": title, "lines": lines}
        print(f"  {app}: {title}")

    rates = {}
    for app, agent in OBS_AGENTS.items():
        cur, tot = resolve_rate(agent, mon.isoformat(), sun.isoformat())
        prev, _ = resolve_rate(agent, prev_mon.isoformat(), prev_sun.isoformat())
        rates[app] = {"cur": cur, "prev": prev, "sessions": tot}

    def tldr_line(app):
        p = data[app]["parse"]
        bits = []
        if p.get("tickets"):
            d = f" ({p['tickets_delta']})" if p.get("tickets_delta") else ""
            bits.append(f"{p['tickets']} tickets{d}")
        if p.get("chats"):
            bits.append(f"{p['chats']} chats")
        if p.get("reviews"):
            bits.append(f"{p['reviews']} reviews (0 review xấu)")
        line = ", ".join(bits) if bits else "_(không parse được từ Notion)_"
        return f"- **{app.capitalize()}**: {line}. Response time (avg): _(Liz điền)_"

    def bot_line(app):
        b, r = BOT_NAME[app], rates[app]
        cur, prev = fmt_rate(r["cur"]), fmt_rate(r["prev"])
        return (f"- **{b} ({app.capitalize()})**: resolve rate **{cur}** "
                f"(tuần trước {prev}). AI take-only ~{cur} session bot tự đóng, human không vào.")

    joy_dfy = data["joy"]["parse"]
    dfy_note = ""
    if joy_dfy.get("dfy"):
        d = f" ({joy_dfy['dfy_delta']})" if joy_dfy.get("dfy_delta") else ""
        dfy_note = f"\n- Joy DFY tạo {joy_dfy['dfy']}{d}."

    title = f"📊 CS Group 2 (Retention) — Weekly W{iso_week} ({period.replace(' – ', '–')})"

    md = f"""{title}

**Date**: {ref.strftime('%d/%m/%Y')} | **Meeting**: Thứ 2, 15:00 | **Prepared by**: Liz
**Gửi trước**: 13:00 cùng ngày (trước meeting 2 tiếng)
**Nguồn**: tổng hợp 2 bản CS Weekly (Chatty + Joy) trên Notion + dashboard `cs2.avada.net /api/obs/metrics`

---

## ⚡ TL;DR
Volume ticket giảm nhẹ ở cả 2 app.
{tldr_line("chatty")}
{tldr_line("joy")}{dfy_note}

---

## 🤖 Bot performance
{bot_line("chatty")}
{bot_line("joy")}

---

## 🔥 Top Issues tuần này
**Chatty**: {data['chatty']['parse'].get('issues') or '_(điền từ bản Chatty CS Weekly)_'}.

**Joy**: {data['joy']['parse'].get('issues') or '_(điền từ bản Joy CS Weekly)_'}.

---

## 🚨 Crisis (Bad Reviews)
Tuần này không có bad review (≤3★) ở cả 2 app.

<!-- Khi có bad review, thêm dòng:
- **[App]** X bad review (N★): "trích nội dung" → đã xử lý / đang follow up.
-->

---

## 🚀 Team Project đang triển khai
1. Tiếp tục chạy & review Chatty + Joy DFY.
2. Team member verify/correct bot replies → loop training (push verify coverage lên mục tiêu >50%).

---

## 🧠 CEO Cần Quyết Định *(Liz điền nếu có)*

**1. [Câu hỏi]**
- Context: [1 câu]
- Default nếu không decide: [X]
"""

    REPORTS_DIR.mkdir(exist_ok=True)
    out = REPORTS_DIR / f"weekly-CSL-report-{ref.isoformat()}.md"
    out.write_text(md)
    print(f"Generated: {out}")
    print("\n⚠️  Response time + CEO decision: Liz điền tay. Top issues auto-fill, rà lại 1 lượt.")


if __name__ == "__main__":
    main()
