# 📋 QA TUẦN — BÁO CÁO CỦA Phoebe
🗓️ Tuần 2026-W31 · 22/07 – 28/07/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 79/100 — Đạt  (▲ +2 so với tuần trước)
🔍 Đã QA: 24 chat
🧠 Mindset: 26.8/34 · 📚 Kiến thức: 26.5/33 · 🛠️ Xử lý: 25.9/33

📝 **Nhận xét chung**
Tuần này bạn xử lý ổn ở các case cần theo dõi nhiều bước (ticket, follow-up, DFY setup) và giữ được bình tĩnh, minh bạch ngay cả khi khách gắt hoặc doạ report Shopify — đây là điểm mạnh rõ nhất, đặc biệt ở chat #14 và #9. Tuy nhiên bạn chưa đạt mức Tốt vì ở case yêu cầu đơn giản, trực tiếp (chat #20 khách chỉ muốn gỡ app) bạn lại vòng qua bước hỏi feedback trước khi đưa hướng dẫn, khiến khách phải lặp lại yêu cầu và chờ thêm nhiều giờ — cần phân biệt rõ: yêu cầu rõ ràng thì giải quyết trước, feedback hỏi sau. Ngoài ra khá nhiều chat trong mẫu phần đóng góp trực tiếp của bạn khá mỏng (chủ yếu điều khiển bot qua /follow-up, /replay) nên chưa thấy hết năng lực xử lý trực tiếp — tuần tới nên chủ động trả lời trực tiếp nhiều hơn để thể hiện rõ chất lượng tư vấn của chính mình.

✅ **Điểm tốt tuần này**
- [P1] Theo tới cùng với case nhiều issue gộp chung 1 chat (VD chat #4: 3 lỗi Inbox — send email offline, location, assignment; chat #8: DFY AI agent setup + hàng loạt điều chỉnh follow-up sau đó) — tạo ticket, update khách từng bước, không bỏ dở giữa chừng. (#4, #8, #19)
- [P2] Giữ bình tĩnh, không phòng thủ khi khách bực/gắt (chat #9 khách chê 'garbage', 'WTF'; chat #14 khách doạ report Shopify) — vẫn giải thích rõ ràng, minh bạch (VD chat #14 giải thích rõ về quyền truy cập collaborator/privacy) và xoa dịu được khách. (#9, #14)
- [P3] Kiến thức kỹ thuật chính xác, verify được với KB: giá Pro $68.99/mo — 500 AI conversations (chat #5) khớp KB; giải thích rõ cơ chế bounce email do mail server nhận, không phải do Chatty (chat #18); giải thích đúng logic AI nhận diện intent theo keyword 'order' vs SKU thiếu data (chat #19). (#5, #18, #19)

🔧 **Cần cải thiện**
- **[QT22] Moderate** — Khi khách yêu cầu rõ ràng và đơn giản (gỡ app khỏi site), bạn không đưa hướng dẫn ngay mà chỉ hỏi lại lý do/feedback trước, khiến khách phải lặp lại yêu cầu và chờ thêm nhiều giờ mới có người (Cody) hướng dẫn tắt app. (#20)
  - Dẫn chứng: Khách: 'please remove this off my site we no longer want it' → Phoebe: 'To assist you better, could you please share with us any difficulties you are facing when using our app?' → 5 tiếng sau khách phải nhắc lại: 'correct please remove it', 'it's still on our site'.
  - → Với yêu cầu rõ ràng (gỡ/tắt tính năng), đưa hướng dẫn thực hiện NGAY trong cùng tin nhắn, rồi mới hỏi thêm lý do/feedback để giữ khách — đừng biến bước hỏi feedback thành điều kiện tiên quyết trước khi hỗ trợ.
- **[KN1] Low** — Lỗi chính tả nhỏ trong câu mở đầu tự giới thiệu. (#16)
  - Dẫn chứng: "Hello! This is Phoebe from Avada support tea. I can see that you are discussing setup FAQ page with our bot." (thiếu chữ 'm' — 'team')
  - → Đọc lại câu chào trước khi gửi, nhất là câu mở đầu lặp lại nhiều chat để tránh lỗi đánh máy.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **2/2** chat phù hợp (đúng lúc: 2, sai lúc: 0)
- Xin review đúng lúc ở cả 2/2 chat phù hợp (khách vừa cảm ơn xong là mời liền) — chat #3 và #17. Không có chat vàng nào bị bỏ lỡ trong mẫu tuần này.

📈 **So với tuần trước**
- Điểm 77 → 79 (▲ +2)
- Trục: Mindset 25.6→26.8, Kiến thức 26.1→26.5, Kỹ năng 25.1→25.9
- Lỗi tuần trước đã hết: KN3, KN7, KT2, QT18 👏

🔗 **Chat đã QA (24):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bf8faa05-b880-4bce-bb46-88e0a9b0a2f7|#1 AWNL Taiwan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_63798fe6-dfbe-488a-b8ee-b10e26b5f6e1|#2 American Expedition Vehicles> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6ee8b515-4a4f-4e35-9dfb-3ca997088270|#3 Pawder> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cc3171cc-26b0-401e-97d8-37669ee16319|#4 Fc Sports> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6aac5198-6468-4099-8f8b-2f6bf7daa6d0|#5 Nutritional Performance Labs> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_226e579f-d01e-4f72-97b8-cfbf458d44ea|#6 Korvexa> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_430549c8-ee3c-4df2-bfa2-53ce6604857c|#7 Canine India> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_39f923d5-8565-4551-8951-36875a5c6170|#8 CR3DesignCo> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2668bd40-d5a2-4e52-b390-58e2a22249e8|#9 WatchPlaza> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bd06d071-b28b-4780-b398-a9f62a80f0b3|#10 Savage California> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_74c6c964-2466-4f2e-b021-a7ebe1e68af4|#11 OuiSi> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_607f6a7f-87cb-462a-b2d3-eb28a8ef9fbd|#12 Riskisyou> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_5e9a040b-ead2-4fb6-9bbd-915302cf5f38|#13 Gold Zerafet Takı> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_49aac28c-7793-4626-a221-c8195a0b57ea|#14 8849 Official Website> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cefa0af9-d403-4582-894f-4bbe543bf790|#15 Enveseur> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9fb56fc6-504f-4121-97bd-a33e9cfa8655|#16 Saltdoll> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e3f852e7-9326-4cf2-baab-0b301a3f69b0|#17 Diouda> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fe9c3758-0749-453f-98be-946647a1eacc|#18 VARON> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e15f0c82-9da0-4ce6-9f87-ddaee9832699|#19 Wiltshire Wood Flooring Supplies> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b1ce6dfc-f277-4581-b535-33f46771c87c|#20 PawMart> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d2b14069-b14f-4b06-91c6-448cefd03b43|#21 My Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8c1964e5-bbec-4636-a7d2-91d2d0567a5b|#22 canfish.store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_20570c7c-137c-4320-8fec-f41ffa3060ec|#23 Collective Expressions> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7d0f45de-130b-4f1b-af22-3ef0dd2af237|#24 visitor3647040>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_