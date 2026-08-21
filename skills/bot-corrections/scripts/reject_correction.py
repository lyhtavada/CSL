#!/usr/bin/env python3
"""
reject_correction.py — mark a bot correction as REJECTED when triage finds
the CS's correction was itself wrong / unnecessary (bot's original_response
was actually fine). This is NOT "verify" — verify means the bot's reply was
confirmed correct as a QA action on the reply itself; reject means the
correction row itself was a bad edit and should stop counting as an open bot
error / stop being treated as training signal.

⚠️ UNCONFIRMED CONTRACT: the /api/corrections/{id} write route has not been
confirmed against the live cs2 API (only GET is documented/tested as of
2026-08-21). The row schema exposes `status` ("draft" seen so far),
`reviewed_by`, `verified_by`, `verified_at` — strongly suggesting a
PUT /api/corrections/{id} with a status-style body is the right shape, but
this is a best guess for the status value itself too ("rejected"). Defaults
to --dry-run (prints the payload, sends nothing). Pass --live to actually
PUT. On the FIRST live run, check the result against the cs2.avada.net
dashboard by hand before trusting this unattended in cron.

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
    body = {"status": "rejected", "reviewed_by": "betty", "reviewed_note": args.reason}

    if not args.live:
        print("DRY-RUN — would PUT", f"{base}/api/corrections/{args.id}")
        print(json.dumps(body, indent=2, ensure_ascii=False))
        print("REJECT_ACTION=dry_run")
        return

    req = urllib.request.Request(
        f"{base}/api/corrections/{args.id}",
        data=json.dumps(body).encode(),
        method="PUT",
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
