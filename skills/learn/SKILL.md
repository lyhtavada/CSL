---
name: learn
description: Use this skill when Liz says "/learn", "note vào learning log", "ghi learning", or pastes something she just learned and wants saved to her personal learning log. Saves to ~/CSL/learnings/ (Liz's personal knowledge journal, separate from Betty's MEMORY.md).
version: 1.0.0
---

# /learn — Ghi vào Learning Log

Lưu nhanh một kiến thức Liz tự học được vào nhật ký cá nhân `~/CSL/learnings/`.

Đây là learning log CỦA LIZ — tách riêng khỏi `MEMORY.md` (của Betty) và `kb/` (nghiệp vụ chính thức).

## Cách chạy

1. Lấy nội dung Liz đưa (sau `/learn` hoặc tin nhắn kèm theo).
2. Nếu nội dung quá ngắn/mơ hồ, tự suy luận tiêu đề + tags từ context conversation. KHÔNG hỏi lại trừ khi thực sự không hiểu.
3. Tạo file mới: `~/CSL/learnings/YYYY-MM-DD-slug.md` (slug kebab-case từ tiêu đề, dùng today's date).
4. Điền theo template bên dưới. Mục nào Liz không nói rõ thì tự điền ngắn gọn từ context, hoặc để `—`.
5. Thêm 1 dòng vào bảng Index trong `~/CSL/learnings/README.md` — **mới nhất lên đầu** (ngay dưới dòng header bảng).
6. Báo lại 1 dòng ngắn: đã lưu vào file nào.

## Template entry

```markdown
---
date: YYYY-MM-DD
tags: [chủ-đề, ...]
---

# {Tiêu đề ngắn}

**Học được gì:** {nội dung chính}

**Bối cảnh / vì sao quan trọng:** {context, hoặc —}

**Áp dụng thế nào:** {action, hoặc —}
```

## Dòng index

`| YYYY-MM-DD | [Tiêu đề](YYYY-MM-DD-slug.md) | tag1, tag2 |`

## Lưu ý

- Mặc định ngắn gọn. Đừng bịa thêm nội dung Liz không nói.
- KHÔNG commit git tự động trừ khi Liz bảo.
- Nếu Liz nói "từ nay luôn..." → đó là quy tắc, vào `CLAUDE.md`, KHÔNG phải learning log.
- Nếu là kiến thức nghiệp vụ sản phẩm/CS → gợi ý đưa vào `kb/` thay vì đây.
