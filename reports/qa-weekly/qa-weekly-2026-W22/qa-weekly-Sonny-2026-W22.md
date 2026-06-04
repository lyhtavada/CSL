# QA Tuần 2026-W22 — Sonny
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 86/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 28.5/34 · 📚 Kiến thức 29.4/33 · 🛠️ Xử lý 28.5/33

## 📝 Nhận xét chung
Tuần này Sonny thể hiện ổn đều — mindset tốt, kiến thức sản phẩm Joy khá chắc, và khả năng thu hồi khi mắc lỗi là điểm nổi bật thực sự đáng khen. Tuy nhiên, điểm yếu rõ nhất là kỹ năng xử lý: một số lần Sonny gây ra lỗi trực tiếp trên widget live của khách (chat #6: text/ảnh sai; chat #10: label "TREATS" bị đổi mà không báo trước), và một số câu trả lời còn có typo đáng kể ("I am I could clarify", "any adjustmentt", "comepleted"). Ngoài ra, ở một vài điểm trong chat #18, Sonny phải gửi email đính chính sau khi đã gửi thông tin sai về widget version — việc này tạo ra thêm friction và làm khách mất tin. Đây là các lỗi có thể tránh nếu kiểm tra kỹ trước khi thao tác/gửi.

## ✅ Điểm tốt
- **[P1]** Sở hữu vấn đề đến cùng — không đẩy đi. Ví dụ điển hình: chat #3, khi Oliver hỏi về CSV tier import và kiểm tra Shopify Flow, Sonny chủ động test trên demo store của mình và gửi kết quả cho khách mà không cần được yêu cầu. Chat #16: Sonny nhận danh sách 7 khách bị thiếu email, xử lý ngay trong cùng session và xác nhận điểm đã được điều chỉnh thủ công trước khi đóng. (#3, #16, #30)
- **[P3]** Chủ động đề xuất thêm giá trị cho khách. Sonny thường xuyên offer DFY widget setup, loyalty page, và theo dõi kết quả mà không cần khách hỏi. Chat #15: sau khi khách từ chối V4 lần đầu, Sonny không bỏ cuộc mà tự redesign theo phản hồi của khách và gửi lại bản tùy chỉnh mới — chủ động một cách có chất lượng. (#15, #22, #28)
- **[P2]** Phục hồi lỗi nhanh và chuyên nghiệp. Chat #6: khách phàn nàn widget là 'a disaster', Sonny lập tức nhận lỗi ('I regret that the images and the text I chose didn't suit your preference'), hoàn nguyên và hỏi thêm về mobile. Chat #28: khách phàn nàn về wording sai, Sonny xử lý trong vòng 30 phút và gửi follow-up email giải thích. (#6, #10, #28)
- **[P4]** Giải thích kỹ thuật rõ ràng và đúng. Chat #2: giải thích công thức tính point calculator (5990/1000 = 5.99 → round → 6 × 30 = 180 credits) chuẩn xác. Chat #30: giải thích Instagram tracking limitation một cách trung thực và đầy đủ. (#2, #3, #30)

## 🔧 Cần cải thiện
- **[KN1 · Moderate]** Typo lặp lại nhiều chat — gây ấn tượng không chuyên nghiệp
  - *Dẫn chứng:* Chat #3: 'I am I could clarify' [14:11:49]; Chat #12: 'any adjustmentt' [21:09:18]; Chat #30: 'comepleted' [11:22:03]; Chat #29: 'continue to support you. May I have...' (cú pháp gãy).
  - → Trước khi gửi tin quan trọng (đặc biệt email/follow-up), đọc lại 1 lần. Bật spellcheck trên trình duyệt. Lỗi typo trong tin nhắn hỏi dữ liệu/xác nhận là dấu hiệu khách hàng đọc ẩu — cần sửa.
- **[QT18 · High]** Thay đổi nội dung live widget của khách mà không thông báo trước — gây hậu quả trực tiếp trên storefront
  - *Dẫn chứng:* Chat #10: Sonny đã tùy chỉnh text/icons khi setup Unified widget preview, nhưng những thay đổi này cũng áp dụng lên widget classic đang live. Khi khách phàn nàn 'Why did it change to TREATS?', Sonny xác nhận: 'I wasn't a
  - → Trước khi bắt đầu bất kỳ thao tác DFY nào, cần xác nhận rõ với khách: 'Thao tác này có ảnh hưởng gì đến widget đang live không?' Nếu có nguy cơ ảnh hưởng, báo khách trước — không để khách tự phát hiện ra. Đây là lỗi gây hệ quả thực tế trên live store.
- **[KN3 · Low]** Một số hướng dẫn về tính năng nâng cao chưa đủ rõ khi khách lần đầu dùng
  - *Dẫn chứng:* Chat #18: Sonny ban đầu gửi thông tin về V4 widget mà thực ra khách đang ở V3 ('em lộn shortcut ạ'). Phải gửi tin đính chính sau. Chat #21: câu trả lời 'Chọn dynamic option' kèm screenshot — không giải thích tại sao opti
  - → Trước khi gửi hướng dẫn về widget version hoặc tính năng, kiểm tra nhanh xem khách đang dùng phiên bản nào. Khi hướng dẫn UI, nêu rõ: 'Bạn đang ở V3 nên menu này sẽ trông như thế này... Để làm X, bạn cần vào đây.' Tránh gửi screenshot không giải thích ngữ cảnh.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.