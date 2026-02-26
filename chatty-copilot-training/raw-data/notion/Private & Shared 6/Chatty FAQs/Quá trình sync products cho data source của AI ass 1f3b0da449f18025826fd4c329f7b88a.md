# Quá trình sync products cho data source của AI assistant bị stuck

Category: AI Assistant

### Problem/ Request

Quá trình sync products cho data source của AI Assistant bị stuck

![image.png](Qu%C3%A1%20tr%C3%ACnh%20sync%20products%20cho%20data%20source%20c%E1%BB%A7a%20AI%20ass/image.png)

### **Nguyên nhân**

Quá trình đồng bộ sản phẩm (sync products) từ Shopify store về data source của AI Assistant có thể bị treo (stuck) do một số lý do như:

- Mạng không ổn định trong quá trình đồng bộ
- Shopify trả về dữ liệu lỗi hoặc không đầy đủ
- Quá trình sync trước đó bị gián đoạn và không được khởi động lại đúng cách

---

### **Flow**

### **1. Xác nhận thời điểm bắt đầu quá trình sync**

- Vào trang **AI Assistant > Data source** của merchant
- Kiểm tra timestamp của lần sync gần nhất để xác định đã bắt đầu từ khi nào

### **2. Nếu sync đã bắt đầu từ lâu mà không có tiến triển**

- Vào **Devzone > Testing**
- Nhấn nút **Start** **Auto Resync** để reset và khởi động lại quá trình sync

![image.png](Qu%C3%A1%20tr%C3%ACnh%20sync%20products%20cho%20data%20source%20c%E1%BB%A7a%20AI%20ass/image%201.png)

> ⚠️ Sau khi nhấn Auto Resync, quá trình sync sẽ được làm mới từ đầu
> 

### **3. Theo dõi và xác nhận kết quả**

- Sau khi resync, CS báo lại khách để tiếp tục theo dõi kết quả
- Khi quá trình hoàn tất (sản phẩm đã hiển thị đầy đủ trong data source), CS nhắn lại để thông báo cho merchant

### **Lưu ý**

- Chỉ nên dùng **Auto Resync** khi chắc chắn sync đang bị treo và không tự xử lý
- Trong lúc sync lại, không khuyến khích merchant thao tác thêm trên app (cập nhật/sửa product tags…) để tránh dữ liệu xung đột