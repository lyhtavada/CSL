"""Google Play Developer API client — read reviews + post replies.

Auth: service account betty-play-reviews@lizs-502610.iam.gserviceaccount.com
(GCP project "Liz's agent"), invited into Play Console with "Reply to reviews".
Key file lives in .secrets/ (gitignored) — never commit it.

⚠️ reviews.list only returns reviews with text created/modified in the LAST 7 DAYS.

Usage (.venv-crisp/bin/python -W ignore tools/appstore/play.py ...):
  reviews <package_name> [--limit N]    recent reviews (with existing reply, if any)
  reply <package_name> <review_id> "<text>"
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

ROOT = Path(__file__).resolve().parents[2]
KEY_PATH = ROOT / ".secrets" / "play-service-account.json"
SCOPES = ["https://www.googleapis.com/auth/androidpublisher"]


def _svc():
    creds = service_account.Credentials.from_service_account_file(str(KEY_PATH), scopes=SCOPES)
    return build("androidpublisher", "v3", credentials=creds, cache_discovery=False).reviews()


def _ts(t):
    return datetime.fromtimestamp(int(t["seconds"]), timezone.utc).isoformat() if t else None


def reviews(package, limit=50):
    res = _svc().list(packageName=package, maxResults=limit).execute()
    out = []
    for rv in res.get("reviews", []):
        comments = rv.get("comments", [])
        user = next((c["userComment"] for c in comments if "userComment" in c), {})
        dev = next((c["developerComment"] for c in comments if "developerComment" in c), None)
        out.append({
            "id": rv["reviewId"],
            "author": rv.get("authorName"),
            "rating": user.get("starRating"),
            "text": (user.get("text") or "").strip(),
            "lastModified": _ts(user.get("lastModified")),
            "language": user.get("reviewerLanguage"),
            "device": user.get("device"),
            "appVersion": user.get("appVersionName"),
            "reply": {"text": dev["text"], "lastModified": _ts(dev.get("lastModified"))} if dev else None,
        })
    return out


def reply(package, review_id, text):
    # Play limit: 350 characters per reply.
    if len(text) > 350:
        raise SystemExit(f"Reply is {len(text)} chars — Google Play max is 350.")
    return _svc().reply(packageName=package, reviewId=review_id, body={"replyText": text}).execute()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("reviews"); r.add_argument("package"); r.add_argument("--limit", type=int, default=50)
    y = sub.add_parser("reply"); y.add_argument("package"); y.add_argument("review_id"); y.add_argument("text")
    a = p.parse_args()
    res = reviews(a.package, a.limit) if a.cmd == "reviews" else reply(a.package, a.review_id, a.text)
    print(json.dumps(res, indent=2, ensure_ascii=False))
