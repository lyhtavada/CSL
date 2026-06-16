#!/usr/bin/env python3
"""
prep.py — fetch all KB v2 files for an app into a local cache and locate the
latest mined-FAQ file. This does the mechanical I/O; the semantic diff
(classify each FAQ COVERED/OUTDATED/GAP/PARTIAL, draft patches) is done by
Claude reading these files per SKILL.md.

Usage:
  python3 prep.py <app> [--faq <path>]

  <app>        chatty | joy
  --faq <p>    explicit mined-FAQ file (default: newest in
               ~/CSL/reports/weekly-faqs/<app>/)

Output:
  - downloads every KB file to /tmp/kb-sync/<app>/<flattened-path>
  - prints a manifest: FAQ file used, agent id, KB file count, and the
    full KB file list so Claude knows what exists.
"""
import glob
import json
import os
import sys

import kb_api

FAQ_DIR = os.path.expanduser("~/CSL/reports/weekly-faqs")


def latest_faq(app):
    pat = os.path.join(FAQ_DIR, app, f"{app}_*.md")
    files = [f for f in glob.glob(pat) if "skeleton" not in os.path.basename(f)]
    if not files:
        return None
    # filenames embed dates app_YYYY-MM-DD_YYYY-MM-DD.md → lexical sort works
    return sorted(files)[-1]


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: prep.py <app> [--faq <path>]")
    app = sys.argv[1].lower()
    if app not in kb_api.APP_AGENTS:
        sys.exit(f"unknown app '{app}' (use: {', '.join(kb_api.APP_AGENTS)})")

    faq_path = None
    if "--faq" in sys.argv:
        faq_path = sys.argv[sys.argv.index("--faq") + 1]
    else:
        faq_path = latest_faq(app)
    if not faq_path or not os.path.exists(faq_path):
        sys.exit(f"no mined-FAQ file found for {app} (looked in {FAQ_DIR}/{app}/)")

    base, token = kb_api.load_creds()
    agent = kb_api.agent_id(app)
    files = kb_api.list_files(base, token, agent)

    cache = f"/tmp/kb-sync/{app}"
    os.makedirs(cache, exist_ok=True)
    for f in files:
        content = kb_api.get_file(base, token, agent, f)
        if content is None:
            continue
        flat = f.replace("/", "__")
        with open(os.path.join(cache, flat), "w") as out:
            out.write(content)

    manifest = {
        "app": app,
        "agent": agent,
        "faq_file": faq_path,
        "kb_cache_dir": cache,
        "kb_file_count": len(files),
        "kb_files": files,
    }
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
