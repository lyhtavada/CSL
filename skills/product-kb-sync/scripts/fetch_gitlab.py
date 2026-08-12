#!/usr/bin/env python3
"""
fetch_gitlab.py — diff an app's B1 (feature docs) and B2 (label/nav) paths
between the last synced commit and current HEAD, via `glab api` (read-only).

Usage:
  python3 fetch_gitlab.py <app>

Does NOT update state — caller updates state only after the diff step
actually completes (same reasoning as fetch_slack.py).
Prints JSON: {app, project, from_sha, to_sha, b1_changes: [...], b2_changes: [...]}
Each change entry: {path, diff} where diff is GitLab's unified diff text.
"""
import json
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
import state


def glab_api(path):
    r = subprocess.run(["glab", "api", path], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        sys.exit(f"glab api failed for {path}: {r.stderr.strip()}")
    return json.loads(r.stdout)


def head_sha(project, branch):
    commits = glab_api(f"projects/{project}/repository/commits?ref_name={branch}&per_page=1")
    return commits[0]["id"]


def compare(project, from_sha, to_sha):
    return glab_api(f"projects/{project}/repository/compare?from={from_sha}&to={to_sha}")


def under_any(path, prefixes):
    return any(path == p or path.startswith(p.rstrip("/") + "/") for p in prefixes)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: fetch_gitlab.py <app>")
    app = sys.argv[1].lower()
    if app not in config.APPS:
        sys.exit(f"unknown app '{app}' (use: {', '.join(config.APPS)})")

    cfg = config.APPS[app]
    project = cfg["gitlab_project"]
    branch = cfg["branch"]

    app_state = state.get_app_state(app)
    from_sha = app_state.get("last_gitlab_commit", {}).get(project)
    to_sha = head_sha(project, branch)

    if not from_sha:
        sys.exit(f"no baseline commit for {app}/{project} in state — seed state/last_sync.json first")

    if from_sha == to_sha:
        out = {"app": app, "project": project, "from_sha": from_sha, "to_sha": to_sha,
               "b1_changes": [], "b2_changes": [], "note": "no new commits since last sync"}
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return

    result = compare(project, from_sha, to_sha)
    diffs = result.get("diffs", [])

    b1_changes, b2_changes, skipped = [], [], 0
    for d in diffs:
        path = d.get("new_path") or d.get("old_path")
        entry = {"path": path, "diff": d.get("diff", "")}
        if under_any(path, cfg["b1_paths"]):
            b1_changes.append(entry)
        elif under_any(path, cfg["b2_paths"]):
            b2_changes.append(entry)
        else:
            skipped += 1

    out = {
        "app": app,
        "project": project,
        "from_sha": from_sha,
        "to_sha": to_sha,
        "commit_count": len(result.get("commits", [])),
        "b1_changes": b1_changes,
        "b2_changes": b2_changes,
        "skipped_unrelated_files": skipped,
        "notes": cfg.get("notes", ""),
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
