---
name: plan-update
description: Use this skill when Liz says "update vào file", "cập nhật plan", or after a discussion that produced decisions/changes that need to be reflected in existing plan files. Scans current conversation, identifies what changed, and proposes file updates before making changes.
version: 1.0.0
---

# /plan-update — Cập nhật plan từ conversation

Scan conversation hiện tại → identify những gì cần update → đề xuất changes → Liz confirm trước khi edit.

## Cách chạy

1. Scan conversation hiện tại — tìm:
   - Quyết định mới được ra
   - Thông tin bổ sung / đính chính so với plan cũ
   - Việc đã hoàn thành cần mark done
   - Hướng đi thay đổi so với plan ban đầu
2. Identify file nào bị ảnh hưởng (trong `playbooks/`, `kb/`, hoặc file khác)
3. Đề xuất changes cụ thể — không edit ngay
4. Chờ Liz confirm rồi mới update

## Output Format (trước khi edit)

```
Mình thấy conversation này có mấy thay đổi cần update:

**File: [tên file]**
- [Dòng/section cũ] → [thay thế bằng gì]
- [Thêm mới: nội dung gì, vào đâu]
- [Xóa: nội dung nào không còn đúng]

Confirm thì mình update luôn nhé?
```

## Notes

- Luôn đề xuất trước, không edit ngay — Liz cần review
- Nếu có nhiều file bị ảnh hưởng, list hết ra để Liz chọn update cái nào
- Ưu tiên accuracy hơn completeness — nếu không chắc thì hỏi
- Sau khi update xong, tóm tắt ngắn những gì đã thay đổi
