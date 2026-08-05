# 📋 QA TUẦN — BÁO CÁO CỦA Linda
🗓️ Tuần 2026-W32 · 29/07 – 04/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 83/100 — Tốt  (▼ -2 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 27.8/34 · 📚 Kiến thức: 28.2/33 · 🛠️ Xử lý: 27.5/33

📝 **Nhận xét chung**
Linda là một trong những CS xử lý chat kỹ và có trách nhiệm nhất trong mẫu tuần này: liên tục confirm lại yêu cầu trước khi thao tác, tự test kỹ trước khi trả lời khách (chat #8 từ chối test bằng đơn hàng thật của khách để tránh ảnh hưởng khách hàng — rất chuẩn), và chẩn đoán đúng gốc rễ vấn đề thay vì chỉ đẩy ticket (chat #13 phát hiện lỗi gõ sai domain email, chat #26 chỉ đúng nguyên nhân AI bịa thông tin). Nhưng có 2 điểm cần sửa thẳng thắn: ở chat #4 bạn để cuộc trò chuyện chuyển sang tán tỉnh cá nhân với khách ("có thể tôi sẽ giữ nó như một bí mật nhỏ") thay vì giữ tông chuyên nghiệp — việc này khiến vai trò support bị mờ đi và có thể ảnh hưởng hình ảnh team. Ở chat #6, khi khách than phiền vì phải tự tạo nhiều Q&A một, bạn chỉ hướng dẫn thêm thay vì chủ động đề nghị làm giúp (như bạn đã làm rất tốt ở chat #3, #11) — khách cuối cùng rời đi vì thấy tool "không phù hợp". Tuần tới tập trung: giữ ranh giới chuyên nghiệp khi khách đùa/khen cá nhân, và chủ động giảm tải công việc cho khách thay vì chỉ hướng dẫn khi thấy khách đang quá tải.

✅ **Điểm tốt tuần này**
- [P1] Ownership/an toàn cho khách: từ chối dùng đơn hàng thật của khách để test vì sợ ảnh hưởng đến khách hàng cuối, chủ động xin đơn test thay thế — tư duy bảo vệ khách rất tốt. (#8)
- [P2] Chẩn đoán đúng gốc rễ vấn đề thay vì chỉ escalate: phát hiện lỗi gõ sai domain email (boob... vs bobo...) khiến khách không nhận được email xác thực; chỉ đúng nguyên nhân AI bịa thông tin do thiếu metafield. (#13, #26)
- [P3] Kiên nhẫn cao với khách khó/đòi hỏi nhiều trong thời gian dài mà không mất bình tĩnh hay bỏ cuộc. (#4, #23)
- [P4] Thói quen confirm lại yêu cầu bằng câu "Just to confirm..." trước khi thao tác, giảm rủi ro làm sai ý khách. (#3, #5, #14)
- [P5] Chủ động giới thiệu thêm tính năng có lợi cho khách ngoài câu hỏi ban đầu (Proactive Chat) thay vì chỉ trả lời đúng câu hỏi. (#9)

🔧 **Cần cải thiện**
- **[Mindset-professionalism] Moderate** — Đáp lại theo kiểu tán tỉnh khi khách buông lời trêu chọc cá nhân, thay vì giữ tông chuyên nghiệp trung lập. (#4)
  - Dẫn chứng: Customer: "tu est belle tu est de quelle origine" → Linda: "Merci pour vos gentils mots. Vous êtes aimable et merveilleux aussi... peut-être que je le garderai comme un petit secret jusqu'à notre prochaine rencontre 😊"
  - → Khi khách khen/trêu chọc cá nhân, cảm ơn ngắn gọn rồi chuyển hướng ngay về công việc hỗ trợ, tránh đáp lại theo kiểu flirt để giữ ranh giới chuyên nghiệp.
- **[KN1] Low** — Lệnh nội bộ (/lindahello) bị dính vào tin nhắn gửi cho khách, trông thiếu chuyên nghiệp. (#24)
  - Dẫn chứng: "Lascio che mi occupi io e ti aiuto direttamente./lindahello"
  - → Đọc lại tin nhắn trước khi gửi để tránh lệnh/slash-command lẫn vào nội dung khách nhìn thấy.
- **[Mindset-proactive] Moderate** — Khi khách than phiền vì phải tự thêm nhiều Q&A một, chỉ hướng dẫn viết instruction rõ hơn thay vì chủ động đề nghị làm giúp — khách cuối cùng rời đi vì thấy tốn công. (#6)
  - Dẫn chứng: Customer: "SO you want me to create answers 1 by 1?? Its like so many questions" → Linda chỉ trả lời hướng dẫn cách viết instruction cụ thể hơn, không đề nghị hỗ trợ nhập giúp; khách sau đó nói "naah your tool isn't the right fit for me its still 2024 level, thanks anyways"
  - → Khi thấy khách đang quá tải công việc, chủ động đề nghị làm giúp (giống cách đã làm tốt ở các chat khác khi hỏi "muốn mình thêm 15 Q&A giúp hay để bạn tự thêm") để giảm ma sát và giữ khách.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **10/12** chat phù hợp (đúng lúc: 10, sai lúc: 0)
- Đã xin review đúng lúc ở 10/12 chat khách hài lòng phù hợp — tỷ lệ tốt, không có ca nào xin sai lúc. Bỏ lỡ 2 chat vàng đáng tiếc: #9 và #19, khách khen rất nhiệt tình ("you're amazing") nhưng không được mời để lại review.

📈 **So với tuần trước**
- Điểm 85 → 83 (▼ -2)
- Trục: Mindset 29.0→27.8, Kiến thức 28.2→28.2, Kỹ năng 28.2→27.5
- Lỗi lặp lại từ tuần trước: KN1
- Lỗi tuần trước đã hết: KN2, QT18 👏
- Lỗi mới tuần này: Mindset-proactive, Mindset-professionalism

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cefa0af9-d403-4582-894f-4bbe543bf790|#1 Enveseur> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b7a16c25-889b-423e-b89e-2be8b7939593|#2 NOIR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3ea9c757-d91f-4898-b6c7-d6c079c0bc06|#3 Tellytalephone> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_22337ace-d993-4142-a55a-c98cb8c75fae|#4 E-VELO> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cfaa9d3b-9335-47b0-80d6-96c6a0210d40|#5 Wright Beauty> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_08a23b8b-d855-4bd7-8307-52fc154f42dc|#6 Stamplified> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7f0ff348-c02d-4519-872b-37f63130ae1c|#7 Living.Fit> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e8a2e4cb-afb4-487a-a842-5bb6dc367667|#8 Senior Style> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_678dc5c3-c5a1-49bd-8914-cea707036961|#9 My Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b8c80091-98c3-4c89-8396-0f57c44825a8|#10 The Zoofamily> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8808fddf-a8ce-4a59-957a-1fafde09f65c|#11 Azurlis™ Botanical Skin Care> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bcaedc2a-94f5-4dd9-8f69-633dcfdad5e9|#12 سنفينكو عُمان  > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ca132d6a-8bf6-45a8-be82-ac35ceceb54b|#13 BOBO WELLNESS> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_11347cab-7202-4bd1-ae6f-204c79f7ea41|#14 The Low Vision Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2ebce4de-7e88-4517-a48e-a445ff8efdaf|#15 Betterlovedoll> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_26eb8bed-729d-4be7-9731-cabaf27b46c1|#16 Direct Coins> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9fab7992-39b0-4af7-ad19-955536fd7b81|#17 HappyLaulea> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7ed75446-feb7-4629-bb11-bfefdb27e7b7|#18 Lasercyber-tech> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9b190eab-23d1-4cad-acd9-a3692a946be3|#19 El Sinclaire> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_22d9ff91-3702-4bce-a674-cb21be8b3346|#20 RacksBrax> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f857d326-da78-48e7-8e45-b868d97e539f|#21 Milanesas Delivery> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e6656556-82a6-4a39-9f0a-eaad6ff9939f|#22 Fjrjrltd> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7edbf8b2-1e85-41c1-9b46-dca05024128b|#23 Yelf.> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ca22955f-5be8-4118-a617-cdaea078565e|#24 Peter's abiti da lavoro S.R.L.S> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_74a19695-e00b-4ca7-a326-1f12426a0a86|#25 Ridstar> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_60992930-bf7b-484c-84d3-fb39fd26bae7|#26 Casa Outlet Furniture> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0a76bfe4-e031-48e3-9237-e3104ceae2bc|#27 Outdoors Lifestyle> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f93cf54d-e3f9-43d7-b972-4fc0c727f712|#28 IMPLICIT> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_04520caa-7f51-4356-8901-e1122d5082f2|#29 Steady Vitamins> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c334d6a4-ba21-4243-a940-351518fe0dab|#30 Artiteq>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_