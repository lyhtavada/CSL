# QA Tuần 2026-W22 — Andy
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 84/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 28.3/34 · 📚 Kiến thức 28.2/33 · 🛠️ Xử lý 27.8/33

## 📝 Nhận xét chung
Andy có phong cách làm việc khá nhất quán: warmth thật sự, ownership cao — bạn hiếm khi để khách rơi vào khoảng trống không có người theo dõi. Điểm mạnh nổi bật nhất là khả năng xử lý nhiều kịch bản kỹ thuật phức tạp (Zendesk, FCR metric, pixel disconnect, delay widget, chat history sau downgrade) với độ chính xác tốt và luôn theo đến khi có kết quả. Điểm cần tập trung: một số lần khi khách hỏi sâu ("why 75%?", "it's not logical"), bạn lặp lại câu trả lời cũ hoặc phản hồi hơi cắt đoạn mà không giải thích thêm — điều này làm khách phải hỏi lại hoặc cảm thấy bị bác bỏ. Trục Skill thấp nhất trong 3 trục: một vài chat kết thúc thiếu chốt bước tiếp theo rõ ràng hoặc confirm từ khách, dẫn đến chat lửng.

## ✅ Điểm tốt
- **[P1]** Ownership cao và nhất quán: Andy theo sát đến khi vấn đề được giải quyết, tự động gửi follow-up email sau khi tech team fix xong (chat #1, #14, #18, #29, #30). Không bỏ khách giữa chừng kể cả ca dài. (#1, #14, #18, #29, #30)
- **[P2]** Kiến thức sản phẩm vững: xử lý chính xác nhiều scenario kỹ thuật — chat history sau downgrade (#16), FCR 75% logic (#6), pixel disconnect (#29), AI email-only Pro/Plus (#29), conversation limit logic Free plan (#7, #16). (#6, #16, #29)
- **[P3]** Warmth và relationship-building thật sự: không phải set đặt, khách trong nhiều chat phản hồi tích cực ('You are really good', 'top team', 'you just made my day much better'). Andy tạo được cảm giác khách được chăm sóc cá nhân. (#1, #2, #5, #15)

## 🔧 Cần cải thiện
- **[KN7 · Moderate]** Lặp lại câu trả lời cũ mà không giải thích thêm khi khách tiếp tục hỏi — khách phải hỏi nhiều lần hơn cần thiết.
  - *Dẫn chứng:* Chat #6: Khách hỏi 'why 75% conversations? not all?' → Andy: 'That is the current logic at the moment.' Khách hỏi lại 'how to locate the 75% conversations?' → Andy: 'We shall manually check on each conversations in the I
  - → Khi khách hỏi lý do đằng sau một logic, đừng chỉ nói 'that is the current logic' — thêm 1 câu giải thích tại sao: 'We exclude the slowest 25% to avoid outliers skewing your team's average.' Một câu đủ để khách không cần hỏi lại.
- **[KN3 · Low]** Một số hướng dẫn kỹ thuật thiếu bước chốt 'confirm từ khách' sau khi thực hiện thay đổi — khách không biết mình cần làm gì tiếp theo.
  - *Dẫn chứng:* Chat #8: Andy set up auto-reply setting cho EKA Packaging, nhưng khi khách hỏi lại 'the tests you just sent to me still have no automatic reply' — Andy chỉ nói 'We are double-checking this to ensure the system automatica
  - → Sau mỗi lần thực hiện thay đổi cho khách, luôn kết bằng: 'I just [action]. Could you please refresh and test from your end? Let me know what you see.' Không để khách phải tự đoán.
- **[QT18 · Low]** Một số chat kết thúc mà không có chốt rõ ràng hoặc bước tiếp theo — đặc biệt khi vấn đề chưa 100% giải quyết nhưng khách im.
  - *Dẫn chứng:* Chat #26 (Mama's Desserts): Andy giải thích không thể connect Knowledge Base app, đề xuất CSV import. Khách chỉ respond bằng auto-reply email 2 lần. Andy không gửi thêm message xác nhận hoặc hướng dẫn bước tiếp theo — ch
  - → Khi khách không confirm sau một đề xuất, hãy gửi thêm 1 tin nhắn ngắn: 'Let me know if you'd like me to guide you through the CSV import process. I'm here when you're ready.' Đừng để mở đầu chat lửng.
- **[KN5 · Low]** Một vài lần có xu hướng tư vấn trước khi xác nhận đúng vấn đề — dẫn đến tốn thêm round.
  - *Dẫn chứng:* Chat #1 (line 138): Khi khách giải thích muốn chatbox chỉ embedded dưới product mà không redirect ngay, Andy phản hồi 'It is not logical if you allow your customers to input the questions there and then not direct them t
  - → Với yêu cầu customize hoặc UX không thông thường, hỏi thêm 1 câu để hiểu full context trước khi giải thích: 'Could you help me understand what you'd like to happen after a customer types their question?' Hiểu xong rồi mới tư vấn.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.