import urllib.request, json, base64, time, datetime, csv, sys, os
from dotenv import dotenv_values

_env = dotenv_values(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
API_KEY = _env["CRISP_API_KEY"]
API_SECRET = _env["CRISP_API_SECRET"]
WEBSITE_ID = _env["CRISP_WEBSITE_RETENTION"]
TZ = datetime.timezone(datetime.timedelta(hours=7))
cutoff = datetime.datetime.now(tz=TZ) - datetime.timedelta(days=30)

auth = base64.b64encode(f"{API_KEY}:{API_SECRET}".encode()).decode()
headers = {
    "Authorization": f"Basic {auth}",
    "X-Crisp-Tier": "plugin"
}

def api_get(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

# Step 1: Scan all pages
print("=== STEP 1: Scanning all pages ===", flush=True)
sessions = []
total_app_joy = 0
page = 1

while True:
    url = f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversations/{page}"
    try:
        result = api_get(url)
        data = result.get("data", [])
    except Exception as e:
        print(f"  ERROR page {page}: {e}", flush=True)
        break

    if not data:
        print(f"  Page {page}: empty — stopping", flush=True)
        break

    page_joy = 0
    page_recent = 0
    for s in data:
        segs = s.get("meta", {}).get("segments", [])
        if "app_joy" not in segs:
            continue
        total_app_joy += 1
        page_joy += 1
        created_ms = s.get("created_at", 0)
        dt = datetime.datetime.fromtimestamp(created_ms / 1000, tz=TZ)
        if dt >= cutoff:
            page_recent += 1
            sessions.append({
                "session_id": s["session_id"],
                "created_at": dt,
                "nickname": s.get("meta", {}).get("nickname", ""),
                "email": s.get("meta", {}).get("email", ""),
            })

    print(f"  Page {page}: {len(data)} convos, {page_joy} app_joy, {page_recent} recent", flush=True)
    page += 1
    time.sleep(0.1)

total_pages = page - 1
print(f"\nTotal pages scanned: {total_pages}", flush=True)
print(f"Total app_joy sessions (all time): {total_app_joy}", flush=True)
print(f"Sessions within 30 days: {len(sessions)}", flush=True)

# Step 2: Fetch messages for each session
print("\n=== STEP 2: Fetching messages ===", flush=True)
rows = []
success = 0
fail = 0

for i, s in enumerate(sessions):
    sid = s["session_id"]
    url = f"https://api.crisp.chat/v1/website/{WEBSITE_ID}/conversation/{sid}/messages"
    try:
        result = api_get(url)
        msgs = result.get("data", [])
        lines = []
        for m in msgs:
            content = m.get("content", "")
            if not isinstance(content, str):
                continue
            content = content.strip()
            if not content:
                continue
            from_val = m.get("from", "")
            nick = m.get("user", {}).get("nickname", "")
            if from_val == "operator":
                label = f"[CS: {nick}]" if nick else "[CS]"
            else:
                label = "[User]"
            lines.append(f"{label} {content}")
        transcript = "\n".join(lines)
        rows.append({
            "Session ID": sid,
            "Date": s["created_at"].strftime("%Y-%m-%d %H:%M:%S"),
            "Merchant Name": s["nickname"],
            "Merchant Email": s["email"],
            "Transcript": transcript,
        })
        success += 1
        if (i + 1) % 10 == 0:
            print(f"  Fetched {i+1}/{len(sessions)}...", flush=True)
    except Exception as e:
        print(f"  ERROR {sid}: {e}", flush=True)
        fail += 1
    time.sleep(0.15)

# Step 3: Export CSV
out_path = "/Users/avada/CSL/reports/crisp-joy-transcripts.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["Session ID", "Date", "Merchant Name", "Merchant Email", "Transcript"],
        quoting=csv.QUOTE_ALL
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"\n=== DONE ===", flush=True)
print(f"Pages scanned:            {total_pages}", flush=True)
print(f"Total app_joy (all time): {total_app_joy}", flush=True)
print(f"Sessions in 30 days:      {len(sessions)}", flush=True)
print(f"Exported successfully:    {success}", flush=True)
print(f"Failed:                   {fail}", flush=True)
print(f"File: {out_path}", flush=True)
