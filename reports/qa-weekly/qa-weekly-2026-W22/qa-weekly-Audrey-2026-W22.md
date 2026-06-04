# QA Tuần 2026-W22 — Audrey
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 84/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 28.1/34 · 📚 Kiến thức 28.5/33 · 🛠️ Xử lý 27/33

## 📝 Nhận xét chung
Tuần này bạn thể hiện khá ổn: tone ấm, chủ động nhìn xa hơn yêu cầu của khách (tự phát hiện widget bị đè, tự đề xuất fix icon), và theo đuổi case tới khi có kết quả rõ ràng. Điểm mạnh nổi bật nhất là mindset proactive — nhiều chat bạn làm thêm mà khách không cần hỏi. Điểm cần tập trung nhất tuần tới là kỹ năng xử lý: một lần copy-paste nhầm nội dung email sang sai case (chat #5), một lần hiểu sai store khách đang dùng và phải hỏi lại nhiều lần (chat #1). Hai lỗi này đều làm khách bối rối và kéo dài chat không cần thiết — đây là vấn đề cần sửa để giữ điểm skill nhất quán.

## ⚠️ Cần Liz xem trước
- Chat #5: Audrey gửi nhầm email nội dung 'VIP Tier migration completed' cho merchant đang report lỗi điểm bị tính sai sau khi huỷ đơn. Không phải data breach nhưng là sai sót nghiêm trọng về communication — cần Liz review trước khi DM.

## ✅ Điểm tốt
- **[P1]** Ownership xuyên suốt: theo case tới khi có kết quả, không đóng lửng khi chưa có feedback từ khách. Ví dụ chat #2 (VIP migration): escalate → confirm fix → follow-up email → nhận feedback xác nhận từ khách trước khi kết thúc. (#2, #9, #23)
- **[P2]** Chủ động vì khách: phát hiện vấn đề chưa được hỏi và xử lý luôn mà không chờ khách báo. Chat #3 bạn tự nhận thấy loyalty button bị gift button đè và đề xuất đổi vị trí; chat #9 tự phát hiện icon widget thừa và hỏi khách trước khi xóa. (#3, #9, #15)
- **[P3]** Tone ấm, tạo được rapport thật — khách chủ động để lại review và comment tốt về cá nhân bạn sau khi chat. Không phải dạng 'xã giao' mà là từ chất lượng support thực tế. (#9, #2, #15)

## 🔧 Cần cải thiện
- **[KN1 · High]** Copy-paste nhầm nội dung email sang sai case: gửi email nói 'we have successfully migrated the customers' VIP Tiers data to your EU store' cho khách đang hỏi về điểm bị trừ sai sau khi huỷ đơn — hoàn toàn không liên quan.
  - *Dẫn chứng:* [11:42:19] CS (Audrey): 'I'm delighted to share with you that we have successfully migrated the customers' VIP Tiers data to your EU store. Could you kindly spare a moment to review it again and confirm the update?'
  - → Trước khi gửi email follow-up, đọc lại nội dung một lần và đối chiếu với context của chat đó. Với template email, thêm bước confirm: subject + tên khách + issue chính xác.
- **[KN5 · Moderate]** Hiểu sai store khách đang dùng: khách nói đang cài Joy trên 2 stores và cần fix link trên nekane.mx, nhưng bạn giả định là store aguascalientes-travel và hỏi lại — làm khách phải giải thích lại nhiều lần.
  - *Dẫn chứng:* [06:31:15] CS (Audrey): 'Ah, asumo que te gustaría cambiar el enlace de inicio de sesión para este sitio web https://aguascalientes-travel.myshopify.com/password'
  - → Khi khách đề cập nhiều stores, xác nhận rõ store nào đang được hỏi trước khi truy cập hoặc giả định. Câu xác nhận đơn giản: 'Just to confirm, you'd like me to check nekane.mx, correct?' — tránh nhầm.
- **[KN3 · Low]** Đôi khi trả lời có chút cứng nhắc khi cần hướng dẫn cụ thể hơn. Chat #27: khi khách hỏi về milestone behavior, bạn trả lời đúng nhưng chưa đủ rõ về việc historical data có được tính hay không — Hana phải vào sau để giải thích đầy đủ.
  - *Dẫn chứng:* [08:54:48] CS (Audrey): 'I'd like to inform you that deleting and recreating a milestone program will not reset your customers' historical purchase data. Joy reviews the customer's history in your store to determine whet
  - → Khi trả lời câu hỏi về logic hệ thống (milestone, VIP tier), thêm ví dụ cụ thể ngay vào câu trả lời: 'For example, if a customer already spent 60,000 THB before, they will immediately qualify for the new milestone.' Điều này giúp khách không cần hỏi lại.
- **[KN1 · Low]** Một lần giữa chat với merchant có Liz nhắc nhở bạn không cần confirm store URL trước khi hướng dẫn — chỉ cần guide thẳng khi câu hỏi là generic về cách dùng tính năng.
  - *Dẫn chứng:* [07:52:22] CS (Liz Allen): '@audrey chị ơi, case này kh đang hỏi về cách setup, mình có thể guide kh mà ko cần cf store. Mình chủ động guide kh lại nhé chị'
  - → Phân biệt nhanh: câu hỏi how-to (cách dùng feature) → guide thẳng, không cần confirm store. Câu hỏi bug/lỗi cụ thể → mới cần confirm store để check.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh