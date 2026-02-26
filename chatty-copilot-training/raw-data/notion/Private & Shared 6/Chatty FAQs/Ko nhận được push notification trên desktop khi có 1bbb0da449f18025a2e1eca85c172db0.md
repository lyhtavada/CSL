# Ko nhận được push notification trên desktop khi có tin nhắn mới

Category: Notifications

### **Problem/ Request**

MC ko nhận được push notification khi có tin nhắn mới

---

### **Possible causes**

- MC chưa enable Push notification cho new or unread messages ở App Settings
- MC chưa Allow notification cho app hoặc standalone link [app.meetchatty.com](http://app.meetchatty.com) của app ở Browsers, và PC/ laptop settings
- Lỗi app
- Ngoài ra push noti sẽ ko pop lên nếu máy đang ở mode presentation, là kiểu chình chiếu, hay đang screen recording

---

### **Support flow**

- CS hỏi xem MC đang dùng thiết bị gì
- CS cần đảm bảo CS đã cài đặt đủ các setting sau, dùng shortcut ***!push-noti-check:***
    - Đã allow notification ở [Browser](https://prnt.sc/JEKewQcAqNYx)
    - Đã allow notification ở [PC/ laptop settings](https://prnt.sc/VE_6yfDtZEQ_)
    - PC/ laptop đang ở chế độ nhận thông báo như bình thường, ko ở chế độ Silent, Do not disturb.
- CS cần test lại phía mình, nếu tính năng hoạt động bình thường thì chụp bằng chứng để gửi cho MC, chứng minh rằng feature vẫn hoạt động. Sau đó có thể giải thích rằng issue có thể đến từ setting của device.
- Trong TH MC đã set đúng nhưng vẫn ko nhận đc thông báo push, CS gợi ý:
    - Clear cache và cookies
    - Tắt computer đi và bật lại
    - Mở Inspect code (F12) > Application > Service worker > Update [https://app.meetchatty.com/firebase-messaging-sw.js](https://app.meetchatty.com/firebase-messaging-sw.js)
    
    ![image.png](Ko%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20push%20notification%20tr%C3%AAn%20desktop%20khi%20c%C3%B3/image.png)
    
- Trong quá trình hỗ trợ, nếu CS nhận thấy việc hướng dẫn và thu thập đầy đủ thông tin từ KH mất quá nhiều thời gian và ko giải quyết được vấn đề, CS có thể chủ động đề xuất phương án để team sử dụng Teamviewer hoặc Anydesk nhằm trực tiếp kiểm tra phần cài đặt cho khách hàng.
    - Shortcut: **`!teamview-check`**
- Nếu issue vẫn xảy ra, CS forward issue cho dev kèm thông tin chi tiết.

<aside>

💡 Trong lúc đợi fix issue, CS cần recommend type thay thế như Email notification hoặc install mobile app để nhận đc instant notification về new message.

</aside>

- CS theo dõi và cập nhật tiến độ cho MC