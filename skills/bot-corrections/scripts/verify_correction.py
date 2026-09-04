#!/usr/bin/env python3
"""
verify_correction.py — mark a bot correction as VERIFIED when triage confirms
the CS's correction was accurate (bot's original_response was wrong, CS's
corrected_response is the right answer). This is the counterpart to
reject_correction.py: verify = the correction itself is good training signal
(bot was wrong, human fix is right) — used after branch (a) system-bug ticket
filed, or (b) KB patch drafted, whenever the correction that triggered it was
itself confirmed correct during trace. Do NOT call this for branch (c)
(CS was wrong) — use reject_correction.py there instead.

⚠️ UNCONFIRMED CONTRACT: same caveat as reject_correction.py — the
PUT /api/corrections/{id} write route has not been confirmed against the
live cs2 API (only GET is documented/tested as of 2026-08-21). Row schema
exposes `status` ("draft" seen so far), `reviewed_by`, `verified_by`,
`verified_at` — best guess is a PUT with a status-style body, "verified" as
the status value is also a guess. Defaults to --dry-run (prints the payload,
sends nothing). Pass --live to actually PUT. On the FIRST live run, check the
result against the cs2.avada.net dashboard by hand before trusting this
unattended in cron.

Usage:
  python3 verify_correction.py --id 1655 --reason "Traced session, CS's fix matches KB / correct answer" [--live]
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
    ap.add_argument("--reason", required=True, help="why the CS correction was confirmed accurate")
    ap.add_argument("--live", action="store_true", help="actually PUT (default: dry-run print only)")
    args = ap.parse_args()

    base, token = load_creds()
    body = {"status": "verified", "reviewed_by": "betty", "reviewed_note": args.reason}

    if not args.live:
        print("DRY-RUN — would PUT", f"{base}/api/corrections/{args.id}")
        print(json.dumps(body, indent=2, ensure_ascii=False))
        print("VERIFY_ACTION=dry_run")
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
        print("VERIFY_ACTION=live_ok")
    except urllib.error.HTTPError as e:
        print(f"VERIFY_ACTION=live_failed HTTP {e.code}: {e.read().decode()[:500]}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
