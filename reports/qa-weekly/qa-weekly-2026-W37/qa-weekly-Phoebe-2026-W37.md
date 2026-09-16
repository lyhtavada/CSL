# QA Weekly — Phoebe — 2026-W37 (09/09 – 15/09/2026)

**Điểm tuần:** 80/100 — Tốt 👍 — ▲ +2 so với tuần trước (78)
**Đã QA:** 11 chat (loại 1 chat không tính)

## Breakdown 3 trục
- 🧠 Mindset: 27.2/34
- 📚 Kiến thức: 27.3/33
- 🛠️ Xử lý: 25.4/33
- Trục yếu nhất: **🛠️ Xử lý**

## 📝 Nhận xét chung
Tuần này bạn xử lý case khá chắc tay và kiên trì, đặc biệt với khách khó hoặc case kỹ thuật phức tạp (billing tranh chấp của GYM SUPPLEMENTS, case kỹ thuật nhiều lớp của MUS) — bạn verify kỹ trước khi trả lời thay vì đoán, đó là điểm mạnh rõ nhất và cũng là lý do trục Kiến thức/Mindset của bạn ổn. Tuy nhiên trục Kỹ năng xử lý đang là điểm yếu nhất trong 3 trục: có case gửi nhầm hẳn ngôn ngữ khiến khách phải hỏi lại "?!", và nhiều lỗi chính tả/ngữ pháp nhỏ lặp lại ở nhiều ngôn ngữ khác nhau. Đây không phải lỗi kiến thức nhưng làm khách mất thời gian hỏi lại và giảm cảm giác chuyên nghiệp — tuần tới nên đọc lại tin trước khi gửi, đặc biệt khi copy-paste hoặc trả lời nhanh nhiều case cùng lúc.

## ✅ Điểm tốt
- [P2] Kiến thức kỹ thuật sâu và chính xác — giải thích rõ 3 điều kiện để AI nhận biết sản phẩm thuộc collection ("Yes, the AI can tell a product is in the '+30.000 vinilos' collection with 03 conditions..."), và tự cập nhật lại câu trả lời khi tính năng bulk-edit mới ra mắt thay vì để khách chờ. (#10)
- [P1] Ownership tốt với case khó/nhạy cảm — case tranh chấp discount của khách VIP (GYM SUPPLEMENTS, sắp uninstall), bạn không đoán mà yêu cầu screenshot/video để verify từng bước, chủ động hỏi Andy/báo Liz khi vượt khả năng xử lý. (#5)
- [P4] Trình bày rõ ràng, có cấu trúc khi update khách — ví dụ tách 2 vấn đề rõ ràng (page path mismatch + popup setting) kèm ảnh minh hoạ ở chat #1, và trả lời presale nhiều điểm bằng bullet có nguồn tham khảo ở chat #12. (#1, #12)

## 🔧 Cần cải thiện
- **[KN3] (Moderate)** Gửi nhầm tin nhắn tiếng Trung cho khách đang chat tiếng Đức/tiếng Anh, khiến khách hoang mang phải hỏi lại (#8)
  - Evidence: [10:48:40] CS (Phoebe): 感谢您提供的截图。让我为您查看一下 → [10:48:53] Customer (Yelf.): ?!
  - Action: Trước khi gửi, đặc biệt khi copy-paste từ chat khác hoặc dùng template, đọc lại 1 lần để chắc đúng ngôn ngữ/đúng chat đang xử lý.
- **[KN2] (Low)** Trả lời chưa đi thẳng vào câu hỏi trực tiếp của khách, khiến khách phải nhắc lại (#5)
  - Evidence: [15:42:27] Customer: have any link ? → [15:42:50] Customer: read my previous message (trước khi Phoebe mới đưa link cụ thể ở tin sau)
  - Action: Khi khách hỏi cụ thể ("have any link?"), trả lời trực tiếp câu hỏi đó trước, rồi mới bổ sung thêm ngữ cảnh/hướng dẫn liên quan.
- **[KN1] (Low)** Lỗi chính tả/ngữ pháp nhỏ lặp lại nhiều chat, kể cả trong tiếng Anh và tiếng Tây Ban Nha (#4, #6, #10)
  - Evidence: "may I please know if have you received any email" (#4); "please take your tiem" (#6); "admitimos la exportación del transcripción" — sai giống trong tiếng Tây Ban Nha, đúng phải là "de la transcripción" (#10)
  - Action: Đọc lại câu trước khi gửi, đặc biệt câu dài hoặc viết bằng ngôn ngữ không phải tiếng mẹ đẻ, để tránh lặp lỗi làm giảm tính chuyên nghiệp.

## 🌟 Xin review (observe-only, không tính điểm)
- Đã xin review ở 0/1 chat phù hợp
- Chỉ có 1 chat đủ điều kiện xin review trong tuần (#2 — khách cảm ơn sau khi được hỗ trợ), và bạn chưa xin ở chat đó. Không phải lỗi, nhưng có thể tận dụng thêm khi khách vừa cảm ơn/hài lòng.

## 📈 So với tuần trước
- Điểm: 78 → 80

## 🔗 Chat đã QA (12)
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8575f5ae-862c-4dc0-851f-1e2e8788dbb9|#1 Scentsium> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_aa3c49f0-301c-4b03-ba9b-bec469bd768d|#2 Aéraly> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7b7f7dd3-fc7e-489e-b2bb-272bdde022d8|#3 RituelKaizen> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_84efa84a-0bb4-473d-8ecf-a21e4c6a8bf3|#4 LuxxeCoast> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9c48305a-f987-45d8-b413-dd1ef45cd92c|#5 GYM SUPPLEMENTS U.S> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b456bf88-e2a5-4e28-82f1-f24d67d21502|#6 Triple T Outdoors LLC> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_843d4490-edcf-401d-a633-fa862d96f23a|#7 CRAZYGIRL> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7edbf8b2-1e85-41c1-9b46-dca05024128b|#8 Yelf.> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4d2ba00e-4755-470b-a56c-4558756a2eab|#9 Gemini Diamond> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_994cfe87-8c35-4af0-82d2-e50c4d23deb3|#10 MUS> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_02457eaa-f400-4766-ba5a-fef283599f80|#11 vacuéa> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_07ca20af-a55c-44d1-9994-5f483681a4e3|#12 Customercare>
