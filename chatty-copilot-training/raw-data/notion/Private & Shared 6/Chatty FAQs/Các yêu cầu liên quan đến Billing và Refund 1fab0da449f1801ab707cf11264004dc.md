# Các yêu cầu liên quan đến Billing và Refund

Category: Subscription

## **CS tìm hiểu lý do MC muốn cancel subscription hoặc refund:**

Trước khi nhận request, CS cần hiểu rõ lý do MC yêu cầu. Một số lý do phổ biến:

- **Bị tính phí ngoài ý muốn** (sau khi đã gỡ app hoặc trong thời gian trial)
- **Sự cố về subscription**
- **App không đáp ứng kỳ vọng**
- **Vấn đề kỹ thuật với app** (→ Trong trường hợp này, CS cần chủ động hỗ trợ khắc phục trước)

➡️ xác nhận vấn đề với MC, dùng shortcut **`!cancel-reason`** 

### Xử lý khi App không đáp ứng kỳ vọng hoặc xảy ra lỗi trong quá trình sử dụng

### **1. Ghi nhận vấn đề & xác định rõ kỳ vọng của MC**

Việc MC không hài lòng có thể đến từ:

- Tính năng không như mong đợi
- Giao diện khó dùng
- Setup khó hoặc MC không biết cách sử dụng

🎯 Mục tiêu: CS cần xác định rõ MC mong muốn app hỗ trợ như thế nào → đưa giải pháp/khắc phục phù hợp **trước khi xử lý refund**.

```jsx
Thanks for your feedback. I’m sorry to hear the app didn’t meet your expectations. Could you please share more details about what you were looking to achieve or what didn’t work as expected? I’d love to help clarify or find a solution that works for you.

```

---

### **2. Chủ động đề xuất hỗ trợ & test lại tính năng**

Nếu lỗi thuộc về setup/feature, hoặc MC chưa biết dùng:

- Hướng dẫn lại
- Thu thập thông tin về issue và hỗ trợ MC xử lý issue đó
- Nếu MC đã nắm được tính năng, và các vấn đề đã được giải quyết, khuyến khích MC tiếp tục dùng app (có thể nhắn lên nhóm, tham khảo CSL xem có thể offer discount tháng tới cho MC hay ko).

<aside>
⚠️

Nếu lý do refund là do app không đáp ứng kỳ vọng hoặc gặp lỗi, CS phải chủ động follow-up để xử lý triệt để vấn đề cho merchant, tránh để họ uninstall hoặc cancel app khi vấn đề chưa được giải quyết.

</aside>

### **3. Trong trường hợp MC vẫn muốn huỷ và refund**

- Gửi lời xin lỗi
- Xin đầy đủ các thông tin sau, dùng shortcut **`!billing-details`** :
    - Ảnh chụp hóa đơn có đầy đủ: **tên app, chu kỳ bill, số tiền**
        
        → Đảm bảo đúng định dạng: 
        
        ![image.png](C%C3%A1c%20y%C3%AAu%20c%E1%BA%A7u%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20Billing%20v%C3%A0%20Refund/image.png)
        
    - Xác nhận xem MC **đã thanh toán** hóa đơn hay chưa
    - Hướng dẫn MC **downgrade về gói Free** nếu chưa làm để tránh bị charge tiếp

### 4. CS tạo card:

- CS hẹn KH, dùng shortcut **`!refund-process`**
- Sau khi đã có đủ thông tin và **app đã ở bản Free**, CS tạo card, assign CSL và note lại đầy đủ chi tiết yêu cầu.

### Khi MC chỉ đơn giản không muốn tiếp tục dùng app hoặc subscribe nhầm (ko phải lý do liên quan đến app)

### 1. CS thu tập thông tin:

- Xin đầy đủ các thông tin sau, dùng shortcut **`!billing-details`** :
    - Ảnh chụp hóa đơn có đầy đủ: **tên app, chu kỳ bill, số tiền**
        
        → Đảm bảo đúng định dạng: 
        
        ![image.png](C%C3%A1c%20y%C3%AAu%20c%E1%BA%A7u%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20Billing%20v%C3%A0%20Refund/image.png)
        
    - Xác nhận xem MC **đã thanh toán** hóa đơn hay chưa
    - Hướng dẫn MC **downgrade về gói Free** nếu chưa làm để tránh bị charge tiếp

### 2. CS tạo card:

- CS hẹn KH, dùng shortcut **`!refund-process`**
- Sau khi đã có đủ thông tin và **app đã ở bản Free**, CS tạo card, assign CSL và note lại đầy đủ chi tiết yêu cầu.

<aside>
⚠️

CS **KHÔNG được phép** tự ý đồng ý bất kỳ request refund hoặc hỗ trợ nào mà chưa có sự phê duyệt của CSL.
Nếu CS tự ý đồng ý, CS sẽ phải tự chịu trách nhiệm và chi trả cho khoản đó.

</aside>