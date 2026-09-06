#!/usr/bin/env python3
"""
fetch_store.py — gom mọi thứ Betty KHÔNG lấy được qua MCP về 1 store, phục vụ /store-research.

Chia việc rõ ràng:
  - MCP analytic (Betty tự gọi):  merchant_profile, merchant_cs_history, shop_profile,
    sale_deals_list/deal_get, merchant_transactions, storeleads_*
  - Script này:                   storefront config thật (app đang cài + config Joy/Chatty
    render ra trang), transcript Crisp đầy đủ (BigQuery), lịch call (Google Calendar)

Usage:
  fetch_store.py --shop keepers-collective-website.myshopify.com \
                 [--site thekeeperscollective.com] [--email jillian@...] \
                 [--days 180] [--out DIR]

Mỗi phần chạy độc lập: một phần lỗi vẫn in phần còn lại, và ghi rõ lý do lỗi.
Output: DIR/{storefront.json, joy_program.json, crisp.md, calendar.json} + digest ra stdout.
"""
import argparse, json, os, re, sys, traceback
import urllib.request, urllib.error

sys.path.insert(0, "/Users/avada/CSL")
ENV_PATH = "/Users/avada/CSL/.env"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def section(t):
    print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)


# ---------------------------------------------------------------- storefront
def http_get(url, timeout=30):
    r = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        return resp.geturl(), resp.read().decode("utf-8", "replace")


# Nhận diện app qua script src / global. Cố ý giữ danh sách ngắn: chỉ những app
# ảnh hưởng tới câu chuyện loyalty/CS. App lạ vẫn được liệt kê ở "other_vendors".
APP_SIGNS = {
    "Joy Loyalty (Avada)": [r"avada-joy\.js", r"joy-loyalty-program"],
    "Chatty (Avada)":      [r"avada-chatty", r"chatty-widget", r"cdn\.chatty\.net"],
    "Avada (khác)":        [r"avada", r"avadaio"],
    "Klaviyo":             [r"klaviyo"],
    "Awtomic":             [r"awtomic"],
    "Recharge":            [r"rechargeapps|recharge-"],
    "Yotpo":               [r"yotpo"],
    "Okendo":              [r"okendo"],
    "Judge.me":            [r"judge\.me|judgeme"],
    "Loox":                [r"loox\.io"],
    "Smile.io":            [r"smile\.io"],
    "LoyaltyLion":         [r"loyaltylion"],
    "Stamped":             [r"stamped\.io"],
    "Gorgias":             [r"gorgias"],
    "Tidio":               [r"tidio"],
    "Moast":               [r"moast\.io"],
    "Attentive":           [r"attentive"],
    "Postscript":          [r"postscript"],
}


def json_blobs_near(html, needle, min_len=1500, max_back=25000):
    """Notion/Shopify nhúng config app dạng JSON literal trong <script>. Tìm ngược từ
    `needle` về dấu { gần nhất decode được — cách duy nhất ổn định vì không có
    biến/anchor cố định giữa các theme."""
    dec = json.JSONDecoder()
    out = []
    for m in re.finditer(needle, html):
        i = m.start()
        for back in range(0, max_back):
            p = i - back
            if p < 0:
                break
            if html[p] != "{":
                continue
            try:
                obj, end = dec.raw_decode(html[p:])
            except Exception:
                continue
            if end >= min_len:
                out.append((p, obj))
                break
    # khử trùng lặp theo vị trí
    seen, uniq = set(), []
    for p, o in out:
        if p in seen:
            continue
        seen.add(p)
        uniq.append(o)
    return uniq


def joy_summary(cfg, prog):
    """Quy đổi config thô thành mấy con số Liz cần trên call: %hoàn, tier bật chưa,
    có referral chưa. Không phán quyết — chỉ tính."""
    s = {}
    if cfg:
        s["plan"] = cfg.get("plan")
        s["currency"] = cfg.get("currency")
        s["tier_program_enabled"] = cfg.get("enableTierProgram")
        s["referral_v2"] = cfg.get("useReferralV2")
        s["widget_v3"] = cfg.get("useWidgetV3")
        s["installed_at"] = cfg.get("latestInstalledDate")
        s["timezone"] = cfg.get("timezoneSelected")
    if not prog:
        return s
    earn, spend, tiers = prog.get("earning") or [], prog.get("spending") or [], prog.get("tiers") or []
    s["earning"] = [{
        "title": r.get("title"), "event": r.get("event"),
        "points": r.get("earnPoint"), "per_money": r.get("rateMoney"),
        "status": r.get("status"), "draft": r.get("isDraft"),
        "limit": f"{r.get('usageLimit')}/{r.get('limitInterval') or ''}{r.get('limitUnit')}",
        "start": r.get("startDate"),
    } for r in earn]
    s["spending"] = [{
        "title": r.get("title"), "spend_point": r.get("spendPoint"),
        "get_amount": r.get("earnAmount"), "redeem_type": r.get("redeemType"),
        "min_order": r.get("orderReqAmount") if r.get("orderReq") not in (None, "none") else None,
        "status": r.get("status"),
    } for r in spend]
    s["tiers"] = [{
        "name": r.get("name"), "target_point": r.get("targetPoint"),
        "target_point_update": r.get("targetPointUpdate"),
        "deleted": r.get("isDeleted"), "perks": r.get("contentPerk"),
    } for r in tiers]

    # $/point + % hoàn: chỉ tính khi cả 2 vế có số, tránh bịa tỉ lệ
    vals = [(float(r["spendPoint"]), float(r["earnAmount"]))
            for r in spend if str(r.get("spendPoint") or "").strip() not in ("", "None")
            and str(r.get("earnAmount") or "").strip() not in ("", "None")]
    if vals:
        s["money_per_point"] = sorted({round(a / p, 4) for p, a in vals if p})
    order_rule = next((r for r in earn if r.get("event") == "place_order"), None)
    if order_rule and s.get("money_per_point"):
        try:
            pts_per_dollar = float(order_rule["earnPoint"]) / float(order_rule["rateMoney"])
            s["cashback_pct"] = sorted({round(pts_per_dollar * mpp * 100, 2) for mpp in s["money_per_point"]})
        except Exception:
            pass
    # điểm kiếm được mà KHÔNG cần mua hàng — nguồn rò rỉ discount hay bị bỏ sót
    nonpurchase = [r for r in earn
                   if r.get("event") not in ("place_order", "place_order_subscription")
                   and r.get("status") and not r.get("isDraft")]
    try:
        s["free_points_stackable"] = sum(float(r.get("earnPoint") or 0) for r in nonpurchase)
        if s.get("money_per_point"):
            s["free_points_worth"] = round(s["free_points_stackable"] * max(s["money_per_point"]), 2)
    except Exception:
        pass
    s["has_referral_program"] = bool(prog.get("referral") or prog.get("referralProgram"))
    return s


def do_storefront(shop, site, outdir):
    section("STOREFRONT")
    url = f"https://{site or shop}"
    final, html = http_get(url)
    print(f"fetched {url} -> {final} ({len(html):,} bytes)")
    res = {"requested": url, "final_url": final, "bytes": len(html)}

    low = html.lower()
    res["apps_detected"] = sorted({name for name, pats in APP_SIGNS.items()
                                   if any(re.search(p, low) for p in pats)})
    print("apps:", ", ".join(res["apps_detected"]) or "(none matched)")

    # config chung của Joy (khối có useWidgetV3)
    cfg = next(iter(json_blobs_near(html, r'"useWidgetV3"', min_len=300)), None)
    # khối program: earning/spending/tiers
    prog = None
    for b in json_blobs_near(html, r'"(place_order|amount_discount)"', min_len=2000):
        if isinstance(b, dict) and {"earning", "spending"} & set(b):
            prog = b
            break
    if cfg or prog:
        res["joy"] = joy_summary(cfg, prog)
        json.dump({"config": cfg, "program": prog},
                  open(os.path.join(outdir, "joy_program.json"), "w"), indent=1)
        print("joy config: OK ->", os.path.join(outdir, "joy_program.json"))
        print(json.dumps(res["joy"], indent=1, ensure_ascii=False)[:4000])
    else:
        print("joy config: không tìm thấy trên storefront (app chưa cài, widget tắt, "
              "hoặc theme render kiểu khác)")

    # Chatty chưa có schema config ổn định trên storefront → chỉ soi dấu vết, không đoán
    chatty_hits = sorted(set(re.findall(r"[\w./-]*(?:chatty|avada-chat)[\w./-]*", low)))[:20]
    if chatty_hits:
        res["chatty_traces"] = chatty_hits
        print("chatty traces:", chatty_hits)

    res["other_vendors"] = sorted(set(re.findall(r"cdn\.shopify\.com/extensions/[\w-]+/([\w-]+)/", html)))[:40]
    print("shopify app extensions:", res["other_vendors"])

    json.dump(res, open(os.path.join(outdir, "storefront.json"), "w"), indent=1)
    return res


# -------------------------------------------------------------------- crisp
def do_crisp(shop, email, days, outdir):
    section("CRISP (BigQuery)")
    from dotenv import dotenv_values
    from google.oauth2 import service_account
    from google.cloud import bigquery

    env = dotenv_values(ENV_PATH)
    creds = service_account.Credentials.from_service_account_info({
        "type": "service_account", "project_id": "avada-crm",
        "private_key_id": env["BQ_SA_PRIVATE_KEY_ID"],
        "private_key": env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n"),
        "client_email": env["BQ_SA_CLIENT_EMAIL"],
        "token_uri": "https://oauth2.googleapis.com/token",
    }, scopes=["https://www.googleapis.com/auth/bigquery",
               "https://www.googleapis.com/auth/cloud-platform"])
    client = bigquery.Client(project="avada-crm", credentials=creds)

    # shopifyDomain là cột chuẩn; email là fallback cho session mở trước khi domain
    # được gắn vào conversation.
    sql = """
    SELECT timestamp, session_id, website_id, segments, fromType, origin, content,
           agentEmail, customerEmail, customerNickname, shopifyDomain
    FROM `avada-crm.avada_cs.crisp_chats`
    WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL @days DAY)
      AND ( shopifyDomain = @shop
            OR (@email != '' AND customerEmail = @email) )
    ORDER BY timestamp ASC
    """
    job = client.query(sql, job_config=bigquery.QueryJobConfig(query_parameters=[
        bigquery.ScalarQueryParameter("shop", "STRING", shop),
        bigquery.ScalarQueryParameter("email", "STRING", email or ""),
        bigquery.ScalarQueryParameter("days", "INT64", days),
    ]))
    rows = list(job.result())
    print(f"{len(rows)} messages, {len({r['session_id'] for r in rows})} sessions "
          f"(last {days}d)")

    path = os.path.join(outdir, "crisp.md")
    with open(path, "w", encoding="utf-8") as f:
        cur = None
        for r in rows:
            if r["session_id"] != cur:
                cur = r["session_id"]
                f.write(f"\n\n## session {cur}  ({r['segments']})\n"
                        f"https://app.crisp.chat/website/{r['website_id']}/inbox/{cur}/\n\n")
            who = r["agentEmail"] or r["customerNickname"] or r["fromType"]
            f.write(f"[{r['timestamp']:%Y-%m-%d %H:%M}] {r['fromType']}/{who}: {r['content']}\n\n")
    print("->", path)
    for sid in dict.fromkeys(r["session_id"] for r in rows):
        sess = [r for r in rows if r["session_id"] == sid]
        print(f"  {sess[0]['timestamp']:%Y-%m-%d} → {sess[-1]['timestamp']:%Y-%m-%d}  "
              f"{len(sess):3d} msg  {sid}")
    return path


# ----------------------------------------------------------------- calendar
def do_calendar(shop, site, email, outdir):
    section("GOOGLE CALENDAR")
    import datetime
    from gapi.client import calendar
    svc = calendar()
    now = datetime.datetime.utcnow()
    ev = svc.events().list(
        calendarId="primary",
        timeMin=(now - datetime.timedelta(days=90)).isoformat() + "Z",
        timeMax=(now + datetime.timedelta(days=90)).isoformat() + "Z",
        singleEvents=True, orderBy="startTime", maxResults=2500,
    ).execute()

    # khớp theo email trước (chắc chắn), rồi tới token tên miền (bắt các lịch do
    # sale đặt, tiêu đề chỉ có tên brand)
    tokens = {t for t in re.split(r"[.\-]", (site or shop).split(".")[0]) if len(t) > 3}
    hits = []
    for e in ev.get("items", []):
        emails = [a.get("email", "") for a in e.get("attendees", [])]
        blob = " ".join([e.get("summary", ""), e.get("description", "") or ""] + emails).lower()
        if (email and email.lower() in blob) or any(t in blob for t in tokens):
            hits.append({
                "start": e["start"].get("dateTime") or e["start"].get("date"),
                "summary": e.get("summary"), "status": e.get("status"),
                "organizer": (e.get("organizer") or {}).get("email"),
                "attendees": [(a.get("email"), a.get("responseStatus")) for a in e.get("attendees", [])],
                "meet": e.get("hangoutLink"),
                "description": e.get("description"),
            })
    print(f"{len(hits)} matching events (±90d)  tokens={sorted(tokens)}")
    for h in hits:
        print(f"  {h['start']}  {h['summary']}  [{', '.join(f'{a}={s}' for a, s in h['attendees'])}]")
    json.dump(hits, open(os.path.join(outdir, "calendar.json"), "w"), indent=1)
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shop", required=True, help="myshopify domain, vd x.myshopify.com")
    ap.add_argument("--site", help="domain công khai, vd thekeeperscollective.com")
    ap.add_argument("--email", help="email merchant (để bắt thêm session Crisp + lịch)")
    ap.add_argument("--days", type=int, default=180, help="cửa sổ Crisp, mặc định 180")
    ap.add_argument("--out", default=None, help="thư mục output")
    a = ap.parse_args()

    outdir = a.out or f"/tmp/store-research/{a.shop.split('.')[0]}"
    os.makedirs(outdir, exist_ok=True)
    print("OUT:", outdir)

    for label, fn in [("storefront", lambda: do_storefront(a.shop, a.site, outdir)),
                      ("crisp",      lambda: do_crisp(a.shop, a.email, a.days, outdir)),
                      ("calendar",   lambda: do_calendar(a.shop, a.site, a.email, outdir))]:
        try:
            fn()
        except Exception:
            section(f"{label.upper()} — LỖI")
            traceback.print_exc()
            print(f"\n>>> Phần {label} thất bại. Các phần khác vẫn chạy; đừng ghi lên "
                  f"Notion là 'không có dữ liệu' — ghi là 'không lấy được'.")


if __name__ == "__main__":
    main()
