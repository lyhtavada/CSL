# Folder `kb/` dùng thế nào

## Nó là gì

`kb/` là **nguồn sự thật** của bạn. Đây là chỗ Claude đi tra khi bạn hỏi về policy, giá, giới hạn gói, quy trình.

Không có `kb/` → nó sẽ **bịa**. Và nó bịa rất tự tin.

## Quy tắc

| Quy tắc | Vì sao |
|---|---|
| File trong `kb/` là **chỉ đọc** | Đây là tài liệu gốc. Sửa lung tung → sai lan ra mọi reply sau đó |
| Chỉ bỏ vào đây thứ **đã được xác nhận đúng** | Rác vào = rác ra |
| Ghi **ngày cập nhật** ở đầu mỗi file | Để biết file nào cũ, cần refresh |
| Một chủ đề = một file | Dễ tìm, dễ cập nhật, nó cũng tra chính xác hơn |

## Nên có những file gì

Bắt đầu với 4 file này, thêm dần theo nhu cầu:

- `tone-and-voice.md` — ✅ đã có sẵn
- `pricing-<app>.md` — bảng giá và giới hạn từng gói
- `refund-policy.md` — quy tắc refund, ai được duyệt, mức nào
- `escalation.md` — khi nào escalate, escalate cho ai

Sau này thêm: `faq-<app>.md`, `known-issues.md`, `integration-<tên>.md`...

## Cách kiểm tra nó có thật sự đọc `kb/` không

Thỉnh thoảng test bằng câu này:

```
Theo file trong kb/, gói Pro của Chatty giới hạn bao nhiêu conversation/tháng?
Trích nguyên câu trong file cho tôi xem.
```

Nếu nó trích được nguyên văn → đang đọc thật.
Nếu nó trả lời chung chung không trích được → nó đang đoán. Kiểm lại file.

## Cập nhật khi nào

- Khi có release mới đổi tính năng / giới hạn
- Khi có thay đổi giá
- Khi phát hiện nó trả lời sai một chủ đề → sửa file `kb/` tương ứng, đừng chỉ sửa từng reply
