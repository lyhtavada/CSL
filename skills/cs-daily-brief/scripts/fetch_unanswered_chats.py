#!/usr/bin/env python3
"""
Chats where the merchant is the last one to speak — nobody (bot or human CS)
has replied since. Added 2026-09-03 per Liz's request, triggered by finding
session_852e24d1-05c6-4aef-94fb-c4ef4692d4bf: merchant wrote "I want support"
on 28/8, and the session sat untouched until Liz noticed it by hand on 3/9.

Unlike the other 3 fetchers, this is NOT scoped to the rolling 24h window —
"unanswered" is a standing state, not something that happened in the window.
A chat stays flagged every single day until someone actually replies, which
is the point (nag until fixed, same "sanity over silence" spirit as the rest
of this skill). `--date` here only sets the "as of" cutoff (that date's 08:30
VN, matching the other fetchers' window end) so a manual re-run for a past
morning reproduces what that morning's report would have shown.

Detection, per session_id:
  - Look only at `type IN ('text','file')` — EXCLUDES `type='note'`, which is
    an internal Crisp note (not visible to the merchant). This matters: the
    example session above has a note from Liz today ("@sonny fu chat này
    giúp chị nhé") that is NOT a reply to the merchant — if notes counted as
    replies this fetcher would have silently cleared the flag the moment
    someone left an internal comment. Confirmed live 2026-09-03.
  - Also require `origin = 'chat'` — EXCLUDES `origin='email'`. session_id is
    permanent per visitor in Crisp (same fact chat_count.py relies on), so a
    visitor's inbox keeps collecting messages for weeks after their real
    conversation was resolved. Confirmed live 2026-09-03: several sessions
    with a long, already-resolved chat history had a stray `origin='email'`
    message weeks later — a marketing newsletter or an automated "your
    ticket has been closed" notification auto-piped into the same thread —
    which then permanently looked like "merchant spoke last, unanswered"
    even though nobody needed to reply to it. `origin='chat'` is the real
    live-chat channel and is what actually needs a reply.
  - Take the single latest such message per session (ROW_NUMBER, not just
    MAX(timestamp), since we need the row's fromType too).
  - Flag if that latest message has fromType = 'user' (merchant) — meaning
    the merchant spoke last, whether or not a bot or human ever replied
    earlier in the thread. fromType='operator' covers BOTH the AI bot
    (agentEmail IS NULL) and a human CS (agentEmail set) — see
    fetch_ai_tickets.py — so "last message not from CS" and "last message
    not fromType=operator" are the same condition; no need to special-case
    the bot.
  - `minHoursWaiting` (thresholds.json) suppresses very fresh messages so a
    merchant who wrote 5 minutes before the 08:45 cron isn't flagged before
    CS has had any chance to answer.
  - `lookbackDays` bounds the scan (old, permanently-abandoned sessions
    aren't worth resurfacing forever) — configurable, not a correctness
    requirement.

Session link: https://app.crisp.chat/website/{website_id}/inbox/{session_id}
(website_id is shared across Joy + Chatty + Wishlist — confirmed live
2026-09-03: 72a663b0-4cda-4e3b-8878-426bdd79364c for all three).

Usage:
  python3 fetch_unanswered_chats.py --json                # as of today 08:30 (VN)
  python3 fetch_unanswered_chats.py --date 2026-08-10 --json
"""
import os, sys, json, argparse, datetime as dt

sys.path.insert(0, os.path.dirname(__file__))
from _common import load_env, bq_client, VN  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_shared"))
from chat_count import APP_SEGMENTS, INTERNAL_EMAIL_PATTERNS  # noqa: E402

DEFAULT_LOOKBACK_DAYS = 30
DEFAULT_MIN_HOURS_WAITING = 3


def fetch_unanswered(client, segments, cutoff_str, lookback_start_str):
    seg_clause = " OR ".join(f"segments LIKE @s{i}" for i in range(len(segments)))
    internal_clause = "AND NOT (" + " OR ".join(
        f"LOWER(customerEmail) LIKE '{p}'" for p in INTERNAL_EMAIL_PATTERNS
    ) + ")"

    sql = f"""
    WITH msgs AS (
      SELECT session_id, website_id, timestamp, fromType, content,
             customerEmail, customerNickname
      FROM `avada-crm.avada_cs.crisp_chats`
      WHERE ({seg_clause})
        AND type IN ('text', 'file')
        AND origin = 'chat'
        AND timestamp >= TIMESTAMP(@lookback_start)
        AND timestamp <  TIMESTAMP(@cutoff)
        {internal_clause}
    ),
    ranked AS (
      SELECT *, ROW_NUMBER() OVER (
        PARTITION BY session_id ORDER BY timestamp DESC
      ) AS rn
      FROM msgs
    )
    SELECT session_id, website_id, timestamp AS last_msg_at, content,
           customerEmail, customerNickname
    FROM ranked
    WHERE rn = 1 AND fromType = 'user'
    ORDER BY last_msg_at ASC
    """
    from google.cloud import bigquery
    params = [
        bigquery.ScalarQueryParameter(f"s{i}", "STRING", f"%{s}%")
        for i, s in enumerate(segments)
    ] + [
        bigquery.ScalarQueryParameter("lookback_start", "STRING", lookback_start_str),
        bigquery.ScalarQueryParameter("cutoff", "STRING", cutoff_str),
    ]
    job = bigquery.QueryJobConfig(query_parameters=params)
    return list(client.query(sql, job_config=job).result())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYY-MM-DD (VN) — cutoff is this day's 08:30, "
                                   "matching the other fetchers' window end — default yesterday")
    ap.add_argument("--lookback-days", type=int, default=DEFAULT_LOOKBACK_DAYS)
    ap.add_argument("--min-hours-waiting", type=float, default=DEFAULT_MIN_HOURS_WAITING)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.date:
        day = dt.datetime.strptime(a.date, "%Y-%m-%d").replace(tzinfo=VN)
    else:
        day = (dt.datetime.now(VN) - dt.timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0)
    cutoff = day.replace(hour=8, minute=30, second=0, microsecond=0) + dt.timedelta(days=1)
    lookback_start = cutoff - dt.timedelta(days=a.lookback_days)
    min_wait = dt.timedelta(hours=a.min_hours_waiting)

    env = load_env()
    client = bq_client(env)
    cutoff_str = cutoff.strftime("%Y-%m-%d %H:%M:%S+07")
    lookback_start_str = lookback_start.strftime("%Y-%m-%d %H:%M:%S+07")

    apps_out = {}
    for app, segs in APP_SEGMENTS.items():
        rows = fetch_unanswered(client, segs, cutoff_str, lookback_start_str)
        chats = []
        for r in rows:
            last_msg_at = r.last_msg_at
            if cutoff - last_msg_at.astimezone(VN) < min_wait:
                continue
            waited = cutoff - last_msg_at.astimezone(VN)
            chats.append({
                "sessionId": r.session_id,
                "chatLink": f"https://app.crisp.chat/website/{r.website_id}/inbox/{r.session_id}",
                "customer": r.customerNickname or r.customerEmail or "Khách",
                "lastMessage": (r.content or "").strip()[:200],
                "lastMsgAtVn": last_msg_at.astimezone(VN).strftime("%d/%m/%Y %H:%M"),
                "daysWaiting": round(waited.total_seconds() / 86400, 1),
            })
        apps_out[app] = {"count": len(chats), "chats": chats}

    out = {
        "cutoffVn": cutoff.strftime("%d/%m/%Y %H:%M"),
        "lookbackDays": a.lookback_days,
        "minHoursWaiting": a.min_hours_waiting,
        "apps": apps_out,
        "total": sum(v["count"] for v in apps_out.values()),
    }

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"as of {out['cutoffVn']}: total={out['total']}")
        for app, d in apps_out.items():
            print(f"  {app}: {d['count']}")
            for c in d["chats"]:
                print(f"    {c['customer']} — {c['daysWaiting']}d — {c['chatLink']}")


if __name__ == "__main__":
    main()
