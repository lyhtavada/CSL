"""Upload a file to notes.avada.net and print the share URL.

Usage: python3 upload.py path/to/file.md [--ext md|html]
Strips YAML frontmatter (--- ... ---) from .md files before upload, since
that's Claude Code file metadata, not content meant to be shared.
"""
import argparse
import json
import os
import re
import sys
import urllib.request

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


def strip_frontmatter(text):
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--ext", choices=["md", "html"], default=None)
    args = ap.parse_args()

    ext = args.ext or ("html" if args.path.endswith(".html") else "md")
    with open(args.path, encoding="utf-8") as f:
        content = f.read()
    if ext == "md":
        content = strip_frontmatter(content)

    env = load_env()
    key = env["NOTES_API_KEY"]

    req = urllib.request.Request(
        f"https://notes.avada.net/api/upload?ext={ext}",
        data=content.encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "text/plain",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)

    print(data["url"])


if __name__ == "__main__":
    main()
