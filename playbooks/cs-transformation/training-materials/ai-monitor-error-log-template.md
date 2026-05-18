# AI Monitor — Error Log Template

> **Dùng cho:** Hazel, Phoebe (Chatty) + Hana, Audrey (Joy)
> **Mục đích:** Ghi nhận AI errors một cách có hệ thống để fix training data hiệu quả
> **Nguyên tắc:** Ghi đủ thông tin để người khác đọc log là hiểu được vấn đề — không cần giải thích thêm.

---

## Tại sao phải log đủ thông tin?

Ghi "AI trả lời sai" không giúp được gì.

Ghi đủ:
- **Câu hỏi gốc** → biết user intent là gì
- **AI reply** → biết AI hiểu sai chỗ nào
- **Correct answer** → biết phải fix thành gì
- **Root cause** → biết fix ở đâu (missing Q&A? sản phẩm hết hàng? tone sai?)

Không có root cause → training data fix sẽ sai chỗ.

---

## Error Log — Format

### Dùng Google Sheet hoặc Notion table với các cột sau:

| Cột | Nội dung | Ví dụ |
|-----|----------|-------|
| **Date** | Ngày ghi nhận | 2026-04-02 |
| **App** | Chatty / Joy | Chatty |
| **Conversation ID** | ID của conversation (nếu có) | #4821 |
| **Topic** | Chủ đề của câu hỏi | Product recommendation |
| **Customer question** | Câu hỏi gốc của khách (copy y nguyên) | "Do you have a size guide for the oversized hoodie?" |
| **AI reply** | AI đã trả lời gì (copy y nguyên) | "I'm sorry, I don't have that information. Please contact our support team." |
| **Correct answer** | Câu trả lời đúng phải là gì | Size guide URL hoặc bảng size cụ thể |
| **Error type** | Phân loại lỗi (xem bên dưới) | Missing data |
| **Root cause** | Tại sao AI sai | Size guide chưa được add vào data sources |
| **Fix needed** | Cần làm gì để fix | Add size guide vào FAQs hoặc custom Q&A |
| **Status** | Open / In progress / Fixed | Open |
| **Fixed by** | Ai fix | Hazel |

---

## Error Types — Phân loại

| Error Type | Định nghĩa | Ví dụ |
|-----------|-----------|-------|
| **Missing data** | AI không có thông tin để trả lời | Khách hỏi về size guide nhưng chưa có trong training data |
| **Wrong data** | AI có thông tin nhưng trả lời sai | AI nói sản phẩm còn hàng nhưng thực ra đã hết |
| **Misunderstood intent** | AI hiểu sai câu hỏi của khách | Khách hỏi "can I return this?" — AI trả lời về shipping thay vì return policy |
| **Wrong tone** | AI trả lời đúng thông tin nhưng tone không phù hợp | Merchant angry, AI vẫn chirpy và liệt kê features |
| **Over-escalated** | AI chuyển human trong khi tự xử được | Khách hỏi giờ hoạt động, AI transfer human thay vì trả lời |
| **Under-escalated** | AI không chuyển human khi cần | Khách complain về refund, AI vẫn cố giải thích chính sách |
| **Hallucinated** | AI bịa thông tin không có trong training data | AI nói "free shipping on all orders" trong khi store không có policy này |

---

## Ví dụ Log Hoàn Chỉnh

### Chatty Example

| Field | Content |
|-------|---------|
| Date | 2026-04-01 |
| App | Chatty |
| Conversation ID | #5032 |
| Topic | Shipping time |
| Customer question | "How long does shipping take to Canada?" |
| AI reply | "We ship to Canada. Please check our website for shipping details." |
| Correct answer | "We ship to Canada in 7–14 business days via standard shipping. Express is 3–5 business days." |
| Error type | Missing data |
| Root cause | Shipping policy chưa có breakdown theo country, chỉ có general "international shipping available" |
| Fix needed | Update shipping policy page → re-sync. Hoặc add custom Q&A: "Shipping to Canada?" → answer với timeline cụ thể |
| Status | Open |
| Fixed by | — |

---

### Joy Example

| Field | Content |
|-------|---------|
| Date | 2026-04-01 |
| App | Joy |
| Conversation ID | #2187 |
| Topic | Points expiration |
| Customer question | "Do my points expire?" |
| AI reply | "Yes, points expire after 12 months of inactivity." |
| Correct answer | "Points don't expire on this store — the merchant hasn't enabled point expiration." |
| Error type | Wrong data |
| Root cause | AI đang trả lời theo Joy default behavior, nhưng merchant này chưa bật expiration setting |
| Fix needed | Add custom Q&A cho store này: "Do points expire?" → "No, your points don't expire." |
| Status | Open |
| Fixed by | — |

---

## Cách dùng Error Log trong ca trực

**Trong ca:**
- Khi thấy AI reply đáng ngờ → copy conversation ID và note nhanh
- Không cần dừng lại để điền full form — note nhanh vào draft
- Nếu case cần escalate → escalate trước, log sau

**Sau ca (hoặc cuối shift):**
- Điền đầy đủ vào log từ notes nhanh
- Review log cũ: có pattern nào mới xuất hiện không?
- Flag cho Liz nếu có error type "Hallucinated" hoặc "Under-escalated" → priority fix

**Weekly:**
- Tổng hợp: tuần này AI sai nhiều nhất về topic nào?
- Đề xuất training data entries cần thêm/sửa
- Hana (Joy) + Hazel (Chatty) lead weekly review

---

## Priority Fix — Thứ tự xử lý

| Priority | Error Type | Tại sao |
|----------|-----------|---------|
| P1 — Fix ngay | Hallucinated, Under-escalated | Risk nhất: AI bịa thông tin hoặc bỏ sót case cần người |
| P2 — Fix trong tuần | Wrong data, Wrong tone | Affect merchant experience trực tiếp |
| P3 — Fix khi có time | Missing data, Over-escalated | AI không tệ, chỉ chưa đủ thông tin |
| P4 — Monitor thêm | Misunderstood intent | Cần thêm variants trong training data để AI hiểu nhiều cách hỏi hơn |
