# Chatty Proactive Care — AM-style Check-in cho KH Pro + Plus

**Mục đích:** Đưa Chatty CS từ reactive (chờ KH chat) sang proactive (chủ động chạm KH cao cấp như Account Manager), để giữ chân và mở rộng nhóm KH Pro + Plus.

**Owner:** Liz (CSL) — thiết kế & escalation
**Người chăm:** 4 CS in-house — Andy, Jade, Hazel, Linda
**Trạng thái:** Spec v1 (2026-06-17) — chờ Liz duyệt trước khi dựng skill/cron

---

## 1. Bức tranh KH (số liệu thực, pull từ warehouse 2026-06-17)

| Plan | Số shops | MRR | Cách chăm |
|------|----------|-----|-----------|
| **Plus** | 39 | ~$4.7k | Assign cố định (mini-AM) |
| **Pro** | 623 | ~$24.6k | Trigger-based, xoay ca |
| Tổng care | **662** | ~$29.4k | |

Nguồn: `avada-crm.avada_product_dash.dash_merchant_360`, `app_id='avadaFaq'`, `is_paying_now=TRUE`.

---

## 2. Mô hình ownership (lai theo tầng)

### Plus (39 shops) — assign cố định
- Chia đều 4 CS → **~10 Plus/người**
- Mỗi CS là mini-AM của nhóm Plus của mình: nhớ tên, biết ngành, chủ động chạm định kỳ
- Nhịp tối thiểu: **1 chạm/tháng/KH** kể cả khi không có trigger (relationship touch)

### Pro (623 shops) — trigger-based, xoay ca
- KHÔNG assign cứng (155/người sẽ loãng)
- Bot lọc ra KH **có lý do để chạm** trong tuần → đẩy vào care queue
- CS trong ca nhận từ queue, chạm xong tạo ticket
- Mục tiêu: chất lượng chạm, không chạm đại trà

> Lý do chọn lai: tập trung quan hệ thật vào 39 Plus giá trị cao; 623 Pro để trigger lọc số ít thực sự cần, tránh quá tải 4 người.

---

## 3. Triggers (đều có sẵn trong `dash_merchant_360` — không cần dựng thêm)

| Trigger | Điều kiện (cột) | Hành động |
|---------|-----------------|-----------|
| **Mới upgrade Pro/Plus** | `days_since_install` thấp / vừa đổi plan | Onboarding check 7 ngày đầu |
| **Low usage** | `chatty_conversations_30d` thấp, `chatty_last_activity_at` xa, `usage_segment` = low | "Thấy bên mình chưa dùng nhiều X…" |
| **Nguy cơ churn** | `churn_label`, `days_to_churn` ngắn, `billing_issue_count > 0` | Chạm cứu, nhắc giá trị đã nhận |
| **Ticket căng** | `has_open_urgent_ticket` / `has_open_billing_ticket` | Follow-up sau khi fix |
| **AI kém hiệu quả** | `chatty_ai_not_found_answers_30d` cao | Đề xuất train thêm FAQ / DFY |
| **Relationship touch** (Plus) | đã >30 ngày chưa chạm | Check-in định kỳ, không cần lý do |

> Ngưỡng cụ thể (vd "low usage = <X convo/30d") sẽ chốt ở bước dựng skill, sau khi xem phân phối thực tế.

---

## 4. Full vòng vận hành

```
[1] LIST + TRIGGER (cron, hàng tuần)
    → query dash_merchant_360 (app=avadaFaq, Pro+Plus)
    → tính trigger cho từng shop
    → ra "care queue" tuần: shop | plan | trigger | gợi ý template

[2] NHẮC (Slack, nhóm CS Chatty)
    → Plus: tag CS được assign
    → Pro: đẩy vào queue chung, ai trong ca nhận
    → mỗi dòng: domain, plan, lý do chạm, link template

[3] CHẠM (CS thực hiện)
    → CS dùng template phù hợp trigger, tone "đồng hành"

[4] TRACK = TẠO TICKET trên Avada Ticket
    → POST /tickets: appName="Chatty", domain, appPlan,
      members=[CS chạm], tag "proactive-care", subject "[Care] <trigger>"
    → cập nhật tsStatus theo phản hồi KH (waiting_customer / done)

[5] ĐO (định kỳ)
    → retention/churn nhóm được chăm vs không
    → expansion (upgrade) sau chạm
    → số chạm/tháng, tỉ lệ KH phản hồi
```

### Track-by-ticket — chi tiết API
- `POST https://avada-ts-a9cb0.web.app/api/external/tickets`
- Header: `X-API-Key: <AVD_TICKET_API_KEY>` (đã có trong `~/CSL/.env`)
- Field chính: `subject`, `appName="Chatty"`, `appPlan`, `domain` (auto lookup store), `members[]` (memberId Firebase UID + displayName — lấy qua `GET /members`), `tagIds` (tag "proactive-care" để lọc), `priority`, `tsStatus`
- Mỗi lần chạm = 1 ticket → nối thẳng vào KPI/DFY tracker, có owner + status để theo dõi, không cần sheet/Notion riêng

---

## 5. Playbook giọng & escalation

- Tone theo `_identity/tone-and-voice.md`, nhưng nghiêng **"đồng hành"** hơn là "support": chủ động, gợi mở, không chờ KH hỏi
- Mỗi trigger có 1 template riêng (onboarding / low-usage / renew / post-incident / relationship touch)
- **Escalate lên Liz khi:** KH đòi giảm giá, upsell lên Enterprise, KH Plus có dấu hiệu churn nặng, complaint vượt tầm CS

---

## 6. Việc cần làm để go-live

| # | Việc | Ai |
|---|------|-----|
| 1 | Chốt ngưỡng trigger (xem phân phối usage thực) | Betty + Liz |
| 2 | Chia 39 Plus cho 4 CS (assign cố định) | Liz |
| 3 | Lấy memberId 4 CS qua `GET /members` | Betty |
| 4 | Tạo tag "proactive-care" trong ticket system | Liz/Betty |
| 5 | Viết bộ template theo trigger | Betty |
| 6 | Dựng skill `/chatty-care` (query → queue → Slack → tạo ticket) | Betty |
| 7 | Cài cron hàng tuần (theo pattern cs-weekly) | Liz chạy install |
| 8 | Dashboard đo retention nhóm chăm vs không | Betty (giai đoạn 2) |

---

*Spec này chưa dựng code — chờ Liz duyệt mô hình & ngưỡng trước khi build skill.*
