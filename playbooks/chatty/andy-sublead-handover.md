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

### 2.2 CS Performance
- **QA:** chấm 3 trục Mindset/Knowledge/Skill cho từng CS Chatty từ chat thật, feedback sau khi Liz duyệt. Có bản QA tháng riêng theo policy/penalty (`playbooks/qa/`).
- **Bot corrections (để đo CS có đang train bot đúng không):** gom câu Ivy bị CS sửa theo topic + người sửa, feed vào KB/training.
- **DFY point (KPI tháng):** Chatty tính theo % task hoàn thành/block (AI 50 + Chatbox 30 + Video 50 = max 130p).
- **Bot performance (context để hiểu tải CS):** AI resolved % (`aiResolvedPct`, cs2 `/api/obs/metrics`) — mốc cần theo dõi: **≥60%** để chuyển Phase 3 CS Transformation (Hazel/Phoebe async hoá, Andy/Jade tăng tải AM). Hiện tại (tuần 07–13/09): Ivy **54.5%** — chưa đạt.

### 2.3 Project đang triển khai

**DFY**
- **Proactive DFY Pilot** — Andy đang chạy trực tiếp (từ 2026-06-23, 4 ca/tuần): lấy list KH mới cài ≤14 ngày + Pro/Plus từ bảng analytics public (`https://analytics.avada.net/public/views/sytCf8kfby3J5Yknohqa`, tự refresh 1h) → audit store → viết email cá nhân hoá → tạo ticket ngay (tag `DFY-new` + `proactive`). Full SOP: `playbooks/chatty/chatty-proactive-dfy-pilot.md`.
- **DFY thường (reactive)**: flow + checklist ở `playbooks/chatty/chatty-dfy-flow.md`.
- Andy đã nắm rõ mảng này — có thể cân nhắc nhân rộng pilot sang Jade/Hazel/Linda khi phù hợp.

**CS AI agent** (Ivy/Joyce trên `cs2.avada.net`)
- Liz sẽ gửi doc chi tiết riêng hoặc trao đổi trực tiếp 1-1 để Andy nắm kiến trúc/flow đầy đủ.
- Việc liên quan đang chạy song song: KB audit sau UI restructure Chatty (Chatbox tách AI Mode/Legacy, AI agent page dựng lại bento hub Skills/Scenarios) — 6/21 file đã patch, 15 file còn lại, chưa test lại toàn bộ batch. Chi tiết ở memory `chatty_ui_restructure_kb_audit.md`.

**TS AI agent** (`ts2.avada.net` — TS Elite v1 đang chạy thật, TS AI Agent v2 đang xây để thay thế)
- Liz sẽ gửi doc chi tiết riêng hoặc trao đổi trực tiếp 1-1. Đầu mối chính bên product: anh Quân.

### 2.4 Weekly/Monthly report liên quan
- **CS Weekly (Chatty)** — volume, bot performance, DFY, top issues → Notion + Slack digest nhóm CS.
- **DFY Weekly (Chatty)** — report cho lãnh đạo (PM + anh Sam) — Inbound vs Proactive, adopt rate, DFY/install.
- **DFY Tracker (tháng)** — KPI Point theo CS.
- **CEO Weekly** (gộp Chatty+Joy) — gửi anh Sam trước họp thứ 2.
- **CS Daily brief** — báo Liz hàng ngày, chỉ bung khi có gì bất thường.

### 2.5 Crisis management khi có bad review
- Process gốc: `kb/cs-process/shared-cs-process/handle-complaints.md` — SLA phản hồi **2 giờ**, 7 bước (respond nhanh → professional → tìm root cause → nhận trách nhiệm → đề xuất giải pháp/compensation → follow through → document).
- **Escalate lên CS Leader (Slack) khi:** đã thử 2 lần vẫn còn giận · merchant đe doạ pháp lý · đe doạ để lại review xấu công khai · liên quan refund/compensation · merchant VIP.
- Report tuần có mục riêng theo dõi bad review (≤3★) trong tuần, so với tuần trước.

### 2.6 Training CS Chatty
- Onboarding CS mới + đào tạo kỹ năng theo 2 track đã định nghĩa trong CS Transformation Plan (`playbooks/cs-transformation/chatty-transformation.md`): **AI Monitor** (Hazel/Phoebe — đọc AI trả lời, sửa training data) và **AM/Onboarding Call** (Andy/Jade — call, proactive check-in).
- Andy đã tự đi qua track AM nên có thể trực tiếp đào tạo CS mới ở track này; track AI Monitor Liz vẫn dẫn dắt chính.
- Hiện Chatty chưa có skill chấm test/grading riêng cho trainee (Joy đã có `/grade-joy-trainee`, Chatty chưa) — phần này để Liz cân nhắc có cần build tương tự hay không.

### 2.7 Họp team hàng tuần
- Andy tham gia điều phối cùng Liz — chuẩn bị nội dung từ các mục 2.1–2.6 (chỉ số app, CS performance, tiến độ project, crisis nếu có, training) để đưa vào agenda họp team Chatty.

### 2.8 Xử lý tình huống khó, KH high-risk, refund/billing escalation
- **Escalation matrix** (`kb/cs-process/shared-cs-process/escalation-matrix.md`): refund request, merchant giận sau 2 lần xử lý, VIP merchant, policy exception → escalate CS Leader ngay qua Slack/Trello. Andy là điểm nhận escalation đầu tiên thay Liz cho các case này; case vượt thẩm quyền (số tiền lớn, VIP đặc biệt, policy exception chưa có tiền lệ) vẫn cần Liz duyệt cuối.
- **Billing/refund:** theo `kb/cs-process/shared-cs-process/handle-billing-refund.md` + `handle-billing.md`.
- **Tình huống nhạy cảm khác:** `handle-sensitive-situations.md` / `sensitive-situations.md`.
- **Discount request (xin giảm giá):** theo `handle-discount-requests.md` — có promotion đang chạy thì CS tự xử lý; không có promotion thì escalate xin duyệt.
- **Tạo discount code:** thao tác tạo code thật (Shopify/billing system) — Liz sẽ hướng dẫn trực tiếp/thao tác mẫu cho Andy vì hiện chưa có doc ghi lại quy trình kỹ thuật, chỉ có policy khi nào được tạo.

---

## 3. Việc Andy nhận trước (đã chốt với Liz)

**Andy nhận ngay:**
1. **Theo dõi chỉ số app nói chung** — review, chat, install (2.1)
2. **CS performance** — QA, bot corrections, DFY point, bot resolved % (2.2)
3. **Crisis management** khi có bad review (2.5)
4. **Training CS Chatty** — riêng track AM (2.6)
5. **Họp team hàng tuần** (2.7)
6. **Xử lý tình huống khó, KH high-risk, refund/billing escalation** — kể cả tạo discount code (2.8, Liz hướng dẫn thao tác tạo code trực tiếp trước khi Andy tự làm)

**Chưa nhận vội — chờ doc/meeting riêng:**
- **CS AI agent** và **TS AI agent** (2.3) — Liz sẽ gửi doc chi tiết hơn hoặc set 1-1 để Andy nắm kiến trúc/flow trước khi nhận việc liên quan.

**Andy KHÔNG cần đụng vào** (Liz vẫn giữ): điều phối cross-team (PM/Tech Lead Tesla), duyệt cuối các case vượt thẩm quyền (refund/policy exception lớn, VIP đặc biệt).

---

*Cập nhật doc này khi có thay đổi role/scope — nhớ đồng bộ `_identity/team-g2.md` nếu Andy đổi title chính thức.*
