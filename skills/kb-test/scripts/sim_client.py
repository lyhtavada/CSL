#!/usr/bin/env python3
"""
sim_client.py — thin client for the hosted sim gateway (/api/sim/*) used by
kb-test's sim mode. Runs test questions through the REAL bridge pipeline
(webhook -> gate -> worker -> process.ts -> agent) against a sim environment
with its OWN database — no local process, no Tailscale, doesn't touch real
merchant data.

Setup (2026-09-04, replaces the old local sim-crisp + Tailscale flow —
Quảng/Fennic stood up a hosted sim gateway):
  1. Base URL: https://sim.avada.net (public internet, no VPN/Tailscale needed)
  2. Auth: API token, separate from the prod CS2_API_TOKEN — ask Quảng
     (Fennic, Slack U01N91HCC3F) for access/token, requires `console.chat`
     permission. Set SIM_API_TOKEN in ~/CSL/.env.
  3. SIM_BASE_URL in ~/CSL/.env is optional — defaults to https://sim.avada.net.

Docs: https://notes.avada.net/NsrlpDfTTa.md?name=api-cong-sim (API reference)

Note from the docs: calls made with `wait: true` are more reliable hitting
`cs-ai-03:8031` directly (tailnet-only) instead of through sim.avada.net, to
avoid proxy timeouts on slow generations. kb-test defaults to sim.avada.net
(no Tailscale needed) — only switch to the tailnet host if you see frequent
timeouts and already have Tailscale set up.
"""
import json
import os
import sys
import urllib.error
import urllib.request
import uuid

ENV_PATH = os.path.expanduser("~/CSL/.env")

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
                elif line.startswith("SIM_API_TOKEN="):
                    token = line.split("=", 1)[1].strip()
    except FileNotFoundError:
        sys.exit(f"ERROR: {ENV_PATH} not found")
    base = base or "https://sim.avada.net"
    if not token:
        sys.exit(
            "ERROR: SIM_API_TOKEN missing in ~/CSL/.env — ask Quảng (Fennic, Slack "
            "U01N91HCC3F) for a sim gateway API token (needs console.chat permission)."
        )
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


def ensure_sim_up(base, token):
    """Hosted sim gateway — no local process to start. Just check auth/
    reachability. Tries /api/sim/version first (docs say it reports the
    running code version — useful to confirm a sim-xxx branch deploy landed
    before trusting a test result), but that route 404s on the current
    deploy (confirmed 2026-09-04) so fall back to /api/sim/sessions, which
    is live, to prove the token + endpoint both work."""
    try:
        out = _req("GET", f"{base}/api/sim/version", token, timeout=10)
        print(f"sim gateway version: {json.dumps(out)}", file=sys.stderr)
        return
    except Exception:
        pass
    try:
        _req("GET", f"{base}/api/sim/sessions", token, timeout=10)
    except Exception as e:
        sys.exit(f"ERROR: sim gateway not reachable at {base}: {e}")


def new_session_id(app):
    return f"sim_kbtest_{app}_{uuid.uuid4().hex[:10]}"


def create_session(base, token, session_id, profile):
    body = {"sessionId": session_id, **profile}
    return _req("POST", f"{base}/api/sim/session", token, body)


def send_message(base, token, session_id, text, as_="customer", wait=True, timeout_ms=120000):
    body = {"sessionId": session_id, "text": text, "as": as_, "wait": wait, "timeoutMs": timeout_ms}
    return _req("POST", f"{base}/api/sim/message", token, body, timeout=timeout_ms / 1000 + 5)


def last_reply_text(result):
    """Pull the final bot text reply out of an /api/sim/message result."""
    replies = result.get("replies") or []
    if not replies:
        return ""
    return replies[-1]["content"]
