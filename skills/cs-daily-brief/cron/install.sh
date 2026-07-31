#!/bin/bash
#
# Install / reinstall the daily cs-daily-brief launchd job.
# Symlinks the versioned plist (kept in CSL) into ~/Library/LaunchAgents,
# so the source of truth stays in the repo.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.cs-daily-brief"
SRC="$HERE/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

if [[ "${1:-}" == "--remove" ]]; then
  launchctl unload "$DEST" 2>/dev/null || true
  rm -f "$DEST"
  echo "Removed $LABEL."
  exit 0
fi

chmod +x "$HERE/run-cs-daily-brief.sh"

# Reload cleanly if already installed.
launchctl unload "$DEST" 2>/dev/null || true
ln -sf "$SRC" "$DEST"
launchctl load "$DEST"

echo "Installed $LABEL → runs daily 8:45 local (reports on the previous full day)."
echo "  plist (source): $SRC"
echo "  symlink:        $DEST"
echo "  log:            /tmp/cs-daily-brief.log"
echo
echo "Test now without waiting for 8:45:"
echo "  launchctl start $LABEL"
echo "  # or run the script directly:"
echo "  bash $HERE/run-cs-daily-brief.sh"
