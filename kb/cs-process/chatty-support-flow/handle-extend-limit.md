# Extend AI Training Limits cho Merchant

## When to Use
Khi merchant yêu cầu tăng limit cho Products, Custom Answers, URL & File, AI Conversations, hoặc AI Scenarios — vì đã chạm giới hạn plan hiện tại.

## Who
- **CS Agent (Chatty):** Tự xử lý extend Products, Custom Answers, URL & File
- **PM (qua #sale-cs-success):** Duyệt extend AI Conversations và AI Scenarios

## Plan Limits

| Feature | Free | Basic ($19.99) | Pro ($68.99) | Plus ($199) |
|---------|------|----------------|--------------|-------------|
| AI conversations | 50/month | 100/month | 500/month | 1,000/month |
| Products for AI training | 200 | 1,500 | 8,000 | Unlimited |
| Custom answers for AI training | 100 | 1,000 | Unlimited | Unlimited |
| URL & File for AI training | 20 | 50 | 500 | Unlimited |
| AI scenarios | 5 | 5 | 15 | — |

## Phân loại: CS tự extend vs. cần escalate

| Loại limit | CS tự extend? | Ghi chú |
|------------|---------------|---------|
| Products for AI training | ✅ Có | Extend lên limit của plan tiếp theo |
| Custom answers for AI training | ✅ Có | Extend lên limit của plan tiếp theo |
| URL & File for AI training | ✅ Có | Extend lên limit của plan tiếp theo |
| AI conversations | ❌ Không | Escalate → xem quy trình riêng |
| AI scenarios | ❌ Không | Escalate → xem quy trình riêng |

## Flow: CS tự extend (Products / Custom Answers / URL & File)

### 1. Xác nhận nhu cầu

Khi MC báo chạm limit, xác nhận:
- MC đang ở plan nào?
- Loại limit nào bị chạm? (Products, Custom Answers, hay URL & File)
- MC cần bao nhiêu? (VD: "I have 300 products but can only sync 100")

### 2. Quyết định extend bao nhiêu

**Nguyên tắc: extend lên đúng limit của plan tiếp theo (1 bậc), không hơn.**

| MC đang ở | Products | Custom Answers | URL & File |
|-----------|----------|----------------|------------|
| Free → extend lên | 1,500 (= Basic) | 1,000 (= Basic) | 50 (= Basic) |
| Basic → extend lên | 8,000 (= Pro) | Unlimited (= Pro) | 500 (= Pro) |
| Pro → extend lên | Unlimited (= Plus) | Đã Unlimited | Unlimited (= Plus) |
| Plus | Đã Unlimited | Đã Unlimited | Đã Unlimited |

**Lưu ý:**
- Chỉ extend 1 bậc. MC muốn nhiều hơn → khuyến khích upgrade plan
- Trên Plus, Products / Custom Answers / URL & File đều **Unlimited** → không cần extend. MC Plus báo chạm wall → khả năng là lỗi sync, không phải quota

### 3. Thực hiện extend trên DevZone

1. Vào **DevZone** → tìm store theo domain
2. Điều chỉnh limit tương ứng (Products / Custom Answers / URL & File)
3. Confirm thay đổi đã apply

### 4. Tag conversation

Sau khi extend xong, thêm tag **`extended-limit`** vào conversation trên Crisp.

Mục đích: để team có thể filter và review lại các case đã extend, theo dõi MC có upgrade sau đó không.

### 5. Confirm với merchant

> Great news! I've extended your [Products/Custom Answers/URL & File] limit so you can continue setting up your AI assistant. You should now be able to [sync more products / add more custom answers / upload more files].
>
> Just so you know, if you need even more capacity in the future, upgrading to [next plan] would give you [limit of next plan] and also unlock [key feature of that plan]. Let me know if you need any help with that!

### 6. Decision points

- **MC yêu cầu extend nhiều loại cùng lúc** → extend từng loại, tất cả lên 1 bậc
- **MC đã được extend trước đó và quay lại xin thêm** → khuyến khích upgrade, nếu MC vẫn muốn → báo CSL
- **MC ở Free plan** → vẫn extend lên Basic limit, nhưng nhấn mạnh lợi ích upgrade
- **MC ở Plus và cần vượt limit** → escalate PM qua #sale-cs-success

## Flow: Cần escalate (AI Conversations / AI Scenarios)

CS **không tự extend** 2 loại limit này. Refer đến quy trình riêng:

### AI Conversations
→ Xem: [AI Conversation Limit Extension](../../../ai-copilot-training/chatty/training-data/chatty-cs-process/ai-conversation-limit-extension.md)

Tóm tắt:
1. Thu thập info: store URL, plan hiện tại, volume chat/tháng, lý do cần thêm
2. Kiểm tra upgrade có giải quyết không → khuyến khích upgrade trước
3. Escalate **#sale-cs-success**, tag PM với đầy đủ thông tin
4. Chờ duyệt → confirm với MC

### AI Scenarios
→ Xem: [AI Scenario Limit Extension](../../../ai-copilot-training/chatty/training-data/chatty-cs-process/ai-scenario-limit-extension.md)

Tóm tắt:
1. Hỏi MC cần thêm bao nhiêu scenarios, use case cụ thể
2. Escalate **#sale-cs-success**, tag PM/CSL với store URL + plan + số scenarios cần + use cases
3. Chờ duyệt → confirm với MC

## Notes

- **Mục đích extend:** cho MC trải nghiệm đủ để thấy giá trị Chatty → tự upgrade. Không phải cho free vĩnh viễn.
- **Luôn tag `extended-limit`** sau khi extend — bắt buộc, không bỏ qua.
- **Không extend AI Conversations và AI Scenarios** — 2 loại này ảnh hưởng trực tiếp đến billing và product strategy, cần PM duyệt.
- **MC quay lại xin extend lần 2+** → đây là signal mạnh rằng MC cần upgrade. Push upgrade, nếu MC vẫn từ chối → báo CSL.
