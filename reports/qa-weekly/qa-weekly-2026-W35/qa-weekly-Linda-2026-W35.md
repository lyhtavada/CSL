📋 *QA TUẦN — BÁO CÁO CỦA Linda*
🗓️ Tuần W35 · 19/08 – 25/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *Điểm tuần:* 80/100 — Tốt  (▲ +4 so với tuần trước (76→80))
🔍 Đã QA: 20 chat
Breakdown: 🧠 Mindset 26.75/34 · 📚 Kiến thức 27.1/33 · 🛠️ Xử lý 26.05/33

📝 *Nhận xét chung*
Tuần này bạn xử lý ổn định trên diện rộng — điểm nổi bật nhất là ownership: gần như mọi case bạn đều theo tới cùng, tự test trước khi báo khách, escalate kèm ticket rõ ràng và quay lại xác nhận fix (chat #1, #6, #8, #10, #12, #13, #18), thay vì báo xong rồi bỏ đó. Kiến thức về giá/gói ở chat #9 rất chuẩn, khớp KB. Nhưng có 2 vấn đề cần nhìn thẳng: (1) ở chat #3 bạn trả lời hoàn toàn bằng tiếng Trung cho khách đang viết tiếng Anh, khiến khách phải tự dịch — ngay sau đó khách bực và nói thẳng "You have a bug somewhere", một phần vì giao tiếp rối; (2) ở chat #19 khi khách đưa bằng chứng kỹ thuật cụ thể (network log 19-21 file JS) bạn chỉ đưa số liệu khác (7 file) mà không đối chiếu rõ vì sao lệch, dễ khiến khách cảm thấy bị gạt đi thay vì được lắng nghe thật sự. Hướng tập trung tuần tới: luôn khớp ngôn ngữ trả lời đúng với khách đang dùng, và khi khách đưa số liệu/bằng chứng cụ thể thì phải đối chiếu rõ ràng thay vì chỉ lặp lại con số của mình.

✅ *Điểm tốt tuần này*
• Ownership mạnh — escalate có ticket rõ ràng, tự test trước khi báo khách và quay lại xác nhận fix thay vì đóng lửng, lặp lại nhất quán qua nhiều chat (#1, #6, #8, #10, #12, #13, #18)
• Bảo vệ dữ liệu khách hàng tốt — từ chối dùng order thật của khách để test vì sợ ảnh hưởng/trigger notification, chủ động đề nghị dùng order test thay thế (#10)
• Kiến thức giá/gói chính xác, khớp KB (Plus $199/tháng, 1,000 AI conversations, unlimited products) và chủ động book call với PM, follow-up khi khách miss lịch hẹn (#9)
• Xử lý khéo tình huống nhạy cảm về quyền truy cập theme — trấn an khách rõ ràng là sẽ không đổi code khi chưa xin phép trước, giữ được lòng tin (#18)

🔧 *Cần cải thiện*
• [KN3] Trả lời lệch ngôn ngữ với khách — khách đang viết tiếng Anh nhưng CS trả lời hoàn toàn bằng tiếng Trung, khách phải tự dịch mới hiểu (#3)
   → Dẫn chứng: [09:25:48] CS (Linda): 嗨！我是Linda。感谢您的联系。让我进一步为您提供帮助。 (trong khi tin trước đó của khách umakov.sk là tiếng Anh: "The text message is already translated. See the screen")
   → Luôn kiểm tra ngôn ngữ tin nhắn gần nhất của khách trước khi gửi, trả lời đúng ngôn ngữ đó thay vì mặc định/nhầm ngôn ngữ khác
• [KN7] Khi khách đưa bằng chứng kỹ thuật cụ thể (network log đo được 19-21 file JS), CS chỉ đưa ra con số khác (7 file) từ phía mình mà không đối chiếu hay giải thích vì sao chênh lệch, khiến phản hồi có vẻ phủ nhận thay vì thực sự điều tra bằng chứng khách đưa (#19)
   → Dẫn chứng: Khách: "When I audit the site's network requests with Chatty enabled, it adds 19-21 separate JavaScript files... That's a measurable fact from the browser's own network log" → Linda: "the app only loads around 7 JS files... we don't see any significant delay"
   → Khi khách đưa số liệu/bằng chứng đo được cụ thể, phải đối chiếu trực tiếp với số liệu đó (xin screenshot để so sánh ngay, giải thích rõ vì sao 2 con số khác nhau) thay vì chỉ nêu lại số của mình
• [KN6] Đưa ra kết luận/giải pháp (bật Focus Chat mode) hơi vội trước khi hỏi rõ khách muốn gì, phải điều chỉnh lại sau khi khách phản hồi không đúng ý (#7)
   → Dẫn chứng: [16:03:43] CS (Linda): Vous voulez dire que vous souhaitez que le chat en direct s'ouvre automatiquement quand vous ouvrez des sites web. (sau nhiều vòng khách phải làm rõ lại yêu cầu 'plein écran sur téléphone')
   → Xác nhận lại rõ ràng yêu cầu của khách trước khi đề xuất giải pháp, tránh vòng đi vòng lại nhiều lần

🌟 *Xin review (chỉ ghi nhận, không tính điểm)*
• Đã xin review đúng lúc ở 2/3 chat khách hài lòng phù hợp.
   Đã xin review đúng lúc ở 2/3 chat KH vừa hài lòng (chat #2, #10 — xin ngay sau khi khách cảm ơn/xác nhận xong việc). Ở chat #7 xin hơi sớm — khách vừa nói 'merci' nhưng ngay sau đó vẫn tiếp tục yêu cầu fix vấn đề khác (mobile fullscreen) chưa xong hẳn, nên cân nhắc chờ khách thực sự xong việc mới xin.

📈 *So với tuần trước*
• ▲ +4 so với tuần trước (76→80)
• Lỗi lặp lại từ tuần trước: KN3 — cần ưu tiên sửa vì đã nhắc tuần trước mà chưa cải thiện.
• Đã khắc phục so với tuần trước: KN1, KT1 👏

🔗 *Chat đã QA (20):*
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8628ff44-39f0-43e8-be20-e38b8d28437a|#1 The Vial Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8362c6dc-2acb-48e9-addc-66b8435c62a0|#2 CalmPaw> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_be9f3f4d-e5ca-4d73-8390-a742f8fa9e8c|#3 umakov.sk> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e6718968-69b2-4f87-8d9d-cf440f22f442|#4 Thypochofficial> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_87038f28-0742-4af0-b3cf-e7faf524aa1a|#5 Rheidon Tech> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1d439850-af85-41fa-b4bd-725bef2a5bae|#6 Wig Is Fashion> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_401ebd41-72d0-45f7-a5f0-877d0e4ae49f|#7 AUDACE > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2f857737-5255-4e29-b4bd-83fe72cc1398|#8 Delight> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2dd5142c-0c93-4db8-b273-baa84ca7faf6|#9 Fomo Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e8a2e4cb-afb4-487a-a842-5bb6dc367667|#10 Senior Style> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9739b8d0-37a3-4676-ab49-dc2827f0d960|#11 Yone> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ae4add3f-ed0d-415f-941c-c9f6a790a6f5|#12 Elite Reformer> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c689096f-1275-44c2-8ae7-c62eb2edfc29|#13 World of Clogs> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0a7c7604-f677-4ff9-9a42-129338197e89|#14 Rosarium Flowers> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6cfab961-be65-4aca-b887-e15b3a1b90ae|#15 NIIMBOT> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2f87c8a5-7d84-498e-8e9f-b05288e5d6d7|#16 Throne Boss Australia> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cb12d172-dd3d-4339-b148-e5caddeffb80|#17 SanaVi Health Systems> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0973ca39-7572-4f8a-bffe-370ddc05d30f|#18 Steelspan Storage Systems> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1a6ef0b6-dd59-40d4-8e63-62e430c09232|#19 Esamy> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c986267b-b8b6-4675-bc95-84ad2f4365f0|#20 niimbotstore.uk>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_