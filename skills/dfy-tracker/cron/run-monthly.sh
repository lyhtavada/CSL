#!/bin/bash
#
# Monthly DFY KPI report run — invoked by launchd (com.avada.dfy-tracker-monthly).
# Runs Claude Code headless to generate the Joy AND Chatty DFY monthly KPI reports
# for LAST month and save them into:
#   reports/dfy/joy/joy-dfy-{YYYY-MM}.md      (tag-based scoring)
#   reports/dfy/chatty/chatty-dfy-{YYYY-MM}.md (task-based scoring)
#
# Manual run (e.g. machine was off on the 2nd):  bash run-monthly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/dfy-tracker-monthly.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== dfy-tracker-monthly run: $(date) =====" >> "$LOG"

cd "$REPO"

# --dangerously-skip-permissions: headless, no interactive approval available.
# Auth uses the Claude subscription (OAuth) → draws on subscription quota,
# not a paid API bill. Unset any ANTHROPIC_API_KEY a repo .env might inject
# so we don't accidentally switch into paid-API mode.
unset ANTHROPIC_API_KEY

rc=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

# Báo Telegram cho Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "DFY Tracker (monthly)" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
