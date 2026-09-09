📋 *QA TUẦN — BÁO CÁO CỦA Phoebe*
🗓️ Tuần W36 · 02/09 – 08/09/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *Điểm tuần:* 78/100 — Đạt  (▼ -1 so với tuần trước (79→78))
🔍 Đã QA: 19 chat
Breakdown: 🧠 Mindset 26.2/34 · 📚 Kiến thức 26.8/33 · 🛠️ Xử lý 24.8/33

📝 *Nhận xét chung*
Tuần này bạn thể hiện rõ là người xử lý case kỹ thuật khó rất chắc tay — chủ động reproduce lỗi trước khi báo dev, theo case đến cùng qua nhiều ngày (WhatsApp WABA ở Yelf, email forwarding ở Lenovra), và trung thực về giới hạn sản phẩm thay vì hứa suông. Đây là điểm mạnh rõ nhất, giúp bạn xử lý tốt cả case bán hàng phức tạp (so sánh app với Oct8ne). Điểm cần thẳng thắn nhìn nhận: câu trả lời thỉnh thoảng còn thiếu một bước xác nhận rõ ràng trước khi đưa hướng dẫn, khiến khách phải hỏi lại hoặc phản đối "không đúng chỗ" (rõ nhất ở case Multigenus) — điều này kéo dài chat và tạo cảm giác dò dẫm dù bạn nắm được vấn đề. Ngoài ra nhiều câu trấn an bị lặp lại gần như nguyên văn giữa các case khác nhau, làm giảm cảm giác cá nhân hoá dù nỗ lực xử lý thực tế rất tốt — tuần tới nên tập trung xác nhận đúng màn hình/nguyên nhân trước khi hướng dẫn, và bớt dùng câu mẫu.

✅ *Điểm tốt tuần này*
• [P1] Ownership mạnh — tự reproduce lỗi trước khi escalate, theo case đến cùng qua nhiều ngày/nhiều lần handoff mà không đóng lửng (case email forwarding Lenovra kéo dài 2+ ngày qua nhiều nhà cung cấp email; case WhatsApp WABA của Yelf kéo dài hàng tuần với nhiều lần cập nhật chủ động). (#1, #6)
• [P2] Trung thực về giới hạn sản phẩm thay vì hứa suông hoặc bịa — chủ động đề xuất giải pháp thay thế khi tính năng không hỗ trợ được. (#8, #6)
• [P4] Xử lý case bán hàng/tư vấn phức tạp rất chỉn chu — trả lời đầy đủ, có cấu trúc rõ 6 câu hỏi so sánh app của khách Arganour, kèm theo dõi sát các câu hỏi follow-up nhiều tuần liền. (#10)
• [P3] Giữ bình tĩnh, kiên nhẫn với khách khó tính/đang bực (Multigenus liên tục hối thúc bằng tiếng Ba Lan, Yelf sau nhiều tuần chưa xong vẫn được trấn an đều đặn). (#2, #6)

🔧 *Cần cải thiện*
• [KN3] Hướng dẫn ban đầu đôi khi chưa rõ khiến khách phải hỏi lại/phản đối, kéo dài thời gian xử lý — nhất là khi khách đang bực. (#2)
   → Dẫn chứng: Chat #2 (Multigenus): Phoebe trả lời "Rozumiem. Zalecamy otworzyć AI agent > przewinąć w dół, aby znaleźć Settings" nhưng khách phản hồi "ale to nie jest to" (không đúng chỗ) — phải thử lại 2-3 lần mới trúng.
   → Trước khi đưa hướng dẫn, xác nhận lại đúng màn hình/tính năng khách đang xem (xin screenshot trước) thay vì đoán đường dẫn menu.
• [KN3] Câu trả lời gây hiểu lầm khiến khách phải hỏi lại "vậy vấn đề là do tôi à?" — thiếu một câu tóm tắt rõ nguyên nhân trước khi đưa bước tiếp theo. (#9)
   → Dẫn chứng: Chat #9 (DecoDine): Phoebe nói "I have just tried to subscribe your notification on my browser and it is saved successfully" rồi hỏi khách chụp màn hình, khách phản hồi "so whats the issue here by me?" cho thấy khách không hiểu ai đang gặp lỗi.
   → Luôn mở đầu bằng 1 câu tóm tắt ngắn: "Ở phía em test thì OK, nên có thể do trình duyệt/thiết bị của shop — mình thử [bước] giúp em nhé" để khách không phải đoán.
• [mindset-tone] Nhiều câu trả lời lặp lại khuôn mẫu ("Thank you so much for your understanding", "Please rest assured...", "Rozumiem") ở hầu hết các chat — làm giảm cảm giác được quan tâm thật sự, nhất là với khách đang chờ lâu hoặc đang bực (vd Yelf, Multigenus chat kéo dài nhiều ngày). (#1, #4, #9, #10)
   → Dẫn chứng: Lặp lại xuyên suốt nhiều chat: "Thank you so much for your understanding" / "Please rest assured that any updates will be notified to you as soon as possible!" gần như nguyên văn ở chat #1, #4, #9, #10.
   → Cá nhân hoá câu trấn an theo đúng bối cảnh case (nhắc lại chi tiết cụ thể khách vừa nói) thay vì dùng template cố định, đặc biệt với khách đã chờ nhiều ngày.

🌟 *Xin review (chỉ ghi nhận, không tính điểm)*
• Đã xin review đúng lúc ở 3/4 chat khách hài lòng phù hợp.
   Đã xin review đúng lúc 2/4 chat khách vừa hài lòng (chat #4 Elvo Shop, #7 border CSS) — tự nhiên, ngay sau khi khách cảm ơn. 1 lần xin hơi sớm khi chưa chắc vấn đề đã xong hẳn (chat #5, hỏi review trước khi xác nhận notification mobile đã ổn). Nhiều chat còn lại việc xin review do CS khác (Ivy/Andy/Hazel) thực hiện, không thuộc phần của Phoebe.

📈 *So với tuần trước*
• ▼ -1 so với tuần trước (79→78)

🔗 *Chat đã QA (19):*
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_767d0e07-b2de-4d6e-81b8-8a2409b9c48b|#1 Lenovra> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b4698881-bcb0-4e6b-8eb8-7e14b607eca9|#2 Multigenus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_84efa84a-0bb4-473d-8ecf-a21e4c6a8bf3|#3 LuxxeCoast> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2822f8ff-75b0-4689-98ce-669e68df1c0c|#4 Theelvoshop> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9d1d8db9-6b7d-4be0-aadb-582519fceb34|#5 Beautiful Blooms> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7edbf8b2-1e85-41c1-9b46-dca05024128b|#6 Yelf.> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_73a56d4f-dcdb-4256-be01-1bb632af2bcc|#7 Site and Storage> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7f04d2ed-8652-4d89-936a-4e22b7f53f1b|#8 No Boundaries Sport> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fcf31857-e69c-4984-800e-24ec3527b0fa|#9 DecoDine> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b3d059d2-e5bd-4807-869e-b18b0c8fd1f3|#10 ARGANOUR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6d52120b-ab1d-4192-a4b4-4d2caf6a16fa|#11 Personal Projector > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a45e1cdf-e24d-457d-b0ce-450a67e5d733|#12 Dessclusive> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_445d0684-801b-4df9-95eb-7828af39eee4|#13 Goldenora™> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b8dff355-9292-46aa-8cb7-c4decf791068|#14 Duftzwillinge by Fidawn> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_5f9eca0c-6237-4c5f-9f60-b4366e43764b|#15 CaMarz Impressions LLC> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_41d39eba-c685-4330-a8ab-5141998b2023|#16 Saint Swyn> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a1e82fec-93c4-4f16-a4a7-21960e72e608|#17 SOARDISTUSA> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_07265e24-decb-449c-9254-675837fc53e9|#18 British Broth Company> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c90638b7-80cb-4e7c-9f62-5f728e247284|#19 Kabelbinders.com>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_