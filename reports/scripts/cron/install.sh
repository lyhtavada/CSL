#!/bin/bash
#
# Install / reinstall the CEO-weekly launchd job.
# Symlinks the versioned plist (kept in CSL) into ~/Library/LaunchAgents,
# so the source of truth stays in the repo.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.ceo-weekly"
SRC="$HERE/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl unload "$DEST" 2>/dev/null || true
  rm -f "$DEST"
  echo "Removed $LABEL."
  exit 0
fi

chmod +x "$HERE/run-weekly.sh"

# Reload cleanly if already installed.
launchctl unload "$DEST" 2>/dev/null || true
ln -sf "$SRC" "$DEST"
launchctl load "$DEST"

echo "Installed $LABEL → runs Mondays 13:00 local (4h sau cs-weekly)."
echo "  plist (source): $SRC"
echo "  symlink:        $DEST"
echo "  log:            /tmp/ceo-weekly.log"
echo
echo "Test now without waiting for Monday:"
echo "  launchctl start $LABEL"
echo "  # or run the script directly:"
echo "  bash $HERE/run-weekly.sh"
