# Subscription Status Mismatch — CRM vs. App

## When to Use
Khi merchant báo plan hiển thị trong app khác với plan ở CRM — ví dụ CRM hiện Pro nhưng login vào app lại thấy Basic, hoặc ngược lại.

## Nguyên nhân
Status chưa kịp sync giữa Shopify billing và hệ thống Chatty. Thường xảy ra sau khi merchant vừa upgrade/downgrade/cancel.

## Flow

```
KH báo plan sai → CS vào DevZone
                        ↓
            Tìm store → bấm "Check Subscription"
                        ↓
                  Đợi vài giây → hệ thống sync lại
                        ↓
             Hỏi KH reload app và kiểm tra lại
                        ↓
              ┌─────────────────────────┐
              │ Đúng rồi? → Done        │
              │ Vẫn sai? → Escalate TS  │
              └─────────────────────────┘
```

## Các bước chi tiết

1. Vào DevZone → tìm store của merchant
2. Bấm **Check Subscription** để trigger sync
3. Hỏi KH reload lại app (Ctrl+Shift+R hoặc đóng/mở lại)
4. Xác nhận plan đã đúng chưa

## Escalate khi nào

- Sau khi Check Subscription vẫn còn sai → tag TS
- Merchant bị charge sai plan → tag TS + note rõ lịch sử plan

## Template reply

> Hi [Name], I've just synced your subscription status on our end. Could you please refresh the app and check if the correct plan is now showing? Let me know if it still looks off!
