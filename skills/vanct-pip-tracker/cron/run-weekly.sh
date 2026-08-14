#!/bin/bash
#
# Weekly VanCT PIP tracker run — invoked by launchd (com.avada.vanct-pip-tracker-weekly).
# Runs Monday 11:00, reports the FULL week that just ended, and writes into
# the Google Sheet ("Overview" tab): SLA / DFY / ONB / check-in muộn.
#
# Product Knowledge (row 7) is deliberately NOT run here — Liz reviews it
# manually each week instead of letting it run unsupervised (it needs an
# LLM to read real chat transcripts and judge them, burns real subscription
# quota, and a misread should be caught before it lands in the sheet). See
# prompt_knowledge_check.txt — run it by hand:
#   claude -p "$(cat skills/vanct-pip-tracker/cron/prompt_knowledge_check.txt)"
#
# Manual run: bash run-weekly.sh
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="/Users/avada/CSL"
LOG="/tmp/vanct-pip-tracker-weekly.log"
PY="$REPO/.venv-crisp/bin/python"

echo "===== vanct-pip-tracker-weekly run: $(date) =====" >> "$LOG"

cd "$REPO"

rc=0
"$PY" "$REPO/skills/vanct-pip-tracker/scripts/fill_weekly.py" >> "$LOG" 2>&1 || rc=$?

echo "===== done: $(date) =====" >> "$LOG"

python3 "$REPO/skills/_shared/notify_tele.py" --job "VanCT PIP tracker (weekly)" \
  --status "$([ "${rc:-0}" -eq 0 ] && echo ok || echo fail)" --log "$LOG" >> "$LOG" 2>&1 || true

exit "${rc:-0}"
