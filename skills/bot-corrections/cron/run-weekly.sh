#!/bin/bash
#
# Weekly bot-corrections run — invoked by launchd (com.avada.bot-corrections).
#
# Step 1 (pure script): pull correction (câu bot bị CS sửa) của Joyce + Ivy trong
# tuần vừa qua (Thứ 5 tuần trước → Thứ 4 tuần này), ghi report markdown vào
# reports/bot-corrections/, commit.
#
# Step 2 (Claude headless): diff report tuần này với KB live trên CS v2 cho cả
# 2 app, classify COVERED/OUTDATED/GAP/PARTIAL, soạn payload patch, DM Telegram
# cho Liz. Review-gate — KHÔNG tự push/reindex, Liz duyệt rồi tự chạy push_kb.py.
#
# Manual run:  bash run-weekly.sh
#
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/bot-corrections.log"
SCRIPT="$REPO/skills/bot-corrections/scripts/fetch_corrections.py"
DIFF_PROMPT="$HERE/prompt-diff.txt"

echo "===== bot-corrections run: $(date) =====" >> "$LOG"
cd "$REPO" || { echo "cd $REPO failed" >> "$LOG"; exit 1; }

python3 "$SCRIPT" >> "$LOG" 2>&1
rc=$?
if [ $rc -ne 0 ]; then
  echo "fetch_corrections.py exited $rc" >> "$LOG"
  python3 "$REPO/skills/_shared/notify_tele.py" --job "Bot Corrections" \
    --status fail --log "$LOG" >> "$LOG" 2>&1 || true
  exit $rc
fi

# Commit report mới + prune report cũ (fetch_corrections.py chỉ giữ 2 tuần gần nhất
# /app -> git add -A để bắt cả file bị xoá, không phải chỉ file mới/sửa)
if [ -n "$(git status --porcelain reports/bot-corrections/ 2>/dev/null)" ]; then
  git add -A reports/bot-corrections/ >> "$LOG" 2>&1
  git commit -m "bot-corrections: weekly report $(date +%Y-%m-%d)" >> "$LOG" 2>&1
  echo "committed report (+ prune)" >> "$LOG"
else
  echo "no report changes to commit" >> "$LOG"
fi

echo "----- diff vs KB v2 (review-gate, no push) -----" >> "$LOG"

# Headless: subscription OAuth (no API bill). Unset any repo-injected key.
unset ANTHROPIC_API_KEY

diff_rc=0
"$CLAUDE_BIN" -p "$(cat "$DIFF_PROMPT")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || diff_rc=$?

echo "===== done: $(date) =====" >> "$LOG"

if [ $diff_rc -ne 0 ]; then
  echo "diff step exited $diff_rc (report tuần này vẫn đã commit ở trên)" >> "$LOG"
  python3 "$REPO/skills/_shared/notify_tele.py" --job "Bot Corrections" \
    --status fail --log "$LOG" >> "$LOG" 2>&1 || true
  exit $diff_rc
fi

# Diff step tự gửi Telegram digest chi tiết (per app) rồi — không gửi trùng nữa.
