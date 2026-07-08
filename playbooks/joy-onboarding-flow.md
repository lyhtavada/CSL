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
> *"Hi [name], I saw you recently installed Joy and are getting your loyalty program set up — I'd love to help you get it set up properly so it's ready to launch. Would you like me to walk through it with you and set things up together?"*

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
- **Nhánh B/C:** không có plan → gửi **Setup Sheet** cho KH điền (§4) → CS review → setup → test.

> **Khi nào gửi Setup Sheet:**
> - **A1 / B1 (KH đã có plan chi tiết):** ❌ đừng gửi sheet — **xin plan của KH luôn**, đỡ bắt họ chép lại.
> - **A2 / B2 / C (KH chưa có plan rõ):** ✅ gửi sheet để chốt rule.
> - ⚠️ **Đừng gửi ngay câu đầu** (trước discovery) — sheet 6 tab, quăng sớm KH dễ ngợp & bỏ. Offer + hỏi 3 câu trước, biết nhánh rồi mới gửi.

---

## 3B. Flow chi tiết từng nhánh + template chat (EN)

> Template tiếng Anh để CS **copy-paste trong live chat** (tone thân thiện, ngắn gọn). Thay `[name]`, `[old app]`, `[X]`… cho đúng KH. **Ai setup là tùy KH:** hỏi KH muốn CS làm hộ hay tự làm rồi đi theo nhánh tương ứng — template có sẵn cả 2 (xem §3B.6).

### Câu offer + discovery (dùng chung, mọi nhánh)

**Offer:**
> *"Hi [name], I saw you recently installed Joy and are getting your loyalty program set up — I'd love to help you get it set up properly so it's ready to launch. Want me to walk through it with you and set things up together?"*

**Discovery (hỏi rải, đừng dồn 1 lúc):**
> *"When are you hoping to launch your loyalty program?"*
> *"Have you run a loyalty program before — on another app or store?"*
> *"Are you moving over from another loyalty app? If so, do you already have your points/customer data exported?"*

→ Từ 3 câu trả lời, map vào nhánh:

| Trả lời của KH | Nhánh |
|----------------|-------|
| Đang chuyển từ app loyalty khác + đã có plan chi tiết | **A1** |
| Đang chuyển từ app khác + chưa có plan rõ | **A2** |
| Từng chạy loyalty (không migrate app) + có plan sẵn | **B1** |
| Từng chạy loyalty + chưa có plan rõ | **B2** |
| Chưa từng chạy loyalty bao giờ | **C** |

---

### 3B.1 — Nhánh A1: Migrate + KH đã có plan chi tiết

**Flow:** xin plan KH → chạy 3 câu migration → xác nhận KH có trên Shopify → chốt cách import → CS review + setup → test → launch.

```
Xin plan  →  3 câu migration  →  confirm customers on Shopify  →  chốt import (file vs sync)
   →  review + setup  →  test full loop  →  KH OK  →  Sandbox → Live
```

**Template:**
> *(Xin plan)* *"Perfect — since you've already mapped out your program, could you share your plan/doc with me? I'll review it and set everything up to match."*
>
> *(3 câu migration — playbook §2.1)* *"A few quick things about the move so we get it right the first time:"*
> *"1. Which app are you coming from — [old app]?"*
> *"2. Is your program based on points earned, or amount spent?"*
> *"3. Do you have your data as a file to import, or should we sync from your existing Shopify orders?"*
>
> *(Confirm)* *"One important thing: the customers you're migrating need to already exist in your Shopify — points and tiers attach to Shopify customers. Are they all in there?"*
>
> *(Set expectation)* *"Heads up — from most apps we can bring over the points balance; full activity history usually doesn't carry over. I'll confirm exactly how far your balance migrates before we import, so there are no surprises."*
>
> *(Sau setup)* *"All set up on Sandbox — I've matched your plan. Want to take a look before we go live?"*

⚠️ **Không import ngay.** Migrate là chỗ dễ vỡ nhất — data lớn/phức tạp → forward TS. Import **một lần**, verify 10–20 account trước khi launch.

---

### 3B.2 — Nhánh A2: Migrate + KH chưa có plan rõ

**Flow:** như A1 nhưng **thêm bước gửi Setup Sheet** để KH chốt rule (vì chưa có plan).

```
Gửi Setup Sheet  →  3 câu migration  →  confirm on Shopify  →  KH điền sheet
   →  review + setup  →  test  →  launch
```

**Template:**
> *(Gửi sheet)* *"No worries — I'll send you a quick setup sheet so we can shape your program together. Just fill in the Value column; if you're unsure on anything, follow the Suggested column or leave it blank and we'll figure it out. Here you go: [link bản copy]"*
>
> *(Nếu KH bí)* *"If you're not sure what values to pick, our in-app AI can look at your store's AOV and industry and suggest earn/redeem rates — want me to run that for you?"*
>
> *(3 câu migration + confirm on Shopify)* → giống A1.

---

### 3B.3 — Nhánh B1: Đã dùng loyalty trước (không migrate) + có plan sẵn

**Flow:** không migrate data → xin plan → CS review + setup → test → launch. Đơn giản nhất.

```
Xin plan  →  review + setup  →  test full loop  →  KH OK  →  Sandbox → Live
```

**Template:**
> *(Xin plan)* *"Great — since you've run one before and know what you want, could you share your rules/plan? I'll review it and get it set up for you."*
>
> *(Sau setup)* *"Done on Sandbox. I ran a quick test — earning and redeeming both work. Want to review before we launch?"*

---

### 3B.4 — Nhánh B2: Đã dùng loyalty trước + chưa có plan rõ

**Flow:** gửi Setup Sheet → KH điền → CS review + setup → test → launch.

**Template:**
> *(Gửi sheet)* *"Since you've run a program before, this'll be quick — I'll send a setup sheet, just fill in the Value column with your rules. Suggested values are there if you want a starting point: [link bản copy]"*
>
> *(Sau khi KH điền)* *"Thanks! I'll review these and set it all up on Sandbox, then loop you in to check before we go live."*

---

### 3B.5 — Nhánh C: Chưa từng chạy loyalty bao giờ

**Flow:** KH cần **được gợi ý nhiều nhất** — CS đề xuất preset theo ngành/AOV, dùng AI agent, chốt rule cùng KH → setup → test → launch.

```
Gợi ý preset (industry/AOV) + AI agent  →  gửi Setup Sheet có preset  →  chốt rule cùng KH
   →  setup  →  test  →  launch
```

**Template:**
> *(Trấn an + offer gợi ý)* *"Totally fine — a lot of stores start their first program with us, I'll guide you the whole way. I'll suggest a simple setup based on your industry and average order value so you don't have to start from scratch."*
>
> *(AI agent)* *"Our in-app AI can read your store's AOV and industry and propose earn/redeem rates and tiers — want me to generate a starting plan you can tweak?"*
>
> *(Gửi sheet có preset)* *"Here's a setup sheet with suggested values already filled in as a starting point — adjust anything you like, and I'll set it up: [link bản copy]"*
>
> *(Chốt cùng KH)* *"Here's what I'd recommend to start: earn 1 point per $1, 100 points = $5 off, plus a welcome bonus. Simple and proven — happy to adjust. Sound good?"*

---

### 3B.6 — Ai setup: CS làm hộ vs KH tự làm (hỏi KH, tùy yêu cầu)

Sau khi chốt rule ở bất kỳ nhánh nào, **hỏi KH muốn ai thao tác:**
> *"Would you like me to set this up for you, or would you prefer to do it yourself with me guiding you step by step?"*

**Nếu KH muốn CS làm hộ** → xin quyền truy cập:
> *"Happy to set it up for you. I'll work on a test theme + Sandbox so nothing affects your live store or real customer data. I'll let you know as soon as it's ready to review."*
> *(Nếu cần collaborator access)* *"To set this up on your end, could you send a staff/collaborator invite? That lets me configure everything directly — I'll only touch the loyalty setup."*

**Nếu KH muốn tự làm** → CS guide từng bước:
> *"No problem — I'll walk you through it. First, let's turn on Sandbox Mode so we can test safely..."* *(hướng dẫn theo Module 3 / KB LIVE, chỗ nào KH vướng thì tra [playbook FAQ](./joy-dfu-onboarding-playbook.md)).*

> Dù ai bấm nút, **CS vẫn own ticket tới launch** (§7) và **luôn test cho KH xem trước khi Sandbox → Live**.

---

### 3B.7 — Câu launch (dùng chung, mọi nhánh) 🚀

Luôn **xin KH gật trước khi bật live** — đây là lúc khách bắt đầu tích điểm thật:
> *"Everything's tested and working on Sandbox. Ready for me to switch it to live? Once we do, your customers will start earning points for real."*

Sau launch:
> *"You're live! 🎉 Your program is now earning points for every order. Here's where you can track results — [assisted revenue + redemption rate]. I'll check in to see how it's going."*

---

## 4. Setup Sheet (KH điền rule)

**Master template (Google Sheet):** https://docs.google.com/spreadsheets/d/1Dnvg96dqgXmckuj4lVpQ3GM4_Fs4yB-h-xClSWvhdME/edit
(Nội dung tương ứng ở [`joy-onboarding-program-checklist.md`](./joy-onboarding-program-checklist.md).)

**Cách dùng — clone 1 bản / KH:**
1. Mở master → **File → Make a copy** → đặt tên `[Store] — Joy Setup`.
2. Gửi bản copy cho KH → KH điền cột **Value** (ô đỏ). Chỗ chưa chắc → theo cột **Suggested / Preset**, hoặc để trống, hoặc dùng **AI agent trong app** (đọc AOV/industry sinh gợi ý).
3. **Paste link bản copy** vào field "Detail program" của ticket chính.

> ⚠️ **Không cho nhiều KH điền chung 1 sheet** — clone riêng từng bản để data tách bạch, KH không thấy data của nhau.

Sheet gồm các tab: Program Setup (store info + launch date + program config + integrations + migration) · Earning · Redemption · VIP tier · Referral · Milestones · go-live check.

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
