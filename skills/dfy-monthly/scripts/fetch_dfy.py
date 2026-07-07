#!/usr/bin/env python3
"""
Fetch + analyze monthly DFY tickets for an app (Chatty) from the Avada Ticket API.

Pulls DFY tickets for a month, splits them into Inbound (no `proactive` tag) vs
Proactive (has `proactive` tag), computes adopt rate per group + insights, maps
each CS to their KPI nickname, and emits a single JSON blob to stdout (or --out).

Usage:
  python3 fetch_dfy.py --app chatty --month 2026-06 [--out /tmp/dfy.json]

Auth: AVD_TICKET_API_KEY from CSL/.env.

Output shape (JSON):
  {
    "app": "chatty", "month": "2026-06",
    "period": {"start": "2026-06-01", "end": "2026-06-30"},
    "total": 27, "adopted": 14, "adopt_pct": 52,
    "inbound":   {"count": 22, "adopted": 14, "adopt_pct": 64, "tickets": [...]},
    "proactive": {"count": 5,  "adopted": 0,  "adopt_pct": 0,  "tickets": [...]},
    "per_cs": [{"nick": "AnhBD", "display": "AnhBD (Andy)", "count": 16,
                "adopted": 7, "adopt_pct": 44, "video": 9, "video_pct": 56}, ...],
    "insights": {
        "video":   {"yes_adopt_pct": 69, "no_adopt_pct": 27, "yes_n": 16, "no_n": 11, "delta": 42},
        "ai":      {"full_adopt_pct": 83, "zero_adopt_pct": 0},
        "chatbox": {"task_pct": 16, "zero_ticket": 19, "total_ticket": 27},
        "timing":  {"by_week": {"1":1,"4":20,"5":6}, "peak_week": 4, "peak_n": 20},
        "review_yes": 4
    }
  }

A ticket row: {date, ticket_id, url, store, cs_nick, cs_display, tasks_done,
               tasks_total, tags}
"""
import os, sys, json, argparse, calendar
import urllib.request, urllib.parse
from collections import defaultdict, Counter

BASE = "https://avada-ts-a9cb0.web.app"

# App name as the Ticket API expects it.
APP_NAME = {"chatty": "Chatty", "joy": "JOY Loyalty"}

# Tags that mark a ticket as DFY (scoring + tracking). A ticket is DFY if it has
# ANY of these. Kept in sync with /dfy-tracker + /dfy-weekly.
DFY_SET = {
    "DFY-1", "DFY-adopted", "DFY-coupon-images", "DFY-following-up", "DFY-new",
    "DFY-no-adopt", "DFY-tier-banner", "DFY-tier-icon", "DFY-video",
    "ai agent", "chatbox", "proactive",
}

# trello username / displayName (lowercased) -> KPI nickname.
# Source of truth: _identity/team-g2.md. The Ticket API returns username=None and
# puts the handle in displayName with inconsistent casing (Andy_Avada, Alicia_CS,
# rosiele, Audrey_avada...), so match case-insensitively and include those aliases.
NICK = {
    "liz_avada": "LyHT", "hana_avada": "HangHM", "audrey_avada": "VanCT",
    "alyssa_avada": "LyPK", "sonny_avada": "HuyTC", "alicia_avada": "AnhLN",
    "rosie_avada": "ThaoLTT", "jade_avada": "PhuongNT", "mirra_avada": "MinhBT",
    "andy_avada": "AnhBD", "hazel_avada": "HienPT", "megan_avada": "TrangNTH",
    "cody_avada": "ChauHM", "phoebe_avada": "PhuongTTM", "linda1_avada": "LinhTLK",
    # displayName aliases seen in the Ticket API
    "alicia_cs": "AnhLN", "rosiele": "ThaoLTT",
}
# Nickname -> friendly display used in tables (nickname + English name).
DISPLAY = {
    "AnhBD": "AnhBD (Andy)", "PhuongNT": "PhuongNT (Jade)",
    "PhuongTTM": "PhuongTTM (Phoebe)", "HienPT": "HienPT (Hazel)",
}


def load_env():
    env = {}
    root = os.path.join(os.path.dirname(__file__), "..", "..", "..")
    path = os.path.join(root, ".env")
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k] = v.strip().strip('"').strip("'")
    return env


def api_get(path, key, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-API-Key": key})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def tag_map(key):
    data = api_get("/api/external/tags", key)
    arr = data.get("data", data)
    if isinstance(arr, dict):
        arr = arr.get("tags", arr)
    out = {}
    for tg in arr:
        tid = tg.get("id") or tg.get("_id") or tg.get("tagId")
        out[tid] = tg.get("name") or tg.get("title")
    return out


def names(t, id2name):
    return [x for x in (id2name.get(i) for i in (t.get("tagIds") or [])) if x]


def creator(t):
    m = [x for x in t.get("members", []) if x.get("isCreate")] or t.get("members", [])[:1]
    if not m:
        return "?"
    # API gives username=None; the handle lives in displayName. Match either,
    # case-insensitively, against the NICK table.
    raw = m[0].get("username") or m[0].get("displayName") or ""
    return NICK.get(raw.lower(), raw or "?")


def blocks(t):
    """Return (ai_tasks, chatbox_tasks, video_tasks) split by task title prefix."""
    ai = [k for k in t.get("tasks", []) if str(k.get("title", "")).startswith("AI Agent:")]
    cb = [k for k in t.get("tasks", []) if str(k.get("title", "")).startswith("Chatbox:")]
    vid = [k for k in t.get("tasks", []) if str(k.get("title", "")).lower().startswith("bonus")]
    return ai, cb, vid


def has_video(t):
    return any(k.get("completed") for k in blocks(t)[2])


def row(t, id2name):
    url = t.get("shortUrl") or ""
    if url.startswith("/"):
        url = BASE + url
    tks = t.get("tasks", [])
    nick = creator(t)
    return {
        "date": (t.get("createdAt") or "")[:10],
        "ticket_id": t.get("ticketId"),
        "url": url,
        "store": (t.get("store") or [{}])[0].get("domain", ""),
        "cs_nick": nick,
        "cs_display": DISPLAY.get(nick, nick),
        "tasks_done": sum(1 for k in tks if k.get("completed")),
        "tasks_total": len(tks),
        "tags": names(t, id2name),
    }


def adopt(group, id2name):
    a = sum(1 for t in group if "DFY-adopted" in names(t, id2name))
    pct = round(100 * a / len(group)) if group else 0
    return a, pct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default="chatty", choices=["chatty", "joy"])
    ap.add_argument("--month", required=True, help="YYYY-MM, e.g. 2026-06")
    ap.add_argument("--out", help="Write JSON here instead of stdout")
    a = ap.parse_args()

    env = load_env()
    key = env["AVD_TICKET_API_KEY"]

    y, m = map(int, a.month.split("-"))
    start = f"{y:04d}-{m:02d}-01"
    end = f"{y:04d}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"

    id2name = tag_map(key)
    resp = api_get("/api/external/tickets/by-date", key,
                   {"startDate": start, "endDate": end, "appName": APP_NAME[a.app]})
    tickets = resp.get("data", {}).get("tickets", [])

    # DFY = has any DFY-set tag; open only; drop sale_request + Liz test tickets.
    dfy = [t for t in tickets if set(names(t, id2name)) & DFY_SET]
    op = [t for t in dfy
          if t.get("ticketStatus") != "closed"
          and t.get("tsStatus") != "sale_request"
          and not (creator(t) == "LyHT" and not names(t, id2name))]

    proactive = [t for t in op if "proactive" in names(t, id2name)]
    inbound = [t for t in op if "proactive" not in names(t, id2name)]

    atot, ptot = adopt(op, id2name)
    ainb, pinb = adopt(inbound, id2name)
    apr, ppr = adopt(proactive, id2name)

    # ---- per-CS ----
    g = defaultdict(list)
    for t in op:
        g[creator(t)].append(t)
    per_cs = []
    for nick, ts in sorted(g.items(), key=lambda x: -len(x[1])):
        a_, p_ = adopt(ts, id2name)
        v = sum(1 for t in ts if has_video(t))
        per_cs.append({
            "nick": nick, "display": DISPLAY.get(nick, nick), "count": len(ts),
            "adopted": a_, "adopt_pct": p_,
            "video": v, "video_pct": round(100 * v / len(ts)) if ts else 0,
        })

    # ---- insights ----
    vid_yes = [t for t in op if has_video(t)]
    vid_no = [t for t in op if not has_video(t)]
    _, vy_pct = adopt(vid_yes, id2name)
    _, vn_pct = adopt(vid_no, id2name)

    ai_full = [t for t in op if blocks(t)[0] and all(k.get("completed") for k in blocks(t)[0])]
    ai_zero = [t for t in op if blocks(t)[0] and not any(k.get("completed") for k in blocks(t)[0])]
    _, aif_pct = adopt(ai_full, id2name)
    _, aiz_pct = adopt(ai_zero, id2name)

    cb_done = cb_tot = cb_zero = 0
    for t in op:
        cb = blocks(t)[1]
        d = sum(1 for k in cb if k.get("completed"))
        cb_done += d
        cb_tot += len(cb)
        if d == 0:
            cb_zero += 1

    by_week = Counter()
    for t in op:
        d = (t.get("createdAt") or "")[:10]
        try:
            day = int(d[8:10])
            by_week[str((day - 1) // 7 + 1)] += 1
        except ValueError:
            pass
    peak_week, peak_n = (max(by_week.items(), key=lambda x: x[1]) if by_week else ("0", 0))

    review_yes = sum(1 for t in op if "review-yes" in names(t, id2name))

    result = {
        "app": a.app, "month": a.month,
        "period": {"start": start, "end": end},
        "total": len(op), "adopted": atot, "adopt_pct": ptot,
        "inbound": {"count": len(inbound), "adopted": ainb, "adopt_pct": pinb,
                    "tickets": [row(t, id2name) for t in sorted(inbound, key=lambda z: z.get("createdAt", ""))]},
        "proactive": {"count": len(proactive), "adopted": apr, "adopt_pct": ppr,
                      "tickets": [row(t, id2name) for t in sorted(proactive, key=lambda z: z.get("createdAt", ""))]},
        "per_cs": per_cs,
        "insights": {
            "video": {"yes_adopt_pct": vy_pct, "no_adopt_pct": vn_pct,
                      "yes_n": len(vid_yes), "no_n": len(vid_no), "delta": vy_pct - vn_pct},
            "ai": {"full_adopt_pct": aif_pct, "zero_adopt_pct": aiz_pct,
                   "full_n": len(ai_full), "zero_n": len(ai_zero)},
            "chatbox": {"task_pct": round(100 * cb_done / cb_tot) if cb_tot else 0,
                        "zero_ticket": cb_zero, "total_ticket": len(op)},
            "timing": {"by_week": dict(sorted(by_week.items())),
                       "peak_week": int(peak_week), "peak_n": peak_n},
            "review_yes": review_yes,
        },
    }

    blob = json.dumps(result, ensure_ascii=False, indent=2)
    if a.out:
        with open(a.out, "w") as f:
            f.write(blob)
        print(f"Wrote {a.out} ({result['total']} DFY tickets, adopt {result['adopt_pct']}%)", file=sys.stderr)
    else:
        print(blob)


if __name__ == "__main__":
    main()
