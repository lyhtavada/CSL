# Các vấn đề liên quan đến POS

Category: POS extension

### **Problem**

Khách báo lỗi khi sử dụng POS (ví dụ: không hiển thị điểm, không áp dụng reward, không đồng bộ dữ liệu, Failed to load…).

---

### **Causes**

- Có thể do lỗi chung của hệ thống POS hoặc app Joy.
- Có thể do lỗi phát sinh riêng ở một store cụ thể (liên quan đến thiết bị, cấu hình, hoặc quyền truy cập).

---

### **Flow**

1. CS check xem MC đang ở đúng bản mới nhất của Joy POS Extension chưa, nhiều lúc có thể do MC đang ở bản cũ. Bản mới có tên là **Joy Loyalty** sau khi add vào Tile.

![image.png](C%C3%A1c%20v%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20POS/image.png)

![image.png](C%C3%A1c%20v%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20POS/image%201.png)

1. **CS kiểm tra lại lỗi phía thiết bị của mình**:
    - Nếu **có lỗi tương tự**, xác nhận đây là **lỗi chung**, báo ngay cho Dev team xử lý.
2. Nếu **không có lỗi tương tự** → có thể là lỗi riêng của store, tiến hành theo các bước sau:
    - Nhờ MC update lên POS app version mới nhất > remove current tile > Add lại Joy Extension mới nhất để xem có hoạt động không.
    
    **Nếu vẫn không hoạt động:**
    
    - **Xin thông tin thiết bị** từ merchant để xác định môi trường test (dùng shortcut **`!pos-details`**).
    - **Xin quyền truy cập vào POS** từ merchant để CS/ TS/ Techlead/dev team có thể trực tiếp kiểm tra (dùng shortcut **`!pos-access`**).
    - Sau khi merchant **cấp quyền thành công**, **CS thử login và POS của MC và check lại từ phía mình.**
        - **Nếu ko có lỗi tương tự:** có thể do device, nhờ MC update lại device OS hoặc POS app (nếu chưa) và thử lại. Nếu phía KH vẫn ko work, CS report lỗi cho dev team.
        - **Nếu có lỗi tương tự:** CS forward cho dev luôn, hẹn lịch follow-up và cập nhật tiến độ xử lý cho merchant theo thông tin từ dev.
    
    <aside>
    📧
    
    request.pos@avadagroup.com/`Avada12345!@` 
    
    Scan QR sau để lấy mã 2FA authentication:
    
    ![image.png](C%C3%A1c%20v%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20POS/image%202.png)
    
    </aside>
    
    <aside>
    💡
    
    Chỉ sử dụng tài khoản Partner mặc định đã lưu trong shortcut.
    → Đây là tài khoản dùng chung, đã cài sẵn 2FA qua Authenticator App nhiều người truy cập được.
    
    ❌ Không dùng tài khoản cá nhân để xin quyền truy cập POS.
    
    request.pos@avadagroup.com/`Avada12345!@`
    
    CS **dùng tài khoản trên** để login vào Partner Dashboard. Sau đó, scan mã QR dưới đây bằng ứng dụng Authenticator.
    
    ![image.png](C%C3%A1c%20v%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20POS/image%203.png)
    
    Sau khi đăng nhập thành công, CS có thể **truy cập POS của MC như bình thường** để kiểm tra và hỗ trợ.
    
    </aside>
    
3. Trường hợp merchant **không thể cấp quyền POS**, CS vẫn **báo case lên Dev** kèm:
    - Mô tả chi tiết lỗi.
    - Thông tin thiết bị + bản POS app đang dùng.
    - Video/ảnh chụp lỗi (nếu có).
    - Tất cả dữ liệu cần thiết để Dev có thể **tái hiện lỗi**.