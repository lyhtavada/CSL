#!/usr/bin/env bash
# SessionStart hook: pull latest changes from the other machine.
# Safe — autostash keeps any in-progress local edits, rebase keeps history linear.
set -euo pipefail

cd "$(git -C "${CLAUDE_PROJECT_DIR:-$PWD}" rev-parse --show-toplevel 2>/dev/null)" || exit 0

# Skip if no network / remote unreachable, so a session never gets blocked offline.
if ! git ls-remote --exit-code origin >/dev/null 2>&1; then
  echo "[csl-sync] Remote không reachable — bỏ qua pull." >&2
  exit 0
fi

git pull --rebase --autostash origin main 2>&1 | tail -3 || {
  echo "[csl-sync] Pull gặp conflict — cần xử lý tay (git status)." >&2
  exit 0
}

# Also refresh the Joy source clone (separate GitLab repo, gitignored).
# Fully isolated: never blocks the session — offline / expired token / conflict all fail soft.
(
  joy_dir="$(git -C "${CLAUDE_PROJECT_DIR:-$PWD}" rev-parse --show-toplevel)/joy-src"
  [ -d "$joy_dir/.git" ] || exit 0
  cd "$joy_dir" || exit 0
  git ls-remote --exit-code origin >/dev/null 2>&1 || { echo "[joy-src] Remote không reachable — bỏ qua." >&2; exit 0; }
  git pull --depth 1 --rebase --autostash origin master 2>&1 | tail -2 | sed -E 's#oauth2:[^@]+@#oauth2:***@#g' || echo "[joy-src] Pull lỗi — bỏ qua." >&2
) || true
