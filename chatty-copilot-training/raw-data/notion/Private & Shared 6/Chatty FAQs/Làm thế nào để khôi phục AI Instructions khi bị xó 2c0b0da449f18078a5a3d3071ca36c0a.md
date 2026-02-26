# Làm thế nào để khôi phục AI Instructions khi bị xóa nhầm?

Category: AI Assistant

## Problem

Merchant vô tình xóa toàn bộ **AI Instructions** trong Chatty và không còn bản sao để khôi phục.

---

## **Giải pháp khôi phục nhanh nhất**

### **Cách đơn giản nhất: Lấy lại từ Trace Logs**

Chatty luôn lưu AI Instructions được sử dụng tại thời điểm AI trả lời. Vì vậy, mọi convo cũ đều chứa bản **AI Instruction** mà hệ thống đã dùng.

### **Các bước thực hiện:**

1. **Vào Dashboard → Tools → [Trace Logs](https://platform.openai.com/logs?api=traces)**
2. **Tìm một cuộc hội thoại cũ** của store đó (thời điểm AI còn hoạt động bình thường).
3. Mở chi tiết trace → tìm AI Instruction trước khi bị xóa trong các agent: Response/ Retrieval

VD: dưới đây là 1 instuction version trong Retrieval agent của 1 store

![image.png](L%C3%A0m%20th%E1%BA%BF%20n%C3%A0o%20%C4%91%E1%BB%83%20kh%C3%B4i%20ph%E1%BB%A5c%20AI%20Instructions%20khi%20b%E1%BB%8B%20x%C3%B3/image.png)

1. Copy toàn bộ nội dung và **paste lại vào mục AI Instructions** trong Chatty.

---

# **Lưu ý quan trọng**

- Nên chọn một convo có ngày gần nhất *trước lúc bị xóa* để đảm bảo instructions phù hợp.
- Nếu store dùng multi-language, hãy kiểm tra đúng trace của ngôn ngữ tương ứng.
- Sau khi khôi phục, merchant có thể review lại để chỉnh sửa theo nhu cầu.