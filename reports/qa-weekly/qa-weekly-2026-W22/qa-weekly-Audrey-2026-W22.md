# QA Tuần 2026-W22 — Audrey
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 83/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 27.4/34 · 📚 Kiến thức 28.7/33 · 🛠️ Xử lý 27.3/33

## 📝 Nhận xét chung
Tuần này bạn xử lý tốt và đều tay — tone ấm, ownership cao trên các case kéo dài nhiều ngày (KOSPET migration, Klairs launch), và mindset chủ động nổi bật qua việc tự phát hiện UI conflicts mà khách chưa kịp hỏi. Điểm yếu cần tập trung: một số chat bạn xuất phát không chắc — hỏi lại thứ không cần thiết hoặc confirm sai store trước khi đọc kỹ context, khiến khách phải sửa lại và chat bị kéo dài thêm vài vòng. Ngoài ra, khi gặp câu hỏi hơi mơ hồ, phản xạ "không chắc tôi hiểu đúng" mà không thử tự tóm tắt trước làm giảm cảm giác confident của bạn với khách. Hướng ưu tiên: đọc kỹ context và intent trước khi reply — xác nhận store/issue bằng cách tóm tắt hiểu của bạn thay vì hỏi ngược lại khi chưa cần thiết.

## ✅ Điểm tốt
- **[P3]** Chủ động phát hiện UI conflict mà khách chưa đề cập: tự nhận thấy loyalty button bị che bởi gift button (chat #3), icon hiển thị đè lên sticky add-to-cart (chat #9), và widget bị che bởi floating cart (chat #11) — đề xuất và fix ngay trong cùng session. (#3, #9, #11)
- **[P2]** Ownership mạnh trên case đa ngày: theo sát KOSPET VIP migration qua nhiều lần trao đổi cho đến khi customer xác nhận điểm đã đúng (chat #2), và điều phối reset điểm + go-live cho Klairs đúng deadline (chat #18). (#2, #18)
- **[P1]** Khi đã xác định đúng vấn đề, xử lý gọn và nhanh: phát hiện setting 'Display after login' gây widget ẩn và fix ngay (chat #15), giải thích SPF record step-by-step rồi tự test email thành công (chat #8), và xác định đúng root cause của referral block bị ẩn do tag restriction (chat #28). (#15, #8, #28)

## 🔧 Cần cải thiện
- **[KN6 · Moderate]** Kết luận/assume sai trước khi đọc kỹ context, khiến khách phải đính chính lại nhiều lần.
  - *Dẫn chứng:* Chat #1: 'Ah, asumo que te gustaría cambiar el enlace de inicio de sesión para este sitio web https://aguascalientes-travel.myshopify.com/password' — trong khi khách đang nói về nekane.mx, một store khác hoàn toàn. Khách
  - → Trước khi đưa ra action item, tóm tắt lại hiểu của bạn bằng 1 câu ('Bạn muốn đổi link button trên store nekane.mx, đúng không?') thay vì tự suy và assume luôn — giúp tiết kiệm ít nhất 2-3 tin qua lại.
- **[QT22 · Low]** Phản hồi không theo đúng thứ tự câu hỏi — khách hỏi về notification nhưng bạn chuyển sang hướng dẫn AI training trước, khiến khách bị lạc.
  - *Dẫn chứng:* Chat #12: Khách hỏi 'what should I check to activate chat from my mobile including receiving notification.' Audrey trả lời bằng hướng dẫn AI training ('To effectively train your AI agent...') thay vì ưu tiên answer câu n
  - → Khi khách có nhiều câu hỏi, đánh số và trả lời theo thứ tự ưu tiên của khách — notification cấp bách hơn AI training, nên xử lý trước.
- **[KN2 · Low]** Hỏi lại thông tin không cần thiết khi đã có đủ context để guide trực tiếp.
  - *Dẫn chứng:* Chat #21: Audrey hỏi 'Could you please confirm if this is your website URL https://bf1665-81.myshopify.com?' để confirm store trước khi guide — nhưng khách chỉ hỏi cách setup AI agent, không cần truy cập store. Liz phải 
  - → Với các câu hỏi how-to chung (cách setup, cách train AI), guide thẳng theo UI flow mà không cần confirm store trước — chỉ hỏi store URL khi cần kiểm tra trực tiếp trên store.
- **[KN3 · Low]** Đưa ra câu trả lời mập mờ cho câu hỏi kỹ thuật cụ thể, sau đó nhường cho người khác trả lời rõ hơn.
  - *Dẫn chứng:* Chat #27: Audrey viết 'I'd like to inform you that deleting and recreating a milestone program will not reset your customers' historical purchase data. Joy reviews the customer's history in your store to determine whethe
  - → Khi trả lời về milestone/tier logic, luôn đề cập đến ảnh hưởng của start date: nếu có start date thì chỉ tính purchases từ ngày đó — đây là điểm mấu chốt khách hay hiểu nhầm nhất.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh