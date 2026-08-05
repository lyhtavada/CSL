# 📋 QA TUẦN — BÁO CÁO CỦA Phoebe
🗓️ Tuần 2026-W32 · 29/07 – 04/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 75/100 — Đạt  (▼ -4 so với tuần trước)
🔍 Đã QA: 15 chat (loại 1 chat không đủ điều kiện)
🧠 Mindset: 24.9/34 · 📚 Kiến thức: 25.5/33 · 🛠️ Xử lý: 24.3/33

📝 **Nhận xét chung**
Tuần này bạn xử lý ổn về mặt kiến thức kỹ thuật — nắm khá vững các case phức tạp (translation pricing, metafield limitation, FRT) và có vài lần chủ động sửa lại thông tin sai của bot AI, đây là ownership thật đáng ghi nhận. Nhưng điểm cần thẳng thắn nhìn nhận: nhiều lượt tương tác của bạn chỉ dừng ở câu ngắn qua lệnh /follow-up hoặc "Let me check", thiếu chiều sâu chủ động giải thích cho khách; và ở case notification lặp email (chat #7), bạn bỏ qua hướng dẫn rõ ràng có sẵn trong KB, đưa khách đi sai hướng khiến vấn đề chưa được giải quyết dứt điểm. Tuần tới nên ưu tiên: tra kỹ KB trước khi trả lời case đã có sẵn hướng xử lý thay vì đoán, và diễn đạt rõ đơn vị/số liệu ngay từ đầu để khách không phải hỏi lại.

✅ **Điểm tốt tuần này**
- [P1] Chủ động phát hiện và sửa lại thông tin sai của bot AI thay vì để nó trôi qua — chat #7: bot Ivy giải thích sai về notification 'Conversations assigned to AI assistant', Phoebe vào đính chính rõ ràng ('I would like to correct that... it sends email notification one time only'); chat #15: phát hiện khách đang hiểu nhầm text từ FAQ/Conversation Starter là do AI bịa, chỉnh hướng đúng nguồn. Đây là ownership thật, không phải chấp nhận cho qua. (#7, #15)
- [P2] Kiến thức sản phẩm khá vững ở các case kỹ thuật phức tạp: giải thích đúng bảng giá Real-time Translation (50/300/700 theo Basic/Pro/Plus, khớp KB) dù có lỡ lời rồi tự sửa ngay; giải thích rõ ràng, mạch lạc về giới hạn metafield trong product-lookup tool (chat #4) và cách tính First Response Time/stale backlog (chat #10) — đều đúng và không vòng vo. (#1, #4, #10)
- [P3] Xin review đúng thời điểm khách đang hài lòng, không gượng ép — chat #2 và #5 khách đồng ý ngay sau khi vấn đề được giải quyết; đặc biệt chat #14, sau khi xin review khách xác nhận luôn 'I just gave you 5 stars' — kết quả thực tế, không chỉ là thao tác hình thức. (#2, #5, #14)

🔧 **Cần cải thiện**
- **[KT2] High** — Khách báo rõ vấn đề trùng khớp case 'Too Many / Duplicate Notifications' đã có sẵn hướng xử lý trong KB (Settings → Notifications → chọn 'notify only when unread', kiểm tra có nhiều channel notification cùng bật không), nhưng Phoebe không tra và đưa ra hướng xử lý không liên quan, khiến khách vẫn chưa hết vướng mắc tới cuối đoạn chat. (#7)
  - Dẫn chứng: "I am recieving emails every time i reply to the bot, so i get 3-4 emails..." → Phoebe: "Ah, those are the emails from us, not from the Chatty Inbox. You are advised to open a random one and find the Unsubscribe button."
  - → Khi khách phàn nàn về nhận quá nhiều notification/email trùng lặp, tra ngay case notification-issues trong KB trước khi trả lời — hướng đúng là chỉnh Settings → Notifications (notify only when unread) chứ không phải suy đoán nguồn email khác rồi bảo khách unsubscribe.
- **[KN3] Low** — Trả lời về giá Translation thiếu đơn vị rõ ràng ngay từ đầu khiến khách hiểu nhầm thành phí theo tháng, phải mất thêm lượt hỏi lại để làm rõ. (#1)
  - Dẫn chứng: "And the Translation feature is available for the paid plans, 50 for Basic, 300 for Pro and 700 for Plus" → khách hỏi lại "$700 per month? that seems high" → Phoebe phải sửa "Ahhh, 700 conversations. Sorry for that mistake."
  - → Khi nêu số liệu limit/quota, luôn gắn rõ đơn vị ngay trong câu đầu tiên (vd '700 conversations/month') để tránh khách hiểu nhầm sang số tiền, đỡ mất thêm lượt trao đổi.
- **[KN6] Moderate** — Với case email alias phức tạp (support@ là alias của sales@), Phoebe đưa ra hướng xử lý chung chung (gỡ cài đặt lại app) khi chưa xác định rõ nguyên nhân, trong khi nguyên nhân thật (một CS khác phát hiện sau) là lỗi gõ sai domain trong cấu hình alias. (#6)
  - Dẫn chứng: "Sorunu çözmek için uygulamayı kaldırıp tekrar eklemenizi öneririm" (đề xuất gỡ và cài lại app để khắc phục) — trong khi vấn đề thật sự là lỗi chính tả domain (support@boobwellness.com thay vì bobowellness.com), được Linda phát hiện sau đó.
  - → Với case setup/config phức tạp (alias email, domain...), kiểm tra kỹ lại từng field cấu hình (đối chiếu chính tả, domain) trước khi đề xuất giải pháp chung chung như gỡ cài lại app — tránh bắt khách làm thao tác không cần thiết.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **4/4** chat phù hợp (đúng lúc: 4, sai lúc: 0)
- Xin review đúng lúc ở cả 4/4 chat phù hợp (#2, #5, #13, #14) — đều xin ngay khi khách vừa hài lòng/cảm ơn, không có trường hợp xin sai lúc. Chat #14 đặc biệt tốt: khách xác nhận đã để 5 sao ngay trong chat.

📈 **So với tuần trước**
- Điểm 79 → 75 (▼ -4)
- Trục: Mindset 26.8→24.9, Kiến thức 26.5→25.5, Kỹ năng 25.9→24.3
- Lỗi tuần trước đã hết: KN1, QT22 👏
- Lỗi mới tuần này: KN3, KN6, KT2

🔗 **Chat đã QA (16):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cefa0af9-d403-4582-894f-4bbe543bf790|#1 Enveseur> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_5fc3a912-58ce-4b1b-85d0-33d004204572|#2 Damara Day Spa Fallsview Casino Resort> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9f483cc7-4a93-4c00-9b18-cd07e33e33c8|#3 Slate-Lite> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b7a16c25-889b-423e-b89e-2be8b7939593|#4 NOIR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bcf1844c-80e1-4a4b-83d7-690eba68e604|#5 Feed Vapor> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ca132d6a-8bf6-45a8-be82-ac35ceceb54b|#6 BOBO WELLNESS> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6af36054-cf1b-4fa5-bbb4-ddf9fc38f61d|#7 Swimzi> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_05f6cc56-c868-4ec7-87d9-7ac9462cd3af|#8 Hemani Herbal> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9951484f-f289-4b02-acc7-aab00603c1e3|#9 Vils Clothes> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6a72a5a9-97bb-4b3b-ae1d-4bcf86b7bdd7|#10 SKYROVER> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0cfbfc5a-1974-4c19-ab95-398a6bd0c17d|#11 Velobsessive> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_20178de9-cc95-446e-8cf0-c47e994f5f7a|#12 Artstickly shop> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fd08ca42-0eec-45d5-b951-e27da87cd9f7|#13 Bassmera> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f375512c-ac0f-480a-8db9-4dbacd122b60|#14 Frolana Natural> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f04b3fb2-38b9-4eff-9d34-39b824099a69|#15 Di Vincenzo Boutique> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9c48305a-f987-45d8-b413-dd1ef45cd92c|#16 GYM SUPPLEMENTS U.S>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_