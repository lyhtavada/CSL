#!/bin/bash
#
# Weekly DFY report run — invoked by launchd (com.avada.dfy-weekly-chatty).
# Runs Claude Code headless to generate the just-finished week's (Fri→Thu) Chatty
# DFY report and post it to the Chatty CS Slack channel as Liz, plus a Notion
# sub-page (newest on top).
#
# Manual run (e.g. machine was off on Friday):  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/dfy-weekly-chatty.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== dfy-weekly-chatty run: $(date) =====" >> "$LOG"

cd "$REPO"

# --dangerously-skip-permissions: headless, no interactive approval available.
# Auth uses the Claude subscription (OAuth) → subscription quota, not paid API.
# Unset any ANTHROPIC_API_KEY a repo .env might inject.
unset ANTHROPIC_API_KEY

rc=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

# Telegram báo Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "DFY Weekly (Chatty)" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
