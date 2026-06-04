# QA Tuần 2026-W22 — Sonny
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 76/100 — Đạt  
**Đã QA:** 30 chat  
**Phân bố:** 🌟2 ✅26 🟡1 🟠0 🔴1 ⛔0

## 📝 Nhận xét chung
Tuần này bạn xử lý tốt về chiều rộng — 30 chat, đa ngôn ngữ (tiếng Tây Ban Nha, Pháp, Đức, Trung, Serbia), tất cả đều được tiếp nhận và xử lý không bỏ sót. Điểm mạnh rõ nhất là khả năng chủ động: thường xuyên follow-up bằng email, offer free widget setup, đưa ra giải pháp trước khi khách hỏi. Tuy nhiên, có một sự cố nghiêm trọng ở chat #10: khi customize widget preview, bạn vô tình ghi đè content fields lên live widget của merchant mà không cảnh báo trước — khách phát hiện label "TREATS" đã thay "REWARDS" trên live store và hỏi "ai đã làm điều này." Bạn thừa nhận "I wasn't aware that the content is updated as well" — đây là hậu quả của việc thực hiện thao tác kỹ thuật mà không kiểm tra rõ scope tác động, gây mất tin tưởng với khách hàng đang dùng live store. Ngoài ra, ở chat #3, tin nhắn "I am I could clarify" là lỗi ngữ pháp đáng chú ý. Hướng cần tập trung: trước khi thực hiện bất kỳ thao tác customize nào (widget, content, theme), luôn xác nhận rõ với khách: thao tác này sẽ ảnh hưởng đến phần nào của store, có tác động live không.

## ✅ Điểm tốt
- **[P2]** Chủ động cao — thường xuyên follow-up bằng email chi tiết sau khi xử lý xong (chat #1, #3, #5, #9, #10, #25), offer free widget setup proactively trước khi khách yêu cầu. Đây là điểm nhấn rõ nhất của Sonny trong tuần. (#1, #3, #5, #9, #10, #25)
- **[P3]** Giải thích rõ ràng có bước — ở chat #4 hướng dẫn sandbox mode + sign-up reward rất rõ ràng, khách follow được ngay. Chat #2 giải thích logic point calculator chính xác và đủ bước. (#4, #2)
- **[P5]** Đọc kỹ context khi tiếp nhận ca — ở chat #13, nhận ra khách đang frustrated với AI bot, ngay lập tức clarify 'I am a real human' và tiếp tục hỗ trợ ấm áp, không để khách phải lặp lại yêu cầu. (#13)
- **[P1]** Empathy rõ ở chat #10 khi phải xử lý sự cố do chính mình gây ra — xin lỗi thẳng thắn và đề nghị revert tất cả thay đổi, không đổ lỗi hệ thống. (#10)

## 🔧 Cần cải thiện
- **[KN5 · High]** Thực hiện thao tác kỹ thuật (widget content customization) mà không kiểm tra scope tác động, dẫn đến ghi đè content trên live store của khách mà không cảnh báo trước.
  - *Dẫn chứng:* [09:23:13] CS (Sonny): 'When I set up the new Unified widget for you, I also customized the texts to improve the on-brand and it applied to the current widget version too as they share the same content fields. So I am so
  - → Trước bất kỳ thao tác customize nào (widget, content, theme), luôn xác nhận rõ với khách: 'Thao tác này sẽ chỉ tác động đến [phần preview/draft theme] — không ảnh hưởng live store cho đến khi bạn approve.' Nếu không chắc scope, test trên demo store trước hoặc hỏi tech team trước khi thao tác.
- **[KN1 · Low]** Lỗi ngữ pháp rõ rệt trong tin nhắn gửi khách hàng.
  - *Dẫn chứng:* [14:11:49] CS (Sonny): 'Great! I am I could clarify' — câu thiếu nghĩa, đọc không ra.
  - → Đọc lại tin nhắn một lần trước khi gửi, đặc biệt với những câu ngắn phản hồi tự nhiên — đây là những câu dễ bị lỗi nhất.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.