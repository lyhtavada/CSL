#!/bin/bash
# Gen weekly CS Group 2 (Retention) report.
# Từ 2026-06-22: report = TỔNG HỢP 2 bản CS Weekly (Chatty + Joy) trên Notion
# + resolve rate từ cs2.avada.net /api/obs/metrics.
# Không còn dựng template rỗng + scan ticket như trước.
#
# Logic nằm trong gen-team2-weekly.py. Top Issues auto-fill từ Notion;
# Response time + CEO decision để Liz điền tay.

SCRIPTS_DIR="$(dirname "$0")"
python3 "$SCRIPTS_DIR/gen-team2-weekly.py" "$@"
