# Chatty AI Assistant Test — Answer Key

## MCQ Questions (auto-graded, 1pt each)

| # | Question | Correct Answer |
|---|---|---|
| 1 | What is the AI Assistant in Chatty? | A tool that helps you solve customer questions faster based on the information you provide. |
| 2 | How does the AI Assistant work? | It uses the information from products and custom answers/FAQs you provide to generate answers and resolve customer questions faster. |
| 3 | What triggers Unresolved Questions? | When a customer marks an answer as not helpful OR clicks "talk to agent" |
| 4 | Why review Unresolved Questions? | To identify content gaps and improve AI training |
| 5 | Training methods | Syncing published products, importing FAQs, adding questions, URLs, and uploading files |
| 6 | Limitation for product recommendation | It cannot suggest complementary products unless mentioned in descriptions |
| 7 | Add data source using CSV? | Yes |
| 8 | How to test AI without enabling | AI Assistant > Test |
| 9 | Purpose of adding data sources | To provide more accurate and personalized responses to customers |
| 10 | How often is product data updated | Daily at 12:00 AM PST |
| 11 | Where to change AI welcome message | AI assistant > Settings > AI identity |
| 12 | What counts as an AI reply | A message sent by the AI that directly responds to a customer inquiry (product suggestions, follow-up clarifications, etc.) |
| 13 | What happens when AI replies exceed limit | AI replies stop for new conversations until the next billing cycle; human agents can still handle ongoing chats; all other features remain active |
| 14 | Why organize training data into categories | It makes AI training more effective and helps highlight content gaps easily |
| 15 | Recommended FAQ practice | Include one clear, specific question per entry (e.g., one clear question about return policy timeframe) |
| 16 | What is included in scenario instruction | A descriptive name, trigger keywords, detailed instructions for AI, and active/inactive status |
| 17 | Product data that can be synced | Standard product attributes: description, images, vendor, pricing, variants, collections, inventory count |
| 18 | Where to set AI Availability | In AI Assistant Settings |
| 19 | Required for order status scenario | Set up required order information in Order tracking settings |

---

## Open-ended Questions (manual grading, 1pt each)

### Q20 — Role section: what to define?
**Full marks (1pt):** "Define who your assistant is and what they help customers with"
(matches exactly the field description in UI — this is the Role field's purpose)

### Q21 — AI Role example for skincare brand
**Full marks (1pt):** Clear identity statement + what the AI helps with. Example:
"You are a friendly customer support assistant for an online skincare brand. Your goal is to help customers find the right products, answer questions, and provide excellent service."
**Partial credit:** Acceptable if it includes brand identity + purpose, even if brief.

### Q22 — What happens if AI doesn't know the answer?
**Full marks (1pt):** AI informs customer it doesn't have enough information + suggests contacting human agent + question appears in Unresolved Questions for merchant to add training data.

### Q23 — How to prevent AI giving medical advice?
**Full marks (1pt):** Add instruction in General Instructions > **Boundaries** section.

### Q24 — AI responds in multiple languages?
**Full marks (1pt):** Add rule in General Instructions telling AI to detect customer's language and respond in that language.

### Q25 — Structure responses for usage/benefits/safety?
**Full marks (1pt):** Define response structure in General Instructions > **Behaviours** section (e.g., Usage → Benefits → Safety).

### Q26 — How many AI skills? Name them.
**Full marks (1pt):** 7 skills in 2 groups:
- Shopping skills: Product recommendations, Size guide, Inventory status, Product questions suggestions
- Customer support skills: Human handover, After-sales support (refund/return), Order tracking

### Q27 — Discount not appearing — first step?
**Full marks (1pt):** Go to Chatty > Training Data > Discounts > verify discounts are present > click Sync if needed. Check if the discount is ACTIVE in Shopify.

### Q28 — Chatty sync active AND inactive discounts?
**Full marks (1pt):** No — Chatty only syncs **ACTIVE** discount codes. Inactive/expired ones are not synced. This prevents AI from promoting expired campaigns.

### Q29 — Markets & currencies section purpose?
**Full marks (1pt):** Helps AI answer questions using customer's local currency, know which products can ship to customer's country, and send correct product URL for customer's market (sub-domain).

### Q30 — Market not showing in Training data — what to do?
**Full marks (1pt):** Go to Training Data > Markets & Currencies > check status is Active > click Sync now > ensure Markets and Currencies toggle is enabled.

### Q31 — Product recommendations skill?
**Full marks (1pt):** Helps AI understand what customers want and recommend the most relevant products from the store at the right time (bestsellers, new arrivals, based on customer questions/needs).

### Q32 — Best sellers/New arrivals not showing — check first?
**Full marks (1pt):** Check if the status of Best sellers / New arrivals is **Activated** first. If active but showing 0 products, merchant needs to manually add products.

### Q33 — After-sales Support scenario?
**Full marks (1pt):** Guides AI to handle topics related to Return & Refund and Order management (cancel, edit). AI is trained to answer post-purchase questions with empathy and process.
*Note: video demo required per question — if no video provided, deduct 0.5pt.*

### Q34 — Order tracking scenario?
**Full marks (1pt):** Allows customers to check order status and shipment directly in chatbox via AI, without contacting support. Customer provides order number and email.
*Note: video demo required — if no video provided, deduct 0.5pt.*

### Q35 — AI doesn't transfer to human, only shows contact form?
**Full marks (1pt):** 
1. Enable Human Handover scenario
2. Transfer behavior → select **No Transfer**
3. Response customization → select **Contact form**

### Q36 — Train AI for size recommendations?
**Full marks (1pt):** Use Shopping Skills > **Size Guide** — upload size chart images, assign per product, add instructions for how AI should use size data. Adding FAQ about sizing is supplementary.

### Q37 — Shopify metafields AI can learn?
**Full marks (1pt):** Text (single/list), Rich text, Numbers (integers/decimals), True/false, Rating.

### Q38 — Product-specific FAQs?
**Full marks (1pt):** Yes. Training Data > Products > find product > click 3-dot icon > Add FAQs / Manage FAQs.

### Q39 — Custom scenarios — when to create + examples?
**Full marks (1pt):** When merchant wants AI to handle a specific customer situation with predefined instructions/flow. Must include at least 1-2 examples (e.g., refund request flow, download transcript guide, handling out-of-stock inquiries, recommending alternatives).

### Q40 — Products per plan + can limit be extended?
**Full marks (1pt):** Free: 100 / Basic: 500 / Pro: 8,000 / Plus: 20,000. Cannot extend without upgrading. Bonus (not required): internal extension via dev_zone with CSL/CSM approval for certain high-value customers.
