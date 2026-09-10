"""Upload/update/delete a note on notes.avada.net.

Usage:
  python3 upload.py path/to/file.md [--ext md|html]
  python3 upload.py path/to/file.md --update <id-or-url>
  python3 upload.py --delete <id-or-url>

Strips YAML frontmatter (--- ... ---) from .md files before upload, since
that's Claude Code file metadata, not content meant to be shared.

Update/delete verified 2026-09-10 by probing the real API (no public docs
exist for these — /api-ref and /docs both 404 on notes.avada.net):
  - PUT /api/upload/{id}?ext=md|html — requires X-Notes-Git-Email,
    X-Notes-Hostname, X-Notes-Client, X-Notes-Client-Type (must be
    literally "cli", server 400s on any other value) headers.
  - DELETE /api/upload/{id} — only needs Authorization.
"""
import argparse
import json
import os
import re
import socket
import subprocess
import sys
import urllib.error
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


def extract_id(id_or_url):
    """Accept either a bare id or a full https://notes.avada.net/<id>.<ext> URL."""
    m = re.search(r"/([A-Za-z0-9]+)\.(md|html)(?:$|\?)", id_or_url)
    if m:
        return m.group(1), m.group(2)
    return id_or_url, None


def git_email():
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "config", "user.email"],
            capture_output=True, text=True, timeout=5,
        )
        email = out.stdout.strip()
        return email or "unknown@avada.io"
    except Exception:
        return "unknown@avada.io"


def notes_meta_headers():
    return {
        "X-Notes-Git-Email": git_email(),
        "X-Notes-Hostname": socket.gethostname(),
        "X-Notes-Client": "claude-code",
        "X-Notes-Client-Type": "cli",
    }


def request(method, url, key, data=None, extra_headers=None):
    headers = {"Authorization": f"Bearer {key}"}
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read()
            return resp.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", help="file to upload/update (omit with --delete)")
    ap.add_argument("--ext", choices=["md", "html"], default=None)
    ap.add_argument("--update", metavar="ID_OR_URL", help="update an existing note in place")
    ap.add_argument("--delete", metavar="ID_OR_URL", help="delete an existing note")
    args = ap.parse_args()

    env = load_env()
    key = env["NOTES_API_KEY"]

    if args.delete:
        note_id, _ = extract_id(args.delete)
        status, body = request(
            "DELETE", f"https://notes.avada.net/api/upload/{note_id}", key
        )
        if status not in (200, 204):
            print(f"error: delete failed ({status}): {body.decode('utf-8', 'replace')}", file=sys.stderr)
            sys.exit(6)
        print(f"deleted: {note_id}")
        return

    if not args.path:
        print("error: pass a file path, or use --delete <id-or-url>", file=sys.stderr)
        sys.exit(2)

    ext = args.ext
    with open(args.path, encoding="utf-8") as f:
        content = f.read()

    if args.update:
        note_id, url_ext = extract_id(args.update)
        ext = ext or url_ext or ("html" if args.path.endswith(".html") else "md")
        if ext == "md":
            content = strip_frontmatter(content)
        status, body = request(
            "PUT",
            f"https://notes.avada.net/api/upload/{note_id}?ext={ext}",
            key,
            data=content.encode("utf-8"),
            extra_headers={"Content-Type": "text/plain", **notes_meta_headers()},
        )
        if status not in (200, 204):
            print(f"error: update failed ({status}): {body.decode('utf-8', 'replace')}", file=sys.stderr)
            sys.exit(6)
        print(f"updated: https://notes.avada.net/{note_id}.{ext}")
        return

    ext = ext or ("html" if args.path.endswith(".html") else "md")
    if ext == "md":
        content = strip_frontmatter(content)

    status, body = request(
        "POST",
        f"https://notes.avada.net/api/upload?ext={ext}",
        key,
        data=content.encode("utf-8"),
        extra_headers={"Content-Type": "text/plain"},
    )
    if status not in (200, 201):
        print(f"error: upload failed ({status}): {body.decode('utf-8', 'replace')}", file=sys.stderr)
        sys.exit(6)
    data = json.loads(body)
    print(data["url"])


if __name__ == "__main__":
    main()
