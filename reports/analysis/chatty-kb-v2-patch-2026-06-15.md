# Chatty KB v2 (Ivy) — Patch Package

> Nguồn: diff 40 FAQ mined từ 280 chat thật (Jun 02–09 2026) vs KB live của `chatty-agent` trên v2 (`https://cs2.avada.net`).
> Ngày soạn: 2026-06-15. Áp dụng vào: `GET/PUT .../api/kb/file?agent=chatty-agent&path=<path>`.
> Tổng: 1 sửa (OUTDATED) + 5 bổ sung (GAP). Các PARTIAL nhỏ liệt kê ở cuối.

---

## 1. SỬA — `kb/case/email-channel-issues.md` (OUTDATED) 🔴

Domain forwarding đã đổi `@chattyemail.com` → `@chatty.email` (xác nhận từ chat Jun 02–09). File còn sót 2 chỗ dùng domain cũ (line ~144 và ~206), trong khi line 228 đã dùng đúng domain mới.

**Sửa 1 — line ~144 (mục "Chatty Emails Going to Spam"):**
- Cũ: `Recommend using a **custom sender domain** instead of the default `noreply@chattyemail.com` if they haven't already`
- Mới: `Recommend using a **custom sender domain** instead of the default `noreply@chatty.email` if they haven't already`

**Sửa 2 — line ~206 (mục "AI/Agent Email Replies Delivered to Customer"):**
- Cũ: `The default sender address is `noreply@chattyemail.com` unless you have configured a custom sender domain.`
- Mới: `The default sender address is `noreply@chatty.email` unless you have configured a custom sender domain.`

**Thêm 1 section mới (để khách bị mất mail tự fix):**

```markdown
## Verification Address Changed (@chattyemail.com → @chatty.email)

Chatty's email forwarding/verification domain changed from `@chattyemail.com` to the new `@chatty.email`. If a merchant set up forwarding before the change and emails stopped arriving:

1. Open the email provider's forwarding settings
2. Update the forwarding/verification address to the new `@chatty.email` address shown in **Settings → Channels → [email] → View Instructions**
3. Re-paste and re-save, then click **Proceed** to re-verify

> Always copy the current forwarding address from View Instructions rather than reusing an old one — the old `@chattyemail.com` address no longer verifies.
```

---

## 2. BỔ SUNG — `kb/faq/channels.md` (GAP, mined Q26) 🟠

KB hiện chỉ hướng dẫn bật AI Channels, **không nêu điều kiện plan**. Khách Free/Basic tưởng AI chạy được trên social.

**Chèn ngay sau block "Facebook Messenger & Instagram" / "WhatsApp" (khoảng line 47):**

```markdown
---

## AI Auto-Reply by Channel & Plan

AI conversations are available on all plans (Free, Basic, Pro, Plus), but **AI auto-reply on social channels requires Pro or higher**:

- **Free & Basic:** AI auto-reply works **only for the chat widget on your website**.
- **Pro & Plus:** AI auto-reply also works on **WhatsApp, Facebook Messenger, and Instagram**.

Connecting a channel and enabling AI on it are **two separate steps**: connect under **Settings → Channels**, then enable AI per channel under **AI agent → Settings → AI Channels**. The AI only replies to **new** incoming messages after it's enabled.

> Chatty currently supports connecting **one Facebook account**.
```

Thêm tag vào frontmatter: `"AI on WhatsApp"`, `"AI on Messenger"`, `"AI Pro plan"`, `"AI channel plan"`.

---

## 3. BỔ SUNG — `kb/faq/pricing.md` (GAP, mined Q31) 🟠

KB chưa có thông tin bulk/multi-store discount. Dễ hứa nhầm điều kiện.

**Chèn ngay sau mục "Annual Billing Discount" (khoảng line 205):**

```markdown
---

## Bulk / Multi-Store Discount

A **20% lifetime bulk discount** is available for merchants running multiple stores:

- Applies to **monthly Pro or Plus** plans only.
- Requires **at least 2 stores on Pro or above** to qualify (they do **not** all need the same plan).
- **Not** available for the Basic plan.
- **Cannot** be combined with annual plans (annual already includes ~15–17% off). A store on annual must switch to monthly to use the bulk discount.

> Each store is billed separately by Shopify, so the discount code is applied per store. Collect the merchant's store count and current plans, then forward the request to the team — do not promise eligibility before confirming.
```

Thêm tag: `"bulk discount"`, `"multi-store discount"`, `"20% discount"`, `"multiple stores pricing"`.

---

## 4. BỔ SUNG — `kb/faq/chatbox-settings.md` (GAP, mined Q35) 🟠

KB có mục cart drawer (hide widget) nhưng **không có** cách tắt AI Add-to-Cart hay fix cart rỗng.

**Chèn ngay sau mục "Hide Widget When Cart Drawer Opens" (khoảng line 192):**

```markdown
---

## Disabling Add-to-Cart / Cart Showing Empty

**To remove the cart feature:** The cart section and the AI's Add-to-Cart feature can be removed on request — the tech team disables them (useful when a merchant wants the widget as a pure FAQ/support tool). Collect the store URL and forward to the team.

**Cart shows empty after the AI adds items:** The AI does add items correctly, but some custom themes (custom cart drawers / non-standard Ajax carts) don't follow Shopify's standard cart behavior, so the drawer needs a refresh to reflect the change. The fix is for the team to add the `chatty:cart:changed` event to the theme.

To apply it, ask the merchant to grant collaborator access: **Shopify Settings → Users → Security → Collaborator request code**, then escalate to the team with the store URL and the code.
```

Thêm tag: `"disable add to cart"`, `"cart empty"`, `"chatty:cart:changed"`, `"remove cart feature"`.

---

## 5. BỔ SUNG — `kb/case/access-login-issues.md` (GAP, mined Q36) 🟠

Message "Chatty needs to be updated by the owner" lặp lại trong chat nhưng KB chưa có.

**Chèn ngay trước mục "Related" (khoảng line 131):**

```markdown
## "Chatty needs to be updated by the owner" / Intermittent Access Loss

## Symptom

Staff/admin accounts intermittently lose access or see a message that **Chatty needs to be updated by the owner**, then it seems to "resolve itself" before recurring.

## Cause

This message comes from **Shopify**, not Chatty. When a Chatty update requires new permissions, Shopify asks the **store owner (primary account holder)** to approve them. Until the owner approves, non-owner accounts can get blocked when starting a new session — which is why it appears intermittently.

## Resolution

1. Confirm the affected user is **not** the store owner.
2. Ask the **store owner** to open Chatty from Shopify Admin → Apps → Chatty and **approve the pending permission update**.
3. After the owner approves, the message stops appearing for all staff.

> Do not escalate as a Chatty bug — this is Shopify's standard permission-approval flow.
```

Thêm tag: `"updated by owner"`, `"needs to be updated"`, `"permission approval"`, `"intermittent access"`.

---

## 6. BỔ SUNG — `kb/case/notification-issues.md` hoặc file media mới (GAP, mined Q39) 🟠

Image retention nâng 90→180 ngày, video ~18MB. KB chưa có (KHÔNG nhầm với "90 days data retention" của ai-compliance — đó là thứ khác).

**Chèn vào `kb/case/notification-issues.md` ngay trước "Related" (khoảng line 146), hoặc tạo file mới `kb/case/inbox-media-issues.md`:**

```markdown
---

## Missing Images / Videos in Inbox

**Missing images:** Older chat images may have passed the previous **90-day image retention** window. Retention has been extended to **180 days** — ask the merchant to refresh the inbox to view them again. If specific *recent* images are missing, escalate to support to investigate.

**Video won't display / "too large":** Chatty's inbox can only process video attachments up to **~18MB** (driven by email-provider attachment caps of ~20–25MB). Larger videos won't sync or display.

> Workaround: ask customers to share large videos via a cloud link (Google Drive, Dropbox, WeTransfer) instead of attaching the file directly.
```

Thêm tag: `"missing images"`, `"image retention"`, `"180 days"`, `"video too large"`, `"18MB"`, `"video not displaying"`.

---

## PARTIAL — bổ sung nhỏ (gộp khi tiện, ưu tiên thấp hơn)

| File | Thêm sub-point |
|---|---|
| `kb/faq/knowledge-base.md` (Q4) | Cách link store thứ 2: Install Chatty → **Activate** để link account; **store switcher ở góc trên-trái** app.meetchatty.com; mobile chỉ nhận notification của store đang switch. |
| `kb/faq/faqs-block.md` (Q21) | Feature **Custom Knowledge → Sync Store Page → Add Q&A** tự sinh ~15 starter Q&A từ store pages (chiêu agent dùng nhiều nhất — high freq ~14 sessions). |
| `kb/faq/add-category.md` (Q23) | Categories **không** hiện được trên chat page (chỉ widget homepage); **không có option tắt JSON-LD** auto-generated (đã log feedback). |
| `kb/faq/team.md` (Q37) | Workaround link invite/reset không mở: dùng **VPN US/EU (không Hong Kong)**; **tracking/click-monitoring segment** trong URL làm hỏng link → dùng link gốc. |
| `kb/faq/inbox.md` / `kb/faq/others.md` (Q38) | **Store-to-store migration không hỗ trợ**; conversation history gắn theo store (không theo account/domain); chỉ copy tay được Instructions/Scenarios/FAQ. |
| `kb/faq/inbox.md` (Q40) | Case messages **lẫn giữa các thread** → xử lý **high-priority, escalate dev**; merchant gửi **conversation IDs** để điều tra. |

---

## Thứ tự áp dụng đề xuất

1. **#1 Email `@chatty.email`** — sửa nhanh 2 dòng, khách đang mất mail.
2. **Q21 Sync Store Page → Add Q&A** (PARTIAL) — tần suất cao nhất (~14 sessions).
3. **#2 AI social cần Pro+** — gating dễ trả lời sai.
4. **#3 Bulk discount** — tránh hứa nhầm revenue.
5. **#5 owner-permission**, **#4 cart**, **#6 image/video retention** — gom 1 đợt.
