#!/usr/bin/env python3
"""
create_bug_ticket.py — file a system-bug ticket for Fennic (dev) when a bot
correction traces back to an AGENT BUG (retrieval/tool/router/prompt), not a
missing-KB-content problem.

Ticket API: POST https://avada-ts-a9cb0.web.app/api/external/tickets
  header X-API-Key = AVD_TICKET_API_KEY (~/CSL/.env)
  fields: subject(req), appName="Avada CS Ai", priority, members[]
          ({memberId, displayName}), tagIds

Members are fixed: Liz (CSL) + Fennic (dev owner of the AI agent).
  Liz   id = 6ib3wuO08IRX6qi87PK3Nv7pVTe2
  Fennic id = mlqDFdz7RBPrxLGkLufXPlbefIf2

Dedup: same root-cause bug repeating across days must NOT spam Fennic with a
new ticket every run. State file skills/bot-corrections/state/system-bugs.json
maps a stable `bug_key` (kebab-case slug the caller derives from the root
cause, e.g. "chatty-handoff-promise-no-tag") -> last ticket filed for it. On a
repeat:
  - GET the existing ticket; if still open (tsStatus not in done/closed states)
    -> SKIP creating a new one, POST a progress comment instead (confirmed
    endpoint: POST /api/external/tickets/{internal_id}/comments body
    {content, type:"commentTicket"} — see avada_ticket_post_comment_endpoint
    memory) noting the new occurrence (correction id/session), and bump
    occurrence count + last_seen. Do NOT touch tsStatus — Liz changes that
    herself (feedback_ticket_progress_comments, 2026-08-21).
  - If it's closed/done -> treat as regressed, file a NEW ticket (bug likely
    reintroduced) and update state.

Tag: looks up tag "ai-bot-bug" via GET /api/external/tags and applies it if it
exists (create the tag once manually in helpdesk if you want this filter to
work — script does not create tags).

Usage:
  python3 create_bug_ticket.py --bug-key <slug> --title <subject> \
      --summary <full description incl. session/correction ids + trace excerpt> \
      --app chatty|joy [--priority normal|high|urgent]

  On a repeat (existing open ticket), --summary is used as the comment body
  posted to the existing ticket instead of a new ticket's description.

Prints:  TICKET_ACTION=created|commented_existing_open|regressed_new
         TICKET_URL=<url>
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

ENV_PATH = os.path.expanduser("~/CSL/.env")
STATE_PATH = os.path.join(os.path.dirname(__file__), "..", "state", "system-bugs.json")
TICKET_BASE = "https://avada-ts-a9cb0.web.app"

MEMBERS = [
    {"memberId": "6ib3wuO08IRX6qi87PK3Nv7pVTe2", "displayName": "Liz"},
    {"memberId": "mlqDFdz7RBPrxLGkLufXPlbefIf2", "displayName": "Fennic"},
]
APP_NAME = "Avada CS Ai"
BUG_TAG_NAME = "ai-bot-bug"

# tsStatus values treated as "already closed" -> a repeat means regression,
# not spam. Adjust here if helpdesk uses different literals; verify on the
# first live ticket before trusting this list.
CLOSED_STATUSES = {"done", "closed", "resolved"}


def load_key():
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("AVD_TICKET_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    sys.exit("ERROR: AVD_TICKET_API_KEY missing in ~/CSL/.env")


def _req(method, path, key, body=None):
    url = TICKET_BASE + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("X-API-Key", key)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} -> HTTP {e.code}: {e.read().decode()[:500]}")


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as f:
            return json.load(f)
    return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def find_bug_tag_id(key):
    try:
        out = _req("GET", "/api/external/tags", key)
    except RuntimeError:
        return None
    tags = out if isinstance(out, list) else out.get("tags", out.get("data", []))
    for t in tags:
        if t.get("name") == BUG_TAG_NAME:
            return t.get("id")
    return None


def create_ticket(key, title, summary, app, priority):
    body = {
        "subject": title,
        "description": summary,
        "appName": APP_NAME,
        "priority": priority,
        "tsStatus": "pending",
        "members": MEMBERS,
    }
    tag_id = find_bug_tag_id(key)
    if tag_id:
        body["tagIds"] = [tag_id]
    return _req("POST", "/api/external/tickets", key, body)


def get_ticket(key, ticket_id):
    """Returns (tsStatus_lower, ticketId, internal_id, url) or None on failure."""
    try:
        out = _req("GET", f"/api/external/tickets/{ticket_id}", key)
    except RuntimeError:
        return None
    t = out.get("data", out) if isinstance(out, dict) else out
    return (t.get("tsStatus") or "").lower(), t.get("ticketId"), t.get("id"), t.get("url")


def post_comment(key, internal_id, content):
    return _req("POST", f"/api/external/tickets/{internal_id}/comments", key,
                {"content": content, "type": "commentTicket"})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bug-key", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--summary", required=True)
    ap.add_argument("--app", required=True, choices=["chatty", "joy"])
    ap.add_argument("--priority", default="normal")
    args = ap.parse_args()

    key = load_key()
    state = load_state()
    entry = state.get(args.bug_key)

    if entry:
        info = None
        try:
            info = get_ticket(key, entry["ticket_id"])
        except Exception as e:
            print(f"WARN: could not re-check existing ticket status: {e}", file=sys.stderr)
        if info is not None:
            status, _ticket_id, internal_id, url = info
            if status not in CLOSED_STATUSES:
                entry["occurrences"] = entry.get("occurrences", 1) + 1
                entry["last_seen_app"] = args.app
                if internal_id:
                    entry["internal_id"] = internal_id
                try:
                    post_comment(key, internal_id or entry.get("internal_id"),
                                 f"[Betty] New occurrence (#{entry['occurrences']}) — {args.summary}")
                except RuntimeError as e:
                    print(f"WARN: could not post comment on existing ticket: {e}", file=sys.stderr)
                save_state(state)
                print("TICKET_ACTION=commented_existing_open")
                print(f"TICKET_URL={url or entry.get('ticket_url', '')}")
                return

    try:
        out = create_ticket(key, args.title, args.summary, args.app, args.priority)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    t = out.get("data", out) if isinstance(out, dict) else out
    ticket_id = t.get("ticketId") or t.get("id")
    internal_id = t.get("id")
    ticket_url = t.get("url") or f"https://helpdesk.avada.net/tickets/{internal_id or ''}"

    state[args.bug_key] = {
        "ticket_id": ticket_id,
        "internal_id": internal_id,
        "ticket_url": ticket_url,
        "app": args.app,
        "title": args.title,
        "occurrences": 1,
    }
    save_state(state)
    print("TICKET_ACTION=created" if not entry else "TICKET_ACTION=regressed_new")
    print(f"TICKET_URL={ticket_url}")


if __name__ == "__main__":
    main()
