#!/bin/bash
#
# Install / reinstall the twice-weekly product-kb-sync DIFF launchd job.
# Symlinks the versioned plist (kept in CSL) into ~/Library/LaunchAgents.
# Source of truth stays in the repo.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
# Run this in a normal Terminal — the permission classifier blocks Claude
# from loading launchd jobs headless.
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.product-kb-sync"
SRC="$HERE/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl unload "$DEST" 2>/dev/null || true
  rm -f "$DEST"
  echo "Removed $LABEL."
  exit 0
fi

chmod +x "$HERE/run-twice-weekly.sh"

launchctl unload "$DEST" 2>/dev/null || true
ln -sf "$SRC" "$DEST"
launchctl load "$DEST"

echo "Installed $LABEL → runs Tue + Fri 10:00 local (diff only, never auto-pushes)."
echo "  plist (source): $SRC"
echo "  symlink:        $DEST"
echo "  log:            /tmp/product-kb-sync.log"
echo
echo "Test now without waiting:"
echo "  launchctl start $LABEL"
echo "  # or run the script directly:"
echo "  bash $HERE/run-twice-weekly.sh"
