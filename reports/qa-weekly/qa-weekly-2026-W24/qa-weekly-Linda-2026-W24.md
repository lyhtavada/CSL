# QA Tuần 2026-W24 — Linda
**App:** — · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 83/100 — Tốt  (▲ +3 so với W23: 80)
- 🧠 Mindset 24.0/34 · 📚 Kiến thức 29.0/33 · 🛠️ Xử lý 27.0/33
- 🔍 Đã QA: 30 chat
- Trục yếu nhất: **Mindset**

## 📝 Nhận xét chung
Linda hoàn thành tuần W24 với 30 chats, đạt mức Tốt (83). Điểm mạnh nổi bật là chủ động DFY setup, xử lý đa ngôn ngữ (Chinese, Japanese, German, English) tốt, escalation đúng quy trình. Điểm cần cải thiện: lắng nghe live coaching của Liz trong Chat #6 còn chậm, một số lỗi grammar lặp lại, và một lần xin review hơi sớm. Với tư cách là CS đang Training, tiến bộ rõ rệt so với tuần đầu.

## ✅ Điểm tốt
- Linda thường xuyên kiểm tra settings phía backend và thực hiện setup trực tiếp cho merchant thay vì chỉ hướng dẫn từng bước. Ví dụ Chat #22: tự soạn cả template NASM coach instruction và gửi cho merchant xem duyệt. (#1 #4 #5 #10 #22 #25)
- Duy trì Chinese suốt Chat #16 (bug nghiêm trọng routing messages sai khách), Japanese chính xác trong Chat #23, German trong Chat #2. Crisp live-translate hỗ trợ nhưng Linda xử lý context mượt. (#7 #16 #23 #24)
- Luôn tạo ticket với link Slack hoặc mô tả đầy đủ. Chat #28: tag Liz đúng cách khi gặp câu hỏi ngoài phạm vi (security certifications) và chuyển rõ nội dung escalate. (#6 #12 #16 #19 #25 #26 #28)
- Đa số review ask được đặt sau khi merchant đã confirm hài lòng. Chat #23: xin review bằng tiếng Nhật phù hợp context. (#1 #4 #14 #17 #23)
- Không chỉ xử lý vấn đề được hỏi mà còn phát hiện và bật thêm settings hữu ích (AI Re-engage After Resolution) mà không cần được yêu cầu. (#25 #29)

## 🔧 Cần cải thiện
- **[QT18] · High** Không follow live coaching của Liz kịp thời (Chat #6) (#6)
   > Liz đã nhắn nội bộ: 'họ đang cáu rồi, ko nên đổ cho internet nữa' và 'ko nên nói nhiều quá em ạ' — nhưng Linda vẫn tiếp tục đề nghị speedtest và giải thích dài dòng sau đó. Đây là coaching trực tiếp từ CS Leader trong live chat, cần apply ngay lập tức.
   → Khi Liz (hoặc bất kỳ senior nào) nhắn coaching nội bộ trong lúc chat đang diễn ra, đó là tín hiệu cần thay đổi hướng ngay. Rút ngắn reply, focus vào next action cụ thể, không phân tích thêm nguyên nhân khi KH đang bực.
- **[KN1] · Moderate** Lỗi grammar lặp lại (#1 #9 #12 #30)
   > Chat #1: 'Grear to hear' (dòng 79) | Chat #9: 'We're very appreciate' (Liz flagged nội bộ) | Chat #12: 'No promblem' (dòng 2627) | Chat #30: 'better undestand' (lặp pattern)
   → Một số lỗi này xuất hiện ở những câu rất ngắn — nên proofread trước khi gửi, đặc biệt với các câu closing/transition. Gợi ý shortcuts đúng: 'Great to hear!', 'We really appreciate it.', 'No problem at all.', 'better understand'.
- **[QT25] · Low** Xin review lặp 3 lần trong một chat (Chat #2) (#2)
   > Trong Chat #2 (soundmaxx-online.de), Linda xin review 3 lần. Lần đầu appropriate, hai lần sau tạo cảm giác gây áp lực không cần thiết.
   → Một lần xin review là đủ. Nếu merchant không phản hồi sau lần đầu, không nhắc lại trong cùng session. Có thể theo dõi qua follow-up email sau nếu cần.
- **[QT9] · Low** Xin review hơi sớm khi vấn đề chưa hoàn toàn xong (Chat #15) (#15)
   > Linda xin review trong Chat #15 (EpicLoot) khi setup chưa được confirm xong hoàn toàn bởi merchant.
   → Chỉ xin review sau khi merchant đã confirm satisfied hoặc nói 'thank you' / 'it works'. Nếu ticket vẫn đang mở, đợi đến khi close.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 8/24 chat phù hợp (đúng lúc 6, chưa đúng lúc 2).
- 6 chats excluded khỏi eligible vì ĐÃ CÓ review (chats #7, #8, #21, #24, #29, #30). Linda hỏi review ở 8/24 eligible chats (~33%). Chat #2: hỏi 3 lần trong 1 session (mistimed). Chat #15: hỏi hơi sớm khi vấn đề chưa confirmed xong (mistimed). 6 lần đúng timing tốt. Không có trường hợp xin Shopify review khi đã có review.

## 📈 So với tuần trước (W23)
- Điểm 80 → 83 (▲ +3)
