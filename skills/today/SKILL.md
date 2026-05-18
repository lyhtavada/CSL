---
name: today
description: Use this skill when Liz says "today", "plan my day", "hôm nay làm gì", or wants a daily plan. Combines Google Calendar + recent conversation history to prioritize the day.
version: 1.0.0
---

# /today — Kế hoạch ngày

Tạo kế hoạch ngày cho Liz dựa trên lịch và context công việc gần đây.

## Cách chạy

1. Đọc Google Calendar hôm nay (nếu có access)
2. Scan conversation history 2–3 ngày gần nhất — tìm:
   - Việc đang làm dở
   - Quyết định chưa có kết quả
   - Việc Liz nói "để sau", "làm sau", "xem lại sau"
   - Pending items cần follow up
3. Tổng hợp và sắp xếp theo mức ưu tiên

## Output Format

```
📋 Today — {ngày}

📅 Lịch họp:
• [giờ] Tên cuộc họp

🔴 Phải làm hôm nay:
• ...

🟡 Nên làm hôm nay nếu có thể:
• ...

🔁 Đang dở / cần follow up:
• ...

💭 Cần chú ý:
• ...
```

## Notes

- Nếu không có lịch họp thì bỏ phần đó
- Ưu tiên những việc có deadline hoặc đang block người khác lên đầu
- Giữ ngắn — không quá 10 items tổng cộng
- Dùng tiếng Việt
