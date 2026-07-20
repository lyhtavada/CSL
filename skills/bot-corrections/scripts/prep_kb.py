#!/usr/bin/env python3
"""
prep_kb.py — cache live KB v2 files for an app + locate the newest bot-corrections
report (output of fetch_corrections.py), so Claude can diff corrections against the
KB (COVERED / OUTDATED / GAP / PARTIAL) and draft patches.

Usage:
  python3 prep_kb.py <app> [--report <path>]

  <app>          chatty | joy
  --report <p>   explicit corrections report file (default: newest in
                 ~/CSL/reports/bot-corrections/<app>/)

Output:
  - downloads every KB file to /tmp/bot-corrections-kb/<app>/<flattened-path>
  - prints a manifest: report file used, agent id, KB file count, full KB file list
"""
import glob
import json
import os
import sys

import kb_api

REPORT_DIR = os.path.expanduser("~/CSL/reports/bot-corrections")


def latest_report(app):
    pat = os.path.join(REPORT_DIR, app, f"{app}-corrections-*.md")
    files = glob.glob(pat)
    if not files:
        return None
    # filenames embed the Monday date → lexical sort works
    return sorted(files)[-1]


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: prep_kb.py <app> [--report <path>]")
    app = sys.argv[1].lower()
    if app not in kb_api.APP_AGENTS:
        sys.exit(f"unknown app '{app}' (use: {', '.join(kb_api.APP_AGENTS)})")

    report_path = None
    if "--report" in sys.argv:
        report_path = sys.argv[sys.argv.index("--report") + 1]
    else:
        report_path = latest_report(app)
    if not report_path or not os.path.exists(report_path):
        sys.exit(f"no corrections report found for {app} (looked in {REPORT_DIR}/{app}/)")

    base, token = kb_api.load_creds()
    agent = kb_api.agent_id(app)
    files = kb_api.list_files(base, token, agent)

    cache = f"/tmp/bot-corrections-kb/{app}"
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
        "report_file": report_path,
        "kb_cache_dir": cache,
        "kb_file_count": len(files),
        "kb_files": files,
    }
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
