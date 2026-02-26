# AI suggest sai domain (product URL) khi khách truy cập market

Category: AI Assistant
PIC: Ly Hoàng
Type: Feature request

### Mô tả issue chung

Khi khách hàng truy cập website theo domain market (ví dụ: `abc.fr`), AI assistant trong website vẫn suggest sản phẩm với link từ **main domain** (ví dụ: `abc.com`). Điều này dẫn đến tình trạng khách truy cập đúng market domain nhưng khi click vào link sản phẩm được gợi ý lại bị điều hướng sang domain khác.

Hậu quả:

- Giá, chính sách bán hàng hoặc nội dung trên main domain có thể khác với market domain mà khách đang ở.
- Gây hiểu nhầm, trải nghiệm không nhất quán và rủi ro không tuân thủ về hiển thị giá/thuế theo quốc gia.
    
    **Ví dụ**
    
    - Khách đang truy cập **`mondepetit.fr` (France)**, dùng browser French + VPN French, hỏi AI về sản phẩm.
    - AI gợi ý sản phẩm nhưng link trả về lại là từ **`mondepetit.com` (Spain)**.
    - Do đó, khách thấy giá và chính sách theo market Spain, trong khi đúng ra AI phải suggest link thuộc domain France (`mondepetit.fr`).

---

### **Giới hạn hiện tại:**

- App mới chỉ lưu dữ liệu sản phẩm ứng với **1 domain chính**.
- Chưa hỗ trợ multi-domain theo market.

---

### **Kế hoạch fix:**

- Trong roadmap tháng tới: dùng **Storefront API** để lấy product theo ID + locale → trả về link với domain đúng market hiện tại.

---

### Flow

1. **Xác nhận bối cảnh khách:**
    - Domain truy cập (`.fr`, `.de`…), AI trả về link product ở URL khác.
2. **Kiểm tra Shopify Markets:**
    - Country có nằm trong Market setup chưa.
    - Domain mapping đã gắn đúng chưa.
    - Shortcut **`!ask-market`**:
        
        > Could you please confirm if [Country name] has been added under your Markets in Shopify Admin, and that the domain [market domain] is mapped there? A quick screenshot of your Markets settings would also be helpful.
        > 
3. **CS tự test lại issue**
    - Vào đúng domain market mà khách báo (ví dụ `mondepetit.fr`).
    - Hỏi AI cùng câu hỏi của khách.
    - Kiểm tra link AI trả về có bị `.com` thay vì `.fr` không.
    - Chụp màn hình lưu lại làm bằng chứng.
4. Thông báo cho merchant, **dùng** shortcut **`!AI-suggest-wrong-market-link`**
    - Đây là hạn chế kỹ thuật hiện tại, không phải lỗi cấu hình.
    - Đã có kế hoạch fix trong tháng tới.
5. **CS tạo card.**
6. **CS chủ động fu để cập nhật tiến độ cho MC.**