# AI trả lời sai thông tin (price, inventory…) của sản phẩm

Category: AI Assistant

### 🔸Problem**:**

Merchant phản ánh rằng AI chatbot đã cung cấp sai thông tin về giá cả, khuyến mãi hoặc chi tiết sản phẩm cho khách hàng.

---

### 🔸**Cause:**

- Dữ liệu training hoặc kết nối chưa được cập nhật đầy đủ, gây nhầm lẫn cho AI.
- Sản phẩm có thay đổi giá gần đây nhưng hệ thống chưa đồng bộ.
- Cách đặt câu hỏi khiến AI hiểu sai ngữ cảnh hoặc logic sản phẩm.

---

### 🔸**Flow:**

1. **CS xác nhận lại nội dung trả lời sai**
    - Xin merchant cung cấp đoạn chat cụ thể có lỗi (screenshot hoặc đoạn chat copy).
    - Xác minh rõ: sản phẩm nào, thông tin nào sai (giá, mô tả, ưu đãi,...).
2. **CS kiểm tra tình trạng sync của sản phẩm**
    - Kiểm tra xem sản phẩm đó đã được sync vào hệ thống AI chưa.
    - Xác định lần sync gần nhất là khi nào.
    - Nếu thông tin chưa được sync gần đây hoặc nghi ngờ sai lệch, có thể **đề xuất merchant sync lại sản phẩm đó** (nêu rõ hướng dẫn sync nếu cần).
    
    ![image.png](AI%20tr%E1%BA%A3%20l%E1%BB%9Di%20sai%20th%C3%B4ng%20tin%20(price,%20inventory%E2%80%A6)%20c%E1%BB%A7a%20s/image.png)
    
    ![image.png](AI%20tr%E1%BA%A3%20l%E1%BB%9Di%20sai%20th%C3%B4ng%20tin%20(price,%20inventory%E2%80%A6)%20c%E1%BB%A7a%20s/image%201.png)
    
    - Sau khi sync, kiểm tra lại câu trả lời của AI:
        - Nếu **AI trả lời đúng sau khi sync**, CS cần **giải thích lại cho merchant về nguyên nhân gây ra lỗi** (do sản phẩm chưa được đồng bộ dữ liệu đầy đủ vào AI).
        - Gợi ý merchant thường xuyên sync lại sản phẩm sau khi cập nhật nội dung/giá để tránh lỗi tương tự.
3. **Nếu dữ liệu đã đúng mà AI vẫn trả lời sai**
    - CS xác minh:
        - Sản phẩm đã được sync đúng cách.
        - Thông tin hiển thị trong hệ thống đầy đủ và chính xác.
    - Nếu xác nhận dữ liệu huấn luyện là đúng → **CS tạo card và forward issue cho team dev/AI** để xử lý logic của AI.
4. **Follow up**
    - Theo dõi tiến độ xử lý từ team dev/AI.
    - Thông báo lại cho merchant khi AI đã được fix hoặc cập nhật xong.
    - Confirm lại rằng AI đang trả lời đúng sau cập nhật.

---

### ⚠️ **Lưu ý:**

- CS không được tự chỉnh sửa hệ thống AI hoặc tự xử lý dữ liệu mà không rõ nguyên nhân gốc.
- Luôn kiểm tra tình trạng sync trước khi kết luận lỗi do AI.
- Nếu lỗi ảnh hưởng lớn đến trải nghiệm người dùng cuối, cân nhắc escalate và trao đổi thêm với PM nếu cần.