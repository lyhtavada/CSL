# QA Tuần 2026-W22 — Sonny
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 87/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 28.2/34 · 📚 Kiến thức 30/33 · 🛠️ Xử lý 29/33

## 📝 Nhận xét chung
Bạn hoàn thành một tuần ổn định với 30 chat đa phần là Joy, xử lý cả tiếng Anh, tiếng Tây Ban Nha, tiếng Pháp, tiếng Đức, tiếng Trung, tiếng Ý — thể hiện tính linh hoạt đáng kể. Điểm mạnh nổi bật nhất là ownership: bạn theo sát case qua nhiều ca, gửi email cập nhật chủ động, và hoàn thành công việc đúng hẹn. Tuy nhiên có 2 lần bạn đưa nội dung/thông tin ra ngoài mà chưa kiểm tra kỹ — một lần thay đổi label widget live khiến khách bị ngạc nhiên (chat #10), một lần widget setup bị khách chê hết lượt vì nội dung không phù hợp brand (chat #28) — cả hai đều làm kéo dài chat và mất điểm tin tưởng. Đây là hướng cần tập trung: trước khi push bất kỳ thứ gì ra live hoặc gửi preview, hãy verify xem nội dung đó có ảnh hưởng tới live store không và có match với brand khách chưa.

## ✅ Điểm tốt
- **[P1]** Ownership xuyên suốt — theo dõi case qua nhiều ca, gửi email cập nhật chủ động, không để case rơi giữa chừng. Đặc biệt rõ ở các case phức tạp kéo dài nhiều ngày. (3, 12, 23)
- **[P2]** Proactive thật sự — export CSV trước khi khách hỏi (chat #23), đề xuất DFY service đúng thời điểm, offer widget upgrade kèm demo link và preview trước khi live. (12, 15, 23)
- **[P3]** Tự nhận lỗi rõ ràng khi mắc phải — ở chat #10 xác nhận ngay việc label bị thay đổi là do mình, ở chat #18 tự gửi tin đính chính sau khi nhận ra lỗi v3/v4, không che giấu hay đổ lỗi. (10, 18, 28)

## 🔧 Cần cải thiện
- **[KN5 · Moderate]** Widget setup với nội dung không phù hợp brand khách, gây khách bức xúc và phải reset toàn bộ
  - *Dẫn chứng:* Customer (Callum Whitehouse): 'Please remove all of those images. Please remove the product recommendations... the wording is very bad. We wouldn't say Labs points, Gather Joy, Claim Perks'
  - → Trước khi setup widget DFY, đọc tên brand/tone của store (xem header, product names) để chọn label và image phù hợp. Tránh dùng Joy default text khi store có naming convention riêng. Preview nội dung một lần trước khi gửi link cho khách.
- **[KN5 · Moderate]** Thay đổi nội dung shared giữa classic widget và unified widget mà không kiểm tra scope — dẫn đến live widget bị thay đổi ngoài ý muốn
  - *Dẫn chứng:* CS (Sonny): 'Yes my apologies. I wasn't aware that the content is updated as well' — sau khi khách phát hiện label 'REWARDS' bị đổi thành 'TREATS' trên live store
  - → Khi customise unified widget content, luôn kiểm tra trước xem field đó có được share với classic widget không. Nếu không chắc, test trên preview link trước khi confirm với khách rằng chỉ ảnh hưởng widget mới.
- **[KN1 · Low]** Gửi message tiếng Anh cho khách đã chat hoàn toàn bằng tiếng Pháp trong cùng một chat, gây inconsistency
  - *Dẫn chứng:* CS (Sonny) [chat #15, 16:08]: 'Please take a quick look at my screenshots to see where I configure the new version widget and its result. Or directly click on this link...' — trong khi toàn bộ conversation trước đó là ti
  - → Khi đã dùng ngôn ngữ nào với khách trong chat đó, giữ consistent. Nếu gửi template tiếng Anh, thêm một dòng bằng ngôn ngữ của khách để chào trước.
- **[KN3 · Low]** Gửi tin nhắn offer widget upgrade sai version (nhầm v3/v4 shortcut), buộc phải gửi tin đính chính rõ ràng và xin lỗi
  - *Dẫn chứng:* CS (Sonny) [chat #18]: 'In this new version, you will be able to set the detail description for each redeeming program on the widget' — sau đó Liz comment: 'kh này vẫn ở v3 mà @sonny', Sonny phải gửi: 'Please disregard m
  - → Trước khi gửi offer widget upgrade, verify version của store (classic vs unified) bằng cách xem widget settings hoặc check referral block type. Tránh gửi template sai version gây mất uy tín.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.