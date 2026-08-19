📋 *QA TUẦN — BÁO CÁO CỦA Audrey*
🗓️ Tuần W34 · 12/08 – 18/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *Điểm tuần:* 80/100 — Tốt  (Tuần đầu chấm lại sau 3 tuần (Audrey 0 chat W31-W33; lần gần nhất W29: 87đ) — không tính delta chặt.)
🔍 Đã QA: 14 chat
Breakdown: 🧠 Mindset 27.4/34 · 📚 Kiến thức 26.8/33 · 🛠️ Xử lý 25.9/33

📝 *Nhận xét chung*
Tuần này bạn xử lý tốt các case Joy phức tạp — case billing $490 do Klaviyo sync (chat #2) và migration VIP tier nhiều bước (chat #11, #10) đều được theo tới cùng, tạo ticket rõ ràng, escalate đúng chỗ. Điểm mạnh nhất là sự cẩn trọng: ở chat #12 bạn không tin ngay vào help doc cũ mà double-check với dev team trước khi trả lời khách, tránh được thông tin sai. Tuy nhiên có một lỗ hổng rõ ràng cần sửa: ở chat #9 bạn hiểu sai câu hỏi của khách ngay từ đầu (khách hỏi "chỉnh sửa ở đâu" nhưng bạn trả lời về việc revoke coupon), khiến khách phải nhắc lại nhiều lần và bật ra câu "I don't think we understand each other" — đây là hệ quả trực tiếp của việc không confirm lại đúng vấn đề trước khi đưa hướng xử lý, làm kéo dài chat không cần thiết. Ngoài ra ở chat #5 khách phàn nàn thẳng về tốc độ phản hồi ("sei molto lenta a rispondere") — cần chú ý pace khi case dồn dập, đừng để khách phải hỏi lại vì chờ quá lâu.

✅ *Điểm tốt tuần này*
• Ownership tốt trên case phức tạp/nhạy cảm: case billing $490 do bulk metafield update trigger Klaviyo sync — theo tới cùng, tạo ticket kỹ, chủ động escalate refund cho management thay vì né tránh ("I'll also escalate your refund request to our management team for their review") (chat #2)
• Kiến thức: không tin ngay vào help doc cũ mà double-check với dev team trước khi trả lời — phát hiện help doc bị outdated và báo khách rõ ràng thay vì trả lời sai theo doc ("After a double-check with our development team, I am happy to confirm...our Helpdesk documentation...contained some inaccurate information") (chat #12)
• Kỹ năng: luôn confirm lại yêu cầu phức tạp trước khi thực hiện, tránh làm sai trên case migration nhiều điều kiện ("Just to confirm, you'd like to migrate $1000 VIP amount spent...Do I understand it correctly?") (chat #11)
• Chủ động vì khách: tự gửi danh sách website DTC tham khảo dù khách không hỏi cụ thể link, và chủ động đề xuất free setup service cho widget khi merchant đang di chuyển từ Smile.io (chat #1, #6)

🔧 *Cần cải thiện*
• [KN5] Hiểu sai câu hỏi của khách ngay từ đầu, đưa ra hướng xử lý không đúng trọng tâm khiến khách phải nhắc lại nhiều lần và bực bội (chat #9)
   → Dẫn chứng: Khách hỏi cách kiểm tra/edit cấu hình gift cho Superstar tier, nhưng Audrey trả lời về việc revoke discount code khiến khách phải nói: "I don't think we understand each other... My issue is not with the discount code... I want to check it myself too... you said you checked it yourself"
   → Trước khi đưa giải pháp, paraphrase lại đúng câu hỏi khách vừa hỏi (đặc biệt câu hỏi dài/nhiều ý) để confirm hiểu đúng, tránh nhảy thẳng vào hướng xử lý cũ đã quen tay
• [QT8] Khách phàn nàn trực tiếp về tốc độ phản hồi trong lúc chờ xử lý case downgrade (chat #5)
   → Dẫn chứng: "sei molto lenta a rispondere" (bạn trả lời rất chậm) — khách nói thẳng giữa chat khi đang chờ câu trả lời đơn giản
   → Khi case cần thời gian xử lý nội bộ, gửi tin báo trước thời gian dự kiến ngay ("cho mình 2-3 phút để confirm nhé") thay vì để khách chờ im lặng rồi mới giải thích sau khi bị nhắc
• [KN1] Gửi trùng lặp 2 tin nhắn giống hệt nhau liên tiếp — nhỏ nhưng thiếu chuyên nghiệp (chat #1)
   → Dẫn chứng: 05:50:30 và 05:50:31 gửi 2 câu gần như y hệt: "是的，您可以在Shopify折扣中找到Joy折扣..." rồi lại gửi lại ngay sau đó
   → Kiểm tra lại trước khi gửi khi đang trả lời nhanh liên tiếp, tránh double-send

🌟 *Xin review (chỉ ghi nhận, không tính điểm)*
• Đã xin review đúng lúc ở 0/1 chat khách hài lòng phù hợp.
   Chỉ có 1/10 chat 'chưa có review' đủ điều kiện xin (khách hài lòng/vấn đề xong) — hầu hết các chat khác đều là case đang xử lý dở dang (ticket/escalation còn pending) nên không tính vào mẫu. Ở chat đủ điều kiện (#7, khách cảm ơn và từ chối upgrade nhẹ nhàng), Audrey chưa chủ động xin review — có thể tận dụng thời điểm này lần sau.

📈 *So với tuần trước*
• Tuần đầu chấm lại sau 3 tuần (Audrey 0 chat W31-W33; lần gần nhất W29: 87đ) — không tính delta chặt.

🔗 *Chat đã QA (14):*
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a041e982-0086-446a-b9ad-7b226da8d0bf|#1 Fei f> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4c3a5a1f-6e04-4670-a88d-dd033abc84b3|#2 BLAEK Coffee> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cd81ac62-b4ee-4256-bc43-62aa3059b5e1|#3 Nissoplus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_958eae46-ec70-4330-befa-a5a5215122a5|#4 CHENG ZHAO> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e9f92cd5-d081-45e5-adaa-1bec3b88b35d|#5 Claudia (US) Colomboni> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b05f85fb-6a10-4911-be25-705fb5490623|#6 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b76729c8-2b7d-4976-a672-06d40da2420f|#7 Sebastian Apablaza> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_03f885cc-0a96-4260-aae9-fd44f444dea9|#8 IKJUN JANG> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1083ca8f-ee1c-4341-ad66-d6ceded9f158|#9 Monica Olavarria> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bad7ebd0-190c-424e-bfa8-8c7ca446c9dc|#10 due studio> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c6aad2fe-efa8-480d-877a-ffdb41c800c1|#11 Dylan Ong> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_efefa726-4f4f-4694-8fdc-b96f8e606dba|#12 Farro Chip> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0cea6a1a-010a-402d-8043-b5b8b2c55cbd|#13 Auston Wong> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2c58ecb5-015f-4ff9-b549-37604618395c|#14 han leong ong>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_