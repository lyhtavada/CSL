# MC contact vì khi login vào link https://app.meetchatty.com thì nhận được thông báo incorrect email or password

Category: Chatbox

### Problem / Request

Merchant liên hệ vì khi đăng nhập vào link [https://app.meetchatty.com/](https://app.meetchatty.com/) thì nhận được thông báo:

**“Incorrect email or password”**

![image.png](MC%20contact%20v%C3%AC%20khi%20login%20v%C3%A0o%20link%20https%20app%20meetcha/image.png)

---

### Causes

- Thông thường, khi một agent được invite làm team member trong store Chatty, họ sẽ nhận được email mời. Khi click vào nút **"Create account"**, họ sẽ được dẫn tới [https://app.meetchatty.com](https://app.meetchatty.com/) để tạo tài khoản.

![image.png](MC%20contact%20v%C3%AC%20khi%20login%20v%C3%A0o%20link%20https%20app%20meetcha/image%201.png)

- Tại màn hình tạo tài khoản, có **2 lựa chọn**:
    1. **Create account**: Agent sẽ tự nhập mật khẩu → sau này phải dùng chính mật khẩu đó để đăng nhập.
    2. **Sign up with Google**: Không cần tạo mật khẩu, hệ thống sẽ tự kết nối tài khoản qua email → mỗi lần đăng nhập cần dùng đúng email & mật khẩu email.
    
    ![image.png](MC%20contact%20v%C3%AC%20khi%20login%20v%C3%A0o%20link%20https%20app%20meetcha/image%202.png)
    

---

### Flow

1. Hỏi lại merchant/agent xem **lúc tạo tài khoản**, họ đã:
    - **Tự tạo mật khẩu**, hay
    - **Dùng “Sign up with Google”**
2. Xử lý theo từng trường hợp:
    - **Nếu chọn “Create account”**:
        
        → Họ cần đăng nhập bằng email + mật khẩu đã tạo.
        
        → Nếu quên mật khẩu → hướng dẫn nhấn **"Forgot password"** để đặt lại.
        
        ![image.png](MC%20contact%20v%C3%AC%20khi%20login%20v%C3%A0o%20link%20https%20app%20meetcha/image%203.png)
        
    - **Nếu chọn “Sign up with Google”**:
        
        → Hướng dẫn đăng nhập lại bằng cách click “Sign in with Google” và dùng đúng tài khoản Gmail trước đó.