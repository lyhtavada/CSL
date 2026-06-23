#!/bin/bash
#
# Weekly CS bulletin run — invoked by launchd (com.avada.cs-weekly).
# Runs Claude Code headless to generate the team-facing CS weekly reports
# for Chatty + Joy (period = Mon→Sun of last week). Output = Notion sub-pages
# only (one per app) + a Slack digest to each CS channel — nothing written to the repo.
#
# Manual run:  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/cs-weekly.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== cs-weekly run: $(date) =====" >> "$LOG"

cd "$REPO"

# --dangerously-skip-permissions: headless, no interactive approval available.
# Auth uses the Claude subscription (OAuth) → subscription quota, not a paid API
# bill. Unset any ANTHROPIC_API_KEY a repo .env might inject so we don't switch
# into paid-API mode.
unset ANTHROPIC_API_KEY

rc=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

# Báo Telegram cho Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "CS Weekly" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
