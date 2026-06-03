#!/bin/bash
#
# Daily CS report run — invoked by launchd (com.avada.cs-daily) at 09:00 local.
# Runs Claude Code headless to generate the CS Team G2 daily report over the
# last 24h (9:00 yesterday -> 9:00 today VN) and post it to #cs-2-daily.
#
# Manual run:  bash run-daily.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/cs-daily.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== cs-daily run: $(date) =====" >> "$LOG"

cd "$REPO"

# Fresh working dir each run so stale data from a prior day can't leak in.
rm -rf /tmp/csdaily

# --dangerously-skip-permissions: headless, no interactive approval available.
# Auth uses the Claude subscription (OAuth) -> draws on subscription quota, not
# a paid API bill. Unset any ANTHROPIC_API_KEY a repo .env might inject so we
# don't accidentally switch into paid-API mode.
unset ANTHROPIC_API_KEY

"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1

echo "===== done: $(date) =====" >> "$LOG"
