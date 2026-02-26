# Tính năng Notifications bị disabled

Category: Notifications

### ✏️ Scenario

MC contact muốn đc enable tính năng Notifications

### ⁉️Possible causes

Hiện tại đang có nhiều scammer lợi dụng app Joy để gửi email phishing. Vì vậy, tất cả các store mới tạo dưới 7 ngày và cài app từ sau ngày 13/1 sẽ bị disable tính năng Notifications. Các store tạo trên 7 ngày vẫn sử dụng tính năng này như bình thường.

### ➡️ Support flow

1. CS xin store URL từ MC.

2. Sử dụng shortcut ***!stop-notifications*** để giải thích lý do và hẹn khách.

3. CS thực hiện verify store:

- Thông thường, scammer hay sử dụng dev store để gửi phishing emails.
- CS cần review kỹ store dựa trên các yếu tố như store form, nội dung, hoặc dấu hiệu bất thường để nhận biết.

4. Kết quả xử lý:

- Nếu là store thật: [Enable tính năng trong Dev_zone](https://prnt.sc/Rt7Ny0pdnV5k) và báo lại MC ***!approved-notifications***

![image.png](T%C3%ADnh%20n%C4%83ng%20Notifications%20b%E1%BB%8B%20disabled/image.png)

- Nếu không phải là store thật: Sử dụng shortcut ***!denied-notifications*** để từ chối và giải thích lý do.

### 🪞 References

### Tips & Tricks (optional)

rule với store <7 days là logic ngầm, CS KO ĐƯỢC share với users để tránh trường hợp dùng trick để bypass rule.