# Chatty CS — Handover cho Andy (Sublead)

**Mục đích:** Andy lên làm sublead hỗ trợ Liz quản lý CS team Chatty. Doc này tổng hợp toàn bộ task Liz đang follow up cho Chatty — để Andy pick up dần, không cần hỏi lại từ đầu.

**Ngày viết:** 2026-09-17 | **Owner gốc:** Liz (CSL) | **Scope:** Chatty only (Joy Andy không cần theo)

---

## 1. Bối cảnh nhanh

Liz là CS Leader phụ trách 3 app (Chatty, Joy Loyalty, Joy Wishlist), báo cáo anh Sam (CEO). Andy đã quen Chatty từ **CS Transformation Plan** — track **AM/Onboarding Call** cùng Jade (xem `playbooks/cs-transformation/chatty-transformation.md`), và là CS đầu tiên chạy pilot **Proactive DFY** từ 2026-06-23. Việc lên sublead là mở rộng từ track đó, không phải bắt đầu lại.

**Team Chatty (in-house, roster đầy đủ ở `_identity/team-g2.md`):**
| Tên | Nickname KPI | Slack | Vai trò hiện tại |
|---|---|---|---|
| Bùi Đức Anh | AnhBD (Andy) | U09DC212XN0 | Sublead (mới) + AM track + Proactive DFY pilot |
| Nguyễn Thị Phương | PhuongNT (Jade) | U07CGHSHNMB | AM track |
| Phạm Thu Hiền | HienPT (Hazel) | U09FYACFH2T | AI Monitor |
| Trương Lê Khánh Linh | LinhTLK (Linda) | U0AHSHQU59T | CS Chatty |
| Trần Thị Mai Phương | PhuongTTM (Phoebe) | U0A84BE00FK | AI Monitor |
| Bùi Tuyết Minh | MinhBT (Mirra) | U08GX75N5CZ | Remote, part-time |
| Hoàng Minh Châu | ChauHM (Cody) | U08TZM2LL74 | Remote, part-time |

**Đầu mối product Chatty (Team Tesla):**
- PM: Quách Thanh Tùng (`tungqt@avada.io`, Slack U01NJA7R38C)
- Tech Lead: Vũ Minh Đạt (`datvm@avada.io`, Slack U01N91ZKMK7)
- Bug report AI (classifier/guard/retrieval trên cs2) → gửi **Fennic** (Slack U01N91HCC3F), KHÔNG gửi Đạt/PM.

---

## 2. Đầu việc đang follow up cho Chatty

### 2.1 Theo dõi chỉ số app nói chung — review, chat, install
- **Review App Store (Shopify):** `/count-reviews` — đếm ad-hoc theo tháng/khoảng ngày, dùng scraper đã validate (KHÔNG dùng MCP `avada-analytic` hay đếm tay trên listing, cả 2 đều sai số).
- **Review mobile app (iOS/Play Store):** `/reply-reviews` — fetch review chưa reply, draft theo tone, **Liz duyệt trước khi post**, cron T3+T6 17:00 gửi draft qua Telegram, không bao giờ tự post.
- **Chat volume:** `/count-chats` — đếm conversation thật (sessionize theo merchant, loại traffic nội bộ Avada), logic dùng chung với `/cs-weekly` nên số luôn khớp report tuần.
- **Install:** không có skill riêng — số install lấy từ `dash_merchant_360` (BigQuery, app_id `avadaFaq`), hiện đang dùng làm mẫu số cho tỷ lệ DFY/install trong `/dfy-weekly-chatty`.

### 2.2 CS Performance
- **QA:** `/qa-weekly` (cron T4 14:00) — chấm 3 trục Mindset/Knowledge/Skill cho từng CS G2 (gồm Andy/Jade/Hazel/Linda) từ chat thật, DM kết quả sau khi Liz duyệt. `/qa-cs` = bản QA tháng, chấm theo policy/penalty (`playbooks/qa/`).
- **Bot corrections (để đo CS có đang train bot đúng không):** `/bot-corrections` — T2-T6 15:00, gom câu Ivy bị CS sửa theo topic + người sửa, feed vào KB/training.
- **DFY point (KPI tháng):** `/dfy-tracker` — Chatty tính theo % task hoàn thành/block (AI 50 + Chatbox 30 + Video 50 = max 130p), chạy ngày 2 đầu tháng.
- **Bot performance (context để hiểu tải CS):** AI resolved % (`aiResolvedPct`, cs2 `/api/obs/metrics`) — mốc cần theo dõi: **≥60%** để chuyển Phase 3 CS Transformation (Hazel/Phoebe async hoá, Andy/Jade tăng tải AM). Hiện tại (tuần 07–13/09): Ivy **54.5%** — chưa đạt.

### 2.3 Project đang triển khai

**DFY**
- **Proactive DFY Pilot** — Andy đang chạy trực tiếp (từ 2026-06-23, 4 ca/tuần): lấy list KH mới cài ≤14 ngày + Pro/Plus từ bảng analytics public (`https://analytics.avada.net/public/views/sytCf8kfby3J5Yknohqa`, tự refresh 1h) → audit store → viết email cá nhân hoá → tạo ticket ngay (tag `DFY-new` + `proactive`). Full SOP: `playbooks/chatty/chatty-proactive-dfy-pilot.md`.
- **DFY thường (reactive)**: flow + checklist ở `playbooks/chatty/chatty-dfy-flow.md`.
- Andy đã nắm rõ mảng này — có thể cân nhắc nhân rộng pilot sang Jade/Hazel/Linda khi phù hợp.

**CS AI agent** (Ivy/Joyce trên `cs2.avada.net`)
- Liz sẽ gửi doc chi tiết riêng hoặc trao đổi trực tiếp 1-1 để Andy nắm kiến trúc/flow đầy đủ.
- Việc liên quan đang chạy song song: KB audit sau UI restructure Chatty (Chatbox tách AI Mode/Legacy, AI agent page dựng lại bento hub Skills/Scenarios) — 6/21 file đã patch, 15 file còn lại, chưa chạy `/kb-test` cho cả batch. Chi tiết ở memory `chatty_ui_restructure_kb_audit.md`, làm theo flow `/product-kb-sync`.

**TS AI agent** (`ts2.avada.net` — TS Elite v1 đang chạy thật, TS AI Agent v2 đang xây để thay thế)
- Liz sẽ gửi doc chi tiết riêng hoặc trao đổi trực tiếp 1-1. Đầu mối chính bên product: anh Quân.

### 2.4 Weekly/Monthly report liên quan
| Report | Nhịp | Nội dung |
|---|---|---|
| `/cs-weekly` (Chatty) | T2 9:00 (cron) | Volume, bot performance, DFY, top issues → Notion + Slack digest nhóm CS |
| `/dfy-weekly-chatty` | T6 16:30 (cron) | Report DFY cho lãnh đạo (PM + anh Sam) — Inbound vs Proactive, adopt rate, DFY/install |
| `/dfy-tracker` (Chatty) | Ngày 2 đầu tháng | KPI Point theo CS |
| CEO Weekly (gộp Chatty+Joy) | T2 13:00, trước họp 15:00 | `reports/weekly/ceo-weekly-*.md`, gửi anh Sam |
| `/cs-daily-brief` | Hàng ngày 10:00 | DM Liz, exception-only |

### 2.5 Crisis management khi có bad review
- Process gốc: `kb/cs-process/shared-cs-process/handle-complaints.md` — SLA phản hồi **2 giờ**, 7 bước (respond nhanh → professional → tìm root cause → nhận trách nhiệm → đề xuất giải pháp/compensation → follow through → document).
- **Escalate lên CS Leader (Slack) khi:** đã thử 2 lần vẫn còn giận · merchant đe doạ pháp lý · đe doạ để lại review xấu công khai · liên quan refund/compensation · merchant VIP.
- Report tuần (`/cs-weekly`) có mục riêng **🚨 Crisis (Bad Reviews)** — tự flag bad review ≤3★ trong tuần, so tuần trước. Reply review thật (App Store/Play Store) qua `/reply-reviews`.

---

## 3. Việc Andy nhận trước (đã chốt với Liz)

**Andy nhận ngay:**
1. **Theo dõi chỉ số app nói chung** — review, chat, install (2.1)
2. **CS performance** — QA, bot corrections, DFY point, bot resolved % (2.2)
3. **Crisis management** khi có bad review (2.5)

**Chưa nhận vội — chờ doc/meeting riêng:**
- **CS AI agent** và **TS AI agent** (2.3) — Liz sẽ gửi doc chi tiết hơn hoặc set 1-1 để Andy nắm kiến trúc/flow trước khi nhận việc liên quan.

**Andy KHÔNG cần đụng vào** (Liz vẫn giữ): điều phối cross-team (PM/Tech Lead Tesla), quyết định escalation VIP/refund cuối cùng.

---

*Cập nhật doc này khi có thay đổi role/scope — nhớ đồng bộ `_identity/team-g2.md` nếu Andy đổi title chính thức.*
