#!/bin/bash
# Gen full weekly CSL report:
# 1. Tạo file template (gen-weekly-report.sh)
# 2. Scan Slack và fill vào Top Issues (scan-weekly-issues.py)

SCRIPTS_DIR="$(dirname "$0")"
REPORTS_DIR="$SCRIPTS_DIR/../weekly"

echo "=== Step 1: Generate report template ==="
bash "$REPORTS_DIR/gen-weekly-report.sh"

echo ""
echo "=== Step 2: Fetch Avada Ticket issues ==="
python3 "$SCRIPTS_DIR/scan-weekly-issues.py"

echo ""
echo "Done! Latest report:"
ls -t "$REPORTS_DIR/weekly-CSL-report-"*.md 2>/dev/null | head -1
