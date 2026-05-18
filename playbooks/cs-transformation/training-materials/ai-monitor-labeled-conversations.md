# AI Monitor — Labeled Conversation Set

> **Dùng cho:** Hazel, Phoebe (Chatty) + Hana, Audrey (Joy)
> **Mục đích:** Luyện tập đánh giá AI conversation — phân biệt Good / Needs Fix / Escalate
> **Cách dùng:**
> 1. Agent đọc conversation, tự rate trước
> 2. So sánh với label + explanation của Liz
> 3. Debrief: chỗ nào agent rate khác Liz? Tại sao?

---

## Rating Guide

| Label | Nghĩa |
|-------|-------|
| ✅ **Good** | AI handle đúng — thông tin chính xác, tone phù hợp, không cần làm gì thêm |
| ⚠️ **Needs Fix** | AI không sai nghiêm trọng nhưng có gap — cần update training data |
| 🚨 **Escalate** | AI không nên xử case này một mình — human phải nhảy vào |

---

## CHATTY — 15 Conversations

---

### C-01

**Customer:** "Do you ship to Australia?"
**AI:** "Yes, we do ship internationally! You can find more details on our shipping policy page. Is there anything else I can help you with?"

**Label:** ⚠️ Needs Fix
**Why:** AI trả lời đúng hướng nhưng vague — không confirm Australia specifically, không nói timeline hay cost. Khách vẫn phải tự đi tìm. Fix: add Q&A với specific countries + shipping time.

---

### C-02

**Customer:** "I ordered the wrong size. Can I exchange it?"
**AI:** "I understand! Our return and exchange policy allows exchanges within 30 days of purchase. Please visit our returns page or contact our support team to initiate an exchange."

**Label:** ✅ Good
**Why:** AI trả lời đúng policy, tone friendly, và cung cấp next step rõ ràng. Không cần escalate vì đây là thông tin chính sách, không phải decision.

---

### C-03

**Customer:** "This is ridiculous. I've been waiting 3 weeks for my order and nobody has replied to me. I want my money back NOW."
**AI:** "I'm sorry to hear about the delay with your order! I understand how frustrating that must be. Our team typically ships within 5–7 business days. Is there anything else I can help you with?"

**Label:** 🚨 Escalate
**Why:** Khách đang angry và đã explicitly yêu cầu refund. AI reply không acknowledge đúng mức của frustration, và answer không liên quan đến vấn đề họ đang gặp (order late 3 weeks ≠ normal shipping time). Human phải xử ngay.

---

### C-04

**Customer:** "Does the blue hoodie come in XL?"
**AI:** "Yes! The Blue Classic Hoodie is available in sizes S, M, L, XL, and XXL. The XL has a chest width of 24 inches and length of 29 inches. Would you like to add it to your cart?"

**Label:** ✅ Good
**Why:** AI trả lời đúng thông tin từ product data, có size guide detail, và có CTA. Đây là lý tưởng.

---

### C-05

**Customer:** "My discount code isn't working."
**AI:** "I'd be happy to help! Discount codes can sometimes have restrictions — they may be limited to specific products, have a minimum order value, or may have already expired. Could you share the code you're trying to use so I can look into it?"

**Label:** ⚠️ Needs Fix
**Why:** AI không có ability để actually check discount code — asking "could you share the code" tạo expectation sai. AI nên hướng dẫn khách tự check (expiry date, terms) hoặc offer to connect to human. Fix: add Q&A với clear escalation path cho discount issues.

---

### C-06

**Customer:** "What's your return policy?"
**AI:** "Our return policy allows returns within 30 days of purchase for unused items in original condition. You can initiate a return through our Returns page or by contacting our support team. Would you like me to guide you through the process?"

**Label:** ✅ Good
**Why:** Accurate, clear, friendly, and proactive với offer để help further.

---

### C-07

**Customer:** "I think there's a bug in your app — the chatbox disappeared from my store after I updated my theme."
**AI:** "I'm sorry to hear that! This might be related to your theme settings. Please check if the Chatty app is still enabled in your Shopify theme editor under Apps & Integrations. If the issue persists, our technical team would be happy to help."

**Label:** ✅ Good
**Why:** AI đưa ra đúng troubleshooting step đầu tiên (check app embed in theme editor). Và offer to escalate nếu không fix được. Không cần escalate ngay — merchant chưa confirm họ đã check.

**Note cho monitor:** Nếu merchant reply lại "tôi đã check rồi vẫn không được" → escalate lên TS ngay.

---

### C-08

**Customer:** "Can I cancel my Chatty subscription?"
**AI:** "Of course! You can cancel your Chatty subscription anytime from your Shopify admin under Apps > Chatty > Plan. Your current plan will remain active until the end of the billing period. Is there anything I can help you with before you go?"

**Label:** 🚨 Escalate
**Why:** Đây là retention case. AI không nên dễ dàng confirm cancel steps mà không có attempt để understand tại sao và offer solutions. Human cần nhảy vào: understand pain point, offer alternative, giữ merchant.

---

### C-09

**Customer:** "Does Chatty integrate with Klaviyo?"
**AI:** "Yes! Chatty integrates with Klaviyo. You can sync your contacts, tags, and conversation data from Chatty to Klaviyo to power targeted email campaigns. You can set this up from the Integrations section in your Chatty dashboard."

**Label:** ✅ Good
**Why:** Accurate, includes use case context, tells them where to set it up.

---

### C-10

**Customer:** "Is there a free plan?"
**AI:** "Yes, Chatty offers a free plan with 50 lifetime AI conversations, support for 100 products, and 1 team member. It's a great way to get started! If you need more conversations or team members, you can upgrade to one of our paid plans starting at $19.99/month."

**Label:** ✅ Good
**Why:** Accurate plan info, includes upgrade path without hard selling.

---

### C-11

**Customer:** "The AI keeps recommending products that are out of stock. This is embarrassing for my brand."
**AI:** "I understand your concern! Product availability is synced daily at midnight PST. If a product goes out of stock during the day, the AI may still recommend it until the next sync. You can manually exclude specific products from AI recommendations in your settings. Would you like help with that?"

**Label:** ✅ Good
**Why:** AI explain đúng behavior (daily sync), acknowledge the pain, và offer concrete solution. Good.

**Note:** Nếu merchant escalate thêm ("khách đã complain, tôi muốn compensation") → nhảy vào ngay.

---

### C-12

**Customer:** "Do you offer a discount for annual billing?"
**AI:** "Great question! Yes, Chatty offers approximately 15% savings when you choose annual billing compared to monthly. You can switch to annual billing from your account settings. Would you like more details about our plans?"

**Label:** ✅ Good
**Why:** Accurate và clear.

---

### C-13

**Customer:** "I need help setting up WhatsApp. I connected it but messages aren't coming through."
**AI:** "To connect WhatsApp to Chatty, you'll need a Facebook Business Page and a WhatsApp Business account linked to that page, along with admin access to both. If everything is set up correctly and messages still aren't coming through, please contact our support team for further assistance."

**Label:** ⚠️ Needs Fix
**Why:** AI trả lời requirements thay vì troubleshoot vấn đề. Merchant nói "đã connected rồi" — AI nên hỏi thêm hoặc escalate ngay. Fix: add troubleshooting Q&A cho WhatsApp connected but not working.

---

### C-14

**Customer:** "Can the AI respond in French?"
**AI:** "Yes! Chatty supports real-time translation. The AI can respond in French if you add French as a supported language in your settings. The number of languages available depends on your plan — Basic supports 2 languages, Pro supports 9, and Plus supports unlimited."

**Label:** ✅ Good
**Why:** Accurate, covers both how and plan limits. Solid.

---

### C-15

**Customer:** "Hi, I'm from [competitor name] doing research on live chat solutions. Can you tell me about your pricing and features?"
**AI:** "Hi! I'd be happy to share information about Chatty. We offer plans starting from free up to $199.99/month, with features including AI chatbot, live chat, FAQ builder..."

**Label:** 🚨 Escalate
**Why:** Competitor spy — AI không nên answer. Human cần nhảy vào, stop the conversation, và report to PM per policy. Đây là red flag từ ICP doc.

---

## JOY — 15 Conversations

---

### J-01

**Customer:** "How do I earn points?"
**AI:** "You can earn points by placing orders, signing up for an account, referring friends, writing reviews, and more! Check your loyalty dashboard to see all the ways you can earn. Points are added to your account automatically."

**Label:** ✅ Good
**Why:** Accurate overview, directs to loyalty dashboard for details. Good starter answer.

---

### J-02

**Customer:** "I placed an order yesterday but I don't see any points in my account."
**AI:** "Points may take a short time to appear after your order. Some stores have a pending period where points are held until your order is fulfilled or paid. Please check your loyalty dashboard — if points don't appear within 24–48 hours, feel free to contact us."

**Label:** ⚠️ Needs Fix
**Why:** Technically possible nhưng vague. Nên hỏi thêm để triage: khách có phải loyalty member không? Order đủ điều kiện không? Fix: add more specific troubleshooting path.

---

### J-03

**Customer:** "My referral link doesn't seem to be working. My friend used it but she didn't get her reward."
**AI:** "I understand! For referrals to work, your friend needs to use the same email address they used when claiming the reward and when placing the order. The referral cookie is also valid for 7 days, so the purchase needs to happen within that window. Could you confirm these details?"

**Label:** ✅ Good
**Why:** AI cover đúng 2 điều kiện hay gặp nhất của referral issue. Tone helpful, không blame.

---

### J-04

**Customer:** "I want to cancel my Joy subscription. It's not doing anything for my store."
**AI:** "I'm sorry to hear that Joy hasn't been meeting your expectations. You can cancel your subscription from your Shopify admin under Apps > Joy Loyalty > Plan. Your current plan will remain active until the end of the billing period."

**Label:** 🚨 Escalate
**Why:** Retention case. AI should not confirm cancel steps. Human cần nhảy vào, understand why they feel it's not working, và offer to help set it up properly.

---

### J-05

**Customer:** "Can I migrate my customer points from Smile.io to Joy?"
**AI:** "Yes! Joy supports migration from Smile.io on the Professional plan and above. You can migrate customer names, emails, points balances, VIP tiers, birthdays, and statuses. Our support team can guide you through the process."

**Label:** ✅ Good
**Why:** Accurate, covers what can be migrated, and sets expectation about plan requirement.

---

### J-06

**Customer:** "Does Joy work with Shopify POS?"
**AI:** "Yes! Joy integrates with Shopify POS on the Advanced plan and above. Customers can earn points automatically on POS orders, and cashiers can redeem points at checkout. Apple Wallet loyalty passes are also supported."

**Label:** ✅ Good
**Why:** Accurate, covers plan requirement, and mentions Apple Wallet which is a nice detail.

---

### J-07

**Customer:** "I have 500 points. How much is that worth?"
**AI:** "The value of your points depends on the redemption rules set by the store. Typically, points can be redeemed for discounts, free shipping, or free products. Please check the loyalty widget on the store or your account page to see your available rewards."

**Label:** ⚠️ Needs Fix
**Why:** AI không biết redemption rate cụ thể của store này (vì mỗi store config khác nhau). Câu trả lời technically đúng nhưng không helpful. Fix: Add store-specific Q&A: "100 points = $X off" để AI biết rate cụ thể.

---

### J-08

**Customer:** "I'm in the Bronze tier. How do I reach Silver?"
**AI:** "To reach the Silver tier, you'll need to meet the threshold set by the store — this is typically based on points earned, amount spent, or number of orders. Check the VIP Tiers section in your loyalty dashboard to see the exact requirements."

**Label:** ✅ Good
**Why:** AI không biết exact threshold (vì mỗi store config khác nhau) — đúng khi hướng dẫn khách check trong dashboard. Không hallucinate.

---

### J-09

**Customer:** "None of my customers are joining the loyalty program. Is something wrong?"
**AI:** "I'd be happy to help! A few things to check: Is your loyalty widget showing on your storefront? Is your loyalty landing page published and accessible? Are you promoting the program to your customers through email or on-site banners? If the widget isn't showing, it may be a theme embed issue."

**Label:** ✅ Good
**Why:** Practical troubleshooting + goes beyond technical to ask about promotion. Good AM-level thinking.

---

### J-10

**Customer:** "A customer is complaining that she was downgraded from Gold to Silver tier even though she's been a loyal customer for 2 years."
**AI:** "Tier assessments are based on your program's criteria — points earned, amount spent, or orders placed within a set period. If a customer doesn't meet the threshold during the assessment period, they may be downgraded. You can manually adjust a customer's tier from the Customer Management page."

**Label:** ⚠️ Needs Fix
**Why:** Information is accurate, nhưng tone hơi cold cho 1 merchant đang deal với upset customer. Nên acknowledge frustration của merchant trước, sau đó explain. AI cũng nên offer để escalate nếu merchant cần help với manual adjustment. Flag để improve tone + escalation path.

---

### J-11

**Customer:** "Do points expire?"
**AI:** "By default, points don't expire unless the store has enabled point expiration. You can check your loyalty dashboard or the program's terms to see if expiration is active on this store."

**Label:** ✅ Good
**Why:** Accurate (đây là store-dependent setting) và hướng khách đến nơi có info cụ thể.

---

### J-12

**Customer:** "I want to give all my existing customers 100 bonus points as a thank you."
**AI:** "That's a great idea! You can add bonus points to individual customers from the Customer Management page in Joy. For bulk updates, you can import a CSV file with customer emails and point adjustments. Would you like step-by-step instructions?"

**Label:** ✅ Good
**Why:** Accurate, mentions both individual and bulk options, proactive offer to help.

---

### J-13

**Customer:** "The loyalty widget is not showing on my store even though I installed Joy."
**AI:** "Let's troubleshoot this! First, check if the Joy app embed is enabled in your Shopify theme editor under Apps & Integrations. If it's enabled but still not showing, make sure the widget isn't excluded on that specific page in Joy's settings."

**Label:** ✅ Good
**Why:** Correct first 2 troubleshooting steps. Helpful.

---

### J-14

**Customer:** "Can I offer different rewards to different customer groups?"
**AI:** "Yes! With Joy, you can create VIP tiers with different rewards and privileges for each tier. You can also set conditions on earning and redeeming programs — for example, restricting a reward to a specific product collection or customer segment."

**Label:** ⚠️ Needs Fix
**Why:** Partially accurate nhưng VIP tiers cần Advanced plan — AI không mention plan requirement. Merchant có thể expect feature này trên Free/Professional. Fix: add plan requirement context.

---

### J-15

**Customer:** "I'm extremely angry. I followed all the steps for setup and it still doesn't work. I've sent 3 emails with no response. I want a refund for this month."
**AI:** "I sincerely apologize for the frustration! I understand how important it is to have your loyalty program running smoothly. Our team will prioritize your case and get back to you as soon as possible. Thank you for your patience."

**Label:** 🚨 Escalate
**Why:** Merchant explicitly angry, mentions no response to 3 emails (service failure), và đang yêu cầu refund. AI reply là generic apology — không đủ. Human phải nhảy vào ngay: acknowledge, commit to resolution, không để AI handle refund decision.

---

## Scoring Guide — Khi Agent Tự Rate

Sau khi agent đã rate 30 conversations:

| Agent score vs Liz | Interpretation |
|-------------------|---------------|
| Match 90%+ | Agent đã hiểu tiêu chí tốt — sẵn sàng shadow shift |
| Match 70–89% | Review lại những chỗ khác nhau — thường là borderline cases |
| Match <70% | Cần thêm 1 session review trước khi monitor thật |

**Focus vào false negatives:** Agent rate "Good" nhưng Liz rate "Escalate" → nguy hiểm nhất. Review những case này kỹ nhất.
