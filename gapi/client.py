"""Authed Google API clients for the account authorized via auth_setup.py.

    from gapi.client import calendar, sheets

Smoke test — prints the authed account and its calendars:
    .venv-crisp/bin/python gapi/client.py
"""
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

HERE = Path(__file__).parent
TOKEN = HERE / "token.json"

# Single source of truth — auth_setup.py imports this list.
# Read + write on Calendar, Sheets, and full Drive (search/read/edit any file
# in the account's Drive, not just files this app created — upgraded from
# drive.file 2026-08-28 so Liz can hand over a file name instead of a link/ID).
# Changing this list requires rerunning auth_setup.py to re-consent.
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/forms.body",
]


def _creds():
    if not TOKEN.exists():
        raise SystemExit(f"No {TOKEN} — run: .venv-crisp/bin/python gapi/auth_setup.py")

    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds.valid:
        return creds

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOKEN.write_text(creds.to_json())
        return creds

    raise SystemExit("Token invalid/revoked — rerun: .venv-crisp/bin/python gapi/auth_setup.py")


def calendar():
    return build("calendar", "v3", credentials=_creds(), cache_discovery=False)


def sheets():
    return build("sheets", "v4", credentials=_creds(), cache_discovery=False)


def drive():
    return build("drive", "v3", credentials=_creds(), cache_discovery=False)


def forms():
    return build("forms", "v1", credentials=_creds(), cache_discovery=False)


if __name__ == "__main__":
    cals = calendar().calendarList().list(maxResults=50).execute().get("items", [])

    # The primary calendar's id is the account's own email address.
    primary = next((c for c in cals if c.get("primary")), None)
    print(f"Authed as: {primary['id'] if primary else 'unknown'}")

    for c in cals:
        print(f"  calendar: {c['summary']}  [{c['id']}]")
