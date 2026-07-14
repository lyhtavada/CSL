# KB Patch Review — từ corrections 13–14/07/2026

**Trạng thái:** ⏸️ Chờ Liz duyệt. Chưa push gì lên `cs2.avada.net`.

4 patch, đi từ 5/7 correction tuần này. 2 correction còn lại không patch được (giải thích ở cuối).

Nguyên tắc áp dụng: viết cái **ĐÚNG**, không viết negative example kiểu "đừng nói X"
(bot copy nguyên ra cho khách).

---

## Patch 1 — Chatty · `kb/faq/ai-agent-settings.md`

**Correction nguồn:** #1 Phoebe (13/07, chat tiếng TBN) + #5 Andy (14/07, chat tiếng Trung)

**Lỗi Ivy:** Cả 2 ca đều trỏ khách vào `AI agent → Instructions → Manage → General
instructions → Role` để đổi tên. Sai. CS sửa thành 2 đáp án khác nhau vì đó là 2 cái
tên khác nhau:
- Phoebe: tên **AI agent** → `AI agent → Settings → Name`
- Andy: tên trong ảnh khách là tên **team/operator** → `Team settings`

**Chẩn đoán:** KB hiện có mục "AI Identity" nói đúng là Name nằm ở `AI agent → Settings`,
nhưng **không hề phân biệt** với tên team, và không có tag nào chặn Ivy trượt sang
"Role instructions". Ivy đang gộp 3 thứ (AI name / team name / role prompt) làm một.

**Sửa:** thay nguyên khối `## AI Identity` bằng bản dưới. Phần còn lại của file giữ nguyên.

### Nội dung mới

```markdown
## AI Identity

Customize the AI's name and avatar, shown to customers in conversations.
Path: **AI agent → Settings**.

- **Name**: The name shown to customers in the chatbox. Set it at
  **AI agent → Settings → Name**.
- **Avatar**: Choose a preset avatar, or upgrade to upload a custom image
- **Welcome message**: The first message customers see. Click **Insert customer name**
  to personalize it with the customer's name.

### Which "name" does the merchant mean? (three different fields)

Chatty has three separate name/identity fields. Identify which one the merchant is
pointing at before giving a path — a screenshot usually makes it obvious.

| What they want to change | Where it lives | What it affects |
|---|---|---|
| **AI agent name** — the name customers see when the AI replies | **AI agent → Settings → Name** | The AI's display name in the chatbox |
| **Team member / operator name** — the name on a human agent's profile | **Settings → Team → Manage** (edit the member) | The name customers see when a human replies |
| **Role / persona instructions** — how the AI describes itself and behaves | **AI agent → Instructions → Manage → General instructions → Role** | The AI's tone and self-description, **not** its display name |

**Common request — "make the AI introduce itself as our brand, not as an AI / not as
Chatty":** this is two settings working together.
1. Set the display name at **AI agent → Settings → Name** to the brand name.
2. Describe the persona at **AI agent → Instructions → Manage → General instructions →
   Role** (e.g. "You are the support assistant for BRAND").

Changing the Role text alone does **not** change the display name — the name field is
what customers see on the message.
```

**Tags cần thêm vào frontmatter** (cuối list tags hiện có):

```yaml
    - "change AI name"
    - "rename AI"
    - "AI display name"
    - "team member name"
    - "operator name"
    - "agent name"
    - "cambiar nombre"
    - "nombre del asistente"
    - "修改名字"
    - "改名"
```

---

## Patch 2 — Chatty · `kb/faq/team.md`

**Correction nguồn:** #5 Andy (14/07)

**Lỗi:** Ivy không biết tên team member sửa ở đâu, nên đẩy khách sang Role instructions.

**Chẩn đoán:** File `team.md` nói cách **mời** member, **assign**, **deactivate** — nhưng
không có chỗ nào nói **sửa tên** một member đã có. Đây là GAP thật.

**Sửa:** chèn mục mới ngay sau khối `## Inviting Team Members`, trước `---` và
`## Assigning Conversations`.

### Nội dung mới

```markdown
---

## Editing a Team Member's Name

The name shown to customers when a **human agent** replies comes from that team
member's profile — not from the AI agent settings.

1. Go to **Settings** → **Team** → **Manage**
2. Click the member you want to edit
3. Update the **Name** → **Save**

Note: the **email** of a member cannot be changed after the invite is sent.

> Don't confuse this with the **AI agent's** name, which customers see when the AI
> replies — that one is at **AI agent → Settings → Name**. See kb_ai-agent-settings.
```

**Tags cần thêm:**

```yaml
    - "edit member name"
    - "change team member name"
    - "rename agent"
    - "operator name"
    - "team settings name"
```

---

## Patch 3 — Chatty · `kb/faq/faqs-block.md`

**Correction nguồn:** #4 Jade (14/07)

**Lỗi Ivy — nặng nhất tuần:** khách nói *"we don't need AI agent, we want each product
to display its own FAQs"*, Ivy trả lời:

> "go to AI agent → Training data → Products, pick the product, and click Add FAQs or
> Manage FAQs to attach questions directly to that product"

**Flow này không tồn tại.** Ivy hallucinate một tính năng. CS sửa thành: tạo FAQs block
cho từng nhóm sản phẩm → display condition `Product pages → By collection/tag`.

**Chẩn đoán:** KB `faqs-block.md` thực ra **đã có** đúng thông tin (bước 5, display
condition có By collection / By tag). Nhưng khách hỏi bằng ngôn ngữ "per-product FAQ" và
lại kèm chữ "AI agent" → Ivy retrieve nhầm sang training-data. KB thiếu một mục nói
thẳng use-case này bằng đúng từ khách dùng.

**Sửa:** chèn mục mới ngay sau `## FAQs Block Overview`.

### Nội dung mới

```markdown
## Showing Different FAQs on Different Products

To give each product (or group of products) its own set of FAQs on the storefront,
use **FAQs blocks** — this works with or without the AI agent, and does not require
the AI agent at all.

1. Go to **FAQs** → **FAQs block** → **Add block**
2. Click **Browse** and select the questions for this group of products
3. Under display condition, tick **Product pages** and choose:
   - **By collection** — show this block only on products in a given collection
   - **By tag** — show this block only on products carrying a given tag
4. **Save**, then add the block to the product template in the theme editor
   (**Add section** → **Chatty FAQs block** → paste the Block ID)
5. Repeat: create one block per collection/tag, each with its own questions

There's no limit on the number of blocks, so a store can have as many product-specific
FAQ sets as it needs.

> This is a **storefront display** feature and is separate from **AI agent → Training
> data**, which teaches the AI to answer in chat. Adding FAQs to a block does not
> require the AI agent to be active.
```

**Tags cần thêm:**

```yaml
    - "per product faq"
    - "each product own faq"
    - "product specific faq"
    - "different faq per product"
    - "faq by tag"
    - "faq by collection"
    - "faq without ai"
```

---

## Patch 4 — Joy · `kb/reference/earning-programs.md`

**Correction nguồn:** #2 Jade (14/07) — khách Maison Koko

**Lỗi Joyce:** khách hỏi set 1.5 điểm/$ cho tier "Koko Steeper" và 2 điểm/$ cho tier
"Koko Master". Joyce trả:

> "you'd need to bridge it with Shopify Flow (segment members by tier tag, then award a
> calculated point amount per order)"

Sai — Joy làm được natively. CS sửa: cấu hình qua **Place Order program**, nhưng cần
**upgrade lên Rule Engine** trước (ở Earning programs).

**Chẩn đoán:** `earning-programs.md` mô tả rate cơ bản (1 pt/$1) nhưng **không nói** cách
đặt rate KHÁC NHAU theo VIP tier. `rule-engine.md` có nhắc "Customer segment | Bonus for
VIP tier" trong bảng use-case nhưng quá mờ, không có path.
→ Joyce không nối được, nên bịa ra Shopify Flow.

> 🔍 **ĐÃ VERIFY TỪ SOURCE JOY (GitLab `avada/starlink-team/joy`, master) — 14/07.**
> Correction của Jade đúng ở chỗ "Joy làm được natively, không cần Shopify Flow", nhưng
> **2 chi tiết bị lệch**, và mình viết KB theo source:
>
> 1. **KHÔNG cần Rule Engine.** VIP-tier rate là một option trong nhóm radio
>    *"Who to reward"* của chính program Place order. Nó render ở **cả** bản cũ
>    (`PlaceOrderProgram.js:910`) lẫn bản Rule Engine (`PlaceOrderV2Program.js:1281`).
>    Gate duy nhất: **VIP Tier program phải đang bật** — chưa bật thì radio xám kèm
>    helptext *"You haven't setup VIP Tier yet"*. VIP Tier chỉ cần **plan trả phí bất kỳ**
>    (`isPremium(shop)` = PLAN_TIER_0, tức Pro/Essential là đủ). Rule Engine gate ở
>    Advanced+ nhưng **không liên quan** tới tính năng này.
> 2. **KHÔNG có field "VIP tier" trong panel "Check if".** Condition builder của Place
>    order chỉ có 7 field customer (`const/option.js` → `conditionCustomerOptionsI18n`):
>    City, Location, Email, Phone, Customer status, Customer tag, Tax exempt.
>    Chọn tier xong, form **tự đẻ ra một ô nhập rate cho từng tier**
>    (`earnPointsTiers[tierId]`, `PlaceOrderV2Program.js:1348-1400`).

**Sửa:** chèn mục mới ngay sau khối `## Reward methods`.

### Nội dung mới

```markdown
---

## Different earning rates per VIP tier (points multiplier)

A merchant can give each VIP tier its own earning rate — e.g. **1.5 points per $1 for a
mid tier and 2 points per $1 for the top tier**. This is built into the **Place an order**
program. It does **not** need Shopify Flow, and it does **not** need the Rule Engine.

**Requirement:** the shop must already have a **VIP Tier program set up and enabled**
(VIP Tiers is available on any paid plan). If VIP Tiers isn't set up, the tier option on
the Place-order program is greyed out with the note *"You haven't setup VIP Tier yet"* —
set up the tiers first.

**How to set it up:**

1. Go to **Joy Admin → Reward programs → Earning programs → Place an order**
2. Find the **"Who to reward"** options and select
   **"Only customers in a VIP tier can earn points"**
3. The form then shows **one earning-rate field per tier** — enter each tier's own rate
   (e.g. 1.5 points per $1 for the mid tier, 2 points per $1 for the top tier)
4. **Save**

Each tier now earns at its own rate, and a customer earns at the rate of whichever tier
they are currently in.
```

**Tags cần thêm:**

```yaml
    - "points multiplier"
    - "multiplier"
    - "tier multiplier"
    - "rate per tier"
    - "different rate per tier"
    - "1.5x points"
    - "2x points"
    - "vip tier earning rate"
```

> ⚠️ **Một điểm cần Liz confirm:** patch này viết theo lời CS sửa (Place order + Rule
> Engine + điều kiện Customer theo tier). Mình chưa verify được **chính xác** condition
> chọn VIP tier nằm ở đâu trong panel "Check if" (KB hiện chỉ ghi chung là
> Customer/Order/Product/Collection). Nếu Liz confirm được đúng field, mình chỉnh lại
> bước 4 cho khớp trước khi push.

---

## Patch 5 — Joy · `kb/case/widget.md`

**Correction nguồn:** #1 Sonny (13/07)

**Lỗi Joyce:** khách gửi ảnh, xin dời widget lên trên nút Add to Cart. Joyce bảo khách
tự làm được qua `Widget → Settings → Launcher → Alignment`. CS sửa: cái này cần tech
team can thiệp **CSS**, phải escalate.

**Chẩn đoán — khác 3 ca trên:** KB **đã đúng sẵn**. Mục "Unified widget float button
overlaps the mobile checkout button" có đủ 4 bước, và **Step 4 nói rõ**: pixel-precise
placement → collect screenshot + escalate + CSS. Joyce đọc tới Step 1 rồi dừng, hứa luôn
với khách.

→ Đây là lỗi **ordering/ưu tiên**, không phải KB thiếu data. Patch nhẹ: đưa tín hiệu
"khách gửi ảnh / muốn vị trí chính xác" lên **đầu** mục để Joyce gặp trước Step 1.

**Sửa:** thay khối `**Resolution Steps:**` trong mục "Unified widget float button
overlaps the mobile checkout button" bằng bản dưới.

### Nội dung mới

```markdown
**First, split the request into two kinds:**

- **"Move it away from the checkout/Add-to-Cart button"** (rough clearance is enough) →
  the built-in launcher settings can do this. Go to Step 1.
- **"Put it exactly here"** — the merchant sends a **screenshot/mockup with a target
  position**, or asks to place it relative to a specific theme element (above the
  Add-to-Cart bar, inside a section, etc.) → the built-in settings **cannot** do this.
  It needs custom CSS from the team. Go straight to Step 4 and escalate; do not tell
  the merchant they can do it themselves in Launcher settings.

**Resolution Steps:**
- **Step 1:** Reposition the launcher — **Settings → Launcher → Alignment** and adjust
  position/offset so it clears the checkout button.
- **Step 2:** Use page-hide rules to hide the widget on cart/checkout pages where it
  conflicts.
- **Step 3:** If the merchant prefers, they can switch back to **Classic** while the
  issue is logged.
- **Step 4:** For pixel-precise placement, collect a screenshot + device + page URL and
  escalate to the team to apply targeted CSS via collaborator access. Append
  `<escalate_human>` to the reply.
```

---

## 2 correction KHÔNG patch

**#2 Ivy — Andy (13/07)** — khách nói "okay thanks!", Ivy trả "our team is still looking
into the order recall issue", CS sửa: *"Báo khách xong rồi mà, làm gì còn still looking
into the issue nữa"*.
→ Lỗi **context/state**, không phải kiến thức. Ivy không biết case đã resolve. Không có
KB nào sửa được — thuộc về logic đọc trạng thái conversation. Nếu lặp lại nhiều, mình
gom lại thành issue riêng gửi team dev.

**#3 Ivy — Andy (13/07)** — khách gửi ảnh order SF#12292, Ivy bảo "this looks like a
genuine lookup issue on the AI's end", CS sửa: *"Trong ảnh mới có Order ID thôi. Track
order cần cả order ID lẫn email/phone"*.
→ Cái này **có thể** là GAP ở `kb/faq/order-tracking.md` (điều kiện cần để tra order).
Mình chưa đọc file đó nên chưa dám soạn patch. Nếu Liz muốn, mình check thêm và bổ sung
Patch 6.

---

## Tóm tắt để duyệt

| # | App | File | Loại | Rủi ro |
|---|-----|------|------|--------|
| 1 | Chatty | `kb/faq/ai-agent-settings.md` | Thay khối AI Identity + tags | Thấp — làm rõ 3 field |
| 2 | Chatty | `kb/faq/team.md` | Thêm mục Edit member name | Thấp — GAP thật |
| 3 | Chatty | `kb/faq/faqs-block.md` | Thêm mục per-product FAQ | Thấp — chống hallucinate |
| 4 | Joy | `kb/reference/earning-programs.md` | Thêm mục tier multiplier | ⚠️ Cần confirm bước 4 |
| 5 | Joy | `kb/case/widget.md` | Đảo ưu tiên escalate | Thấp — KB vốn đúng |

Liz duyệt xong, mình push qua `push_kb.py` rồi **reindex** cả 2 agent (không reindex thì
bot vẫn dùng bản cũ).
