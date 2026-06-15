#!/usr/bin/env python3
"""
push_kb.py — push reviewed KB patches to CS v2, then reindex.

Input: a payloads JSON file = array of {agent, path, content} objects
(produced after the diff/review step). Each entry is POSTed to /api/kb/file
(auto git commit), then the agent is reindexed once at the end.

Usage:
  python3 push_kb.py <payloads.json>
  python3 push_kb.py <payloads.json> --no-reindex   # write only, reindex later

Safe to re-run: writes are idempotent (same path+content overwrites).
"""
import json
import sys

import kb_api


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: push_kb.py <payloads.json> [--no-reindex]")
    payloads_path = sys.argv[1]
    do_reindex = "--no-reindex" not in sys.argv[2:]

    base, token = kb_api.load_creds()
    ops = json.load(open(payloads_path))
    if not ops:
        sys.exit("no payloads to push")

    agents = sorted({o["agent"] for o in ops})
    print(f"Pushing {len(ops)} file(s) to {base} for agent(s): {', '.join(agents)}\n")

    failed = []
    for o in ops:
        r = kb_api.put_file(base, token, o["agent"], o["path"], o["content"])
        ok = isinstance(r, dict) and r.get("ok")
        print(f"  {'OK ' if ok else 'FAIL'} POST {o['path']}  -> {json.dumps(r)}")
        if not ok:
            failed.append(o["path"])

    if failed:
        print(f"\n{len(failed)} write(s) FAILED — NOT reindexing. Fix and re-run:")
        for p in failed:
            print(f"  - {p}")
        sys.exit(1)

    if do_reindex:
        for agent in agents:
            print(f"\nReindexing {agent} ...")
            r = kb_api.reindex(base, token, agent)
            print(f"  {json.dumps(r)}")
            if isinstance(r, dict) and r.get("partial"):
                print("  WARNING: partial reindex — some chunks failed, check the agent.")
    else:
        print("\nSkipped reindex (--no-reindex). Run later: kb_api.py reindex <app>")

    print("\nDone.")


if __name__ == "__main__":
    main()
