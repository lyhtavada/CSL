# 📋 QA TUẦN — BÁO CÁO CỦA Jade
🗓️ Tuần 2026-W32 · 29/07 – 04/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 83/100 — Tốt  (— 0 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 27.9/34 · 📚 Kiến thức: 28.1/33 · 🛠️ Xử lý: 27.1/33

📝 **Nhận xét chung**
Tuần này Jade xử lý khối lượng chat rất lớn và đa dạng (Joy, Chatty, Wishlist, nhiều ngôn ngữ), phong cách làm việc chắc tay, ownership rõ — nhiều case kéo dài nhiều ngày (deliverability email, DMARC, milestone coupon, referral) bạn đều bám sát tới cùng, không đẩy việc, đây là điểm mạnh nổi bật nhất. Nhưng có 2 lỗi cần sửa ngay: ở chat #6 bạn báo sai giá — nói Essential plan có 1000 orders miễn phí/tháng trong khi KB ghi rõ chỉ 500/tháng, ngay sau khi khách xác nhận volume ~1000 đơn để chọn plan — đây là lỗi kiến thức nghiêm trọng, dễ khiến khách bất ngờ phí overage sau này và cần Liz review lại case này. Ở chat #9 (case GDPR nhạy cảm, khách đang căng thẳng), bạn hỏi lại đúng điều khách đã xác nhận khiến khách phải lặp lại trong bực bội — cần đọc kỹ lại toàn bộ context trước khi hỏi, đặc biệt với khách đang khó chịu. Hướng tập trung tuần tới: luôn double-check số liệu giá/quota với KB trước khi tư vấn plan, và rà lại tin nhắn trước đó trước khi đặt câu hỏi để tránh hỏi trùng.

✅ **Điểm tốt tuần này**
- [P1] Ownership rất tốt với case dài nhiều ngày — chat #2 (đồng bộ email/DMARC, warm-up campaign) bạn theo dõi liên tục suốt ~1 tuần, luôn cập nhật chủ động dù case bị đẩy qua nhiều bước kỹ thuật, không để khách phải hỏi lại tiến độ. (#2, #28)
- [P3] Chủ động đề xuất thêm ngoài câu hỏi khách — chat #1 chủ động quay video demo redeem points, chat #29 chủ động phát hiện và hỏi khách có muốn chỉnh luôn phần 2 widget chưa canh chỉnh dù khách chỉ hỏi 1 vấn đề. (#1, #29)
- [P5] Giải thích kỹ thuật rõ ràng, có cấu trúc — chat #1 so sánh store credit vs points mạch lạc, chat #11 giải thích cơ chế referral/milestone coupon từng bước dễ hiểu. (#1, #11)

🔧 **Cần cải thiện**
- **[KT1] Critical** — Tư vấn sai giá/quota Joy Essential plan — nói 1000 orders miễn phí/tháng trong khi KB ghi rõ chỉ 500 orders/tháng (overage $15/100), ngay sau khi khách xác nhận volume ~1000 đơn/tháng để chọn plan. (#6)
  - Dẫn chứng: CS (Jade): "I think the Essential plan (POS option enabled) would be a suitable package, since on this plan, you will have up to 1000 free orders/month." — KB pricing.md: Essential = 500 free orders/mo.
  - → Luôn mở KB pricing (fetch_kb.py joy kb/reference/pricing.md) để chốt số liệu chính xác trước khi tư vấn plan, đặc biệt khi khách đang cân nhắc dựa trên volume đơn hàng.
- **[KN2] Moderate** — Hỏi lại đúng điều khách đã xác nhận trong case GDPR nhạy cảm, khách phải lặp lại trong bực bội. (#9)
  - Dẫn chứng: Customer: "ich sagte doch bereits, dass ich die Daten aus dem System gelöscht habe!" (tôi đã nói rồi là tôi đã xóa dữ liệu khỏi hệ thống!) — sau khi Jade hỏi lại đúng câu khách vừa xác nhận ở tin trước, thậm chí gửi trùng 2 lần cùng 1 câu hỏi.
  - → Đọc lại kỹ tin nhắn gần nhất của khách trước khi đặt câu hỏi tiếp theo, đặc biệt với khách đang căng thẳng/khiếu nại — tránh hỏi lại thông tin đã có.
- **[KN3] Low** — Trả lời khó hiểu khiến khách phải hỏi lại để làm rõ. (#8)
  - Dẫn chứng: CS (Jade Nguyen): "You cannot I'd like to inform you that" → Customer: "can or cannot ?"
  - → Viết câu trả lời trực tiếp, đặt kết luận (can/cannot) lên đầu câu thay vì cấu trúc lộn xộn.

🚨 **Severe flags — Liz xem trước khi gửi**
- KT1 — chat #6: báo sai quota Joy Essential plan (1000 vs thực tế 500 orders/tháng theo KB) khi khách đang quyết định plan dựa trên volume đơn hàng, cần Liz review trước khi DM

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **1/4** chat phù hợp (đúng lúc: 0, sai lúc: 1)
- Chỉ 1/4 chat phù hợp có xin review (chat #27), và lần đó xin ngay sau khi vừa gửi fix chưa được khách xác nhận đã hoạt động — hoá ra khách quay lại báo vẫn còn lỗi khác, hơi vội. Phần lớn chat còn lại khách cảm ơn/hài lòng nhưng Jade không chủ động xin review (để bot Ivy/Joyce xin thay hoặc bỏ qua).

📈 **So với tuần trước**
- Điểm 83 → 83 (— 0)
- Trục: Mindset 28.1→27.9, Kiến thức 28.6→28.1, Kỹ năng 26.7→27.1
- Lỗi tuần trước đã hết: KN1, KN7 👏
- Lỗi mới tuần này: KN2, KN3, KT1

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_894f5998-cde6-47bf-b4d6-840bc8bd1deb|#1 Orsolya Lele> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2e758c4c-f7e3-4be8-9612-d3e32e26a1b8|#2 Tian Zhao> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_193b8bef-9be7-4360-a323-33576213b38a|#3 wilson wu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_16dd95bf-4055-4cd4-87e2-9352b108eb2b|#4 Rena Blöhß> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9af8819e-e609-41ed-87cd-a58c471e3f57|#5 Purki Jewels> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7eaff53b-1d6a-4af7-b8b9-c93447720c00|#6 Tyler Crook> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_14cefa8a-5f59-4c58-a1fb-3ff8e69fb6cc|#7 DragonShock> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ce2ae69a-d1d6-4e1c-bf11-e90e4c79b030|#8 Magnus Rolstad> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d26db0e1-24c8-4161-8688-850b0506e6af|#9 Susanne von Lauenstein> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_13ecfca4-e90b-4ec4-ba5a-401e5fdaab0c|#10 Airmaster Fan Company> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cd81ac62-b4ee-4256-bc43-62aa3059b5e1|#11 Nissoplus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0d27ab70-bde3-4f89-92d2-3de38f7b8719|#12 Zhibin Zou> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b3d059d2-e5bd-4807-869e-b18b0c8fd1f3|#13 ARGANOUR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ba861373-81a1-4801-9720-c3d14a09f722|#14 caiwu jigao> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_596ee1d6-9ce8-4aa2-93df-e98fb060fe75|#15 Resin Society > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_da66d2e3-5d10-4d4c-bf15-694fc29da22c|#16 N&L ESSENTIALS> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2dbdde1a-8bc6-4a7c-aae9-69ea46e6d372|#17 Daniele Zuliani> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bb140945-7f94-4132-9698-1de2c37b7edd|#18 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_05f6cc56-c868-4ec7-87d9-7ac9462cd3af|#19 Hemani Herbal> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_da5a49b0-0fc4-425d-8d45-e5aa2409251c|#20 visitor3639480> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_238a3a60-b817-4faf-b7b2-18f830d1397f|#21 IJMAL CHANNEL> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ef4626fd-8759-48cf-af83-d8a1c5951736|#22 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d6265ab8-2712-496a-9e5c-4092dc362558|#23 Abtin & Co. > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e5ab723f-ad1c-4f60-b014-72c9c015d556|#24 Hans Chan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_260645fb-a4e4-417c-a400-c61e7b891aa1|#25 visitor3653469> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1dcbd01e-3243-4b88-9261-eed58a54491d|#26 Denti Care Enterprizes> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_11347cab-7202-4bd1-ae6f-204c79f7ea41|#27 The Low Vision Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_79815bb8-c235-4837-a5c9-3671d432183d|#28 Aaron Olinyk> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_980074d7-f70d-4ab8-a1b3-db6e970480d7|#29 Cuura Malaysia> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_347e2400-ef11-4725-b8b5-7db91fd1e877|#30 Justin Wong>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_