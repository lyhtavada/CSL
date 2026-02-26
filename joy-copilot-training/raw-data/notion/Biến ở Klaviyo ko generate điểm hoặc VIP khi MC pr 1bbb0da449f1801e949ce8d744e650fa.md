# Biến ở Klaviyo ko generate điểm hoặc VIP khi MC preview email content

Category: Integrations

### ✏️ Scenario

Sau khi đã integrate app Joy với Klaviyo thành công, các attributes sau sẽ được sync sang app Klaviyo:

- Birthday: customer's birthday collected by Joy
- Joy loyalty points: customer's current balance in Joy
- Joy Referral URL: customer's referral link
- Joy VIP tier: customer's current VIP Tier name in Joy

Thông tin như điểm thưởng, VIP tier hoặc trạng thái thành viên có thể được tự động hiển thị trong email nhờ các biến (variables) được cung cấp sẵn trong trình chỉnh sửa email của Klaviyo. Bạn có thể xem video hướng dẫn sau để hiểu rõ cách thiết lập:

[https://www.loom.com/share/0deab38b8f284d76ac6ebeefeea91003](https://www.loom.com/share/0deab38b8f284d76ac6ebeefeea91003)

Sau khi tạo xong nội dung email, hầu hết MC sẽ chọn một profile (hay còn gọi là contact trong app AEM) để **xem trước (preview)** cách email sẽ hiển thị cho khách hàng. Nếu profile đó đã có thông tin về điểm, tier, birthday hoặc member status, các giá trị tương ứng sẽ được **tự động hiển thị đúng** dựa trên các biến bạn đã chèn vào trong nội dung email.

![image.png](Bi%E1%BA%BFn%20%E1%BB%9F%20Klaviyo%20ko%20generate%20%C4%91i%E1%BB%83m%20ho%E1%BA%B7c%20VIP%20khi%20MC%20pr/image.png)

Tuy nhiên, đôi khi vẫn xảy ra lỗi: ví dụ, khi chọn một profile để xem trước, số điểm, VIP tier hoặc trạng thái thành viên không hiển thị hoặc hiển thị sai – mặc dù profile đó đã có dữ liệu.

4o

![image.png](Bi%E1%BA%BFn%20%E1%BB%9F%20Klaviyo%20ko%20generate%20%C4%91i%E1%BB%83m%20ho%E1%BA%B7c%20VIP%20khi%20MC%20pr/image%201.png)

### ⁉️Possible causes

- **Quá trình đồng bộ dữ liệu chưa hoàn tất**, nên thông tin từ app chưa được cập nhật đầy đủ sang Klaviyo.
- **MC chưa tạo đủ API key cần thiết** khi thiết lập kết nối giữa Joy Loyalty app và Klaviyo, dẫn đến dữ liệu không được sync chính xác.
- **Một số lý do khác liên quan đến cấu hình hoặc hạn chế của hệ thống** cũng có thể gây ra tình trạng hiển thị sai hoặc thiếu dữ liệu.

### ➡️ Support flow

1. **Xác định profile cụ thể đang gặp vấn đề:**
    
    Hỏi MC xem họ đang **preview hoặc gửi test email** cho profile (customer) nào trong Klaviyo.
    
2. **Kiểm tra thông tin trong app Joy:**
    
    Vào app Joy và tìm đúng customer đó để kiểm tra xem họ đã có các thông tin cần thiết (points, tier, member status) chưa.
    
3. **Kiểm tra trạng thái integration:**
    - Truy cập vào **Joy > Integration > Klaviyo** để xác nhận rằng quá trình kết nối đã hoàn tất.
    
    ![image.png](Bi%E1%BA%BFn%20%E1%BB%9F%20Klaviyo%20ko%20generate%20%C4%91i%E1%BB%83m%20ho%E1%BA%B7c%20VIP%20khi%20MC%20pr/image%202.png)
    
    - Đồng thời, nhờ MC **gửi ảnh chụp chi tiết của 1 profile bất kỳ trong Klaviyo**, để kiểm tra xem thông tin từ Joy đã được đồng bộ sang Klaviyo chưa. Ví dụ: điểm và tier có đang hiển thị đúng trong custom properties không.
    
    ![image.png](Bi%E1%BA%BFn%20%E1%BB%9F%20Klaviyo%20ko%20generate%20%C4%91i%E1%BB%83m%20ho%E1%BA%B7c%20VIP%20khi%20MC%20pr/image%203.png)
    
4. **Xử lý tiếp theo tùy theo kết quả kiểm tra:**
- Nếu cài đặt và đồng bộ thiếu, nhờ MC generate 1 API key khác và thử integrate lại.
- Nếu cài đặt và đồng bộ đều đúng mà vẫn xảy ra lỗi: **CS chuyển issue cho dev team điều tra thêm** và thông báo lại cho MC rằng dev đang xử lý.
1. Trong suốt quá trình, CS cần **liên tục cập nhật tiến độ cho MC** cho đến khi vấn đề được giải quyết hoàn toàn.

###