# QA Tuần 2026-W24 — Jade
**App:** Chatty · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 83/100 — Tốt  (▲ +1 so với W23: 82)
- 🧠 Mindset 27.4/34 · 📚 Kiến thức 27.9/33 · 🛠️ Xử lý 27.7/33
- 🔍 Đã QA: 30 chat
- Trục yếu nhất: **Mindset**

## 📝 Nhận xét chung
Tuần này Jade giữ được phong độ ổn định — ownership tốt, biết tạo ticket đúng lúc và follow-up chủ động. Điểm nổi bật là xử lý đa ngôn ngữ (tiếng Anh, Trung, Thổ Nhĩ Kỳ, Hàn, Thái) mượt mà và không hề lúng túng. Những chat ngắn cuối tuần (từ #28 trở đi) kéo điểm xuống vì Jade chỉ vừa vào thì hết session — không phải lỗi của Jade. Hướng cải thiện tuần tới: khi tiếp nhận vấn đề phức tạp từ khách, confirm lại yêu cầu cụ thể trước khi đưa ra đề xuất thay vì để dev loop lại sau.

## ✅ Điểm tốt
- Ownership + chủ động follow-up: nhiều chat Jade không chỉ xử lý xong rồi đóng mà còn gửi email cập nhật kết quả sau khi tech team hoàn thành (#3, #13, #21). Đây là dấu hiệu rõ của CS hiểu rằng case chưa xong cho đến khi khách xác nhận. (#3 #13 #21)
- Xử lý import khách hàng quy mô lớn (#4): Jade tự chuẩn bị file, phát hiện data mismatch (9237 vs 7059 customers), phối hợp với TS, và thông báo tiến độ rõ ràng. Chủ động và kỹ lưỡng trong case phức tạp. (#4)
- Đa ngôn ngữ mượt mà: Jade xử lý chat tiếng Trung (#6, #10, #27), tiếng Thổ Nhĩ Kỳ (#8), tiếng Hàn (#17), tiếng Thái (#27) tự nhiên, không bị gián đoạn flow hỗ trợ. Không có trường hợp nào CS gửi tiếng khác với khách. (#6 #8 #10 #17 #27)
- Review ask đúng lúc: ở chat #9 sau khi merchant nói 'amazing!!!' và chat #23 sau khi merchant xác nhận fix thành công — Jade xin review tự nhiên, không gượng ép. Chat #23 được kết quả ngay (merchant gửi ảnh review). (#9 #23)

## 🔧 Cần cải thiện
- **[KN1] · Low** Lỗi đánh máy nhỏ xuất hiện trong chat quan trọng: 'Thank you for your patienec' (#2)
   > CS (Jade): 'Thank you for your patienec' — chat #2 với merchant đang hỏi về downgrade plan.
   → Đây là lỗi nhỏ nhưng trong chat với merchant đang cân nhắc downgrade thì sự chuyên nghiệp trong từng chi tiết quan trọng hơn. Tập thói quen đọc lại 1 giây trước khi gửi.
- **[KN7] · Low** Trong chat #24 (data export request), Jade chuyển ticket nhưng không giải thích được sơ bộ về khả năng hỗ trợ — để merchant không rõ kỳ vọng. (#24)
   > CS (Jade): 'Regarding your request, allow me to forward it to the internal team for further investigation. If possible, can you kindly share the email you would like to receive this daily report?' — Merchant hỏi về CSV export, API endpoint, scheduled export, nhưng Jade không cho biết Joy hiện có hỗ trợ gì (hay không) trước khi chuyển dev.
   → Khi nhận request kỹ thuật phức tạp, hãy set expectation ngắn gọn: 'Joy hiện có export CSV trong phần Analytics, nhưng scheduled export hoặc API mình cần xác nhận thêm với dev team.' Làm khách không bị 'đứng trong bóng tối' trong khi chờ.
- **[QT22] · Low** Trong chat #3, merchant hỏi về 'top block' khi Jade đang xử lý nhiều yêu cầu song song — câu hỏi 'The changes that were made could they be applied to top block' bị trả lời chậm và thiếu xác nhận rõ. (#3)
   > Customer (Malia Joseph): 'The changes that were made could they be applied to top block' → CS (Jade): 'For this request, can you kindly explain it further so we can better support you?' — Merchant đã giải thích ngay sau đó rằng họ đã tự di chuyển block, không cần action nữa. Nhưng Jade đã không chốt lại rõ ràng là vấn đề đó đã được giải quyết bởi chính merchant.
   → Khi merchant tự xử lý một phần rồi báo lại, hãy confirm: 'Got it — bạn đã tự move block và vấn đề Total display đã ổn rồi, phải không? Mình sẽ chỉ cần xử lý phần heading text size và widget button nhé.' Tránh để các thread nhỏ bị lơ lửng.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 2/4 chat phù hợp (đúng lúc 2, chưa đúng lúc 0).
- Đã xin review 2/4 chat phù hợp (chat #9 và #23 — cả hai đúng lúc, khách vừa xác nhận hài lòng). Còn bỏ lỡ 2 chat có khách tỏ ra rất vui (#1 'o my god its so simple, well done', #16 'all good, thank you!'). Lần sau khi khách khen hoặc nói 'all good', đó là thời điểm vàng để mời để lại review nhẹ nhàng. Lưu ý: chat #5 merchant đã có review tag nên không tính vào mẫu eligible — Jade không cần xin thêm ở đây.

## 📈 So với tuần trước (W23)
- Điểm 82 → 83 (▲ +1)
