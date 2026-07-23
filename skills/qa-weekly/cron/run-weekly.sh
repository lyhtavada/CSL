#!/bin/bash
#
# Weekly QA run — invoked by launchd (com.avada.qa-weekly).
# Runs Claude Code headless to grade in-house CS chats for the week that just
# ended, writes reports into reports/qa-weekly/qa-weekly-<ISO-week>/, then DMs
# the full result to Liz for review. It does NOT send anything to CS — Liz
# reviews and gives the go-ahead manually.
#
# Schedule: Friday 14:00 local (see com.avada.qa-weekly.plist).
# Manual run:  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/qa-weekly.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== qa-weekly run: $(date) =====" >> "$LOG"

cd "$REPO"

# Headless: no interactive approval. Auth via Claude subscription (OAuth) —
# runs draw on subscription quota, not a paid API bill. Unset any
# ANTHROPIC_API_KEY a repo .env might inject so we stay in subscription mode.
unset ANTHROPIC_API_KEY

# The prompt fans grading into background Workflow batches. Headless claude
# kills still-running background tasks after 600s by default — not enough for
# 9 CS x 30 chats, so it exits before any report is written.
# 0 = wait indefinitely for our own background workflows to finish.
export CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0

rc=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

# Báo Telegram cho Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "QA Weekly" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
