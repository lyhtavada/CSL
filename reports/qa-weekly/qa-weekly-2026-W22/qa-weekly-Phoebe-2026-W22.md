# QA Tuần 2026-W22 — Phoebe
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 85/100 — Tốt  
**Đã QA:** 24 chat  
**3 trục:** 🧠 Mindset 28.3/34 · 📚 Kiến thức 28.4/33 · 🛠️ Xử lý 28/33

## 📝 Nhận xét chung
Tuần này Phoebe thể hiện phong cách làm việc chắc tay và có trách nhiệm — nổi bật nhất là khả năng tiếp nhận ca bàn giao giữa chừng, nắm bắt context nhanh, và chủ động hoàn thành issue thay vì chờ đợi. Kiến thức sản phẩm Chatty ổn định, không có claim sai nào nghiêm trọng. Điểm cần tập trung: một số thời điểm bạn hỏi lại thông tin khách đã cung cấp (chat #10: khách đã paste toàn bộ nội dung FAQ mà bạn vẫn xin screenshot), hoặc giải thích chưa đúng trọng tâm câu hỏi (chat #11: khách hỏi về form khi transfer sang human, bạn trả lời về pre-chat form) — những lỗi này khiến khách phải giải thích lại, kéo dài chat không cần thiết. Cải thiện bước "xác nhận lại ý khách trước khi trả lời" sẽ đẩy điểm lên rõ rệt.

## ✅ Điểm tốt
- **[P1]** Ownership xuyên suốt ca dài và phức tạp — chat #1 (AlphaInfuse) là ví dụ điển hình: Phoebe tiếp nhận giữa chừng, tổng hợp toàn bộ issue còn tồn đọng, gửi update kỹ thuật chi tiết 3 điểm vào cuối ca, không bỏ sót bất kỳ vấn đề nào. (#1)
- **[P2]** Proactive trên nhiều chat — chủ động sync sản phẩm, bật AI cho khách, re-sync custom knowledge URLs bị stuck mà không cần được yêu cầu. Khách tại chat #4 và #6 đều được hỗ trợ vượt hơn câu hỏi ban đầu. (#2, #4, #6)
- **[P3]** Kiến thức pricing chính xác — xác nhận đúng Basic 50 AI/tháng + $0.40/extra và Free plan 50 lifetime conversations không reset hàng tháng, không có claim nào trái KB. (#2, #3, #7)
- **[P4]** Xử lý đa ngôn ngữ tốt — chat #3 (tiếng Đức), #12 (tiếng Pháp), #18 và #20 (tiếng Tây Ban Nha) đều được phục vụ đúng ngôn ngữ, tone tự nhiên. (#3, #12, #18, #20)

## 🔧 Cần cải thiện
- **[KN2 · Moderate]** Hỏi lại thông tin khách đã cung cấp, khiến khách phải giải thích lần nữa.
  - *Dẫn chứng:* Chat #10 [12:27]: CS (Phoebe): "Could you please help me to take a screenshot so that I can preview it better?" — trong khi khách ở tin nhắn trước đó đã paste toàn bộ nội dung About Us và FAQ với nội dung rõ ràng.
  - → Trước khi xin thêm thông tin, đọc lại các tin nhắn gần nhất của khách. Nếu nội dung đã đủ để xử lý, hãy bắt tay vào giải quyết luôn thay vì xin thêm evidence.
- **[KN5 · Moderate]** Hiểu lệch câu hỏi, tư vấn sai feature ban đầu trước khi được Liz gợi ý điều chỉnh.
  - *Dẫn chứng:* Chat #11 [10:24]: CS (Phoebe): "the pre-chat form requires customers to provide their name and email before they can continue chatting. Please note that this data will automatically sync to the conversation details here.
  - → Khi khách đề cập đến 'query form' hoặc form mà khách điền khi nói chuyện với AI, hãy clarify ngay: đây là pre-chat form hay After-sales/human handover form? Câu hỏi một dòng sẽ tránh được việc giải thích sai hoàn toàn.
- **[KN3 · Low]** Một số tin nhắn briefing/update quá chung chung ở những thời điểm khách đang chờ — không mang thêm thông tin.
  - *Dẫn chứng:* Chat #5 [11:21]: CS (Phoebe): "Hello Anirban, This is Phoebe from Avada, I'm happy to assist you today. Thank you for getting back! Please rest assured that you'll be updated as soon as there's any progress. Have a great
  - → Khi nhảy vào một case đang pending, ít nhất nêu được bước tiếp theo cụ thể: 'Mình đã forward lên Nolan, dự kiến sẽ có update trong X giờ' — dù ngắn nhưng cho khách biết mình đang ở đâu trong quy trình.
- **[KN6 · Low]** Giải thích tính năng hơi vội trong tình huống phức tạp, dẫn đến customer confusion.
  - *Dẫn chứng:* Chat #1 [13:48]: CS (Phoebe): "Yes, with the existing custom scenarios added and with the Human handover, AI should ask for the reason and unassign itself from the conversation" — câu trả lời mơ hồ, không rõ là sẽ ask re
  - → Khi chưa chắc 100% về behavior của một setting combination, hãy nói thẳng: 'Mình đang test thử — sẽ confirm kết quả ngay thay vì đưa ra kết luận trước khi test xong.'

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.