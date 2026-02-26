# Disable/ enable AI follow-up questions

Category: AI Assistant

## 1. Issue KH đang gặp là gì?

- KH phản hồi rằng:
    - Không muốn AI hỏi thêm các câu follow-up.
    - Không muốn AI lan man hoặc gợi ý thêm sản phẩm/dịch vụ không liên quan.
    
    ![image.png](Disable%20enable%20AI%20follow-up%20questions/image.png)
    
- KH chỉ muốn:
    - AI trả lời **đúng và trực tiếp** câu hỏi ban đầu của họ.

<aside>

**Lưu ý:** CS/TS có thể nhầm lẫn tính năng này với AI assistant skills: Follow up questions. Nhưng đây là 2 tính năng hoàn toàn khác nhau.

</aside>

---

## 2. Nguyên nhân vì sao AI lại hỏi thêm?

- Mặc định:
    - AI được thiết kế để:
        - Clarify thêm context.
        - Đề xuất thêm giải pháp hoặc sản phẩm liên quan.
- Tuy nhiên:
    - Với một số KH, hành vi này bị xem là:
        - Không cần thiết.
        - Gây khó chịu.
        - Không đúng expectation khi chỉ cần câu trả lời ngắn, đúng trọng tâm.

---

## 3. Flow xử lý cho CS

### Bước 1: Xác nhận lại nhu cầu KH

CS cần confirm:

- KH muốn AI:
    - Chỉ trả lời đúng câu hỏi.
    - Không hỏi thêm bất kỳ follow-up nào.
    
    > *I understand. If you prefer the AI to only answer your question directly without any follow-up or suggestions, we do support that behavior.*
    > 

---

### Bước 2: CS tắt tính năng trong Devzone

![image.png](Disable%20enable%20AI%20follow-up%20questions/image%201.png)

---

### Bước 3: Giải thích impact sau khi tắt

CS cần nói rõ:

- Sau khi tắt:
    - AI sẽ không hỏi thêm để làm rõ ngữ cảnh.
    - Câu trả lời có thể:
        - Ngắn hơn.
        - Ít cá nhân hóa hơn.
- Đây là hành vi mong muốn theo yêu cầu của KH, không phải bug.

> *Once this option is enabled, the AI won’t ask for additional clarification or suggest related content. It will focus strictly on answering what was asked.*
> 

---

### Bước 4: Follow up xác nhận

- Nhờ KH test lại.
- Xác nhận AI đã trả lời đúng expectation.

> *Could you please help test again and let me know if the AI response now matches your expectation?*
>