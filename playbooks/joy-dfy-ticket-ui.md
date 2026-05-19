# Avada Ticket — "Done for You" Section UI Spec

**Status:** Draft
**Owner:** Liz (G2 CS Leader)
**Created:** 2026-05-18
**Updated:** 2026-05-19
**Related:** [`joy-dfy-flow.md`](./joy-dfy-flow.md) — quy trình + checklist + template

---

## 0. Tóm tắt — Ai làm gì

Feature này do **2 dev** phụ trách, scope tách biệt nhau:

### Fennic — Avada Ticket
Build section "Done for You" trong Avada Ticket (tool nội bộ). Bao gồm:
- Sidebar item mới "Done for You" (§2)
- 6 status tabs riêng (§3)
- Ticket card với checklist progress bar (§4)
- Detail panel: checklist 19 items, recommendation editor, FU history, close actions (§5)
- "+ New Ticket" form (§8)
- API endpoint để nhận ticket tạo từ Crisp extension (phục vụ Raymond)
- Dashboard / KPI widgets — phase 2 (§9)

**Ref sections:** §2 → §5, §8, §9, §10

### Raymond — TS Crisp Extension
Thêm tính năng DFY vào Crisp extension hiện có. Bao gồm:
- Button "Done for You" trong Crisp chat header (§6)
- Popup eligibility checklist + ticket info form — gọi API của Fennic để tạo ticket (§6)
- AI widget analysis: tự động phân tích widget store, hiển thị kết quả trong popup, auto-populate checklist khi tạo ticket (§7)

**Ref sections:** §6, §7

---

## 1. Mục đích

Spec UI cho **section mới "Done for You"** trong Avada Ticket (tool nội bộ tự build). Section này quản lý DFY tickets cho Joy MC trả phí — workflow, status set, và metrics khác với general support ticket nên cần tách riêng.

CS tự tạo ticket (không có bot auto-tạo). Quy trình + checklist + template merchant-facing message xem trong [`joy-dfy-flow.md`](./joy-dfy-flow.md).

---

## 2. Vị trí trong sidebar

Sidebar item mới, đặt **giữa "Tickets Management" và "Follow Up"**:

```
Dashboard
Tickets
Tickets Management
─── Done for You  ⬅ NEW
Follow Up
Dev Fixing
Feature Requests
Search Tickets
KPI
Resolution Time
AI Assistant
```

Tách riêng khỏi "Tickets" vì DFY có workflow, status set, và metrics khác với general support ticket. Tránh trộn lẫn để CS không bị nhiễu khi filter tickets thường.

---

## 3. Header — Status tabs

Thay vì dùng status chung của Tickets view (Pending / Doing / Dev Fixing / Wait Permission / Wait Customer / Speed Up / Done Speed Up / Dev Done / Done / Billing / Sale Request,…), section DFY dùng **6 status riêng**:

| Tab | Màu gợi ý | Count source |
|---|---|---|
| **New** | grey | status = New |
| **Recommendation Sent** | yellow | status = Recommendation Sent |
| **Following Up** | orange | status = Following Up |
| **Adopted** ✅ | green | status = Adopted (closed) |
| **Partially Adopted** 🔶 | amber | status = Partially Adopted (closed) |
| **No Adoption** ❌ | red | status = No Adoption (closed) |

> Định nghĩa status + transition rules xem trong [`joy-dfy-flow.md`](./joy-dfy-flow.md) §3.

Filter top giữ tương tự "Tickets" view:
- **My Tickets / All Tickets** toggle
- Search box
- Sort (Newest first / Oldest first / FU due / Last activity)
- Ticket count
- **+ New Ticket** button

Tạm **bỏ filter "App"** (DFY chỉ áp dụng Joy hiện tại) — add lại sau nếu mở rộng sang Chatty.

---

## 4. Ticket card (list bên trái)

Mỗi card hiển thị:

- **Tags row:** `DFY` + status badge + `Joy` + plan badge (`Essential` / `Advanced` / `Ultimate`)
- **Title:** ngắn gọn, vd "Setup widget — abcstore.myshopify.com"
- **Sub-line:** store URL (clickable, mở storefront)
- **Assignee avatars** (CS owner)
- **Created / Last activity** time
- **Checklist progress bar** — vd `8/16 items` — visual indicator để CS scan nhanh ticket nào đang stuck

### Mockup card

```
┌─────────────────────────────────────────────┐
│ [DFY] [Auditing] [Joy] [Advanced]           │
│                                             │
│ Setup widget — abcstore.myshopify.com       │
│ abcstore.myshopify.com                      │
│                                             │
│ 👤 hazel_avada      ▓▓▓░░░░░ 6/23          │
│ 🕐 4 hours ago                              │
└─────────────────────────────────────────────┘
```

---

## 5. Detail panel (bên phải, khi chọn ticket)

| Section | Nội dung |
|---|---|
| **Header** | MC info: name, email, plan, install date, store URL (clickable, mở storefront) |
| **Crisp link** | URL conversation gốc (click → mở Crisp trong tab mới) |
| **Status + sub-tag** | Dropdown editable: status (6 options: New / Recommendation Sent / Following Up / Adopted / Partially Adopted / No Adoption) + sub-tag (`No Response` / `Declined` / `Blocked`) |
| **Default checklist** | 4 sections theo `joy-dfy-flow.md` §5: Widget màu sắc & branding (7 items), Widget layout & content (7 items), Widget earning & redeem blocks (4 items), Setup health (5 items) — tổng 23 items. Mỗi item có checkbox + note field để CS ghi kết quả audit |
| **Recommendations** | Rich text field, CS soạn nội dung gửi MC (English only). Có button **"Insert template"** để load template mặc định từ `joy-dfy-flow.md` §6.1 |
| **Send to merchant** | Button gửi recommendation qua Crisp (auto-paste vào Crisp conversation) hoặc email |
| **Follow-up history** | Timeline list các lần FU (FU1, FU2, FU3) với timestamp + nội dung + response của MC. Button **"Add FU note"** để CS log mỗi lần FU |
| **FU reminder** | Date picker — CS tự set ngày FU tiếp theo (không bot remind). CS có thể filter list "FU due today" từ sidebar/sort |
| **Close actions** | 3 button: **"Close as Adopted"** ✅ / **"Close as Partially Adopted"** 🔶 / **"Close as No Adoption"** ❌ — kèm dropdown sub-tag + text field lý do |
| **Activity log** | Ai làm gì lúc nào (CS A tạo ticket, CS B update status, FU note added,…) |

### Mockup detail panel

```
┌─────────────────────────────────────────────────────────────┐
│ Setup widget — abcstore.myshopify.com  [Recommendation Sent ▼] │
│                                                             │
│ MC: ABC Store · john@abcstore.com                          │
│ Plan: Advanced · Installed: 2026-05-10                     │
│ Store: abcstore.myshopify.com  🔗                           │
│ Crisp: chat/session/xyz123  🔗                              │
│                                                             │
│ ─── Checklist ────────────────────────────────── 6/23 ──── │
│ ▼ Widget — Màu sắc & branding (3/7)                       │
│   ☑ Màu primary match store          [note: #000 ok]      │
│   ☑ Background color match theme      [note: dark ✓]      │
│   ☑ Logo header đã thay                                    │
│   ☐ Button/text color ăn theo primary                     │
│   ☐ Ảnh header contrast tốt                               │
│   ☐ Currency icon custom                                  │
│   ☐ Guest/Member card image đã thay                       │
│ ▶ Widget — Layout & content (0/7)                          │
│ ▶ Widget — Earning & Redeem (0/4)                          │
│ ▶ Setup health (0/5)                                       │
│                                                             │
│ ─── Recommendations ──────────────────── [Insert template] │
│ [Rich text editor — CS soạn rcm]                           │
│                            [Send to merchant via Crisp] 📨 │
│                                                             │
│ ─── Follow-up history ─────────────────── [+ Add FU note] │
│ • FU1 sent 2026-05-15 14:00 — "Just checking..."          │
│   Response: "Will try this week"                           │
│ • FU2 scheduled: 2026-05-20  [📅 change]                  │
│                                                             │
│ ─── Close ──────────────────────────────────────────────── │
│ [Close as Adopted ✅]  [Partially Adopted 🔶]  [No Adoption ❌] │
│                                                             │
│ ─── Activity log ────────────────────────────────────────  │
│ • hazel_avada created ticket — 2026-05-13 10:00            │
│ • hazel_avada → Recommendation Sent — 2026-05-13 10:15     │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. Crisp Extension — "Done for You" button

### 6.1 Context

TS extension hiện tại đã nối Crisp với Avada Ticket. Dev của extension cần thêm button **"Done for You"** vào Crisp sidebar (cạnh các action hiện có), để CS tạo DFY ticket trực tiếp từ conversation — không cần mở Avada Ticket riêng.

### 6.2 Button

- **Vị trí:** Crisp conversation sidebar, cùng chỗ với các action button hiện có của extension
- **Label:** `Done for You`
- **Hiển thị khi nào:** Luôn hiện với mọi conversation (CS tự judge eligibility trước khi click)

### 6.3 Popup khi click button

Mở inline popup/modal ngay trong Crisp (không redirect). Gồm 2 phần:

**Phần 1 — Eligibility checklist (required trước khi submit)**

CS phải tick đủ trước khi bấm tạo ticket:

- [ ] MC đang dùng Joy paid plan (Essential / Advanced / Ultimate)
- [ ] Store thuộc ít nhất 1 nhóm: new install (≤30 ngày) / installed but not launched / launched but not on-brand
- [ ] Message có intent liên quan setup / widget / loyalty page — hoặc CS chủ động phát hiện khi xử lý case khác

> Nếu chưa tick đủ 3 → button "Create Ticket" disabled + tooltip: _"Please confirm all eligibility conditions first"_

**Phần 2 — Ticket info (auto-fill từ Crisp nếu được)**

| Field | Auto-fill? | Ghi chú |
|---|---|---|
| MC name | ✅ từ Crisp contact | Editable |
| MC email | ✅ từ Crisp contact | Editable |
| Store URL | ✅ từ Crisp contact metadata (nếu có) | Editable, format `xxx.myshopify.com` |
| Plan | ⚠️ query từ Joy DB nếu có store URL | Dropdown: Essential / Advanced / Ultimate |
| Crisp conversation URL | ✅ auto (current session URL) | Read-only |
| Initial notes | ❌ manual | CS ghi context ngắn |

**Action buttons:**
- `Create Ticket` — tạo ticket trong Avada Ticket, status = **New**, đính kèm Crisp URL, close popup
- `Cancel` — đóng popup, không tạo

**Sau khi tạo thành công:**
- Toast notification trong Crisp: _"DFY ticket created — [link mở ticket trong Avada Ticket]"_
- Checklist 19 items auto-generate trong ticket

### 6.4 Mockup popup

```
┌──────────────────────────────────────────────┐
│  Done for You                            [×] │
├──────────────────────────────────────────────┤
│  Eligibility check                           │
│  ☐ MC đang dùng Joy paid plan                │
│  ☐ Store: new install / not launched /       │
│     not on-brand                             │
│  ☐ Intent: setup / widget / loyalty page     │
├──────────────────────────────────────────────┤
│  Ticket info                                 │
│  Name     [ABC Store              ]          │
│  Email    [john@abcstore.com      ]          │
│  Store    [abcstore.myshopify.com ]          │
│  Plan     [Advanced ▼             ]          │
│  Notes    [                       ]          │
│           [                       ]          │
├──────────────────────────────────────────────┤
│              [Cancel]  [Create Ticket ▶]     │
└──────────────────────────────────────────────┘
```

### 6.5 Dependencies cần confirm với dev extension

1. Extension có access Crisp contact data (name, email, metadata) để auto-fill không?
2. Current session URL (Crisp conversation URL) có lấy được từ context extension không?
3. Có API endpoint nào trong Avada Ticket để tạo DFY ticket programmatically không? (POST ticket với type=DFY)
4. Joy DB có expose API để query plan theo store URL không? (để auto-fill + validate plan)

---

## 7. Crisp Extension — AI Widget Analysis

### 7.1 Mục đích

Khi CS mở popup "Done for You" (§6), extension tự động phân tích widget + loyalty page của store đó bằng AI — trả về nhận xét cụ thể về màu sắc, icon, branding — để CS không phải audit thủ công từ đầu.

Tham khảo: Gemini đã làm được phân tích tương tự (màu chủ đạo, độ tương phản, điểm trừ, icon system) — đây là output mong muốn của feature này.

### 7.2 Trigger

- Tự động chạy khi CS mở popup "Done for You" và có store URL
- Hoặc CS bấm nút **"Analyze widget"** thủ công trong popup nếu muốn chạy lại

### 7.3 Input

- **Store URL** (lấy từ Crisp contact hoặc CS nhập thủ công)
- Extension screenshot hoặc fetch storefront → đưa vào AI model để phân tích

### 7.4 Output — AI trả về

AI phân tích theo đúng checklist widget audit (§5.1 của `joy-dfy-flow.md`), output gồm:

| Mục | AI nhận xét |
|---|---|
| **Màu background widget** | Match / không match dark-light theme → gợi ý màu cụ thể nếu cần đổi |
| **Button color** | Match màu chủ đạo store không → hex gợi ý |
| **Icon contrast** | Đủ contrast / quá mờ / quá ồn ào |
| **Tên chương trình** | Dùng brand name riêng hay generic |
| **Tên point** | Custom hay default "points" |
| **Wording CTA** | Nhận xét ngắn + gợi ý nếu cần đổi |
| **Overall** | 1-2 câu tóm tắt: widget đang on-brand / off-brand / cần gì nhất |

### 7.5 Hiển thị trong popup

Kết quả AI hiện ngay trong popup "Done for You", bên dưới eligibility checklist — trước khi CS điền ticket info:

```
┌──────────────────────────────────────────────┐
│  Done for You                            [×] │
├──────────────────────────────────────────────┤
│  Eligibility check                           │
│  ☑ MC đang dùng Joy paid plan                │
│  ☑ Store: launched but not on-brand          │
│  ☑ CS chủ động phát hiện khi xử lý case      │
├──────────────────────────────────────────────┤
│  🤖 Widget analysis  [↻ Re-analyze]          │
│  ─────────────────────────────────────────   │
│  Background: ❌ White panel on dark theme    │
│    → Suggest: change to #0D0D0D or #1A1A1A  │
│  Button color: ⚠️ Black ok, but no accent   │
│    → Suggest: add gold/silver highlight      │
│  Icon contrast: ✅ OK                        │
│  Program name: ✅ "Timeless Loyalty" — good  │
│  Point name: ⚠️ Using default icon, no name │
│  CTA wording: ✅ Clear                       │
│  Overall: Off-brand background is the main  │
│  issue — fix this first for biggest impact. │
├──────────────────────────────────────────────┤
│  Ticket info                                 │
│  ...                                         │
└──────────────────────────────────────────────┘
```

### 7.6 Auto-populate checklist

Khi CS tạo ticket, kết quả AI analysis tự động điền vào checklist 19 items trong ticket (pre-fill note field + tick ✅/❌ theo kết quả) — CS chỉ cần review và adjust, không phải gõ lại từ đầu.

### 7.7 Training data / prompt guidelines cho dev

AI cần nhận diện được:

- **Màu sắc:** background color của widget panel, button primary color, icon color — so sánh với màu dominant của storefront (header, hero section)
- **Contrast:** text trên background có đạt WCAG AA không (ratio ≥ 4.5:1)
- **Brand name:** widget title có chứa store/brand name không, hay chỉ là "Loyalty Program" / "Rewards"
- **Point name:** có custom point name hay dùng generic "points" / default icon
- **CTA wording:** "Join Now" / "Sign In" vs wording sáng tạo hơn match brand voice

Gemini output mẫu (reference cho prompt engineering):
> _"Tone màu chủ đạo: Đen (#000000) và Trắng (#FFFFFF). Điểm trừ nhỏ: Vì chỉ có đen trắng nền nhìn hơi thiếu 'nhiệt' hoặc thiếu một màu sắc tạo điểm nhấn (Highlight Color) để kích thích người ta bấm vào."_

### 7.8 Dependencies cần confirm với dev extension

1. Extension có thể screenshot hoặc fetch rendered storefront (JS-rendered) không? — đây là điều kiện tiên quyết vì widget render bằng JS
2. Dùng model nào cho analysis? (Gemini / GPT-4o / Claude) — cần multimodal (vision)
3. Latency chấp nhận được: phân tích xong trong vòng bao lâu để UX không bị block?
4. Kết quả AI có lưu vào ticket để xem lại sau không?

---

## 8. "+ New Ticket" form

Khi CS click **"+ New Ticket"** button, mở modal/form với các field:

| Field | Type | Mô tả |
|---|---|---|
| **Crisp conversation URL** | URL input | Paste link Crisp. Nếu Crisp API support → auto-fill các field MC info dưới |
| **MC name** | Text | Auto-fill từ Crisp hoặc manual |
| **MC email** | Email | Auto-fill từ Crisp hoặc manual |
| **Store URL** | URL | Format: `xxx.myshopify.com` |
| **Plan** | Dropdown | `Essential` / `Advanced` / `Ultimate` (chỉ paid plan — không có Free) |
| **Install date** | Date | Auto-fill từ Joy database nếu được, hoặc manual |
| **Initial notes** | Textarea | CS ghi context khi tạo (vd "MC hỏi sao widget không hiện trên mobile") |
| **Assignee** | Dropdown CS list | Default = CS đang tạo, có thể đổi |
| **Eligibility confirmation** | Checkbox (required) | "Đã verify MC dùng plan trả phí + message liên quan setup/widget/page" |

**Sau khi save:**
- Status mặc định = **New**
- Default checklist (23 items) auto-generate
- Ticket xuất hiện trong tab **New** + sidebar count tăng
- Activity log: "[CS] created ticket"

---

## 9. Dashboard / KPI widgets (phase 2)

Thêm vào Dashboard hoặc KPI section của Avada Ticket các widget riêng cho DFY:

| Widget | Hiển thị |
|---|---|
| **Adoption rate** | % `Adopted / (Adopted + No Adoption)` — weekly + trend |
| **Avg time New → Recommendations Sent** | Số giờ trung bình — weekly |
| **Tickets Following Up overdue** | Count tickets có FU reminder date < hôm nay |
| **Top decline reasons** | Bar chart từ sub-tag + close reason — monthly |
| **DFY ticket volume** | Số ticket tạo mới / tuần — trend |
| **Per-CS adoption rate** | Bảng CS + adoption rate cá nhân — coaching signal |

Metrics đầy đủ xem [`joy-dfy-flow.md`](./joy-dfy-flow.md) §7.

---

## 10. Dependencies cần xác nhận với dev team

1. **Crisp conversation URL** có parse được để auto-fill MC info (name, email) không?
2. **Send recommendation qua Crisp API** hay CS manual copy-paste vào Crisp?
3. **Joy MC plan** có query được từ database Avada không? (để validate eligibility + show plan badge)
4. **Joy install date** có sẵn trong DB không?
5. Cần thêm **field tag/category mới** trong ticket schema để phân biệt DFY với general ticket không? (ảnh hưởng filter, count, search)
6. **FU reminder filter** — cần index trên FU date không? (để filter "FU due today" performant)
7. **Permission model** — DFY section có cần role-based access không? (vd chỉ Joy team thấy được)

---

## 11. Phase rollout

| Phase | Scope | Timeline (tentative) |
|---|---|---|
| **Phase 1 — MVP** | Sidebar item, 6 status tabs, ticket card, detail panel (checklist + rcm + FU history + close), New Ticket form | 2-3 tuần build |
| **Phase 2 — Polish** | Dashboard widgets, KPI, Crisp API integration (auto-fill + send), advanced filter (FU due today) | sau pilot 2 tuần |
| **Phase 3 — Expand** | Mở rộng sang Chatty (nếu pilot Joy thành công) — add filter App, plan badge Chatty,… | tbd |

---

## 12. Open questions

- Có cần **bulk action** (close nhiều ticket cùng lúc, reassign,…) trong phase 1 không?
- **Notification:** CS có cần được notify khi FU reminder đến hạn (qua Avada Ticket bell hay Slack)?
- **Search:** CS có cần search trong recommendation content không, hay chỉ search title/MC info?
- **Export:** Liz có cần export DFY tickets ra CSV cho weekly report không?
