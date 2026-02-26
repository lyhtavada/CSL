# Hide product preview card ở chat page

Category: AI Assistant

![image.png](Hide%20product%20preview%20card%20%E1%BB%9F%20chat%20page/image.png)

Product preview card là thẻ hiển thị sản phẩm (tên, giá, icon add to cart) được AI Assistant tự động gợi ý trong quá trình chat nhằm hỗ trợ bán hàng và tăng khả năng chuyển đổi.

Một số lý do MC muốn remove card trên:

- MC không muốn AI gợi ý sản phẩm tự động
- Giao diện chat bị “rối” hoặc không phù hợp branding
- MC chỉ muốn dùng chat cho support, không cho sales

Hiện tại app chưa có setting riêng để tắt hoặc ẩn feature này. Về mặt kỹ thuật, có thể hide bằng CSS, nhưng phần preview này đang dùng chung class với phần tin nhắn Reply to, nên sẽ ẩn cả 2 nếu dùng CSS:

![image.png](Hide%20product%20preview%20card%20%E1%BB%9F%20chat%20page/image%201.png)

### Flow

Khi nhận được yêu cầu, CS cần **giải thích rõ cho merchant** rằng product preview card được thiết kế để hỗ trợ bán hàng. Sau đó, CS **chủ động hỏi thêm lý do** merchant muốn remove, ví dụ do giao diện, trải nghiệm chat, hay vì chỉ dùng chat cho support.

Dựa trên lý do cụ thể, CS sẽ **định hướng solution phù hợp**:

- Nếu merchant không muốn AI bán hàng, CS có thể gợi ý điều chỉnh lại cách dùng AI hoặc tập trung vào các skill support.
- Nếu merchant lo giao diện rối, CS giải thích impact của việc hide bằng CSS và vì sao không khuyến khích.
- Nếu merchant cần kiểm soát rõ ràng hơn, CS ghi nhận feedback và escalate lên team product để xem xét giải pháp lâu dài.

Mục tiêu của flow này là giúp merchant hiểu đúng bản chất tính năng, tránh workaround rủi ro, và đảm bảo giải pháp đưa ra phù hợp với nhu cầu thực tế của từng merchant.