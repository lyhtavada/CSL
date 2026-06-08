# QA Tuần 2026-W23 — Hazel
**Giai đoạn:** 01/06 – 07/06  
**App:** Chatty  
**Điểm:** 83/100 — Tốt (▲ +2 so tuần trước)  
**Đã QA:** 30 chat
**3 trục:** 🧠 Mindset 27/34 · 📚 Kiến thức 28/33 · 🛠️ Xử lý 28/33

## 📝 Nhận xét chung
Tuần này bạn ổn định hơn W22 — đặc biệt ownership mạnh, escalate đúng, follow-up email chủ động. Kiến thức kỹ thuật về AI channels, product sync, metafield vẫn giữ vững. Điểm cần sửa ngay: (1) khi làm việc trực tiếp trên store của khách, xác nhận lại yêu cầu trước khi thực hiện — tránh lặp lại lỗi KN5; (2) luôn giữ ngôn ngữ nhất quán với khách, đặc biệt trong chat đa ngôn ngữ dài.

## ✅ Điểm tốt
- **[P2]** Kiến thức kỹ thuật tốt và chính xác — metafield types, AI channel setup, AI training data, product sync limits đều trả lời đúng và rõ ràng. (8 13 21 28 30)
- **[P3]** Ownership mạnh — chủ động nhận case, escalate đúng thời điểm, follow-up qua email chủ động sau khi xử lý xong. (4 8 12 28)
- **[P1]** Đồng cảm với khách hàng khó tính và thể hiện nhẫn nại; luôn xác nhận lại yêu cầu trước khi thực hiện để tránh hiểu nhầm. (10 15 21)

## 🔧 Cần cải thiện
- **[KN3 · moderate]** Chuyển ngôn ngữ lạc — đang hỗ trợ khách bằng tiếng Tây Ban Nha nhưng gửi 1 tin nhắn tiếng Anh mà không nhận ra ngay.
  - *Dẫn chứng:* Chat #28 line: 'I saved it for you. Please help me reload the page and double-check it on your side' — khách đang chat hoàn toàn bằng tiếng Tây Ban Nha, Hazel đột ngột switch sang tiếng Anh. (28)
  - → Trước khi gửi, kiểm tra ngôn ngữ đang dùng có khớp với ngôn ngữ của khách không. Với Crisp live translate: chỉ cần gõ tiếng Anh và bật translate — nhưng nếu reply thủ công thì phải nhất quán.
- **[KN5 · moderate]** Hiểu lệch yêu cầu khách → đưa ra hành động sai — khách muốn element hiển thị rõ hơn, CS lại ẩn nó đi.
  - *Dẫn chứng:* Chat #7: Khách muốn hiện element trên widget, Hazel thực hiện CSS ẩn element thay vì làm nổi bật — không hỏi lại để xác nhận trước khi can thiệp vào store. (7)
  - → Với các yêu cầu customize có thể hiểu theo nhiều hướng, hỏi lại 1 câu xác nhận trước: 'Just to confirm — bạn muốn element này hiển thị rõ hơn, hay ẩn đi?' Đừng assumption.
- **[QT18 · low]** Kết thúc chat mà không có next step rõ ràng — chat quá ngắn, không đủ context để biết vấn đề có được giải quyết hay chưa.
  - *Dẫn chứng:* Chat #18: Toàn bộ Hazel entry chỉ gồm wrap-up message + review ask, không có nội dung xử lý vấn đề được ghi lại — không thể đánh giá resolution. (18)
  - → Trong mỗi chat shift handoff, dù ngắn, cần xác nhận với khách vấn đề đã được giải quyết chưa trước khi đóng hoặc xin review.
- **[QT9 · low]** Hỏi thêm thông tin mà khách đã cung cấp, gây trùng lặp không cần thiết.
  - *Dẫn chứng:* Chat #29 line: 'هل بدأت للتو في استخدام تطبيقنا؟ هل استخدمت روبوتات الدردشة بالذكاء الاصطناعي من أي تطبيقات أخرى من قبل...' — câu hỏi mang tính cá nhân hóa nhưng không liên quan đến vấn đề kỹ thuật khách đang hỏi, có thể khiến khách cảm thấy được thăm dò thay vì được hỗ trợ. (29)
  - → Chỉ hỏi thêm khi thông tin đó thực sự cần để resolve case. Câu hỏi engage nên để sau khi issue đã xong, không đan xen vào giữa luồng hỗ trợ kỹ thuật.
- **[QT22 · low]** Bỏ qua câu hỏi phụ của khách trong cùng một tin nhắn — chỉ trả lời phần chính, không acknowledge phần còn lại.
  - *Dẫn chứng:* Chat #14: Khách hỏi cả về AI training lẫn về giới hạn plan, Hazel chỉ trả lời phần AI training mà không đề cập đến câu hỏi về plan limit. (14)
  - → Khi khách hỏi nhiều thứ trong 1 tin nhắn, đọc kỹ toàn bộ trước khi reply. Nếu cần xử lý từng phần, acknowledge tất cả câu hỏi trước: 'I'll address both questions.'

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin review ở **6/22** chat phù hợp (4 đúng lúc, 2 chưa đúng lúc).
- Chat #5: Hazel hỏi review trong khi issue overlap chưa được resolve hoàn toàn — mistimed. Chat #6: Header 'ĐÃ CÓ review' nhưng Hazel vẫn hỏi — không tính là eligible. Chat #28: Header 'ĐÃ CÓ review', Hazel pivot sang Trustpilot (khác platform) sau khi G2 bị từ chối — borderline acceptable vì context khác nhau, nhưng cần cẩn thận. Chats #1, #8, #11, #12: timing tốt, well-timed.

## 📈 So tuần trước
W22→W23: +2 điểm (81→83). KN3 (ngôn ngữ lạc) đã cải thiện rõ — W22 lỗi tiếng Pháp/Tây Ban Nha nhiều hơn, W23 chỉ còn 1 slip nhỏ ở chat #28. QT18 (không acknowledge kịp) giảm nhưng vẫn còn ở chat #18. KN1 (typo) không còn xuất hiện — fixed. Lỗi mới W23: KN5 (misread request, chat #7), QT9 (unnecessary probing question, chat #29).
