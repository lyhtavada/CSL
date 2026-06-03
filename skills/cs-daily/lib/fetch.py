"""Step 1: Pull Crisp transcripts (Joy+Chatty) for the 24h window, split into
classify batches. Output:
  /tmp/csdaily/sessions_raw.json  — full transcripts + meta (for review-detect)
  /tmp/csdaily/cls_batch_{i}.json — slim transcripts for issue/quality classify
  /tmp/csdaily/window.json        — window meta for the renderer

Usage: python3 fetch.py [YYYY-MM-DD]   (date = the END day at 9:00; default today VN)
"""
import os, sys, json, datetime as dt
from common import load_env, bq_client, window, to_utc_str, VN

OUT = "/tmp/csdaily"
os.makedirs(OUT, exist_ok=True)
N_BATCH = 7

def main():
    env = load_env()
    if len(sys.argv) > 1:
        d = dt.datetime.strptime(sys.argv[1], "%Y-%m-%d").replace(tzinfo=VN)
        now = d.replace(hour=9)
    else:
        now = dt.datetime.now(VN)
    start, end = window(now)
    us, ue = to_utc_str(start), to_utc_str(end)

    client = bq_client(env)
    # Joy = app_joy ; Chatty = app_chatty OR app_faqs
    q = f"""
    WITH target AS (
      SELECT session_id,
        CASE WHEN ANY_VALUE(segments) LIKE '%app_joy%' THEN 'Joy'
             WHEN ANY_VALUE(segments) LIKE '%app_chatty%' OR ANY_VALUE(segments) LIKE '%app_faqs%' THEN 'Chatty' END app,
        ANY_VALUE(segments) seg, ANY_VALUE(shopifyDomain) domain, ANY_VALUE(customerNickname) cust
      FROM `avada-crm.avada_cs.crisp_chats`
      WHERE timestamp >= TIMESTAMP('{us}') AND timestamp < TIMESTAMP('{ue}')
      GROUP BY session_id HAVING app IS NOT NULL
    )
    SELECT c.session_id, t.app, t.seg, t.domain, t.cust,
           c.timestamp, c.fromType, c.content, c.agentEmail
    FROM `avada-crm.avada_cs.crisp_chats` c JOIN target t USING(session_id)
    WHERE c.type='text' ORDER BY c.session_id, c.timestamp
    """
    sessions = {}
    for r in client.query(q):
        s = sessions.setdefault(r.session_id, {
            "app": r.app, "seg": r.seg, "domain": r.domain, "cust": r.cust,
            "agents": set(), "msgs": []})
        who = "MERCHANT" if r.fromType == "user" else ("AGENT" if r.fromType == "operator" else (r.fromType or "?").upper())
        if r.agentEmail:
            s["agents"].add(r.agentEmail)
        txt = (r.content or "").strip().replace("\n", " ")
        if txt:
            s["msgs"].append(f"[{who}] {txt[:400]}")

    raw = []
    for sid, d in sessions.items():
        d["agents"] = sorted(d["agents"])
        raw.append({"session_id": sid, **d})
    json.dump(raw, open(f"{OUT}/sessions_raw.json", "w"), ensure_ascii=False)

    # slim for classify (cap long transcripts)
    slim = []
    for x in raw:
        m = x["msgs"]
        if len(m) > 24:
            m = m[:6] + ["...(cắt giữa)..."] + m[-14:]
        slim.append({"id": x["session_id"][-12:], "app": x["app"],
                     "domain": (x["domain"] or "").replace("https://", "").replace("http://", ""),
                     "cust": x["cust"], "agents": x["agents"], "t": m})
    batches = [[] for _ in range(N_BATCH)]
    for i, x in enumerate(slim):
        batches[i % N_BATCH].append(x)
    for i, b in enumerate(batches):
        json.dump(b, open(f"{OUT}/cls_batch_{i}.json", "w"), ensure_ascii=False)

    json.dump({
        "start_vn": start.strftime("%d/%m/%Y %H:%M"),
        "end_vn": end.strftime("%d/%m/%Y %H:%M"),
        "start_date": start.strftime("%Y-%m-%d"),
        "end_date": end.strftime("%Y-%m-%d"),
        "n_batch": N_BATCH,
        "total": len(raw),
        "joy": sum(1 for x in raw if x["app"] == "Joy"),
        "chatty": sum(1 for x in raw if x["app"] == "Chatty"),
    }, open(f"{OUT}/window.json", "w"))

    print(json.dumps({"total": len(raw), "joy": sum(1 for x in raw if x['app']=='Joy'),
                      "chatty": sum(1 for x in raw if x['app']=='Chatty'),
                      "n_batch": N_BATCH, "out": OUT}, ensure_ascii=False))

if __name__ == "__main__":
    main()
