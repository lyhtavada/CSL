"""Authed Gmail API client for the account authorized via gmail_auth_setup.py.

    from gapi.gmail_client import gmail

Smoke test — prints the authed account and unread count:
    .venv-crisp/bin/python gapi/gmail_client.py
"""
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

HERE = Path(__file__).parent
TOKEN = HERE / "gmail_token.json"

# Single source of truth — gmail_auth_setup.py imports this list.
# gmail.modify covers read/send/reply/label/trash, but NOT permanent delete
# or changing account settings/filters — kept separate from the
# Calendar/Sheets token (client.py) so a scope change on one doesn't force
# re-consent on the other.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
]


def _creds():
    if not TOKEN.exists():
        raise SystemExit(f"No {TOKEN} — run: .venv-crisp/bin/python gapi/gmail_auth_setup.py")

    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds.valid:
        return creds

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOKEN.write_text(creds.to_json())
        return creds

    raise SystemExit("Token invalid/revoked — rerun: .venv-crisp/bin/python gapi/gmail_auth_setup.py")


def gmail():
    return build("gmail", "v1", credentials=_creds(), cache_discovery=False)


if __name__ == "__main__":
    svc = gmail()
    profile = svc.users().getProfile(userId="me").execute()
    print(f"Authed as: {profile['emailAddress']}")
    print(f"Total messages: {profile['messagesTotal']}")
