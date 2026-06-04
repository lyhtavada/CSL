# QA Tuần 2026-W22 — Andy
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 84/100 — Đạt  
**Đã QA:** 9 chat  
**Phân bố:** 🌟1 ✅7 🟡0 🟠1 🔴0 ⛔0

## 📝 Nhận xét chung
Tuần này bạn xử lý vững, tone với khách ổn định và thái độ hỗ trợ thật sự. Điểm mạnh rõ nhất là khả năng đọc context và linh hoạt ngôn ngữ — chuyển sang tiếng Pháp khi khách khó hiểu tiếng Anh là điểm cộng thực sự, không phải kỹ năng ai cũng làm được. Tuy nhiên, khi khách yêu cầu ví dụ cụ thể hoặc giải thích rõ hơn về một metric (chat #6 — FCR 75%), bạn lặp lại "That is the current logic at the moment" ba lần mà không có ví dụ hay giải thích thêm — khách nói thẳng "I am confused" nhưng vẫn không được giải đáp. Đây là lỗi giao tiếp thực sự: câu trả lời chung chung trong khi khách cần con số cụ thể, dẫn đến khách bỏ cuộc thay vì hiểu. Tuần tới, khi khách hỏi "why" hoặc "can you give me an example" — đó là tín hiệu cần dừng lại và giải thích cụ thể hơn, không nên lặp cùng một câu.

## ✅ Điểm tốt
- **[P5]** Chat #3 (Blumia Lab): Bạn chủ động hỏi xác nhận thị trường mục tiêu trước khi tư vấn ('Aux francophones uniquement?'), sau đó chuyển sang hỗ trợ hoàn toàn bằng tiếng Pháp khi khách gặp khó khăn với tiếng Anh. Đây là đọc context rõ ràng và hành động kịp thời — khách kết thúc chat với '你êtes top'. (#3)
- **[P2]** Chat #1 (HotTubs24): Bạn chủ động phát hiện cài đặt notification của khách chỉ chọn 'assigned conversations' và gợi ý bật 'unassigned conversations' trước khi khách hỏi — đúng thứ khách cần. (#1)
- **[P4]** Chat #4 (Clendo) và Chat #9 (AlphaInfuse): Xử lý gọn, đúng trọng tâm, không vòng vo. Chat #9 đặc biệt ngắn gọn và đủ — giải thích auto-resolve + Resolved tab đúng ngay lần đầu. (#4, #9)

## 🔧 Cần cải thiện
- **[KN3 · Moderate]** Giải thích metric FCR 75% lặp đi lặp lại mà không có ví dụ cụ thể, khiến khách nói thẳng là bị confused nhưng vẫn không được làm rõ.
  - *Dẫn chứng:* CS (Andy): 'That is the current logic at the moment.' (lặp lại 3 lần tại [05:52:42], [06:05:04], [10:17:39]). Customer (Xtra Store): 'I am confused with the rate 75%'
  - → Khi khách nói 'confused' hoặc hỏi 'why' lần hai — đó là tín hiệu phải dừng và cho ví dụ số cụ thể. Ví dụ: 'Nếu bạn có 100 chat, sort theo FRT từ nhanh nhất, hệ thống lấy 75 chat đầu để tính trung bình — 25 chat chậm nhất bị loại ra.' Một dòng ví dụ như vậy sẽ cắt đứt vòng lặp.
- **[KN7 · Moderate]** Khi khách hỏi cho ví dụ về FCR, Andy trả lời vague thay vì cung cấp ví dụ số cụ thể theo yêu cầu.
  - *Dẫn chứng:* Customer (Xtra Store): 'sorry, could you please give me example?' — CS (Andy): 'Unfortunately we don't have the example available at the moment' [05:54:16]
  - → Khi KB hoặc logic có thể xây dựng ví dụ số được, không nên từ chối. Tự tạo ví dụ giả định để minh họa logic ('Giả sử bạn có 100 chat và FRT của chúng là...') — không cần dữ liệu thật của khách.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.