#!/bin/bash
#
# Install/refresh the cs-daily launchd job (runs 09:00 local every day).
# Symlinks the plist into ~/Library/LaunchAgents and (re)loads it.
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLIST="$HERE/com.avada.cs-daily.plist"
LABEL="com.avada.cs-daily"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

chmod +x "$HERE/run-daily.sh"

# Unload any previous version, then symlink + load the current one.
launchctl unload "$DEST" 2>/dev/null || true
ln -sf "$PLIST" "$DEST"
launchctl load "$DEST"

echo "Installed $LABEL → runs daily at 09:00 local."
echo "Manual test:  bash $HERE/run-daily.sh"
echo "Logs:         /tmp/cs-daily.log"
echo "Status:       launchctl list | grep cs-daily"
