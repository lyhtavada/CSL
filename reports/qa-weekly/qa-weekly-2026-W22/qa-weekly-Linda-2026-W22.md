# QA Tuần 2026-W22 — Linda
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 81/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 27.1/34 · 📚 Kiến thức 28.5/33 · 🛠️ Xử lý 25.7/33

## 📝 Nhận xét chung
Tuần này bạn thể hiện phong cách làm việc chủ động và có tâm — sẵn sàng đào sâu vào case phức tạp, test AI thực tế thay vì chỉ hướng dẫn lý thuyết, và không bỏ lửng khi khách hàng chưa xong. Đây là điểm mạnh thật sự và nhất quán qua nhiều chat. Điểm yếu rõ nhất là ngôn ngữ: lỗi ngữ pháp/chính tả xuất hiện khá đều đặn ("We're very appreciate", "let me done a quick test", "double-chẹc", "forr", "jusst", "expactation") — dù không gây hiểu nhầm nghiêm trọng, nhưng khi gặp hàng loạt như vậy trong một chat, khách sẽ cảm nhận được sự thiếu chau chuốt và điều đó ảnh hưởng đến uy tín chuyên nghiệp. Cần tập trung sửa ngay: đọc lại trước khi gửi, đặc biệt các câu xác nhận hoặc tóm tắt quan trọng.

## ✅ Điểm tốt
- **[P1]** Chủ động tự test AI thực tế trên store của khách và cung cấp screenshot/video kết quả, thay vì chỉ hướng dẫn lý thuyết. Điều này giúp khách thấy rõ vấn đề được xử lý và tăng niềm tin vào support. (#1, #10, #16, #25)
- **[P2]** Ownership tốt — không bỏ lửng case giữa chừng, chủ động follow-up sau ca (gửi email cập nhật kết quả, ping lại khi có tin mới từ dev team). Nhiều case kéo dài nhiều ngày Linda vẫn tiếp tục theo dõi. (#4, #21, #23, #25)
- **[P3]** Chủ động cung cấp mẹo hữu ích ngoài phạm vi câu hỏi ban đầu (Sync Store Page, Review Source, AI re-engage setting) — đúng tinh thần proactive, giúp khách cài đặt tốt hơn mà không cần hỏi thêm. (#2, #3, #5, #9)
- **[P4]** Kiên nhẫn với những khách hàng khó tính hoặc chat rất dài với nhiều vấn đề chồng chất (AlphaInfuse nhiều issues liên tiếp, MoreShopping phàn nàn về giá). Không mất bình tĩnh, luôn duy trì tone tích cực. (#1, #12)

## 🔧 Cần cải thiện
- **[KN1 · Moderate]** Lỗi ngữ pháp và chính tả xuất hiện đều đặn trong nhiều chat, giảm tính chuyên nghiệp của phản hồi.
  - *Dẫn chứng:* "We're very appreciate your understand and cooperation" (chat #1); "let me done a quick test" (chat #1, #10); "double-chẹc" (chat #1); "Thanks for informations" (chat #3); "expactation" (chat #1); "I already test the AI 
  - → Trước khi gửi các tin nhắn xác nhận hoặc tóm tắt quan trọng, đọc lại nhanh 5 giây để bắt lỗi. Ưu tiên sửa các cụm hay mắc: 'appreciate' (không dùng 'We're very appreciate'), 'it works' (không 'it work'), 'let me do' (không 'let me done').
- **[KN5 · Moderate]** Một số trường hợp hiểu lệch yêu cầu khách, dẫn đến tư vấn sai hướng trước khi điều chỉnh lại.
  - *Dẫn chứng:* Chat #17: Khách hỏi về lazy loading (chỉ muốn biết có cấu hình được không), Linda ban đầu xử lý như là một bug report và escalate lên tech team. Phải mất thêm 2 tin nhắn mới hiểu đúng yêu cầu.
  - → Với các câu hỏi kỹ thuật ngắn gọn, đọc lại một lần trước khi trả lời để xác định đây là 'how-to question' hay 'bug report'. Nếu không chắc, hỏi một câu xác nhận ngắn thay vì escalate ngay.
- **[QT9 · Low]** Một số trường hợp hỏi lại thông tin khách đã cung cấp hoặc vòng vo khi tìm ID/link conversation, kéo dài chat không cần thiết.
  - *Dẫn chứng:* Chat #3: Khách gửi link session nhưng Linda hỏi lại "May I ask the name or the ID of that convo" và sau đó hỏi lại store URL — dù thông tin đã có trong chat context hoặc CRM.
  - → Trước khi hỏi khách thêm, kiểm tra context chat và CRM một lần. Nếu cần hỏi, gộp thành một câu duy nhất ('Bạn có thể chia sẻ tên chat và store URL không?' thay vì hỏi từng cái).
- **[QT18 · Low]** Một số chat ngắn kết thúc mà không có chốt rõ bước tiếp theo hoặc offer hỗ trợ thêm, đặc biệt với các case mà vấn đề chưa được confirm hoàn toàn.
  - *Dẫn chứng:* Chat #30: Khách hỏi về chargeback process, Linda hỏi clarifying question nhưng chat kết thúc ở đó mà không có follow-up sau khi khách offline.
  - → Với các case đang chờ khách phản hồi, để lại một tin nhắn chốt rõ: 'Mình sẽ chờ câu trả lời từ bạn để tiếp tục xử lý. Nếu bạn offline, mình sẽ gửi update qua email [email].'

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh