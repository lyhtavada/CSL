# QA Tuần 2026-W22 — Andy
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 81/100 — Đạt  
**Đã QA:** 26 chat  
**Phân bố:** 🌟2 ✅19 🟡0 🟠5 🔴0 ⛔0

## 📝 Nhận xét chung
Bạn nhiệt tình và gánh được khối lượng chat lớn. Nhưng điểm đáng lưu ý: nhiều chat dính lỗi nhỏ lặp lại về quy trình và diễn đạt (5 chat ở mức Minor) — gộp lại kéo điểm xuống rõ. Đây là lỗi 'chất lượng đồng đều', không phải lỗi nặng đơn lẻ. Cần sửa: chăm chút phần chốt chat — báo khách bước tiếp theo rõ ràng trước khi đóng, đừng để lửng.

## ✅ Điểm tốt
- **[P3]** Xử lý request đổi support email từng bước rất gọn và rõ — confirm email muốn nhận noti, gửi verification, test noti, rồi chủ động transfer admin role. KH làm theo được ngay, không phải hỏi lại. (chat #5)
- **[P2]** Chủ động làm hơn KH yêu cầu: tự sync products xong còn 'added the important URLs I could find on your website to the AI knowledge base' và nhờ KH check thiếu sót — giúp AI train tốt hơn mà KH chưa kịp xin. (chat #2, chat #5)
- **[P5]** Trả lời chính xác các câu hỏi plan/limit phức tạp đúng KB: Free 100 products + random activate, Basic 12 tháng vs Free 90 ngày chat history, Pro 300 AI conversations/tháng (cả gói năm) + $0.4/extra. Không sai con số nào. (chat #22, chat #8)
- **[P1]** Tone ấm, kiên nhẫn xuyên suốt nhiều ngôn ngữ (Đức, Nhật, Ý) và nhiều ca dài. KH House Of Beyond thúc giục liên tục ('Did you check? Andy') vẫn giữ bình tĩnh, KH cuối chat khen và chào thân thiện. (chat #9, chat #13, chat #25)

## 🔧 Cần cải thiện
- **[QT10 · Moderate]** Đề nghị review kèm phần thưởng (free month) — vi phạm policy Shopify/G2 trong ref_ask-for-review: 'Strictly Prohibited — Offering anything in exchange for a review (discounts, free months, perks)'.
  - *Dẫn chứng:* chat #18: 'https://www.g2.com/products/chatty/take_survey  As a thank you, we're delighted to offer you a free month for Basic and Pro plans. Just send us a quick screenshot after submitting it...' — 
  - → Bỏ hẳn phần 'free month/discount để đổi review'. Dùng template review trung tính đã được duyệt (không gắn quà). Nếu có chương trình G2 incentive riêng thì tách khỏi lời mời review, đừng gộp 'review → get free month'.
- **[QT10 · Moderate]** Hướng dẫn KH nội dung review ('mention Andy') — policy cấm 'Telling the merchant what to write or guiding the content'.
  - *Dẫn chứng:* chat #9: 'If possible, hope you mention "Andy" in the review :P'; lặp lại ở chat #18: 'If possible, hope you mention "Andy" in the review :$'
  - → Không gợi ý KH viết gì hay nhắc tên mình trong review. Chỉ gửi link review trung tính rồi cảm ơn, để KH tự do viết.
- **[QT10 · Moderate]** Pre-screen cảm xúc trước khi xin review ('a tiny favor') — policy cấm 'Pre-screening for sentiment before asking (may I ask a favor?)'. Có lúc còn xin review khi task vẫn đang chờ tech team.
  - *Dẫn chứng:* chat #12: 'Ahh, while you are still here, could I ask for a tiny favor, please? :P' (xin review trong khi icon-resize task chưa xong); chat #26: 'Ahh, while you are still here, could I ask for a tiny 
  - → Theo 4-step flow: hỏi 'Is there anything else I can help with?' và chốt KH hết vấn đề trước, rồi gửi thẳng lời mời review trung tính — không mở đầu bằng 'may I ask a favor'. Đừng xin review khi còn task pending.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh. (Lưu ý: điểm này chỉ dựa trên nội dung chat với khách — chưa gồm phối hợp TS/dev, tạo & follow-up ticket, bàn giao ca hay xin review thực tế; không phải đánh giá năng lực toàn diện.)