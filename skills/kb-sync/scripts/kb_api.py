#!/usr/bin/env python3
"""
kb_api.py — thin client for the CS v2 KB API. Same API surface exists on
TWO environments (confirmed 2026-09-04, sim runs the same app code as
prod, just a separate DB — no data crossover):
  - prod: cs2.avada.net  (real merchants, real bots)
  - sim:  sim.avada.net  (own DB, edit/reindex freely, zero prod impact —
    stood up by Quảng/Fennic; no VPN/Tailscale needed)

Routes (confirmed from the v2 API catalog, present on both):
  GET  /api/kb/files?agent=<id>            -> ["agent.yaml", "kb/faq/...md", ...]
  GET  /api/kb/file?agent=<id>&path=<p>    -> {"content": "..."}
  POST /api/kb/file   body {agent,path,content}  -> {"ok":true}   (auto git commit)
  POST /api/kb/reindex body {agent}              -> {"ok":true,"chunks":N,"partial":false}

Auth: Authorization: Bearer <token> (super_admin token — separate tokens
per environment, do not reuse one for the other).
Creds read from ~/CSL/.env: CS2_API_URL + CS2_API_TOKEN (prod), or
SIM_BASE_URL + SIM_API_TOKEN (sim). `load_creds(target="sim")` picks sim.

**Recommended flow for a KB patch, safest first** (2026-09-04): push to sim
→ reindex sim → test (kb-test, direct or sim mode against sim.avada.net) →
if OK → push same content to prod → reindex prod. Sim's KB is a frozen
snapshot as of whenever it was last synced — it will NOT auto-reflect a
prod patch pushed without also pushing to sim, so don't assume sim is
already current.

Agent ids: chatty-agent (Chatty/Ivy), joy-loyalty-agent (Joy), wishlist-agent (Joy Wishlist/Wendy).
"""
import json
import os
import sys
import urllib.request
import urllib.parse

ENV_PATH = os.path.expanduser("~/CSL/.env")
APP_AGENTS = {
    "chatty": "chatty-agent",
    "joy": "joy-loyalty-agent",
    "wishlist": "wishlist-agent",
}


TARGET_KEYS = {
    "prod": ("CS2_API_URL=", "CS2_API_TOKEN=", "CS2_API_URL / CS2_API_TOKEN"),
    "sim": ("SIM_BASE_URL=", "SIM_API_TOKEN=", "SIM_BASE_URL / SIM_API_TOKEN"),
}


def load_creds(target="prod"):
    if target not in TARGET_KEYS:
        sys.exit(f"ERROR: unknown target {target!r}, must be 'prod' or 'sim'")
    url_key, token_key, names = TARGET_KEYS[target]
    url = token = None
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith(url_key):
                    url = line.split("=", 1)[1].strip()
                elif line.startswith(token_key):
                    token = line.split("=", 1)[1].strip()
    except FileNotFoundError:
        sys.exit(f"ERROR: {ENV_PATH} not found")
    if not url or not token:
        sys.exit(f"ERROR: {names} missing in ~/CSL/.env (target={target})")
    return url.rstrip("/"), token


def agent_id(app):
    a = app.lower().strip()
    if a in APP_AGENTS:
        return APP_AGENTS[a]
    # allow passing a raw agent id directly
    return a


def _req(method, url, token, body=None, timeout=180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("User-Agent", "kb-sync/1.0")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def list_files(base, token, agent):
    url = f"{base}/api/kb/files?agent={urllib.parse.quote(agent)}"
    out = _req("GET", url, token)
    return out if isinstance(out, list) else out.get("files", [])


def get_file(base, token, agent, path):
    q = urllib.parse.urlencode({"agent": agent, "path": path})
    out = _req("GET", f"{base}/api/kb/file?{q}", token)
    if isinstance(out, dict) and "content" in out:
        return out["content"]
    return None


def put_file(base, token, agent, path, content):
    return _req("POST", f"{base}/api/kb/file", token,
                {"agent": agent, "path": path, "content": content})


def reindex(base, token, agent):
    return _req("POST", f"{base}/api/kb/reindex", token, {"agent": agent}, timeout=300)


def chat(base, token, agent, message):
    """POST /api/chat — test the live bot as a merchant would. Returns the full
    response dict: {agent, reply, model, duration_ms, sources_count}."""
    return _req("POST", f"{base}/api/chat", token,
                {"agent": agent, "message": message}, timeout=90)


if __name__ == "__main__":
    # quick CLI: kb_api.py list <app> | get <app> <path> | reindex <app> [--target sim|prod]
    args = sys.argv[1:]
    target = "prod"
    if "--target" in args:
        i = args.index("--target")
        target = args[i + 1]
        del args[i:i + 2]
    base, token = load_creds(target)
    if len(args) < 2:
        sys.exit("usage: kb_api.py {list|get|reindex} <app> [path] [--target sim|prod]")
    cmd, app = args[0], args[1]
    agent = agent_id(app)
    if cmd == "list":
        print("\n".join(list_files(base, token, agent)))
    elif cmd == "get":
        print(get_file(base, token, agent, args[2]))
    elif cmd == "reindex":
        print(json.dumps(reindex(base, token, agent)))
    else:
        sys.exit(f"unknown cmd {cmd}")
