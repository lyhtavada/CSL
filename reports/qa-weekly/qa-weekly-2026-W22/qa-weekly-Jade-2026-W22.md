# QA Tuần 2026-W22 — Jade
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 84/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 27.6/34 · 📚 Kiến thức 28.7/33 · 🛠️ Xử lý 27.4/33

## 📝 Nhận xét chung
Tuần này bạn thể hiện rõ điểm mạnh ở ownership: tiếp nhận ca handoff mượt, chủ động follow-up kết quả, và xử lý được nhiều loại case phức tạp (Joy POS, Smile.io migration, AI scenario training, Chatty auto-translate bug). Chat 18 (Littolo House) là điểm sáng thật sự — phân tích use case phức tạp ra kế hoạch 2 phase cụ thể cho thấy bạn nắm sản phẩm vững và chịu suy nghĩ thay khách. Điểm cần tập trung nhất là trục Skill: trong một số chat bạn đưa ra câu trả lời chưa chắc mà không báo rõ, hoặc mở câu hỏi xác nhận không cần thiết khi thông tin đã đủ — điều này làm khách phải nhắn thêm và chat kéo dài. Nếu cải thiện được sự gọn gàng trong bước giải thích và confirm thông tin, bạn hoàn toàn có thể lên Xuất sắc.

## ✅ Điểm tốt
- **[P1]** Ownership rõ ràng xuyên suốt nhiều chat: tiếp nhận handoff đúng cách, không để khách chờ không có thông tin, chủ động follow-up kết quả kỹ thuật (chat #7: fix chatty:cart:changed event; chat #22: gửi link screenshot kết quả CSS; chat #30: email chủ động về metafield conflict). (#7, #22, #30)
- **[P2]** Kiến thức sản phẩm vững: phân tích use case cashback 2-phase cho Littolo House (chat #18) chuẩn kỹ thuật, giải thích rõ Rule Engine vs Redeem programs, nêu đúng giới hạn plan. Chat #19 (Joy POS permission) cũng cung cấp hướng dẫn đầy đủ cho cả 2 permission model mà không cần phải tra lại. (#18, #19)
- **[P3]** Chủ động đề xuất thêm giá trị cho khách khi không được hỏi: offer unified widget upgrade tự nhiên trong chat #4, #8, #22; đề xuất Chatty Lab tool trong chat #6; hướng dẫn email notifications sau khi giải quyết xong vấn đề chính trong chat #9. (#4, #8, #22)
- **[P4]** Tone ấm và kiên nhẫn với khách khó — giữ được chuyên nghiệp với AGARO khi merchant tỏ thái độ muốn uninstall (chat #26), và với AWNL Taiwan khi merchant liên tục nói 'please take a look at my previous chat, I dont think you understand my issue' (chat #29). (#26, #29)

## 🔧 Cần cải thiện
- **[KN6 · Moderate]** Kết luận hoặc tư vấn khi chưa hiểu đủ vấn đề — trong chat #21 khách gửi 3 lần 'Please help me fix 404 page' (đây là cụm từ bot trigger của Chatty, không phải mô tả lỗi thật), nhưng Jade trả lời như đây là lỗi app thật: 'You can try reloading the app page many times/ clearing the browser's cache'. Điều này khiến khách không được hướng dẫn đúng.
  - *Dẫn chứng:* CS (Jade): You can try reloading the app page many times/ clearing the browser's cache, and then accessing the Chatty app again to check if the issue can be addressed.
  - → Khi khách lặp đúng một câu nhiều lần mà không bổ sung thông tin, hãy dừng lại và xác nhận ý định thật: 'It looks like this might be a preset trigger phrase — could you tell me specifically which page or section you're having trouble with?' Đừng rush vào giải pháp generic.
- **[QT9 · Moderate]** Hỏi lại thông tin không cần thiết, làm vòng vo flow — chat #13 (POS loyalty pass): Jade hỏi 'Can you kindly share the customer's email' rồi sau đó hỏi tiếp 'May I know where I can access the Loyalty Pass block', dù khách đã cho biết ngay từ đầu họ dùng Apple Wallet Pass và chỉ cần xác nhận quy trình scan. Câu hỏi thứ 2 không cần thiết vì Jade tự tìm được.
  - *Dẫn chứng:* CS (Jade): May I know where I can access the Loyalty Pass block on the website to generate a code on my end? — và ngay sau đó: CS (Jade): Ah I can see it here, no worries
  - → Trước khi hỏi khách thêm thông tin, hãy tự kiểm tra trước trong app/store xem có tìm được không. Nếu tự tìm được thì tự xử lý, chỉ hỏi khi thực sự cần input của khách.
- **[KN3 · Low]** Câu trả lời không rõ ràng khi khách cần hướng dẫn cụ thể — chat #24 (EKA Packaging): khách mô tả rõ 'conversations marked as inactivity have no automatic reply' kèm screenshot. Jade xác nhận AI Agent đang off, nhưng phần giải thích về inactivity vs AI connection không đủ rõ để khách tự làm theo: 'For the inactivity notice, I think it is related to your Automatic resolution setting'  — dùng 'I think' mà không xác nhận, và không dẫn khách vào đúng setting.
  - *Dẫn chứng:* CS (Jade): Yes, it will automatically respond to new messages. For the inactivity notice, I think it is related to your Automatic resolution setting. Can you kindly share with us the conversation ID of the related conver
  - → Khi đã nhìn thấy vấn đề (AI off), dẫn khách thẳng vào giải pháp: 'The AI Agent is currently off — once you turn it on, it will respond to new messages automatically. For the inactivity label, this is triggered by the Auto Resolution setting at Settings > Inbox > Auto Resolution. Would you like me to walk you through both?' Tránh 'I think' và tránh hỏi conversation ID khi chưa cần thiết.
- **[KN1 · Low]** Lỗi ngữ pháp nhỏ trong chat tiếng Anh: 'our all does not have a separate sign up flow' (chat #11) — viết tắt tối nghĩa ('all' thay cho 'app'), có thể gây nhầm lẫn cho khách không phải người bản ngữ.
  - *Dẫn chứng:* CS (Jade): Currently, our all does not have a separate 'sign up' flow for customers to join the loyalty program yet.
  - → Soát lại trước khi gửi tin dài. Câu này nên là: 'Currently, our app does not have a separate sign-up flow for customers to join the loyalty program yet.' Lỗi nhỏ nhưng tích lũy nhiều lần ảnh hưởng đến sự chuyên nghiệp.
- **[KN7 · Low]** Câu trả lời chung chung khi cần cụ thể hơn — chat #25 (AnointDebib): khách hỏi về widget load delay, Jade giải thích đây là expected behavior (widget loads after page) nhưng không đề xuất bất kỳ giải pháp cụ thể nào để giảm cảm giác lag, cũng không commit rõ có escalate không.
  - *Dẫn chứng:* CS (Jade): Regarding the widget appearance, I would like to share that this is currently the expected behavior. The widget is designed to appear only after the page has finished loading completely, which is why it may sh
  - → Khi giải thích 'expected behavior', luôn kèm theo 1 trong 2: (1) bước tiếp theo cụ thể ('Our tech team will check if there's a way to reduce this delay — I've created a ticket'), hoặc (2) workaround thực tế. Đừng để khách cảm giác bị đưa vào ngõ cụt.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh