"""Step 3: After Claude writes /tmp/csdaily/reviews.json (review-detect results:
list of {id, asked, outcome, note}), this script computes shift status, renders the
full report, and posts it to Liz via Slack DM.

Usage:
  python3 render.py          → render + post to Slack DM
  python3 render.py --print  → render + print only (no Slack)
"""
import os, sys, json
from collections import Counter, defaultdict
from common import (load_env, api_get, short_plan, window, parse_iso,
                    EMAIL2NICK, TEAM, VN)
import datetime as dt
import urllib.request

OUT = "/tmp/csdaily"
# Post target: #cs-2-daily channel (bot must be invited). Falls back to Liz DM if unset.
SLACK_TARGET = "C0B8042TXQ9"
PLAN_RANK = {"Enterprise": 0, "Advanced": 1, "Plus": 2, "Pro": 3, "Basic": 4}
SEV_RANK = {"unanswered": 0, "needs_improve": 1, "good": 2, "excellent": 3}


def plan_tag(x):
    sp = short_plan(x.get("plan"))
    return f"({sp} ✅)" if x.get("paid") else f"({sp})"


def nm(x):
    return x.get("shopname") or x.get("cust") or x.get("domain")


def shift_status(env, win_start, win_end, start_date, end_date):
    late, miss_in, miss_out = [], [], []
    shifts = api_get(env, f"/shifts?start={start_date}&end={end_date}").get("data", [])
    for sh in shifts:
        st, en = parse_iso(sh["start"]), parse_iso(sh["end"])
        if en < win_start or st > win_end:
            continue
        g2 = [c for c in sh.get("cs", []) if "G2" in (c.get("groupLabel") or "")]
        if not g2:
            continue
        checks = api_get(env, f"/shifts/{sh['id']}/checks").get("data", [])
        bye = defaultdict(dict)
        for ch in checks:
            bye[ch["email"]][ch["type"]] = ch
        for c in g2:
            em = c["email"]; nick = EMAIL2NICK.get(em, c.get("name", "?"))
            ci = bye[em].get("checkin"); co = bye[em].get("checkout")
            t = sh["title"]
            if not ci:
                miss_in.append((nick, t))
            else:
                m = int((parse_iso(ci["createdAt"]) - st).total_seconds() / 60)
                if m > 5:
                    late.append((nick, t, m))
                if not co:
                    miss_out.append((nick, t))
    return late, miss_in, miss_out


def build(env):
    win = json.load(open(f"{OUT}/window.json"))
    s = json.load(open(f"{OUT}/enriched.json"))
    rv = {r["id"]: r for r in json.load(open(f"{OUT}/reviews.json"))}
    byid = {x["id"]: x for x in s}

    ws, we = window(dt.datetime.strptime(win["end_date"], "%Y-%m-%d").replace(hour=9, tzinfo=VN))
    late, miss_in, miss_out = shift_status(env, ws, we, win["start_date"], win["end_date"])

    joy = [x for x in s if x["app"] == "Joy"]
    chatty = [x for x in s if x["app"] == "Chatty"]
    L = []
    L.append("📊 BÁO CÁO CS HÀNG NGÀY")
    L.append(f"📅 {win['start_vn']} - {win['end_vn']}")
    L.append("")
    L.append("TỔNG QUAN")
    L.append(f"• Total: {len(s)} conversations")
    L.append(f"• Joy Loyalty: {len(joy)} | Chatty: {len(chatty)}")
    L.append("")
    L.append("⏰ CHECKIN / CHECKOUT (Team G2)")
    if late:
        L.append("🔴 Checkin muộn:")
        for nick, t, m in sorted(late, key=lambda x: -x[2]):
            L.append(f"  • {nick} — {t} (muộn {m}p)")
    if miss_in:
        L.append("⛔ Miss checkin:")
        for nick, t in miss_in:
            L.append(f"  • {nick} — {t}")
    if miss_out:
        L.append("🚪 Miss checkout:")
        for nick, t in miss_out:
            L.append(f"  • {nick} — {t}")
    if not (late or miss_in or miss_out):
        L.append("  ✅ Tất cả OK")
    L.append("")
    L.append("---")
    L.append("")

    def top_issues(arr, label):
        L.append(f"TOP ISSUES — {label}")
        L.append("")
        cnt = Counter(x["issue"] for x in arr)
        ranked = sorted(arr, key=lambda x: (not x.get("paid"), not x["needs_followup"], -cnt[x["issue"]]))
        for i, x in enumerate(ranked[:4], 1):
            flag = " ⚠️" if x["needs_followup"] else ""
            L.append(f"{i}. {x['issue']} — {nm(x)} {plan_tag(x)}")
            L.append(f"   {x['topic']}. CS ({x['cs_nick']}): {x['quality_note']}{flag}")
            L.append("")

    top_issues(joy, "JOY LOYALTY")
    L.append("---"); L.append("")
    top_issues(chatty, "CHATTY")
    L.append("---"); L.append("")

    paid_fu = [x for x in s if x.get("paid") and x["needs_followup"]]
    paid_fu.sort(key=lambda x: (PLAN_RANK.get(short_plan(x.get("plan")), 9), SEV_RANK.get(x["quality"], 9)))
    L.append("⚠️ PAID PLANS — TOP 3 CẦN FOLLOW-UP")
    L.append("")
    for x in paid_fu[:3]:
        L.append(f"🟢 {nm(x)} {plan_tag(x)} — {x['issue']}. CS: {x['cs_nick']}")
        L.append(f"   {x['quality_note']}")
        L.append("")
    if len(paid_fu) > 3:
        L.append(f"   (+{len(paid_fu)-3} paid shop khác cần follow-up)")
    L.append("")
    L.append("---")
    L.append("")

    # review
    asks = [(rid, r) for rid, r in rv.items() if r["asked"]]
    got = [(rid, r) for rid, r in asks if r["outcome"] == "got"]
    declined = [(rid, r) for rid, r in asks if r["outcome"] == "declined"]
    noresp = [(rid, r) for rid, r in asks if r["outcome"] == "no_response"]

    def info(rid):
        x = byid.get(rid, {})
        return (nm(x) if x else rid), x.get("cs_nick", "?")

    L.append("⭐ XIN REVIEW (trong session)")
    L.append("")
    L.append(f"• CS đã xin review: {len(asks)} session")
    L.append(f"• ✅ Xin được: {len(got)} | ⏳ Chưa phản hồi: {len(noresp)} | ❌ Từ chối: {len(declined)}")
    L.append("")
    if got:
        L.append("✅ Xin được:")
        for rid, r in got:
            shop, cs = info(rid)
            L.append(f"  • {shop} — CS: {cs}. {r['note']}")
        L.append("")
    if declined:
        L.append("❌ Bị từ chối:")
        for rid, r in declined:
            shop, cs = info(rid)
            L.append(f"  • {shop} — CS: {cs}. {r['note']}")
        L.append("")
    if noresp:
        L.append("⏳ Xin nhưng chưa phản hồi (cần follow-up):")
        for rid, r in noresp:
            shop, cs = info(rid)
            L.append(f"  • {shop} — CS: {cs}. {r['note']}")
        L.append("")
    L.append("---")
    L.append("")

    good = [x for x in s if x["quality"] in ("excellent", "good")]
    bad = [x for x in s if x["quality"] in ("needs_improve", "unanswered") and x["cs_nick"] in TEAM]
    exc = [x for x in s if x["quality"] == "excellent"]
    L.append("👥 CS PERFORMANCE")
    L.append("")
    L.append("✅ Tốt:")
    for x in exc[:3]:
        L.append(f"• {x['issue']}: CS ({x['cs_nick']}) {x['quality_note']}")
    L.append(f"• +{max(len(good)-3,0)} cases handled well")
    L.append("")
    L.append("⚠️ Cần cải thiện:")
    for x in bad:
        L.append(f"• {nm(x)} ({x['cs_nick']}): {x['quality_note']}")
    L.append("")
    L.append("---")
    L.append("")

    setup = sum(1 for x in s if "Setup" in x["issue"])
    bugs = sum(1 for x in s if x["issue"] == "Bug")
    active = sorted({x["cs_nick"] for x in s if x["cs_nick"] in TEAM})
    pct = round(100 * len(got) / max(len(asks), 1))
    L.append("💡 INSIGHT")
    L.append(f"• {setup} setup questions → cần improve onboarding docs")
    L.append(f"• {bugs} bug reports → theo dõi escalation với dev")
    L.append(f"• {len(asks)} lần xin review, {len(got)} thành công ({pct}%) → {len(noresp)} session cần nhắc lại")
    L.append(f"• {len(paid_fu)} paid customers cần follow-up → ưu tiên trong 24h")
    L.append(f"• Agents active (G2): {', '.join(active)}")
    return "\n".join(L)


def post_slack(env, text):
    tok = env["SLACK_BOT_TOKEN_AVADA"]
    ch = SLACK_TARGET
    # Slack message limit ~40k chars; chunk on section dividers if needed
    chunks = []
    cur = ""
    for block in text.split("\n---\n"):
        piece = ("\n---\n" if cur else "") + block
        if len(cur) + len(piece) > 3500:
            chunks.append(cur); cur = block
        else:
            cur += piece
    if cur:
        chunks.append(cur)
    for c in chunks:
        req = urllib.request.Request("https://slack.com/api/chat.postMessage",
            data=json.dumps({"channel": ch, "text": c, "unfurl_links": False}).encode(),
            headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"})
        res = json.load(urllib.request.urlopen(req))
        if not res.get("ok"):
            print("SLACK ERROR:", res.get("error"))
            return False
    return True


def main():
    env = load_env()
    report = build(env)
    open(f"{OUT}/report.txt", "w").write(report)
    if "--print" in sys.argv:
        print(report)
    else:
        ok = post_slack(env, report)
        print("Posted to Slack DM:", ok)


if __name__ == "__main__":
    main()
