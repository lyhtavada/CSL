---
category: CS Process
topic: Asking for Reviews (Shopify + G2)
source: cs-process
---

Q: When should I ask a merchant for a review?
Q: What's the right timing to request a Shopify App Store review?
Q: How do I know if it's a good time to ask for a review?
A: Ask for a review when the merchant has clearly experienced value. Use judgment — timing matters more than completing every single request.

**First, check if the conversation already has a Shopify review tag:**
- If the conversation has `rv_yes_joy`, `review_yes_joy`, `rv_yes_chatty`, `review_yes_chatty`, or `review_yes_faq` → the merchant already left a Shopify review. **Do not ask for Shopify again. Ask for G2 instead** (see G2 section below).
- If no review tag → proceed with the Shopify review flow below.

**✅ Good times to ask (Shopify):**
- Merchant has used the app and seen value from it
- Merchant expresses satisfaction, says thank you, or compliments the support
- After successfully resolving a specific issue or question
- After handling 1-2 initial requests successfully — don't wait to finish everything if the merchant is already happy
- Remaining requests are customization or nice-to-haves (not blockers)
- All main questions have been answered

**🚫 Never ask when:**
- Merchant hasn't seen value yet / still in early setup
- Conversation is tagged `high_risk` or `don't_ask_for_review`
- During onboarding (before they've had a chance to experience the app)
- Merchant is frustrated, has an unresolved issue, or complained
- You just unlocked a feature from dev_zone or removed branding (unless told otherwise by CSL)
- Merchant already declined or didn't respond after the first ask — don't repeat

---

Q: How do I ask for a review in live chat?
Q: What's the correct process to request a review from a merchant?
Q: What template should I use to ask for a review?
A: Follow this 3-step flow:

**Step 1: Ask permission first**
Don't send the review link out of nowhere. Start with:
> *"While you're here, may I ask for a quick favor?"*

This makes the merchant feel respected rather than pushed.

**Step 2: Send the review template**
After they agree, use the pre-approved shortcut (`!chatty-rv`, `!joy-rv`, etc.) from the **Ask for reviews** category in Message Shortcuts. Don't write your own — use the prepared template.

Example of what the template looks like:
> *"Would you mind leaving a quick review for our support and app via this link? It only takes a few seconds and we really appreciate your feedback!"*

**Step 3: Follow up after sending**
After sending the link, use shortcut `!rv-done` to gently remind them to update you when they're done:
> *"I'd be so grateful if you could update me once it's done so I can thank you in time!"*

Or more casual: *"I can't wait to see it!"* / *"So excited to see your review!"*

---

Q: What are the rules around Shopify review requests?
Q: What am I not allowed to do when asking for reviews?
Q: Can I offer a discount in exchange for a review?
A: Shopify has strict policies around review requests. Violations can put the app's listing at risk.

**Strictly prohibited (Shopify):**
- Offering anything in exchange for a review (discounts, free months, perks)
  - ❌ *"Get one month free by leaving us a review!"*
- Asking only for positive reviews or 5-star reviews
  - ❌ *"Like our service? Leave us a positive review!"*
  - ❌ *"Positive feedback keeps us going!"*
- Telling the merchant what to write or guiding the content
- Pressuring or repeatedly asking after a decline
- Asking the merchant to edit, remove, or change an existing review when their issue hasn't been resolved

**Always use neutral language:**
> *"We value feedback! It helps us improve our product and keeps us motivated. Let us know how we're doing."*

**Important:** CS can only use pre-approved review templates. If you want to change any template, get CSL approval before using it.

---

Q: What do I do after a merchant leaves a review?
Q: How do I tag a conversation after getting a review?
A: After a merchant leaves a review, add a segment to the conversation in this format:

`rv_yes_[appname]`

Examples:
- Joy Loyalty → `rv_yes_joy`
- Air Product Reviews → `rv_yes_air`
- Chatty → `rv_yes_chatty`

After a merchant leaves a **G2 review**, tag with:
- Joy Loyalty → `rv_yes_g2_joy`
- Chatty → `rv_yes_g2_chatty`

**Why this matters:**
- Prevents asking the same merchant for a review again
- Avoids annoying merchants who already reviewed
- Helps track review activity accurately per merchant

---

Q: Can a merchant still leave a review after uninstalling the app?
Q: How long does a merchant have to leave a review after uninstalling?
A: Yes. After uninstalling, a merchant has **45 days** to leave a review on the Shopify App Store before that option expires.

---

Q: When should I ask for a G2 review instead of Shopify?
Q: The merchant already left a Shopify review — what do I do now?
Q: How do I ask for a G2 review?
A: If the conversation already has a Shopify review tag (`rv_yes_joy`, `review_yes_joy`, `rv_yes_chatty`, `review_yes_chatty`, `review_yes_faq`) **and** the merchant is currently satisfied and engaged — pivot to G2 instead.

G2 is a separate review platform. We run a special program: merchants who leave a G2 review and get approved receive a thank-you gift (free plan month or cash gift depending on their plan).

**Chatty — G2 template:**
> Ah, I'd love to update that we're running a special program where merchants who leave a review on G2 and get approved will receive 1 free month on Basic or Pro plan as a thank-you gift!
>
> Would you mind taking a few minutes to share your thoughts here?
> https://www.g2.com/products/chatty/take_survey
>
> Once your review is published, just send us a screenshot and we'll send your discount code right away!

**Joy — G2 template (Pro/Essential plan):**
> Ah, I'd love to update that we're running a special program where merchants who leave a review on G2 and get approved will receive 1 month free on their current plan as a thank-you gift!
>
> Would you mind taking a few minutes to share your thoughts here?
> https://www.g2.com/products/joy-loyalty/reviews/start
>
> Once your review is published, just send us a screenshot and we'll get your free month sorted right away!

**Joy — G2 template (Advanced plan):**
> Ah, I'd love to update that we're running a special program where merchants on Advanced plan who leave a review on G2 and get approved will receive a $50 thank-you gift!
>
> Would you mind taking a few minutes to share your thoughts here?
> https://www.g2.com/products/joy-loyalty/reviews/start
>
> Once your review is published, just send us a screenshot and we'll get your gift sorted right away!

**How to tell Joy merchant's plan:** Check the visitor data label in Crisp — it shows "Pro", "Advanced", etc.

**After they submit their G2 review:**
Tag the conversation: `rv_yes_g2_joy` or `rv_yes_g2_chatty`

**Do not ask for G2 if:**
- Merchant is already tagged `rv_yes_g2_joy` or `rv_yes_g2_chatty` — already done
- Merchant is frustrated or conversation had complaints
- Merchant is on a free plan (no plan info visible — use the Chatty/Joy Pro template as safe default)
