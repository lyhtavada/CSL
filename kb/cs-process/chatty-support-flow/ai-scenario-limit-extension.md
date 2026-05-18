# AI Scenario Limit Extension

## When to Use
Khi merchant hit scenario limit và cần thêm scenarios ngoài giới hạn plan.

## Who
- **CS Agent:** Thu thập thông tin, escalate
- **PM hoặc CSL (qua #sale-cs-success):** Duyệt extension request

## Plan Limits

| Plan | Scenario Limit |
|------|---------------|
| Free / Basic | 5 scenarios |
| Pro | 15 scenarios |
| Plus | — |

**Lưu ý:** Store cũ (tạo trước khi có limit) giữ nguyên số scenarios hiện có, không bị áp limit mới.

## Flow

### 1. Hiểu nhu cầu của merchant

Hỏi MC:
- Cần thêm bao nhiêu scenarios và tại sao?
- Use case cụ thể: loại câu hỏi / situation nào sẽ được cover?
- Plan hiện tại là gì?

*(Càng cụ thể càng tốt — giúp approval nhanh hơn)*

### 2. Escalate lên #sale-cs-success

Post vào **#sale-cs-success**, tag PM hoặc CSL với:
- Store URL + plan hiện tại
- Số scenarios đang dùng
- Số scenarios cần thêm
- Use cases / situations sẽ handle

**Chờ approval trước khi thực hiện bất kỳ thay đổi nào.**

### 3. Confirm với merchant

Sau khi được duyệt, confirm limit đã update và MC có thể tiếp tục.

**Sample response (khi hỏi thông tin):**

> Thanks for getting in touch! To help with your request, could you share a bit more about what you'd like to use the additional scenarios for — for example, what types of customer questions or situations you're looking to cover?
>
> This helps us process your request faster. I'll follow up once I have an update from our team.
