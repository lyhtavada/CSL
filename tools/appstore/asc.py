"""App Store Connect API client — read customer reviews + post replies.

Auth: Liz's Individual API Key (role Customer Support). Individual keys sign the
JWT with `sub: "user"` and no `iss` (Team Keys use an Issuer ID instead).
Key file lives in .secrets/ (gitignored) — never commit it.

Usage (.venv-crisp/bin/python tools/appstore/asc.py ...):
  apps                                  list apps the key can see
  reviews <app_id> [--limit N]          newest reviews (with existing reply, if any)
  reply <review_id> "<text>"            create/replace the developer response
"""
import argparse
import json
import sys
import time
from pathlib import Path

import jwt
import requests

ROOT = Path(__file__).resolve().parents[2]
KEY_ID = "XP8I9FYCXB1L"
KEY_PATH = ROOT / ".secrets" / f"ApiKey_{KEY_ID}.p8"
BASE = "https://api.appstoreconnect.apple.com/v1"


def _token():
    now = int(time.time())
    payload = {"sub": "user", "iat": now, "exp": now + 15 * 60, "aud": "appstoreconnect-v1"}
    return jwt.encode(payload, KEY_PATH.read_text(), algorithm="ES256",
                      headers={"kid": KEY_ID, "typ": "JWT"})


def _req(method, path, **kw):
    r = requests.request(method, f"{BASE}{path}",
                         headers={"Authorization": f"Bearer {_token()}"}, timeout=30, **kw)
    if r.status_code >= 400:
        sys.exit(f"HTTP {r.status_code}: {r.text}")
    return r.json() if r.content else {}


def apps():
    data = _req("GET", "/apps", params={"fields[apps]": "name,bundleId", "limit": 200})
    return [{"id": a["id"], **a["attributes"]} for a in data["data"]]


def reviews(app_id, limit=20):
    data = _req("GET", f"/apps/{app_id}/customerReviews", params={
        "sort": "-createdDate", "limit": limit, "include": "response",
    })
    responses = {i["id"]: i["attributes"] for i in data.get("included", [])
                 if i["type"] == "customerReviewResponses"}
    out = []
    for rv in data["data"]:
        rel = (rv.get("relationships", {}).get("response", {}) or {}).get("data")
        out.append({"id": rv["id"], **rv["attributes"],
                    "response": responses.get(rel["id"]) if rel else None})
    return out


def reply(review_id, text):
    body = {"data": {
        "type": "customerReviewResponses",
        "attributes": {"responseBody": text},
        "relationships": {"review": {"data": {"type": "customerReviews", "id": review_id}}},
    }}
    return _req("POST", "/customerReviewResponses", json=body)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("apps")
    r = sub.add_parser("reviews"); r.add_argument("app_id"); r.add_argument("--limit", type=int, default=20)
    y = sub.add_parser("reply"); y.add_argument("review_id"); y.add_argument("text")
    a = p.parse_args()
    if a.cmd == "apps":
        res = apps()
    elif a.cmd == "reviews":
        res = reviews(a.app_id, a.limit)
    else:
        res = reply(a.review_id, a.text)
    print(json.dumps(res, indent=2, ensure_ascii=False))
