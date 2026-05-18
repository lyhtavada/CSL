#!/bin/bash
# Gen weekly CSL report mỗi thứ 2 lúc 1PM
# Tạo file mới với ngày tuần hiện tại

SCRIPTS_DIR="$(dirname "$0")"
REPORTS_DIR="$SCRIPTS_DIR/../weekly"
DATE=$(date +"%Y-%m-%d")
WEEK=$(date +"%Y-W%V")
OUTPUT="$REPORTS_DIR/weekly-CSL-report-$DATE.md"

# Tính Mon-Sun của tuần trước
LAST_MON=$(date -v-7d -v-mon +"%d/%m")
LAST_SUN=$(date -v-7d -v+sun +"%d/%m/%Y")

cat > "$OUTPUT" << EOF
# CS Group 2 (Retention) — Weekly Report
**Date**: $(date +"%d/%m/%Y") | **Meeting**: Thứ 2, 15:00 | **Prepared by**: Liz
**Gửi trước**: 13:00 cùng ngày (trước meeting 2 tiếng)
**Week**: $WEEK | **Period**: $LAST_MON – $LAST_SUN

---

## TL;DR
- Session:  (↑% so với tuần trước)
- First response time (avg):  (tuần trước: )

---

## Top Issues tuần này

---

## Bad Reviews

🟢 Đã convert
-

🔴 Đang follow up
- 

---

## Alerts

- **[Tên vấn đề]**: [1 câu mô tả + trạng thái]

---

## Team Updates

- [Cập nhật về team]

---

## CSL Projects đang triển khai

**1. [Tên project]**
[1-2 câu cập nhật trạng thái]

**2. [Tên project]**
[1-2 câu cập nhật trạng thái]

---

## CEO Cần Quyết Định *(tối đa 3)*

**1. [Câu hỏi]**
- Context: [1 câu]
- Default nếu không decide: [X]

**2. [Câu hỏi]** *(nếu có)*
- Context: ...
- Default: ...

**3. [Câu hỏi]** *(nếu có)*
- Context: ...
- Default: ...

---

## Appendix *(không cần đọc trước meeting)*
- Breakdown ticket theo app
- Agent workload detail
- Full ticket list nếu cần
EOF

echo "Generated: $OUTPUT"
