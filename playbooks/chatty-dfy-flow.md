# Chatty DFY — CS Flow & Checklist

**Owner:** Liz (CS Leader)
**Created:** 2026-05-27

---

## 1. Scope — Khi nào áp dụng DFY

**Eligibility (thỏa ít nhất 1 trong các nhóm):**
- **New install** — cài app trong vòng 30 ngày, chưa setup gì
- **Installed but inactive** — cài lâu nhưng widget vẫn default (chưa đổi màu, chưa có FAQ, AI chưa train)
- **Active but not on-brand** — đang dùng nhưng widget chưa match theme store

**KHÔNG tạo ticket DFY nếu:**
- MC đã có ticket DFY active (chưa close) → update ticket cũ thay vì tạo mới

---

## 2. Modules

CS offer 3 module độc lập. MC có thể nhận 1, 2 hoặc cả 3 tùy nhu cầu.

| Module | Nội dung | Ai làm |
|--------|----------|--------|
| **M1 — Chatbox** | Widget branding + proactive chat (product recommendation) | CS setup → KH duyệt |
| **M2 — FAQ** | Add FAQ từ file sẵn + FAQ page | CS setup → KH duyệt |
| **M3 — AI** | AI brand settings + human handover + sync URLs | CS setup với input từ KH |

**Thứ tự ưu tiên nếu làm cả 3:** M1 → M2 → M3
> M1 cho KH thấy kết quả ngay. M3 cần input từ KH nhiều nhất nên để cuối.

---

## 3. CS Flow

DFY entry point chính: **email onboarding → KH click CTA → redirect về app → live chat tự pop-up offer**. CS cũng có thể chủ động offer trực tiếp khi phát hiện store eligible (shortcut `!chatty-dfy-offer`).

### 3.0 — Trigger pop-up khi KH vào từ email

Khi KH click CTA trong email onboarding → redirect về app → live chat pop-up message offer **cả gói DFY** (M1+M2+M3). Tone ngắn gọn, đi thẳng, 1 CTA.

**Template pop-up (gửi KH):**
> 👋 Glad you made it! Your free done-for-you setup is ready — branded widget, FAQs, and AI all handled by me.
>
> Want me to start? Just reply **"yes"** 👇

> **Lưu ý:** Dòng mở đầu nên khớp với CTA trong email. VD email "Get my free setup" → pop-up "Your **free setup** is ready"; email "Claim my done-for-you service" → "Let's get your **done-for-you setup** started".

### 3.1 — Sau khi KH reply "yes"

**Bước 0 — Chốt + tạo ticket (ngay, đừng để KH nguội):**
> Awesome, let's do it! 🙌 I'll take a look at your store and start setting things up. Give me a bit and I'll show you the first result shortly.

→ Tạo ticket DFY → set label `DFY-new` → bắt đầu đếm SLA 48H.

**Bước 1 — CS audit store** (không cần hỏi KH): widget đang default hay đã custom? FAQ có chưa / KH có file FAQ không? AI đã train chưa, plan có AI không? → update label `DFY-in-progress`.

**Bước 2 — Làm theo thứ tự M1 → M2 → M3.** Pop-up offer cả gói để KH thấy giá trị, nhưng khi *làm* vẫn tuần tự — M1 là quick win tạo niềm tin, M3 cần input KH nhiều nhất nên để cuối.

**M1 — Chatbox** (CS tự làm, nhanh trong vài giờ đầu):
- Setup branding + proactive chat ở trạng thái **draft** → preview → **quay video ngắn** → gửi KH duyệt:
  > Here's how your new chat widget looks 👇 [video]. Want me to adjust anything, or should I make it live?
- KH duyệt → activate.

**M2 — FAQ** (cần KH gửi file, hoặc CS tự soạn bộ cơ bản từ store):
> Next, I can set up your FAQs so customers self-serve the common questions. Got a list/file already? Send it over — or I'll draft a starter set from your store and you just review.

- Import FAQ → setup FAQ page → preview → gửi duyệt → activate.

**M3 — AI** (nhiều input nhất, để cuối):
- Gửi KH **pre-session checklist** (§4) để collect input:
  > Last one — let's get your AI assistant trained. Quick checklist so I set it up right 👇 [checklist]
- Có đủ info → setup brand voice + handover + sync URLs → test → confirm với KH.

**Bước 3 — Done + xin review:** gắn label module hoàn thành (`DFY-M1` / `DFY-M2` / `DFY-M3`) → nếu convert được review: gắn `review-yes` + post ảnh/video vào comment (tính point) → **không close ngay**, để mở chờ follow-up.

**Bước 4 — Follow-up sau 2–5 ngày** → check store:
- **Có adopt** → gắn `DFY-adopted` → close ticket
- **Không phản hồi / chưa adopt** → gửi reminder (template `!dfy-remind`) → gắn `DFY-no-adopt` → close ticket

### 3.2 — Nếu CS chủ động offer (không qua email)

Khi CS tự phát hiện store eligible trong lúc xử lý chat khác → dùng template offer trực tiếp (mở đầu bằng audit), rồi vào flow từ Bước 0:
> Hey, I took a look at your store and noticed your Chatty widget is still on the default setup, so I'd love to offer you something.
>
> We have a **done-for-you setup** (completely free) where I personally set it up to fit your store: your colors, your logo, your tone — plus FAQs and AI if you want. Built around how your store looks and what your customers need, not a generic template.
>
> Interested? Just let me know and I'll get started. No setup needed on your end, and you can still adjust anything you want.

> SLA: Có kết quả và báo KH trong vòng **48H** sau khi tạo ticket. Quá 48H không update → escalate Liz.

> **Tính point:** Follow-up đúng hạn + gắn đủ tag là điều kiện bắt buộc để ticket được tính.

---

## 4. Bộ câu hỏi thu thập thông tin — Ivy bot tự hỏi trong chat

> **Đây là câu hỏi Ivy bot tự động hỏi KH trong live chat** (bot-driven), không phải CS người hỏi thủ công. Wording đã viết theo tone merchant-friendly — bot dùng gần như nguyên văn. CS chỉ vào cuộc khi KH cần người hoặc bot bí input.
>
> Hai bộ câu hỏi tách theo module: **Chatbox (M1)** hỏi khi setup widget; **AI Agent (M3)** hỏi khi train AI. Mỗi câu trả lời map thẳng vào checklist kỹ thuật §5 để CS/bot thực thi.

### 4.1 — Chatbox setup (M1)

1. What colors or style feel like your brand, so the chat blends in naturally on your storefront?
2. Besides live chat, would you like customers to see other ways to reach you here — like email or phone?
3. What do customers usually ask you about? I'll turn those into one-tap starter buttons so they get answers in seconds.
4. Would it help to gently ask for a name and email before chatting, so you can always follow up and never miss a customer?
5. I'd suggest showing the chat on every page and on mobile too, so customers can reach you wherever they are — sound good?

### 4.2 — AI Agent setup (M3)

1. What would you like to call your assistant, and how should it greet your customers?
2. Would you like it to always be there for customers, or only step in when you're away — and what are your usual active hours?
3. Where would you like to get notified when a new chat comes in — web push, email, or both?
4. Tell me a bit about your brand and products, and how you'd like your assistant to sound — warm and casual, or more polished? Also, are there any topics or things you'd rather it not say or handle, so I can set the right boundaries?
5. When a customer needs a real person — whether it's a general question or an after-sales request like a return, refund, or order change — how would you like it routed to you? I can set it up to: (1) transfer the chat straight into your Chatty inbox, (2) collect their details and follow up by email, or (3) simply show your contact info so they can reach you directly.
6. Would you like the assistant to be able to look up a customer's order status directly, or should that always go to you?

---

## 5. Checklist theo module

### M1 — Chatbox + Proactive Chat

*Chatbox* (map câu hỏi §4.1)
- [ ] Background color match brand primary color *(← câu 1: brand color/style)*
- [ ] Custom launcher icon (nếu brand có icon riêng)
- [ ] Logo đã upload
- [ ] Heading text viết lại theo brand tone
- [ ] Description text viết lại theo brand tone
- [ ] Order tracking bật/tắt phù hợp (chỉ bật nếu store dùng tracking)
- [ ] FAQs block — chọn featured questions phù hợp
- [ ] Contact info đúng — thêm email/phone nếu KH muốn kênh khác ngoài chat *(← câu 2)*
- [ ] Primary color match brand *(← câu 1)*
- [ ] Starter buttons (quick replies) từ câu KH hay hỏi — one-tap để KH có đáp án nhanh *(← câu 3)*
- [ ] Pre-chat form — bật thu name + email trước khi chat (nếu KH đồng ý) để không miss lead *(← câu 4)*
- [ ] Display: bật trên **mọi trang** + **mobile** (mặc định recommend, xác nhận với KH) *(← câu 5)*

*Proactive Chat — Product Recommendation*
- [ ] Message text viết lại theo brand tone
- [ ] Product logic phù hợp (default: Best sellers — hỏi KH nếu muốn khác)
- [ ] Trigger: All product pages (hỏi KH nếu muốn specific pages)
- [ ] Background color + text color match brand
- [ ] Campaign ở trạng thái **draft** — gửi KH duyệt trước khi activate

---

### M2 — FAQ

*Nội dung FAQ*
- [ ] Có nguồn FAQ — KH gửi file, hoặc CS soạn bộ starter từ store (policy, shipping, returns, sizing, payment)
- [ ] Tạo/đặt category hợp lý (mặc định có sẵn "Order & Shipping", "Exchange & Return" — edit cho khớp store)
- [ ] Import questions (CSV bulk nếu file lớn — 5 field: Question, Answer, Category, Published, Featured; max 1MB)
- [ ] Featured questions — chọn câu hay hỏi nhất để hiện ở trang đầu chatbox
- [ ] Answer viết lại theo brand tone, không sai chính sách store
- [ ] Mọi question + category để **Published** (không sót Draft)

*FAQ Page*
- [ ] Bật **Display FAQs page** + set URL
- [ ] Layout + màu (title/question/background) match brand, đủ tương phản
- [ ] Heading + description viết theo brand tone
- [ ] Bật **Contact us section** → cấu hình click behavior (mở chat/redirect đúng)
- [ ] Thêm FAQ page vào store navigation (Main menu / Footer) nếu KH muốn

*Recommended*
- [ ] FAQs block trên product page cho câu hỏi product-specific (nếu store phù hợp)
- [ ] Branding removal (nếu KH ở plan cho phép)

---

### M3 — AI

> ⚠️ AI nâng cao (Instructions, Scenarios, Custom Q&A, Data Source mở rộng) chỉ có trên **paid plan**. Check plan KH trước khi setup — Free plan AI rất hạn chế.

*Brand voice & Instructions* (AI Assistant → Instructions) — map câu hỏi §4.2
- [ ] Bot name + welcome/greeting message + avatar theo brand (thay default "Chatty AI") *(← câu 1: tên + cách chào)*
- [ ] Custom Instructions — brand tone/voice theo input KH (warm & casual / polished, ngôn ngữ, độ dài câu) *(← câu 4: brand + products + tone)*
- [ ] Instruction "Always respond in the same language as the customer" (nếu store đa ngôn ngữ)
- [ ] **Boundaries** — instruction né các topic/việc KH không muốn bot xử lý hoặc nói *(← câu 4: things you'd rather it not say/handle)*

*Data Sources* (AI Assistant → Data Sources)
- [ ] Sync Products — verify số lượng không vượt giới hạn plan (Free 100 / Basic 500 / Pro 8K / Plus 20K)
- [ ] Auto-sync store pages đã chạy (Shipping/Return/Privacy/Terms/FAQ/Contact/About — tự sync, verify đủ)
- [ ] Add URLs ngoài KH cung cấp vào Custom Knowledge (submit từng page URL, không chỉ domain)
- [ ] Upload file KH gửi nếu có (.CSV/.PDF/.TXT/.JSON, max 2MB; CSV ưu tiên cho dữ liệu có cấu trúc)
- [ ] Custom Q&A pairs cho thông tin chưa có trong product/page

*Handover & Transfer* (AI Assistant → Transfer) — map câu hỏi §4.2
- [ ] Contact Support Email đúng (AI lấy email từ đây)
- [ ] **Routing khi KH cần người** — chốt theo lựa chọn KH ở câu 5 (general Q hoặc after-sales: return/refund/order change): *(← câu 5)*
  - (1) **Transfer** chat thẳng vào Chatty inbox, hoặc
  - (2) **Collect details** → follow up qua email, hoặc
  - (3) **Show contact info** để KH tự liên hệ
- [ ] **Availability mode** — always-on (bot luôn trả) hay chỉ step-in khi team away; set đúng *(← câu 2)*
- [ ] Online hours / active hours đã set đúng (để AI báo đúng khi team offline) *(← câu 2)*
- [ ] **Notification channel** — set nơi KH nhận thông báo khi có chat mới: web push / email / cả hai *(← câu 3)*
- [ ] Assignment mode — recommend Automatic (round-robin) thay vì Manual
- [ ] **Order lookup** — bật cho AI tra order status trực tiếp, hoặc route về người (theo lựa chọn KH) *(← câu 6)*

*Scenarios* (Instructions → Assistant Skills → Custom Scenarios)
- [ ] Tạo scenario cho flow đặc thù store (returns, order lookup, discount, size guide…) theo input KH

*Test trước khi live* (AI Assistant → Test)
- [ ] Test các câu hỏi chính bằng feature **Test** (KHÔNG tốn quota, KHÔNG test trên live chat KH)
- [ ] Verify AI trả lời đúng tone + đúng thông tin → confirm KH → activate

---
