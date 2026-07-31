#!/bin/bash
#
# Install / reinstall the weekly DFY-report (Chatty, leadership) launchd job.
# Symlinks the versioned plist (kept in CSL) into ~/Library/LaunchAgents,
# so the source of truth stays in the repo.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.dfy-weekly-chatty"
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

echo "Installed $LABEL → runs every Friday at 16:30 local."
echo "  plist (source): $SRC"
echo "  symlink:        $DEST"
echo "  log:            /tmp/dfy-weekly-chatty.log"
echo
echo "This job posts the just-finished week's (Fri→Thu) Chatty DFY report straight to"
echo "the CS channel as Liz."
echo
echo "Test now without waiting for Friday:"
echo "  launchctl start $LABEL"
echo "  # or run the script directly:"
echo "  bash $HERE/run-weekly.sh"
