# QA Tuần 2026-W22 — Hazel
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 81/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 26.6/34 · 📚 Kiến thức 27.5/33 · 🛠️ Xử lý 26.6/33

## 📝 Nhận xét chung
Tuần này bạn thể hiện sự ổn định đáng ghi nhận — xử lý đa ngôn ngữ (tiếng Pháp, Trung, Ý, Tây Ban Nha, Việt), đa dạng case từ kỹ thuật phức tạp đến setup cơ bản, đều giữ được sự bình tĩnh và kiến thức tốt. Điểm nổi bật nhất là chat #22 với khách hàng kỹ thuật (intentioncph): câu trả lời về deferred loading / Firebase JS API rất sâu và chuẩn xác — đây là loại câu hỏi nhiều CS khác sẽ né. Tuy nhiên, có 2 lỗi lặp lại cần sửa ngay: (1) chuyển ngôn ngữ lạc sang tiếng Anh trong khi khách đang chat tiếng Pháp/Tây Ban Nha mà không phát hiện ra ngay — điều này buộc khách phải tự dịch và làm giảm trải nghiệm; (2) ở một số chat dài, bạn không gửi tin nhắn xác nhận nhanh trước khi vào xử lý, khiến khách chờ không biết bạn có đọc hay không — Liz đã nhắc nhở trực tiếp về điểm này ở chat #9.

## ✅ Điểm tốt
- **[P2]** Kiến thức kỹ thuật tốt và sâu — đặc biệt chat #22 (intentioncph), câu trả lời về deferred loading / Firebase JS API / ChattyJS.openWidget() API chi tiết, chính xác, đúng với cách developer cần thông tin. (#22, #7, #18)
- **[P3]** Ownership tốt — chủ động đề nghị thay màu chatbox miễn phí cho khách (chat #1), tự nhận và xử lý case phức tạp mà không đẩy đi, follow-up đúng hạn qua email/inbox sau khi đóng ca. (#1, #2, #27)
- **[P1]** Giải quyết vấn đề có hệ thống — ở chat #2 (cart sync / Hoppy Free Shipping), bạn hỏi đúng thông tin cần thiết, xác nhận lại vấn đề từ Loom video trước khi escalate, tránh hao effort thừa. (#2, #15, #29)

## 🔧 Cần cải thiện
- **[KN3 · Moderate]** Chuyển ngôn ngữ lạc: khách nói tiếng Pháp/Tây Ban Nha, Hazel reply bằng tiếng Anh mà không nhận ra ngay — buộc khách phải đọc/dịch thêm
  - *Dẫn chứng:* Chat #2 line 522: CS (Hazel): 'You can click on your account and view the review you've written while it's waiting to be reviewed by G2.' — khách đang chat hoàn toàn bằng tiếng Pháp, Hazel tự nhận lỗi ở dòng 529: 'Désolé
  - → Trước khi gửi, check xem ngôn ngữ bạn sắp dùng có khớp với ngôn ngữ khách đang chat không. Với Crisp có live translate, chỉ cần type bằng tiếng Anh và bật translate — không cần tự gõ tiếng bản địa, nhưng nếu đang reply thủ công thì phải giữ nhất quán.
- **[QT18 · Low]** Để khoảng trống dài trước khi acknowledge khách — khách chờ không biết CS có đọc hay không, Liz phải nhắc trực tiếp
  - *Dẫn chứng:* Chat #9: Khách gửi lúc 15:11, Hazel không reply gì từ 15:17 đến 15:21 (trong lúc đang soạn). Liz nhắn lúc 15:19: 'Em cứ rep nhanh trc 1 câu nhé, ko để khoảng trống như vậy, kh lại tưởng mình off mất'
  - → Ngay khi nhận được câu hỏi dài hoặc cần thời gian xử lý, gửi ngay 1 dòng xác nhận ('Thank you! Give me a moment to look into this') trước khi soạn câu trả lời đầy đủ.
- **[KN1 · Low]** Một số lỗi typo nhỏ trong chat
  - *Dẫn chứng:* Chat #1: 'Please give me a moment to review the prevous messages first' (prevous → previous). Chat #29: 'Please give me a moment to review the previous messaages first' (messaages → messages).
  - → Đọc lại nhanh trước khi gửi — đặc biệt các câu mở đầu shift handoff hay dễ bị copy-paste lỗi.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh