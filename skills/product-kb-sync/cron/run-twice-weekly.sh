#!/bin/bash
#
# Twice-weekly product-KB-sync DIFF run — invoked by launchd
# (com.avada.product-kb-sync, Tue + Fri 10:00). Diffs Slack product-release
# posts + GitLab label/nav/feature-doc changes against live CS v2 KB for
# chatty + joy, builds payloads, DMs Liz to review.
# Does NOT push to v2, does NOT reindex, does NOT advance state (review-gate).
#
# Manual run:  bash run-twice-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/product-kb-sync.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== product-kb-sync diff run: $(date) =====" >> "$LOG"

cd "$REPO"

unset ANTHROPIC_API_KEY

rc=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

python3 "$REPO/skills/_shared/notify_tele.py" --job "Product KB Sync" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
