#!/bin/bash
#
# Weekly FAQ mining run — invoked by launchd (com.avada.mine-faqs).
# Runs Claude Code headless to mine FAQs for both Joy and Chatty over the
# last 7 days, writing dated files into Liz/faq_from_chats/{app}/.
#
# Manual run:  bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/claw-weebhook-crisp-chat"
LOG="/tmp/mine-faqs-weekly.log"
PROMPT_FILE="$HERE/prompt.txt"

echo "===== mine-chat-faqs weekly run: $(date) =====" >> "$LOG"

cd "$REPO"

# --dangerously-skip-permissions: headless, no interactive approval available.
# Auth uses the Claude subscription (OAuth), so runs draw on subscription quota,
# not a paid API bill — no --max-budget-usd needed.
# Unset any ANTHROPIC_API_KEY that a repo .env might inject, so we don't
# accidentally switch into paid-API mode.
unset ANTHROPIC_API_KEY

"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-opus-4-8 \
  --fallback-model claude-sonnet-4-6 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1

echo "===== done: $(date) =====" >> "$LOG"
