# QA Tuần 2026-W22 — Linda
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 79/100 — Đạt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 26.7/34 · 📚 Kiến thức 26.8/33 · 🛠️ Xử lý 25.5/33

## 📝 Nhận xét chung
Tuần này Linda xử lý khối lượng chat lớn với tinh thần chủ động và tận tâm rõ rệt — bạn sẵn sàng vào thẳng cấu hình, chạy test AI, sửa issue thực tế trên store thay vì chỉ hướng dẫn lý thuyết. Điểm mạnh nổi bật nhất là ownership: theo case đến cùng, tự làm thay vì đẩy khách tự xử. Tuy nhiên, điểm yếu cần tập trung ngay là kỹ năng diễn đạt: lỗi chính tả lặp lại nhiều chat (jusst, expactation, double-chẹc, assisst, forr, lòa), câu trả lời đôi khi vòng vo trước khi đi vào vấn đề — hệ quả trực tiếp là khách phải hỏi lại hoặc chỉnh lại bạn giữa chừng. Nếu không cải thiện kỹ năng viết, chất lượng phục vụ tốt của bạn sẽ bị giảm đi đáng kể vì khách cảm nhận được sự thiếu chuyên nghiệp trong từng tin nhắn.

## ⚠️ Cần Liz xem trước
- KB inconsistency flag (không phải lỗi CS): Chat #18 — faq_team.md ghi Pro=5 total nhưng faq_pricing.md ghi Pro=10 members. Linda nói '10 member in total'. Liz verify và update KB trước khi feedback CS.

## ✅ Điểm tốt
- **[P1]** Ownership mạnh — chủ động vào cấu hình, chạy test AI, debug trực tiếp trên store thay vì chỉ hướng dẫn. KH không cần tự làm nhiều. (#1, #4, #5, #25)
- **[P3]** Proactive về tips và tối ưu: thường xuyên gợi ý Sync Store Page, Review Source, Best Seller setup, AI re-engage sau khi xử lý xong yêu cầu chính — thể hiện tư duy nghĩ xa hơn yêu cầu của khách. (#1, #3, #9, #13)
- **[P2]** Follow-up có trách nhiệm: gửi email cập nhật cho KH sau ca, theo dõi tiến trình G2 review, báo kết quả rõ ràng. (#4, #10, #21, #23)

## 🔧 Cần cải thiện
- **[KN1 · Moderate]** Lỗi chính tả và ngữ pháp lặp lại nhiều chat — làm giảm hình ảnh chuyên nghiệp
  - *Dẫn chứng:* Chat #1: 'double-chẹc it on your end', 'Let me done a quick test', 'expactation', 'jusst show the reason'; Chat #14: 'I've already sent it to our team to check the lòa page forr you'; Chat #6: 'We're very appreciate your
  - → Trước khi gửi, đọc lại lần cuối — đặc biệt với các tin nhắn dài. Cài extension kiểm tra chính tả cho tiếng Anh. Tập trung vào các lỗi lặp nhiều nhất: 'just', 'assistance', 'double-check'.
- **[QT9 · Moderate]** Hỏi vòng vo trước khi đi vào vấn đề — khách phải nhắc lại hoặc chỉnh lại bạn
  - *Dẫn chứng:* Chat #17: Linda hỏi 'You mean that Chatty takes a few seconds to load when you open the page, am I right?' → 'Can you kindly share details about what you want' → khách phải nhắc lại: 'I think you misunderstood me'. Chat 
  - → Đọc kỹ và xem hết ảnh/video KH gửi trước khi hỏi. Nếu cần xác nhận, hỏi 1 câu cụ thể, không hỏi mở chung chung.
- **[QT22 · Moderate]** Bỏ sót câu hỏi khi KH hỏi nhiều vấn đề cùng lúc
  - *Dẫn chứng:* Chat #1 [11:39:40]: KH hỏi 3 vấn đề (human handoff, AI reply about shipping, refund setup). Linda trả lời về refund/AI settings nhưng không đề cập shipping query cho đến nhiều tin sau. Chat #25 [09:35:33]: KH hỏi về vega
  - → Khi KH hỏi nhiều vấn đề, tóm tắt list và xử lý từng cái. Ví dụ: 'Tôi thấy bạn có 3 câu hỏi, để tôi xử lý lần lượt: 1)... 2)... 3)...'
- **[KT2 · Low]** Phản hồi ban đầu chưa chính xác về metafield vs tag trong Chatty product sync
  - *Dẫn chứng:* Chat #25 [09:35:33]: KH báo AI không nhận diện sản phẩm vegan/gluten-free từ Shopify metafield. Linda hướng dẫn 'add more detailed product descriptions' — sai hướng. KH phải giải thích lại là dùng metafield. Linda sau đó
  - → Khi gặp case AI không đọc được thông tin sản phẩm, hỏi KH lưu data đó ở đâu (metafield, tag, description) trước khi đưa hướng dẫn. Verify KB về metafield support trong Chatty.
- **[KT1 · Low]** Claim về số team member của Pro plan có thể sai — cần Liz verify KB inconsistency trước khi xác nhận
  - *Dẫn chứng:* Chat #18 [10:54:00]: CS (Linda): 'We have pro plan that you can add 10 member in total' — KB faq_team.md ghi Pro = 4 additional (5 total), nhưng faq_pricing.md ghi '10 team members'. Hai file KB mâu thuẫn nhau.
  - → [FLAG CHO LIZ] Verify số team member chính xác cho Pro plan trong KB trước khi coaching Linda về điểm này. Nếu KB sai thì update KB, không phải lỗi CS.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.