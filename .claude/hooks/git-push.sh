#!/usr/bin/env bash
# Stop hook: commit & push any changes so the other machine sees them next session.
set -euo pipefail

cd "$(git -C "${CLAUDE_PROJECT_DIR:-$PWD}" rev-parse --show-toplevel 2>/dev/null)" || exit 0

GIT_DIR_PATH="$(git rev-parse --git-dir)"

# Never commit on top of a half-finished rebase/merge. This is the guard that
# was missing on 2026-08-10: the pull below left a rebase stopped mid-conflict,
# and every later run of this hook piled another commit onto the resulting
# detached HEAD — 12 of them, none on any branch, none pushed, before anyone
# noticed. A broken state needs a human, not more commits.
if [ -d "$GIT_DIR_PATH/rebase-merge" ] || [ -d "$GIT_DIR_PATH/rebase-apply" ] \
   || [ -f "$GIT_DIR_PATH/MERGE_HEAD" ] || [ -f "$GIT_DIR_PATH/CHERRY_PICK_HEAD" ]; then
  echo "[csl-sync] Đang có rebase/merge/cherry-pick dở — BỎ QUA commit+push." >&2
  echo "[csl-sync] Xử lý tay rồi hãy tiếp tục: git status" >&2
  exit 0
fi

# Detached HEAD → commits would land on no branch at all. Same reasoning.
if ! git symbolic-ref -q HEAD >/dev/null; then
  echo "[csl-sync] HEAD đang detached — BỎ QUA, commit sẽ không nằm trên branch nào." >&2
  exit 0
fi

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
# Do NOT swallow a failure here (the old `|| true` did, and that is exactly how
# a conflicted rebase got left behind): abort so the tree is clean again, and
# say so loudly instead of pushing on top of a mess.
if ! git pull --rebase --autostash origin main >/dev/null 2>&1; then
  git rebase --abort 2>/dev/null || true
  echo "[csl-sync] Pull --rebase bị conflict — đã abort, KHÔNG push." >&2
  echo "[csl-sync] Commit ở local vẫn an toàn. Merge tay rồi push: git pull origin main" >&2
  exit 0
fi

git push origin main 2>&1 | tail -2 || echo "[csl-sync] Push thất bại — kiểm tra git status." >&2
