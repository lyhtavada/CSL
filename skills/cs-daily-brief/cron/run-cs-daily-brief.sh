#!/bin/bash
#
# Daily CS brief run — invoked by launchd (com.avada.cs-daily-brief).
# Runs Claude Code headless: conversation volume + checkin/checkout for the
# previous full day, plus the neglected-ticket watch (see SKILL.md), DMs Liz.
#
# Manual run:  bash run-cs-daily-brief.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/cs-daily-brief.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== cs-daily-brief run: $(date) =====" >> "$LOG"

cd "$REPO"

# --dangerously-skip-permissions: headless, no interactive approval available.
# Auth uses the Claude subscription (OAuth) → subscription quota, not a paid API
# bill. Unset any ANTHROPIC_API_KEY a repo .env might inject so we don't switch
# into paid-API mode.
unset ANTHROPIC_API_KEY

rc=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

# Báo Telegram cho Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "CS Daily Brief" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
