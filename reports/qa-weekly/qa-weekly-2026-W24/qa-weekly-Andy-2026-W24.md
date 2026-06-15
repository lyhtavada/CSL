# QA Tuần 2026-W24 — Andy
**App:** Chatty · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 85/100 — Tốt  (▲ +1 so với W23: 84)
- 🧠 Mindset 27.4/34 · 📚 Kiến thức 29.4/33 · 🛠️ Xử lý 28.0/33
- 🔍 Đã QA: 29 chat (loại 1)
- Trục yếu nhất: **Mindset**

## 📝 Nhận xét chung
Andy tăng nhẹ so với W23 (84→85). Điểm mạnh ổn định: proactive ownership, warmth thật sự xuyên suốt đa ngôn ngữ, knowledge chính xác (pricing, history, downgrade behavior). KN5 tái diễn (chat #22 — German, misidentify request). QT25 xuất hiện lần đầu (chat #29 — hứa update sau 1 tiếng nhưng không quay lại đúng hẹn). QT18 tiếp tục (chat #23 — no closure before end). KN3 tiếp tục (chat #13 — no confirm after fix). 'Please cooperate' tone ở W23 chat #12 không tái diễn tuần này — cải thiện nhỏ về Mindset.

## ✅ Điểm tốt
- Chủ động nhận diện vấn đề trước khi khách hỏi. Chat #1: 'I noticed that your product data has not enabled on AI agent knowledge base yet, would you like me to assist?' Chat #13: 'I noticed that you have not set up the support email yet.' Chat #30: 'May I know which questions you want to display so I can adjust for you?' (#1 #2 #13 #30)
- Warmth thật sự, không scripted. 'The pleasure is all mine', 'Lovely to know', 'El placer es todo mío' — consistent across 6+ languages. Chat #25: duy trì follow-up nhiều session với khách Rafael, tạo và chỉnh scenario theo yêu cầu, gửi confirmation screenshot. (#2 #4 #5 #6 #15 #24 #25)
- Chat #3: Hướng dẫn WABA setup 6 bước chi tiết đúng quy trình. Chat #16: Cung cấp full JS code cho cart event. Chat #26: Giải thích chính xác downgrade behavior (100 products random → manual select; 90-day history cutoff; chat history deleted permanently — not preserved). Knowledge verified against Chatty pricing: Free=100 products, 90d; Basic=500 products, 12mo. (#3 #16 #26)

## 🔧 Cần cải thiện
- **[KN5] · Low** Trả lời trước khi hiểu đúng vấn đề (tái diễn từ W23) (#22)
   > Chat #22: Khách nói 'kannst du bei dem link des widerrufsrechts die aktuelle URL hinterlegen?' (muốn update URL right-of-withdrawal). Andy hỏi 'Darf ich wissen, ob Sie diese URL für die Bestellverfolgung verwenden möchten?' (hỏi về order tracking URL — sai context). Khách phải clarify thêm. Lỗi giống W23 chat #27: customer nói 'web version tends to lag' → Andy suggest mobile app.
   → Trước khi đề xuất solution, đọc lại câu hỏi gốc của khách — đặc biệt khi có nhiều URL type (order tracking vs withdrawal link vs other). Nếu không chắc, hỏi: 'Just to confirm, are you referring to [X] or [Y]?'
- **[QT25] · Moderate** Hứa update nhưng không quay lại đúng giờ (lần đầu xuất hiện) (#29)
   > Chat #29: 06:45:10 CS (Andy): '关于您的案件，目前仍在调查中，我将在1小时后回来与您分享更新。' — Cam kết quay lại sau 1 tiếng. Thực tế: customer nhắn lại lúc 08:24 ('还要多久啊') — hơn 1.5 tiếng sau — Andy mới respond. Đây là bug nghiêm trọng (messages routing sang customer khác), hứa tiến độ mà không giữ = tạo thêm frustration.
   → Nếu cam kết timeframe, phải set reminder và quay lại đúng giờ. Với bug nghiêm trọng (live-store impact), update interval ngắn hơn (30 phút). Nếu chưa có update thì cũng phải check in: '我还在处理中，感谢您的耐心。'
- **[QT18] · Low** Chat kết thúc không có closure rõ ràng (tái diễn từ W23) (#23)
   > Chat #23: Andy enables product data, gửi screenshot, hỏi 'May I know if the AI agent's response correctly as you expected?' — Khách không respond và chat kết thúc. Không có follow-up, không có handoff note.
   → Nếu khách không respond sau 15-20 phút, gửi một tin nhắn closing: 'I'll leave this open for you. Feel free to reach back if you have questions!' Hoặc note nội bộ trước khi off.
- **[KN3] · Low** Thiếu confirm sau khi fix (tái diễn từ W23) (#13)
   > Chat #13: Andy báo đã setup support email và gửi screenshot (similar pattern to W23 chat #29 với FAQ). Không hỏi khách xác nhận thử lại từ đầu trước khi chuyển sang bước tiếp theo.
   → Sau khi báo fix, luôn thêm: 'Could you try it on your end and let me know if everything looks correct?' Đừng assume fix là done cho đến khi khách confirm.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 5/13 chat phù hợp (đúng lúc 5, chưa đúng lúc 0).
- 5/13 eligible chats có review ask, tất cả đều well-timed. Không có mistimed case (cải thiện so với W23 khi có chat #3 mistimed). Cần tăng coverage — đặc biệt với các chat ngắn, resolved, khách cảm ơn (chats #9, #11, #30).

## 📈 So với tuần trước (W23)
- Điểm 84 → 85 (▲ +1)
