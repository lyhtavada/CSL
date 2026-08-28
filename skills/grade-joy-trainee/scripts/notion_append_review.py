#!/usr/bin/env python3
"""
notion_append_review.py — append CSL-review callout blocks into a graded
Notion page, right after the table/answer block they refer to.

Mechanical only — the review items (which anchor, what text, what verdict
color) are decided by Claude reading the trainee's answers, per SKILL.md.
Only run this AFTER Liz has approved the review shown in chat.

Input: a JSON file, a list of objects:
  {
    "page_id": "...",     // the page the anchor block lives on
    "anchor_id": "...",   // block id to insert the callout right after
    "text": "...",        // callout body (may contain \n for line breaks)
    "verdict": "ok" | "warn" | "unanswered" | "note"
  }

`verdict` maps to icon/color so Claude doesn't have to pick emoji/hex by hand:
  ok         -> ✅ blue_background      (đúng)
  warn       -> ⚠️ yellow_background    (có lỗi / cần sửa / cần verify)
  unanswered -> ❌ red_background       (chưa trả lời)
  note       -> 📝 gray_background      (ghi chú chung, không phải chấm điểm)

Usage:
  python3 notion_append_review.py review.json
"""
import os
import sys
import json
import time
import urllib.request

ENV_PATH = os.path.expanduser("~/CSL/.env")
API = "https://api.notion.com/v1"

VERDICT_STYLE = {
    "ok": ("✅", "blue_background"),
    "warn": ("⚠️", "yellow_background"),
    "unanswered": ("❌", "red_background"),
    "note": ("📝", "gray_background"),
}


def load_key():
    try:
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("NOTION_API_KEY="):
                    return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    print("ERROR: NOTION_API_KEY not found in ~/CSL/.env", file=sys.stderr)
    sys.exit(1)


KEY = load_key()
HEADERS = {"Authorization": f"Bearer {KEY}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}


def patch(page_id, body):
    data = json.dumps(body).encode()
    r = urllib.request.Request(f"{API}/blocks/{page_id}/children", data=data, headers=HEADERS, method="PATCH")
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()}


def append_callout(page_id, anchor_id, text, verdict):
    icon, color = VERDICT_STYLE[verdict]
    if not text.startswith("CSL Review"):
        text = "CSL Review (Liz):\n" + text
    body = {
        "children": [{
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [{"type": "text", "text": {"content": text}}],
                "icon": {"type": "emoji", "emoji": icon},
                "color": color,
            },
        }],
        "after": anchor_id,
    }
    status, resp = patch(page_id, body)
    return status == 200, status, resp


def main():
    if len(sys.argv) != 2:
        print("Usage: notion_append_review.py review.json", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1]) as f:
        items = json.load(f)

    fails = []
    for item in items:
        ok, status, resp = append_callout(item["page_id"], item["anchor_id"], item["text"], item["verdict"])
        tag = "OK  " if ok else "FAIL"
        print(f"{tag} {item['page_id'][:8]} anchor={item['anchor_id'][:8]} status={status}")
        if not ok:
            print(f"     {json.dumps(resp)[:300]}")
            fails.append(item)
        time.sleep(0.35)

    print(f"\nDone. {len(items) - len(fails)}/{len(items)} succeeded.")
    if fails:
        print("Failed items:")
        for it in fails:
            print(f"  page={it['page_id']} anchor={it['anchor_id']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
