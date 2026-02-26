# Email notifcations của app bị vào spam box

Category: Notifications

## Possible causes

Một số lý do thường gặp:

- MC mới bắt đầu dùng app, provider mail (Gmail, Outlook…) chưa “quen” địa chỉ gửi của Chatty nên auto cho vào spam.
- Nội dung email có những từ/format dễ bị bộ lọc spam đánh dấu (nhiều link, nhiều hình, chữ ít).
- MC hoặc ai đó lỡ tay bấm “Report spam” trước đó, nên các email sau tự vào spam.
- Tần suất gửi email tới inbox đó nhiều trong thời gian ngắn (nhiều notify, nhiều transcript).
- Domain gửi là shared domain của hệ thống (không phải domain riêng của MC) nên độ trust chưa cao với mailbox của họ.

---

### Flow gợi ý

1. **Hướng dẫn MC “dạy” mailbox không coi đó là spam**

Gợi ý MC làm các bước sau:

- Mở email trong spam box.
- Bấm “Not spam” hoặc “Report as not spam”.
- Thêm địa chỉ gửi (sender của Chatty) vào contact / safe sender list.
1. **Theo dõi thêm**
- Giải thích là việc học của bộ lọc spam cần vài lần tương tác, nên sau khi làm các bước trên, bảo MC theo dõi thêm 1–2 ngày.
- Nếu vẫn bị spam thường xuyên, báo lại để team check log / gửi cho dev nếu cần.

Câu trả lời mẫu:

<aside>

In most cases, this happens because the email provider has not fully recognized our sender address yet, or the messages were previously marked as spam. To help fix this, could you please try the steps below:

- Open one of the Chatty notification emails in your Spam/Junk folder.
- Click “Not spam” (or a similar option) to move it back to your inbox.
- Add the sender address to your contacts or safe sender list.

After doing this, your email provider should start delivering future notifications directly to the inbox. If you still see new notifications going to spam after this, please let me know which email address you are using to receive them and I’ll be happy to check further with our team.

</aside>