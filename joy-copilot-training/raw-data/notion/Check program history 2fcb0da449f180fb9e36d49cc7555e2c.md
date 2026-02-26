# Check program history

Category: Reward programs
PIC: Đỗ Minh Quân

## Mục đích của guide

Giúp CS/TS **xác minh lịch sử thay đổi của một program** (hiện tại hoặc trong quá khứ), từ đó:

- Làm rõ vì sao program **work không đúng như kỳ vọng**
- Kiểm tra xem **logic/condition đã từng được chỉnh sửa hay chưa**
- Có dữ liệu cụ thể để **giải thích lại cho MC**, thay vì phải escalate lên dev

## 1. Problem

Trong quá trình support, thường gặp các case:

- Program hiện tại **không chạy đúng** (earning sai, redeem không apply, milestone không trigger, v.v.)
- MC khẳng định:
    - *“Bên tôi chưa từng thay đổi program”*
    - hoặc *“Không nhớ trước đây đã set điều kiện như thế nào”*
- CS/TS **không có dữ liệu lịch sử**, nên trước đây buộc phải:
    - Báo dev check log
    - Chờ phản hồi, mất thời gian cho cả MC và team

## 2. Solution

Hiện tại, trong **Dev Zone** đã có tính năng **Program History**, cho phép CS/TS:

- Chủ động kiểm tra **toàn bộ lịch sử thay đổi của một program**
- Biết được:
    - Program được **create / update khi nào**
    - **Field nào đã bị thay đổi**
    - Giá trị **trước và sau** của từng lần chỉnh sửa

⇒ Nhờ đó, các issue dạng “program từng set khác nhưng MC không nhớ” có thể được xử lý **nhanh và minh bạch hơn**, không cần đợi dev.

![image.png](Check%20program%20history/image.png)

## 3. Supported Programs

Tính năng **Program History** hỗ trợ **tất cả program có thể phân biệt bằng Program ID**, bao gồm:

- Earning programs
- Redeeming programs
- Perks
- Exclusive deals
- Milestones
- Và các program khác có Program ID

## 4. Steps: Cách check Program History

### Step 1: Lấy Program ID

CS/TS có thể lấy Program ID bằng một trong các cách:

- Từ **URL** khi mở chi tiết program trong admin
    
    ![image.png](Check%20program%20history/image%201.png)
    
- Từ **Network tab** (DevTools) khi load hoặc update program
    
    ![image.png](Check%20program%20history/image%202.png)
    

### Step 2: Truy cập Program History trong Dev Zone

Có 2 cách:

- Truy cập trực tiếp đường dẫn: `/dev_zone/program_history`
    
    ![image.png](Check%20program%20history/image%203.png)
    
- Hoặc vào Dev Zone và **search keyword “Program History”**
    
    ![image.png](Check%20program%20history/image%204.png)
    

---

### Step 3: Tìm kiếm theo Program ID

- Nhập **Program ID** vào ô search
- Nhấn **Search**

Hệ thống sẽ trả về toàn bộ lịch sử thay đổi của program tương ứng.

![image.png](Check%20program%20history/image%205.png)

### Step 4: Đọc và phân tích dữ liệu trả về

### 4.1. Thứ tự hiển thị

- History log được hiển thị **từ mới → cũ**
- Dòng trên cùng là **thay đổi gần nhất**

### 4.2. Các cột thông tin chính

- **Timestamp**: Thời điểm thay đổi
- **Operation**:
    - `CREATE` – tạo program
    - `UPDATE` – cập nhật program
- **Fields changed**: Danh sách các field đã bị thay đổi trong lần đó

### 4.3. Sử dụng Filter

- Có thể filter theo **field cụ thể**
- Phù hợp khi cần:
    - Track xem **field này bị thay đổi từ khi nào**
    - Giá trị **đã đổi như thế nào qua từng lần update**

![image.png](Check%20program%20history/image%206.png)

### 4.4. Xem chi tiết từng activity

- Click vào **icon hình con mắt** bên trái mỗi dòng
- Dùng để kiểm tra **changed details**:
    - Giá trị cũ
    - Giá trị mới
    - Context của lần thay đổi đó

![image.png](Check%20program%20history/image%207.png)

![image.png](Check%20program%20history/image%208.png)