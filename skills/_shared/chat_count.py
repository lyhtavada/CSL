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

Usage:
    from chat_count import chat_count, APP_SEGMENTS
    n = chat_count(bq_client, APP_SEGMENTS["chatty"], "2026-07-20", "2026-07-27")
"""
import datetime

GAP_HOURS = 6
MIN_USER_MSGS = 2
LOOKBACK_DAYS = 2  # >= GAP_HOURS/24 rounded up, with margin

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
