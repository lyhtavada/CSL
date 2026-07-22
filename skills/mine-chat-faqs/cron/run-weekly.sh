#!/bin/bash
#
# Weekly FAQ mining + KB diff/patch run — invoked by launchd (com.avada.mine-faqs).
# Runs Claude Code headless to mine FAQs for Joy, Chatty, and Wishlist over the
# LAST FULL CALENDAR WEEK (Mon→Sun), writing dated files into
# CSL/reports/weekly-faqs/{app}/, then chains into the kb-sync diff+patch flow
# and DMs Liz a review digest. Never pushes to v2 / reindexes.
#
# Manual run:  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/mine-faqs-weekly.log"
PROMPT_FILE="$HERE/prompt.txt"

# Last full completed calendar week: Monday → Sunday, ending on the most recent
# past Sunday. Computed from WEEK_END backward so it's correct regardless of
# which weekday the job actually runs on (currently Tuesday 11:00).
WEEK_END="$(date -v-sun +%Y-%m-%d)"                                  # most recent past Sunday
WEEK_START="$(date -j -v-6d -f %Y-%m-%d "$WEEK_END" +%Y-%m-%d)"      # Monday of that same week

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

rc=0
"$CLAUDE_BIN" -p "$PROMPT" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

# Báo Telegram cho Liz (xong + lỗi). Notify không được làm hỏng job.
python3 "$REPO/skills/_shared/notify_tele.py" --job "Mine FAQs + KB Diff" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
