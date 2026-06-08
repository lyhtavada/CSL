# QA Tuần 2026-W23 — Linda
**Giai đoạn:** 01/06 – 07/06  
**App:** —  
**Điểm:** 80/100 — Tốt (▼ -1 so tuần trước)  
**Đã QA:** 30 chat
**3 trục:** 🧠 Mindset 28.3/34 · 📚 Kiến thức 27.4/33 · 🛠️ Xử lý 24.5/33

## 📝 Nhận xét chung
Tuần này Linda duy trì được phong cách làm việc chủ động và có tâm — sẵn sàng tự test AI trên store, gắn kết theo case dài, và chủ động gợi ý tips ngay cả khi khách không hỏi. Điểm yếu lớn nhất vẫn là lỗi ngữ pháp và chính tả lặp lại qua nhiều chat ("We're very appreciate", "let me done", "double-chẹc", "forr", "expactation", "it work properly to this flow") — đây là lỗi tồn tại từ W22 và chưa có cải thiện rõ rệt, ảnh hưởng trực tiếp đến ấn tượng chuyên nghiệp trong mắt khách. Bạn cần ưu tiên sửa điểm này trước: đọc lại câu trước khi gửi, đặc biệt các tin nhắn xác nhận hoặc tóm tắt case.

## ✅ Điểm tốt
- **[P1]** Chủ động tự test AI thực tế trên store của khách, cung cấp screenshot/video kết quả thay vì chỉ hướng dẫn lý thuyết. Điều này giúp khách thấy rõ vấn đề đang được xử lý và tăng niềm tin vào support. (#1 #4 #14 #15 #18)
- **[P2]** Ownership tốt — không bỏ lửng case giữa chừng, chủ động follow-up sau ca bằng email update, ping lại khi có tin từ dev team. Nhiều case kéo dài nhiều ngày Linda vẫn tiếp tục theo dõi. (#1 #2 #17 #21 #25)
- **[P3]** Chủ động cung cấp mẹo hữu ích ngoài phạm vi câu hỏi ban đầu (Sync Store Page, Review Source, AI re-engage setting, Collection Data toggle) — đúng tinh thần proactive, giúp khách cài đặt tốt hơn mà không cần hỏi thêm. (#2 #3 #5 #10 #14)
- **[P4]** Kiên nhẫn và ổn định tone khi gặp khách khó hoặc case phức tạp kéo dài nhiều issue chồng chất. Không mất bình tĩnh, luôn duy trì thái độ tích cực và chuyên nghiệp. (#1 #4 #6 #21)

## 🔧 Cần cải thiện
- **[KN1 · Moderate]** Lỗi ngữ pháp và chính tả xuất hiện đều đặn qua nhiều chat, giảm tính chuyên nghiệp và uy tín trong mắt khách hàng. Lỗi này đã được ghi nhận từ W22 nhưng chưa cải thiện.
  - *Dẫn chứng:* "We're very appreciate your understand and cooperation" (#1); "let me done a quick test" (#1, #2); "double-chẹc" (#1); "expactation" (#1); "it work properly to this flow" (#2); "Np problem" (#13); "forr" (#1); "Becasue" (#2) (#1 #2 #13)
  - → Trước khi gửi các tin nhắn xác nhận, tóm tắt hoặc câu quan trọng, đọc lại nhanh 5 giây. Ưu tiên sửa các cụm hay mắc: 'appreciate' (không dùng 'We're very appreciate'), 'let me do' (không 'let me done'), 'it works' (không 'it work').
- **[KN5 · Low]** Một số trường hợp hiểu lệch vấn đề ban đầu hoặc tư vấn trước khi confirm đủ thông tin, dẫn đến phải quay lại điều chỉnh.
  - *Dẫn chứng:* Chat #1: Khi khách hỏi "Chattyhatbox looks like this... how can i group these questions" (line 160-163), Linda confirm "you want the FAQ to display only two categories" trong khi khách đã rõ là 3 sections. Phải hỏi lại sau khi khách nói "actually 3 sections, not 2". (#1)
  - → Với các yêu cầu setup có nhiều chi tiết, đọc lại một lần và đặt một câu confirm ngắn gọn trước khi bắt đầu thay đổi. Ví dụ: 'Bạn muốn 3 categories hiển thị trong chatbox, mỗi cái expand khi click, đúng không?'
- **[QT9 · Low]** Một số trường hợp hỏi lại thông tin mà khách đã cung cấp hoặc hỏi thiếu trọng tâm, làm dài thêm chat không cần thiết.
  - *Dẫn chứng:* Chat #4: Khách đã nói rõ muốn AI chỉ trả lời dựa trên dữ liệu website và không tự thêm thông tin, nhưng Linda hỏi "Could you share some common customer questions or scenarios" (line 1094) sau khi khách đã mô tả ví dụ cụ thể ngay trước đó. (#4)
  - → Trước khi hỏi thêm, đọc lại 2-3 tin nhắn gần nhất của khách. Nếu cần clarify, gộp tất cả vào 1 câu hỏi thay vì hỏi từng cái.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin review ở **5/8** chat phù hợp (3 đúng lúc, 0 chưa đúng lúc).
- Linda đã xin review ở 5/8 chat phù hợp (khách hài lòng, chưa có review). Đáng khen là timing tốt ở #3, #10, #14 — xin đúng lúc khách vừa confirm xong. Bỏ lỡ ở #6 (kết thúc ca mà không xin), #7 (khách đang setup chưa xong). Không có trường hợp xin sai lúc. Tiếp tục duy trì nhé.

## 📈 So tuần trước
Điểm tuần này 80, giảm nhẹ 1 điểm so với W22 (81). KN1 (lỗi ngữ pháp/chính tả) vẫn lặp lại và chưa cải thiện — đây là lỗi cần ưu tiên sửa ngay vì đã xuất hiện 2 tuần liên tiếp. KN5 (hiểu lệch yêu cầu) giảm rõ so với W22 — tiến bộ tốt. QT18 (chốt bước tiếp theo) từ W22 đã cải thiện, không còn xuất hiện nhiều tuần này. QT9 (hỏi vòng vo) vẫn xuất hiện nhẹ ở một vài chat nhưng ít hơn W22.
