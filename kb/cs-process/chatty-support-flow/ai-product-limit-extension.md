# AI Product Sync Limit Extension

## When to Use
Khi store có nhiều hơn 5,000 sản phẩm và muốn mở rộng giới hạn AI Product Recommendation sync.

## Background
AI Product Recommendation cho phép sync toàn bộ thông tin sản phẩm vào AI để trả lời chính xác hơn. Giới hạn backend mặc định là **5,000 sản phẩm/store**. Khi vượt quá, app hiển thị thông báo lỗi.

Khi MC nhấn "Contact Us" ở màn hình đó, tin nhắn tự động gửi vào Crisp:
> *"I want to expand the limitation for AI product recommendation."*

## Flow

### 1. Xác nhận thông tin store

Sau khi chào hỏi và xác nhận store URL, hỏi:
- Tổng số sản phẩm trong store? *(shortcut `!number-products`)*
- Tổng số orders đã đặt / trong tháng? *(shortcut `!number-orders`)*

### 2. Xử lý theo quy mô store

**Store < 10,000 sản phẩm + < 100 orders/tháng:**

1. Khuyến khích dùng thử Pro (trial 14 ngày + $1 tháng đầu) *(shortcut `!pro-upgrade-chatty`)*
2. Nếu MC upgrade → vào DevZone enable Unlimited AI → báo MC bắt đầu sync
3. Nếu MC không muốn upgrade → ping Liz tại **#cs-group-2** để tham khảo
   - MC có thể hỏi tại sao Pricing không ghi limit nhưng trong app lại có → dùng shortcut `!beta-ai-sync` để giải thích tính năng đang ở Beta

**Store > 10,000 sản phẩm + > 100 orders/tháng:**

1. Khuyến khích dùng thử Pro *(shortcut `!pro-upgrade-chatty`)*
2. Gửi link book demo call để MC thảo luận với PM *(shortcut `!chatty-demo-call`)*
3. Nếu MC book call → hẹn xử lý request với PM, tiếp tục support
4. Nếu MC không book call và muốn xử lý qua live chat:
   - Dù MC có upgrade hay không → ping **@TungQT** tại **#chatty-support** với đầy đủ thông tin (product + order number) *(shortcut `!10k-products`)*
   - Proceed theo solution của PM

### 3. Tiếp tục support

Follow up với MC theo tiến trình và hỗ trợ thêm nếu cần.
