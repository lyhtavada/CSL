"""Authed Google API clients for the account authorized via auth_setup.py.

    from gapi.client import calendar, sheets, drive

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
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
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


if __name__ == "__main__":
    who = drive().about().get(fields="user").execute()["user"]
    print(f"Authed as: {who.get('emailAddress')}")

    for c in calendar().calendarList().list(maxResults=20).execute().get("items", []):
        print(f"  calendar: {c['summary']}  [{c['id']}]")
