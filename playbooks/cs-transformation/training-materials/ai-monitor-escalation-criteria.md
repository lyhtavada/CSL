# AI Monitor — Escalation Criteria

> **Dùng cho:** Hazel, Phoebe (Chatty) + Hana, Audrey (Joy)
> **Mục đích:** Biết khi nào để AI tự xử, khi nào phải nhảy vào
> **Nguyên tắc:** Khi không chắc → escalate. Sai về phía safe hơn là bỏ sót.

---

## Tổng quan — 3 tình huống cơ bản

| Tình huống | Hành động |
|-----------|-----------|
| AI đang xử lý tốt | Để AI chạy, không cần làm gì |
| AI đang xử lý, nhưng reply có vấn đề | Flag để sửa training data sau — không cần nhảy vào ngay |
| AI cần người, hoặc case thuộc danh sách bên dưới | Nhảy vào ngay, tiếp nhận conversation |

---

## CHATTY — Escalate ngay (không cần đợi AI transfer)

### Luôn escalate — không exception:

| Loại case | Lý do |
|-----------|-------|
| Khách yêu cầu hoàn tiền / refund | Policy decision — AI không có thẩm quyền |
| Billing dispute | Cần check subscription, Shopify billing — AI không access được |
| Merchant angry / frustrated rõ ràng | Tone của AI không phù hợp khi khách đang giận |
| Bug report từ merchant | Cần forward cho TS team — AI không handle được |
| Merchant đang mất dữ liệu (conversations, contacts) | Urgent tech issue |
| Merchant muốn cancel app / uninstall | Retention case — cần human |
| Merchant hỏi về enterprise / custom deal | Sales territory |
| Khách dùng ngôn ngữ không phải English mà AI đang trả lời sai | Translation issue |
| Khách là VIP / large merchant (Pro/Plus plan) | High-value, cần high-touch |

### Escalate nếu AI đã reply 2–3 lần mà chưa giải quyết được:

- Merchant hỏi lại câu đó nhiều lần → AI không hiểu, cần human interpret
- AI reply "I'm not sure" hoặc "I don't have information about that" → training gap, nhưng khách cần câu trả lời ngay
- AI recommend sản phẩm sai hoặc hết hàng → nhảy vào, đính chính

### Không cần escalate — để AI xử:

| Loại case | Ghi chú |
|-----------|---------|
| Product questions (ingredients, sizing, specs, compatibility) | AI được train cho việc này |
| Giờ shipping / chính sách return cơ bản | AI có từ data sources |
| FAQ thông thường | Nếu AI được train đúng |
| Order tracking request | AI skill: order tracking trong chatbox |
| "Chatbox ở đâu / làm sao để mở" | Chatbox how-to |

---

## JOY — Escalate ngay (không cần đợi AI transfer)

### Luôn escalate — không exception:

| Loại case | Lý do |
|-----------|-------|
| Points dispute / khách complain bị mất điểm | Cần verify + manual adjustment — AI không làm được |
| Billing / subscription issue | Cần check account |
| Merchant angry / frustrated | Không để AI xử khi merchant đã upset |
| Bug report (points không earn, widget không hiện) | Cần debug, forward TS |
| Migration support (từ Smile, Yotpo, v.v.) | Process phức tạp, cần guided support |
| Merchant muốn cancel | Retention case |
| Enterprise inquiry | Sales territory |
| VIP tier complaint từ end customer của merchant | Sensitive — affect merchant's customer relationship |

### Escalate nếu AI đã reply 2–3 lần mà chưa giải quyết:

- Merchant hỏi về custom earning rule phức tạp → AI có thể không biết edge cases
- Merchant hỏi về Shopify Flow integration → nếu vượt quá basic setup
- AI không confident → nhảy vào thay vì để AI guess

### Không cần escalate — để AI xử:

| Loại case | Ghi chú |
|-----------|---------|
| "Điểm của tôi đâu?" → hướng dẫn xem points balance | Basic how-to |
| "Làm sao để redeem điểm?" | Basic how-to |
| "Loyalty widget ở đâu trên store?" | Basic how-to |
| "Birthday reward hoạt động thế nào?" | Standard feature explanation |
| "Referral link của tôi ở đâu?" | Basic how-to |

---

## SLA — Response Time

| Scenario | SLA |
|----------|-----|
| AI transfer trong FT hours (8AM–12AM) | Pickup ≤ 5 min |
| AI transfer overnight (12AM–8AM) | Pickup ≤ 15 min (remote/outsource cover) |
| Angry merchant / urgent escalation | Pickup ≤ 3 min |

> **Khi AI transfer:** AI sẽ gửi message tự động "An agent will be with you shortly." — merchant biết phải chờ. Không panic, nhưng đừng để quá SLA.

---

## Cách nhảy vào conversation đang chạy

1. Open conversation trong inbox
2. Assign cho mình (remove AI assignee)
3. Đọc chat summary AI đã tạo (ở top of conversation khi AI transfer)
4. Tiếp tục từ đó — không hỏi lại những gì khách đã nói với AI

**Câu mở khi nhảy vào:**

> "Hi [Name], I'm [your name] from the support team — I've reviewed your conversation and I'm here to help."

*(Không cần nói "AI đã transfer tôi vào" — giữ seamless)*

---

## Khi AI trả lời sai — Không phải lúc nào cũng escalate

Nếu AI đã reply sai nhưng conversation đã ended:
→ **Không cần escalate** — log lỗi vào error log, fix training data

Nếu AI đang trong conversation và vừa reply sai:
→ **Nhảy vào nếu** lỗi có thể gây nhầm lẫn nghiêm trọng (sai giá, sai chính sách, hết hàng)
→ **Để yên và log nếu** lỗi nhỏ, không affect outcome (ví dụ: AI nói "please allow 3–5 business days" nhưng thực tế là 2–3)
