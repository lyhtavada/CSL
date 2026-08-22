# CS → AM Transition — Execution Plan

**Status:** Draft — Liz + Daisy điền deadline
**Owner:** Liz (CS Leader), **Co-PIC:** Daisy
**Created:** 2026-08-22
**Parent plan:** [cs-transformation-plan.md](cs-transformation-plan.md) — this doc executes the "AM role" + open-questions items from that plan (budget/tools for AM, remote agent comms) into concrete tasks with PIC and deadline.

---

## Context

CS team đang chuyển từ live chat 24/7 → mô hình phân tầng theo plan:
- **Free / Essential** → ticket-based support (không live chat 24/7)
- **Advanced / Ultimate** → AM (Account Manager) phụ trách, quan hệ 1:1

3 đầu việc chính cần làm song song: (1) salary structure vị trí AM mới, (2) job description, (3) chuyển đổi tool/process từ live chat sang ticket.

**PIC của kế hoạch này (build/design):** chỉ **Liz** và **Daisy**.
**Người chuyển đổi (subject của transition, không phải PIC):** các bạn CS hiện tại — theo `cs-transformation-plan.md` là Andy/Jade/Sonny/Alyssa (Chatty + Joy) đang được gán role AM. PIC nào cần duyệt cùng Sam thì đánh dấu riêng ở cột Note.

---

## Workstream A — Salary Structure (AM role)

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| A1 | Benchmark salary AM tại các công ty SaaS tương đương (thị trường VN, remote) | Daisy | TBD | Not started | |
| A2 | Định nghĩa base + biến động (commission/bonus theo retention, upsell, CSAT) | Liz | TBD | Not started | |
| A3 | Map level (Junior/Senior AM) với band lương hiện tại của CS để tránh lệch thang | Liz | TBD | Not started | |
| A4 | Trình phê duyệt structure | Liz | TBD | Not started | cần Sam duyệt |
| A5 | Communicate structure mới cho các CS được chọn chuyển sang AM | Liz | TBD | Not started | đối tượng: CS team, không phải PIC |

**Câu hỏi cần chốt trước khi làm A2:** AM có gắn commission theo retention/upsell không, hay giữ fixed salary như CS hiện tại? (ảnh hưởng lớn tới cách tính band)

---

## Workstream B — Job Descriptions

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| B1 | JD cho **AM** (Advanced/Ultimate) — trách nhiệm: onboarding call, health check định kỳ, upsell/renewal, escalation cho merchant tier cao | Daisy | TBD | Not started | |
| B2 | JD update cho **CS/Ticket handler** (Free/Essential) — trách nhiệm: xử lý ticket + AI monitor, không còn live chat trực | Liz | TBD | Not started | |
| B3 | Định nghĩa rõ ranh giới: case nào Ticket handler escalate lên AM, case nào AM tự xử lý | Liz | TBD | Not started | |
| B4 | Review JD trước khi công bố nội bộ | Liz + Daisy | TBD | Not started | cần Sam duyệt |
| B5 | Công bố JD mới cho team, gắn với KPI framework mới (đã note ở cs-transformation-plan.md checklist "Design new KPI framework for each role") | Liz | TBD | Not started | đối tượng công bố: CS team |

---

## Workstream C — Live Chat 24/7 → Ticket Transition (tooling & process)

### C1. Free / Essential → Ticket-only

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| C1.1 | Xác nhận tool ticket hiện tại (Avada Ticket API) đủ chức năng cho merchant tier thấp tự tạo ticket, hay cần build thêm form/portal | Daisy | TBD | Not started | cần dev/PM confirm khả năng build |
| C1.2 | Tắt/giới hạn live chat entry point cho Free/Essential trên widget (chỉ hiện AI + nút "Create a ticket") | Daisy | TBD | Not started | thực thi kỹ thuật do dev, Daisy theo dõi/spec |
| C1.3 | Định nghĩa SLA phản hồi ticket cho tier này (khác SLA live chat cũ) | Liz | TBD | Not started | |
| C1.4 | Update `kb/cs-process/` support flow docs phản ánh flow mới (bỏ nhánh live chat 24/7 cho tier thấp) | Liz | TBD | Not started | |
| C1.5 | Thông báo merchant hiện tại về đổi kênh support (email/in-app announcement) | Daisy | TBD | Not started | |

### C2. Advanced / Ultimate → AM-led

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| C2.1 | Chốt tool AM cần: CRM/scheduling cho onboarding call + health check (đã list ở open question trong cs-transformation-plan.md — chưa có answer) | Liz + Daisy | TBD | Not started | cần Sam duyệt budget |
| C2.2 | Setup call scheduling tool (Calendly/Google Calendar — đã có `gapi` calendar access sẵn, có thể tận dụng) | Daisy | TBD | Not started | |
| C2.3 | Setup call recording/notes tool nếu cần (tuân thủ policy ghi âm với merchant) | Daisy | TBD | Not started | |
| C2.4 | Định nghĩa health-check cadence cho AM (vd. touch point mỗi X tuần cho Ultimate, mỗi X tuần cho Advanced) | Liz | TBD | Not started | |
| C2.5 | Merchant tier Advanced/Ultimate vẫn cần fallback chat/ticket khi AM offline — định nghĩa coverage | Liz | TBD | Not started | |

---

## Gợi ý bổ sung (chưa có trong yêu cầu gốc, nên cân nhắc thêm)

- **D. Data & tracking:** Cần track được: merchant nào thuộc tier nào (Free/Essential vs Advanced/Ultimate), volume ticket theo tier, AM workload (số account/AM) — nếu chưa có, thêm task xây dashboard/report trước khi go-live.
- **E. Timeline & rollout plan:** Hiện các task đều "TBD" — nên chốt 1 mốc go-live chung (vd. pilot 1 tháng với 1 AM + subset merchant Ultimate trước khi roll toàn bộ).
- **F. Training:** AM là role mới cho tất cả (đã note trong cs-transformation-plan.md) — cần lịch training/shadow với Avada AM team trước khi go-live, không chỉ JD suông.
- **G. Risk/rollback:** Nếu Free/Essential merchant phản ứng tiêu cực với việc mất live chat, cần plan B (vd. tạm thời vẫn cho chat giờ cao điểm).

Đề xuất gộp D–G vào bảng task ở trên sau khi Liz xác nhận scope, và gắn PIC/deadline cụ thể (hiện tại đang để TBD vì cần Liz + Sam chốt).

---

## Next step

1. Liz điền PIC cụ thể (tên người) + deadline cho từng task ở trên.
2. Update `cs-transformation-plan.md` → Open Questions section: đánh dấu "Budget/tools for AM" đã có plan chi tiết ở đây (link qua lại).
3. Sau khi chốt, có thể tách từng workstream (A/B/C) thành ticket/task riêng để track tiến độ nếu cần.
