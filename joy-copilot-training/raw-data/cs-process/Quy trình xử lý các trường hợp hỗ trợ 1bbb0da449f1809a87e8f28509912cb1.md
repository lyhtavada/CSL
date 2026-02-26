# Quy trình xử lý các trường hợp hỗ trợ

Owner: Ly Hoàng
Created time: March 19, 2025 2:56 PM

## Phần 1: Decision Tree - Merchant liên hệ về gì?

```
Merchant reaches out
        ↓
  [Phân loại issue]
        ↓
    ┌───┴───┐
    ↓       ↓
Questions  Problems

```

### **Priority Matrix**

| Priority | Definition | Examples | Response Time | Resolution Target |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **P0 - Critical** | App down, data loss, security issue, affects all merchants or financial loss to merchants,  | App won't load, all points deleted, payment processing broken, buyers cannot add to cart or checkout | Immediate | 4-24 hours |  |  |
| **P1 - High** | Core feature broken, affects merchant business | Rewards can't be redeemed, reviews not displaying, chatbot not responding | 2-4 hours | 1-5 days |  |  |
| **P2 - Medium** | Minor feature issue, workaround available | Email delay, minor display issue, non-critical feature glitch | 4-24 hours | 1-2 weeks |  |  |
| **P3 - Low** | Cosmetic issue, enhancement | Color alignment, text typo, minor UI inconsistency | 1-2 days | Backlog |  |  |

## Phần 2: Các trường hợp hỗ trợ và quy trình xử lý

> 👉 CS tham khảo thêm: [Các kênh trao đổi & Hướng dẫn Escalation](https://www.notion.so/C-c-k-nh-trao-i-H-ng-d-n-Escalation-280b0da449f180199ca0e226c0b450bc?pvs=21)
> 

|  | Case | Ví dụ | Phân loại | Quy trình | Khi nào escalate? |
| --- | --- | --- | --- | --- | --- |
| 1 | How-to Questions (Câu hỏi cách sử dụng) | "How do I create a reward?"
"Where can I see my customer points?"
"How do I customize the widget color?"
"Can customers redeem points at checkout?” | **Handler:** CS Agent

**Priority:** Normal

**SLA:** 4-24 hours first response | **Step 1: CS nhận chat**
↓
**Step 2: Check knowledge base**
- Có article sẵn?
- Documentation đầy đủ?
↓
**Step 3: Provide answer**
- Link to documentation
- Step-by-step instructions
- Screenshots if helpful
↓
**Step 4: Follow up**
- "Did this help?"
- Offer additional assistance
↓
**Step 5: Close chat (optional)**
- Mark as resolved
- Update KB if needed | - Question về advanced technical configuration → TS qua [Trello card](https://www.notion.so/Quy-t-c-khi-t-o-card-b-ng-CS-Extension-65c7b896321a4e3195e7065390f9cf04?pvs=21)
- Question về feature không tồn tại →  PM qua Slack channel
- Question relates to bug → Follow Case 3 |
| 2 | Feature Requests (Yêu cầu tính năng mới) | "Can you add tier expiration feature?"
"I need to export customer points data"
"Can rewards be applied automatically?"
"Integration with [app name]?” | **Handler:** CS Agent (collect) → PM/BA (evaluate)

**Priority:** Low (unless multiple merchants)

**SLA:** Acknowledge within 24h, evaluation timeline varies | **Step 1: CS nhận feature request**
↓
**Step 2: Understand the need**
- Why do they need this?
- What's their use case?
- Workaround available?
↓
**Step 3: Check existing features**
- Does this exist already?
- Can current features solve this?
↓
├─→ YES: Guide merchant
│
└─→ NO: Document request
↓
**Step 4: Document detailed request**
- Merchant info
- Use case
- Business impact
- Similar requests count (optional)
↓
**Step 5: Submit to Product team**
- Add to feature request [Trello board](https://trello.com/b/7abgoJwX/avada-feature-request-board)
- Tag PM/BA in #slack-channel nếu cần thiết
↓
**Step 6: Set merchant expectations**
- "We've forwarded to Product team"
- "No timeline yet"
- "Will update if prioritized"
↓
**Step 7: Follow up monthly**
- Check status with PM
- Update merchant if any movement | **When to escalate to PM:**
- Request from multiple merchants (5+)
- VIP merchant request
- Request aligns with known roadmap
- Urgent business need |
| 3 | Issue/Bug Reports (Báo cáo lỗi) | "Points not being credited"
"Widget not displaying"
"Email notifications not sending"
"App crashed when I clicked X” | **Handler:** CS (triage) → TS (investigate) → Dev (fix)

**Priority:** Varies (P0 to P3)

**SLA:** Depends on priority | **Step 1: CS nhận bug/issue report**
↓
**Step 2: Initial triage**
✓ Read merchant description carefully
✓ Ask clarifying questions if needed
↓
**Step 3: Basic troubleshooting**
✓ Check merchant settings
✓ Verify app is installed correctly
✓ Check if program/feature is active
✓ Review recent changes merchant made
✓ Test on test store if possible
↓
**Step 4: Can CS resolve?**
↓
├─→ YES: It's configuration issue
│   → Guide merchant to fix
│   → Verify fix works
│   → Close ticket
│
└─→ NO: Likely technical bug
↓
**Step 5: Gather evidence**
✓ Screenshots
✓ Screen recording
✓ Steps to reproduce
✓ Console errors (if merchant can provide)
✓ Store URL
✓ Affected features
↓
**Step 6: Assess priority**
[Use priority matrix below]
↓
**Step 7: Escalate to TS/ dev** 
→ [Create Trello Card](https://www.notion.so/Quy-t-c-khi-t-o-card-b-ng-CS-Extension-65c7b896321a4e3195e7065390f9cf04?pvs=21)
↓
**Step 8: Update merchant**
→ "Escalated to technical team"
→ Set expectations on timeline
→ Provide ticket reference |  **When to escalate to PM/ techlead:**
-  CS xác định rõ đây là bug cần dev fix (không phải config issue). CS tạo card và escalate lên nhóm app tương ứng.

**Conditions để escalate trực tiếp:**
✅ CS đã troubleshoot kỹ (confirmed không phải merchant setting)
✅ Bug rõ ràng, có steps to reproduce chính xác
✅ Có đầy đủ evidence (screenshots, video, store URL)
✅ Đã assess priority (P0/P1/P2/P3) |
| 4 | Billing & Subscription (Thanh toán & gói dịch vụ) | "I was charged but didn't use the app"
"How do I upgrade my plan?"
"Can I get a refund?"
"Why is my charge different?"
"I want to cancel subscription” | **Handler:** CS Agent (most cases), CS Leader (refunds)

**Priority:** Normal (unless dispute)

**SLA:** 4-24 hours | **Step 1: Identify billing issue type**
↓
├─→ General inquiry (how to upgrade, plan comparison)
│   → CS handles directly
│
├─→ Charge confusion (why charged, charge amount)
│   → CS explains, provides invoice
│
├─→ [Refund request
│   → Escalate CS Leader](https://www.notion.so/C-c-y-u-c-u-li-n-quan-n-Billing-v-Refund-1fab0da449f1801ab707cf11264004dc?pvs=21)
│
└─→ [Dispute/chargeback
→ Immediate escalate CS Leader](https://www.notion.so/C-c-y-u-c-u-li-n-quan-n-Billing-v-Refund-1fab0da449f1801ab707cf11264004dc?pvs=21)
↓
**Step 2: Gather information**
✓ Check charge history
✓ Review plan usage
✓ Check subscription status
✓ Understand merchant concern
↓
**Step 3: Provide explanation or escalate** |  |
| 5 | Complaints & Negative Feedback (Phàn nàn) | "Your app is terrible!"
"This is too complicated"
"I've been waiting for days for help"
"Nothing works properly"

 app store review | **Handler:** CS Agent (initial), CS Leader (if escalates)

**Priority:** High

**SLA:** 2-4 hours | **Step 1: Respond quickly**
→ Acknowledge immediately (within 2 hours)
↓
**Step 2: Don't take personally**
→ Stay professional
→ Empathize genuinely
↓
**Step 3: Understand root cause**
→ What actually went wrong?
→ Is it fixable?
→ Is it our fault?
↓
**Step 4: Take ownership**
→ Apologize for experience
→ Commit to resolution
↓
**Step 5: Provide solution**
→ Specific action plan
→ Timeline
→ Compensation if appropriate
↓
**Step 6: Follow through**
→ Do exactly what you promised
→ Update proactively
→ Verify satisfaction
↓
**Step 7: Document and learn**
→ What can we improve?
→ Share with team
→ Update processes if needed | **When to escalate CS Leader qua Slack channel:**
- After 2 attempts, merchant still angry
- Merchant threatens legal action
- Merchant threatens public negative review
- Issue involves refund/compensation
- VIP merchant complaint |
| 6 | Pre-sales Questions (Câu hỏi trước khi mua) | "Does your app do X?"
"How much does it cost?"
"Can it integrate with Y?"
"Is there a free trial?"
"Comparison with competitor Z” | **Handler:** CS Agent

**Priority:** High (potential customer)

**SLA:** 2-4 hours | **Step 1: Respond quickly**
→ Fast response shows good service
↓
**Step 2: Understand their needs**
→ What are they trying to achieve?
→ What's their business model?
→ What features are most important?
↓
**Step 3: Provide clear information**
→ Honest about capabilities
→ Don't oversell
→ Explain value
↓
**Step 4: Address concerns**
→ Competitor comparison (if asked)
→ Pricing objections
→ Technical limitations
↓
**Step 5: Guide next steps**
→ Encourage trial
→ Offer onboarding help
→ Share resources
↓
**Step 6: Follow up**
→ Check if they installed
→ Offer setup assistance
→ Track conversion | - Đối với [Chatty](https://www.notion.so/Chatty-575d918aff7947bcaf2b37129ebc19a0?pvs=21) và [Joy Loyalty](https://www.notion.so/Joy-Loyalty-478e46bc5d0542bca22b4d70c3a1c8ce?pvs=21),  |
| 7 | Integration Questions (Tích hợp với app khác) | "Can this work with [App X]?"
"I use [App Y] for Z, will they conflict?"
"How do I connect with Klaviyo?"
"Integration with my custom theme?” | **Handler:** CS (basic), TS (complex)

**Priority:** Normal

**SLA:** 4-24 hours | **Step 1: Identify integration type**
↓
├─→ Native integration (we built it)
│   → CS provides guide
│
├─→ Common third-party app
│   → CS provides standard answer
│
├─→ Custom/uncommon integration
│   → Escalate TS for assessment
│
└─→ Theme customization
→ Escalate TS via Trello card
↓
**Step 2: Provide information**
→ How it works
→ Setup instructions
→ Limitations if any
↓
**Step 3: Offer support**
→ Guide through setup
→ Test together if needed |  |
| 8 | Users Asking for Discount | - Trial User Asking for Discount
- Existing Customer Asking for Discount
- Multiple Stores / Volume Discount
- Special Cases (Students, Non-profits, etc.) | **Handler:** CS Agent (initial) → CS Leader (decision)

**Priority:** Normal

**SLA:** 4-24 hours for response, 24-48 hours for decision | **Scenario 1: App đang có chương trình discount/promotion
Step 1: CS check current promotions**
→ Check app-specific announcements
↓
**Step 2: Verify merchant eligibility**
✓ New customer or existing?
✓ Plan level requirements
✓ Any exclusions?
↓
**Step 3: Provide information directly**
→ Share promotion details
→ Explain how to claim
→ Provide promo code if applicable
↓
**Step 4: No escalation needed**
→ CS handles completely
→ Close ticket when merchant satisfied

**Scenario 2: App KHÔNG có chương trình discount
Step 1: CS confirms no active promotion**
→ Check promotion calendar
→ Confirm with team if unsure
↓
**Step 2: Set expectations with merchant**
→ Acknowledge request
→ Explain need to review
→ Provide timeline
↓
**Step 3: Escalate to appropriate team**
↓
├─→ Joy Loyalty
│   → Slack: #sales-cs-success
│   → Tag: @sales-manager
│
├─→ Chatty
│   → Slack: #sales-cs-success
│   → Tag: @pm-chatty
│
└─→ Others
→ Slack channels: @cs-leader + @pm
↓
**Step 4: CS waits for decision (24-48h)**
↓
**Step 5: CS communicates decision to merchant**
→ Approved: Provide details
→ Declined: Offer alternatives | - Tham khảo thêm:
+ Joy: [MC xin discount để upgrade lên Paid plan](https://www.notion.so/MC-xin-discount-upgrade-l-n-Paid-plan-1ccb0da449f1802da54bc61d7db2ed15?pvs=21) 
+ Chatty: [MC xin discount để upgrade lên paid plan ](https://www.notion.so/MC-xin-discount-upgrade-l-n-paid-plan-1e0b0da449f18083b0d0f0bbfd296230?pvs=21)  |
| 9 | Request demo calls | "Can you show me how this works?"
"I'd like a demo before committing"
"Can we schedule a call to discuss features?"
"I need help setting up, can we do a screen share?"
"Do you offer onboarding calls?" | **Handler:** Depends on app (see App-Specific Flows below)

**Priority:** High (potential conversion)

**SLA:** Response within 4 hours, schedule within 24-48 hours | **Merchant requests demo**
↓
**Check which app**
↓
├─→ AOV, Joy, Chatty, Solar apps (Order Limit, Subscription, Survey, PDF)
│   → Proceed with demo scheduling (see related demo offer flows)
│
└─→ Other apps
→ Politely decline, offer alternative support through chat | - Joy: [**Flow Demo Call – Joy Loyalty**](https://www.notion.so/Flow-Demo-Call-Joy-Loyalty-1bbb0da449f180f383e9d14d4cfcc9a9?pvs=21) 
- Chatty:
+ [**Flow Demo Call – Chatty**](https://www.notion.so/Flow-Demo-Call-Chatty-280b0da449f180a09621f1342e8a54a9?pvs=21) 
+ [Expand the limitation for AI Product Recommendation](https://www.notion.so/Expand-the-limitation-for-AI-Product-Recommendation-b90eeb3be7c3431793bb3df6dd2801f1?pvs=21)  |

## Phần 3: Escalation Matrix

### Quick Reference: Khi nào escalate ai?

| Situation | Escalate To | Timeline | How |
| --- | --- | --- | --- |
| Technical bug (CS đã troubleshoot) | TS | Immediate | Trello card |
| Cannot reproduce bug | TS  | Immediate | Trello card |
| Critical bug (P0) | PM + TS leader | Immediate | Slack channel with context |
| Refund request | CS Leader | Immediate | Slack channel with context or Trello card |
| Angry merchant (after 2 attempts) | CS Leader | Immediate | Slack channel with context or Trello card |
| VIP merchant anything | CS Leader | FYI immediately | Slack channel with context |
| Feature request (multiple merchants) | PM  | Weekly batch | Slack channel with context |
| Design/UX confusion (multiple cases) | PM | Weekly batch | Slack channel with context |
| Complex custom integration | PM | After initial assessment | Slack channel with context |
| Security concern | CS Leader + PM | Immediate | Slack channel with context + #urgent |
| Data loss issue | CS Leader + PM | Immediate | Slack channel with context + #urgent |
| Policy exception | CS Leader + PM | Immediate | Slack channel with reasoning |
| Pricing negotiation | PM/ Sales manager | Immediate | Slack channel with details |

## Phần 4: Priority & SLA Matrix

### Response Time SLA (tham khảo)

| Ticket Type | Priority | First Response | Resolution Target |
| --- | --- | --- | --- |
| P0 - Critical Bug | Critical | < 1 hour | 4-24 hours |
| P1 - High Bug | High | < 4 hours | 2-5 days |
| P2 - Medium Bug | Medium | < 24 hours | 1-2 weeks |
| Complaint | High | < 2 hours | Same day |
| Pre-sales | High | < 4 hours | Same day |
| How-to (VIP) | High | < 2 hours | < 6 hours |
| How-to (Regular) | Normal | < 24 hours | < 48 hours |
| Feature Request | Low | < 24 hours | No commitment |
| Billing (not refund) | Normal | < 4 hours | Same day |
| Refund Request | High | < 2 hours | < 24 hours |

##