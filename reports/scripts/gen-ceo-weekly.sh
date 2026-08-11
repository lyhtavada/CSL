#!/bin/bash
# Gen CEO Weekly report (CS Group 2 / Retention — gửi anh Sam).
# Report = TỔNG HỢP 2 bản CS Weekly (Chatty + Joy) trên Notion
# + AI resolved / CS không phải đụng tay từ cs2.avada.net /api/obs/{metrics,sessions}
# + DFY tuần (ticket/adopt%/review%/install%) fetch live qua fetch_dfy_week.py.
#
# CS Weekly (skill /cs-weekly) = team-facing, gửi nhóm CS. CEO Weekly = bản này, gửi Sam.
# Logic trong gen-ceo-weekly.py. Top Issues auto-fill; Response time + CEO decision Liz điền tay.
#
# Chạy:  bash gen-ceo-weekly.sh [--date YYYY-MM-DD]

SCRIPTS_DIR="$(dirname "$0")"
python3 "$SCRIPTS_DIR/gen-ceo-weekly.py" "$@"
