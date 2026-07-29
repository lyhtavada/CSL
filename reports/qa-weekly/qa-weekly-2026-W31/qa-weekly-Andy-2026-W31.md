# 📋 QA TUẦN — BÁO CÁO CỦA Andy
🗓️ Tuần 2026-W31 · 22/07 – 28/07/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 81/100 — Tốt  (▼ -4 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 27.0/34 · 📚 Kiến thức: 27.7/33 · 🛠️ Xử lý: 26.0/33

📝 **Nhận xét chung**
Tuần này Andy thể hiện phong cách làm việc rất có trách nhiệm — theo sát các ca kỹ thuật phức tạp (email forwarding, WhatsApp, bug đồng bộ dữ liệu/tin nhắn lẫn khách) qua nhiều giờ, nhiều ca làm việc, luôn quay lại đúng hẹn và báo cập nhật rõ ràng thay vì im lặng bỏ đó — đây là điểm mạnh nổi bật nhất. Kiến thức về giá/plan chính xác, khớp KB ở tất cả các case được kiểm (Plus $199/1000 conv, Pro 10 members, 7-day trial...). Điểm cần thẳng thắn nhìn nhận: bạn còn hơi máy móc khi khách đã nói rõ ý muốn nhiều lần (case Simplex Glow: khách xác nhận huỷ subscription "hơn 10 lần" mà bạn vẫn lặp lại yêu cầu xác nhận theo policy, khiến khách bực thêm và hệ thống phải flag "nên chuyển người" 2 lần) — hệ quả là kéo dài chat và làm khách cảm thấy không được lắng nghe. Ngoài ra có vài lỗi chính tả nhỏ và 1 lần mời review dù khách đã có review từ trước (không kiểm tra header) — nhỏ nhưng cho thấy cần cẩn thận hơn ở chi tiết. Hướng tập trung tuần tới: khi khách đã confirm rõ ràng, xử lý ngay thay vì hỏi lại theo quy trình cứng nhắc, và tận dụng tốt hơn khoảnh khắc khách khen ngợi để xin review (bỏ lỡ 2 chat vàng tuần này).

✅ **Điểm tốt tuần này**
- [P1] Ownership rất tốt — theo case kỹ thuật phức tạp xuyên nhiều giờ/nhiều ca, luôn quay lại đúng hẹn báo update thay vì im lặng (email forwarding kéo dài cả buổi, bug đồng bộ tin nhắn lẫn khách) (#2, #3, #5, #27)
- [P4] Trung thực, không overpromise khi chưa chắc — ví dụ từ chối xác nhận thông tin ngoài thẩm quyền thay vì nói bừa cho khách vui (#3)
- [P2] Kiến thức giá/plan chính xác, khớp KB ở mọi case được kiểm (Plus $199/1000 conversations, Pro 10 team members, 7-day trial) (#3, #4, #7)
- [P1] Giữ bình tĩnh, không mất kiên nhẫn dù khách rất bực vì bug nghiêm trọng (tin nhắn bị gửi nhầm cho khách khác, dữ liệu bị xáo trộn) (#21, #27, #30)

🔧 **Cần cải thiện**
- **[KN2] Moderate** — Lặp lại yêu cầu xác nhận dù khách đã nói rõ ý muốn nhiều lần, làm khách bực và kéo dài chat (#17)
  - Dẫn chứng: Khách: "cancel and delete i dont need your service again please i have confirmed more than 10 times" — Andy: "Due to our company policy, we need your confirmation before apply the change to your subscription plan"
  - → Khi khách đã confirm rõ ràng (nhất là lặp lại nhiều lần), xử lý ngay thay vì lặp lại câu hỏi xác nhận theo quy trình cứng nhắc — có thể xác nhận 1 câu ngắn gọn rồi làm luôn.
- **[KN1] Low** — Lỗi chính tả nhỏ trong câu trả lời khách (#11)
  - Dẫn chứng: "CS (Andy): Absolultey"
  - → Đọc lại câu ngắn trước khi gửi, đặc biệt khi trả lời nhanh.
- **[QT-review] Low** — Mời khách để lại review dù chat header ghi khách đã có review rồi, gây thừa/có thể làm phiền (#7)
  - Dẫn chứng: Header: "Review: ĐÃ CÓ review (không cần xin)" nhưng Andy vẫn gửi: "would you mind spending a few moments sharing your feedback about our app and support via this link..."
  - → Check nhanh trạng thái Review ở đầu chat trước khi mời review để tránh hỏi thừa.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **4/6** chat phù hợp (đúng lúc: 4, sai lúc: 0)
- Xin đúng lúc ở 4/6 chat khách hài lòng phù hợp (#2, #4, #10, #11) — bỏ lỡ 2 chat vàng khách khen ngợi nhiệt tình mà không xin (#3, #5). Có 1 lần xin thêm ở chat #7 dù khách đã có review từ trước (không tính vào eligible), hơi thừa nhưng không gây khó chịu.

📈 **So với tuần trước**
- Điểm 85 → 81 (▼ -4)
- Trục: Mindset 29.5→27.0, Kiến thức 27→27.7, Kỹ năng 28.5→26.0
- Lỗi lặp lại: KN1 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: KT1 👏

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_45fd308b-100e-404d-8f99-a9e1c75cee1b|#1 AB Medical> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_224197ab-c751-4596-8bf1-dcb32a4bb5a3|#2 Canvas Art Barn> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7d0f45de-130b-4f1b-af22-3ef0dd2af237|#3 visitor3647040> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bfc84b36-8e58-4733-b1dd-79ff2fde7c1a|#4 ogawa coffee> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cefa0af9-d403-4582-894f-4bbe543bf790|#5 Enveseur> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b3d059d2-e5bd-4807-869e-b18b0c8fd1f3|#6 ARGANOUR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d5793d88-e811-46af-8290-5d3e11fb4a94|#7 SGI> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_5b152a14-5c80-45ed-a4c5-e45d9b7b19e1|#8 Innovative Computers Limited> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a0b16a35-a74e-4082-851d-ba9d53ca5c92|#9 TTLIFE OXYGEN CONCENTRATOR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1b68ebdd-c786-4dd9-ac83-4757f7e055ba|#10 CISSEY CLOTHING> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_abde44a4-d88b-47c3-a39a-a9fd1e9e344b|#11 Cuura Malaysia Sdn Bhd> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e9eab1c2-6066-4356-bd75-677f8c9753bb|#12 Kaycee Corporation> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d9272f6d-edd0-4cef-a300-a4ec2947a7bd|#13 My Veloraa> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_186bdc89-bf2b-4f02-9f55-87266cdac977|#14 Cuura Malaysia Sdn Bhd> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_765129d2-eb6d-4039-917c-0dacec58c4ed|#15 Endnutrition.com> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_dcae370d-5203-41cb-882c-356e4341795a|#16 lankeleisi.eu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bb928895-c91f-46e6-9c46-1718fa15e4e6|#17 Simplex Glow> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0605080a-9210-4642-ab5e-fdce716ce960|#18 Sana Kubi> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f23c1358-5382-4b03-9fe9-cb7c39fb072b|#19 VARON-FR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a45e1cdf-e24d-457d-b0ce-450a67e5d733|#20 Dessclusive> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_05b3d75c-6c44-47ab-8ac3-b028130cd781|#21 Daixidreadology> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b7cbab74-f54d-4aa9-aa28-0524769e3f6a|#22 Lumiere Hair> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ecd4fbef-17e7-4f48-8013-13ac74956eb2|#23 Golden Key Rent Car LLC> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ed330aba-4496-4092-8fb0-3c89798ac4bc|#24 Soft Mozart> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_efad6231-25c6-421c-9cdf-d22a42ce9f56|#25 GET VELLARA> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8a07ed1e-9b43-4fed-ae0d-2cb429c95566|#26 TRYSHOPPY > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8ded1ddc-e6f2-4e6b-be73-b51fe8bff833|#27 LIVALL RIDING> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f35d02fa-046e-4063-9834-1a32707a2761|#28 FPDL Supplies> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_dc4ae619-d78a-41c6-b473-8db90f83976d|#29 Banglez Bazar > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_74c6c964-2466-4f2e-b021-a7ebe1e68af4|#30 OuiSi>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_