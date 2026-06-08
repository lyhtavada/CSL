# QA Tuần 2026-W23 — Audrey
**Giai đoạn:** 01/06 – 07/06  
**App:** Joy  
**Điểm:** 83/100 — Tốt (= tuần trước)  
**Đã QA:** 30 chat
**3 trục:** 🧠 Mindset 27.3/34 · 📚 Kiến thức 28.2/33 · 🛠️ Xử lý 27.4/33

## 📝 Nhận xét chung
Tuần này bạn duy trì phong độ ổn định và đều tay — ownership cao trên các case phức tạp kéo dài nhiều ngày (subscription milestones #1, duplicate account #11, past-order sync #20), và có những khoảnh khắc nổi bật rõ rệt như giải thích root cause gọn sau khi merge tài khoản, hay chủ động tổng hợp outstanding items trước ngày launch. Điểm cần tập trung: lỗi KN6 (assume sai store/context trước khi đọc kỹ) vẫn xuất hiện ở chat #2 — đây là pattern lặp từ W22, cần ưu tiên sửa; và câu trả lời về milestone logic ở chat #27 vẫn thiếu điểm mấu chốt về start date, dễ khiến khách hiểu nhầm.

## ✅ Điểm tốt
- **[P2]** Ownership mạnh trên case đa ngày: chủ động tổng hợp 3 outstanding items (Loyalty Hub, Notification, Widget Consolidation) thành status update có cấu trúc rõ ràng trước ngày launch của khách. (#1)
- **[P3]** Proactive và chính xác trong tư vấn Advanced Rule Engine — giải thích priority logic đúng, verify lại config sau khi khách chỉnh, xác nhận tính toán điểm cụ thể (450 points) trước khi đóng case. (#3)
- **[P1]** Ownership xuất sắc trên case duplicate account: merge tài khoản nhanh, giải thích root cause rõ (guest checkout vs Shopify account ID tạo 2 Joy records), review ask đúng lúc ngay sau khi khách xác nhận mọi thứ ổn. (#11)
- **[P2]** Xử lý case phức tạp nhiều yêu cầu song song hiệu quả: sync past orders, giải thích coupon limit at checkout (Shopify Plus only), hướng dẫn VIP tier benefits — giữ flow gọn và khách hài lòng xuyên suốt. (#20)
- **[P3]** Tư vấn API và giải pháp thay thế rất chất lượng: xác nhận API chỉ có ở Ultimate ($499/tháng), đề xuất 2 phương án cụ thể ở Advanced (Custom Program POS trigger vs API exception + Revamp), chủ động hỏi rõ thêm về payment method và workflow trước khi tư vấn. (#6)

## 🔧 Cần cải thiện
- **[KN6 · Moderate]** Assume sai store/context trước khi đọc kỹ thông tin khách đã cung cấp — khiến khách phải đính chính và chat kéo dài thêm nhiều vòng không cần thiết.
  - *Dẫn chứng:* Ah, asumo que te gustaría cambiar el enlace de inicio de sesión para este sitio web https://aguascalientes-travel.myshopify.com/password (#2)
  - → Trước khi đưa ra action item, tóm tắt lại hiểu của bạn bằng 1 câu ('Bạn muốn đổi link button trên store nekane.mx, đúng không?') thay vì tự suy và assume luôn — khách đã nói rõ nekane.mx từ trước đó.
- **[KN3 · Low]** Câu trả lời về milestone logic thiếu điểm mấu chốt quan trọng nhất: ảnh hưởng của start date. Nếu milestone có start date, chỉ purchases từ ngày đó mới được tính — đây là điểm khách hay hiểu nhầm nhất và Audrey không đề cập.
  - *Dẫn chứng:* I'd like to inform you that deleting and recreating a milestone program will not reset your customers' historical purchase data. Joy reviews the customer's history in your store to determine whether they qualify. (#27)
  - → Khi trả lời về milestone/tier logic liên quan đến historical data, luôn thêm 1 câu về start date: 'Lưu ý nếu bạn set start date cho program mới, chỉ purchases từ ngày đó mới được tính — nếu muốn tính lại toàn bộ lịch sử, để start date trống hoặc đặt về ngày rất xa trong quá khứ.'
- **[QT25 · Low]** Để khách chờ gần 30 phút cho một câu hỏi how-to đơn giản về POS (khách hỏi cách tốt nhất để khách hàng xem điểm qua POS-only store) mà không có tin nhắn trung gian báo đang check.
  - *Dẫn chứng:* Sure thing! Please allow me some time to check it for you — [26 phút im lặng] — Hi again! Thank you for waiting! (#29)
  - → Với câu hỏi how-to chung (không cần tra store), reply trong 5-10 phút. Nếu cần thêm thời gian, báo ngay: 'Mình cần thêm khoảng X phút để kiểm tra, mình sẽ quay lại ngay.'

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin review ở **4/6** chat phù hợp (4 đúng lúc, 0 chưa đúng lúc).
- Bạn xin review đúng lúc ở 4/6 chat phù hợp — ngay sau khi khách xác nhận hài lòng (#3 G2 review, #4 Shopify review, #11 sau merge account, #20 sau sync past orders). Còn bỏ lỡ khoảng 2 chat khách happy mà chưa xin (#7 khách hài lòng sau khi SpringGlass issue được giải thích, #24 sau khi widget bug được fix và khách confirm OK).

## 📈 So tuần trước
Điểm tuần này giữ nguyên so với W22 (83 → 83). KN6 (assume sai context) lặp lại từ W22 — đây là pattern cần ưu tiên sửa tuần tới. Điểm tích cực: KN2 (hỏi lại không cần thiết) và QT22 (bỏ sót câu hỏi) không còn xuất hiện rõ rệt — tiến bộ tốt. KN3 về milestone start date vẫn là điểm yếu dai dẳng từ W22 cần attention.
