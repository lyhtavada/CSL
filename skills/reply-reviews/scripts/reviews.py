#!/usr/bin/env python3
"""Pending-review queue for App Store (iOS) + Google Play (Android).

Store clients live in tools/appstore/{asc,play}.py. State: state/drafts.json
(keyed by short numeric id so Liz can approve from Telegram: "post 1,3").

Run with .venv-crisp/bin/python -W ignore:

  reviews.py fetch [--out FILE]        unreplied reviews not yet drafted/skipped (JSON)
  reviews.py save <drafts.json>        add drafts: [{review_id, store, app, reply, flag?}, ...]
  reviews.py list                      drafts still pending approval
  reviews.py edit <id> "<text>"        replace a draft's reply text
  reviews.py post <id,id,...> [--live] post drafts (dry-run unless --live)
  reviews.py skip <id,id,...>          mark as not replying

A review drops out of `fetch` once it has a reply in the store, or is in
drafts.json with any status (pending / posted / skipped). Android API only
returns reviews from the last 7 days — a pending Android draft older than that
can still be posted (reply endpoint doesn't have the 7-day limit).
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "appstore"))
import asc  # noqa: E402
import play  # noqa: E402

CONFIG = json.loads((SKILL / "config.json").read_text())
STATE = SKILL / "state" / "drafts.json"
PLAY_MAX = 350


def _load():
    return json.loads(STATE.read_text()) if STATE.exists() else {"next_id": 1, "drafts": {}}


def _save(state):
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def fetch():
    state = _load()
    known = {d["review_id"] for d in state["drafts"].values()}
    ignore = {n.lower() for n in CONFIG["ignore_reviewers"]}
    out = []
    for app, cfg in CONFIG["apps"].items():
        if cfg.get("ios_app_id"):
            for r in asc.reviews(cfg["ios_app_id"], limit=200):
                if r["response"] or r["id"] in known or (r["reviewerNickname"] or "").lower() in ignore:
                    continue
                out.append({"review_id": r["id"], "store": "ios", "app": app, "rating": r["rating"],
                            "author": r["reviewerNickname"], "title": r["title"], "text": r["body"],
                            "date": r["createdDate"], "territory": r["territory"]})
        if cfg.get("android_package"):
            for r in play.reviews(cfg["android_package"], limit=100):
                if r["reply"] or r["id"] in known or (r["author"] or "").lower() in ignore:
                    continue
                out.append({"review_id": r["id"], "store": "android", "app": app, "rating": r["rating"],
                            "author": r["author"], "title": None, "text": r["text"],
                            "date": r["lastModified"], "language": r["language"],
                            "appVersion": r["appVersion"]})
    return out


def save(path):
    state = _load()
    known = {d["review_id"] for d in state["drafts"].values()}
    added = []
    for d in json.loads(Path(path).read_text()):
        if d["review_id"] in known:
            continue
        if d["store"] == "android" and len(d["reply"]) > PLAY_MAX:
            sys.exit(f"Draft for {d['review_id']} is {len(d['reply'])} chars — Google Play max {PLAY_MAX}.")
        did = str(state["next_id"])
        state["next_id"] += 1
        state["drafts"][did] = {**d, "status": "pending", "drafted_at": _now()}
        added.append(did)
    _save(state)
    return {"added": added}


def pending():
    return {k: v for k, v in _load()["drafts"].items() if v["status"] == "pending"}


def edit(did, text):
    state = _load()
    d = state["drafts"][did]
    if d["store"] == "android" and len(text) > PLAY_MAX:
        sys.exit(f"{len(text)} chars — Google Play max {PLAY_MAX}.")
    d["reply"] = text
    d["edited_at"] = _now()
    _save(state)
    return d


def post(ids, live):
    state = _load()
    results = []
    for did in ids:
        d = state["drafts"].get(did)
        if not d or d["status"] != "pending":
            results.append({"id": did, "ok": False, "error": "not a pending draft"})
            continue
        if not live:
            results.append({"id": did, "dry_run": True, "store": d["store"], "reply": d["reply"]})
            continue
        cfg = CONFIG["apps"][d["app"]]
        try:
            if d["store"] == "ios":
                asc.reply(d["review_id"], d["reply"])
            else:
                play.reply(cfg["android_package"], d["review_id"], d["reply"])
            d["status"], d["posted_at"] = "posted", _now()
            results.append({"id": did, "ok": True, "store": d["store"]})
        except (Exception, SystemExit) as e:  # asc._req exits on HTTP error
            results.append({"id": did, "ok": False, "error": str(e)})
        _save(state)
    return results


def skip(ids):
    state = _load()
    for did in ids:
        if did in state["drafts"]:
            state["drafts"][did]["status"], state["drafts"][did]["skipped_at"] = "skipped", _now()
    _save(state)
    return {"skipped": ids}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch"); f.add_argument("--out")
    s = sub.add_parser("save"); s.add_argument("file")
    sub.add_parser("list")
    e = sub.add_parser("edit"); e.add_argument("id"); e.add_argument("text")
    po = sub.add_parser("post"); po.add_argument("ids"); po.add_argument("--live", action="store_true")
    sk = sub.add_parser("skip"); sk.add_argument("ids")
    a = p.parse_args()

    if a.cmd == "fetch":
        res = fetch()
        if a.out:
            Path(a.out).write_text(json.dumps(res, indent=2, ensure_ascii=False))
        print(json.dumps(res, indent=2, ensure_ascii=False))
        print(f"TOTAL_NEW={len(res)}")
    elif a.cmd == "save":
        print(json.dumps(save(a.file)))
    elif a.cmd == "list":
        print(json.dumps(pending(), indent=2, ensure_ascii=False))
    elif a.cmd == "edit":
        print(json.dumps(edit(a.id, a.text), indent=2, ensure_ascii=False))
    elif a.cmd == "post":
        print(json.dumps(post(a.ids.split(","), a.live), indent=2, ensure_ascii=False))
    else:
        print(json.dumps(skip(a.ids.split(","))))
