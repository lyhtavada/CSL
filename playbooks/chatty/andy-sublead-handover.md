# Chatty CS — Handover cho Andy (Sublead)

**Mục đích:** Andy lên làm sublead hỗ trợ Liz quản lý CS team Chatty. Doc này tổng hợp toàn bộ task Liz đang follow up cho Chatty — để Andy pick up dần, không cần hỏi lại từ đầu.

**Ngày viết:** 2026-09-17 | **Owner gốc:** Liz (CSL) | **Scope:** Chatty only (Joy Andy không cần theo)

---

## 1. Bối cảnh nhanh

Liz là CS Leader phụ trách 3 app (Chatty, Joy Loyalty, Joy Wishlist), báo cáo anh Sam (CEO). Andy đã quen Chatty từ **CS Transformation Plan** — track **AM/Onboarding Call** cùng Jade (xem `playbooks/cs-transformation/chatty-transformation.md`), và là CS đầu tiên chạy pilot **Proactive DFY** (mục 3 dưới đây) từ 2026-06-23. Việc lên sublead là mở rộng từ track đó, không phải bắt đầu lại.

**Team Chatty (in-house, roster đầy đủ ở `_identity/team-g2.md`):**
| Tên | Nickname KPI | Slack | Vai trò hiện tại |
|---|---|---|---|
| Bùi Đức Anh | AnhBD (Andy) | U09DC212XN0 | Sublead (mới) + AM track + Proactive DFY pilot |
| Nguyễn Thị Phương | PhuongNT (Jade) | U07CGHSHNMB | AM track, Proactive Care (Pro+Plus) |
| Phạm Thu Hiền | HienPT (Hazel) | U09FYACFH2T | AI Monitor, Proactive Care |
| Trương Lê Khánh Linh | LinhTLK (Linda) | U0AHSHQU59T | CS Chatty, Proactive Care |
| Trần Thị Mai Phương | PhuongTTM (Phoebe) | U0A84BE00FK | AI Monitor |
| Bùi Tuyết Minh | MinhBT (Mirra) | U08GX75N5CZ | Remote, part-time |
| Hoàng Minh Châu | ChauHM (Cody) | U08TZM2LL74 | Remote, part-time |

**Đầu mối product Chatty (Team Tesla):**
- PM: Quách Thanh Tùng (`tungqt@avada.io`, Slack U01NJA7R38C)
- Tech Lead: Vũ Minh Đạt (`datvm@avada.io`, Slack U01N91ZKMK7)
- Bug report AI (classifier/guard/retrieval trên cs2) → gửi **Fennic** (Slack U01N91HCC3F), KHÔNG gửi Đạt/PM.

---

## 2. Task đang follow up — chi tiết theo mức ưu tiên

### 2.1 🔴 KB audit sau UI restructure (đang làm dở, ưu tiên cao nhất)
Chatty đổi UI 2 lần trong tháng 8/2026 (Chatbox tách AI Mode/Legacy, AI agent page dựng lại thành bento hub — Skills/Scenarios tách trang riêng). Slack release notes **không** nhắc 2 thay đổi này nên KB cũ bị stale nhiều chỗ.

- **Đã xong:** 6/21 file đã patch + push + reindex (2026-09-03): `chatbox-settings.md`, `ai-agent-settings.md`, `human-handover.md`, `ai-training-setup.md`, `train-ai.md`, `product-quiz.md`.
- **Còn lại 15 file** — priority:
  - 🔴 Critical: `kb/reference/knowledge-base.md`, `kb/faq/knowledge-base.md`, `persona/facts.md`
  - 🟠 Case files lớn: `kb/case/ai-wrong-responses.md` (18 ref stale, file to nhất), `kb/case/chatbox-widget-issues.md`
  - 🟡 Nhỏ (1-3 ref): `kb/faq/live-chat.md`, `embedded-chatbox.md`, `deep-links.md`, `inbox.md`, `general-settings.md`, `klaviyo.md`, `data-sources.md`, `flows/done_for_you.md`, `kb/case/ai-sync-issues.md`, `kb/case/translation-issues.md`
- **Cách làm:** đường dẫn UI mới đã verify sẵn từ source code, không cần đào lại. Chạy `skills/kb-sync/scripts/prep.py chatty` refresh cache → patch theo flow `/product-kb-sync` (draft → Liz duyệt → push + reindex).
- **Chưa làm:** `/kb-test` cho cả batch (chưa chạy lần nào trong 3 lần push trước) — nên chạy sau khi xong 15 file còn lại.
- Chi tiết: memory `chatty_ui_restructure_kb_audit.md`.

### 2.2 🟠 Chatty Proactive Care — thiết kế AM-style check-in cho Pro+Plus (đang viết spec)
Mục tiêu: CS chủ động follow-up KH Pro (623 shop) + Plus (39 shop) thay vì chỉ reactive.

- **Đã quyết (2026-06-17):** 4 CS in-house tham gia — **Andy, Jade, Hazel, Linda**. Plus assign cố định (~10/người); Pro không assign cứng, dùng trigger (mới upgrade, low usage, nguy cơ churn, ticket căng, AI kém) → care queue → xoay ca 4 CS.
- **Track:** mỗi lần chạm = tạo ticket Avada Ticket (tag `proactive-care`, appName Chatty) → nối vào KPI/DFY, đo retention nhóm chăm vs không.
- **Còn thiếu:** skill `/chatty-care` + cron chưa dựng (theo pattern `cs-weekly`/`dfy-weekly-chatty`). Đây là phần Andy có thể giúp đẩy tiếp — vì Andy/Jade/Hazel/Linda chính là 4 người sẽ chạy.
- Full spec: `playbooks/chatty/chatty-proactive-care.md`.

### 2.3 🟢 Chatty Proactive DFY Pilot — đang chạy, Andy đã biết rõ
Andy chính là CS pilot ban đầu (bắt đầu 2026-06-23, 4 ca/tuần). Flow: lấy list KH mới cài ≤14 ngày + Pro/Plus từ bảng analytics public → audit store → viết email cá nhân hoá → tạo ticket ngay (tag `DFY-new` + `proactive`).
- Bảng nguồn: `https://analytics.avada.net/public/views/sytCf8kfby3J5Yknohqa` (tự refresh 1h).
- Full SOP: `playbooks/chatty/chatty-proactive-dfy-pilot.md`.
- **Andy nên bàn giao/nhân rộng phần này cho CS khác** giờ đã lên sublead — nếu định mở rộng pilot sang Jade/Hazel/Linda thì hợp nhất luôn với Proactive Care (2.2), vì cùng đối tượng Pro/Plus.

### 2.4 🟡 CS Transformation — theo dõi trigger chuyển phase
`playbooks/cs-transformation/chatty-transformation.md` — team đang ở giữa Phase 2 (AI Pilot). Trigger chuyển Phase 3 (Scale Down): **AI resolved ≥ 60%** đo bằng `aiResolvedPct` trên `cs2.avada.net /api/obs/metrics` (KHÔNG dùng công thức cũ đã bỏ 11/08).
- Số mới nhất (tuần 07-13/09): Ivy AI resolved **54.5%** — vẫn **chưa đạt** mốc 60%.
- Khi đạt: Hazel/Phoebe chuyển từ real-time monitor → async; Andy/Jade tăng call volume + bắt đầu xử lý expansion/upsell.
- KPI framework mới (AM: call completed, conversion, retention...) đã có sẵn trong file, áp dụng khi qua Phase 3.

### 2.5 🔵 Nhịp báo cáo/vận hành định kỳ Chatty (đã chạy ổn, Andy cần biết để không hỏi lại)
| Việc | Nhịp | Note |
|---|---|---|
| `/cs-weekly` (Chatty) | T2 9:00 (cron) | Volume, bot performance, DFY, top issues → Notion + Slack digest nhóm CS |
| `/dfy-weekly-chatty` | T6 16:30 (cron) | Report DFY cho lãnh đạo (PM + anh Sam), Inbound vs Proactive, adopt rate |
| `/dfy-tracker` (Chatty) | Ngày 2 đầu tháng | KPI Point theo CS — Chatty tính theo % task/block (AI 50/Chatbox 30/Video 50, max 130p) |
| `/bot-corrections` (Chatty) | T2-T6 15:00 | Câu Ivy bị CS sửa, để update KB/training |
| `/product-kb-sync` (Chatty) | T3+T6 10:00 | Sync KB theo release/GitLab diff |
| `/qa-weekly` | T4 14:00 | Chấm QA 3 trục (Mindset/Knowledge/Skill) cho team G2, gồm Andy/Jade/Hazel/Linda |
| `/reply-reviews` | T3+T6 17:00 | Draft reply App Store/Play Store, Liz duyệt trước khi post |
| `/cs-daily-brief` | Hàng ngày 10:00 | DM Liz, exception-only (chỉ bung khi có gì bất thường) |

Andy không cần chạy các skill này — chỉ cần biết chúng tồn tại để không tự hỏi "sao số này ở đâu ra" và biết dòng dữ liệu chảy về đâu (Notion CS Weekly, Slack digest nhóm CS).

---

## 3. Việc Andy nên nhận trước (đề xuất, Liz confirm lại)

1. **KB audit (2.1)** — mảng lớn nhất còn dở, không cần escalate nhiều, chỉ cần thời gian + review pattern đã có sẵn.
2. **Proactive Care (2.2)** — Andy là 1 trong 4 người sẽ chạy, nên hợp lý để Andy giúp hoàn thiện thiết kế/khởi động thay vì chờ Liz build xong mới học.
3. **Theo dõi mốc AI resolved 60%** (2.4) — để chủ động chuẩn bị team chuyển nhịp làm việc (AM track tăng tải) khi tới ngưỡng, không bị động.
4. Việc **KHÔNG cần Andy đụng vào** (Liz vẫn giữ): điều phối cross-team (PM/Tech Lead Tesla), review KPI/point cuối tháng, quyết định escalation VIP/refund.

---

*Cập nhật doc này khi có thay đổi role/scope — nhớ đồng bộ `_identity/team-g2.md` nếu Andy đổi title chính thức.*
