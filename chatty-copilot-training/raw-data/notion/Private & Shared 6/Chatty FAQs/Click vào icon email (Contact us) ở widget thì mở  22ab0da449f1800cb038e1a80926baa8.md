# Click vào icon email (Contact us) ở widget thì mở ra blank page

Category: Chatbox
PIC: Đỗ Minh Quân

## Vấn đề

Khi nhấn vào Email contact button (có link dạng `mailto:email@example.com`) trên widget, thay vì mở ứng dụng gửi mail (như Gmail, Outlook, Mail...), trình duyệt lại mở ra một tab trắng (blank) và không thực hiện hành động nào.

![image.png](Click%20v%C3%A0o%20icon%20email%20(Contact%20us)%20%E1%BB%9F%20widget%20th%C3%AC%20m%E1%BB%9F%20/image.png)

---

## Nguyên nhân

- Trình duyệt chưa được cấu hình để xử lý mailto links
- Không có ứng dụng email mặc định trong hệ điều hành
- Trình duyệt chặn hoặc không hỗ trợ mở ứng dụng
- Có tiện ích (extension) can thiệp hoặc ngăn chặn redirect
- Truy cập Gmail nhưng chưa cấp quyền xử lý mailto

---

## Cách xử lý theo từng trình duyệt

### 1️⃣ Google Chrome, Brave, Opera, Cốc Cốc (và các Chromium browser khác)

1. **Cho phép trang web xử lý giao thức mailto**
- Truy cập:
    - Chrome: `chrome://settings/handlers`
    - Brave: `brave://settings/handlers`
    - Opera: `opera://settings/handlers`
    - Cốc Cốc: `coccoc://settings/handlers`
- Bật tùy chọn: **“Sites can ask to handle protocols”**
1. **Cho Gmail xử lý mailto (hoặc app khác)**
- Truy cập [https://mail.google.com](https://mail.google.com/)
- Khi đang ở Gmail, kiểm tra góc phải thanh địa chỉ xem có biểu tượng **hai hình thoi lồng vào nhau**
- Nhấn vào → chọn **Cho phép Gmail mở các liên kết email (Allow)** → **Done**

![image.png](Click%20v%C3%A0o%20icon%20email%20(Contact%20us)%20%E1%BB%9F%20widget%20th%C3%AC%20m%E1%BB%9F%20/image%201.png)

<aside>
💡

**Nếu không thấy biểu tượng:**

- Kiểm tra lại **Protocol handlers** của trình duyệt xem đã có email chưa: [https://prnt.sc/YJ9gq05iYAsy](https://prnt.sc/YJ9gq05iYAsy)
- Reload lại Gmail hoặc thử mở trong tab ẩn danh
</aside>

### 2️⃣ Firefox

1. Mở Firefox → menu ≡ → Settings
2. Vào mục General → cuộn xuống phần Applications
3. Tìm dòng mailto
4. Trong cột Action, chọn:
    - Use Gmail
    - Use Microsoft Outlook
    - Hoặc chọn Always ask nếu muốn được hỏi mỗi lần

![image.png](Click%20v%C3%A0o%20icon%20email%20(Contact%20us)%20%E1%BB%9F%20widget%20th%C3%AC%20m%E1%BB%9F%20/image%202.png)

### 3️⃣ Safari (macOS)

Safari không tự xử lý mailto link qua Gmail, bắt buộc phải đặt ứng dụng email mặc định trên hệ điều hành:

1. Mở ứng dụng Mail.app
2. Vào Mail **→** Preferences **→** General
3. Trong dòng Default email reader, chọn:
    - Mail.app, Outlook,...
    - (Không hỗ trợ mở trực tiếp Gmail trừ khi có app hỗ trợ riêng)

![image.png](Click%20v%C3%A0o%20icon%20email%20(Contact%20us)%20%E1%BB%9F%20widget%20th%C3%AC%20m%E1%BB%9F%20/image%203.png)

### 4️⃣ Cài đặt mặc định hệ điều hành (Windows/macOS)

Nếu muốn dùng ứng dụng như Outlook, Thunderbird thay vì Gmail:

- **Windows:**
    1. Vào Settings **→** Apps **→** Default apps
    2. Nhập mailto → chọn ứng dụng mong muốn

![image.png](Click%20v%C3%A0o%20icon%20email%20(Contact%20us)%20%E1%BB%9F%20widget%20th%C3%AC%20m%E1%BB%9F%20/image%204.png)

- **macOS:**
    1. Mở Mail.app
    2. Vào Preferences **→** General
    3. Đặt Default email reader phù hợp

![image.png](Click%20v%C3%A0o%20icon%20email%20(Contact%20us)%20%E1%BB%9F%20widget%20th%C3%AC%20m%E1%BB%9F%20/image%203.png)