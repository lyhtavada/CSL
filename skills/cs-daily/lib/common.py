"""Shared helpers for /cs-daily report: BigQuery + Admin API + roster."""
import os, json, datetime as dt, urllib.request, urllib.parse, warnings
warnings.filterwarnings("ignore")

ROOT = os.path.expanduser("~/CSL")

def load_env():
    """Minimal .env loader (no external deps)."""
    env = {}
    with open(os.path.join(ROOT, ".env")) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            v = v.strip()
            if v and v[0] in "\"'" and v[-1] == v[0]:
                v = v[1:-1]
            env[k.strip()] = v
    return env

# ---- CS Team G2 roster: email -> nickname, nickname -> display name ----
EMAIL2NICK = {
    "hanghm@avadagroup.com": "HangHM", "vanct@avadagroup.com": "VanCT",
    "lypk@avadagroup.com": "LyPK", "phuongnt01@avadagroup.com": "PhuongNT",
    "phuongnt@avadagroup.com": "PhuongNT", "huytc@avadagroup.com": "HuyTC",
    "anhln.ctv@avadagroup.com": "AnhLN", "minhbt.ctv@avadagroup.com": "MinhBT",
    "anhbd@avadagroup.com": "AnhBD", "hienpt@avadagroup.com": "HienPT",
    "trangnth.ctv@avadagroup.com": "TrangNTH", "thaoltt.ctv@avadagroup.com": "ThaoLTT",
    "chauhm@avadagroup.com": "ChauHM", "phuongttm.ctv@avadagroup.com": "PhuongTTM",
    "linhtlk@avadagroup.com": "LinhTLK", "lyht@avada.io": "LyHT",
}
NICK2NAME = {
    "HangHM": "Hana", "VanCT": "Audrey", "LyPK": "Alyssa", "PhuongNT": "Jade",
    "HuyTC": "Sonny", "AnhLN": "Alicia", "MinhBT": "Mirra", "AnhBD": "Andy",
    "HienPT": "Hazel", "TrangNTH": "Megan", "ThaoLTT": "Rosie", "ChauHM": "Cody",
    "PhuongTTM": "Phoebe", "LinhTLK": "Linda", "LyHT": "Liz",
}
TEAM = set(NICK2NAME.keys())

# ---- time window: 9:00 (yesterday) -> 9:00 (today) VN time ----
VN = dt.timezone(dt.timedelta(hours=7))

def window(now=None):
    """Return (start_vn, end_vn) = yesterday 9:00 -> today 9:00 VN.
    Pass now (a tz-aware datetime) explicitly; defaults to current time."""
    if now is None:
        now = dt.datetime.now(VN)
    end = now.replace(hour=9, minute=0, second=0, microsecond=0)
    start = end - dt.timedelta(days=1)
    return start, end

def to_utc_str(d):
    return d.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

def parse_iso(t):
    return dt.datetime.fromisoformat(t.replace("Z", "+00:00"))

# ---- Admin API ----
def api_get(env, path):
    base = env["AVD_API_BASE"]; tok = env["AVD_TOKEN"]
    req = urllib.request.Request(f"{base}{path}", headers={"Authorization": f"Bearer {tok}"})
    return json.load(urllib.request.urlopen(req, timeout=30))

# ---- BigQuery client ----
def bq_client(env):
    from google.cloud import bigquery
    from google.oauth2 import service_account
    key = env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n")
    info = {"type": "service_account", "project_id": "avada-crm",
            "private_key_id": env["BQ_SA_PRIVATE_KEY_ID"], "private_key": key,
            "client_email": env["BQ_SA_CLIENT_EMAIL"], "token_uri": "https://oauth2.googleapis.com/token"}
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/bigquery",
                      "https://www.googleapis.com/auth/cloud-platform"])
    return bigquery.Client(credentials=creds, project="avada-crm")

def short_plan(p):
    if not p or p == "?":
        return "free"
    p = str(p).lower()
    for k, v in [("enterprise", "Enterprise"), ("advanced", "Advanced"),
                 ("plus", "Plus"), ("pro", "Pro"), ("basic", "Basic"), ("free", "free")]:
        if k in p:
            return v
    return p
