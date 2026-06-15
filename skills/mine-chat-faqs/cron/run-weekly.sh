#!/bin/bash
#
# Weekly FAQ mining run — invoked by launchd (com.avada.mine-faqs).
# Runs Claude Code headless to mine FAQs for both Joy and Chatty over the
# LAST FULL CALENDAR WEEK (Mon→Sun), writing dated files into
# CSL/reports/weekly-faqs/{app}/.
#
# Manual run:  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/mine-faqs-weekly.log"
PROMPT_FILE="$HERE/prompt.txt"

# Last full calendar week: Monday → Sunday of the week BEFORE today.
# (Job runs Monday; we want the previous Mon..Sun, not the current week.)
WEEK_START="$(date -v-mon -v-7d +%Y-%m-%d)"   # most recent past Monday, then back 7 days
WEEK_END="$(date -v-sun +%Y-%m-%d)"           # most recent past Sunday (yesterday when run on Mon)

echo "===== mine-chat-faqs weekly run: $(date) =====" >> "$LOG"
echo "window: $WEEK_START → $WEEK_END" >> "$LOG"

cd "$REPO"

# --dangerously-skip-permissions: headless, no interactive approval available.
# Auth uses the Claude subscription (OAuth), so runs draw on subscription quota,
# not a paid API bill — no --max-budget-usd needed.
# Unset any ANTHROPIC_API_KEY that a repo .env might inject, so we don't
# accidentally switch into paid-API mode.
unset ANTHROPIC_API_KEY

PROMPT="$(cat "$PROMPT_FILE")
WINDOW (use these EXACT dates): --start $WEEK_START --end $WEEK_END (last full Mon→Sun week).
Output filename dates = $WEEK_START to $WEEK_END."

"$CLAUDE_BIN" -p "$PROMPT" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1

echo "===== done: $(date) =====" >> "$LOG"
