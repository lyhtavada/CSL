#!/bin/bash
#
# Monthly DFY KPI report run — invoked by launchd (com.avada.dfy-tracker-monthly).
# Runs Claude Code headless to generate the Joy DFY monthly KPI report for
# LAST month and save it into reports/dfy/joy/joy-dfy-{YYYY-MM}.md.
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

"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1

echo "===== done: $(date) =====" >> "$LOG"
