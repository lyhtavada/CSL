# QA Weekly — Sonny — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 80/100 — Tốt  (▼ -9)  
**Đã QA:** 30 chat

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 26.7/34 |
| 📚 Kiến thức | 26.9/33 |
| 🛠️ Xử lý | 26.4/33 |

## 📝 Nhận xét chung

Tuần này bạn ôm khối lượng chat lớn và nhiều case thuộc dạng khó — bug kỹ thuật phức tạp, khách bực bội, dự án custom dài hơi — và nhìn chung xử lý chắc tay, kiên nhẫn, không né việc; đây là điểm mạnh rõ nhất, thể hiện đậm nét ở chat #10 và #23 khi khách nói nặng lời mà bạn vẫn giữ bình tĩnh giải thích tới cùng. Tuy nhiên phải nói thẳng: ở chat #22 bạn báo NGƯỢC chiều giá cũ/giá mới của gói Essential ($29 là giá mới chứ không phải giá cũ như bạn nói) — đồng nghiệp phải chữa ngay trong chat, đây là lỗi kiến thức nặng nhất tuần vì có thể khiến khách ra quyết định nâng cấp/downgrade dựa trên thông tin sai. Hướng cần tập trung tuần tới: (1) luôn double-check chiều giá cũ/mới trước khi trả lời billing, (2) khi khách xin compensation/giảm giá, chốt rõ ai xử lý và mốc thời gian phản hồi thay vì nói chung chung.

## ✅ Điểm tốt tuần này

- Kiên nhẫn/ownership xuất sắc với khách khó và bực bội — chat #10 (KH nói "Your screenshots are useless", "time to switch to smile.io", "very disappointed with you") Sonny vẫn bình tĩnh giải thích lại nhiều lần không phản ứng tiêu cực và không né việc; chat #23 (bug kéo dài hơn 1 tuần, KH bực nhiều lần) vẫn theo tới cùng, không đóng chat lửng. (#10, #23)
- Chủ động nghĩ xa hơn câu hỏi của khách — tự đề xuất giải pháp/workaround phức tạp (Milestone + Shopify Flow cho case custom "Style Asset Eligible" ở #15; chủ động sửa AI trả lời sai về free plan/loyalty page ở #14 trước khi khách phát hiện). (#15, #14)
- Kiến thức kỹ thuật vững ở case khó — điều tra domain/OAuth/TikTok in-app browser rất bài bản, có test kèm video chứng minh app không phải nguyên nhân (#3); giải thích đúng cơ chế currency bug do order import (#23). (#3, #23)
- Mời review đúng lúc, tự nhiên — luôn hỏi ngay sau khi khách vừa khen/cảm ơn xong việc, không gượng ép (#7, #21). (#7, #21)

## 🔧 Cần cải thiện

- **[KT1] Critical** — Báo sai chiều giá cũ/giá mới của gói Essential — nói $29/tháng là giá CŨ trong khi đây thực tế là giá MỚI (hiệu lực từ 9/2), giá cũ grandfathered đúng ra chỉ khoảng $24.90-24.99/tháng. Đồng nghiệp (Andrew) phải sửa lại ngay trong cùng chat. (#22)
  - Dẫn chứng: [08:19:15] CS (Sonny): "是的，您目前使用的是我们Essential计划的旧价格，费用为$29/月" → [08:20:59] CS (Avada/Andrew follow-up): "您目前的套餐是Joy Pro，基础费用为每月$24.99"
  - → Trước khi báo giá/plan, luôn xác nhận chiều đúng: giá cũ (grandfathered) LUÔN thấp hơn giá hiện hành trên KB, không phải ngược lại. Khi không chắc cohort, hỏi lại đồng nghiệp/leader trước khi trả lời khách để tránh gây hiểu nhầm về billing.
- **[QT18] Moderate** — Khi khách 2 lần chủ động xin giảm giá 2 tháng vì lỗi hệ thống kéo dài hơn 1 tuần, Sonny chỉ trả lời chung chung sẽ "báo team" mà không chốt ai xử lý hay khi nào có phản hồi, khiến yêu cầu billing nhạy cảm bị treo lửng. (#23)
  - Dẫn chứng: [15:48:31] Customer: "ok, please discount me 2 months since this is taking so long because of those errors" → [15:49:59] CS (Sonny): "I will let the Joy internal team know about your feedback. Thank you for your patience."
  - → Với yêu cầu compensation/billing, chốt rõ: ai sẽ xử lý (leader/billing team) và mốc thời gian khách sẽ nghe phản hồi, thay vì câu trả lời chung chung dễ gây cảm giác bị lờ đi.
- **[KN1] Low** — Gửi trùng lặp y hệt 1 câu 2 lần liên tiếp, thiếu chuyên nghiệp dù không ảnh hưởng nội dung tư vấn. (#19)
  - Dẫn chứng: [08:47:07] CS (Sonny): "感谢您的理解"  [08:47:20] CS (Sonny): "感谢您的理解" (gửi lặp lại nguyên văn)
  - → Rà lại tin nhắn trước khi gửi, tránh gửi trùng do thao tác nhanh.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **5/7** chat phù hợp (đúng lúc: 5, sai lúc: 0)
- Xin review đúng lúc ở 5/7 chat phù hợp — luôn hỏi ngay sau khi khách vừa cảm ơn/khen xong (#2, #4, #7, #11, #21), không có ca nào xin sai lúc. Bỏ lỡ 2 chat khách đã cảm ơn xong mà chưa mời (#12, #29) — case ngắn, dễ quên chốt cuối.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 89 → 80 (▼ -9)
- Lỗi lặp lại từ 2026-W28: KN1 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: KN3, QT25 👏
