# Follow-up Merchant Feedback (#chatty-notice)

## When to Use
Khi bot tag bạn trong thread ở channel #chatty-notice — nghĩa là có merchant vừa feedback về AI reply của Chatty và bạn cần follow-up.

## Who
- **CS Agent (Chatty):** Thực hiện follow-up
- **CS Leader (Liz):** Escalation nếu feedback nghiêm trọng hoặc CS không phản hồi

## Channel #chatty-notice là gì?

Channel này lưu từng feedback riêng lẻ mà merchant gửi về mỗi câu trả lời của AI trong conversation. Khi merchant rate (👍/👎) một AI reply, hệ thống tự động gửi message vào channel theo template sau:

```
Bot Message Feedback

Shop ID: [shop_id]                    Shop Domain: [domain.myshopify.com]
Shop Email: [email]

Conversation ID: [id hoặc N/A]       Message ID: [message_id]

Feedback Type: positive / negative    Reason: [lý do hoặc N/A]

Bot Message:
[Nội dung AI đã trả lời cho merchant]

Customer Feedback:
[Comment của merchant về câu trả lời, nếu có]
```

## Flow xử lý

### 1. Bot tag CS đang trực
Khi có feedback mới, Avada Bot tự detect CS Chatty đang trong ca trực và tag trực tiếp vào thread đó.

- **Lần 1:** Bot tag CS đang trực
- **Lần 2** (sau 15 phút nếu CS chưa reply): Bot nhắc lại
- **Sau lần 2:** Bot dừng — nếu CS vẫn chưa xử lý, Liz sẽ xử lý

### 2. CS đọc và phân loại feedback

Mở thread mà bot vừa tag, đọc nội dung feedback và xác định:

| Thông tin | Lấy từ đâu |
|-----------|------------|
| Store nào? | Shop Domain / Shop Email |
| Feedback loại gì? | Feedback Type: positive / negative |
| AI trả lời gì? | Bot Message |
| KH nói gì? | Customer Feedback |
| Có conversation ID không? | Conversation ID (có thể N/A) |

### 3. Phân loại và quyết định action

| Loại feedback | Action |
|---------------|--------|
| 👍 Positive, không có comment đặc biệt | Reply thread: "Noted ✅" — không cần chat KH |
| 👎 Negative + AI trả lời sai info | Tìm conversation → chat follow-up với KH → log action |
| 👎 Negative + comment mơ hồ / không rõ issue | Tìm conversation → chat hỏi thêm KH → log action |
| 👎 Negative + issue nghiêm trọng (sai giá, sai product, sai policy) | Tìm conversation → fix ngay → log action → báo Liz |
| Feedback liên quan đến bug | Log action → tạo Trello card cho TS |

### 4. Tìm conversation và follow-up với merchant
- Dùng **Shop Domain** hoặc **email address của store** để tìm conversation trên Crisp, nếu chưa có conversation trước đó, CS tự tạo chat mới.
- Follow-up với KH: clarify thông tin sai, hỏi thêm chi tiết, hoặc hỗ trợ tiếp

### 5. Log action vào thread #chatty-notice

Sau khi follow-up xong, reply vào thread bot đã tag với format:

```
Link: [Crisp conversation URL]
Action: [mô tả ngắn việc đã làm]
```

Ví dụ:
```
Link: https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f66943bd-4e7e-464d-914a-16a170cbc1d4/
Action: AI trả lời sai shipping policy, đã correct và gửi info đúng cho KH
```

```
Noted ✅ — positive feedback, không cần follow-up
```

### 6. Decision points — khi nào escalate?

- **AI liên tục trả lời sai cùng 1 topic** → báo Liz để review AI training data
- **Merchant rất angry / đe dọa review xấu** → escalate Liz ngay (xem [escalation-matrix.md](../shared-cs-process/escalation-matrix.md))
- **Phát hiện bug (AI gửi sai link, sai giá, sai product)** → tạo Trello card cho TS, báo Liz
- **Không tìm được conversation / không có cách liên hệ KH** → ghi note trong thread, báo Liz

## Timeline

| Event | Deadline |
|-------|----------|
| Bot tag lần 1 | Reply trong 15 phút |
| Bot nhắc lần 2 | Reply ngay |
| Follow-up với KH | Trong ca trực hiện tại |
| Log action vào thread | Ngay sau khi follow-up xong |

## Notes

- **Không bỏ qua thread** — mỗi feedback đều cần ít nhất 1 reply (kể cả positive chỉ cần "Noted ✅")
- **"Customer Data Request"** trong channel → bot tự skip, bạn cũng skip — không cần action
- **Feedback ngoài giờ trực** → ca sau sẽ được bot tag, không cần lo
- **Nhiều CS cùng được tag** (overlap ca) → ai thấy trước reply trước, người còn lại không cần duplicate
