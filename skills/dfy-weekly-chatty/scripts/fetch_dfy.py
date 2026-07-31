#!/usr/bin/env python3
"""
Fetch + analyze weekly DFY tickets for an app (Chatty) from the Avada Ticket API.

Pulls DFY tickets for a Fri→Thu week, splits them into Inbound (no `proactive`
tag) vs Proactive (has `proactive` tag), computes adopt rate per group +
insights, maps each CS to their KPI nickname, and emits a single JSON blob to
stdout (or --out).

Usage:
  python3 fetch_dfy.py --app chatty --start 2026-07-31 --end 2026-08-06 [--out /tmp/dfy.json]

Auth: AVD_TICKET_API_KEY + BQ_SA_* from CSL/.env.

Review tracking is automatic (not a manual `review-yes` tag), three layers:
1. session_id from the ticket's chatLink, matched against `avada_cs.crisp_chats`
   for a `review_yes_chatty`/`rv_yes_chatty`/`review_yes_faq` segment.
2. store-domain fallback, for reviews that landed on a different chat.
3. store-name fallback: the ticket's own Crisp `customerNickname` (= visitor
   data "name") matched against this week's Chatty App Store review names
   (scraped, see fetch_reviews.py) — catches reviews nobody tagged at all.
`dfy_per_install` compares this week's DFY ticket count against Chatty's
new installs that week (`avada_product_dash.dash_daily_installs`).

Output shape (JSON):
  {
    "app": "chatty",
    "period": {"start": "2026-07-31", "end": "2026-08-06"},
    "total": 27, "adopted": 14, "adopt_pct": 52,
    "inbound":   {"count": 22, "adopted": 14, "adopt_pct": 64, "tickets": [...]},
    "proactive": {"count": 5,  "adopted": 0,  "adopt_pct": 0,  "tickets": [...]},
    "per_cs": [{"nick": "AnhBD", "display": "AnhBD (Andy)", "count": 16,
                "adopted": 7, "adopt_pct": 44, "video": 9, "video_pct": 56}, ...],
    "insights": {
        "video":   {"yes_adopt_pct": 69, "no_adopt_pct": 27, "yes_n": 16, "no_n": 11, "delta": 42},
        "ai":      {"full_adopt_pct": 83, "zero_adopt_pct": 0},
        "chatbox": {"task_pct": 16, "zero_ticket": 19, "total_ticket": 27},
        "timing":  {"by_day": {"Fri":1,"Mon":4,"Tue":20}, "peak_day": "Tue", "peak_n": 20},
        "review_yes": 4,
        "review": {"count": 4, "total": 27, "pct": 15},
        "dfy_per_install": {"dfy_tickets": 27, "installs": 1689, "pct": 1.6}
    }
  }

A ticket row: {date, ticket_id, url, store, cs_nick, cs_display, tasks_done,
               tasks_total, tags}
"""
import os, re, sys, json, argparse, datetime, importlib.util
import urllib.request, urllib.parse
from collections import defaultdict, Counter

BASE = "https://avada-ts-a9cb0.web.app"

# App Store review "name" = the store's display name, same string Crisp stores
# as `customerNickname` for that store's chats. Lets us match a review back to
# a DFY ticket even when nobody tagged the chat with review_yes_chatty — see
# memory dfy_monthly_review_name_match.md. Loaded by path since cs-weekly/
# isn't a package.
_FR_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "cs-weekly", "scripts", "fetch_reviews.py")
_spec = importlib.util.spec_from_file_location("fetch_reviews", _FR_PATH)
fetch_reviews = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fetch_reviews)
REVIEW_APP_SLUG = {"chatty": "chatty"}

# Segments on a Crisp session that mean "this store already left a review" —
# see memory bq_crisp_segments.md. Chatty carries variants because the app was
# formerly named FAQ.
REVIEW_SEGMENTS = ["review_yes_chatty", "rv_yes_chatty", "review_yes_faq"]

SESSION_RE = re.compile(r"session_([a-f0-9-]+)")

# App name as the Ticket API expects it.
APP_NAME = {"chatty": "Chatty", "joy": "JOY Loyalty"}

# app_id as used in the analytics warehouse (dash_daily_installs). Chatty was
# formerly named "FAQ" internally, hence "avadaFaq".
INSTALL_APP_ID = {"chatty": "avadaFaq"}

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
    # 2026-07: the API started also emitting bare first names (no "_avada"
    # suffix) as displayName for some tickets — same person, different
    # string. Without these, per-CS grouping silently splits one CS into two
    # rows (e.g. "Andy 30" + "Andy 9" instead of one "AnhBD (Andy) 39").
    "liz": "LyHT", "hana": "HangHM", "audrey": "VanCT", "alyssa": "LyPK",
    "sonny": "HuyTC", "alicia": "AnhLN", "rosie": "ThaoLTT", "jade": "PhuongNT",
    "mirra": "MinhBT", "andy": "AnhBD", "hazel": "HienPT", "cody": "ChauHM",
    "phoebe": "PhuongTTM", "linda1": "LinhTLK", "linda": "LinhTLK",
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


def api_get(path, key, params=None, retries=2):
    """no_adopt_raw fetches one comments-endpoint call per non-adopted ticket
    (50+ in a busy week) — a single transient timeout shouldn't kill the
    whole report, so retry a couple of times before giving up."""
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-API-Key": key})
    last_err = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
    raise last_err


def fetch_comments(ticket_internal_id, key):
    """CS comments on a ticket (`/actions`, filtered to type=commentTicket),
    oldest first. Requires the ticket's internal `id` (NOT the human `ticketId`
    like CHAT-260629-PZ2k8J) — the API returns an empty action list otherwise."""
    data = api_get(f"/api/external/tickets/{ticket_internal_id}/actions", key)
    actions = data.get("data", {}).get("actions", [])
    comments = [a for a in actions if a.get("type") == "commentTicket"]
    comments.sort(key=lambda a: a.get("createdAt", ""))
    return [{"author": a.get("author", {}).get("displayName", "?"),
             "at": a.get("createdAt", ""),
             "content": a.get("metadata", {}).get("content", "")}
            for a in comments]


def bq_client(env):
    from google.oauth2 import service_account
    from google.cloud import bigquery

    creds = service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "client_email": env["BQ_SA_CLIENT_EMAIL"],
            "private_key": env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n"),
            "token_uri": "https://oauth2.googleapis.com/token",
        },
        scopes=["https://www.googleapis.com/auth/bigquery"],
    )
    return bigquery.Client(project="avada-crm", credentials=creds)


def session_id_from_chatlink(chat_link):
    if not chat_link:
        return None
    m = SESSION_RE.search(chat_link)
    return m.group(1) if m else None


def fetch_reviewed(client, session_ids, domains, since):
    """Return (set of session_ids, set of shopifyDomains) that already carry a
    review_yes segment. Two-tier match: exact session_id from the ticket's
    chatLink (precise), plus a domain+time fallback for tickets whose review
    landed in a different chat than the one linked on the ticket."""
    if not session_ids and not domains:
        return set(), set()
    from google.cloud import bigquery as bq

    # shopifyDomain is stored as e.g. "https://store.myshopify.com" — strip the
    # scheme (and any trailing slash) before comparing against the ticket's
    # bare store.domain.
    seg_clause = " OR ".join(f"LOWER(segments) LIKE '%{s}%'" for s in REVIEW_SEGMENTS)
    q = f"""
    SELECT DISTINCT session_id,
           REGEXP_REPLACE(REGEXP_REPLACE(LOWER(shopifyDomain), r'^https?://', ''), r'/$', '') AS domain
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE ({seg_clause})
      AND timestamp >= @since
      AND (session_id IN UNNEST(@session_ids)
           OR REGEXP_REPLACE(REGEXP_REPLACE(LOWER(shopifyDomain), r'^https?://', ''), r'/$', '') IN UNNEST(@domains))
    """
    job = client.query(q, job_config=bq.QueryJobConfig(query_parameters=[
        bq.ScalarQueryParameter("since", "TIMESTAMP", since),
        bq.ArrayQueryParameter("session_ids", "STRING", list(session_ids) or [""]),
        bq.ArrayQueryParameter("domains", "STRING", [d.lower() for d in domains] or [""]),
    ]))
    rev_sessions, rev_domains = set(), set()
    for row in job.result():
        if row.session_id:
            rev_sessions.add(row.session_id)
        if row.domain:
            rev_domains.add(row.domain)
    return rev_sessions, rev_domains


def fetch_customer_names(client, session_ids, domains):
    """customerNickname (= visitor-data "name") per session_id and per store
    domain, for matching a ticket's store against the App Store review names
    fetch_review_names() returns — independent of any review_yes tag."""
    if not session_ids and not domains:
        return {}, {}
    from google.cloud import bigquery as bq
    q = """
    SELECT session_id,
           REGEXP_REPLACE(REGEXP_REPLACE(LOWER(shopifyDomain), r'^https?://', ''), r'/$', '') AS domain,
           customerNickname
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE customerNickname IS NOT NULL
      AND (session_id IN UNNEST(@session_ids)
           OR REGEXP_REPLACE(REGEXP_REPLACE(LOWER(shopifyDomain), r'^https?://', ''), r'/$', '') IN UNNEST(@domains))
    """
    job = client.query(q, job_config=bq.QueryJobConfig(query_parameters=[
        bq.ArrayQueryParameter("session_ids", "STRING", list(session_ids) or [""]),
        bq.ArrayQueryParameter("domains", "STRING", [d.lower() for d in domains] or [""]),
    ]))
    by_session, by_domain = {}, {}
    for row in job.result():
        if row.session_id and row.session_id not in by_session:
            by_session[row.session_id] = row.customerNickname
        if row.domain and row.domain not in by_domain:
            by_domain[row.domain] = row.customerNickname
    return by_session, by_domain


def fetch_review_names(app, start, end):
    """Store names on Chatty's App Store reviews this week (scraped page —
    see fetch_reviews.py). Returns a set of normalized (lowered, stripped)
    names. Empty set if the app has no review scraping wired up."""
    slug = REVIEW_APP_SLUG.get(app)
    if not slug:
        return set()
    import datetime
    s = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    e = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    rows = fetch_reviews.fetch(slug, s, e)
    return {nm.strip().lower() for d, _, nm in rows if s <= d <= e and nm}


def fetch_installs(client, app_id, start, end):
    q = """
    SELECT SUM(unique_shops) AS installs
    FROM `avada-crm.avada_product_dash.dash_daily_installs`
    WHERE app_id = @app_id AND day BETWEEN @start AND @end
    """
    from google.cloud import bigquery as bq
    job = client.query(q, job_config=bq.QueryJobConfig(query_parameters=[
        bq.ScalarQueryParameter("app_id", "STRING", app_id),
        bq.ScalarQueryParameter("start", "DATE", start),
        bq.ScalarQueryParameter("end", "DATE", end),
    ]))
    for row in job.result():
        return row.installs or 0
    return 0


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


def ticket_reviewed(t, rev_sessions, rev_domains):
    sess = session_id_from_chatlink(t.get("chatLink"))
    domain = (t.get("store") or [{}])[0].get("domain", "").lower()
    return (sess and sess in rev_sessions) or (domain and domain in rev_domains)


def ticket_reviewed_by_name(t, by_session, by_domain, review_names):
    """Third, independent match layer: the ticket's own store name (Crisp
    customerNickname) against this week's App Store review names — catches
    reviews nobody tagged review_yes_chatty on at all."""
    sess = session_id_from_chatlink(t.get("chatLink"))
    domain = (t.get("store") or [{}])[0].get("domain", "").lower()
    name = (sess and by_session.get(sess)) or (domain and by_domain.get(domain))
    return bool(name and name.strip().lower() in review_names)


def adopt(group, id2name):
    a = sum(1 for t in group if "DFY-adopted" in names(t, id2name))
    pct = round(100 * a / len(group)) if group else 0
    return a, pct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default="chatty", choices=["chatty", "joy"])
    ap.add_argument("--start", required=True, help="YYYY-MM-DD, period start (a Friday)")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD, period end (a Thursday)")
    ap.add_argument("--out", help="Write JSON here instead of stdout")
    a = ap.parse_args()

    env = load_env()
    key = env["AVD_TICKET_API_KEY"]

    start, end = a.start, a.end

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

    DOW = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    by_day = Counter()
    for t in op:
        d = (t.get("createdAt") or "")[:10]
        try:
            dow = datetime.date.fromisoformat(d).weekday()
            by_day[DOW[dow]] += 1
        except ValueError:
            pass
    peak_day, peak_n = (max(by_day.items(), key=lambda x: x[1]) if by_day else ("-", 0))

    # ---- review tracking (automatic, via BigQuery crisp_chats segments) ----
    # Two-tier match: exact session_id parsed from the ticket's chatLink, plus
    # a store-domain fallback (in case the review landed on a different chat
    # session than the one linked on the ticket). See memory bq_crisp_segments.md.
    bq = bq_client(env)
    session_ids = {s for s in (session_id_from_chatlink(t.get("chatLink")) for t in op) if s}
    domains = {(t.get("store") or [{}])[0].get("domain", "") for t in op}
    domains.discard("")
    rev_sessions, rev_domains = fetch_reviewed(bq, session_ids, domains, f"{start} 00:00:00")

    # Third layer: match the ticket's own store name (Crisp customerNickname)
    # against this week's App Store review names — catches reviews nobody
    # tagged at all. Independent of the tag-based match above.
    by_session, by_domain = fetch_customer_names(bq, session_ids, domains)
    review_names = fetch_review_names(a.app, start, end)
    review_by_name = sum(1 for t in op
                          if not ticket_reviewed(t, rev_sessions, rev_domains)
                          and ticket_reviewed_by_name(t, by_session, by_domain, review_names))

    review_yes = sum(1 for t in op if ticket_reviewed(t, rev_sessions, rev_domains)
                      or ticket_reviewed_by_name(t, by_session, by_domain, review_names))
    review_pct = round(100 * review_yes / len(op)) if op else 0

    # ---- DFY tickets / app installs this week ----
    installs = fetch_installs(bq, INSTALL_APP_ID.get(a.app, ""), start, end) if a.app in INSTALL_APP_ID else 0
    dfy_per_install_pct = round(100 * len(op) / installs, 2) if installs else 0

    # ---- no-adopt reasons (raw comments — Betty reads these and derives the
    # reason buckets herself each run; no keyword/tag classification here) ----
    no_adopt = [t for t in op if "DFY-adopted" not in names(t, id2name)]
    no_adopt_raw = []
    for t in no_adopt:
        comments = fetch_comments(t.get("id"), key)
        if comments:
            no_adopt_raw.append({
                "ticket_id": t.get("ticketId"),
                "store": (t.get("store") or [{}])[0].get("domain", ""),
                "cs": DISPLAY.get(creator(t), creator(t)),
                "comments": comments,
            })

    result = {
        "app": a.app,
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
            "timing": {"by_day": {d: by_day.get(d, 0) for d in DOW if by_day.get(d)},
                       "peak_day": peak_day, "peak_n": peak_n},
            "review_yes": review_yes,
            "review": {"count": review_yes, "total": len(op), "pct": review_pct,
                       "matched_by_name": review_by_name},
            "dfy_per_install": {"dfy_tickets": len(op), "installs": installs,
                                "pct": dfy_per_install_pct},
        },
        "no_adopt_raw": no_adopt_raw,
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
