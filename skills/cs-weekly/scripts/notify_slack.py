#!/usr/bin/env python3
"""
Post a CS-weekly digest to the app's CS Slack channel via the Avada bot.

Sends a formatted message (Slack Block Kit): a header (app + week), the TL;DR text,
and a button linking to the full Notion report.

Usage:
  python3 notify_slack.py \
    --channel C0XXXXXX \
    --title "Chatty CS Weekly — W23 (01–07/06/2026)" \
    --tldr-file /tmp/chatty_tldr.txt \
    --notion-url https://www.notion.so/...

  # or pass the TL;DR inline:
  python3 notify_slack.py --channel C0.. --title "..." --tldr "Chatty tuần này..." --notion-url https://...

Auth: SLACK_BOT_TOKEN_AVADA from CSL/.env (bot = avada_bot, team Avada Group).
The bot must be a member of the target channel (invite it once if posting 404s
with not_in_channel).

By default the message is posted with Liz's name + avatar (--as-user, default ON)
so it reads as coming from Liz — the bot looks up her profile live and passes
username/icon_url. Slack still shows a small "APP" tag (unavoidable with a bot token;
only a Liz user token would remove it). Pass --no-as-user to post as the plain bot.
"""

LIZ_USER_ID = "U02GT4PC6RH"  # Hoàng Thị Ly / Ly (Liz)
import os, sys, json, argparse
import requests
from dotenv import load_dotenv

ENV_PATH = "/Users/avada/CSL/.env"


VERIFY_FLAG_PCT = 30  # verify coverage dưới mức này -> ⚠️ nhắc team verify thêm


def _top_line(items):
    if not items:
        return "_(chưa có lượt nào tuần này)_"
    return " · ".join(f"{i['name']} ({i['count']})" for i in items)


def _delta(cur, prev):
    """▲▼ so tuần trước cho số %; trả chuỗi ' (▲2.1)' / '' nếu thiếu data."""
    if not isinstance(cur, (int, float)) or not isinstance(prev, (int, float)):
        return ""
    d = round(cur - prev, 1)
    if d == 0:
        return " (▬)"
    return f" ({'▲' if d > 0 else '▼'}{abs(d)})"


def botqa_block(qa):
    """qa = output của fetch_bot_qa.py (có handle + qa, optional prevWeek).
    Trả 1 section block: Bot performance (Handle) + Bot QA (phần con)."""
    bot = {"chatty": "Ivy", "joy": "Joyce", "wishlist": "Wendy"}.get(qa.get("app"), "Bot")
    h, q = qa.get("handle", {}), qa.get("qa", {})
    prev = qa.get("prevWeek", {})
    ph, pq = prev.get("handle", {}), prev.get("qa", {})

    cov = q.get("verifyCoveragePct")
    flag = " ⚠️ _verify thấp — team verify thêm nhé_" if isinstance(cov, (int, float)) and cov < VERIFY_FLAG_PCT else ""
    reply = q.get("botReplies")

    lines = [
        f"🤖 *Bot performance tuần này ({bot})*",
        f"*Handle*",
        f"• AI resolved: *{h.get('aiResolvedPct')}%*{_delta(h.get('aiResolvedPct'), ph.get('aiResolvedPct'))} — bot xử xong, số khớp dashboard cs2",
        f"• CS không phải đụng tay: *{h.get('takeOnlyPct')}%*{_delta(h.get('takeOnlyPct'), ph.get('takeOnlyPct'))} ({h.get('takeOnlySessions')}/{h.get('aiReplied')} session bot chạy trọn, không escalate)",
        *([f"   _Chênh {h.get('unclearGapPct')}đ = merchant im lặng, chưa rõ có được giúp không_"]
          if h.get("unclearGapPct") else []),
        f"   _AI coverage {h.get('aiReplyCoveragePct')}% · Human takeover {h.get('humanTakeoverPct')}% · Escalation {h.get('escalationRatePct')}%_",
        f"• Volume: {h.get('inbound')} tin vào · {h.get('botReplies')} reply bot",
        f"*QA*",
        f"• Verify coverage: *{cov}%*{_delta(cov, pq.get('verifyCoveragePct'))} ({q.get('verifiedInWeek')}/{reply} reply){flag}",
        f"• Correction rate: *{q.get('correctionRatePct')}%*{_delta(q.get('correctionRatePct'), pq.get('correctionRatePct'))} ({q.get('correctionsInWeek')}/{reply} reply)",
        f"🏆 Top verify: {_top_line(q.get('topVerifiers'))}",
        f"🔧 Top correction: {_top_line(q.get('topCorrectors'))}",
    ]
    return {"type": "section", "text": {"type": "mrkdwn", "text": "\n".join(lines)}}


def onboarding_block(ob):
    """ob = output of fetch_onboarding.py (Joy only). Trả 1 section block, hoặc
    None nếu tuần không có onboarding ticket nào (mới lẫn backlog)."""
    if not ob.get("new_count") and not ob.get("open_count"):
        return None
    prev_new = (ob.get("prevWeek") or {}).get("new_count")
    delta = _delta(ob.get("new_count"), prev_new)

    lines = [
        "🚀 *Onboarding tickets tuần này*",
        f"• Mới: *{ob.get('new_count')}*{delta} · Đang mở: *{ob.get('open_count')}* · "
        f"Go-live tuần này: *{ob.get('golive_count')}*",
        f"• Checklist trung bình (open): *{ob.get('avg_checklist_pct')}%* hoàn thành",
    ]
    delayed = ob.get("delayed") or []
    if delayed:
        items = " · ".join(f"{d['store']} ({d['done']}/{d['total']})" for d in delayed[:5])
        more = f" (+{len(delayed) - 5} khác)" if len(delayed) > 5 else ""
        lines.append(f"⚠️ Trễ (>14 ngày chưa live): {items}{more}")
    return {"type": "section", "text": {"type": "mrkdwn", "text": "\n".join(lines)}}


def build_blocks(title, tldr, notion_url, qa=None, onboarding=None):
    blocks = [
        {"type": "header",
         "text": {"type": "plain_text", "text": f"📊 {title}", "emoji": True}},
        {"type": "section",
         "text": {"type": "mrkdwn", "text": f"*TL;DR*\n{tldr}"}},
    ]
    if qa:
        blocks.append({"type": "divider"})
        blocks.append(botqa_block(qa))
    if onboarding:
        ob_block = onboarding_block(onboarding)
        if ob_block:
            blocks.append({"type": "divider"})
            blocks.append(ob_block)
    blocks += [
        {"type": "actions",
         "elements": [
             {"type": "button",
              "text": {"type": "plain_text", "text": "📄 Xem full trên Notion", "emoji": True},
              "url": notion_url,
              "style": "primary"}
         ]},
        {"type": "context",
         "elements": [{"type": "mrkdwn",
                       "text": "_Bản tin tự động từ `/cs-weekly` · góp ý gửi Liz_"}]},
    ]
    return blocks


def liz_identity(tok):
    """Live-fetch Liz's display name + avatar so the post reads as from her."""
    r = requests.get("https://slack.com/api/users.info",
                     headers={"Authorization": f"Bearer {tok}"},
                     params={"user": LIZ_USER_ID}).json()
    if not r.get("ok"):
        return None, None
    p = r["user"]["profile"]
    name = p.get("display_name") or p.get("real_name")
    avatar = p.get("image_192") or p.get("image_512")
    return name, avatar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", required=True, help="Slack channel ID")
    ap.add_argument("--title", required=True, help="App + week, e.g. 'Chatty CS Weekly — W23 (01–07/06/2026)'")
    ap.add_argument("--notion-url", required=True, help="Full Notion page URL")
    ap.add_argument("--tldr", help="TL;DR text inline")
    ap.add_argument("--tldr-file", help="Path to a file containing the TL;DR text")
    ap.add_argument("--botqa-file", help="Path to JSON output of fetch_bot_qa.py (adds a Bot QA block)")
    ap.add_argument("--onboarding-file", help="Path to JSON output of fetch_onboarding.py (adds an Onboarding block, Joy only)")
    ap.add_argument("--no-as-user", dest="as_user", action="store_false",
                    help="post as the plain avada_bot instead of as Liz")
    ap.set_defaults(as_user=True)
    a = ap.parse_args()

    if a.tldr_file:
        with open(a.tldr_file, encoding="utf-8") as f:
            tldr = f.read().strip()
    elif a.tldr:
        tldr = a.tldr.strip()
    else:
        print("ERROR: provide --tldr or --tldr-file", file=sys.stderr)
        sys.exit(2)

    qa = None
    if a.botqa_file:
        with open(a.botqa_file, encoding="utf-8") as f:
            qa = json.load(f)

    onboarding = None
    if a.onboarding_file:
        with open(a.onboarding_file, encoding="utf-8") as f:
            onboarding = json.load(f)

    load_dotenv(ENV_PATH)
    tok = os.environ["SLACK_BOT_TOKEN_AVADA"]

    blocks = build_blocks(a.title, tldr, a.notion_url, qa, onboarding)
    # `text` is the notification fallback (shown in the channel list / push).
    payload = {
        "channel": a.channel,
        "text": f"{a.title} — {tldr[:120]}",
        "blocks": blocks,
        "unfurl_links": False,
    }
    # Post as Liz (name + avatar) by default — reads as coming from her.
    if a.as_user:
        name, avatar = liz_identity(tok)
        if name:
            payload["username"] = name
        if avatar:
            payload["icon_url"] = avatar
    r = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
        data=json.dumps(payload),
    ).json()
    if not r.get("ok"):
        print(f"ERROR posting to Slack: {r.get('error')}", file=sys.stderr)
        sys.exit(1)
    print(f"Posted to {a.channel} (ts={r.get('ts')})")


if __name__ == "__main__":
    main()
