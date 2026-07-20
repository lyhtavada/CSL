# QA Weekly — Phoebe — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 77/100 — Đạt  (▼ -5)  
**Đã QA:** 23 chat

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 25.6/34 |
| 📚 Kiến thức | 26.1/33 |
| 🛠️ Xử lý | 25.1/33 |

## 📝 Nhận xét chung

Tuần này bạn xử lý ổn về mặt kỹ thuật — kiên nhẫn, tự test lại trước khi báo khách, và trung thực nhận lỗi khi sai (chat #14). Điểm mạnh rõ nhất là các case DFY/sale-lead phức tạp được trả lời đầy đủ, có cấu trúc (chat #16, #9). Tuy nhiên điểm tổng chỉ ở mức "Đạt" vì trục Kỹ năng còn yếu: ở chat #2 bạn trả lời từng câu hỏi rời rạc thay vì đưa roadmap tổng thể, khiến khách phải hỏi lại "giờ làm gì" liên tục và phải giục "làm nhanh hơn được không" — đây là hệ quả trực tiếp của thiếu chủ động dẫn dắt luồng chat. Hướng cần tập trung tuần tới: khi nhận bàn giao case setup nhiều bước, tóm tắt nhanh "đã làm gì — còn gì" ngay đầu để khách không phải dò từng bước, và double-check ngôn ngữ trả lời khớp với khách trước khi gửi.

## ✅ Điểm tốt tuần này

- Ownership tốt, theo tới cùng và tự test lại kết quả trước khi báo khách thay vì chỉ báo 'đã gửi team' — chat #1 (khách khó tính, phàn nàn tên ẩn danh 'nghe như Trung Quốc'): Phoebe tự đổi setting, tự test lại nhiều lần ('Ah, I have just tested again', 'I have just tested it again and AI doesn't mention random name anymore') trước khi confirm với khách. (#1)
- Trả lời sale-lead rất kỹ, đầy đủ, có cấu trúc — chat #16 (khách đang cân nhắc chuyển từ Oct8ne sang Chatty): trả lời từng câu hỏi 1-6 chi tiết, chính xác, kèm đề xuất đặt lịch tư vấn thêm. Khách phản hồi 'Your answers have been very informative and easy to understand'. (#16)
- Trung thực nhận lỗi của chính mình thay vì lấp liếm — chat #14: khi highlight nhầm khoảng ngày trên biểu đồ, Phoebe chủ động nói rõ 'I'm sorry for highlighting it incorrectly. It should be pointed to the Last 7 days, but i drew it wrong.' (#14)
- Xử lý bug kỹ thuật rõ ràng theo format root cause – solution – result, dễ hiểu cho khách — chat #9 (nút Send hiển thị sai màu): 'Root cause: ... Solution: ... Result: ...' rất chuyên nghiệp. (#9)

## 🔧 Cần cải thiện

- **[KN7] Moderate** — Onboarding thiếu roadmap tổng thể, trả lời từng câu hỏi rời rạc khiến khách phải hỏi lại nhiều lần 'giờ làm gì tiếp' — làm chat kéo dài và khách sốt ruột. (#2)
  - Dẫn chứng: Customer (Paulas): 'ok what do I do next' → 'now what' → 'ok so what do I do next' → 'ok can we work a little faster?' Phoebe trả lời từng bước rời rạc: 'May I please know which feature you want to focus on? At the moment, all necessary features have been completed.'
  - → Khi khách chọn DFY/setup nhiều bước, đưa checklist tổng quan ngay từ đầu (đã làm gì / còn gì) thay vì để khách phải hỏi từng bước một, giảm số lần khách phải hỏi 'giờ làm gì'.
- **[KN3] Moderate** — Khách viết tiếng Tây Ban Nha nhưng Phoebe trả lời bằng tiếng Ý ở một đoạn — khách phải tự dịch, gây khó hiểu (dù Phoebe có nhận ra và xin lỗi sau đó). (#5)
  - Dẫn chứng: Customer (Beberso): 'si' (xác nhận bằng tiếng Tây Ban Nha) → CS (Phoebe): 'Grazie per la conferma! Mi conceda gentilmente più tempo per esaminarla per lei' (tiếng Ý). Sau đó Phoebe tự nhận: 'Disculpa si mi herramienta de traducción está traduciendo incorrectamente.'
  - → Trước khi gửi, kiểm tra nhanh ngôn ngữ trả lời có khớp với ngôn ngữ khách vừa dùng không, đặc biệt khi chat có nhiều ngôn ngữ xen kẽ trong ngày.
- **[KT2] Low** — Nhắc lại con số giới hạn sản phẩm '1,500 sản phẩm active' cho khách mà không double-check với KB hiện tại — KB pricing show Basic=500/Pro=8,000/Plus=unlimited, không có mốc 1,500 nào. Có thể là giới hạn kỹ thuật riêng ngoài KB, nhưng nên xác minh trước khi khẳng định với khách để tránh tư vấn sai nếu KB đúng. (#23)
  - Dẫn chứng: CS (Phoebe): 'the AI can only answer questions and crawl information from those 1,500 active products... If you would like to train all products, our highest plan would be suitable for you.'
  - → Khi gặp con số không khớp KB, note lại và hỏi Liz/kỹ thuật xác minh trước khi khẳng định chắc với khách, tránh lặp lại số liệu chưa chắc đúng.
- **[QT18] Low** — Bỏ lỡ cơ hội xin review khi khách vừa cảm ơn/hài lòng rõ ràng, không có action nào theo sau để chốt trải nghiệm. (#4)
  - Dẫn chứng: Customer: 'それなら助かります' (vậy thì đỡ quá) — Phoebe chỉ đáp 'こちらこそ、ありがとうございます!' rồi kết thúc, không mời review dù chat đã xử lý xong nhiều vấn đề kỹ thuật cho khách.
  - → Khi khách vừa cảm ơn/hài lòng rõ, tranh thủ mời review ngay lúc đó — đây là thời điểm vàng.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **1/2** chat phù hợp (đúng lúc: 1, sai lúc: 0)
- Xin review 1/2 chat phù hợp (chat #1, đúng lúc sau khi khách vừa khen 'I love the app... service is amazing'). Bỏ lỡ 1 chat vàng ở #4 khi khách vừa cảm ơn rõ ràng mà không mời review. Mẫu nhỏ vì phần lớn chat của Phoebe là xử lý kỹ thuật/DFY chưa có xác nhận hài lòng rõ ràng cuối chat.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 82 → 77 (▼ -5)
- Lỗi lặp lại từ 2026-W28: KN3, KN7, QT18 — cần ưu tiên sửa
