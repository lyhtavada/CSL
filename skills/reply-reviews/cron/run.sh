#!/bin/bash
#
# reply-reviews run — invoked by launchd (com.avada.reply-reviews), T3 + T6 17:00.
#
# Step 1 (script): fetch unreplied Chatty mobile reviews (App Store + Google Play)
# not yet drafted/skipped. Google Play API only sees the last 7 days, hence 2x/week.
# Step 2 (Claude headless, only when new reviews): draft replies -> save as pending
# -> Telegram digest to Liz. NEVER posts — Liz approves via the Telegram bot.
#
# Manual run:  bash run.sh
#
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_BIN="/opt/homebrew/bin/claude"
REPO="/Users/avada/CSL"
PY="$REPO/.venv-crisp/bin/python"
LOG="/tmp/reply-reviews.log"
SCRIPT="$REPO/skills/reply-reviews/scripts/reviews.py"
JOB="Reply Reviews"

echo "===== reply-reviews run: $(date) =====" >> "$LOG"
cd "$REPO" || { echo "cd $REPO failed" >> "$LOG"; exit 1; }

FETCH_OUT="$("$PY" -W ignore "$SCRIPT" fetch --out /tmp/reply-reviews-new.json 2>&1)"
rc=$?
echo "$FETCH_OUT" >> "$LOG"
if [ $rc -ne 0 ]; then
  echo "fetch exited $rc" >> "$LOG"
  python3 "$REPO/skills/_shared/notify_tele.py" --job "$JOB" --status fail --log "$LOG" >> "$LOG" 2>&1 || true
  exit $rc
fi

TOTAL_NEW="$(echo "$FETCH_OUT" | grep -oE 'TOTAL_NEW=[0-9]+' | cut -d= -f2)"
TOTAL_NEW="${TOTAL_NEW:-0}"

if [ "$TOTAL_NEW" -eq 0 ]; then
  PENDING="$("$PY" -W ignore "$SCRIPT" list 2>/dev/null | "$PY" -c 'import json,sys; print(len(json.load(sys.stdin)))' 2>/dev/null || echo 0)"
  if [ "${PENDING:-0}" -gt 0 ]; then
    python3 "$REPO/skills/_shared/notify_tele.py" --job "$JOB" --status ok \
      --summary "Không có review mới. Còn $PENDING draft chờ chị duyệt — nhắn bot \"list draft review\" để xem." >> "$LOG" 2>&1 || true
  fi
  echo "no new reviews — done: $(date)" >> "$LOG"
  exit 0
fi

# Headless: subscription OAuth (no API bill). Unset any repo-injected key.
unset ANTHROPIC_API_KEY

draft_rc=0
"$CLAUDE_BIN" -p "$(cat "$HERE/prompt.txt")" \
  --model claude-sonnet-5 \
  --dangerously-skip-permissions \
  >> "$LOG" 2>&1 || draft_rc=$?

echo "===== done: $(date) =====" >> "$LOG"

if [ $draft_rc -ne 0 ]; then
  echo "draft step exited $draft_rc" >> "$LOG"
  python3 "$REPO/skills/_shared/notify_tele.py" --job "$JOB" --status fail --log "$LOG" >> "$LOG" 2>&1 || true
  exit $draft_rc
fi
