# QA Tuần 2026-W22 — Audrey
**26/05 – 01/06** · **91/100 — Tốt** · 18 chat
Phân bố: 🌟2 ✅15 🟡1 🟠0 🔴0 ⛔0

## ✅ Điểm tốt
- [P2] Chủ động phát hiện và xử lý vấn đề khách chưa kịp nêu — tự nhận ra nút loyalty bị nút gift che và nút widget che phần dưới màn hình mobile, đề xuất chỉnh ngay: 'I noticed that the loyalty button is being covered by a gift button. Would you like me to change its position from left to right?' và 'I've just adjusted the widget button on the mobile version so that it does not cover the bottom of the screen.' (chat #4)
- [P3] Giải thích kỹ thuật rõ ràng, có bước, làm khách theo được ngay — hướng dẫn cập nhật SPF record cho GoDaddy, chỉ đúng record cần sửa, ghép include:mailgun.org vào record hiện có và còn tự test gửi mail xác nhận: 'you need to combine your existing record... v=spf1 include:mailgun.org +mx +a +ip4:198.57.247.252 ~all' và 'Let me test it on my end... the email was successfully sent to my inbox' (chat #13)
- [P3] Trả lời câu hỏi về điểm/redeem mạch lạc, dẫn khách tới đúng nơi xem hoạt động — 'these are the redemption activities, so it only displays the points redeemed and the discount code generated on that day' và chỉ rõ kiểm tra coupon từ Shopify Discounts. (chat #2)
- [P5] Đọc kỹ context khi nhận ca từ đồng nghiệp, không bắt khách lặp lại — vào tiếp vụ floating cart của Carl, tự xác định theme, thêm CSS z-index và báo kết quả gọn gàng: 'we've addressed your concern by adding a CSS code to adjust the z-index of our widget button'. Tương tự khi tiếp ca Sonny: 'Sonny's shift is over, so please let me know if you have any further questions'. (chat #18, chat #11)

## 🔧 Cần cải thiện
- [KN1·Low] Gửi nhầm tin nhắn canned không liên quan đến vấn đề của khách. Khách (Alien Surface) đang hỏi về điểm loyalty không bị trừ sau khi refund đơn, nhưng mình gửi email báo 'đã migrate VIP Tiers data sang EU store' — nội dung của một case khác hẳn. May là sau đó mình đã gửi tin đính chính, nhưng khách có thể bị rối.
  - DC: [11:42:19] CS (Audrey): I'm delighted to share with you that we have successfully migrated the customers' VIP Tiers data to your EU store. ... [11:48:09] CS (Audrey): Hi again! I'd
  - → Trước khi gửi mỗi tin canned, đọc lại 1 lần xem nội dung có khớp đúng vấn đề khách đang hỏi không — nhất là các template dài. Nếu lỡ gửi nhầm, đính chính ngay kèm 1 câu xin lỗi ngắn để khách không hiểu lầm.
- [QT18·Moderate] Một vài chat tư vấn xong nhưng kết thúc hơi lửng, chưa chốt rõ bước tiếp theo cho khách. Ở chat #3, khi khách hỏi cách hiện point calculator, mình báo cần nâng cấp plan rồi dừng, chưa hỏi khách có muốn được hỗ trợ nâng cấp / xem hướng dẫn tiếp không.
  - DC: [15:48:00] CS (Audrey): I've checked and noticed that you're currently in the Free plan, while this feature is supported on the Essential plan [15:48:26] CS (Audrey): In this case,
  - → Sau khi báo điều kiện (plan/giới hạn), luôn chốt 1 bước tiếp theo rõ ràng: 'Nếu anh/chị muốn, em có thể gửi link so sánh plan / hỗ trợ set up ngay sau khi nâng cấp nhé' để khách biết nên làm gì tiếp.