#!/usr/bin/env python3
"""
Exception layer for /cs-daily-brief: run all 4 fetchers for the window, apply
Liz's rules from cron/thresholds.json, and say whether the day is quiet or
needs reporting.

The split is deliberate: the fetch_*.py scripts stay pure data (they know
nothing about thresholds), this file holds every rule, and the thresholds
themselves live in JSON so Liz can retune without touching code.

Runs all 4 fetchers itself so the cron prompt is one command instead of five,
and so the sanity checks below can't be skipped.

SANITY over silence — the failure mode this whole design has to survive is a
broken pipeline looking exactly like a calm day (BigQuery down, token expired,
API shape changed => every number is 0 => nothing gets flagged => Liz assumes
all is well). So: any fetcher exiting non-zero is a hard error, and an
all-zeros result is reported as SUSPECTED BREAKAGE, never as quiet.

Usage:
  python3 evaluate.py --json                    # yesterday 08:30 -> today 08:30 (VN)
  python3 evaluate.py --date 2026-08-10 --json
"""
import os, sys, json, argparse, subprocess, datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
THRESHOLDS_PATH = os.path.join(SKILL_DIR, "cron", "thresholds.json")
VN = dt.timezone(dt.timedelta(hours=7))
AI_MEMBER_ID = "ai-agent-2"  # same id as fetch_ai_tickets.py

FETCHERS = {
    "conversations": "fetch_conversations.py",
    "checkin": "fetch_checkin.py",
    "aiTickets": "fetch_ai_tickets.py",
    "lizTickets": "fetch_liz_tickets.py",
}


def load_thresholds(path=THRESHOLDS_PATH):
    with open(path) as f:
        return json.load(f)


def run_fetch(script, date):
    """Run one fetcher, return its parsed JSON. Raises on any failure —
    a partial brief is worse than a loud one."""
    p = subprocess.run(
        [sys.executable, os.path.join(HERE, script), "--date", date, "--json"],
        capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        raise RuntimeError(f"{script} exited {p.returncode}: "
                           f"{(p.stderr or '').strip()[-600:]}")
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"{script} did not emit JSON ({e}): "
                           f"{(p.stdout or '')[:300]}")


def sanity_problems(data, cfg):
    """Signals that the numbers are broken rather than genuinely calm."""
    out = []
    s = cfg["sanity"]

    conv = data["conversations"]
    if conv["total"] != sum(conv["counts"].values()):
        out.append("conversations: total khác tổng các app — số liệu không nhất quán")
    if conv["total"] < s["minTotalConversations"]:
        out.append("conversations: tổng = 0 — nghi BigQuery/pipeline lỗi, "
                   "KHÔNG phải ngày yên ắng")

    handled = sum(a.get("handledCount", 0) for a in data["aiTickets"]["apps"].values())
    if handled < s["minBotHandled"]:
        out.append("aiTickets: cả 3 bot handled = 0 — nghi query chat bot lỗi")

    return out


def evaluate(data, cfg):
    """Apply Liz's rules. Returns (flags, quiet)."""
    flags = {}

    # ② Checkin — muộn >= N phút, miss checkin, miss checkout.
    c = data["checkin"]
    late = [x for x in c["late"] if x["minutes"] >= cfg["checkin"]["lateMinutes"]]
    miss_in = c["missCheckin"] if cfg["checkin"]["reportMissCheckin"] else []
    miss_out = c["missCheckout"] if cfg["checkin"]["reportMissCheckout"] else []
    flags["checkin"] = {"late": late, "missCheckin": miss_in, "missCheckout": miss_out,
                        "any": bool(late or miss_in or miss_out)}

    # ③ AI ticket chưa có tiến độ — tsStatus in {pending, doing} AND not done.
    # dueDateDone is True / absent / (rarely) False, so the test is
    # `is not True` — `== False` would almost never fire. See fetch_ai_tickets.py.
    ai = cfg["aiTickets"]
    want = set(ai["flagTsStatus"])
    stale = []
    dfy_unassigned = []
    for app_key, app in data["aiTickets"]["apps"].items():
        for t in app.get("tickets", []):
            matched = False
            if t.get("tsStatus") in want:
                if not (ai["requireDueDateNotDone"] and t.get("dueDateDone") is True):
                    stale.append({**t, "bot": app.get("bot")})
                    matched = True
            # ③b — tsStatus = done_for_you (bot marked DFY done) but the ticket
            # still has nobody but the AI creator on it — no human ever
            # picked it up. Independent condition, checked even if ③a above
            # didn't match (a ticket can't be both, since done_for_you isn't
            # in flagTsStatus, but keep this a separate `if` for clarity).
            if (ai.get("flagDfyUnassigned") and t.get("tsStatus") == "done_for_you"
                    and (t.get("memberIds") or []) == [AI_MEMBER_ID]):
                dfy_unassigned.append({**t, "bot": app.get("bot")})
    stale.sort(key=lambda t: t.get("createdAt") or "")
    dfy_unassigned.sort(key=lambda t: t.get("createdAt") or "")
    flags["aiStale"] = stale
    flags["aiDfyUnassigned"] = dfy_unassigned

    # ④ Ticket cho Liz — báo hết.
    liz = data["lizTickets"]["tickets"] if cfg["lizTickets"]["reportAll"] else []
    flags["lizTickets"] = liz

    quiet = not (flags["checkin"]["any"] or stale or dfy_unassigned or liz)
    return flags, quiet


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYY-MM-DD (VN) — window starts 08:30 this "
                                   "day; default yesterday")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--thresholds", default=THRESHOLDS_PATH)
    a = ap.parse_args()

    if a.date:
        day = dt.datetime.strptime(a.date, "%Y-%m-%d").replace(tzinfo=VN)
    else:
        day = (dt.datetime.now(VN) - dt.timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0)
    start = day.replace(hour=8, minute=30, second=0, microsecond=0)
    end = start + dt.timedelta(days=1)
    date_str = start.strftime("%Y-%m-%d")

    cfg = load_thresholds(a.thresholds)
    data = {name: run_fetch(script, date_str) for name, script in FETCHERS.items()}

    problems = sanity_problems(data, cfg)
    flags, quiet = evaluate(data, cfg)
    if problems:
        quiet = False  # never go silent on a suspected breakage

    out = {
        "date": date_str,
        "windowStartVn": start.strftime("%d/%m/%Y %H:%M"),
        "windowEndVn": end.strftime("%d/%m/%Y %H:%M"),
        "quiet": quiet,
        "sanity": {"ok": not problems, "problems": problems},
        "flags": flags,
        "data": data,
    }

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        conv = data["conversations"]
        print(f"{date_str} — {'QUIET' if quiet else 'CÓ VIỆC'}"
              f"{' [SANITY FAIL]' if problems else ''}")
        print(f"  ① {conv['total']} conv "
              f"(joy={conv['counts']['joy']} chatty={conv['counts']['chatty']} "
              f"wishlist={conv['counts']['wishlist']})")
        ck = flags["checkin"]
        print(f"  ② late>={cfg['checkin']['lateMinutes']}p: {len(ck['late'])}, "
              f"miss in: {len(ck['missCheckin'])}, miss out: {len(ck['missCheckout'])}")
        print(f"  ③ AI ticket chưa tiến độ: {len(flags['aiStale'])}")
        print(f"  ③b DFY chưa ai nhận: {len(flags['aiDfyUnassigned'])}")
        print(f"  ④ ticket cho Liz: {len(flags['lizTickets'])}")
        for p in problems:
            print(f"  ⚠️  {p}")


if __name__ == "__main__":
    main()
