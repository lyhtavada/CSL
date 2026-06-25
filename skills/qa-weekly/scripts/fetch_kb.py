#!/usr/bin/env python3
"""
fetch_kb.py — pull a live KB file for a QA knowledge check, straight from the
CS v2 KB API (cs2.avada.net) — the SAME KB Joyce/Ivy run on. Replaces reading
the old claw-webhook repo files.

Usage:
  python3 fetch_kb.py <app> <path>     # app = chatty|joy ; path = kb/faq/pricing.md
  python3 fetch_kb.py <app> --list     # list all KB paths for that agent

Reuses the kb-sync client (kb_api.py) so creds/agent-ids stay in one place.
"""
import os
import sys

# reuse the kb-sync thin client
sys.path.insert(0, os.path.expanduser("~/CSL/skills/kb-sync/scripts"))
import kb_api  # noqa: E402


def main():
    if len(sys.argv) < 3:
        sys.exit("usage: fetch_kb.py <chatty|joy> <kb/path.md | --list>")
    app, arg = sys.argv[1], sys.argv[2]
    base, token = kb_api.load_creds()
    agent = kb_api.agent_id(app)

    if arg == "--list":
        for f in kb_api.list_files(base, token, agent):
            print(f)
        return

    content = kb_api.get_file(base, token, agent, arg)
    if content is None:
        sys.exit(f"ERROR: KB file not found: agent={agent} path={arg}")
    sys.stdout.write(content)


if __name__ == "__main__":
    main()
