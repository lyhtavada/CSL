# SOP — Phân Loại và Support ICP Trong Chat

**Áp dụng cho:** CS Chatty
**Trigger:** Merchant vào chat, chưa rõ họ thuộc nhóm nào
**Mục tiêu:** Nhận diện đúng chân dung → support đúng cách → offer phù hợp

---

## Tại sao cần làm điều này

Chatty có 4 nhóm merchant khác nhau — mỗi nhóm có nỗi đau khác nhau và kỳ vọng khác nhau. Support đúng nhóm mới tạo được giá trị thật, không phải chỉ giải quyết ticket.

Mục tiêu không phải on-demand support — mà là **hiểu đúng needs và problem**, từ đó offer đúng mức hỗ trợ và chất lượng.

Xem [icp-chatty-cs.md](../icp-chatty-cs.md) để hiểu chi tiết từng chân dung.

---

## Flow tổng quan

```
Merchant vào chat
      ↓
Bước 1: Lọc nhanh — email domain + GMV
      ↓
Bước 2: Hỏi 2–3 câu trong chat để verify
      ↓
Bước 3: Gắn tag chân dung
      ↓
Bước 4: Support đúng cách + offer phù hợp
```

---

## Bước 1 — Lọc nhanh từ tín hiệu đầu tiên

Trước khi hỏi bất cứ điều gì, nhìn ngay vào:

| Tín hiệu | Cách đọc |
|----------|----------|
| **Email domain** | `@gmail/@yahoo` → Solo Explorer. `@brandname.com` → Growing Operator trở lên |
| **GMV trong CRM** | Nếu có → dùng để xác nhận nhóm ngay |
| **Merchant tự nói** | "Tôi đang chạy $X/tháng ads", "Tôi tự quản lý store" → tín hiệu rõ |

Nếu đã rõ → bỏ qua Bước 2, đi thẳng Bước 3.
Nếu chưa rõ → tiếp tục Bước 2.

---

## Bước 2 — Hỏi trong chat để verify

Không hỏi hàng loạt. Chọn **2–3 câu** phù hợp với những gì merchant đang nói. Hỏi tự nhiên, không phải điều tra.

| Câu hỏi | Solo Explorer | Growing Operator | Scaling CX Lead |
|---------|--------------|-----------------|-----------------|
| "What tool are you currently using to chat with customers?" | Shopify Inbox / free app | Tidio / basic app | Gorgias / Zendesk |
| "How many people handle CS on your team, and what hours do they work?" | 0–1 person | 1–3 people, business hours only | 3–5+ people, has manager |
| "Are you running paid ads?" | Not yet / organic only | $3K+/month Meta/Google | Large budget, has agency |
| "What's the one thing you'd most want Chatty to help with?" | Reduce repetitive questions | Stop losing sales after hours | AI handling refunds/order changes end-to-end |

**Nguyên tắc hỏi:**
- Hỏi trong mạch tự nhiên của cuộc trò chuyện — không hỏi thành bảng khảo sát
- Nếu merchant đã trả lời trong câu trước → không hỏi lại
- 2 tín hiệu khớp nhau là đủ để phân loại

---

## Bước 3 — Gắn tag chân dung

Sau khi phân loại, gắn tag trong hệ thống để team nhìn vào biết ngay:

| Tag | Chân dung |
|-----|-----------|
| `icp-solo` | Solo Explorer |
| `icp-growing` | Growing Operator ⭐ |
| `icp-scaling` | Scaling CX Lead |
| `icp-midmarket` | Mid-Market Proof-Giver |
| `icp-unknown` | Chưa đủ thông tin để phân loại |

---

## Bước 4 — Khai thác needs và pain point

Mục tiêu chính ở bước này không phải giải quyết ticket — mà là **hiểu đúng merchant đang cần gì và đang đau ở đâu**. Hai nhóm dưới đây là trọng tâm, kênh khai thác khác nhau.

---

### Solo Explorer — `icp-solo` → Khai thác qua live chat

Không cần call. Khai thác ngay trong mạch chat đang diễn ra.

**Reassure trước** — họ lo AI phá brand, cần trấn an trước khi hỏi sâu hơn.

**Câu hỏi khai thác trong chat:**
- "What kind of questions do customers ask you most often?"
- "How much time do you spend replying to customer messages each day?"
- "Have you ever missed a sale because you couldn't reply in time?"
- "What would make the biggest difference for you if Chatty could handle it?"

**Nguyên tắc:** Hỏi 1–2 câu, không dồn dập. Lắng nghe và phản hồi tự nhiên trước khi hỏi câu tiếp theo.

**Sau khi nghe:** Ghi lại pain point chính vào tag note. Hướng dẫn setup phù hợp với đúng điều họ vừa nói.

---

### Growing Operator — `icp-growing` ⭐ → Offer call để khai thác sâu

Đây là nhóm đáng đầu tư nhất. Khai thác qua call vì họ có nhiều thứ để chia sẻ hơn những gì chat capture được.

**Offer call ngay khi đã qualify** — gửi link cal.com cá nhân của mình:
> "I'd love to learn more about how your store operates and make sure Chatty is set up in a way that actually moves the needle for you — feel free to grab a time that works for you: [your cal.com link]"

**Khi khách đã book:** nhắn vào [#chatty-calls](https://avadaio.slack.com/archives/C09CE4PFWKT) với thông tin: tên store, chân dung, pain point nghe được trong chat, thời gian call.

**Trong call, tập trung vào:**
- "Walk me through what happens after your CS team logs off — what do customers do?"
- "What's the biggest source of missed revenue right now that you're aware of?"
- "If Chatty could only solve one problem for you, what would that be?"
- "What would success look like for you 30 days from now?"

Chi tiết câu hỏi và cách chạy call → xem [handle-icp-discovery-call.md](handle-icp-discovery-call.md)

---

### Scaling CX Lead và Mid-Market

- **Scaling CX Lead** → offer call/demo, xem SOP call
- **Mid-Market** → escalate lên Liz ngay, CS không handle solo

---

## Checklist nhanh cuối conversation

Trước khi close ticket, check:

- [ ] Đã gắn tag chân dung chưa?
- [ ] Support approach có đúng với chân dung không?
- [ ] Đã offer phù hợp chưa (call / tiếp tục chat / escalate)?
- [ ] Nếu là Mid-Market — đã báo Liz chưa?

---

## Lưu ý

- **Không phán xét merchant qua 1 tín hiệu duy nhất** — email cá nhân không có nghĩa chắc chắn là Solo Explorer, có thể Growing Operator mới mở store
- **Chân dung có thể thay đổi** — merchant tháng trước là Solo Explorer, tháng này có thể đã lên Growing Operator
- **Mục tiêu cuối cùng** là hiểu đúng needs và problem — không phải điền đúng tag

---

*Cập nhật: 2026-04-23*
*Liên quan: [icp-chatty-cs.md](../icp-chatty-cs.md)*
