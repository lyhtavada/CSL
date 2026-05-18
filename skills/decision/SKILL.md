---
name: decision
description: Use this skill when Liz has just made a decision in conversation and wants to log it, or when asked to "ghi lại quyết định này", "log decision", "lưu lại". Captures the decision, reasoning, trade-offs, and who needs to know — so it doesn't get lost after context compaction.
version: 1.0.0
---

# /decision — Ghi lại quyết định

Capture quyết định vừa ra trong chat thành decision log có cấu trúc.

## Khi nào dùng

- Liz vừa ra quyết định quan trọng trong conversation
- Liz nói "ghi lại", "log cái này", "nhớ quyết định này"
- Cuối một discussion dài có outcome rõ ràng

## Cách chạy

1. Scan conversation hiện tại — identify quyết định vừa được ra
2. Extract: quyết định là gì, context dẫn đến quyết định, các lựa chọn đã cân nhắc, lý do chọn cái này
3. Output decision log
4. Hỏi Liz có muốn lưu vào file không (và gợi ý file phù hợp)

## Output Format

```
## Decision Log — {ngày}

**Quyết định:** [1 câu rõ ràng]

**Context:** [tại sao cần ra quyết định này]

**Các lựa chọn đã cân nhắc:**
- [Option A] — [lý do không chọn]
- [Option B] — [lý do không chọn]
- ✅ [Option được chọn] — [lý do chọn]

**Trade-off chấp nhận:** [cái gì bị đánh đổi]

**Ai cần biết:** [team, cá nhân liên quan]

**Review lại khi:** [trigger hoặc timeline để xem lại quyết định này]
```

## Notes

- Nếu quyết định chưa final, ghi rõ "Pending — chờ [điều kiện]"
- Phần "Review lại khi" quan trọng — quyết định hôm nay có thể sai sau 3 tháng
- Sau khi output, hỏi Liz có muốn append vào file plan liên quan không
- Dùng tiếng Việt
