"""
state.py — read/write the incremental sync cursor for product-kb-sync.

Tracks, per app: the last Slack ts already processed from the shared
release channel, and the last GitLab commit sha already diffed per repo.
Committed to the CSL repo (small, needed across runs) — NOT gitignored,
unlike kb-sync's temp payload files.
"""
import json
import os

STATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "state", "last_sync.json")


def load():
    with open(STATE_PATH) as f:
        return json.load(f)


def save(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        f.write("\n")


def get_app_state(app):
    return load().get(app, {"last_slack_ts": None, "last_gitlab_commit": {}})


def update_app_state(app, *, last_slack_ts=None, gitlab_commits=None):
    state = load()
    entry = state.setdefault(app, {"last_slack_ts": None, "last_gitlab_commit": {}})
    if last_slack_ts is not None:
        entry["last_slack_ts"] = last_slack_ts
    if gitlab_commits:
        entry["last_gitlab_commit"].update(gitlab_commits)
    save(state)
