# Joy Loyalty — Onboarding Flow (CS thao tác trên chat)

**Owner:** Liz (CS Leader)
**Created:** 2026-07-07 · **Updated:** 2026-07-08
**Status:** v2 — Phase 1 (CS chủ động offer trong chat). Phase 2 (trigger tự động trong app) để sau.

> **File này chỉ nói: CS làm gì trên chat, tạo ticket ra sao, issue phát sinh xử lý thế nào.**
> Kiến thức "làm thế nào / hiểu tại sao" (7 bước có exit-criteria, migration, VIP tier, guest/member, Widget V4, FAQ 50 case) → nằm ở **[`joy-dfu-onboarding-playbook.md`](./joy-dfu-onboarding-playbook.md)**. File này chỉ trỏ sang, KHÔNG lặp lại.
>
> Khác gì với [`joy-dfy-flow.md`](./joy-dfy-flow.md)? DFY thiên về **làm hộ widget + đẩy go-live** cho store gần xong. **Onboarding flow này** dành cho KH **Advanced+** cần **build cả loyalty program từ đầu** — có discovery đầu vào, 1 ticket sống/KH xuyên suốt.

---

## 0. Mục tiêu & phạm vi

**Phase 1:** CS **chủ động offer** onboarding cho KH **Advanced trở lên** ngay trong chat → đưa họ từ "vừa lên plan / chưa có program" đến **launch được program đúng ý**, có hoặc không migration.

- **Phase 1 (bản này):** CS trực tiếp offer trong chat.
- **Phase 2 (sau):** trigger tự động trong app khi KH lên Advanced / mới install → nudge onboarding.

**Nguyên tắc xuyên suốt:** mỗi KH = **1 ticket onboarding chính**. Mọi issue phát sinh (bug, câu hỏi, report tiến độ) **note thẳng vào ticket đó**, không tách lẻ. Ngoại lệ duy nhất: **widget customize** → ticket con riêng nhưng **insert link vào ticket chính** (§5).

---

## 1. Eligibility — Khi nào CS offer

CS offer onboarding khi **cả 2** đúng:

1. **Plan = Advanced trở lên** (scope Phase 1 — KH giá trị cao, đáng đầu tư setup full).
2. Store thuộc ít nhất một nhóm:
   - **Mới lên Advanced / mới install**, chưa có program hoàn chỉnh
   - **Chưa launch** — chưa có earning/redeeming active, hoặc còn sandbox
   - **Đang hỏi trong chat** về setup earning / redeem / VIP / migrate / import

**KHÔNG offer lại** nếu KH đã có ticket onboarding đang mở → update ticket cũ.

---

## 2. Mở đầu — CS offer + Discovery (trên chat)

### 2.1 Câu offer
> *"Hi [name], I noticed you're on our Advanced plan — I'd love to help you get your loyalty program set up properly so it's ready to launch. Would you like me to walk through it with you and set things up together?"*

### 2.2 Discovery — 3 câu mở đầu (đừng hỏi dồn 1 lúc)
Mục tiêu: biết **timeline**, **kinh nghiệm loyalty trước đó**, và **có phải migrate không**.

1. **Launch timeline:** *"When are you planning to launch your loyalty program?"*
2. **Kinh nghiệm trước đó:** *"Have you run a loyalty program before — either on another app or store?"*
3. **(Nếu có dùng trước đó) Migration:** *"Are you moving over from another loyalty app? If so, do you already have your customer/points data exported?"*

> Từ 3 câu này → CS xác định nhánh ở §3.
> Intake sâu hơn (points vs amount, Legacy/NCA, integrations bắt buộc) → làm theo **Bước 0** của [playbook](./joy-dfu-onboarding-playbook.md).

---

## 3. Decision tree — Phân nhánh theo tình huống KH

```
KH mới ở Advanced
        │
        ├── A. MIGRATE từ app loyalty khác sang
        │        ├── A1. Đã có detailed plan  → xin KH gửi plan → CS review + setup theo → test
        │        └── A2. Chưa có plan rõ       → gửi checklist Google Sheet → KH điền rule
        │                                          (KH chưa biết → hướng dẫn dùng AI agent trong app)
        │        + Migration LUÔN chạy 3 câu ở playbook §2.1 (từ đâu / point-amount / file-sync)
        │
        ├── B. ĐÃ dùng loyalty trước (không migrate app / build lại từ đầu)
        │        ├── B1. Đã có plan/rule sẵn   → gửi CS → CS review + setup giúp → test
        │        └── B2. Chưa có plan rõ       → gửi checklist Google Sheet → KH điền
        │
        └── C. CHƯA từng dùng loyalty bao giờ
                 → CS gợi ý preset theo ngành/AOV
                 → hỗ trợ KH dùng AI agent trong app (đọc AOV, industry…) đề xuất rule
                 → chốt rule → CS setup → test
```

- **Nhánh A (migrate):** đây là chỗ dễ vỡ nhất — **không làm ngay theo yêu cầu lẻ "migrate hộ"**. Chạy đủ **3 câu migration** ([playbook §2.1](./joy-dfu-onboarding-playbook.md)) trước. Xác nhận KH đã có customer trên Shopify. Data lớn/phức tạp → forward TS.
- **Nhánh B/C:** không có plan → gửi **checklist Google Sheet** ([`joy-onboarding-program-checklist.md`](./joy-onboarding-program-checklist.md)) → KH điền → CS setup → test.

---

## 4. Checklist Google Sheet (KH điền rule)

CS clone [`joy-onboarding-program-checklist.md`](./joy-onboarding-program-checklist.md) thành 1 Google Sheet/KH → KH điền rule → paste link vào field "Detail program" của ticket chính. KH chưa biết điền gì → theo cột **Gợi ý / Preset**, hoặc dùng **AI agent trong app** (đọc AOV/industry sinh gợi ý).

Sheet gồm: store info + launch date · program basics · earning · redeeming · VIP tier · referral · member vs guest · migration/import · milestones · go-live check.

---

## 5. Ticket structure — 1 ticket onboarding chính / KH

**Quy tắc vàng:** mỗi KH = **1 ticket onboarding sống**. Mọi issue liên quan onboarding (bug, câu hỏi, report tiến độ) → note thẳng vào **cùng thread ticket đó**, không tách lẻ.

### 5.1 Checklist trong ticket chính
- [ ] **Launch date**
- [ ] **Detail program** — *(paste link Google Sheet của KH)*
- [ ] **Earning / Redeeming rule** — đã chốt & setup?
- [ ] **VIP tier setup** (nếu có) — tag + metafield đã sync?
- [ ] **Migration hoặc Import** — data export chưa / import xong chưa
- [ ] **Guest vs Member** — đã config phân quyền/hiển thị?
- [ ] **Test one full loop** (earn → redeem) OK — cho KH xem & xác nhận
- [ ] **Widget customize** — *(ticket con riêng → insert link vào đây)*
- [ ] Get merchant OK → **switch sandbox → live** 🚀

### 5.2 Widget = ticket con, link về ticket chính
Widget customize **tách ticket riêng** (theo checklist widget on-brand ở [`joy-dfy-flow.md §7`](./joy-dfy-flow.md), chi tiết convert V4 ở [playbook §2.5](./joy-dfu-onboarding-playbook.md)) → **insert link ticket con vào ticket chính**. Mọi thứ khác giữ trong ticket chính.

---

## 6. Xử lý issue phát sinh trong lúc onboard

Trong lúc onboard, KH hay báo lỗi/hiện tượng (không cộng điểm, coupon invalid, widget không hiện, perk không apply…). Cách CS xử lý:

1. **KHÔNG tách ticket mới** — note issue vào **cùng ticket onboarding chính** (trừ widget = ticket con).
2. **Tự chẩn đoán trước, đừng đẩy dev vội** — tra **FAQ theo domain** ở [playbook Phần 3](./joy-dfu-onboarding-playbook.md) (A Points · B Coupon · C Metafield · D Widget · E VIP · F Migration · G Integration · H Config). Nhớ: **51% ticket escalate hóa ra không phải bug Joy**.
3. **Chạy lăng kính triage** 🟢 config · 🔵 đúng-thiết-kế · 🟠 3rd-party · 🔴 bug Joy thật. Chỉ escalate 🔴, **kèm bằng chứng** (state đã check).
4. **Hỏi Joy AI agent trước** cho câu hỏi chẩn đoán (guest hay member? order này vì sao không earn? coupon điều kiện thật?) — nhanh hơn mò tay.

---

## 7. Ownership & SLA (chat trực theo ca)

- **Nhận là own tới cùng.** Nhận case nào chịu trách nhiệm tới khi xong.
- **Hẹn rõ:** việc cần thời gian (vd import) → hẹn khách **~1 ngày** và làm tới nơi.
- **Bàn giao ca liền mạch:** hết ca chưa xong → để lại note trạng thái đầy đủ để ca sau nối tiếp, không bắt khách kể lại từ đầu.
- **Không đá việc** — không assign bạn khác "import hộ" chỉ vì hết ca, trừ khi đã bàn giao rõ.

---

## 8. Flow trên chat (tóm tắt end-to-end)

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
   [5] SETUP → TEST cho KH xem & xác nhận (đừng bỏ) → get OK → SANDBOX → LIVE 🚀
        │
   [6] Widget customize → ticket con → link vào ticket chính
        │
   [7] Issue phát sinh → note vào CÙNG ticket + tự triage (playbook FAQ) trước khi đẩy dev
```

---

## 9. TODO — Liz chốt sau

- [ ] Chốt **cột cuối** Google Sheet checklist + template dùng chung.
- [ ] Xác nhận **label/section ticket** (vd `onboarding-new` / `onboarding-in-progress`) đồng bộ DFY labels.
- [ ] Ngưỡng import data lớn: **CS tự làm** vs **forward TS**.
- [ ] Phase 2: trigger tự động trong app (điều kiện trigger, nội dung nudge) + skill `joy-onboarding-plan` (xem [playbook — canvas](./joy-dfu-onboarding-playbook.md)).
