# Customer đã viết review nhưng ko nhận được điểm

Category: Reward programs

## Problem

Customer phản hồi rằng họ đã hoàn thành việc viết review nhưng không nhận được điểm thưởng từ chương trình loyalty.

---

## Cause

- Joy Loyalty chỉ tự động ghi nhận và cộng điểm **sau khi review được published**.
- Cả Joy Loyalty và app Reviews (Air Reviews, Judge.me, Yotpo, Loox, Stamped, Growave, Reviews.io, Tydal) đều cần đang ở **paid plan** để tính năng hoạt động.
- Nếu review chỉ ở trạng thái "Pending" hoặc app review không ở paid plan → hệ thống **không trigger** cộng điểm.

---

## Flow

1. **CS tự vào app và xác nhận lại app review mà merchant đang dùng + đảm bảo app đã được connect với Joy Loyalty và Write reviews program đã được tạo.**
2. **Xác nhận trạng thái subscription của cả 2 apps**:
    
    → Cả Joy Loyalty và App Reviews phải ở Paid Plan.
    
3. **Xác minh trạng thái review của customer**:
    
    → Review cần phải **published** (không pending/hidden).
    
4. **Nếu setup đúng + review published mà vẫn không nhận được điểm**:
    
    → **Escalate cho dev team** để kiểm tra bug.
    
    ➔ Khi gửi cho dev, ngoài chi tiết về lỗi cùng với store và chat URL, CS cần cung cấp thêm: **tên app review + plan của app review**
    
5. **Giải thích cho merchant**:
    - Giải thích quy trình tự động cộng điểm.
    
    ![image.png](Customer%20%C4%91%C3%A3%20vi%E1%BA%BFt%20review%20nh%C6%B0ng%20ko%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20%C4%91i%E1%BB%83m/image.png)
    
    - Nếu cần xử lý nhanh, merchant có thể tự **adjust points** cho khách trong mục Customers.
6. CS tiếp tục theo dõi và