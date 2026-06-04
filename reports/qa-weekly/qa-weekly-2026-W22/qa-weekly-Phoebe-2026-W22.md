# QA Tuần 2026-W22 — Phoebe
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 83/100 — Tốt  
**Đã QA:** 24 chat  
**3 trục:** 🧠 Mindset 27.5/34 · 📚 Kiến thức 27.9/33 · 🛠️ Xử lý 27.1/33

## 📝 Nhận xét chung
Tuần này bạn thể hiện phong cách làm việc đều tay, ổn định ở hầu hết các chat — đặc biệt nổi bật ở những case phức tạp (Chat #1 Richpanel + human handover, Chat #13 spare parts, Chat #9 proactive chat fix) nơi bạn vừa đọc tình huống nhanh, vừa deliver kết quả cụ thể có screenshot/link. Mindset ownership tốt: bạn không bỏ lửng, theo đuổi case tới khi xong và chủ động cập nhật khách kể cả khi chưa có solution cuối cùng. Điểm cần tập trung: ở một số chat bạn chưa nắm đúng yêu cầu khách ngay lần đầu (Chat #11: hỏi về email notification nhưng tư vấn về pre-chat form data; Chat #10: khách paste URL + FAQ content nhưng bạn hỏi URL lại nhiều lần) — kiểu hiểu lệch này làm khách phải giải thích lại, kéo dài chat không cần thiết và giảm trust. Thêm vào đó, một số chat ngắn (Chat #24, #21) có độ trễ phản hồi dài mà không có thông báo trước cho khách.

## ✅ Điểm tốt
- **[P1]** Ownership tốt — theo đuổi case tới cùng, không bỏ lửng. Ở Chat #1 Phoebe nhận case từ Linda, tóm tắt đầy đủ ngữ cảnh, kiểm tra kỹ scenario vs. After-sales conflict, tạo 2 tickets riêng biệt, và gửi update tổng hợp chi tiết (17:03) dù cuối tuần. Ở Chat #9, sau khi fix xong còn gửi follow-up email xác nhận kết quả có link demo. (#1, #9, #13)
- **[P3]** Chủ động vì khách — trong nhiều chat Phoebe không chỉ giải quyết câu hỏi được hỏi mà còn chủ động phát hiện và fix thêm vấn đề chưa được báo: Chat #4 tự đồng bộ URLs 'In Progress', Chat #7 nhắc khách dùng Test AI mode để tiết kiệm quota, Chat #2 proactively sync products và bật AI knowledge data. (#4, #7, #2)
- **[P2]** Empathy đúng lúc với khách khó — ở Chat #13 khi khách (AGARO) đang chuẩn bị rời app do chi phí, Phoebe sau khi giải quyết xong technical issue thì viết một message retention có dẫn chứng cụ thể (hỏi budget kỳ vọng, chuyển cho Nolan) — thể hiện đặt lợi ích giữ khách lên trên. (#13, #1)
- **[P5]** Trình bày kết quả rõ ràng, có cấu trúc — Chat #1 update tổng hợp lúc 17:03 liệt kê 3 điểm rõ ràng với screenshots/links. Chat #24 trả lời câu hỏi German/English setup bằng 2 bước cụ thể. Khách có thể làm theo ngay không cần hỏi lại. (#1, #24, #21)

## 🔧 Cần cải thiện
- **[KN5 · Moderate]** Hiểu lệch yêu cầu khách trước khi tư vấn — tư vấn sai trọng tâm, khách phải giải thích lại, kéo dài chat và giảm trust.
  - *Dẫn chứng:* Chat #11: Khách hỏi 'I noticed that chatty isnt sending us any query form filled by customer to our emails' (muốn nhận email khi có form submission). Phoebe trả lời về pre-chat form data đồng bộ vào Inbox: 'the pre-chat 
  - → Trước khi tư vấn, đọc lại toàn bộ câu hỏi và xác định: khách đang gặp vấn đề gì, họ muốn outcome gì? Nếu không chắc thì hỏi 1 câu confirm ngắn trước ('Để chắc mình hiểu đúng — bạn muốn nhận email notification mỗi khi AI xử lý xong form phải không?') thay vì tư vấn luôn.
- **[KN2 · Low]** Hỏi lại thông tin khách đã cung cấp, gây cảm giác không theo dõi conversation.
  - *Dẫn chứng:* Chat #10: Khách vừa paste toàn bộ nội dung About Us + FAQ và nói 'I pasted about us and FAQ for the 404 page FAQ'. Phoebe trả lời: 'Could you please help me to take a screenshot so that I can preview it better?' — khách 
  - → Trước khi hỏi thêm, scroll lên đọc lại 5-7 message gần nhất của khách. Chỉ hỏi thêm khi thực sự thiếu thông tin, không hỏi lại những gì đã có trong chat.
- **[QT18 · Low]** Một số chat Phoebe disappear trong thời gian dài mà không thông báo rõ cho khách, hoặc kết thúc phần tham gia mà không chốt rõ step tiếp theo.
  - *Dẫn chứng:* Chat #24: Phoebe greet lúc 15:17, rồi im đến 16:47 (90 phút) mới trả lời, không có message 'để mình kiểm tra' trong khoảng đó. Chat #15: Phoebe hỏi screenshot lúc 14:46 rồi chat dừng hẳn ở phía Phoebe — không rõ có resol
  - → Nếu cần thời gian kiểm tra >10 phút, gửi một message ngắn 'Để mình kiểm tra, khoảng X phút sẽ có kết quả nhé!' Khi kết thúc phần xử lý của mình trong một chat dài, luôn confirm bước tiếp theo cho khách hoặc báo rõ ai sẽ follow up.
- **[KN6 · Low]** Một lần kết luận chưa đủ thông tin, đặt câu hỏi vòng vòng thay vì đọc context sẵn có.
  - *Dẫn chứng:* Chat #18 (MUS): Khách hỏi về 'idioma y descripción acorde a nuestro mercado uruguayo'. Phoebe hỏi lại: '¿Podría por favor indicarme si desea mostrar el chatbox en Uruguay?' — quá rộng và không đúng trọng tâm. Sau đó tiếp
  - → Khi khách nhắc đến country/market cụ thể, ngay lập tức map sang ngôn ngữ và confirm 1 câu: 'Bạn muốn chatbox hiển thị bằng tiếng Tây Ban Nha cho thị trường Uruguay đúng không?' Không cần hỏi từng step riêng lẻ.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.