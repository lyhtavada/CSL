---
name: emerge
description: Use this skill when Liz says "emerge", "bận nhưng không biết bận gì", "đang nghĩ gì vậy", or wants to find hidden patterns in her thinking. Scans 14 days of conversation history + MEMORY.md to surface recurring themes, unresolved questions, and unexpected connections.
version: 1.0.0
---

# /emerge — Tìm những thứ đang nghĩ nhưng chưa đặt tên

Skill này không tóm tắt — nó tìm patterns ẩn trong cách Liz đang suy nghĩ và làm việc.

## Cách chạy

1. Scan conversation history 14 ngày qua
2. Đọc MEMORY.md
3. Phân tích:
   - Chủ đề nào xuất hiện ≥ 3 lần ở các ngày / context khác nhau?
   - Câu hỏi nào được đặt ra nhưng chưa có câu trả lời rõ ràng?
   - Việc nào Liz nói "để sau" hoặc "xem lại" nhưng chưa bao giờ quay lại?
   - 2 chủ đề nào tưởng không liên quan nhưng thực ra cùng 1 bài toán?
   - Liz đang spend thời gian vào đâu so với những gì thực sự quan trọng?

## Output Format

```
🔮 Emerge Report — {ngày}

## Chủ đề lặp lại
• [chủ đề] — xuất hiện ở [contexts, ngày]

## Câu hỏi chưa trả lời
• [câu hỏi] — lần đầu xuất hiện [ngày], vẫn chưa resolved vì...

## Việc bị treo
• [việc] — nói "để sau" từ [ngày], có nên quyết định dứt điểm không?

## Kết nối ẩn
• [A] ↔ [B] — [tại sao chúng liên quan, insight là gì]

## Một câu hỏi để suy nghĩ
• [1 câu hỏi mở — không cần trả lời ngay]
```

## Notes

- Đây là skill cần reasoning sâu — không rush
- Phần "Kết nối ẩn" là phần quan trọng nhất, dành nhiều thời gian cho nó
- Kết thúc bằng 1 câu hỏi mở, không phải action item — mục tiêu là spark thinking
- Dùng tiếng Việt
- Chạy khi Liz cảm thấy "bận nhưng không rõ bận gì" hoặc cần suy nghĩ sâu về hướng đi
