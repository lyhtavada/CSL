# QA Tuần 2026-W22 — Andy
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 83/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 27.7/34 · 📚 Kiến thức 27.7/33 · 🛠️ Xử lý 27.6/33

## 📝 Nhận xét chung
Andy có phong cách làm việc đáng tin cậy và ấm áp — bạn xử lý được cả những chat dài phức tạp lẫn các ca nhanh, duy trì được tone tốt với khách xuyên suốt. Điểm mạnh nổi bật nhất là khả năng đa ngôn ngữ (Pháp, Đức, Ý, Tây Ban Nha, Trung) và ownership ở những ca kỹ thuật nghiêm trọng (mất sale $3k ở chat #14). Tuy nhiên có 1 điểm cần sửa ngay: ở chat #16 bạn khẳng định dữ liệu chat lịch sử "sẽ bị xóa vĩnh viễn khi downgrade" — trong khi KB nội bộ ghi rõ "Downgrading does not delete your data" — nếu thông tin này sai, khách có thể ra quyết định downgrade dựa trên thông tin không chính xác và sau đó khiếu nại. Ngoài ra, ở chat #6 bạn giải thích cùng một nội dung về FCR 75% lặp lại 4 lần mà không thay đổi cách giải thích — khách phải hỏi đi hỏi lại, kéo dài chat không cần thiết. Tuần tới: chú trọng verify trước khi xác nhận thông tin về plan/billing, và khi khách hỏi lại nhiều lần thì cần đổi cách giải thích hoặc escalate.

## ⚠️ Cần Liz xem trước
- CHAT #16: Potential KT1 — Andy confirmed 'older chats will be deleted after downgrading' and 'permanently lost and cannot be recovered', which directly contradicts KB entry: 'Downgrading does not delete your data or settings.' Liz to verify actual downgrade data retention behavior before DM is sent.

## ✅ Điểm tốt
- **[P1]** Ownership xuất sắc ở những ca kỹ thuật phức tạp và dài. Chat #1 (HotTubs24) kéo dài nhiều giờ với hàng chục vấn đề chồng chất — Andy theo đến cùng, đánh dấu urgent, lấy theme access, và cập nhật khách liên tục. Chat #14 (American Muscle Docks) khách mất sale $3k vì AI sai — Andy nhận case, escalate, tự thêm scenario, và follow-up kết quả trong cùng phiên. (CHAT #1, CHAT #14)
- **[P3]** Chủ động phát hiện vấn đề khách chưa hỏi tới. Chat #1: proactively chỉ ra notification settings chưa đúng khi khách chỉ hỏi về AI. Chat #11: tự thêm email hỗ trợ vào AI knowledge base sau khi xử lý xong yêu cầu chính. Chat #3: chủ động nhận ra khách đang dùng default FAQs và đề xuất cập nhật. (CHAT #1, CHAT #3, CHAT #11)
- **[P2]** Empathy tự nhiên và không gượng. Chat #3: chủ động chuyển sang tiếng Pháp khi khách nói 'my English is basic' — không cần khách yêu cầu. Chat #18: thể hiện sự thấu hiểu thực về áp lực chi phí AI của khách ('So sorry to hear so... The AI cost is really high lately due to the pricing increase'). (CHAT #3, CHAT #18)
- **[P1]** Đa ngôn ngữ ổn định và chất lượng. Andy phục vụ khách bằng Pháp (#3), Đức (#4), Ý (#10), Tây Ban Nha (#22, #23), Trung (#29) trong cùng một tuần — không chỉ dịch máy mà còn maintain được tone ấm và nội dung chính xác. (CHAT #3, CHAT #4, CHAT #10, CHAT #22, CHAT #23, CHAT #29)

## 🔧 Cần cải thiện
- **[KT1 · Critical]** Xác nhận sai rằng chat history sẽ bị xóa vĩnh viễn khi downgrade — trong khi KB nói ngược lại
  - *Dẫn chứng:* CS (Andy): 'The older chats will be deleted after downgrading' và 'Your removed chats will be permanently lost and can not be recovered' (CHAT #16)
  - → Trước khi xác nhận bất kỳ hành vi nào liên quan đến billing/plan/data retention, cần tra KB hoặc hỏi lead — đặc biệt là câu hỏi về 'điều gì xảy ra khi downgrade'. KB hiện nói 'Downgrading does not delete your data or settings' — nếu thực tế khác thì cần flag để cập nhật KB. Không được khẳng định một chiều khi chưa chắc.
- **[KN7 · Moderate]** Giải thích FCR 75% lặp lại nguyên văn 4 lần mà không thay đổi cách diễn đạt — khách phải hỏi lại nhiều lần, kéo dài chat
  - *Dẫn chứng:* CS (Andy): 'That is the current logic at the moment.' (x2), 'We will calculate the first response time of the 75% conversations that have the fastest reply', 'As I mentioned, the 75% of the conversations have the fastes 
  - → Khi khách hỏi lại cùng một câu sau 2-3 lần, đây là tín hiệu cách giải thích chưa hiệu quả — cần đổi góc độ (ví dụ: dùng số cụ thể 'nếu có 100 conversation, ta loại 25 chậm nhất, tính trung bình 75 còn lại'), hoặc thừa nhận giới hạn thông tin và escalate sang tài liệu/lead.
- **[KN3 · Low]** Giải thích hành vi auto-resolve trả lời hơi vòng vo khi khách hỏi về Zendesk ticket cho các conversation chưa resolve
  - *Dẫn chứng:* CS (Andy): 'At the moment, all of your conversations will be auto resolved after 60 minutes due to your current settings -> therefore you won't miss any resolved ones as they will be created as a ticket on Zendesk' (CHAT
  - → Với các câu hỏi về flow (điều gì xảy ra với conversation X → Zendesk Y), nên dùng format bước từng bước: 'Bước 1: conversation được resolve (tự động sau 60 phút hoặc thủ công). Bước 2: ngay khi resolve, Zendesk ticket được tạo.' Tránh ghép nhiều điều kiện vào một câu.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.