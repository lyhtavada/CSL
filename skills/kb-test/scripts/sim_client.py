#!/usr/bin/env python3
"""
sim_client.py — thin client for the sim-crisp API (/api/sim/*) used by
kb-test's sim mode. Runs test questions through the REAL bridge pipeline
(webhook -> gate -> worker -> process.ts -> agent) against a local sim
process, instead of the /api/chat shortcut.

Setup (one-time, see sim.env.example + start_sim.sh in this dir):
  1. tailscale up
  2. cp sim.env.example ~/avada-cs-ai-agent-crisp-chat/.env.sim, fill in blanks
  3. ./start_sim.sh   (or let ensure_sim_up() below auto-start it)

Creds: reuses ~/CSL/.env CS2_API_TOKEN as the sim bearer token (same
Postgres, same session/token store when DATABASE_URL in .env.sim points at
prod via HAProxy) plus a new SIM_BASE_URL key for the local sim process.
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid

ENV_PATH = os.path.expanduser("~/CSL/.env")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# dummy merchant profile per app — good enough for KB-content testing;
# override per-question via the "profile" key in questions.json if a test
# needs a specific plan/segment.
DEFAULT_PROFILES = {
    "chatty-agent": {
        "agentId": "chatty-agent",
        "nickname": "KB Test Merchant",
        "email": "kbtest@example.com",
        "shopDomain": "kb-test.myshopify.com",
        "appPlan": "pro",
    },
    "joy-loyalty-agent": {
        "agentId": "joy-loyalty-agent",
        "nickname": "KB Test Merchant",
        "email": "kbtest@example.com",
        "shopDomain": "kb-test.myshopify.com",
        "appPlan": "pro",
    },
    "wishlist-agent": {
        "agentId": "wishlist-agent",
        "nickname": "KB Test Merchant",
        "email": "kbtest@example.com",
        "shopDomain": "kb-test.myshopify.com",
        "appPlan": "pro",
    },
}


def load_sim_creds():
    base = token = None
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("SIM_BASE_URL="):
                    base = line.split("=", 1)[1].strip()
                elif line.startswith("CS2_API_TOKEN="):
                    token = line.split("=", 1)[1].strip()
    except FileNotFoundError:
        sys.exit(f"ERROR: {ENV_PATH} not found")
    base = base or "http://127.0.0.1:8031"
    if not token:
        sys.exit("ERROR: CS2_API_TOKEN missing in ~/CSL/.env (reused as sim bearer token)")
    return base.rstrip("/"), token


def _req(method, url, token, body=None, timeout=125):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("User-Agent", "kb-test-sim/1.0")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode()
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        raise RuntimeError(f"{method} {url} -> {e.code}: {raw}") from None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def ensure_sim_up(base, auto_start=True):
    try:
        urllib.request.urlopen(f"{base}/health", timeout=3)
        return
    except Exception:
        pass
    if not auto_start:
        sys.exit(f"ERROR: sim bridge not reachable at {base}. Run start_sim.sh first.")
    print(f"sim bridge not up at {base}, starting it...", file=sys.stderr)
    result = subprocess.run([os.path.join(SCRIPT_DIR, "start_sim.sh")])
    if result.returncode != 0:
        sys.exit("ERROR: start_sim.sh failed — see output above")


def new_session_id(app):
    return f"sim_kbtest_{app}_{uuid.uuid4().hex[:10]}"


def create_session(base, token, session_id, profile):
    body = {"sessionId": session_id, **profile}
    return _req("POST", f"{base}/api/sim/session", token, body)


def send_message(base, token, session_id, text, as_="customer", wait=True, timeout_ms=120000):
    body = {"sessionId": session_id, "text": text, "as": as_, "wait": wait, "timeoutMs": timeout_ms}
    return _req("POST", f"{base}/api/sim/message", token, body, timeout=timeout_ms / 1000 + 5)


def delete_session(base, token, session_id):
    try:
        return _req("DELETE", f"{base}/api/sim/session/{session_id}", token)
    except Exception as e:
        print(f"  warning: cleanup failed for {session_id}: {e}", file=sys.stderr)
        return None


def last_reply_text(result):
    """Pull the final bot text reply out of an /api/sim/message result."""
    replies = result.get("replies") or []
    if not replies:
        return ""
    return replies[-1]["content"]
