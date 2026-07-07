# Joy Loyalty — Onboarding Flow (Phase 1: CS-offer trong chat)

**Owner:** Liz (CS Leader)
**Created:** 2026-07-07
**Status:** Draft v1 — Phase 1 (CS chủ động offer trong chat). Phase 2 (trigger tự động trong app) để sau.

> Khác gì với [`joy-dfy-flow.md`](./joy-dfy-flow.md)?
> DFY hiện tại thiên về **làm hộ widget + đẩy go-live** cho store đã install & gần xong.
> **Onboarding flow này** dành cho KH **Advanced plan** cần **build cả loyalty program từ đầu** (earning / redeeming / VIP / member-guest / migration / import data) — có discovery đầu vào, có checklist chuẩn, 1 ticket sống/KH xuyên suốt.

---

## 0. Mục tiêu & phạm vi

**Mục tiêu Phase 1:** CS **chủ động offer** hỗ trợ onboarding cho KH đang ở **Advanced plan** ngay trong chat → đưa họ từ "vừa lên plan / chưa có program" đến **launch được program đúng ý** (earning + redeeming + VIP + member/guest), có hoặc không migration.

**Phase roadmap:**
- **Phase 1 (bản này):** CS trực tiếp offer trong chat.
- **Phase 2 (sau):** trigger tự động trong app khi KH lên Advanced / mới install → nudge onboarding.

**Nguyên tắc xuyên suốt:** mỗi KH = **1 ticket onboarding chính**. Mọi issue phát sinh trong quá trình onboard (bug, câu hỏi, report tiến độ) **note thẳng vào ticket đó**, không tách lẻ. Ngoại lệ duy nhất: **widget customize** → tạo ticket con riêng nhưng **insert link vào ticket chính** (xem §5).

---

## 1. Eligibility — Khi nào CS offer

CS offer onboarding khi **cả 2** đúng:

1. **Plan = Advanced trở lên** (đây là scope Phase 1 — KH giá trị cao, đáng đầu tư setup full).
2. Store thuộc ít nhất một nhóm:
   - **Mới lên Advanced / mới install**, chưa có program hoàn chỉnh
   - **Chưa launch** — chưa có earning/redeeming active, hoặc còn sandbox
   - **Đang hỏi trong chat** về cách setup earning / redeem / VIP / migrate / import

**KHÔNG offer lại** nếu KH đã có ticket onboarding đang mở → update ticket cũ.

---

## 2. Mở đầu — CS offer + Discovery (trong chat)

### 2.1 Câu offer
> *"Hi [name], I noticed you're on our Advanced plan — I'd love to help you get your loyalty program set up properly so it's ready to launch. Would you like me to walk through it with you and set things up together?"*

### 2.2 Discovery — 3 câu hỏi mở đầu (đừng hỏi dồn 1 lúc)
Mục tiêu: biết **timeline**, **kinh nghiệm loyalty trước đó**, và **có phải migrate không**.

1. **Launch timeline:** *"When are you planning to launch your loyalty program?"*
2. **Kinh nghiệm trước đó:** *"Have you run a loyalty program before — either on another app or store?"*
3. **(Nếu có dùng trước đó) Migration:** *"Are you moving over from another loyalty app? If so, do you already have your customer/points data exported?"*

> Từ 3 câu này → CS xác định nhánh ở §3 và điền phần đầu checklist (launch date + migration).

---

## 3. Decision tree — Phân nhánh theo tình huống KH

```
KH mới ở Advanced
        │
        ├── A. MIGRATE từ app loyalty khác sang
        │        ├── A1. Đã có detailed plan  → xin KH gửi plan → CS review + setup theo → test
        │        └── A2. Chưa có plan rõ       → gửi checklist Google Sheet → KH điền rule
        │                                          (KH chưa biết → hướng dẫn dùng AI agent trong app)
        │        + Luôn hỏi: có sẵn data export chưa? cần import kiểu gì?
        │
        ├── B. ĐÃ dùng loyalty trước (không migrate app / build lại từ đầu)
        │        ├── B1. Đã có plan/rule sẵn   → gửi CS → CS review + setup giúp → test
        │        └── B2. Chưa có plan rõ       → gửi checklist Google Sheet → KH điền
        │
        └── C. CHƯA từng dùng loyalty bao giờ
                 → CS gợi ý preset theo ngành/AOV
                 → hỗ trợ KH dùng AI agent trong app (đọc AOV, industry…) để đề xuất rule
                 → chốt rule → CS setup → test
```

### 3.1 Nhánh A — Migrate từ app khác
- **A1 — có detailed plan:** xin KH **gửi plan** cho CS (link/doc). CS **review** → set kỳ vọng → **setup giúp** theo plan → **test** → báo KH verify.
- **A2 — chưa có plan:** gửi **checklist Google Sheet** (§4) → KH điền rule. KH chưa biết điền gì → **hướng dẫn dùng AI agent trong app** (đọc AOV / industry để gợi ý).
- **Data (luôn hỏi cả A1/A2):**
  - KH đã **export data** từ app cũ chưa? (point balance, member list, tier)
  - Cần **import** kiểu gì? Format nào? → nếu phức tạp/khối lượng lớn → forward TS.
  - ⚠️ Chốt rõ: **point balance migrate được tới đâu** — đây là điểm dễ vỡ nhất của migrate, set kỳ vọng sớm.

### 3.2 Nhánh B — Đã dùng loyalty nhưng không migrate app
- **B1 — có plan sẵn:** KH gửi plan → CS **review + setup giúp** → test.
- **B2 — chưa có plan:** gửi **checklist Google Sheet** → KH điền → CS setup → test.

### 3.3 Nhánh C — Chưa từng dùng loyalty
- CS **gợi ý thêm**: dựa vào **ngành + AOV** để đề xuất preset earning/redeeming an toàn.
- Hỗ trợ KH bật **AI agent trong app** (đọc AOV, industry…) để tự sinh gợi ý rule.
- Chốt rule cùng KH → CS setup → test.

---

## 4. Checklist Google Sheet (KH điền rule)

> CS tạo **1 Google Sheet checklist** làm template dùng chung → mỗi KH clone/điền → paste link vào ticket chính (field "detail program"). KH điền rule; KH chưa biết → CS gợi ý / dùng AI agent trong app.

Nội dung sheet (KH điền):
- **Launch date** dự kiến
- **Earning rules** — ways to earn + point value (vd signup, place order, review, birthday…)
- **Redeeming rules** — ways to redeem + đổi điểm ra gì (discount, free ship, product…)
- **VIP tier** (nếu có) — số tier, ngưỡng, perk mỗi tier
- **Member vs Guest** — guest thấy/làm được gì, member khác gì
- **Migration / Import** — app cũ nào, data có sẵn chưa, format
- **Ghi chú riêng của KH**

*(Liz bổ sung / chốt cột cuối cùng của sheet sau.)*

---

## 5. Ticket structure — 1 ticket onboarding chính / KH

**Quy tắc vàng:** mỗi KH = **1 ticket onboarding sống**. Mọi issue liên quan onboarding (bug, câu hỏi, report tiến độ) → note thẳng vào **cùng thread ticket đó**, không tách lẻ.

### 5.1 Checklist trong ticket chính
- [ ] **Launch date**
- [ ] **Detail program** — *(paste link Google Sheet của KH vào đây)*
- [ ] **Earning / Redeeming rule** — đã chốt & setup?
- [ ] **VIP tier setup** (nếu có)
- [ ] **Migration hoặc Import** — data export chưa / import xong chưa
- [ ] **Guest vs Member** — đã config phân quyền/hiển thị?
- [ ] **Widget customize** — *(tạo ticket con riêng → insert link ticket con vào đây)*
- [ ] *(Liz bổ sung thêm sau)*

### 5.2 Widget = ticket con, link về ticket chính
Widget customize **tách ticket riêng** (theo checklist widget on-brand ở [`joy-dfy-flow.md §7`](./joy-dfy-flow.md)) → **insert link ticket con vào ticket chính**. Mọi thứ khác giữ trong ticket chính.

---

## 6. Flow trên chat (tóm tắt end-to-end)

```
KH mới (Advanced) xuất hiện trong chat
        │
   [1] CS OFFER (§2.1)
        │
   [2] DISCOVERY 3 câu (§2.2) → xác định nhánh
        │
   [3] TẠO 1 TICKET ONBOARDING CHÍNH  (checklist §5.1)
        │
   [4] PHÂN NHÁNH A / B / C (§3)
        │   ├─ có plan  → KH gửi plan → CS review + setup → test
        │   └─ chưa có  → gửi checklist Sheet → KH điền (or AI agent) → CS setup → test
        │
   [5] SETUP → TEST → báo KH verify
        │
   [6] Widget customize → ticket con → link vào ticket chính
        │
   [7] Mọi issue/report trong quá trình onboard → note vào CÙNG ticket chính (không tách lẻ)
```

---

## 7. TODO — Liz chốt sau

- [ ] Chốt **cột cuối** của Google Sheet checklist (§4) + tạo template sheet dùng chung.
- [ ] Xác nhận **label/section ticket** đặt tên gì (vd `onboarding-new` / `onboarding-in-progress`) để đồng bộ với DFY labels.
- [ ] Rule import data lớn: ngưỡng nào **CS tự làm** vs **forward TS**.
- [ ] Bổ sung item checklist §5.1 nếu thiếu.
- [ ] Chuẩn bị Phase 2: trigger tự động trong app (điều kiện trigger, nội dung nudge).
