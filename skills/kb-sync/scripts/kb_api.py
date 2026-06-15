#!/usr/bin/env python3
"""
kb_api.py — thin client for the CS v2 KB API (cs2.avada.net).

Routes (confirmed from the v2 API catalog):
  GET  /api/kb/files?agent=<id>            -> ["agent.yaml", "kb/faq/...md", ...]
  GET  /api/kb/file?agent=<id>&path=<p>    -> {"content": "..."}
  POST /api/kb/file   body {agent,path,content}  -> {"ok":true}   (auto git commit)
  POST /api/kb/reindex body {agent}              -> {"ok":true,"chunks":N,"partial":false}

Auth: Authorization: Bearer <CS2_API_TOKEN>  (super_admin token).
Creds read from ~/CSL/.env keys CS2_API_URL + CS2_API_TOKEN.

Agent ids: chatty-agent (Chatty/Ivy), joy-loyalty-agent (Joy).
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
}


def load_creds():
    url = token = None
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("CS2_API_URL="):
                    url = line.split("=", 1)[1].strip()
                elif line.startswith("CS2_API_TOKEN="):
                    token = line.split("=", 1)[1].strip()
    except FileNotFoundError:
        sys.exit(f"ERROR: {ENV_PATH} not found")
    if not url or not token:
        sys.exit("ERROR: CS2_API_URL / CS2_API_TOKEN missing in ~/CSL/.env")
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


if __name__ == "__main__":
    # quick CLI: kb_api.py list <app> | get <app> <path> | reindex <app>
    base, token = load_creds()
    if len(sys.argv) < 3:
        sys.exit("usage: kb_api.py {list|get|reindex} <app> [path]")
    cmd, app = sys.argv[1], sys.argv[2]
    agent = agent_id(app)
    if cmd == "list":
        print("\n".join(list_files(base, token, agent)))
    elif cmd == "get":
        print(get_file(base, token, agent, sys.argv[3]))
    elif cmd == "reindex":
        print(json.dumps(reindex(base, token, agent)))
    else:
        sys.exit(f"unknown cmd {cmd}")
