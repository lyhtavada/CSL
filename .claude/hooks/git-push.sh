#!/usr/bin/env bash
# Stop hook: commit & push any changes so the other machine sees them next session.
set -euo pipefail

cd "$(git -C "${CLAUDE_PROJECT_DIR:-$PWD}" rev-parse --show-toplevel 2>/dev/null)" || exit 0

# Nothing changed → nothing to do.
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

git add -A

# Commit message: timestamp + machine name so history shows where the change came from.
STAMP="$(date '+%Y-%m-%d %H:%M')"
HOST="$(scutil --get ComputerName 2>/dev/null || hostname -s)"
git commit -m "auto-sync: ${STAMP} (${HOST})" >/dev/null 2>&1 || exit 0

if ! git ls-remote --exit-code origin >/dev/null 2>&1; then
  echo "[csl-sync] Đã commit nhưng remote không reachable — push lần sau." >&2
  exit 0
fi

# Pull first in case the other machine pushed mid-session, then push.
git pull --rebase --autostash origin main >/dev/null 2>&1 || true
git push origin main 2>&1 | tail -2 || echo "[csl-sync] Push thất bại — kiểm tra git status." >&2
