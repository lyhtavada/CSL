#!/bin/bash
# Gen CEO Weekly report (CS Group 2 / Retention — gửi anh Sam).
# Report = TỔNG HỢP 2 bản CS Weekly (Chatty + Joy) trên Notion
# + resolve rate từ cs2.avada.net /api/obs/metrics. Không scan ticket.
#
# CS Weekly (skill /cs-weekly) = team-facing, gửi nhóm CS. CEO Weekly = bản này, gửi Sam.
# Logic trong gen-ceo-weekly.py. Top Issues auto-fill; Response time + CEO decision Liz điền tay.
#
# Chạy:  bash gen-ceo-weekly.sh [--date YYYY-MM-DD]

SCRIPTS_DIR="$(dirname "$0")"
python3 "$SCRIPTS_DIR/gen-ceo-weekly.py" "$@"
