# QA Tuần 2026-W22 — Hazel
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 83/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 26/34 · 📚 Kiến thức 29.2/33 · 🛠️ Xử lý 26.7/33

## 📝 Nhận xét chung
Tuần này bạn thể hiện ổn định ở cả ba trục — kiến thức sản phẩm vững, xử lý đa ngôn ngữ (Anh, Pháp, Tây Ban Nha, Ý, Tiếng Việt, Tiếng Trung) không lẫn lộn, và biết chủ động điều tra vấn đề trước khi chờ khách hỏi. Điểm mạnh nổi bật nhất là độ chính xác kỹ thuật — đặc biệt rõ ở chat #22 (giải thích toàn bộ JS API cho deferred loading) và chat #7 (giải thích metafield types chính xác). Hướng cần tập trung: trục Kỹ năng và Mindset đang kéo điểm xuống vì hai lỗi lặp lại — (1) nhắn trùng message (chat #12 và #17) và chuyển ngôn ngữ sai trong giữa chat (chat #11), và (2) ở các chat ngắn bạn chưa khai thác hết cơ hội chủ động tư vấn thêm cho khách, dừng lại ở mức "đủ" thay vì "tốt hơn". Hai lỗi này tuy nhỏ nhưng trực tiếp làm khách phải đọc lại hoặc tạo cảm giác thiếu chú ý.

## ✅ Điểm tốt
- **[P2]** Kiến thức kỹ thuật vững và chính xác — giải thích metafield types (chat #7), JS API cho deferred loading (chat #22), billing cycle calculation (chat #17), và Omnisend/Shopify Flow integration (chat #30) đều đúng và đủ chi tiết để khách làm theo được ngay. (#7, #22, #17, #30)
- **[P3]** Xử lý đa ngôn ngữ tốt — chủ động giao tiếp bằng ngôn ngữ của khách (Pháp, Tây Ban Nha, Ý, Tiếng Trung, Tiếng Việt) mà không cần được yêu cầu, giúp khách cảm thấy được phục vụ đúng cách. (#2, #8, #11, #12, #13, #17)
- **[P1]** Chủ động điều tra và cung cấp video minh họa (jam.dev) khi cần — ở chat #15 tự quay screen recording để xác định đúng nguyên nhân lỗi Send button bị che khuất, thay vì chỉ hỏi khách. (#15, #6)
- **[P4]** Follow-through tốt qua async — nhiều chat bạn gửi email/message follow-up có kết quả cụ thể sau khi tech team xử lý xong, không để khách tự chờ không rõ trạng thái. (#4, #18, #19, #27, #30)

## 🔧 Cần cải thiện
- **[KN1 · Moderate]** Gửi trùng tin nhắn trong 2 chat — tạo cảm giác thiếu chú ý và làm khách phải đọc lại.
  - *Dẫn chứng:* Chat #12: [11:08:04] CS (Hazel): Ecco a te 🤗 / [11:08:04] CS (Hazel): Ecco a te 🤗 — tin nhắn gửi hai lần liên tiếp. Chat #17: [04:34:04] CS (Hazel): 你好！😊 我是来自 Avada 支持团队的 Hazel... (gửi y chang hai lần liên tiếp).
  - → Trước khi gửi, kiểm tra nhanh xem đã gửi chưa — đặc biệt khi bàn giao ca hoặc vừa soạn xong message dài. Nếu lỡ gửi trùng thì nhắn 'Xin lỗi, tin nhắn vừa gửi nhầm đúp' để khách không bỡ ngỡ.
- **[KN1 · Low]** Chuyển sang tiếng Anh giữa một cuộc trò chuyện đang dùng tiếng Tây Ban Nha — khách phải nhận ra bất nhất.
  - *Dẫn chứng:* Chat #11: [04:11:36] CS (Hazel): I saved it for you. Please help me reload the page and double-check it on your side — trong khi toàn bộ chat với MUS đang dùng tiếng Tây Ban Nha. Bạn cũng tự nhận ra và xin lỗi sau đó.
  - → Đặt ngôn ngữ cuộc chat ở đầu conversation, giữ nhất quán xuyên suốt. Nếu lỡ sai thì nhắn ngay: 'Xin lỗi, tôi nhầm ngôn ngữ' rồi dịch lại.
- **[KN7 · Low]** Ở một số chat ngắn, phần kết thúc và review ask được xử lý máy móc — không có thêm giá trị nào cho khách.
  - *Dẫn chứng:* Chat #24: khách nói 'this is just a test store / appreciate u help' và Hazel chỉ reply 'Ah got it. Please feel free to ping me here if you need further assistance.' rồi hỏi liệu đây có phải test store không — trong khi đ
  - → Với các chat ngắn mà khách đang ở giai đoạn khám phá, thêm 1 gợi ý cụ thể phù hợp với setup của họ (ví dụ: 'Khi bạn sẵn sàng test live, đây là 3 bước đầu tiên nên làm...'). Tránh kết thúc chỉ với câu 'cứ nhắn lại nhé'.
- **[QT9 · Low]** Ở chat #8, khi khách đã mô tả rõ vấn đề (chat không tìm được catalogue/sản phẩm), Hazel hỏi lại thêm một bước thay vì đọc thêm và xử lý luôn.
  - *Dẫn chứng:* Chat #8: [08:00:18] CS (Hazel): Je ne suis pas tout à fait sûr de comprendre votre question. Pourriez-vous s'il vous plaît clarifier un peu plus — trong khi trước đó khách đã nói 'mon chat ne trouve pas les catalogue / l
  - → Đọc kỹ các tin nhắn liền trước khi hỏi lại. Nếu vẫn chưa rõ 100%, thử đưa ra giả thiết: 'Mình hiểu bạn muốn X — đúng không?' thay vì hỏi chung 'bạn có thể nói rõ hơn không'.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh