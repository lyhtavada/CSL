# QA Tuần 2026-W22 — Hana
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 92/100 — Tốt  
**Đã QA:** 11 chat  
**Phân bố:** 🌟5 ✅6 🟡0 🟠0 🔴0 ⛔0

## 📝 Nhận xét chung
Bạn có một tuần chat chất lượng cao — xử lý chắc tay trên nhiều ngôn ngữ (Tây Ban Nha, Trung, Pháp, Anh), câu hỏi phức tạp về tính năng không làm khó bạn, và bạn chủ động offer DFY + audit setup cho merchant thay vì chỉ trả lời thụ động. Điểm nổi bật nhất là khả năng đọc context sâu — bạn phát hiện referral program đang tắt và tự bật luôn mà không cần merchant hỏi, hay tự scan cả store và đưa ra 3 gợi ý ưu tiên. Hướng cần chú ý tuần tới: khi merchant đã nói rõ "ưu tiên vấn đề X, bỏ qua Y", bạn cần tôn trọng điều đó cho đến hết chat — việc quay lại gợi ý Y làm merchant cảm thấy bạn không thực sự nghe; nếu lặp lại nhiều lần sẽ kéo dài chat vô ích. Ngoài ra, với câu hỏi yes/no đơn giản, hãy trả lời thẳng trước rồi mới hỏi thêm nếu cần — không để merchant phải hỏi lại.

## ✅ Điểm tốt
- **[P2]** Chủ động offer DFY widget service và audit setup store mà không cần merchant hỏi — đề xuất 3 hướng cải thiện loyalty program (loyalty page, referral, account page) sau khi tự review store. (chat #1, chat #3, chat #10)
- **[P3]** Hướng dẫn rõ ràng, có bước cụ thể cho các flow phức tạp: Shopify Flow workaround cho 4th order milestone, VIP tier multiplier setup, point variable explanation. (chat #4, chat #5, chat #7)
- **[P5]** Đọc kỹ context hiện tại trước khi action — tìm được account customer qua email khi search by name không ra, phát hiện referral block đã add nhưng program đang off và tự enable. (chat #3, chat #4)
- **[P1]** Tone ấm, nhất quán trên nhiều ngôn ngữ — giữ được sự kiên nhẫn và thân thiện khi chat kéo dài nhiều giờ với merchant Tây Ban Nha và Trung Quốc. (chat #1, chat #2, chat #5)

## 🔧 Cần cải thiện
- **[QT9 · Moderate]** Tiếp tục offer loyalty page setup sau khi merchant đã nói rõ 'không cần bận tâm cái đó, lo subscription trước'
  - *Dẫn chứng:* [07:50:09] Customer: '这个现在没那么重要 先帮我弄订阅吧' → [07:56:24] CS (Hana): 'I can confirm that you want to setup the Loyalty page, correct?' / [08:03:40] Customer: '现在先不用管这个' → [08:03:40] CS (Hana): 'I understand. We support multi
  - → Khi merchant đã nói skip một topic, đừng gợi lại trong cùng ca — ghi nhớ ưu tiên của merchant và chỉ quay lại nếu họ chủ động hỏi. Việc offer lại làm merchant thấy bạn không nghe, và kéo dài chat không cần thiết.
- **[KN3 · Moderate]** Trả lời vòng vo cho câu hỏi yes/no đơn giản, bắt merchant hỏi lại
  - *Dẫn chứng:* [06:59:26] Customer (Shermaine Wee): 'still have customer account page, right?' → [07:02:57] CS (Hana): 'May I confirm that you refer to the loyalty reward on account page correct?'
  - → Với câu hỏi đóng đơn giản, confirm Yes/No ngay lập tức rồi mới add thêm context nếu cần. Không nên đảo ngược — hỏi lại trước khi trả lời làm merchant phải đợi thêm một vòng không cần thiết.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.