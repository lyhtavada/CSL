#!/usr/bin/env python3
"""
notion_fetch.py — dump a Notion page (or several) to a readable text file
with every block's ID inline, so Claude can read the trainee's answers and
later pick exact anchor IDs to append review callouts after.

Does the mechanical I/O only — no grading, no judgment. That happens when
Claude reads the output per SKILL.md.

Handles the two shapes seen in trainee test pages:
  - A plain page with numbered-question + free-text-paragraph answers
    (e.g. "Week 2 Overview", "Week 2 ICP").
  - A page whose body embeds a child_database (e.g. "Week 2: Joy Loyalty
    App Learning" -> "Kế hoạch chi tiết" DB, one row per day/topic) — each
    row is itself a page with its own Q&A tables. These are auto-expanded
    one level deep (rows are not recursed into their own child_databases).

table_row content lives in `cells`, not `rich_text` — this tripped up a
manual first pass once, so it's handled explicitly here.

Usage:
  python3 notion_fetch.py <notion-url-or-page-id> [<url-or-id> ...]

Output:
  Writes one .txt file per top-level page (plus one per child_database row)
  to /tmp/grade-joy-trainee/<page-id-short>.txt, and prints the manifest
  (file path + page title) so Claude knows what to Read next.
"""
import os
import re
import sys
import json
import urllib.request

ENV_PATH = os.path.expanduser("~/CSL/.env")
OUT_DIR = "/tmp/grade-joy-trainee"
API = "https://api.notion.com/v1"


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
HEADERS = {"Authorization": f"Bearer {KEY}", "Notion-Version": "2022-06-28"}


def req(path):
    r = urllib.request.Request(f"{API}{path}", headers=HEADERS)
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read())


def req_post(path, body):
    data = json.dumps(body).encode()
    r = urllib.request.Request(f"{API}{path}", data=data, headers={**HEADERS, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read())


def extract_page_id(arg):
    # Notion URLs look like .../Some-Title-Words-<32hexid>?v=<32hexview>...
    # The title itself can contain hex-looking letters (a-f), so naive
    # "last 32 hex chars in the string" is unreliable — e.g. "...Profile-
    # b90b0da4..." can false-match starting inside "Profile". Instead: take
    # the last '/'-segment, split it on '-', and the id is the last token
    # (Notion always hyphen-joins the id onto the slug with no internal
    # hyphens in the id itself), before any '?' query string.
    path = arg.split("?", 1)[0]
    last_segment = path.rstrip("/").rsplit("/", 1)[-1]
    candidate = last_segment.rsplit("-", 1)[-1]
    if re.fullmatch(r"[0-9a-fA-F]{32}", candidate):
        return candidate.lower()
    # fallback: bare id passed directly (with or without dashes)
    bare = arg.replace("-", "")
    if re.fullmatch(r"[0-9a-fA-F]{32}", bare):
        return bare.lower()
    raise ValueError(f"Can't find a page id in: {arg}")


def get_children(block_id):
    out = []
    cursor = None
    while True:
        path = f"/blocks/{block_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        data = req(path)
        out.extend(data["results"])
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return out


def rich_text_plain(rt_list):
    return "".join(t.get("plain_text", "") for t in rt_list)


def page_title(page_id):
    data = req(f"/pages/{page_id}")
    title_prop = next((p for p in data.get("properties", {}).values() if p.get("type") == "title"), None)
    if title_prop:
        return rich_text_plain(title_prop["title"]) or page_id
    return page_id


def dump_blocks(block_id, depth=0, out=None, max_depth=12):
    if out is None:
        out = []
    for b in get_children(block_id):
        btype = b["type"]
        bid = b["id"]
        indent = "  " * depth
        content = b.get(btype, {})

        if btype == "table_row":
            cells = content.get("cells", [])
            cell_texts = [rich_text_plain(c) for c in cells]
            out.append(f"{indent}{bid} | [row] " + " || ".join(cell_texts))
            continue

        if btype == "child_database":
            out.append(f"{indent}{bid} | [child_database]")
            continue  # handled separately by caller (needs its own dump section)

        if btype == "child_page":
            out.append(f"{indent}{bid} | [child_page] {content.get('title', '')}")
            continue  # not auto-expanded — only child_database rows are

        text = rich_text_plain(content.get("rich_text", [])) if "rich_text" in content else ""
        if btype == "to_do":
            checked = content.get("checked", False)
            out.append(f"{indent}{bid} | [to_do:{'x' if checked else ' '}] {text}")
        else:
            out.append(f"{indent}{bid} | [{btype}] {text}")

        if b.get("has_children") and depth < max_depth:
            dump_blocks(bid, depth + 1, out, max_depth)

    return out


def find_child_databases(block_id):
    """Top-level only — matches how the Week-2-Learning page is structured."""
    dbs = []
    for b in get_children(block_id):
        if b["type"] == "child_database":
            dbs.append(b["id"])
    return dbs


def query_database(db_id):
    data = req_post(f"/databases/{db_id}/query", {"page_size": 100})
    rows = data["results"]
    while data.get("has_more"):
        data = req_post(f"/databases/{db_id}/query", {"page_size": 100, "start_cursor": data["next_cursor"]})
        rows.extend(data["results"])
    return rows


def slug(page_id, title):
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "-", title.strip())[:60].strip("-")
    return f"{page_id[:8]}_{safe}" if safe else page_id[:8]


def dump_page(page_id, manifest):
    title = page_title(page_id)
    lines = dump_blocks(page_id)
    fname = os.path.join(OUT_DIR, slug(page_id, title) + ".txt")
    with open(fname, "w") as f:
        f.write(f"# {title}\n# page_id={page_id}\n\n" + "\n".join(lines))
    manifest.append((fname, title, page_id))

    # auto-expand any top-level child_database rows (one level deep)
    for db_id in find_child_databases(page_id):
        for row in query_database(db_id):
            dump_page(row["id"], manifest)


def main():
    if len(sys.argv) < 2:
        print("Usage: notion_fetch.py <notion-url-or-page-id> [...]", file=sys.stderr)
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)
    manifest = []
    for arg in sys.argv[1:]:
        page_id = extract_page_id(arg)
        dump_page(page_id, manifest)

    print(f"Wrote {len(manifest)} file(s) to {OUT_DIR}/:\n")
    for fname, title, page_id in manifest:
        print(f"  {fname}\n    title: {title}\n    page_id: {page_id}\n")


if __name__ == "__main__":
    main()
