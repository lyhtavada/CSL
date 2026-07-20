# Cơ chế Reward Point — Ticket AI Agent

> CS dùng AI agent để investigate issue và tạo ticket → được reward point. Point gắn với **giá trị/độ khó issue**, không thưởng cho việc chỉ tạo ticket. 1 point = 1.000đ.
>
> **Khâu review = Review Agent** (LLM-judge do team xây): mỗi ticket sau khi đóng, agent vào đọc + chấm điểm. Agent tự chốt ca rõ ràng; Liz chỉ duyệt exception (L3 + low-confidence/flagged).

## 1. Mục tiêu

Khuyến khích CS dùng AI agent investigate & tạo ticket, thưởng theo **giá trị/outcome thật của issue** — không thưởng cho ticket rác hay ticket chỉ đúng format. Trần **1.000p/CS/tháng** để kiểm soát chi phí.

## 2. Nhận diện ticket thuộc chương trình (gate cứng — auto)

Ticket phải thỏa **CẢ 2** điều kiện, đọc trực tiếp từ field ticket:

- Creator là **CS thật**: `members[isCreate:true].authUid` **≠** `ai-agent-*`
- CS đã **dùng AI agent**: tồn tại `members[].authUid` bắt đầu bằng `ai-agent-`

→ CS nhận point = `members[isCreate:true].displayName` → map sang nickname KPI (bảng có sẵn trong /dfy-tracker). Merge trùng tên (`Alyssa` = `alyssa_avada`).

**Loại ngay (không vào chương trình, không cần agent chấm):**

- AI agent tự tạo ticket (creator là `ai-agent-*`, không có CS) → không có CS để thưởng
- Ticket thường không có AI agent tham gia → không thuộc chương trình

## 3. Review Agent — người chấm điểm

Đây là điểm khác biệt cốt lõi: **không auto-map cứng theo field**, mà để 1 agent đọc nội dung thật và chấm như 1 reviewer.

### 3.1. Trigger

Ticket đóng lại (`ticketStatus = "closed"`) **hoặc** `tsStatus` vào nhóm kết thúc (`done` / `dev_done` / `feature_request`) → đẩy ticket vào hàng đợi Review Agent. Webhook khi mark done, hoặc cron poll ticket mới đóng theo ngày.

### 3.2. Agent đọc gì (đủ context để chấm như người)

- **Ticket fields:** `description`, `tsStatus`, `ticketStatus`, `tagIds`, `store[0].domain`, `members`, `shortUrl`
- **Full Crisp session** (`chatLink` → BigQuery `avada_cs.crisp_chats`, không giới hạn 40 msg như Crisp API)
- **Investigation trace của AI agent** — những gì `ai-agent-*` đã làm trong ticket/chat (CS thực sự dùng agent đào root cause, hay chỉ mở cho có)

### 3.3. Agent chấm 3 trục → verdict

1. **Valid?** — issue có thật + AI agent được dùng thật để investigate. Nếu ticket format đúng nhưng nội dung mỏng / không thực sự cần AI / farm → `valid=false`, **0p** kèm lý do. *(Đây là chỗ agent bịt lỗ hổng mà auto-theo-field không lọc được.)*
2. **Level** — **Basic** / **Dev Confirm**, chấm theo **nội dung Crisp + investigation**, có tham chiếu `tsStatus` (xem §4).
3. **Investigation quality** — độ sâu CS dùng agent (chỉ mở → điểm thấp; đào ra root cause, tái hiện, xác định scope → điểm cao). Ảnh hưởng confidence và tie-break level.

### 3.4. Output

JSON ghi vào ticket note + Notion row:

```json
{ "ticketId": "...", "cs": "Linda", "valid": true, "level": "L2", "point": 35,
  "confidence": 0.86, "reason": "CS dùng agent đào ra bug expire point sai, đẩy dev_done...",
  "flags": [] }
```

`flags` ví dụ: `low_confidence`, `possible_farm`, `l3_candidate`, `dedup_suspect`, `mismatch_tsStatus`.

### 3.5. Human-in-loop (rút gọn)

- **Agent auto-chốt** ca `valid` + level ∈ {L1, L2} + `confidence ≥ ngưỡng` (khởi điểm 0.8) + không flag.
- **Liz duyệt** khi: level = **L3**, hoặc có bất kỳ flag (`low_confidence` / `possible_farm` / `mismatch_tsStatus` …). Point các ca này chỉ cộng sau khi Liz OK.
- Cuối tháng: batch các ca chờ duyệt gom vào 1 Notion view + DM Liz.

> Liz **không** duyệt từng ticket — chỉ chạm vào exception. Đúng tinh thần auto, nhưng review được nội dung thật.

## 4. Bảng LEVEL & point (khung agent chấm)

Agent quyết level dựa trên **nội dung thật**; `tsStatus` là **1 tín hiệu đầu vào để cross-check**, không phải trần cứng.

| Level | Ý nghĩa | Tín hiệu (nội dung + tsStatus) | Point |
|-------|---------|-------------------------------|-------|
| L1 — Basic | Issue xử lý được, khách OK | agent thấy issue hợp lệ, thường kèm `done` / `waiting_customer` | 20 |
| L2 — Dev-confirmed | Bug thật, dev tiếp nhận | agent xác nhận là bug, thường kèm `dev_fixing` / `dev_done` | 35 |
| L3 — High-impact | Bug ảnh hưởng nhiều shop / feed cải thiện AI-KB | agent đánh giá high-impact → gắn `l3_candidate`, **Liz duyệt** | 50 |
| Feature request | Ra feature request hợp lệ | `feature_request` + nội dung agent xác nhận | 15 |

**Cross-check chống farm bằng `tsStatus`:** nếu agent đòi L2/L3 nhưng ticket mới `done`, chưa từng qua `dev_fixing`/`dev_done` → agent hạ confidence + flag `mismatch_tsStatus` → đẩy Liz duyệt. CS không tự set `dev_done` được (phải qua pipeline dev) nên đây là lớp chống farm rẻ mà chắc.

> Ý nghĩa `tsStatus` (giá trị thật đang chạy): `done` = xong khách OK · `dev_fixing`/`dev_done` = đẩy dev / dev đã fix · `feature_request` = ra FR · `done_for_you` = DFY (không thuộc chương trình này) · `waiting_customer`/`pending`/`doing` = đang xử lý · `sale_request`/`billing`/`onb` = ngoài phạm vi.

## 5. Chống farm

- **Agent tự gác** ở §3.3 trục 1 (nội dung mỏng/farm → `valid=false`, 0p).
- `ticketStatus` = invalid / duplicate, hoặc dedup trùng domain + nội dung trong 7 ngày → **0p** (auto, không cần agent).
- Tỷ lệ (invalid + dup + `valid=false`)/CS **> 30%/tuần** → tuần đó chỉ tính L1 (không cho L2/L3), flag Liz.
- **Trần 1.000p/CS/tháng** — chạm trần thì dừng cộng, Liz duyệt nếu vượt.

**Không đạt = 0p** (không phạt).

## 6. Ước chi phí trên data thật (01–15/07)

25 ticket AI agent CS-tạo trong nửa tháng → ~50/tháng cả 2 app.

| App | Ticket | Ước point (theo outcome thật) |
|-----|--------|-------------------------------|
| JOY | 7 | ~210p |
| Chatty | 18 | ~410p |
| Tổng nửa tháng | 25 | ~620p → ~1.2tr/tháng cả 2 app |

Per-CS cao nhất hiện tại (Linda ~12 Chatty ticket) → ~500p/tháng — dưới trần 1.000p thoải mái. Ngân sách thật ~**1–1.5tr/tháng cho cả team** — kiểm soát được. *(Chi phí LLM cho Review Agent: ~50 ticket/tháng × 1 lượt chấm = không đáng kể.)*

## 7. Vận hành

- Skill/service mới `/ai-ticket-reward` — tái dùng code fetch + bảng nickname của /dfy-tracker.
- Luồng: fetch ticket đóng → gate cứng (§2) → **Review Agent chấm** (§3) → auto-chốt L1/L2 hoặc đẩy Liz duyệt (L3/flag) → gom per-CS → report tuần/tháng.
- Cron tuần (monitor + gom ca chờ duyệt) + tháng (chốt point) → Notion + DM Liz.
- **Team xây Review Agent** (LLM-judge): input = ticket + Crisp session + investigation trace; output = JSON §3.4. Prompt/rubric chấm theo §3.3 + §4.

## 8. Ví dụ chấm trên ticket thật

- **JOY-260715-M6azs5** (Alyssa tạo, có ai-agent-2, tsStatus: pending): qua gate cứng → Review Agent đọc Crisp + trace → nếu là bug thật đã đào root cause → L2 (35p), auto-chốt nếu confidence cao; nếu agent thấy high-impact → gắn `l3_candidate`, Liz duyệt.
- **JOY-260715-6ucCLC** (ai-agent-2 tự tạo, không có CS creator): loại ngay ở gate cứng, không đưa vào Review Agent.
