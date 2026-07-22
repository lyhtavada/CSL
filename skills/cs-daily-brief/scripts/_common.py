"""Shared helpers for /cs-daily-brief: env loading, BigQuery client, Admin API,
Team G2 roster, and shift check-in/checkout status. Self-contained (not
imported from skills/cs-daily/lib — that skill was removed 2026-07-22; this
was copied out of it before deletion so /cs-daily-brief keeps working)."""
import os, json, datetime as dt, urllib.request, warnings
from collections import defaultdict
warnings.filterwarnings("ignore")

ROOT = os.path.expanduser("~/CSL")


def load_env():
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


# ---- CS Team G2 roster: email -> nickname ----
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

VN = dt.timezone(dt.timedelta(hours=7))


def to_utc_str(d):
    return d.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def parse_iso(t):
    return dt.datetime.fromisoformat(t.replace("Z", "+00:00"))


def api_get(env, path, retries=3):
    base = env["AVD_API_BASE"]; tok = env["AVD_TOKEN"]
    req = urllib.request.Request(f"{base}{path}", headers={"Authorization": f"Bearer {tok}"})
    last = None
    for attempt in range(retries):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception as e:  # transient SSL/network errors
            last = e
            import time
            time.sleep(1.5 * (attempt + 1))
    raise last


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


def shift_status(env, win_start, win_end, start_date, end_date):
    """Late (>5min) checkins, missed checkins, missed checkouts for Team G2
    shifts overlapping [win_start, win_end]."""
    late, miss_in, miss_out = [], [], []
    shifts = api_get(env, f"/shifts?start={start_date}&end={end_date}").get("data", [])
    for sh in shifts:
        st, en = parse_iso(sh["start"]), parse_iso(sh["end"])
        if en < win_start or st > win_end:
            continue
        g2 = [c for c in sh.get("cs", []) if "G2" in (c.get("groupLabel") or "")]
        if not g2:
            continue
        checks = api_get(env, f"/shifts/{sh['id']}/checks").get("data", [])
        bye = defaultdict(dict)
        for ch in checks:
            bye[ch["email"]][ch["type"]] = ch
        for c in g2:
            em = c["email"]; nick = EMAIL2NICK.get(em, c.get("name", "?"))
            ci = bye[em].get("checkin"); co = bye[em].get("checkout")
            t = sh["title"]
            if not ci:
                miss_in.append((nick, t))
            else:
                m = int((parse_iso(ci["createdAt"]) - st).total_seconds() / 60)
                if m > 5:
                    late.append((nick, t, m))
                if not co:
                    miss_out.append((nick, t))
    return late, miss_in, miss_out
