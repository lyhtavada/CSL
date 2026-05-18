# Chatty — Pre-Chat Page Journey Report

**Scope:** 83 review sessions (Mar–May 2026), Group G2 Retention  
**Sessions with page data available:** 16 / 83  
**Note:** Crisp chỉ lưu browsed pages trong thời gian ngắn — 67 sessions cũ hết data. Kết quả dưới đây dựa trên 16 sessions gần nhất.

---

## Feature Areas Merchant Đang Browse Khi Chat

| Feature Area | Sessions |
|--------------|---------|
| Inbox / Live Chat | 12 |
| AI Assistant (general) | 6 |
| Settings (general) | 6 |
| Widget (general) | 5 |
| FAQs (general) | 5 |
| Widget Chat Page | 4 |
| Notification Settings | 4 |
| Campaigns | 3 |
| FAQ Editor | 3 |
| AI Settings | 3 |
| Subscription / Plans | 3 |
| Widget Appearance | 2 |
| AI Training Data | 2 |
| AI Instructions / Scenarios | 2 |
| Integrations | 1 |
| Translation Settings | 1 |
| AI Unresolved Questions | 1 |
| Analytics | 1 |

---

## Key Observations

### 1. Inbox / Live Chat là nơi merchant bị stuck nhiều nhất (12/16 sessions)
Merchant đang xem inbox trước khi chat — nhưng không phải vì họ đang dùng live chat, mà thường là:
- Đang cố tìm hiểu cách assign conversation, set up notification
- Không biết cách dùng inbox UI (filter, resolve, my-inbox vs inbox)
- Đang check AI handover — xem conversation bị transfer như thế nào

**Implication:** Inbox UX có thể còn confusing. Tooltip hoặc onboarding guide trong inbox sẽ giảm support load.

### 2. Widget + FAQ — merchant tự mày mò trước khi hỏi
- 5 sessions browse `/widget` → sau đó hỏi về customization
- 5 sessions browse `/faqs` → sau đó hỏi cách edit, add, hoặc setup FAQ page
- Pattern: merchant **thử tự làm trước**, stuck, rồi mới chat → CS vào làm thay → review

**Implication:** Đây là nhóm **dễ xin review nhất** vì merchant đã cố tự làm → CS giải quyết nhanh → contrast rõ → appreciation cao.

### 3. AI Assistant — merchant đang explore, chưa biết bắt đầu từ đâu
- 6 sessions browse `/ai_assistant` (general) trước khi hỏi
- Mix giữa settings, training data, instructions, unresolved questions
- Thường là merchant mới kích hoạt AI, chưa biết configure gì trước

**Implication:** Onboarding checklist cho AI setup sẽ giảm "I don't know where to start" questions.

### 4. Notification Settings — pain point rõ ràng
4 sessions browse `/settings/detail/notifications` → đây là feature merchant hay bị miss (không nhận được notification khi có chat mới). CS thường phải guide step by step hoặc gửi video.

### 5. Subscription / Plans — merchant đang cân nhắc upgrade
3 sessions browse `/subscription` trước khi chat → có thể đang cân nhắc upgrade hoặc hỏi về billing. Đây là opportunity để CS upsell và xin review trong cùng 1 session.

---

## Per-Session Detail

| Store | Agent | Pages Visited |
|-------|-------|--------------|
| Naïvia | hienpt | Subscription → Translation → Settings → Widget → AI products → AI skills → AI assistant → FAQs → Notifications |
| Onyx / Onyx Products | linhtlk / hanghm | Inbox → Notifications → FAQ editor → FAQs → AI settings → Campaigns |
| GuguSure | hienpt | Inbox (nhiều conversations) → Widget → Widget chat page → Widget appearance |
| wāk | anhbd | Inbox → Settings → Notifications → Profile → Shortcut creator |
| HammerHouse | phuongttm.ctv | Inbox (nhiều conversations) → Settings |
| Hediye Kutusu | phuongttm.ctv | Inbox → Widget → Widget chat page → AI assistant → AI settings |
| More shopping | minhbt.ctv | Inbox → AI unresolved → AI assistant → Subscription → Settings → Campaigns → AI scenarios → AI skills |
| Martin & Pleasance | vanct | Analytics → Inbox → FAQs → Integrations → Order tracking |
| American Heritage | hienpt | Inbox → Contacts → Settings |
| Kezia Club | hienpt | Inbox → FAQs → Widget chat page → Widget → FAQ block/page |
| Cyo Design | hanghm | Widget advanced → Widget → Widget appearance → Widget chat page |
| Levaxco | hienpt | Inbox → AI training (FAQs) |
| End Nutrition | hanghm | AI assistant |
| CNSAC MedShop | vanct | Settings → Subscription/Plans |
| Gladesville Guitar Factory | phuongnt01 | Inbox (direct link) |

---

## Recommendations cho Product Team

### Quick wins
1. **Inbox onboarding tooltip** — hướng dẫn ngắn "my-inbox vs inbox", cách filter, assign — giảm support load từ nhóm lớn nhất
2. **Notification setup wizard** — thay vì merchant tự mày mò settings, có 1 flow setup notification guided (email + mobile)
3. **AI setup checklist** — khi merchant kích hoạt AI lần đầu, show checklist: Training data → Instructions → Test AI → Go live

### Longer term
1. **Widget customization preview** — merchant đang browse widget/appearance nhiều → live preview sẽ giảm "tôi không thấy thay đổi" questions
2. **Subscription upgrade prompt** — khi merchant browse `/subscription` + đang chat → CS có thể proactively offer deal → convert upgrade + xin review cùng lúc
