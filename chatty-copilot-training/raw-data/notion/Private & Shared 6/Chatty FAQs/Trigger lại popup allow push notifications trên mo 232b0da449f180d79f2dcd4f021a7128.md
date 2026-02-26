# Trigger lại popup allow push notifications trên mobile app

Category: Notifications
PIC: Trương Cảnh Huy

### Problem:

MC vô tình bỏ qua popup allow push notifications sau khi mới cài mobile app, dẫn đến việc không nhận noti trên mobile dù check trên admin thấy đã bật push noti

---

### Solution:

- Cần mở mobile app và truy cập Settings > Notifications từ đó để trigger popup

![image.png](Trigger%20l%E1%BA%A1i%20popup%20allow%20push%20notifications%20tr%C3%AAn%20mo/image.png)

![image.png](Trigger%20l%E1%BA%A1i%20popup%20allow%20push%20notifications%20tr%C3%AAn%20mo/image%201.png)

- Nếu popup không hiển thị thì ấn “Send test” tại mục Web push để trigger thủ công lại popup. Tham khảo video: [https://drive.google.com/file/d/1tRytIJar1mQH8krgOMsaOUw3WQGSkOtz/view?usp=sharing](https://drive.google.com/file/d/1tRytIJar1mQH8krgOMsaOUw3WQGSkOtz/view?usp=sharing)
- Nếu cách trên không work, cần gỡ mobile app và add lại sau đó làm lại bước trên để trigger và test push noti

Video: [https://drive.google.com/file/d/1bN064_QFta6CcJSX4sKhTRDI78k4lkIx/view?usp=sharing](https://drive.google.com/file/d/1bN064_QFta6CcJSX4sKhTRDI78k4lkIx/view?usp=sharing)

- Sau đó thể tham khảo thêm FAQ sau để check thêm trong device settings nếu vẫn chưa nhận được push noti: [Chatty không hiện trong device/notifications settings của mobile](Chatty%20kh%C3%B4ng%20hi%E1%BB%87n%20trong%20device%20notifications%20setti%2023db0da449f1809eb255de13b6ed88a1.md)