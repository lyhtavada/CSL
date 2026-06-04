#!/bin/bash
#
# Weekly QA run — invoked by launchd (com.avada.qa-weekly).
# Runs Claude Code headless to grade in-house CS chats for the week that just
# ended, writes reports into reports/qa-weekly/qa-weekly-<ISO-week>/, then DMs
# the full result to Liz for review. It does NOT send anything to CS — Liz
# reviews and gives the go-ahead manually.
#
# Schedule: Monday 14:00 local (see com.avada.qa-weekly.plist).
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

"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1

echo "===== done: $(date) =====" >> "$LOG"
