"""Step 2: After Claude writes /tmp/csdaily/classified.json (list of objects with
id, app, domain, cust, issue, topic, cs_nick, quality, quality_note, needs_followup),
this script:
  - filters spam/bot-only sessions
  - queries plan tier for follow-up shops (Admin API)
  - builds review-detect batches for the kept sessions
Output:
  /tmp/csdaily/enriched.json      — classified + plan/paid/shopname
  /tmp/csdaily/rv_batch_{i}.json  — review-detect batches
"""
import os, json, urllib.parse
from common import load_env, api_get, short_plan

OUT = "/tmp/csdaily"
N_RV_BATCH = 6
APPKEY = {"Joy": "joy", "Chatty": "chatty"}


def is_noise(x):
    note = (x.get("quality_note") or "").lower()
    return x["cs_nick"] == "?" and any(
        k in note for k in ("spam", "marketing", "no merchant support", "no cs reply"))


def main():
    env = load_env()
    cls = json.load(open(f"{OUT}/classified.json"))
    cls = [x for x in cls if not is_noise(x)]

    # plan only for follow-up shops
    cache = {}
    for x in cls:
        x["plan"] = "?"; x["paid"] = False; x["shopname"] = x.get("cust")
        if not x["needs_followup"] or not x["domain"]:
            continue
        dom = x["domain"]
        if dom not in cache:
            ss = dom.split(".myshopify")[0]
            try:
                cache[dom] = api_get(env, f"/shops/search?searchString={urllib.parse.quote(ss)}&searchAll=true").get("shops", [])
            except Exception:
                cache[dom] = []
        shops = cache[dom]
        want = APPKEY.get(x["app"])
        match = [sh for sh in shops if sh.get("appName") == want and sh.get("shopifyDomain") == dom] \
            or [sh for sh in shops if sh.get("shopifyDomain") == dom]
        if match:
            plan = match[0].get("plan")
            x["shopname"] = match[0].get("name") or x.get("cust")
            if plan:
                x["plan"] = plan
                x["paid"] = ("free" not in str(plan).lower())

    json.dump(cls, open(f"{OUT}/enriched.json", "w"), ensure_ascii=False)

    # review-detect batches: use full transcript from sessions_raw
    raw = {r["session_id"][-12:]: r for r in json.load(open(f"{OUT}/sessions_raw.json"))}
    keep = {x["id"] for x in cls}
    meta = {x["id"]: x for x in cls}
    slim = []
    for sid in keep:
        r = raw.get(sid)
        if not r:
            continue
        m = r["msgs"]
        if len(m) > 30:
            m = m[:8] + ["...(cắt giữa)..."] + m[-18:]
        c = meta[sid]
        slim.append({"id": sid, "app": r["app"],
                     "domain": (r["domain"] or "").replace("https://", "").replace("http://", ""),
                     "cust": r["cust"], "cs_nick": c["cs_nick"], "t": m})
    batches = [[] for _ in range(N_RV_BATCH)]
    for i, x in enumerate(slim):
        batches[i % N_RV_BATCH].append(x)
    for i, b in enumerate(batches):
        json.dump(b, open(f"{OUT}/rv_batch_{i}.json", "w"), ensure_ascii=False)

    print(json.dumps({"kept": len(cls), "followup": sum(1 for x in cls if x['needs_followup']),
                      "paid_followup": sum(1 for x in cls if x.get('paid') and x['needs_followup']),
                      "n_rv_batch": N_RV_BATCH}, ensure_ascii=False))


if __name__ == "__main__":
    main()
