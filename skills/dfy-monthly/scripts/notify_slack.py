#!/usr/bin/env python3
"""
Post a monthly DFY digest to the Chatty CS Slack channel via the Avada bot,
posing as Liz (username + icon overridden to Liz's Slack identity).

Reads fetch_dfy.py JSON for the numbers, builds a Block Kit message with a
"📗 Xem full trên Notion" primary button, and posts it. Does NOT tag anyone.

Usage:
  python3 notify_slack.py --in /tmp/dfy.json --notion-url https://... \
      [--channel C0B62UJRGSJ] [--dm]   # --dm sends to Liz's DM instead (dry-run)

Auth: SLACK_BOT_TOKEN_AVADA from CSL/.env. The Avada bot must be a member of the
target channel (invite once if posting returns not_in_channel).
"""
import os, json, argparse
import urllib.request, urllib.parse

LIZ_USER_ID = "U02GT4PC6RH"          # Hoàng Thị Ly (Liz)
CHATTY_CS_CHANNEL = "C0B62UJRGSJ"     # default channel for Chatty CS
MONTH_VI = {"01": "1", "02": "2", "03": "3", "04": "4", "05": "5", "06": "6",
            "07": "7", "08": "8", "09": "9", "10": "10", "11": "11", "12": "12"}


def load_env():
    env = {}
    root = os.path.join(os.path.dirname(__file__), "..", "..", "..")
    for line in open(os.path.join(root, ".env")):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k] = v.strip().strip('"').strip("'")
    return env


def slack_get(method, token, params=None):
    url = f"https://slack.com/api/{method}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def slack_post(method, token, payload):
    req = urllib.request.Request(
        f"https://slack.com/api/{method}",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def liz_identity(token):
    info = slack_get("users.info", token, {"user": LIZ_USER_ID})
    prof = info["user"]["profile"]
    name = prof.get("display_name") or info["user"].get("real_name")
    img = prof.get("image_512") or prof.get("image_192")
    return name, img


def video_highlight(v):
    """Mirrors build_report.py's video_insight_line — wording adapts to the
    actual delta instead of always claiming video is the strongest lever."""
    delta = v["delta"]
    if delta >= 15:
        return (f"• *Video là đòn bẩy adopt mạnh nhất:* ticket có video adopt *{v['yes_adopt_pct']}%* "
                f"vs không video *{v['no_adopt_pct']}%* → nên đưa quay video thành bước bắt buộc.")
    if delta <= -15:
        return (f"• *Video không cho lợi thế rõ tháng này — ngược lại:* video *{v['yes_adopt_pct']}%* "
                f"vs không video *{v['no_adopt_pct']}%*, cần xem lại.")
    return (f"• *Video chưa cho tín hiệu rõ tháng này:* video *{v['yes_adopt_pct']}%* vs "
            f"không video *{v['no_adopt_pct']}%* — chênh lệch nhỏ, theo dõi thêm.")


def build_blocks(d, notion_url):
    mm = d["month"].split("-")[1]
    yy = d["month"].split("-")[0]
    inb, pro, ins = d["inbound"], d["proactive"], d["insights"]
    v = ins["video"]
    rv = ins["review"]
    dpi = ins["dfy_per_install"]

    title = f"📊 DFY Chatty — Tháng {MONTH_VI.get(mm, mm)}/{yy}"

    # 💡 highlights: video is always shown; review-yes if any. (Chatbox intentionally
    # kept OUT of the Slack digest per Liz — it lives in the Notion Insight section.)
    hi = [video_highlight(v)]
    if ins["review_yes"]:
        hi.append(f"• *DFY sinh {ins['review_yes']} review 5★* — giá trị phụ ngoài giữ widget.")

    cs_line = " · ".join(f"{_short(c['display'])} {c['count']}" for c in d["per_cs"])

    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": title, "emoji": True}},
        {"type": "section", "text": {"type": "mrkdwn",
         "text": f"Gửi cả nhà số liệu DFY Chatty tháng {MONTH_VI.get(mm, mm)} 🎉\n\n"
                 f"*Tổng quan:* {d['total']} ticket · adopted *{d['adopted']} ({d['adopt_pct']}%)*\n"
                 f"⭐ Review xin được: *{rv['count']}/{rv['total']} ({rv['pct']}%)* · "
                 f"📈 DFY/install tháng: *{dpi['dfy_tickets']}/{dpi['installs']} ({dpi['pct']}%)*"}},
        {"type": "section", "text": {"type": "mrkdwn",
         "text": "*Tách theo kênh*\n"
                 f"🔵 *Inbound* (DFY theo yêu cầu KH): *{inb['count']} ticket · adopt "
                 f"{inb['adopt_pct']}%* ({inb['adopted']}/{inb['count']}) → chất lượng DFY tốt, "
                 "KH giữ lại widget cao.\n"
                 f"🟢 *Proactive* (mình chủ động reach out): *{pro['count']} ticket · adopt "
                 f"{pro['adopt_pct']}%* ({pro['adopted']}/{pro['count']}) → kênh mới, cần bàn cách "
                 "tiếp cận."}},
        {"type": "section", "text": {"type": "mrkdwn",
         "text": "*💡 Điểm đáng chú ý*\n" + "\n".join(hi)}},
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*Theo CS:*  {cs_line}"}},
        {"type": "context", "elements": [{"type": "mrkdwn",
         "text": "📌 Số liệu tháng — từ tháng sau sẽ có số so sánh tháng-qua-tháng."}]},
        {"type": "actions", "elements": [{"type": "button",
         "text": {"type": "plain_text", "text": "📗 Xem full trên Notion", "emoji": True},
         "url": notion_url, "style": "primary"}]},
        {"type": "context", "elements": [{"type": "mrkdwn",
         "text": "Báo cáo DFY tháng · góp ý gửi Liz"}]},
    ]
    return title, blocks


def _short(display):
    """`AnhBD (Andy)` -> `Andy`; fallback to the nickname."""
    if "(" in display and ")" in display:
        return display[display.index("(") + 1:display.index(")")]
    return display


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="fetch_dfy.py JSON")
    ap.add_argument("--notion-url", required=True)
    ap.add_argument("--channel", default=CHATTY_CS_CHANNEL)
    ap.add_argument("--dm", action="store_true",
                    help="Send to Liz's DM instead of the channel (dry-run preview)")
    a = ap.parse_args()

    env = load_env()
    token = env["SLACK_BOT_TOKEN_AVADA"]
    d = json.load(open(a.inp))
    name, img = liz_identity(token)
    title, blocks = build_blocks(d, a.notion_url)

    if a.dm:
        channel = slack_post("conversations.open", token, {"users": LIZ_USER_ID})["channel"]["id"]
    else:
        channel = a.channel

    r = slack_post("chat.postMessage", token, {
        "channel": channel,
        "text": title,               # notification fallback
        "blocks": blocks,
        "username": name,
        "icon_url": img,
        "unfurl_links": False, "unfurl_media": False,
    })
    if r.get("ok"):
        print(f"Posted to {channel} (ts={r.get('ts')})")
    else:
        raise SystemExit(f"Slack error: {r.get('error')}")


if __name__ == "__main__":
    main()
