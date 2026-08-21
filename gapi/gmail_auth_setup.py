#!/usr/bin/env python3
"""One-time OAuth setup: log in as the target Google account, save a Gmail refresh token.

Run:  .venv-crisp/bin/python gapi/gmail_auth_setup.py

Opens a browser. Log in with the account whose Gmail should be accessible.
Writes gapi/gmail_token.json; after that, scripts import gapi/gmail_client.py.
"""
import sys
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

HERE = Path(__file__).parent
CREDENTIALS = HERE / "credentials.json"
TOKEN = HERE / "gmail_token.json"

sys.path.insert(0, str(HERE))
from gmail_client import SCOPES  # noqa: E402


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
