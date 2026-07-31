"""
Shared "real conversation" counter for BigQuery avada_cs.crisp_chats.

A conversation = a burst of merchant-initiated text messages (a Crisp session_id
sessionized on silence gaps), counted only when the merchant actually engaged.
Filters out three sources of noise a naive COUNT(DISTINCT session_id) or a raw
message-gap count would miss:

  1. CS/operator-initiated chats (no merchant demand) — anchor gaps on
     fromType='user' only, operator messages never start/reset a conversation.
  2. "Click-and-silence" chats — merchant clicks an app CTA (e.g. "I need help
     setup AI agent"), which fires one automatic text message; bot replies;
     merchant never engages further. Requires >= MIN_USER_MSGS user text
     messages per conversation, which also naturally excludes case 1's leftover
     zero-message sessions.
  3. Avada-internal test traffic — customerEmail on an @avada* domain (staff
     dogfooding the bot), excluded from the count.

Session_id is permanent per visitor in Crisp (a merchant returning weeks later
keeps the same session_id), so sessions are split into separate conversations
whenever a silence gap >= GAP_HOURS occurs between merchant messages. GAP_HOURS
was validated against real Chatty data (2026-07): counts are stable across
2-12h gaps (326/311/311/309/306 at 2/4/6/8/12h), so 6h is not a sensitive
choice, and CS reply latency (median 0min, p95 4min) confirmed shift length
(4h) has no bearing on it — replies are near-instant regardless of shift.

Boundary handling: gaps are computed over a lookback window BEFORE the report
start (not just the report window itself), then only conversations whose
*start* timestamp falls inside [start, end) are counted. Without this, a
conversation that began before the window and continues into it (within
GAP_HOURS) gets wrongly counted as a brand-new conversation — verified on
real data: 5/311 sessions in a sample week were this kind of boundary
spillover.

`chat_count()` counts conversations that *started* inside [start, end) — right for
weekly/monthly reporting, where periods are meant to sum without double-counting a
conversation that spans a period boundary. It only looks BACKWARD (lookback) to get
the gap math right at the start edge; it does not look forward past `end`, so at
report granularities where boundaries are frequent (daily) this systematically
undercounts: a conversation starting late in the day (e.g. 23:00) that continues past
midnight only has 1 message inside the day's window, and gets dropped by the
`min_user_msgs` filter even though it's a real 2+ message conversation.

`chat_count_active()` is for that case (used by /cs-daily-brief): it counts
conversations *active* (>=1 merchant message) inside [start, end), computing
msg_count over the conversation's FULL span using both a lookback AND a lookahead
buffer — so a conversation crossing midnight is correctly kept, and is (by design)
counted on every calendar day it touches, same as the daily brief's original
"sessions touched today" semantics. Do not use this for weekly/monthly volume — it
double-counts conversations spanning a period boundary on purpose.

Usage:
    from chat_count import chat_count, chat_count_active, APP_SEGMENTS
    n = chat_count(bq_client, APP_SEGMENTS["chatty"], "2026-07-20", "2026-07-27")
    n_today = chat_count_active(bq_client, APP_SEGMENTS["chatty"], "2026-07-26", "2026-07-26")
"""
import datetime

GAP_HOURS = 6
MIN_USER_MSGS = 2
LOOKBACK_DAYS = 2  # >= GAP_HOURS/24 rounded up, with margin
LOOKAROUND_DAYS = 2  # lookback/lookahead margin for chat_count_active

APP_SEGMENTS = {
    "chatty": ["app_chatty", "app_faqs"],
    "joy": ["app_joy"],
    "wishlist": ["app_wishlist"],
}

INTERNAL_EMAIL_PATTERNS = ["%avadagroup.com%", "%avada.io%", "%avada.email%"]


def chat_count(client, segments, start, end, gap_hours=GAP_HOURS,
                min_user_msgs=MIN_USER_MSGS, exclude_internal=True):
    """Count real merchant conversations in [start, end] (YYYY-MM-DD, inclusive,
    Asia/Bangkok +07). `segments` is a list like APP_SEGMENTS["chatty"]."""
    from google.cloud import bigquery

    seg_clause = " OR ".join(f"segments LIKE @s{i}" for i in range(len(segments)))
    params = [
        bigquery.ScalarQueryParameter(f"s{i}", "STRING", f"%{s}%")
        for i, s in enumerate(segments)
    ]

    end_excl = (datetime.datetime.strptime(end, "%Y-%m-%d").date()
                + datetime.timedelta(days=1)).isoformat()
    lookback_start = (datetime.datetime.strptime(start, "%Y-%m-%d").date()
                       - datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()

    internal_clause = ""
    if exclude_internal:
        internal_clause = "AND NOT (" + " OR ".join(
            f"LOWER(customerEmail) LIKE '{p}'" for p in INTERNAL_EMAIL_PATTERNS
        ) + ")"

    sql = f"""
    WITH msgs AS (
      SELECT session_id, timestamp
      FROM `avada-crm.avada_cs.crisp_chats`
      WHERE ({seg_clause})
        AND type = 'text' AND fromType = 'user'
        AND content IS NOT NULL AND TRIM(content) != ''
        AND timestamp >= TIMESTAMP("{lookback_start} 00:00:00+07")
        AND timestamp <  TIMESTAMP("{end_excl} 00:00:00+07")
        {internal_clause}
    ),
    flagged AS (
      SELECT session_id, timestamp,
        IF(
          LAG(timestamp) OVER (PARTITION BY session_id ORDER BY timestamp) IS NULL
          OR TIMESTAMP_DIFF(
               timestamp,
               LAG(timestamp) OVER (PARTITION BY session_id ORDER BY timestamp),
               HOUR
             ) >= {gap_hours},
          1, 0
        ) AS is_start
      FROM msgs
    ),
    grouped AS (
      SELECT session_id, timestamp,
        SUM(is_start) OVER (PARTITION BY session_id ORDER BY timestamp) AS grp
      FROM flagged
    ),
    conv AS (
      SELECT session_id, grp, MIN(timestamp) AS conv_start, COUNT(*) AS msg_count
      FROM grouped
      GROUP BY session_id, grp
    )
    SELECT COUNT(*) AS n
    FROM conv
    WHERE msg_count >= {min_user_msgs}
      AND conv_start >= TIMESTAMP("{start} 00:00:00+07")
      AND conv_start <  TIMESTAMP("{end_excl} 00:00:00+07")
    """
    job = bigquery.QueryJobConfig(query_parameters=params)
    return list(client.query(sql, job_config=job).result())[0].n


def chat_count_active(client, segments, start, end, gap_hours=GAP_HOURS,
                       min_user_msgs=MIN_USER_MSGS, exclude_internal=True,
                       lookaround_days=LOOKAROUND_DAYS):
    """Count real merchant conversations ACTIVE (>=1 merchant message) in
    [start, end] (YYYY-MM-DD, inclusive, Asia/Bangkok +07) — see module docstring
    for why this differs from chat_count(). `segments` is a list like
    APP_SEGMENTS["chatty"]."""
    win_start = f"{start} 00:00:00+07"
    win_end_excl = (datetime.datetime.strptime(end, "%Y-%m-%d").date()
                     + datetime.timedelta(days=1)).isoformat() + " 00:00:00+07"
    fetch_start = (datetime.datetime.strptime(start, "%Y-%m-%d").date()
                    - datetime.timedelta(days=lookaround_days)).isoformat() + " 00:00:00+07"
    fetch_end = (datetime.datetime.strptime(end, "%Y-%m-%d").date()
                 + datetime.timedelta(days=1 + lookaround_days)).isoformat() + " 00:00:00+07"
    return chat_count_window(client, segments, win_start, win_end_excl, fetch_start, fetch_end,
                              gap_hours=gap_hours, min_user_msgs=min_user_msgs,
                              exclude_internal=exclude_internal)


def chat_count_window(client, segments, win_start, win_end_excl, fetch_start, fetch_end,
                       gap_hours=GAP_HOURS, min_user_msgs=MIN_USER_MSGS,
                       exclude_internal=True):
    """Count real merchant conversations ACTIVE (>=1 merchant message) in the
    exact [win_start, win_end_excl) timestamp window (each a full
    'YYYY-MM-DD HH:MM:SS+07' string, not just a calendar date) — the
    time-of-day-aware sibling of `chat_count_active`, for callers whose
    reporting window doesn't align to midnight (e.g. /cs-daily-brief's
    08:30-to-08:30 rolling window). `fetch_start`/`fetch_end` are the
    lookaround-widened bounds used for the gap-sessionization CTE, same role
    as in `chat_count_active`. `segments` is a list like APP_SEGMENTS["chatty"]."""
    from google.cloud import bigquery

    seg_clause = " OR ".join(f"segments LIKE @s{i}" for i in range(len(segments)))
    params = [
        bigquery.ScalarQueryParameter(f"s{i}", "STRING", f"%{s}%")
        for i, s in enumerate(segments)
    ]

    internal_clause = ""
    if exclude_internal:
        internal_clause = "AND NOT (" + " OR ".join(
            f"LOWER(customerEmail) LIKE '{p}'" for p in INTERNAL_EMAIL_PATTERNS
        ) + ")"

    sql = f"""
    WITH msgs AS (
      SELECT session_id, timestamp
      FROM `avada-crm.avada_cs.crisp_chats`
      WHERE ({seg_clause})
        AND type = 'text' AND fromType = 'user'
        AND content IS NOT NULL AND TRIM(content) != ''
        AND timestamp >= TIMESTAMP("{fetch_start}")
        AND timestamp <  TIMESTAMP("{fetch_end}")
        {internal_clause}
    ),
    flagged AS (
      SELECT session_id, timestamp,
        IF(
          LAG(timestamp) OVER (PARTITION BY session_id ORDER BY timestamp) IS NULL
          OR TIMESTAMP_DIFF(
               timestamp,
               LAG(timestamp) OVER (PARTITION BY session_id ORDER BY timestamp),
               HOUR
             ) >= {gap_hours},
          1, 0
        ) AS is_start
      FROM msgs
    ),
    grouped AS (
      SELECT session_id, timestamp,
        SUM(is_start) OVER (PARTITION BY session_id ORDER BY timestamp) AS grp
      FROM flagged
    ),
    conv AS (
      SELECT session_id, grp,
        COUNT(*) AS msg_count,
        LOGICAL_OR(timestamp >= TIMESTAMP("{win_start}")
                   AND timestamp < TIMESTAMP("{win_end_excl}")) AS touches_window
      FROM grouped
      GROUP BY session_id, grp
    )
    SELECT COUNT(*) AS n
    FROM conv
    WHERE msg_count >= {min_user_msgs} AND touches_window
    """
    job = bigquery.QueryJobConfig(query_parameters=params)
    return list(client.query(sql, job_config=job).result())[0].n
