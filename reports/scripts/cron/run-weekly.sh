#!/bin/bash
#
# CEO Weekly run — invoked by launchd (com.avada.ceo-weekly), Mondays 13:00.
# Gộp 2 bản CS Weekly (Chatty + Joy) MỚI NHẤT trên Notion + resolve rate obs
# metrics → reports/weekly/ceo-weekly-<DATE>.md. Chạy SAU cs-weekly (09:00) để
# 2 bản nguồn đã push xong.
#
# Thuần Python (gen-ceo-weekly.py), KHÔNG cần Claude headless.
# Response time + CEO decision: Liz điền tay sau. KHÔNG tự push Notion/Slack/commit.
#
# Manual run:  bash run-weekly.sh [--date YYYY-MM-DD]
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="/Users/avada/CSL"
LOG="/tmp/ceo-weekly.log"

echo "===== ceo-weekly run: $(date) =====" >> "$LOG"

cd "$REPO"

rc=0
python3 "$REPO/reports/scripts/gen-ceo-weekly.py" "$@" >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

# Báo Telegram cho Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "CEO Weekly" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
