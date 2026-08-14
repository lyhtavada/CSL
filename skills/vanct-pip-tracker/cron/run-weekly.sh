#!/bin/bash
#
# Weekly VanCT PIP tracker run — invoked by launchd (com.avada.vanct-pip-tracker-weekly).
# Runs Monday 11:00, reports the FULL week that just ended (SLA / DFY / ONB /
# check-in muộn), and writes straight into the Google Sheet ("Overview" tab),
# no LLM step needed.
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
