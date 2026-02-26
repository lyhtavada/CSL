# AI trả lời sai câu hỏi của customer

Category: AI Assistant

### Problem

AI trả lời sai câu hỏi của customer (hoặc trong quá trình merchant đang test, AI trả lời không đúng nội dung mong muốn).

---

### Causes

- AI lấy thông tin từ nguồn (sources) chưa chính xác hoặc chưa phù hợp với câu hỏi.
- Câu hỏi của KH nằm ngoài phạm vi các câu trả lời có sẵn trong nguồn.
- Merchant chưa cung cấp đủ tài liệu hoặc chưa thiết lập đúng thông tin trong mục nguồn trả lời (Knowledge Base/ FAQ).
- Đôi khi câu hỏi của KH không rõ ràng, gây nhầm lẫn trong việc hiểu ý định.
- **Instruction (hướng dẫn cho AI)** chưa phù hợp → khiến AI hiểu sai ngữ cảnh.

<aside>
💡

Câu trả lời của AI dựa trên các yếu tố: 
**1. Instruction** 

- App instruction: mặc định của app mình
- Store instruction: do merchant thêm (gồm cả custom instruction và scenario instruction)

**2. Data source:** Khi review source có thể xem

- Các loại data source
- Scenario instruction
</aside>

---

## CS hỗ trợ theo 2 TH chính:

### 1️⃣ MC đang trong giai đoạn Test, chưa go live:

- Truy cập **Dev Zone** để xem lại lịch sử test: [Dev Zone](https://prnt.sc/zO2UGXkHjJMK)

![image.png](AI%20tr%E1%BA%A3%20l%E1%BB%9Di%20sai%20c%C3%A2u%20h%E1%BB%8Fi%20c%E1%BB%A7a%20customer/image.png)

- Tại đây, bạn có thể xem danh sách conversation test của khách, click View tại mỗi conversation để mở conversation đó trên trang Test của app. Sau đó:
    - Xem toàn bộ **context của cuộc hội thoại**
    - Kiểm tra **nguồn dữ liệu (source)** mà AI sử dụng để tạo câu trả lời → giúp xác định nguyên nhân AI trả lời sai
    - Kiểm tra các **Instruction** đang được áp dụng:
        - **App instruction**: instruction mặc định của app
        - **Store instruction**: do merchant thiết lập (gồm cả **custom** và **scenario instruction**)

<aside>
⚠️

- **Phải mở app Chatty từ CRM trước** → để hệ thống lưu cookie và đăng nhập vào đúng tài khoản store merchant
- Sau đó mới mở lại **Dev Zone** để xem được các cuộc hội thoại test từ đúng store
</aside>

### 2️⃣ AI chatbot trả lời sai ở live chat:

- CS xin chat link/ chat ID của convo mà AI trả lời sai.
- CS vào convo > Click Review Sources dưới mỗi câu trả lời của AI

![image.png](AI%20tr%E1%BA%A3%20l%E1%BB%9Di%20sai%20c%C3%A2u%20h%E1%BB%8Fi%20c%E1%BB%A7a%20customer/image%201.png)

- CS cần review kỹ:
    - Các loại Data source mà AI dùng để trả lời
    - Scenario Instruction nếu có
    - Custom Instruction trong store setting

![image.png](AI%20tr%E1%BA%A3%20l%E1%BB%9Di%20sai%20c%C3%A2u%20h%E1%BB%8Fi%20c%E1%BB%A7a%20customer/image%202.png)

### Sau khi đã có đủ thông tin về nội dung chat và các source/ instruction của AI, CS xử lý tiếp theo 3 TH chính sau:

**a. AI trả lời sai do source chưa đúng hoặc chưa đủ thông tin:**

- CS giải thích cho merchant rằng câu trả lời sai là do nội dung trong nguồn chưa chính xác, chưa đủ rõ ràng hoặc thiếu.
- Đề xuất merchant cập nhật hoặc chỉnh sửa lại nội dung trong source để đảm bảo AI có đủ dữ liệu để trả lời đúng.
- CS có thể hỗ trợ merchant chỉnh sửa nếu cần, hoặc gửi hướng dẫn chi tiết (kèm video/nghiệp vụ nếu có).

**b. AI trả lời sai dù source đã đúng – do AI suy diễn hoặc hiểu sai câu hỏi:**

- CS xác nhận lại rằng nội dung trong source là chính xác, nhưng AI hiểu sai ngữ cảnh hoặc trả lời ngoài phạm vi.
- CS gửi báo cáo lại cho team dev để kiểm tra cách AI xử lý câu hỏi đó.
- Trong thời gian chờ xử lý, CS có thể đề xuất merchant thử:
    - Viết lại câu hỏi theo hướng cụ thể, rõ ràng hơn
    - Thêm tài liệu hướng dẫn chi tiết hơn để AI có thêm dữ liệu học tập.
- Ghi chú kỹ vào ticket để theo dõi tình trạng và cập nhật khi có phản hồi từ dev.

**c.  AI trả lời sai do Instruction không phù hợp**

CS cần thực hiện thêm các bước:

1. **Review lại Instruction của merchant**, gồm:
    - App Instruction
    - Custom Instruction
    - Scenario Instruction
2. **Tìm nguyên nhân** → có phần nào gây hiểu sai, chưa định hướng đúng hành vi trả lời của AI?
3. **Đề xuất chỉnh sửa Instruction**, rồi test lại:
    - Nếu AI trả lời **đúng** sau khi chỉnh: revert lại bản cũ và gửi recommendation bản mới cho merchant
    - Nếu AI vẫn trả lời **sai**: báo lên nhóm để team product/dev kiểm tra App Instruction hoặc logic xử lý

**CS tiếp tục follow-up với merchant** sau khi có hướng xử lý hoặc sau khi dev phản hồi để đảm bảo merchant hài lòng với kết quả.