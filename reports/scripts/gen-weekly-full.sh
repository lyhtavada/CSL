#!/bin/bash
# Gen weekly CS Group 2 (Retention) report — tổng hợp 2 bản CS Weekly Notion.
# Giữ tên cũ để tương thích; nay chỉ gọi gen-weekly-report.sh (đã trỏ sang
# gen-team2-weekly.py). Top Issues auto-fill; Response time + CEO decision Liz điền tay.

SCRIPTS_DIR="$(dirname "$0")"
REPORTS_DIR="$SCRIPTS_DIR/../weekly"

bash "$SCRIPTS_DIR/gen-weekly-report.sh" "$@"

echo ""
echo "Done! Latest report:"
ls -t "$REPORTS_DIR/weekly-CSL-report-"*.md 2>/dev/null | head -1
