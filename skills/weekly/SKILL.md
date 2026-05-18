---
name: weekly
description: Use this skill when Liz says "weekly review", "tổng kết tuần", "tuần này làm được gì", or wants to review the past week. Scans conversation history 7 days to surface wins, blockers, and next week priorities.
version: 1.0.0
---

# /weekly — Tổng kết tuần

Review tuần vừa qua và gợi ý focus tuần tới.

## Cách chạy

1. Scan conversation history 7 ngày qua — tìm:
   - Quyết định đã ra
   - Việc đã hoàn thành
   - Việc bị stuck hoặc treo
   - Chủ đề nào được nhắc đến nhiều
2. Đọc MEMORY.md để có context dài hạn
3. So sánh: tuần này có tiến triển so với những gì đang track không?

## Output Format

```
📊 Weekly Review — {ngày bắt đầu} → {ngày kết thúc}

## Tuần này làm được gì
• [quyết định, milestone, việc hoàn thành]

## Đang kẹt / chưa xong
• [việc chưa tiến triển hoặc bị block]

## Patterns tuần này
• [xu hướng, chủ đề lặp lại, cách Liz đang allocate thời gian]

## Gợi ý ưu tiên tuần tới
1. ...
2. ...
3. ...
```

## Notes

- Honest hơn là positive — nếu tuần kẹt thì nói thẳng
- Patterns không cần nhiều, 1–2 insight thật sự có giá trị hơn list dài
- Dùng tiếng Việt
