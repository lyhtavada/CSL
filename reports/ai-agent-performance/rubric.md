# AI Agent Quality Rubric

> Betty dùng file này khi Liz paste Crisp session link để chấm điểm.

---

## Scoring Labels

| Label | Ý nghĩa |
|-------|---------|
| ✅ Good | AI handle đúng — thông tin chính xác, tone phù hợp, không cần làm gì thêm |
| ⚠️ Needs Fix | AI không sai nghiêm trọng nhưng có gap — cần update training data |
| 🚨 Escalate (Missed) | AI không nên xử case này một mình — human đáng lẽ phải nhảy vào |

---

## Cách Betty chấm 1 conversation

**Bước 1 — Phân loại bucket:**
- Có tag `<escalate_human>` trong conversation? → **Bucket A**
- CS nhảy vào mà không có tag? → **Bucket B**
- AI handle end-to-end? → **Bucket C (AI-resolved)**

**Bước 2 — Rate chất lượng AI:**

Đặt 4 câu hỏi:

1. **Accuracy** — AI trả lời đúng thông tin không?
   - ✅ Accurate / ⚠️ Partially / ❌ Wrong / ❓ Can't verify

2. **Tone** — AI có phù hợp với tình huống không?
   - ✅ Appropriate / ⚠️ Too generic / ❌ Mismatched (e.g., casual khi khách angry)

3. **Resolution** — Vấn đề của merchant được giải quyết không?
   - ✅ Resolved / ⚠️ Partially / ❌ Unresolved / 🔄 Transferred to human

4. **Escalation judgment** — AI quyết định escalate/không escalate đúng không?
   - ✅ Correct / ⚠️ Should have escalated sooner / ❌ Should NOT have escalated / 🚨 Escalation missed

**Bước 3 — Gán overall label:**

| Kết quả | Label |
|---------|-------|
| Tất cả ✅ | ✅ Good |
| 1+ ⚠️, không có ❌ | ⚠️ Needs Fix |
| Bất kỳ ❌ hoặc 🚨 | 🚨 Escalate (Missed) / ❌ Error |

**Bước 4 — Ghi note ngắn:**
- Lý do label
- Training data gap nếu có (dùng cho FA weekly review)

---

## Cases luôn là 🚨 Escalate (Missed) — không exception

**Chatty & Joy:**
- Khách yêu cầu refund / billing dispute
- Merchant angry / frustrated rõ ràng
- Cancel/uninstall request (retention case)
- Bug report chưa được escalate lên TS
- VIP / large merchant (Pro/Plus/Advanced plan)
- Competitor inquiry

**Chatty thêm:**
- Mất dữ liệu (conversations, contacts)
- Enterprise / custom deal inquiry

**Joy thêm:**
- Points dispute / lost points complaint
- Migration support (từ Smile, Yotpo, v.v.)
- VIP tier complaint từ end customer của merchant

---

## Output format khi Betty trả về scorecard

```
## Session: [session_id hoặc link]
**App:** Chatty / Joy
**Date:** YYYY-MM-DD
**Bucket:** A (bot escalated) / B (human stepped in) / C (AI-resolved)

**Scores:**
- Accuracy: ✅ / ⚠️ / ❌
- Tone: ✅ / ⚠️ / ❌
- Resolution: ✅ / ⚠️ / ❌ / 🔄
- Escalation judgment: ✅ / ⚠️ / ❌ / 🚨

**Overall:** ✅ Good / ⚠️ Needs Fix / 🚨 Escalate (Missed)

**Notes:** [lý do + training gap nếu có]
```
