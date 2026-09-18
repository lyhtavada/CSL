#!/bin/bash
# Daily pull for the local Joy source mirror (CSL/joy-src) so Claude never
# reads stale code. Depth-1 shallow repo — pull with --depth 1 to keep it thin.
cd /Users/avada/CSL/joy-src || exit 1
git pull --depth 1 origin master >> /tmp/update_joy_src.log 2>&1
