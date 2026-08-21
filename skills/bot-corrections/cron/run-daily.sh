#!/bin/bash
#
# Daily bot-corrections run — invoked by launchd (com.avada.bot-corrections),
# T2-T6 15:00 local.
#
# Step 1 (pure script): pull correction (câu bot bị CS sửa) của Joyce + Ivy kể
# từ lần chạy trước (T2 nhìn ngược về T6 tuần trước), ghi report markdown vào
# reports/bot-corrections/, commit. App nào 0 correction thì không ghi file.
#
# Step 2 (Claude headless, CHỈ chạy khi có correction mới): TRIAGE từng
# correction — trace lại conversation gốc (cs2_session.py) để tìm root cause,
# rồi 1 trong 3 nhánh: (a) lỗi hệ thống -> tạo ticket cho Fennic
# (create_bug_ticket.py, dedup qua state/system-bugs.json), (b) thiếu/sai KB
# -> soạn payload patch (VẪN review-gate, Liz duyệt rồi tự push_kb.py), (c) CS
# sửa sai -> auto-verify correction (verify_correction.py --live). (a)/(c) tự
# động thẳng (Liz chốt 2026-08-21: auto, chỉ cần báo cáo). DM Telegram digest
# cuối cùng.
#
# Manual run:  bash run-daily.sh
#
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/bot-corrections.log"
SCRIPT="$REPO/skills/bot-corrections/scripts/fetch_corrections.py"
DIFF_PROMPT="$HERE/prompt-triage.txt"

echo "===== bot-corrections run: $(date) =====" >> "$LOG"
cd "$REPO" || { echo "cd $REPO failed" >> "$LOG"; exit 1; }

FETCH_OUT="$(python3 "$SCRIPT" 2>&1)"
rc=$?
echo "$FETCH_OUT" >> "$LOG"
if [ $rc -ne 0 ]; then
  echo "fetch_corrections.py exited $rc" >> "$LOG"
  python3 "$REPO/skills/_shared/notify_tele.py" --job "Bot Corrections" \
    --status fail --log "$LOG" >> "$LOG" 2>&1 || true
  exit $rc
fi

TOTAL_NEW="$(echo "$FETCH_OUT" | grep -oE 'TOTAL_NEW=[0-9]+' | cut -d= -f2)"
TOTAL_NEW="${TOTAL_NEW:-0}"

# Commit report mới (nếu có) + prune report cũ (fetch_corrections.py chỉ giữ
# ~2 tuần gần nhất/app -> git add -A để bắt cả file bị xoá, không phải chỉ
# file mới/sửa)
if [ -n "$(git status --porcelain reports/bot-corrections/ 2>/dev/null)" ]; then
  git add -A reports/bot-corrections/ >> "$LOG" 2>&1
  git commit -m "bot-corrections: daily report $(date +%Y-%m-%d)" >> "$LOG" 2>&1
  echo "committed report (+ prune)" >> "$LOG"
else
  echo "no report changes to commit" >> "$LOG"
fi

if [ "$TOTAL_NEW" -eq 0 ]; then
  echo "no new corrections today — skip diff/notify" >> "$LOG"
  echo "===== done: $(date) =====" >> "$LOG"
  exit 0
fi

echo "----- triage: trace + ticket/patch/verify -----" >> "$LOG"

# Headless: subscription OAuth (no API bill). Unset any repo-injected key.
unset ANTHROPIC_API_KEY

diff_rc=0
"$CLAUDE_BIN" -p "$(cat "$DIFF_PROMPT")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || diff_rc=$?

echo "===== done: $(date) =====" >> "$LOG"

if [ $diff_rc -ne 0 ]; then
  echo "diff step exited $diff_rc (report hôm nay vẫn đã commit ở trên)" >> "$LOG"
  python3 "$REPO/skills/_shared/notify_tele.py" --job "Bot Corrections" \
    --status fail --log "$LOG" >> "$LOG" 2>&1 || true
  exit $diff_rc
fi

# Diff step tự gửi Telegram digest chi tiết (per app) rồi — không gửi trùng nữa.
