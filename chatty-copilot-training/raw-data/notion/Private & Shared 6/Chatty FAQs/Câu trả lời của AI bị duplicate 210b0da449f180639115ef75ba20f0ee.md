# Câu trả lời của AI bị duplicate

Category: AI Assistant

## **Problem/ Request**

Trong quá trình sử dụng live chat, **AI tự động trả lời cùng một nội dung 2 lần hoặc lặp lại nội dung tương tự**, gây trải nghiệm không tự nhiên cho người dùng.

![image.png](C%C3%A2u%20tr%E1%BA%A3%20l%E1%BB%9Di%20c%E1%BB%A7a%20AI%20b%E1%BB%8B%20duplicate/image.png)

---

## **Causes**

1. **Người dùng gửi cùng một câu hỏi nhiều lần** (do bấm gửi lại hoặc mạng lag), hệ thống hiểu là yêu cầu mới nên AI phản hồi lặp.
2. **AI không nhận biết rõ trạng thái cuộc trò chuyện**, dẫn đến xử lý lại prompt cũ thay vì tạo phản hồi mới.
3. **Mạng chậm hoặc không ổn định**, gây delay hoặc gửi trùng tín hiệu về server khiến AI phản hồi lại.
4. **Lỗi xử lý tạm thời từ phía hệ thống AI**, dẫn đến việc generate cùng một nội dung hai lần.

---

## **Flow**

1. CS xin thông tin chat đó (chat ID hoặc tên của customer) và kiểm tra lại nội dung convo:
    - Xác định xem có phải người dùng gửi lặp hay lỗi từ hệ thống.
    - Ghi nhận thời điểm và nội dung 2 câu trả lời giống nhau.
2. Nếu **nghi ngờ lỗi hệ thống**, CS tạo card cho TS kiểm tra:
    - Gửi link đoạn hội thoại + thời điểm + tên merchant.
3. Giải thích tạm thời cho merchant:
    - Xin lỗi vì trải nghiệm không mượt và thông báo team đang kiểm tra.
    - Gợi ý merchant có thể **bấm “refresh chat”** hoặc **chuyển sang manual chat** nếu gặp lặp lại liên tục.
4. Theo dõi và cập nhật cho merchant khi có phản hồi từ team kỹ thuật.