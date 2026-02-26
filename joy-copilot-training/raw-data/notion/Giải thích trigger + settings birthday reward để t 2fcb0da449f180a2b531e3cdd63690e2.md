# Giải thích trigger + settings birthday reward để tính chính xác ngày nhận reward

Category: Reward programs

### ✏️ Scenario

MC thường xin tư vấn về cách set up birthday reward cho hợp ý họ (muốn customer nhận quà ngay sau khi nhập/trong tháng sinh nhật, etc.) hoặc hỏi tại sao customer lại không nhận được birthday reward dù đã nhập trước birthday.

### ⁉️Giải thích settings

Cần phải để ý 2 phần settings chính dẫn đến điều kiện ngày trigger birthday:
1. Birthday allowed after trong dev_zone (default là 30 ngày): [https://capture.avada.io/i/xBMgQbjVHXhU](https://capture.avada.io/i/xBMgQbjVHXhU)
2. Settings When to reward trong app: [https://capture.avada.io/i/L2FSu9HM8Set](https://capture.avada.io/i/L2FSu9HM8Set)
- Exact birthday date: Lấy birthday làm mốc, MC có thể cho phép customer nhận quà trong chính ngày sinh nhật hoặc trước đó vài ngày. Không khuyến khích dùng cho option nhận quà Manual vì customer chỉ cần quên ko claim quà trong ngày là miss.
- Calendar month of birthday: Hệ thống sẽ scan và gửi quà vào ngày 1 mỗi tháng. Tuy nhiên, trong một số trường hợp customer không đủ điều kiện nhận quà vào ngày 1, app sẽ còn 1 đợt scan vào cuối tháng (ngày 30) để đảm bảo customer sẽ không bị miss quà trong năm đó.
- Around birthday (chỉ dùng cho option nhận quà manual): Set 1 date range với mốc là birthday để customer có thể claim quà trong khoảng đó, bỏ qua là miss.
⇒ Cần phải kết hợp cả 2 điều kiện này mới có thể tính chính xác ngày app sẽ trigger bithday. Ví dụ:
- Nếu MC set nhận quà automatic, when to reward là exact birthday date + Reward before day là 7 ngày, thì customer sẽ phải nhập birthday trước ít nhất 30 (theo default) + 7 = 37 ngày để đủ điều kiện nhận quà năm nay. Nếu mà không đủ điều kiện này ⇒ miss.
- Nếu Birthday allowed after chỉnh về 0, MC chọn option nhận quà Automatic và Calendar month of birthday: Hệ thống sẽ gửi quà vào ngày 1 của tháng birthday trong trường hợp customers đã nhập birthday trước ngày 1 tháng đó. Giả sử khách có birthday vào 20/1, mà 15/1 mới nhập, app sẽ scan thêm và gửi quà vào ngày 30.

### ➡️ Một số case thường gặp:

- 

### 🪞 References

[https://trello.com/c/grByLMYE/135911-joy-check-workflow](https://trello.com/c/grByLMYE/135911-joy-check-workflow)
[https://avadaio.slack.com/archives/C020QJ7F7RN/p1766740637739599](https://avadaio.slack.com/archives/C020QJ7F7RN/p1766740637739599)

### Tips & Tricks (optional)