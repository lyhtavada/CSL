# Trigger birthday reward cho 1 customer bất kì

Category: Reward programs

### Problem

- Đến ngày sinh nhật nhưng customer không nhận được birthday reward (có thể do lỗi app).
- Merchant muốn trigger thủ công reward cho một số trường hợp đặc biệt.

---

### Causes

- Hệ thống bị delay hoặc lỗi khi generate birthday reward.
- Customer profile có thông tin ngày sinh nhưng không khớp với reward rule.
- Merchant muốn gửi reward ngoài trigger mặc định.

---

### Flow

1. **CS truy cập Dev zone > Dev tool**.
    - Tìm search option: **Trigger birthday for one customer**.
    
    ![image.png](Trigger%20birthday%20reward%20cho%201%20customer%20b%E1%BA%A5t%20k%C3%AC/image.png)
    
2. **Nhập thông tin customer**
    - Điền **Customer ID** vào field.
    - Nhấn button **Give birthday for one customer**.
    
    > **Lưu ý: chỉ nhấn 1 lần và chờ app xử lý (tránh ấn nhiều lần để không tạo nhiều code).**
    > 
3. **Xác nhận kết quả**
    - Sau khi trigger thành công, hệ thống sẽ tự động:
        - Gửi 1 email đến customer.
        
        ![image.png](Trigger%20birthday%20reward%20cho%201%20customer%20b%E1%BA%A5t%20k%C3%AC/image%201.png)
        
        - Hiển thị discount trong **customer detail page**.
        
        ![image.png](Trigger%20birthday%20reward%20cho%201%20customer%20b%E1%BA%A5t%20k%C3%AC/image%202.png)
        
4. **Thông báo lại cho merchant**
    - CS chủ động cập nhật tình trạng cho merchant sau khi reward đã được trigger thành công.