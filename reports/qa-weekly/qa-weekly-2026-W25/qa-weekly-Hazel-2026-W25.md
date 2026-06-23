# QA Tuần 2026-W25 — Hazel (Chatty)
**Tuần 15/06 – 21/06/2026** · coaching, không phải penalty

## 📊 Điểm tuần: 82/100 — Tốt  (▼ -2 so với W24: 84)
🔍 Đã QA: 30 chat

**Breakdown 3 trục:** 🧠 Mindset 26.4/34 · 📚 Kiến thức 28.0/33 · 🛠️ Xử lý 27.2/33  →  trục yếu nhất: **mindset**

## 📝 Nhận xét chung
Hazel tuần này cho thấy nền tảng vững về kỹ thuật và sự kiên nhẫn với các case phức tạp — xử lý đa ngôn ngữ, theo đuổi nhiều phiên trong cùng một chat, và chủ động test lại sau khi dev fix đều là điểm tốt nhất quán. Trục yếu nhất là Mindset: ở các chat ngắn, các trường hợp handoff, hoặc khi issue chưa xử lý xong, bạn có xu hướng dừng ở mức "chuyển cho dev" mà thiếu bước chủ động confirm lại kỳ vọng của KH hay báo rõ bước tiếp theo — hậu quả là KH cảm giác bị bỏ lơ. Chat #15 là ví dụ điển hình: xin review khi issue chưa xong làm mất đi cảm giác chân thành. Kỹ năng xử lý cũng còn một số điểm cần chú ý: trong chat #26 bạn trả lời tiếng Anh khi KH đang viết tiếng Na Uy, buộc KH phải chuyển đổi ngữ cảnh. Tập trung tuần tới: trước khi kết thúc bất kỳ phiên nào, luôn chốt rõ "bước tiếp theo của tôi là X, bạn sẽ nhận update vào lúc Y" — điều đó sẽ đẩy điểm Mindset lên rõ rệt.

## ✅ Điểm tốt
- [P1] Ownership bền bỉ trong các case dài và phức tạp: theo đuổi nhiều phiên, chủ động test lại sau khi dev fix, và follow-up trước khi KH hỏi lại. (#4 #24 #28)
- [P3] Chủ động phát hiện và fix vấn đề KH chưa hỏi đến: tự xem settings, nhận ra Human Handover bị reset do app update và sửa ngay, báo lại KH. (#1 #10)
- [P2] Empathy và nỗ lực cao với KH khó và KH bực: ở chat #4 (KH Nhật yêu cầu phức tạp về AI training) và chat #28 (KH Tây Ban Nha cần tùy chỉnh màu sắc tỉ mỉ), Hazel kiên nhẫn làm đi làm lại đến khi KH hài lòng. (#4 #28)
- [P4] Knowledge tư vấn chính xác, nhất quán qua 30 chat — không có claim sai về giá/tính năng. Giải thích kỹ thuật rõ ràng (Assisted Revenue tracking, Instagram read-status, email forwarding flow). (#13 #14 #25)

## 🔧 Cần cải thiện
- [QT18] (Moderate) Đóng phiên hoặc chuyển ca mà không chốt rõ bước tiếp theo cho KH, khiến KH không biết khi nào sẽ có update. (#18 #19)
   • Dẫn chứng: [10:56:49] CS (Hazel): 'May I ask whether the customer reached out to you during your outside working hours, according to the schedule you've set up?' — sau đó chuyển cho Phoebe không có câu chốt cho KH.
   → Trước khi rời phiên hoặc handoff, luôn gửi 1 câu chốt rõ: 'Mình đã ghi nhận vấn đề X, team sẽ update bạn trong Y giờ. Nếu cần gì thêm cứ nhắn lại.' Không để KH phải tự đoán.
- [QT18] (Moderate) Xin review khi vấn đề chưa được giải quyết xong — tech team vẫn đang làm việc, KH chỉ vừa nói 'Thanks' xã giao. (#15)
   • Dẫn chứng: [09:13:45] CS (Hazel): 'Ah, I can see you've been using Chatty for a period of time, may I ask for a tiny favor?' ... 'Would you mind spending a few moments sharing your feedback...' — trong khi issue vẫn pending với tech team.
   → Chỉ xin review sau khi KH xác nhận vấn đề đã xong ('Great, it works!' / 'Thank you, all fixed'). Khi issue còn mở hoặc chờ dev, chưa phải lúc.
- [KN3] (Low) Lệch ngôn ngữ ở đầu phiên: KH viết tiếng Na Uy, Hazel trả lời bằng tiếng Anh trước khi chuyển sang Na Uy ở tin sau. (#26)
   • Dẫn chứng: [06:36:35] CS (Hazel): 'You can install the Chatty mobile app by going to Settings > Notifications > Chatty Mobile App.' — trong khi KH vừa viết 'Jeg finner den ikke på app store på min i fhone' (tiếng Na Uy).
   → Khi vào tiếp nhận ca từ CS khác, check ngôn ngữ KH đang dùng trong 2-3 tin gần nhất trước khi gõ. Trả lời đúng ngôn ngữ từ tin đầu tiên luôn.
- [KN5] (Low) Hiểu sai yêu cầu ban đầu: KH muốn làm visible một phần, Hazel lại đi hide nó, sau đó mới nhận ra và xin lỗi. (#1)
   • Dẫn chứng: [09:23:27] CS (Hazel): 'I've hidden this part for you. Please double-check it on your side' — [09:25:12] CS (Hazel): 'Ah, sorry. I misunderstood your point.'
   → Trước khi thực hiện bất kỳ thay đổi nào trên store của KH, confirm lại đúng một câu: 'Bạn muốn phần này hiển thị hay ẩn đi?' — tránh phải revert sau.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 3/6 chat phù hợp (chat #8, #12, #29) — đúng lúc cả 3, tự nhiên và không tạo áp lực. Bỏ lỡ chat #3 (KH hài lòng sau khi setup xong), #9 (KH cảm ơn nhiệt tình 'amazing thank you'), và #27 (KH xác nhận fix xong). Chat #15 bị đánh dấu sai thời điểm — issue vẫn đang pending với dev mà đã xin review. Gợi ý: thêm thói quen kiểm tra xem issue đã resolved chưa trước khi xin.

## 📈 So với tuần trước
Điểm giảm nhẹ từ 84 (W24) xuống 82 (W25). Trục Mindset tuần này thấp hơn (26.4 vs 28.4 W24), phản ánh một số chat handoff chưa có bước chốt rõ. KN3 (lệch ngôn ngữ) vẫn xuất hiện như W24, cần tiếp tục chú ý. Mặt tích cực: Knowledge ổn định và không có KT1 tuần này.

## 🔗 Chat đã QA
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b037db25-4325-427f-9104-1a2b8209b517|#1 AlphaInfuse> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_53807806-75a5-4506-bc81-9e60571e7088|#2 Lege Capsules> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ca22955f-5be8-4118-a617-cdaea078565e|#3 Peter's abiti da lavoro S.R.L.S> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4c8d39b5-631a-465f-8b6d-01328f784428|#4 スマホカバー館> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_66d0c161-8e2e-4329-922b-240f485b7908|#5 Binta Sagale Shop> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0af0e7e4-9a2c-4201-8951-1f75e41fc319|#6 Xtra Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_97f7b906-472c-43a8-899e-2a1a8f10bb86|#7 PURE Sports Nutrition Australia> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e0808926-6ced-4439-b2f5-91782b9e017b|#8 holosport> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b6675ae1-5f07-48b9-a217-3600484d3375|#9 BRUSHOLOGY> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_513bef20-9c3a-456a-8ef7-e2de2241b281|#10 PHANTOM ATHLETICS> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a680e71c-9855-4d8f-893c-343bf818d086|#11 Crate and Barrel Philippines> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3330fb52-95da-4472-9324-1a38a5f804bb|#12 Nicecnc>