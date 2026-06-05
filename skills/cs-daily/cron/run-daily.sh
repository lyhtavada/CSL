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

# Retry on transient auth failures. At 09:00 the OAuth token can still be
# expired/unrefreshed, surfacing as "401 Invalid authentication credentials".
# A short wait lets the token refresh, so retry a few times with backoff
# before giving up. Each retry's output goes into a temp file we can grep.
PROMPT="$(cat "$PROMPT_FILE")"
MAX_ATTEMPTS=3
SLEEP_SECS=(60 120 240)   # 1m, 2m, 4m backoff between attempts

attempt=1
while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
  echo "----- attempt $attempt/$MAX_ATTEMPTS: $(date) -----" >> "$LOG"
  RUN_OUT="$(mktemp)"

  set +e
  "$CLAUDE_BIN" -p "$PROMPT" \
    --model claude-opus-4-8 \
    --fallback-model claude-sonnet-4-6 \
    --dangerously-skip-permissions \
    > "$RUN_OUT" 2>&1
  rc=$?
  set -e

  cat "$RUN_OUT" >> "$LOG"

  # Success = exit 0 AND no auth error in the output.
  if [ "$rc" -eq 0 ] && ! grep -qiE "401|Invalid authentication|Failed to authenticate" "$RUN_OUT"; then
    rm -f "$RUN_OUT"
    echo "===== done (attempt $attempt): $(date) =====" >> "$LOG"
    exit 0
  fi

  rm -f "$RUN_OUT"
  echo "----- attempt $attempt failed (rc=$rc) -----" >> "$LOG"

  if [ "$attempt" -lt "$MAX_ATTEMPTS" ]; then
    wait_s="${SLEEP_SECS[$((attempt-1))]}"
    echo "----- waiting ${wait_s}s before retry (token may refresh) -----" >> "$LOG"
    sleep "$wait_s"
  fi
  attempt=$((attempt+1))
done

echo "===== FAILED after $MAX_ATTEMPTS attempts: $(date) =====" >> "$LOG"
exit 1
