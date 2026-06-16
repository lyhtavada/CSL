#!/usr/bin/env python3
"""
kb_set.py — push ONE KB file straight to CS v2 + reindex. No payload file.

Reads the full new file content from stdin, POSTs it to /api/kb/file
(auto git commit), then reindexes the agent.

Usage:
  python3 kb_set.py <app> <path>            < newcontent.md
  cat new.md | python3 kb_set.py chatty kb/faq/settings.md
  python3 kb_set.py <app> <path> --no-reindex

apps: chatty (chatty-agent), joy (joy-loyalty-agent), or a raw agent id.
Safe to re-run: same path+content overwrites.
"""
import json
import sys

import kb_api


def main():
    args = [a for a in sys.argv[1:] if a != "--no-reindex"]
    do_reindex = "--no-reindex" not in sys.argv[1:]
    if len(args) != 2:
        sys.exit("usage: kb_set.py <app> <path> [--no-reindex]   (content on stdin)")
    app, path = args
    agent = kb_api.agent_id(app)

    content = sys.stdin.read()
    if not content.strip():
        sys.exit("ERROR: empty content on stdin")

    base, token = kb_api.load_creds()
    print(f"POST {path}  -> {agent} @ {base}")
    r = kb_api.put_file(base, token, agent, path, content)
    ok = isinstance(r, dict) and r.get("ok")
    print(f"  {'OK ' if ok else 'FAIL'} {json.dumps(r)}")
    if not ok:
        sys.exit(1)

    if do_reindex:
        print(f"Reindexing {agent} ...")
        r = kb_api.reindex(base, token, agent)
        print(f"  {json.dumps(r)}")
        if isinstance(r, dict) and r.get("partial"):
            print("  WARNING: partial reindex — some chunks failed.")
    print("Done.")


if __name__ == "__main__":
    main()
