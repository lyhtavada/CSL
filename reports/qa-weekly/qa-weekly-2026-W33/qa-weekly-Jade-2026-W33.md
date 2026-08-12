# 📋 QA TUẦN — BÁO CÁO CỦA Jade
🗓️ Tuần 2026-W33 · 05/08 – 11/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 82/100 — Tốt  (▼ -1 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 28/34 · 📚 Kiến thức: 27.4/33 · 🛠️ Xử lý: 27/33

📝 **Nhận xét chung**
Tuần này Jade xử lý ổn định, đặc biệt mạnh ở mindset: kiên trì theo case khó, dài nhiều ngày (kể cả DFY phức tạp) mà không đẩy việc hay đóng lửng, kiến thức plan/pricing khớp KB gần như tuyệt đối. Điểm cần tập trung rõ ràng là sự cẩn thận trong lúc gõ nhanh — gửi nhầm ngôn ngữ và khẳng định "đã fix" khi thực tế chưa xong đều là lỗi có thể tránh nếu chậm lại kiểm tra trước khi gửi, và cả hai đều làm khách phải quay lại hỏi thêm, kéo dài chat không cần thiết. Ngoài ra bạn đang bỏ lỡ khá nhiều cơ hội xin review (4/10 chat KH hài lòng không được hỏi) — nên biến việc xin review thành thói quen mặc định mỗi khi đóng chat thành công.

✅ **Điểm tốt tuần này**
- [P1] Ownership rất tốt với case dài, khó, nhiều ngày — không đẩy việc, không đóng chat lửng dù khách khó tính hoặc kéo dài hàng giờ (chat #1 troubleshooting widget loading cả buổi với khách TQ khó chịu; chat #16, #19 các dự án DFY Joy kéo dài nhiều ngày với hàng chục yêu cầu nhỏ, Jade vẫn theo sát từng phần được giao). (#1, #16, #19)
- [P2] Kiến thức plan/pricing chính xác, khớp KB live — báo đúng giá Essential $29/mo/500 orders (chat #9), đúng phân quyền feature theo plan (Redeem Checkout chỉ Ultimate+Plus, Cart Drawer redeem có ở Advanced — chat #23). (#9, #23)
- [P4] Chủ động làm thêm ngoài yêu cầu gốc để tránh khách phải hỏi lại — ví dụ khi fix vị trí widget xong, tự phát hiện và fix luôn màu chữ bị khó đọc dù khách chưa report (chat #26). (#26)
- [P3] Hướng dẫn rõ từng bước, dùng đúng ngôn ngữ khách (tiếng Đức, tiếng Trung) để khách làm theo được ngay, không vòng vo (chat #2 setup referral program, chat #6 setup AI agent tiếng Đức). (#2, #6)

🔧 **Cần cải thiện**
- **[KN3] Moderate** — Gửi nhầm tiếng Bồ Đào Nha cho khách đang chat hoàn toàn bằng tiếng Trung — có vẻ copy nhầm canned response từ chat khác, làm khách phải tự đoán ý. (#1)
  - Dẫn chứng: "Nossa equipe também o manterá informado assim que o problema de exibição do ícone for corrigido" — trong khi khách BoxAnime chat toàn bằng tiếng Trung suốt cuộc hội thoại.
  - → Kiểm tra lại đúng ngôn ngữ trước khi gửi canned message, đặc biệt khi copy nhanh từ template có sẵn.
- **[KN6] Low** — Khẳng định "đã fix" quá sớm cho vấn đề chưa thực sự xong, khiến khách quay lại báo lỗi tiếp và mất tin tưởng. (#1)
  - Dẫn chứng: "我很高兴地告诉你,我们已经修复了小图标问题" — nhưng ngay sau đó khách vẫn báo "桌面的图标里的LOGO，好小啊" và vấn đề loading gốc vẫn chưa giải quyết.
  - → Chỉ báo "đã fix" khi đã verify chắc chắn với khách; nếu chưa chắc, nói "đang được xử lý, sẽ cập nhật" thay vì khẳng định xong.
- **[KN5] Low** — Hiểu sai câu hỏi của khách về việc tuỳ chỉnh Trigger của Cart Booster template, trả lời lạc sang tính năng phục hồi giỏ hàng bỏ dở chưa có, khiến khách phải nói lại. (#30)
  - Dẫn chứng: Khách hỏi "这个trigger可以自定义设置吗？" → Jade trả lời về việc chưa có "主动的购物车放弃恢复活动" → khách phản hồi "我不理解你的意思，我问的是这个Trigger是否自定义".
  - → Đọc kỹ câu hỏi trước khi trả lời, nếu không chắc ý khách hỏi gì thì confirm lại ngắn gọn trước khi giải thích dài.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **6/10** chat phù hợp (đúng lúc: 6, sai lúc: 0)
- Xin review 6/10 chat khách hài lòng phù hợp, đúng lúc (ngay sau khi khách cảm ơn/hài lòng) — không có lần nào xin sai lúc. Tuy nhiên bỏ lỡ 4 chat KH đã hài lòng, đóng chat xong mà không xin (chat #13, #21, #25, #27) — đây đều là cơ hội tốt, nên tận dụng thêm.

📈 **So với tuần trước**
- Điểm 83 → 82 (▼ -1)
- Trục: Mindset 27.9→28, Kiến thức 28.1→27.4, Kỹ năng 27.1→27
- Lỗi lặp lại từ tuần trước: KN3
- Lỗi tuần trước đã hết: KN2, KT1 👏
- Lỗi mới tuần này: KN5, KN6

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4acda93f-6fb9-4e28-8b3e-7e9291476049|#1 BoxAnime> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_efefa726-4f4f-4694-8fdc-b96f8e606dba|#2 Farro Chip> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_193b8bef-9be7-4360-a323-33576213b38a|#3 wilson wu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ea3e1d01-cbc8-4899-b686-d604a71b9726|#4 visitor3655797> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4bc1e60d-16fd-47f1-813e-a8c61e2edfb6|#5 Aacarto> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2a839073-768d-4b7e-a6d3-dfb919a3ada6|#6 liv bergen> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_28938ca1-ca77-4010-8b3d-86dc955a99dd|#7 Chris Murphy> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_894f5998-cde6-47bf-b4d6-840bc8bd1deb|#8 Orsolya Lele> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2a253970-8f11-4aa2-ae22-422f235cde96|#9 mentor cosmetics> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0ea73084-740b-4cbf-85ec-0afae3192262|#10 Jiarui Zhu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_82d3973c-5bd1-462d-85cf-bd0e88f670c1|#11 Ruvo Pro> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7675185c-f4db-49f4-a9a8-8c80f28e003d|#12 TopTrainer> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d7902a16-4261-4de0-93cb-5983952d92b5|#13 Mark Koay> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_08148c5f-a8bd-489c-9ffb-0776d1dc19bc|#14 D'AZUR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9f483cc7-4a93-4c00-9b18-cd07e33e33c8|#15 Slate-Lite> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b46cd734-920b-454a-98cb-ddbed261018a|#16 創造 富川> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_67706346-c712-4655-9117-738429a672d9|#17 ZU SHAN> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_775b9bc2-71ed-4b9d-9f1b-d5aff54e6599|#18 Brooke James> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_14bc8e63-e2d1-4f6b-8b6d-9f3dc823faa1|#19 ZHANHAO MAI> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a78f01d3-876c-4ff8-a979-62f2587e47ae|#20 Belleze> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8eab5d22-6e42-47df-ad52-0ee6b4b49f06|#21 Johanna Lölkes> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4c3a5a1f-6e04-4670-a88d-dd033abc84b3|#22 BLAEK Coffee> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1d976e53-c856-47eb-956f-7034e8e0aa11|#23 Richard Pye> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_447a2a95-f3fe-4378-84c2-9ab0c9f25af3|#24 Pretty In Paper By B> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bcbc536d-4295-4789-ad39-662f61bdba81|#25 visitor3655791> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_06612275-db32-4d7c-b809-22a281640f6f|#26 Julie Situ> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2aae1aa1-b95c-4fb3-9c3e-a67ad73faf13|#27 subhashini srinivasan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e8929d78-b190-4309-a545-8a685892c5d7|#28 Hugsback> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_58a474d1-7f4c-473f-806c-0a185f17afc7|#29 Aleksandr Krutik> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f181c448-91ee-43a7-85b0-08cec2112239|#30 ExBriteUSA>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_