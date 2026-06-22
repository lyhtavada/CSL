# Chatty Proactive Care — Churn-Save Flow cho KH Pro + Plus

**Mục đích:** Chatty CS chủ động chạm nhóm KH **có dấu hiệu churn** trước khi họ rời app — audit setting store để tìm lý do thật, chạm đúng vấn đề, giữ chân.

**Owner:** Liz (CSL) — thiết kế & escalation
**Người chăm:** 4 CS in-house Chatty — Jade, Andy, Hazel, Linda
**Trạng thái:** Spec v2 (2026-06-22) — thu hẹp về **một trigger duy nhất: churn risk** để gỡ nút ca trực

---

## 0. Vì sao chỉ làm churn-save trước (không làm full proactive care)

Khó khăn lớn nhất của proactive care là **CS làm theo ca trực** — không ai theo được một merchant từ đầu đến cuối: hôm nay Andy chạm, mai Andy nghỉ ca, KH reply thì Jade nhận, không ai "sở hữu" mối quan hệ.

Cách gỡ: **không ôm cả 662 KH**, chỉ chạm **số ít có dấu hiệu churn** mỗi tuần.

- List nhỏ (~55 store, xem §1) → chia 4 CS ≈ 14/người, rải ~3-4 store/người/tuần → vừa sức kể cả đang trực ca, **không cần cắt slot riêng**.
- Có **tool audit setting** → cú chạm có nội dung thật ("store mình thấy phần X chưa bật, đó là lý do Y") thay vì "dạo này sao rồi" → tỉ lệ phản hồi cao hơn.
- **Ticket gánh trí nhớ thay người:** mỗi store churn-save = 1 ticket sống, có owner danh nghĩa. CS ca sau đọc ticket trước khi reply → không mất context dù đổi ca.

> Các trigger khác (onboarding, low-usage, relationship touch) tạm gác — mở rộng sau khi flow churn-save chạy ổn.

---

## 1. Khối lượng thực tế (pull dash_merchant_360, 2026-06-22)

Nguồn: `avada-crm.avada_product_dash.dash_merchant_360`, `app_id='avadaFaq'`, `is_paying_now=TRUE`.

| Plan | Tổng paying | churn_label=1 | + billing issue HOẶC inactive≥21d | MRR |
|------|-------------|---------------|-----------------------------------|-----|
| **Plus** | 39 | 10 | **6** | ~$4.6k |
| **Pro** | 623 | 144 | **49** | ~$24.0k |
| | | | **55 store** | |

**List chạm = churn_label=1 VÀ (billing_issue_count>0 HOẶC inactive≥21 ngày)** → ~55 store.
Chia 4 CS ≈ 14 store/người, rải trong tháng → ~3-4 store/người/tuần.

### Ghi chú schema (đã verify)
- `churn_label` (INT64, 0/1) — signal churn chính, **dùng được**.
- `usage_segment` (STRING): giá trị thực = `high_usage` / `inactive_30d` / `active_usage` / NULL. **KHÔNG có `low`** — dùng `inactive_30d` làm signal low-engagement.
- `billing_issue_count`, `has_open_billing_ticket` — signal billing.
- `chatty_last_activity_at` (TIMESTAMP) — tính inactive bằng `TIMESTAMP_DIFF(..., DAY)`.
- `days_to_churn` **không populate** (toàn NULL) → không dùng.
- `current_mrr` Pro ~$39 / Plus ~$118, không ai ≥$50 → **không lọc/ưu tiên theo MRR**.

---

## 2. Ownership — gỡ nút ca trực

| Nhóm | Owner | Cách vận hành |
|------|-------|---------------|
| **Plus churn-risk (~6)** | Assign cố định 1 CS/store | Mini-AM: CS đó theo store đến khi thoát churn hoặc churn hẳn |
| **Pro churn-risk (~49)** | Owner danh nghĩa ghi trên ticket | Ai trong ca cũng chạm được, nhưng **đọc ticket trước**; follow-up sâu đẩy về owner |

**Nguyên tắc chống đứt đoạn ca trực:**
1. Mỗi store churn-save có **1 ticket sống** (không đóng tới khi resolve) — mọi lần chạm/reply log vào đó.
2. KH reply → CS ca đó **đọc ticket trước khi trả lời** (thấy ngay lần trước ai chạm về gì, KH hứa gì).
3. Ticket có field owner → người trong ca chỉ "trực giúp", việc sâu về owner.

---

## 3. Full vòng vận hành

```
[1] LIST (cron, hàng tuần)
    → query dash_merchant_360 (app=avadaFaq, Pro+Plus, is_paying_now)
    → lọc: churn_label=1 AND (billing_issue_count>0 OR inactive>=21d)
    → loại store đã có ticket churn-save đang mở (tránh chạm trùng)
    → ra "churn-save queue" tuần: domain | plan | signal (billing/inactive) | owner

[2] AUDIT SETTING (CS, trước khi chạm)   ← tool audit: Liz mô tả sau
    → CS mở tool audit setting cho store trong list
    → tìm lý do cụ thể: feature chính chưa bật? config sai? widget ẩn?
    → đây là nội dung của cú chạm

[3] NHẮC (Slack, nhóm CS Chatty)
    → Plus: tag CS owner cố định
    → Pro: đẩy queue + owner danh nghĩa
    → mỗi dòng: domain, plan, signal churn, link tool audit, link template

[4] CHẠM (CS thực hiện)
    → template churn-save, tone "đồng hành": nêu cái thấy được từ audit + đề xuất fix
    → KHÔNG nói "anh/chị sắp bỏ app" — chạm bằng giá trị, không bằng cảnh báo

[5] TRACK = TẠO/UPDATE TICKET trên Avada Ticket
    → 1 store = 1 ticket sống, tag "churn-save"
    → cập nhật tsStatus theo phản hồi (waiting_customer / done / churned)

[6] ĐO (định kỳ)
    → trong nhóm churn-risk được chạm: bao nhiêu thoát churn_label=0 / vẫn paying sau 30-60d
    → so với nhóm churn-risk KHÔNG kịp chạm (control)
    → tỉ lệ KH phản hồi, số store cứu được/tháng
```

### Track-by-ticket — chi tiết API
- `POST https://avada-ts-a9cb0.web.app/api/external/tickets`
- Header: `X-API-Key: <AVD_TICKET_API_KEY>` (đã có trong `~/CSL/.env`)
- Field: `subject="[Churn-save] <signal>"`, `appName="Chatty"`, `appPlan`, `domain`, `members[]` (memberId Firebase UID + displayName, lấy qua `GET /members`), `tagIds` (tag "churn-save"), `priority`, `tsStatus`
- Mỗi store 1 ticket sống → nối thẳng KPI/DFY tracker, có owner + status, không cần sheet/Notion riêng.

---

## 4. Playbook giọng & escalation

- Tone theo `_identity/tone-and-voice.md`, nghiêng **"đồng hành"**: nêu cái thấy được từ audit, gợi mở cách dùng tốt hơn — KHÔNG nhắc tới chuyện "sắp rời app".
- Template churn-save chia theo signal: **billing issue** (giúp xử lý thanh toán) / **inactive** (re-onboard, chỉ feature chưa khai thác).
- **Escalate lên Liz khi:** KH đòi giảm giá / refund, dấu hiệu churn nặng ở Plus, complaint vượt tầm CS, KH muốn downgrade.

---

## 5. Việc cần làm để go-live

| # | Việc | Ai | Trạng thái |
|---|------|-----|-----------|
| 1 | Mô tả tool audit setting (tên, cách truy cập, có API/link không) | Liz | ⏳ chờ Liz |
| 2 | Chia ~6 Plus churn-risk cho 4 CS (assign cố định) | Liz | |
| 3 | Lấy memberId 4 CS (Jade/Andy/Hazel/Linda) qua `GET /members` | Betty | |
| 4 | Tạo tag "churn-save" trong ticket system | Liz/Betty | |
| 5 | Viết 2 bộ template churn-save (billing / inactive) | Betty | |
| 6 | Dựng skill `/chatty-care` (query → lọc churn → queue → Slack → tạo ticket) | Betty | |
| 7 | Cài cron hàng tuần (theo pattern cs-weekly) | Liz chạy install | |
| 8 | Dashboard đo cứu-được vs control | Betty | giai đoạn 2 |

---

*Spec v2 — thu hẹp về churn-save để khả thi với mô hình ca trực. Chờ Liz mô tả tool audit (việc #1) trước khi viết template + dựng skill.*
