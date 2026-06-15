#!/bin/bash
#
# Install / reinstall the weekly FAQ-mining launchd job.
# Symlinks the versioned plist (kept in CSL) into ~/Library/LaunchAgents,
# so the source of truth stays in the repo.
#
#   bash install.sh          # install + load
#   bash install.sh --remove # unload + remove symlink
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABEL="com.avada.mine-faqs"
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

echo "Installed $LABEL → runs Mondays 16:00 local (mines previous Mon→Sun week)."
echo "  plist (source): $SRC"
echo "  symlink:        $DEST"
echo "  log:            /tmp/mine-faqs-weekly.log"
echo
echo "Test now without waiting for Monday 16:00:"
echo "  launchctl start $LABEL"
echo "  # or run the script directly:"
echo "  bash $HERE/run-weekly.sh"
