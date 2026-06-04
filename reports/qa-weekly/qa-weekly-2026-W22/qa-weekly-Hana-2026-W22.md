# QA Tuần 2026-W22 — Hana
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 82/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 27.5/34 · 📚 Kiến thức 27.9/33 · 🛠️ Xử lý 26.9/33

## 📝 Nhận xét chung
Hana có một tuần làm việc ổn định với mindset tích cực và khả năng xử lý nhiều loại case phức tạp trong cả Joy và Chatty — từ setup chuyên sâu (DFY, Klaviyo, sandbox testing, tier/points logic) đến troubleshoot kỹ thuật. Điểm mạnh nổi bật nhất là sự tận tâm và kiên nhẫn với khách khó tính, chủ động đề xuất thêm giải pháp. Điểm cần tập trung: ở những case phức tạp kéo dài, Hana đôi khi không confirm lại đủ rõ vấn đề của khách trước khi tư vấn — dẫn tới khách phải hỏi lại nhiều vòng (rõ nhất ở Chat #12 — khách hỏi về Klaviyo trigger 600 điểm, Hana giải thích vòng quanh milestone/rewards trước khi khách tự giải thích lại). Ngoài ra, skill trình bày ở một số chat ngắn còn ở mức "ổn" chứ chưa đặc biệt rõ — hướng cần tập trung là confirm lại đúng yêu cầu ngay từ đầu và trả lời thẳng vào câu hỏi, tránh để khách phải làm rõ lại nhiều lần.

## ✅ Điểm tốt
- **[P1]** Ownership tốt trên các chat dài và phức tạp: Hana theo đuổi case tới cùng, gửi email follow-up, làm widget/DFY và chủ động báo kết quả khi xong — không đóng lửng. (#1, #3, #5, #7)
- **[P2]** Kiến thức sản phẩm Joy vững: tư vấn chính xác về VIP tier multiplier, Rule Engine migration, referral/points flow, Shopify Flow workaround, store credit vs points. Không có lỗi sai kiến thức nào được xác định. (#5, #7, #22, #30)
- **[P3]** Chủ động vì khách: proactively phát hiện notification chưa bật và offer bật, offer DFY widget styling, đề xuất pre-launch points cho existing customers mà khách chưa hỏi. (#3, #4, #24, #10)
- **[P4]** Empathy tự nhiên, tone ấm với cả khách khó — kiên nhẫn với khách hỏi đi hỏi lại, không mất bình tĩnh khi bị press về thời gian hoàn thành task. (#2, #19, #5)

## 🔧 Cần cải thiện
- **[KN6 · Moderate]** Kết luận và tư vấn trước khi hiểu đúng yêu cầu — khách phải giải thích lại nhiều vòng, kéo dài chat không cần thiết.
  - *Dẫn chứng:* Chat #12: Khách hỏi về Klaviyo trigger khi điểm đạt 600. Hana liên tục giải thích 'Joy: Points Eligible Reward' trigger và milestone reward thay vì xác nhận thẳng rằng trigger 'đúng điểm X' không tồn tại trực tiếp và đề 
  - → Trước khi tư vấn, confirm lại 1 câu rõ ràng: 'Bạn muốn trigger Klaviyo flow thuần túy khi điểm đạt mốc X mà không cần gửi reward đúng không?' — rồi mới trả lời. Nếu feature không có, nói thẳng trước, sau đó mới suggest workaround.
- **[KN3 · Low]** Hướng dẫn đôi khi thiếu bước cụ thể hoặc quá ngắn với tình huống khách chưa quen — khách phải hỏi lại.
  - *Dẫn chứng:* Chat #15: Khi hướng dẫn web-push notification, Hana gửi ảnh setting nhưng khách không tìm thấy option và hỏi lại 'i do not see this option'. Hana mới gửi thêm ảnh thứ hai. Sau đó khách lại hỏi 'how i can check?' sau khi 
  - → Với tính năng technical, nên gửi guide dạng số thứ tự rõ ràng (bước 1, 2, 3) hoặc video thay vì chỉ ảnh screenshot đơn lẻ — đặc biệt khi khách đang trên mobile.
- **[QT22 · Low]** Bỏ sót câu hỏi phụ của khách khi có nhiều request trong một tin nhắn.
  - *Dẫn chứng:* Chat #2: Khách hỏi 'but can't you first help me set it up?' (về Joy Subscription khi app chưa mở được) đồng thời với nhiều yêu cầu khác. Hana đã xử lý từng phần nhưng lúc bàn giao ca không có bản tóm tắt đầy đủ pending i
  - → Khi kết ca trên chat còn nhiều issue pending, để lại 1 dòng tóm tắt rõ trong chat: 'Pending: (1) Joy Subscription app không mở — TS đang xử lý, (2) widget position — đã fix...' Điều này giúp CS tiếp nhận không phải đọc lại toàn bộ.
- **[KN1 · Low]** Một số lỗi nhỏ về typo/ngữ pháp và switch ngôn ngữ đột ngột khi đang chat trong tiếng Tây Ban Nha.
  - *Dẫn chứng:* Chat #1: 'I will check quickly on the earning program setting, allow me a moment' (switch sang English giữa conversation đang dùng tiếng Tây Ban Nha); 'All done. I have changed the program name and launcher lable' (typo:
  - → Double-check tin nhắn trước khi gửi, đặc biệt khi dùng live translate. Duy trì ngôn ngữ nhất quán với ngôn ngữ khách đang dùng trong suốt conversation.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh