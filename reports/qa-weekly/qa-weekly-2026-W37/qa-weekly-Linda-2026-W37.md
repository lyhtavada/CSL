# QA Weekly — Linda — 2026-W37 (09/09 – 15/09/2026)

**Điểm tuần:** 80/100 — Tốt 👍 — ▼ -1 so với tuần trước (81)
**Đã QA:** 19 chat (loại 0 chat không tính)

## Breakdown 3 trục
- 🧠 Mindset: 26.6/34
- 📚 Kiến thức: 26.8/33
- 🛠️ Xử lý: 26.1/33
- Trục yếu nhất: **🧠 Mindset**

## 📝 Nhận xét chung
Tuần này bạn xử lý các case phức tạp, nhiều ngày rất có tâm — chat #1 và #15 cho thấy bạn chịu đầu tư thời gian trả lời chi tiết, có cấu trúc, không đẩy việc. Điểm mạnh nhất là khả năng truy đúng root cause thay vì chỉ escalate cho xong (chat #4, #11). Nhưng có một lỗi lặp lại rõ ràng cần bạn nhìn thẳng vào: bạn có xu hướng trả lời/kết luận trước khi chắc đã hiểu đúng ý khách hoặc trước khi thực sự verify được vấn đề — điều này xảy ra ở ít nhất 3 chat khác nhau trong tuần (#16, #4, #15), khiến khách phải giải thích lại nhiều lần, tốn thời gian của cả hai bên và có lúc khách cảm thấy không được tin (chat #4, khách phải gửi bằng chứng 3 lần). Tuần tới tập trung vào việc paraphrase/confirm lại ý khách trước khi trả lời dài, đặc biệt với câu hỏi ngắn hoặc mơ hồ.

## ✅ Điểm tốt
- [P1] Ownership và độ chi tiết rất tốt với case phức tạp nhiều ngày — chat #1 trả lời đầy đủ, có cấu trúc cho 10 câu hỏi kỹ thuật của KH một lúc (product catalog, add-to-cart, human handover...) kèm screenshot minh chứng; chat #15 (KH Nhật, feedback 7 câu AI trả lời sai) Linda viết phản hồi rất bài bản, tách từng case ra nguyên nhân + hướng fix riêng, không trả lời qua loa. (#1, #15)
- [P3] Chủ động tìm đúng root cause thay vì chỉ escalate cho xong: chat #4 tìm ra app BOGOS là nguyên nhân cart tự mở (không đổ lỗi Chatty); chat #11 giải thích đúng lý do sản phẩm subscription không sync được, giúp KH hiểu bản chất vấn đề. (#4, #11)
- [P4] Cẩn thận confirm phạm vi trước khi làm hành động không thể đảo ngược — chat #5 hỏi rõ 'xóa Training Data thôi hay xóa cả FAQ Manager' trước khi xóa hàng loạt 1000+ FAQ cho khách, tránh xóa nhầm. (#5)

## 🔧 Cần cải thiện
- **[KN5] (Moderate)** Lặp lại pattern: trả lời/kết luận trước khi hiểu đúng ý khách, khiến khách phải giải thích lại nhiều lần — xảy ra ở ít nhất 3 chat khác nhau trong tuần, cần ưu tiên sửa. (#16)
  - Evidence: Chat #16 (Dental Access): khách chỉ muốn SỬA text 'Wishlist' bị dài quá cắt chữ, nhưng Linda trả lời 'Recomendamos manter essa dica de ferramenta em vez de removê-la, pois está relacionada à acessibilidade...' (tưởng khách muốn XÓA). Khách phải đính chính: 'Não queremos removê-la, mas sim alterá-la, pois o texto ficou muito longo... o R ficou cortado.'
  - Action: Trước khi trả lời câu yêu cầu chỉnh sửa, hỏi lại 1 câu ngắn xác nhận đúng ý khách (sửa/xóa/thêm) nếu câu hỏi có thể hiểu theo nhiều hướng, thay vì suy diễn rồi trả lời dài.
- **[KN6] (Moderate)** Kết luận sớm 'không có vấn đề' dù khách đã gửi bằng chứng, khiến khách phải nhắn lại nhiều lần để chứng minh mới được xử lý. (#4)
  - Evidence: Chat #4 (Velvet Glow): khách gửi ảnh cart tự mở, nhưng Linda trả lời 'Ich habe gerade nochmal überprüft, und der Warenkorb öffnet sich nicht automatisch.' Khách phải nhắn lại 3 lần ('doch es macht es... das passiert nur bei ersten shop besuch... es passiert auf mein ipad auf mein mobil und computer') trước khi Linda điều tra sâu và tìm ra nguyên nhân thật (app BOGOS).
  - Action: Khi khách đưa bằng chứng cụ thể (ảnh/video) mà mình test không ra, đừng kết luận 'không có lỗi' — nói rõ 'mình chưa reproduce được, cho mình thêm chi tiết' để tránh khách cảm thấy không được tin.
- **[KN5] (Low)** Cùng pattern hiểu sai ý khách xuất hiện lần thứ 3 trong tuần (chat khác), dù mức độ nhẹ hơn — khách phải chuyển sang tiếng Anh để giải thích lại rõ ý muốn nói. (#15)
  - Evidence: Chat #15: khách nhắn 'この会話が何か間違っているわけではない。このフォームのデフォルトの文言はどこで変えるのかと聞いています' để đính chính lại câu hỏi ban đầu Linda đã hiểu nhầm hướng khác, sau đó khách phải viết hẳn một đoạn tiếng Anh dài để giải thích lại lo ngại thật (anxiety về form tiếng Anh) mới được xử lý đúng.
  - Action: Với khách hàng dùng ngôn ngữ không phải tiếng Anh và câu hỏi ngắn/mơ hồ, paraphrase lại đúng ý khách trước khi giải thích giải pháp, để tránh khách phải tự đính chính.

## 🌟 Xin review (observe-only, không tính điểm)
- Đã xin review ở 1/2 chat phù hợp
- Xin review đúng lúc ở chat #15 (ngay sau khi KH nói cảm ơn/hài lòng) — tốt. Bỏ lỡ 1 chat vàng ở #9 (KH vừa confirm 'ok confirmed' hài lòng nhưng Linda không xin review). Chat #4 đã có review từ trước nên không tính vào mẫu này dù Linda có mời khách review thêm trên G2.

## 📈 So với tuần trước
- Điểm: 81 → 80

## 🔗 Chat đã QA (19)
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fc839821-4608-4796-973c-66c27993ae25|#1 Databazaar> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_5182aec0-b294-4a06-ae9c-1fd396e7482e|#2 PetsPetorium> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0308f801-499a-4eaf-8ee0-f5ca70303547|#3 Foamma USA> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_579d4d29-50b7-4486-a87a-82e9c20832cb|#4 VELVET GLOW> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8ebe21f5-57db-44df-ab38-f2396f88cc49|#5 AntsHQ> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_15a9eec8-5af2-465b-8c52-bb992fee6617|#6 HOULTE> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7b7f7dd3-fc7e-489e-b2bb-272bdde022d8|#7 RituelKaizen> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_85337a4a-451d-4ee6-9983-3ad9513d9fe7|#8 The Clay Hole - Pottery & Art Community> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_99e9b4b1-9e86-43eb-a6c5-689a56fb3b9b|#9 Umicellar> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c189db69-ff7b-4f60-8f71-77062837d267|#10 ammotion> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b264d4a5-7156-4b81-b84b-877f14c768e3|#11 Puff Puff Beauty> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0e6965c0-674a-41c9-a520-c1152475cccb|#12 Montresor> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d53e2f60-e477-4361-8d1b-eb497670a604|#13 Hemani Herbals> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a604f5b7-bf26-4f48-96c3-636a39c6a007|#14 Elevate> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3d6d31f0-44dd-487c-aafd-84439a521111|#15 たいようのとけいてん> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fa5af7b5-d884-4745-ab93-eaa2a07452e5|#16 Dental Access> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1e7010e8-f3cc-42f6-b7ef-3e733db16101|#17 Arab Instruments> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9044455c-2cd5-4f87-bef2-2a6aae4560ba|#18 Phi Villa> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2743fb21-33bc-4285-8618-cd5b2d5fee47|#19 String & Thread>
