#!/usr/bin/env bash
# start_sim.sh — start (or confirm already running) the local sim-crisp bridge
# process used by kb-test's sim mode. Idempotent: if the sim is already
# healthy on SIM_BASE_URL, does nothing.
#
# One-time setup before first run:
#   1. tailscale up   (must be connected to reach prod Postgres via HAProxy)
#   2. cp sim.env.example ~/avada-cs-ai-agent-crisp-chat/.env.sim
#      and fill in DATABASE_URL password + ANTHROPIC_API_KEY + a random
#      CRISP_WEBHOOK_SECRET
#
# Usage: ./start_sim.sh
set -euo pipefail

BRIDGE_DIR="${BRIDGE_DIR:-$HOME/avada-cs-ai-agent-crisp-chat}"
ENV_FILE="${SIM_ENV_FILE:-$BRIDGE_DIR/.env.sim}"
SIM_BASE_URL="${SIM_BASE_URL:-http://127.0.0.1:8031}"
LOG_FILE="${SIM_LOG_FILE:-/tmp/bridge-sim.log}"
PID_FILE="${SIM_PID_FILE:-/tmp/bridge-sim.pid}"

if curl -sf --max-time 3 "$SIM_BASE_URL/health" >/dev/null 2>&1; then
  echo "sim bridge already healthy at $SIM_BASE_URL"
  exit 0
fi

if [ ! -d "$BRIDGE_DIR" ]; then
  echo "ERROR: bridge repo not found at $BRIDGE_DIR" >&2
  echo "  glab repo clone avada/cs-team/avada-cs-ai-agent-crisp-chat ~/avada-cs-ai-agent-crisp-chat" >&2
  exit 1
fi

if [ ! -f "$ENV_FILE" ]; then
  echo "ERROR: $ENV_FILE not found." >&2
  echo "  cp $(dirname "$0")/sim.env.example $ENV_FILE" >&2
  echo "  then fill in DATABASE_URL / ANTHROPIC_API_KEY / CRISP_WEBHOOK_SECRET" >&2
  exit 1
fi

echo "starting sim bridge in $BRIDGE_DIR (log: $LOG_FILE)..."
cd "$BRIDGE_DIR"
# shellcheck disable=SC2046
(set -a; source "$ENV_FILE"; set +a; nohup bun run bridge.ts >"$LOG_FILE" 2>&1 & echo $! > "$PID_FILE")

for i in $(seq 1 30); do
  if curl -sf --max-time 2 "$SIM_BASE_URL/health" >/dev/null 2>&1; then
    echo "sim bridge up (pid $(cat "$PID_FILE")), log at $LOG_FILE"
    exit 0
  fi
  sleep 1
done

echo "ERROR: sim bridge didn't become healthy in 30s — check $LOG_FILE" >&2
exit 1
