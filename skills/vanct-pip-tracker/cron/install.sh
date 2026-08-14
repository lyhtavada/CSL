#!/bin/bash
#
# Install / reinstall the weekly VanCT PIP tracker launchd job.
# Symlinks the versioned plist (kept in CSL) into ~/Library/LaunchAgents,
# so the source of truth stays in the repo.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.vanct-pip-tracker-weekly"
SRC="$HERE/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl unload "$DEST" 2>/dev/null || true
  rm -f "$DEST"
  echo "Removed $LABEL."
  exit 0
fi

chmod +x "$HERE/run-weekly.sh"

launchctl unload "$DEST" 2>/dev/null || true
ln -sf "$SRC" "$DEST"
launchctl load "$DEST"

echo "Installed $LABEL → runs every Friday at 09:00 local."
echo "  plist (source): $SRC"
echo "  symlink:        $DEST"
echo "  log:            /tmp/vanct-pip-tracker-weekly.log"
echo
echo "Test now without waiting for Friday:"
echo "  launchctl start $LABEL"
echo "  # or run the script directly:"
echo "  bash $HERE/run-weekly.sh"
