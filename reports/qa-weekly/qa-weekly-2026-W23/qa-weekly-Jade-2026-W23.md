# QA Tuần 2026-W23 — Jade
**Giai đoạn:** 01/06 – 07/06  
**App:** Chatty  
**Điểm:** 82/100 — Tốt (▼ -2 so tuần trước)  
**Đã QA:** 30 chat
**3 trục:** 🧠 Mindset 27.0/34 · 📚 Kiến thức 27.5/33 · 🛠️ Xử lý 27.1/33

## 📝 Nhận xét chung
—

## ✅ Điểm tốt
- **[P1]** 
- **[P2]** 
- **[P3]** 
- **[P4]** 

## 🔧 Cần cải thiện
- **[KN6 · Moderate]** 
  - *Dẫn chứng:* CS (Jade): 'You can try reloading the app page many times/ clearing the browser's cache, and then accessing the Chatty app again to check if the issue can be addressed.' — Customer had sent 'Please help me fix 404 page' 3 times with NO additional context. This is the same bot trigger pattern flagged in W22 chat #21.
  - → Khi khách lặp đúng một câu nhiều lần mà không bổ sung thông tin, dừng lại và xác nhận ý định thật: 'It looks like this might be a preset trigger phrase — could you tell me specifically which section or page you're having trouble with?' Lỗi này đã xuất hiện tuần trước (W22 #21) — cần đặc biệt chú ý.
- **[KN3 · Low]** 
  - *Dẫn chứng:* CS (Jade): 'Thank you, and you can consider other possible solutions, and this is our recommendation if you would like to provide customers with free gift coupon codes via the Joy app.' — Khách đã nói rõ 'I don't want them to redeem the code through Joy / I can provide that separately' nhưng Jade không đưa ra hướng giải quyết thay thế cụ thể.
  - → Khi khách clarify rằng họ không muốn dùng tính năng Joy để phân phối coupon, hãy xác nhận: 'Got it — so you'd like customers to access a separate discount code independently without going through Joy's redeem flow. In that case, you can create the discount codes in Shopify Discounts and share them directly. The Buy button will be hidden by the CSS we added, and customers use the discount code at checkout.' Tránh để khách cảm giác bị đẩy ngược về đề xuất cũ.
- **[KN7 · Low]** 
  - *Dẫn chứng:* In chat #14 (Amer), Jade's guidance on email marketing integration was high-level without concrete step-by-step instructions or a direct link to relevant settings/docs.
  - → Khi giải thích tính năng có nhiều bước cài đặt, luôn kèm theo: (1) navigation path cụ thể (Settings > ... > ...), (2) screenshot hoặc link docs, (3) next step rõ ràng. Câu trả lời generic không giúp được khách tự thực hiện.
- **[QT_review_ineligible · Low]** 
  - *Dẫn chứng:* Chat #24 (Modern Shade) và #26 (MAMAMIUM): cả 2 chat đều có header 'ĐÃ CÓ review (không cần xin)' nhưng Jade vẫn xin G2 review. Dù G2 ≠ Shopify review, nhóm này đã được tag không cần xin.
  - → Kiểm tra review tag trước khi xin. Nếu chat đã có tag 'ĐÃ CÓ review', bỏ qua bước xin review trong lần này. Nếu muốn cross-platform (Shopify → G2), cần xác nhận với team trước về policy.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin review ở **2/2** chat phù hợp (1 đúng lúc, 1 chưa đúng lúc).
- Đã xin review ở 2/2 chat phù hợp. Lưu ý: có 2 chat đã có review rồi mà vẫn xin lại (#24, #26) — chat đã có review thì không cần xin nữa, tránh làm phiền khách.

## 📈 So tuần trước
Điểm giảm nhẹ 82 vs 84 (W22). KN6 lặp lại từ tuần trước (chat #30 vs W22 #21 — cùng pattern bot trigger). KN3 và KN7 cũng lặp lại dạng nhẹ hơn. Mặt khác, không có lỗi QT9 (hỏi lại thừa) hay KN1 (grammar) tuần này — cải thiện rõ ở 2 điểm đó. Điểm mạnh ownership và proactive value-add tiếp tục ổn định.
