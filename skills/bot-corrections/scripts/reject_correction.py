#!/usr/bin/env python3
"""
reject_correction.py — mark a bot correction as REJECTED when triage finds
the CS's correction was itself wrong / unnecessary (bot's original_response
was actually fine). This is NOT "verify" — verify means the bot's reply was
confirmed correct as a QA action on the reply itself; reject means the
correction row itself was a bad edit and should stop counting as an open bot
error / stop being treated as training signal.

Confirmed contract (from avada-cs-api-docs, 2026-09-04): POST
/api/corrections/{id}/reject — permission `training.corrections`. No body
required. (Counterpart: POST /api/corrections/{id}/approve exists too, not
used by this script — approve is a separate action from verify.)

Usage:
  python3 reject_correction.py --id 1655 --reason "CS correction was inaccurate; bot's original reply was correct" [--live]
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

ENV_PATH = os.path.expanduser("~/CSL/.env")


def load_creds():
    url = token = None
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("CS2_API_URL="):
                    url = line.split("=", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("CS2_API_TOKEN="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        sys.exit(f"ERROR: {ENV_PATH} not found")
    if not url or not token:
        sys.exit("ERROR: CS2_API_URL / CS2_API_TOKEN missing in ~/CSL/.env")
    return url.rstrip("/"), token


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True, help="correction id")
    ap.add_argument("--reason", required=True, help="why the CS correction was wrong / the original bot reply was fine")
    ap.add_argument("--live", action="store_true", help="actually PUT (default: dry-run print only)")
    args = ap.parse_args()

    base, token = load_creds()

    if not args.live:
        print("DRY-RUN — would POST", f"{base}/api/corrections/{args.id}/reject")
        print(f"(reason, not sent to API — for the bot-corrections report only: {args.reason})")
        print("REJECT_ACTION=dry_run")
        return

    req = urllib.request.Request(
        f"{base}/api/corrections/{args.id}/reject",
        data=b"",
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "bot-corrections/1.0",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(r.read().decode())
        print("REJECT_ACTION=live_ok")
    except urllib.error.HTTPError as e:
        print(f"REJECT_ACTION=live_failed HTTP {e.code}: {e.read().decode()[:500]}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
