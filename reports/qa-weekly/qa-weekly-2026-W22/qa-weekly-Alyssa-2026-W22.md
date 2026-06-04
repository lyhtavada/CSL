# QA Tuần 2026-W22 — Alyssa
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 89/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 29.5/34 · 📚 Kiến thức 30.2/33 · 🛠️ Xử lý 29.3/33

## 📝 Nhận xét chung
Alyssa là một CS có mindset phục vụ rõ ràng — bạn không bỏ case giữa chừng, theo sát từ chẩn đoán đến khi khách xác nhận xong, và biết cách xử lý khách khó mà không mất bình tĩnh. Điểm mạnh nổi bật nhất là ownership trên các case dài và phức tạp (chat #2, #10, #28) — đây là thứ không phải CS nào cũng có. Kiến thức sản phẩm vững, ít để khách chờ mà không có lý do. Hướng cần tập trung: lỗi chính tả lặp lại trong nhiều chat (gald, pelasure, convinient, reponses) — dù nhỏ nhưng làm giảm ấn tượng chuyên nghiệp, đặc biệt trong các email update quan trọng; và thói quen bỏ sót câu hỏi khi khách gửi nhiều request một lúc, khiến khách phải hỏi lại và kéo dài chat không cần thiết.

## ✅ Điểm tốt
- **[P1]** Ownership xuất sắc trên các case phức tạp và kéo dài: Alyssa không rời case khi chưa có kết quả — theo sát từ báo cáo TS, gửi email update chi tiết, kiểm tra lại sau khi fix. Chat #2 (Teresa/Joy) kéo hơn 3 ngày với nhiều sub-request, Alyssa xử lý từng mục và chủ động cập nhật. Chat #28 (Life Rich Creative) — case pre-launch cực căng, nhiều lỗi point sync, Alyssa điều phối TS, giải thích tình huống cho khách, bình tĩnh dưới áp lực. (#2, #10, #28)
- **[P3]** Chủ động đề xuất giá trị thêm (DFY widget, loyalty blocks, tính năng mới) một cách tự nhiên và đúng thời điểm, không gượng ép. Ví dụ chat #2: nhận ra customer đang dùng widget cũ, chủ động offer nâng cấp + cải thiện cả Point Calculator, Loyalty Dashboard, cart calculator. Chat #10: sau khi fix xong VIP tier còn hướng dẫn cách dùng Shopify Flow trigger để email reminder. (#2, #6, #10, #22)
- **[P2]** Empathy tự nhiên, không template: Khi khách tỏ ra thất vọng (chat #28 — khách nói 'I'm so sick of reporting these issues'), Alyssa nhận lời thẳng thắn ('I understand your frustration'), không biện hộ, tập trung vào giải quyết. Khi khách cần kiểm tra lại sau khi CS đã tự sửa lỗi (chat #9), giải thích thêm mà không defensive. (#28, #9, #1)
- **[P4]** Kiến thức sản phẩm chắc: Chẩn đoán nhanh, chính xác — chat #1 (widget không hiện do 'Display after login' toggle), chat #12 (cùng vấn đề, nhận ra ngay trong 10 phút), chat #9 (giải thích chính xác newsletter widget vs external subscription form). Không cần hỏi lại nhiều lần hay looping. (#1, #12, #9)

## 🔧 Cần cải thiện
- **[KN1 · Low]** Typo lặp lại nhiều chat — gây ấn tượng thiếu chuyên nghiệp trong văn bản gửi khách
  - *Dẫn chứng:* Chat #13: 'I'm gald to know that it works for you!' và 'reponses'. Chat #1: 'It will be convinient for our team'. Chat #28: 'My pelasure!'
  - → Bật spell-check trên Crisp (hoặc browser). Với các tin nhắn dài/email, đọc lại một lần trước khi gửi — đặc biệt ở câu mở đầu và câu kết. 3 lần typo trong 30 chat là pattern cần sửa ngay.
- **[QT22 · Moderate]** Bỏ sót câu hỏi của khách trong một số chat có nhiều request song song
  - *Dẫn chứng:* Chat #2 (line 14:56:02): Khách hỏi 'Also did you update my outdated widget to the new one?' — Alyssa trả lời nhưng kèm 'I did, but I reverted it back' mà không giải thích lý do, khiến khách bối rối ('Oh lol'). Chat #21 (
  - → Khi khách gửi nhiều câu hỏi cùng lúc, dùng số thứ tự (1. 2. 3.) để reply từng mục và xác nhận đã cover đủ trước khi kết thúc. Nếu không trả lời được ngay, acknowledge luôn: 'Câu 2 mình cần check thêm, trả lời sau 5 phút'.
- **[KN5 · Low]** Một lần giải thích nhầm về newsletter subscription widget setting rồi tự sửa trong email follow-up
  - *Dẫn chứng:* Chat #9 (line 04:00:31): Alyssa gửi email xác nhận lại: 'I have added a new prompt... I found that my previously provided information was incorrect.' — chứng tỏ lần đầu giải thích sai về behavior của 'Earn Points via Pop
  - → Với các setting có behavior phụ thuộc vào context (sandbox mode, plan, toggle state), test trực tiếp trên app hoặc hỏi TS confirm trước khi trả lời customer, tránh phải gửi correction email.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh