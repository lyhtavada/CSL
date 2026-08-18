#!/bin/bash
#
# Install / reinstall the daily bot-corrections launchd job.
# Symlinks the versioned plist (kept in CSL) into ~/Library/LaunchAgents,
# so the source of truth stays in the repo.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.bot-corrections"
SRC="$HERE/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl unload "$DEST" 2>/dev/null || true
  rm -f "$DEST"
  echo "Removed $LABEL."
  exit 0
fi

chmod +x "$HERE/run-daily.sh"

# Reload cleanly if already installed.
launchctl unload "$DEST" 2>/dev/null || true
ln -sf "$SRC" "$DEST"
launchctl load "$DEST"

echo "Installed $LABEL → runs Mon-Fri 15:00 local."
echo "  plist (source): $SRC"
echo "  symlink:        $DEST"
echo "  log:            /tmp/bot-corrections.log"
echo
echo "Test now without waiting for the next scheduled run:"
echo "  launchctl start $LABEL"
echo "  # or run the script directly:"
echo "  bash $HERE/run-daily.sh"
