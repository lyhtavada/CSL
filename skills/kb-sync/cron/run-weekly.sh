#!/bin/bash
#
# Weekly KB-sync DIFF run — invoked by launchd (com.avada.kb-sync).
# Runs Claude Code headless to diff the latest mined-FAQ file against the live
# CS v2 KB for both apps, build payloads, and DM Liz to review.
# It does NOT push to v2 and does NOT reindex (review-gate).
#
# Scheduled Monday 16:30 — 30 min AFTER /mine-chat-faqs (Mon 16:00) writes new files.
#
# Manual run:  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/kb-sync-weekly.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== kb-sync weekly diff run: $(date) =====" >> "$LOG"

cd "$REPO"

# Headless: no interactive approval available. Subscription OAuth (no API bill).
# Unset any repo-injected ANTHROPIC_API_KEY so we stay on subscription auth.
unset ANTHROPIC_API_KEY

"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1

echo "===== done: $(date) =====" >> "$LOG"
