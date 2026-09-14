#!/bin/bash
#
# Twice-weekly product-KB-sync DIFF run — invoked by launchd
# (com.avada.product-kb-sync, Tue + Fri 10:00). Diffs Slack product-release
# posts + GitLab label/nav/feature-doc changes against live CS v2 KB for
# chatty + joy, builds payloads, DMs Liz to review.
# Does NOT push to v2, does NOT reindex, does NOT advance state (review-gate).
#
# Manual run:  bash run-twice-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/product-kb-sync.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== product-kb-sync diff run: $(date) =====" >> "$LOG"

cd "$REPO"

unset ANTHROPIC_API_KEY

# TẠM THỜI (Liz chốt 2026-09-14): tài khoản mặc định (~/.claude) hết quota tuần,
# reset 13:00 15/09 → riêng ngày 15/09 chạy bằng ~/.claude-tsl. Tự hết hạn: từ
# 16/09 quay về mặc định. Xoá block này khi tiện.
if [ "$(date +%Y-%m-%d)" = "2026-09-15" ]; then
  export CLAUDE_CONFIG_DIR="/Users/avada/.claude-tsl"
  echo "(temp override: CLAUDE_CONFIG_DIR=~/.claude-tsl)" >> "$LOG"
fi

rc=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

python3 "$REPO/skills/_shared/notify_tele.py" --job "Product KB Sync" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
