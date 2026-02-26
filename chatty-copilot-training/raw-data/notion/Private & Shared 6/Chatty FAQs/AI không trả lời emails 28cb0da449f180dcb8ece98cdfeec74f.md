# AI không trả lời emails

Category: AI Assistant
PIC: Nguyễn Thị Phượng

### **Problem:**

- Sau khi MC connect email forwarding thành công, AI không trả lời emails được forward sang Inbox

---

### **Cause:**

1. AI Assistant chưa được bật (enable) hoặc chưa cho phép phản hồi qua Email Channel. ([https://prnt.sc/RhA-eqC_SbpA](https://prnt.sc/RhA-eqC_SbpA))
2. Nội dung email **không phải là genuine customer inquiry**, ví dụ:
- Email mang tính spam, marketing, hoặc quảng cáo.
- Email là thông báo hệ thống / auto notification.
- Email không liên quan đến hoạt động bán hàng hoặc hỗ trợ của store.

⇒ Các trường hợp này AI sẽ tự **bỏ qua (shouldReply: false)**.

---

### Flow/ Solution:

1. Kiểm tra trạng thái AI Assistant, đảm bảo AI đã được bật và có quyền phản hồi email: Truy cập phần **AI Assistant Settings → AI Channels → Email** để kiểm tra
2. Hiểu logic hoạt động: 
- Khi AI được bật cho Email Channel, AI sẽ tự động phản hồi các email đến sau **5 phút** nếu không có agent nào trả lời.
- AI chỉ phản hồi **(shouldReply: true)** khi email là một yêu cầu thật sự từ khách hàng, liên quan đến việc bán hàng hoặc hỗ trợ trong store **(về sản phẩm, đơn hàng, hoặc chính sách cửa hàng)** và có thể trả lời được dựa trên thông tin của store **(ví dụ: Product info, FAQs, policy, v.v)**
1. Nếu intent đúng mà AI vẫn không trả lời ⇒ báo dev kiểm tra thêm