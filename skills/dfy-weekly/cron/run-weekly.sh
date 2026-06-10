#!/bin/bash
#
# Weekly DFY report run — invoked by launchd (com.avada.dfy-weekly).
# Runs Claude Code headless to generate the Joy DFY weekly report (Fri→Thu)
# and publish it as a NEW Notion sub-page (newest on top) under the
# "Joy DFY Weekly" page. No repo file, no git commit.
#
# Manual run:  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/dfy-weekly.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== dfy-weekly run: $(date) =====" >> "$LOG"

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
