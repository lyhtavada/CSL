#!/bin/bash
#
# Weekly bot-corrections run — invoked by launchd (com.avada.bot-corrections).
# Pull các correction (câu bot bị CS sửa) của Joyce + Ivy trong tuần trước (Mon→Sun),
# ghi report markdown vào reports/bot-corrections/, rồi commit.
#
# Thuần script (không cần Claude headless) — chỉ fetch + render + git commit.
#
# Manual run:  bash run-weekly.sh
#
set -uo pipefail

REPO="/Users/avada/CSL"
LOG="/tmp/bot-corrections.log"
SCRIPT="$REPO/skills/bot-corrections/scripts/fetch_corrections.py"

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

# Commit report mới (nếu có thay đổi)
if [ -n "$(git status --porcelain reports/bot-corrections/ 2>/dev/null)" ]; then
  git add reports/bot-corrections/ >> "$LOG" 2>&1
  git commit -m "bot-corrections: weekly report $(date +%Y-%m-%d)" >> "$LOG" 2>&1
  echo "committed report" >> "$LOG"
else
  echo "no report changes to commit" >> "$LOG"
fi

echo "===== done: $(date) =====" >> "$LOG"

# Báo Telegram cho Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "Bot Corrections" \
  --status ok --log "$LOG" >> "$LOG" 2>&1 || true
