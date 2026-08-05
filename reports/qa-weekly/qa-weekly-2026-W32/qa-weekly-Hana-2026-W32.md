# 📋 QA TUẦN — BÁO CÁO CỦA Hana
🗓️ Tuần 2026-W32 · 29/07 – 04/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 82/100 — Tốt  (— 0 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 28/34 · 📚 Kiến thức: 27.5/33 · 🛠️ Xử lý: 26.8/33

📝 **Nhận xét chung**
Tuần này bạn thể hiện rõ sự chắc tay về kỹ thuật Joy/Chatty — tự test lỗi (CSS, mobile scroll, cache), theo sát ticket tới cùng, và có nhiều pha chủ động thêm giá trị (phân tích setup của KH ở chat #12 rồi đề xuất top-3 việc nên làm, chủ động mời nâng cấp Unified Widget). Đây là điểm mạnh nhất và là điều khiến bạn khác biệt so với việc chỉ trả lời đúng câu hỏi. Điểm cần thẳng thắn nhìn nhận: ở case BLAEK Coffee (chat #1) bạn để khách phải lặp lại cùng một yêu cầu nhiều lần trong hơn 1 giờ trước khi thật sự hiểu đúng ý — khách đã phải viết "is our request clear? I am not sure" và "we have been texting now for the last hour about the same issue", đây là hệ quả của việc chưa paraphrase lại yêu cầu ngay từ đầu để confirm hiểu đúng. Tuần tới tập trung: xác nhận lại yêu cầu bằng 1 câu tóm tắt trước khi bắt tay xử lý các case nhiều lớp thông tin, để tránh vòng vo và giữ tốc độ xử lý mượt như phần lớn các chat khác trong tuần.

✅ **Điểm tốt tuần này**
- [P1] Ownership rất tốt — theo sát ticket kỹ thuật tới cùng, tự test lại trước khi báo khách xong (VD: chat #16 tự confirm CSS/theme, chat #20 giải thích chi tiết cơ chế sync điểm lịch sử/VIP tier trước khi migrate cho ~26,000 khách) (#16, #20)
- [P3] Chủ động vượt câu hỏi — chat #12 tự phân tích toàn bộ setup loyalty của KH và đề xuất top-3 việc nên làm để tăng ROI, không đợi KH hỏi (#12)
- [P2] Kiến thức kỹ thuật vững, giải thích rõ ràng các case phức tạp (đồng bộ điểm quá khứ, VIP tier, Klaviyo/Omnisend trigger) — không thấy sai kiến thức nào trong tuần đối chiếu KB (#20, #19, #26)
- [P5] Kiên nhẫn với khách khó/nhiều yêu cầu dồn dập vẫn giữ thái độ chuyên nghiệp, không cộc hay bỏ cuộc (case BLAEK Coffee, Kaitlin Johnstone) (#1, #23)

🔧 **Cần cải thiện**
- **[QT9] Moderate** — Để khách phải lặp lại cùng một yêu cầu nhiều lần vì chưa confirm hiểu đúng ngay từ đầu, gây kéo dài chat và khách bực (#1)
  - Dẫn chứng: "this has been the same request since yesterday!" / "we have been texting now for the last hour about the same issue" / "is our request clear? I am not sure."
  - → Khi case có nhiều lớp yêu cầu, paraphrase lại 1 câu tóm tắt yêu cầu của khách và xin confirm TRƯỚC khi bắt tay xử lý, thay vì xử lý từng phần rồi để khách phát hiện chưa đúng ý
- **[KN1] Low** — Vài lỗi chính tả/gõ nhầm trong tin nhắn chuyên nghiệp (#1, #6)
  - Dẫn chứng: "Yes, that's corect" (chat #1); "Hana ehrre" (chat #6); "we have already turned on on our end" (chat #1, lặp từ)
  - → Đọc lại tin nhắn trước khi gửi, đặc biệt các câu xác nhận/kết luận với khách
- **[KN2] Low** — Vòng vo nhẹ khi giải thích sự khác biệt giữa coupon dùng 1 lần (Entry reward) và Perk vĩnh viễn, khiến khách phải hỏi lại nhiều lần mới rõ (#29)
  - Dẫn chứng: "so this doesnt work?" ... "exactly, but as you see, it does add an expiry date automatically, so this is not working" ... "i have to upgrade to a 100 per month deal to make a coupon be used multiple times?"
  - → Dẫn thẳng vào câu trả lời cốt lõi trước (VD: "coupon hiện tại chỉ dùng 1 lần vì đây là Entry reward; muốn áp dụng mọi đơn hàng cần Perk — chỉ có ở Advanced+") rồi mới giải thích chi tiết, để giảm số vòng hỏi lại

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **3/3** chat phù hợp (đúng lúc: 3, sai lúc: 0)
- Xin review đúng lúc ở cả 3/3 chat phù hợp trong tuần (chat #4, #12, #16) — đều xin ngay sau khi khách vừa cảm ơn/hài lòng, và ở chat #12 còn chủ động nhắc tên cả đồng nghiệp khác cùng hỗ trợ case, rất đẹp. Các chat đã có review từ trước (#3, #17, #18, #20, #24) không tính vào mẫu vì không cần xin lại.

📈 **So với tuần trước**
- Điểm 82 → 82 (— 0)
- Trục: Mindset 29.0→28, Kiến thức 28.0→27.5, Kỹ năng 25.0→26.8
- Lỗi lặp lại từ tuần trước: KN1
- Lỗi tuần trước đã hết: KN7 👏
- Lỗi mới tuần này: KN2, QT9

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4c3a5a1f-6e04-4670-a88d-dd033abc84b3|#1 BLAEK Coffee> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_894f5998-cde6-47bf-b4d6-840bc8bd1deb|#2 Orsolya Lele> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_193b8bef-9be7-4360-a323-33576213b38a|#3 wilson wu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_eb2cdf8c-98ed-4eba-ae16-51e2d503634d|#4 LeanLight> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_13a4c794-3c6b-427e-aa5d-0fc26fd77a15|#5 visitor3650290> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b3000394-cf1a-4104-8040-b12e7e5227e9|#6 Daniel Hasagic> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7897647a-350c-4ad5-81bd-d19030353f7f|#7 Ahmed AlMahmoud> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_22a87a54-e63e-4da6-a6aa-5e53bc603ceb|#8 Jolan Ababse> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8c5dcd86-fb07-4b3d-9411-9fe718dd09a8|#9 Orbeluis Guasch> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_66216b80-0053-4c74-9dfc-2d296ceea4b1|#10 Blażej Baar | BELLER.PL> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e9f92cd5-d081-45e5-adaa-1bec3b88b35d|#11 Claudia (US) Colomboni> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d1e7ea57-87cb-4b61-9baa-d8dc468ff61d|#12 The Collective> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9c7210ba-2852-43fd-9bd9-ae851349ef24|#13 Manon del Bubba> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_83bc00af-5620-46f2-a98b-005f6809850b|#14 Paris House of Beauty> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3aeb37ab-d092-4278-b0b8-1b359c5b6c0d|#15 Healthylifehappymind6> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_631fd237-1c43-456b-960e-db3279b6fdac|#16 Healez Beauty> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_03f885cc-0a96-4260-aae9-fd44f444dea9|#17 IKJUN JANG> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_919419ae-6749-4545-8038-c0da796cd749|#18 Samuel Chan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b401eaec-0e89-4606-aa12-e7c14c155201|#19 shi tao wang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3bbe968f-1cca-497e-999c-2e04de0193d4|#20 Nicolas Habran> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e4441a5f-75c0-4905-beb2-df5097185746|#21 Verified Marketplace> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f723d689-2d89-458d-bdd5-1968af1d0494|#22 Susanna Karslian> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_72f38c9b-18d0-4a4d-8416-85018d2f78fb|#23 Kaitlin Johnstone> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_980074d7-f70d-4ab8-a1b3-db6e970480d7|#24 Cuura Malaysia> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7857ff95-79e8-4229-9748-60788bd29549|#25 Krissy Jones> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_155150ef-0b2a-4cad-9ba3-15f251a79a73|#26 ahmad mazn> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_980b0b44-b056-4881-b4f1-e2d1c773c9b0|#27 HAPPYNIMAL TROPICALIS> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9fab7992-39b0-4af7-ad19-955536fd7b81|#28 HappyLaulea> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ce2ae69a-d1d6-4e1c-bf11-e90e4c79b030|#29 Magnus Rolstad> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3a2aca6e-7b53-43c8-8138-d74af2c0bc8c|#30 Studioby Forward>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_