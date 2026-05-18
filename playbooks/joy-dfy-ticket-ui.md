# Avada Ticket — "Done for You" Section UI Spec

**Status:** Draft
**Owner:** Liz (G2 CS Leader)
**Created:** 2026-05-18
**Updated:** 2026-05-18
**Related:** [`joy-dfy-flow.md`](./joy-dfy-flow.md) — quy trình + checklist + template

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
| **Auditing** | blue | status = Auditing |
| **Recommendations Sent** | yellow | status = Recommendations Sent |
| **Following Up** | orange | status = Following Up |
| **Adopted** ✅ | green | status = Adopted (closed) |
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
│ 👤 hazel_avada      ▓▓▓░░░░░ 6/16          │
│ 🕐 4 hours ago                              │
└─────────────────────────────────────────────┘
```

---

## 5. Detail panel (bên phải, khi chọn ticket)

| Section | Nội dung |
|---|---|
| **Header** | MC info: name, email, plan, install date, store URL (clickable, mở storefront) |
| **Crisp link** | URL conversation gốc (click → mở Crisp trong tab mới) |
| **Status + sub-tag** | Dropdown editable: status (6 options) + sub-tag (`Partial` / `No Response` / `Declined` / `Blocked`) |
| **Default checklist** | 3 sections theo `joy-dfy-flow.md` §5: Widget audit (5 items), Loyalty page audit (7 items), Setup health (4 items). Mỗi item có checkbox + note field để CS ghi kết quả audit |
| **Recommendations** | Rich text field, CS soạn nội dung gửi MC (English only). Có button **"Insert template"** để load template mặc định từ `joy-dfy-flow.md` §6.1 |
| **Send to merchant** | Button gửi recommendation qua Crisp (auto-paste vào Crisp conversation) hoặc email |
| **Follow-up history** | Timeline list các lần FU (FU1, FU2, FU3) với timestamp + nội dung + response của MC. Button **"Add FU note"** để CS log mỗi lần FU |
| **FU reminder** | Date picker — CS tự set ngày FU tiếp theo (không bot remind). CS có thể filter list "FU due today" từ sidebar/sort |
| **Close actions** | 2 button: **"Close as Adopted"** ✅ / **"Close as No Adoption"** ❌ — kèm dropdown sub-tag + text field lý do |
| **Activity log** | Ai làm gì lúc nào (CS A tạo ticket, CS B update status, FU note added,…) |

### Mockup detail panel

```
┌─────────────────────────────────────────────────────────────┐
│ Setup widget — abcstore.myshopify.com         [Auditing ▼] │
│                                                             │
│ MC: ABC Store · john@abcstore.com                          │
│ Plan: Advanced · Installed: 2026-05-10                     │
│ Store: abcstore.myshopify.com  🔗                           │
│ Crisp: chat/session/xyz123  🔗                              │
│                                                             │
│ ─── Checklist ────────────────────────────────── 6/16 ──── │
│ ▼ Widget audit (3/5)                                       │
│   ☑ Widget hiển thị trên storefront    [note: OK desktop] │
│   ☑ Position hợp lý                     [note: ...]       │
│   ☑ Màu match theme                                        │
│   ☐ Wording CTA rõ ràng                                   │
│   ☐ Icon không quá ồn ào                                  │
│ ▶ Loyalty page audit (2/7)                                 │
│ ▶ Setup health (1/4)                                       │
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
│ [Close as Adopted ✅]   [Close as No Adoption ❌]          │
│                                                             │
│ ─── Activity log ────────────────────────────────────────  │
│ • hazel_avada created ticket — 2026-05-13 10:00            │
│ • hazel_avada → Auditing — 2026-05-13 10:15                │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. "+ New Ticket" form

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
- Default checklist (16 items) auto-generate
- Ticket xuất hiện trong tab **New** + sidebar count tăng
- Activity log: "[CS] created ticket"

---

## 7. Dashboard / KPI widgets (phase 2)

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

## 8. Dependencies cần xác nhận với dev team

1. **Crisp conversation URL** có parse được để auto-fill MC info (name, email) không?
2. **Send recommendation qua Crisp API** hay CS manual copy-paste vào Crisp?
3. **Joy MC plan** có query được từ database Avada không? (để validate eligibility + show plan badge)
4. **Joy install date** có sẵn trong DB không?
5. Cần thêm **field tag/category mới** trong ticket schema để phân biệt DFY với general ticket không? (ảnh hưởng filter, count, search)
6. **FU reminder filter** — cần index trên FU date không? (để filter "FU due today" performant)
7. **Permission model** — DFY section có cần role-based access không? (vd chỉ Joy team thấy được)

---

## 9. Phase rollout

| Phase | Scope | Timeline (tentative) |
|---|---|---|
| **Phase 1 — MVP** | Sidebar item, 6 status tabs, ticket card, detail panel (checklist + rcm + FU history + close), New Ticket form | 2-3 tuần build |
| **Phase 2 — Polish** | Dashboard widgets, KPI, Crisp API integration (auto-fill + send), advanced filter (FU due today) | sau pilot 2 tuần |
| **Phase 3 — Expand** | Mở rộng sang Chatty (nếu pilot Joy thành công) — add filter App, plan badge Chatty,… | tbd |

---

## 10. Open questions

- Có cần **bulk action** (close nhiều ticket cùng lúc, reassign,…) trong phase 1 không?
- **Notification:** CS có cần được notify khi FU reminder đến hạn (qua Avada Ticket bell hay Slack)?
- **Search:** CS có cần search trong recommendation content không, hay chỉ search title/MC info?
- **Export:** Liz có cần export DFY tickets ra CSV cho weekly report không?
