#!/usr/bin/env python3
"""One-time OAuth setup: log in as the target Google account, save a refresh token.

Run:  .venv-crisp/bin/python gapi/auth_setup.py

Opens a browser. Log in with the account whose Calendar/Sheets/Drive should be
accessible — this is NOT necessarily the account that owns the Cloud project.
Writes gapi/token.json; after that, scripts import gapi/client.py instead.
"""
import sys
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

HERE = Path(__file__).parent
CREDENTIALS = HERE / "credentials.json"
TOKEN = HERE / "token.json"

sys.path.insert(0, str(HERE))
from client import SCOPES  # noqa: E402


def main():
    if not CREDENTIALS.exists():
        raise SystemExit(
            f"Missing {CREDENTIALS}\n"
            "Download the OAuth 'Desktop app' client JSON from Cloud Console "
            "(APIs & Services > Clients) and save it to that path."
        )

    flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS), SCOPES)
    # prompt=consent + access_type=offline so Google re-issues a refresh token
    # even if this account has authorized the app before.
    creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")

    TOKEN.write_text(creds.to_json())
    TOKEN.chmod(0o600)
    print(f"Saved {TOKEN}")

    if not creds.refresh_token:
        print(
            "WARNING: no refresh_token returned — access will die in ~1 hour.\n"
            "Revoke this app at myaccount.google.com/permissions, then rerun."
        )


if __name__ == "__main__":
    main()
