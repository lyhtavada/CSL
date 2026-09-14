#!/bin/bash
#
# Install / reinstall the reply-reviews launchd job (Tue + Fri 17:00).
# Symlinks the versioned plist into ~/Library/LaunchAgents.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.reply-reviews"
SRC="$HERE/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl unload "$DEST" 2>/dev/null || true
  rm -f "$DEST"
  echo "Removed $LABEL."
  exit 0
fi

chmod +x "$HERE/run.sh"

launchctl unload "$DEST" 2>/dev/null || true
ln -sf "$SRC" "$DEST"
launchctl load "$DEST"

echo "Installed $LABEL → runs Tue + Fri 17:00 local."
echo "  log: /tmp/reply-reviews.log"
echo "  test now: bash $HERE/run.sh"
