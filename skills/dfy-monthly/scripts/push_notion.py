#!/usr/bin/env python3
"""
Push a CS-weekly report (Markdown) to Notion as a NEW sub-page under a parent page.

Usage:
  python3 push_notion.py --parent <PARENT_PAGE_ID> --title "Chatty CS Weekly — W23" --md /tmp/chatty_w23.md

Auth: NOTION_API_KEY from CSL/.env. The Notion integration must be shared with the
parent page (Share → Add connections) or the API returns 404.

Markdown supported (enough for the CS-weekly template):
  # / ## / ###            → heading_1 / heading_2 / heading_3
  - item / * item         → bulleted_list_item
  1. item                 → numbered_list_item
  > quote                 → quote
  ---                     → divider
  | table |               → table
  blank / paragraph       → paragraph
  **bold**, _italic_, `code`, [text](url)  → inline rich text

Prints the new page URL on success.
"""
import os, re, sys, json, argparse
import requests
from dotenv import load_dotenv

NOTION_VERSION = "2022-06-28"
API = "https://api.notion.com/v1"


def H():
    key = os.environ["NOTION_API_KEY"]
    return {
        "Authorization": f"Bearer {key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


# ---- inline markdown → Notion rich_text ----
INLINE_RE = re.compile(
    r"(\*\*.+?\*\*|__.+?__|`.+?`|\[.+?\]\(.+?\)|_.+?_|\*.+?\*)"
)


def rich_text(text):
    if not text:
        return []
    out = []
    for tok in INLINE_RE.split(text):
        if not tok:
            continue
        ann = {}
        link = None
        content = tok
        m = re.match(r"\[(.+?)\]\((.+?)\)$", tok)
        if m:
            content, link = m.group(1), m.group(2)
        elif tok.startswith("**") and tok.endswith("**"):
            ann["bold"] = True
            content = tok[2:-2]
        elif tok.startswith("__") and tok.endswith("__"):
            ann["bold"] = True
            content = tok[2:-2]
        elif tok.startswith("`") and tok.endswith("`"):
            ann["code"] = True
            content = tok[1:-1]
        elif tok.startswith("_") and tok.endswith("_"):
            ann["italic"] = True
            content = tok[1:-1]
        elif tok.startswith("*") and tok.endswith("*"):
            ann["italic"] = True
            content = tok[1:-1]
        rt = {"type": "text", "text": {"content": content}}
        if link:
            rt["text"]["link"] = {"url": link}
        if ann:
            rt["annotations"] = ann
        out.append(rt)
    # Notion caps rich_text content at 2000 chars per item — safe for our short lines.
    return out


def table_block(rows):
    width = max(len(r) for r in rows)
    children = []
    for r in rows:
        cells = [rich_text(c.strip()) for c in r] + [[]] * (width - len(r))
        children.append({"type": "table_row", "table_row": {"cells": cells}})
    return {
        "type": "table",
        "table": {
            "table_width": width,
            "has_column_header": True,
            "has_row_header": False,
            "children": children,
        },
    }


def md_to_blocks(md):
    blocks = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        # table: a run of | ... | lines (skip the |---| separator row)
        if s.startswith("|") and s.endswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c for c in lines[i].strip().strip("|").split("|")]
                if not re.match(r"^[\s:|-]+$", lines[i].strip().strip("|")):  # skip separator
                    rows.append(cells)
                i += 1
            if rows:
                blocks.append(table_block(rows))
            continue
        i += 1
        if not s:
            continue
        if s.startswith("### "):
            blocks.append({"type": "heading_3", "heading_3": {"rich_text": rich_text(s[4:])}})
        elif s.startswith("## "):
            blocks.append({"type": "heading_2", "heading_2": {"rich_text": rich_text(s[3:])}})
        elif s.startswith("# "):
            blocks.append({"type": "heading_1", "heading_1": {"rich_text": rich_text(s[2:])}})
        elif s == "---":
            blocks.append({"type": "divider", "divider": {}})
        elif s.startswith("> "):
            blocks.append({"type": "quote", "quote": {"rich_text": rich_text(s[2:])}})
        elif re.match(r"^\d+\.\s", s):
            blocks.append({"type": "numbered_list_item",
                           "numbered_list_item": {"rich_text": rich_text(re.sub(r'^\d+\.\s', '', s))}})
        elif s.startswith("- ") or s.startswith("* "):
            blocks.append({"type": "bulleted_list_item",
                           "bulleted_list_item": {"rich_text": rich_text(s[2:])}})
        else:
            blocks.append({"type": "paragraph", "paragraph": {"rich_text": rich_text(s)}})
    return blocks


def create_page(parent_id, title, blocks):
    # Notion caps children at 100 per request → create with first 100, append the rest.
    # position page_start → new sub-page lands at the TOP of the parent (newest first,
    # so the report list doesn't grow downward over time).
    payload = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "children": blocks[:100],
        "position": {"type": "page_start"},
    }
    r = requests.post(f"{API}/pages", headers=H(), data=json.dumps(payload))
    if r.status_code != 200:
        print("ERROR creating page:", r.status_code, r.text[:400], file=sys.stderr)
        sys.exit(1)
    page = r.json()
    pid = page["id"]
    for j in range(100, len(blocks), 100):
        a = requests.patch(f"{API}/blocks/{pid}/children", headers=H(),
                           data=json.dumps({"children": blocks[j:j + 100]}))
        if a.status_code != 200:
            print("WARN append:", a.status_code, a.text[:300], file=sys.stderr)
    return page.get("url", pid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", required=True, help="Parent Notion page ID")
    ap.add_argument("--title", required=True, help="Sub-page title")
    ap.add_argument("--md", required=True, help="Path to the markdown report")
    a = ap.parse_args()

    load_dotenv("/Users/avada/CSL/.env")
    with open(a.md, encoding="utf-8") as f:
        md = f.read()
    blocks = md_to_blocks(md)
    url = create_page(a.parent, a.title, blocks)
    print(f"Created Notion sub-page: {url}")


if __name__ == "__main__":
    main()
