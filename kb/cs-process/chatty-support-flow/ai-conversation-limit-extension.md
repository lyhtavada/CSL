# AI Conversation Limit Extension

## When to Use
Khi merchant yêu cầu tăng AI conversation limit vì đã chạm giới hạn plan hiện tại.

## Who
- **CS Agent:** Thu thập thông tin, kiểm tra upgrade, escalate
- **PM (qua #sale-cs-success):** Duyệt extension request

## Notes
- AI conversation bonus là **lifetime allocation**, không phải monthly reset
- Luôn kiểm tra upgrade có giải quyết được không trước khi escalate

## Flow

### 1. Thu thập thông tin

Trước khi escalate, collect:
- Store URL
- Plan hiện tại (Free / Basic / Pro / Plus)
- Average chat volume per month (hỏi MC hoặc check analytics)
- Plan MC đang cân nhắc upgrade lên (nếu có)
- Lý do cần thêm conversations

### 2. Kiểm tra upgrade trước

Nếu MC đang ở plan thấp và plan tiếp theo cover đủ volume → khuyến khích upgrade trước. Manual extension chỉ dùng khi upgrade không đủ hoặc MC cần bridge tạm thời.

### 3. Escalate lên #sale-cs-success

Post vào **#sale-cs-success**, tag PM với đầy đủ:
- Store URL + plan hiện tại
- Monthly chat volume (estimated)
- Plan MC đang cân nhắc / lý do cần thêm
- Số conversations cần extend (nếu MC đã nêu cụ thể)

**Chờ approval trước khi thực hiện bất kỳ thay đổi nào.**

### 4. Confirm với merchant

Sau khi được duyệt, xác nhận extension đã apply và tư vấn upgrade nếu phù hợp.

**Sample response (khi hỏi thông tin):**

> Thank you for reaching out! To help you get more AI conversations, I'll need a little more information:
>
> - Approximately how many chats does your store handle per month?
> - Are you considering upgrading your plan, or are you looking for a temporary extension?
>
> Once I have these details, I'll check with our team and get back to you as soon as possible.

## Decision Points

- **Sau khi approved, timeline?** → Tùy availability của team. Nếu urgent, ghi rõ trong escalation message.
- **MC hỏi tại sao cần approval?** → Explain ngắn gọn: conversation limit liên quan đến billing, cần team xác nhận trước khi thay đổi.
