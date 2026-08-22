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
**Người chuyển đổi (subject của transition, không phải PIC):** 4 CS full-time của **Joy** — **Alyssa, Audrey, Sonny, Ethan**.

---

## Workstream A — Salary Structure (AM role)

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| A1 | Benchmark salary AM tại các công ty SaaS tương đương (thị trường VN, remote) | Daisy | TBD | Not started | |
| A2 | Định nghĩa base + biến động (commission/bonus theo retention, upsell, CSAT) | Liz | TBD | Not started | |
| A3 | Map level (Junior/Senior AM) với band lương hiện tại của CS để tránh lệch thang | Liz | TBD | Not started | |
| A4 | Trình phê duyệt structure | Liz | TBD | Not started | cần Sam duyệt |
| A5 | Communicate structure mới cho Alyssa/Audrey/Sonny/Ethan (4 CS Joy full-time chuyển sang AM) | Liz | TBD | Not started | đối tượng: CS team, không phải PIC |

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

## Workstream D — Data & Tracking

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| D1 | Track merchant nào thuộc tier nào (Free/Essential vs Advanced/Ultimate) | Daisy | TBD | Not started | |
| D2 | Track volume ticket theo tier | Daisy | TBD | Not started | |
| D3 | Track AM workload (số account/AM) | Liz | TBD | Not started | cần trước khi go-live để biết capacity |

---

## Workstream E — Timeline & Rollout

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| E1 | Chốt 1 mốc go-live chung cho toàn bộ transition | Liz | TBD | Not started | |
| E2 | Pilot 1 tháng với 1 AM + subset merchant Ultimate | Liz + Daisy | TBD | Not started | |
| E3 | Review kết quả pilot trước khi roll toàn bộ | Liz | TBD | Not started | phụ thuộc E2 |

---

## Workstream F — Training

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| F1 | Lên lịch training/shadow với Avada AM team | Liz | TBD | Not started | |
| F2 | Alyssa/Audrey/Sonny/Ethan shadow thực tế trước khi go-live | Liz | TBD | Not started | AM là role mới cho tất cả, không chỉ JD suông |

---

## Workstream G — Risk & Rollback

| # | Task | PIC | Deadline | Status | Note |
|---|------|-----|----------|--------|------|
| G1 | Định nghĩa risk case: Free/Essential merchant phản ứng tiêu cực khi mất live chat | Liz | TBD | Not started | |
| G2 | Chuẩn bị plan B (vd. tạm giữ live chat giờ cao điểm) | Liz | TBD | Not started | trigger khi G1 xảy ra |

---

## Next step

1. Update bảng "Team Role Assignment — Joy Loyalty" trong `cs-transformation-plan.md` cho khớp danh sách AM mới (Alyssa, Audrey, Sonny, Ethan) — bản hiện tại đang sai (thiếu Ethan, có Audrey là AI Monitor Lead thay vì AM).
2. Liz + Daisy điền deadline cụ thể cho từng task ở trên.
3. Update `cs-transformation-plan.md` → Open Questions section: đánh dấu "Budget/tools for AM" đã có plan chi tiết ở đây (link qua lại).
4. Sau khi chốt, có thể tách từng workstream (A–G) thành ticket/task riêng để track tiến độ nếu cần.
