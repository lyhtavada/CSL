"""Create a secret on secret.avada.net and print the share URL.

Usage:
  python3 share_secret.py "<content>" [--label TEXT] [--mode public|private]
                           [--to email1,email2] [--expires 1h|6h|24h|3d|7d]
                           [--views N]
  python3 share_secret.py --file path/to/file --mode private --to a@avada.io

Reads content from the first positional arg, or from --file if given.
Auth token comes from SECRET_AVADA_TOKEN in ~/CSL/.env (never hardcode it here).
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

ROOT = os.path.expanduser("~/CSL")
API_BASE = "https://secret.avada.net"


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content", nargs="?", help="secret content (omit if using --file)")
    ap.add_argument("--file", help="read content from this file instead")
    ap.add_argument("--label", default=None, help="short label, 0-200 bytes")
    ap.add_argument("--mode", choices=["public", "private"], default="private")
    ap.add_argument("--to", help="comma-separated Avada emails, private mode only")
    ap.add_argument("--expires", default=None, choices=["1h", "6h", "24h", "3d", "7d"])
    ap.add_argument("--views", type=int, default=None, help="1-20")
    args = ap.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("error: pass content as an argument or use --file", file=sys.stderr)
        sys.exit(2)

    env = load_env()
    token = env.get("SECRET_AVADA_TOKEN")
    if not token:
        print(
            "error: SECRET_AVADA_TOKEN missing in ~/CSL/.env — "
            "get it once at https://my.avada.net/myaccount/secret-token",
            file=sys.stderr,
        )
        sys.exit(8)

    body = {"content": content, "mode": args.mode}
    if args.label:
        body["label"] = args.label
    if args.expires:
        body["expiresIn"] = args.expires
    if args.views:
        body["views"] = args.views
    if args.to:
        emails = [e.strip() for e in args.to.split(",") if e.strip()]
        if args.mode == "private":
            body["recipientEmails"] = emails
        else:
            print("warning: --to ignored in public mode", file=sys.stderr)

    req = urllib.request.Request(
        f"{API_BASE}/api/secrets",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        print(f"error: upload failed ({e.code}): {msg}", file=sys.stderr)
        sys.exit(6)

    print(data["url"])
    if "expiresAt" in data:
        print(f"expires: {data['expiresAt']}", file=sys.stderr)
    if "views" in data:
        print(f"views left: {data['views']}", file=sys.stderr)


if __name__ == "__main__":
    main()
