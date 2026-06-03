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
