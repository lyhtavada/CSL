# Chatty CS — Handover cho Andy (Sublead)

**Mục đích:** Andy lên làm sublead hỗ trợ Liz quản lý CS team Chatty. Doc này tổng hợp toàn bộ task Liz đang follow up cho Chatty — để Andy pick up dần.

**Ngày viết:** 2026-09-17 | **Owner gốc:** Liz (CSL) | **Scope:** Chatty only 
---

Đầu việc đang follow up cho Chatty

### 2.1 Theo dõi chỉ số app nói chung — review, chat, install
- **Review App Store (Shopify):** đếm theo tháng/khoảng ngày.
- **Review mobile app (iOS/Play Store):** theo dõi review chưa reply, draft phản hồi theo tone, **Liz duyệt trước khi post** — không tự động post.
- **Chat volume:** đếm conversation thật (sessionize theo merchant, loại traffic nội bộ Avada).
- **Install:** lấy từ data warehouse merchant (`dash_merchant_360`), đang dùng làm mẫu số cho tỷ lệ DFY/install.

### 2.2 CS human/AI Performance
- **QA** 
- **Bot corrections (để đo CS có đang verify/correct bot đúng không)** 
- **DFY review/ point (KPI tháng)** 
- **AI agent performance** 

### 2.3 Project đang triển khai

**DFY**
- **Proactive DFY Pilot** — Andy đang chạy trực tiếp (từ 2026-06-23, 4 ca/tuần): lấy list KH mới cài ≤14 ngày + Pro/Plus từ bảng analytics public (`https://analytics.avada.net/public/views/sytCf8kfby3J5Yknohqa`, tự refresh 1h) → audit store → viết email cá nhân hoá → tạo ticket ngay (tag `DFY-new` + `proactive`). Full SOP: `playbooks/chatty/chatty-proactive-dfy-pilot.md`.
- Andy đã nắm rõ mảng này — có thể cân nhắc nhân rộng pilot sang Jade/Hazel/Linda khi phù hợp.
- **DFY thường (reactive)**: flow + checklist ở `playbooks/chatty/chatty-dfy-flow.md`.


**CS AI agent** (Ivy/Joyce trên `cs2.avada.net`)
- Liz sẽ gửi doc chi tiết riêng hoặc trao đổi trực tiếp 1-1 để Andy nắm kiến trúc/flow đầy đủ.

**TS AI agent** (`ts2.avada.net` — TS Elite v1 đang chạy thật, TS AI Agent v2 đang xây để thay thế)
- Liz sẽ gửi doc chi tiết riêng hoặc trao đổi trực tiếp 1-1. Đầu mối chính bên product: anh Quân.

### 2.4 Weekly/Monthly report liên quan


### 2.5 Crisis management khi có bad review


### 2.6 Training CS Chatty
- Onboarding CS mới + đào tạo kỹ năng theo plan training.

### 2.7 Họp team hàng tuần
- Andy tham gia điều phối cùng Liz — chuẩn bị nội dung từ các mục 2.1–2.6 (chỉ số app, CS performance, tiến độ project, crisis nếu có, training) để đưa vào agenda họp team Chatty.

### 2.8 Xử lý tình huống khó, KH high-risk, refund/billing escalation.
- **Billing/refund**
- **Tình huống nhạy cảm khác** 
- **Discount request (xin giảm giá)**
- **Tạo discount code**

---

## 3. Việc Andy nhận trước khi bắt đầu làm hành chính

**Andy nhận ngay:**
1. **Theo dõi chỉ số app nói chung** — review, chat, install (2.1)
2. **Crisis management** khi có bad review (2.5)
3. **Training CS Chatty** 
4. **Xử lý tình huống khó, KH high-risk** — kể cả tạo discount code
