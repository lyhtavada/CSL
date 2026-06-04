# QA Tuần 2026-W22 — Hazel
**26/05 – 01/06** · **86/100 — Tốt** · 21 chat
Phân bố: 🌟3 ✅16 🟡0 🟠2 🔴0 ⛔1

## ✅ Điểm tốt
- [P2] Chủ động đề xuất giải pháp/cảnh báo trước khi KH kịp hỏi — gợi ý welcome message rõ ràng hơn, chủ động giải thích vì sao không nhận noti cho hội thoại AI handle. (chat #1, chat #13, chat #6)
- [P3] Giải thích có bước, có ảnh minh hoạ, KH làm theo được ngay — hướng dẫn metafield, JSON-LD, custom màu rất gọn gàng. (chat #20, chat #15, chat #9)
- [P5] Đọc kỹ context khi nhận ca giữa chừng, không bắt KH lặp lại — luôn xin một nhịp để đọc tin nhắn trước rồi mới trả lời ('Please give me a moment to review the previous messages first'). (chat #11, chat #14, chat #5)
- [P1] Tone ấm, lịch sự, trấn an đúng lúc khi KH gặp vấn đề — xin lỗi chân thành về sự bất tiện và cam kết theo dõi tiếp. (chat #5, chat #7)

## 🔧 Cần cải thiện
- [KT2·Critical] iOS không nhận push notification: KB ghi rõ Chatty là PWA, trên iOS bắt buộc dùng Safari (Chrome/Firefox iOS không cài được PWA có push). Trong chat KH dùng iPhone + Chrome theo gợi ý ca trước, nhưng mình troubleshoot vòng quanh Settings/Notifications nhiều lượt mà chưa từng nêu yêu cầu Safari — đây là điểm KB đã có sẵn câu trả lời.
  - DC: [08:00:30] CS (Hazel): Bạn tìm trong 2 nút này xem có lựa chọn nào là Thêm vào màn hình chính không nha / [15:24:23] CS (Hazel): nếu tiện bạn có thể giúp mình xóa Chatty trên điện 
  - → Với case noti mobile + iPhone: hỏi ngay browser đang dùng. Nếu là Chrome/Firefox trên iOS, hướng dẫn KH cài lại PWA qua Safari (Share → Add to Home Screen) trước khi đi sâu vào Settings — KB case_notification-issues ghi rõ điểm này, check trước sẽ cắt ngắn được nhiều vòng.
- [KN5·Moderate] Hiểu nhầm ý KH về trial trong một nhịp: KH lo trial sắp hết hạn (còn 3 ngày) thì mình lại trấn an 'cứ từ từ, test bất cứ lúc nào' — chưa nắm đúng mối lo bị charge. Sau đó mình tự nhận ra và sửa lại, nhưng KH đã phải nhắc lại 2 lần.
  - DC: [12:56:09] CS (Hazel): Ah, yes. Take your time / [12:56:57] No rush at all. Our support team is available 24/7 ... → [13:00:06] Ah, I misunderstood your point earlier. Regarding ex
  - → Khi KH nhắc đến trial/billing, confirm lại ý trước khi trấn an: 'Ý bạn là muốn gia hạn trial để tránh bị charge đúng không ạ?' — tránh trả lời lệch khiến KH phải lặp lại.
- [QT18·Moderate] Để khoảng trống lâu khi đang soạn câu trả lời dài, không rep tạm một câu nên KH dễ tưởng mình off (leader đã nhắc ngay trong chat).
  - DC: [15:19:33] CS (Liz Allen): Em cứ rep nhanh trc 1 câu nhé, ko để khoảng trống như vậy, kh lại tưởng mình off mất / [15:18:31] CS (Hazel Pham): e đang soạn văn ạ
  - → Khi cần soạn câu trả lời dài, nhắn trước một câu giữ nhịp: 'Mình đang tổng hợp đầy đủ cho bạn, chờ mình 2-3 phút nha' — KH sẽ biết mình vẫn online.