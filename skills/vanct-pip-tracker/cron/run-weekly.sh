#!/bin/bash
#
# Weekly VanCT PIP tracker run — invoked by launchd (com.avada.vanct-pip-tracker-weekly).
# Runs Monday 11:00, reports the FULL week that just ended, and writes into
# the Google Sheet ("Overview" tab). Two steps:
#   1. fill_weekly.py       — pure Python (SLA / DFY / ONB / check-in muộn)
#   2. prompt_knowledge_check.txt — headless Claude (Product Knowledge row —
#      needs to actually read chat transcripts and compare vs KB, so it's an
#      LLM step, not a data pull)
#
# Manual run: bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
LOG="/tmp/vanct-pip-tracker-weekly.log"
PY="$REPO/.venv-crisp/bin/python"
PROMPT_FILE="$HERE/prompt_knowledge_check.txt"

echo "===== vanct-pip-tracker-weekly run: $(date) =====" >> "$LOG"

cd "$REPO"

rc=0
"$PY" "$REPO/skills/vanct-pip-tracker/scripts/fill_weekly.py" >> "$LOG" 2>&1 || rc=$?

echo "----- knowledge check step -----" >> "$LOG"

unset ANTHROPIC_API_KEY
rc2=0
"$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || rc2=$?

echo "===== done: $(date) =====" >> "$LOG"

final_status="ok"
if [ "${rc:-0}" -ne 0 ] || [ "${rc2:-0}" -ne 0 ]; then final_status="fail"; fi

python3 "$REPO/skills/_shared/notify_tele.py" --job "VanCT PIP tracker (weekly)" \
  --status "$final_status" --log "$LOG" >> "$LOG" 2>&1 || true

if [ "${rc:-0}" -ne 0 ]; then exit "${rc}"; fi
exit "${rc2:-0}"
