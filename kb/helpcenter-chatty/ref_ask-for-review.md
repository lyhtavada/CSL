# Asking for Shopify Reviews — CS Process Guide

<!-- CHUNK: ref-ask-for-review-timing -->
```yaml
chunk_id: "ref__ask-for-review-timing"
doc_id: "cs-ref-ask-for-review"
title: "When to ask (and when not to ask) for a Shopify App Store review"
category: "cs-process"
subcategory: "review-request"
tags: ["review", "ask for review", "timing", "Shopify review", "high_risk", "don't_ask_for_review", "satisfied signal", "do not ask signal"]
applies_when: "CS is deciding whether it's appropriate to ask a merchant for a review"
priority: "high"
```

## Step 0 — Shopify or G2?

Check the conversation segments **before** deciding which review to ask for:

- **Already has a Shopify review tag** (`rv_yes_chatty`, `review_yes_chatty`, `review_yes_faq`) → **skip Shopify, go to G2** (see G2 section at the bottom of this file).
- **Already has a G2 tag** (`rv_yes_g2_chatty`) → **do not ask for any review**.
- **No review tag** → proceed with Shopify decision tree below.

---

## Decision Tree — Should I Ask for a Shopify Review?

Work through these checks in order. Stop at the first NO.

1. Has the merchant exchanged **at least 3–4 back-and-forth messages** in this conversation? → If no, **stop. Too early.**
2. Did the conversation start with a complaint or serious issue? → If yes, **do not ask in this session**, even if the merchant has since said thank you.
3. Is the conversation tagged `high_risk` or `don't_ask_for_review`? → If yes, **stop.**
4. Is the merchant still in early setup / hasn't experienced the app yet? → If yes, **stop.**
5. Did the merchant say something that matches a **"Do NOT Ask" signal** (see below)? → If yes, **stop.**
6. Did the merchant say something that matches a **"Satisfied" signal** (see below)? → If yes, proceed to ask.
7. Have all main questions been answered and any remaining requests are nice-to-haves only? → If yes, proceed to ask.

---

## Satisfied Signals — OK to Ask

These phrases (or close variations) indicate genuine satisfaction:

- *"thank you so much"*, *"thanks a lot"*, *"you're amazing"*
- *"this worked perfectly"*, *"it works now"*, *"problem solved"*
- *"you guys are great"*, *"amazing support"*, *"great help"*
- *"I really appreciate it"*, *"you saved me"*, *"so helpful"*
- *"love the app"*, *"really happy with it"*

> A simple *"thanks"* or *"ok"* alone is **not** a satisfied signal — look for genuine warmth or explicit positive feedback.

---

## "Do NOT Ask" Signals — Stop Immediately

If any of these appear anywhere in the conversation — even if the merchant later says thank you — do not ask for a review in this session:

- *"finally"*, *"finally works"*, *"took so long"*, *"took forever"*
- *"I was so frustrated"*, *"very frustrated"*, *"really annoyed"*
- *"I almost uninstalled"*, *"I was about to remove the app"*
- *"this is a basic feature"*, *"this should work out of the box"*
- *"I've been waiting"*, *"I contacted you before"*, *"again"*
- Merchant expressed that the app **couldn't do something they needed** (even if a workaround was found)
- Merchant had to wait a long time for a resolution

---

## When to Ask (summary)

- Merchant has used the app and seen value from it
- Merchant expresses genuine satisfaction (matches a Satisfied Signal above)
- After successfully resolving a specific issue or question — **and** no Do NOT Ask signals present
- After at least 3–4 exchanges — don't ask in the first 1–2 messages
- Remaining requests are customization or nice-to-haves (not blockers)
- All main questions have been answered

## When NOT to Ask (summary)

- Merchant hasn't seen value yet / still in early setup
- Conversation is tagged `high_risk` or `don't_ask_for_review`
- During onboarding (before they've had a chance to experience the app)
- Merchant is frustrated, has an unresolved issue, or complained
- Conversation started with a complaint — regardless of outcome
- A "Do NOT Ask" signal was present at any point in the conversation
- You just unlocked a feature from DevZone or removed branding (unless told otherwise by CSL)
- Merchant already declined or didn't respond after the first ask — don't repeat
- Only 1–2 messages exchanged so far — conversation is too new

---

<!-- CHUNK: ref-ask-for-review-flow -->
```yaml
chunk_id: "ref__ask-for-review-flow"
doc_id: "cs-ref-ask-for-review"
title: "How to ask for a Shopify review — 4-step process"
category: "cs-process"
subcategory: "review-request"
tags: ["review", "ask for review", "template", "shortcut", "rv-done", "4 steps", "review link"]
applies_when: "CS is ready to ask a merchant for a review and needs to know the correct process"
priority: "high"
```

## 4-Step Review Request Flow

**Step 1: Ask for feedback directly — no pre-screening**

Send one of these neutral messages. Do NOT ask "may I ask a favor?" or "are you happy?" first — that pre-screens for sentiment which violates Shopify review policy.

> *"If you have a moment, we'd really appreciate your feedback on the Shopify App Store. It helps us improve and helps other merchants discover Chatty."*

Or:

> *"We'd love to hear your feedback! If you have a moment, please consider leaving a review on the Shopify App Store — it really helps our team and other merchants."*

**Step 2: Send the review link**

If the merchant responds positively (e.g. "sure", "ok", "happy to"), send the link immediately:
https://apps.shopify.com/chatty#modal-show=WriteReviewModal

If the merchant does not reply within **2 minutes**, send the link proactively without waiting.

**Step 3: Follow up after sending**

After sending the link, send this:
> *"I'd be so grateful if you could update me once it's done so I can thank you in time!"*

Or more casual: *"I can't wait to see it!"* / *"So excited to see your review!"*

**Step 4: Thank the merchant after they leave a review**

Once the merchant confirms they've left a review, respond warmly:
> *"Thank you so much — this truly means a lot to us! Your support helps us keep improving and motivates the whole team. We really appreciate you taking the time! 🙏"*

Or more casual: *"You're amazing, thank you!! This made my day!"* / *"So grateful — thank you for supporting us!"*

After thanking them, remember to tag the conversation: `rv_yes_chatty`

---

<!-- CHUNK: ref-ask-for-review-rules -->
```yaml
chunk_id: "ref__ask-for-review-rules"
doc_id: "cs-ref-ask-for-review"
title: "Shopify review request — prohibited behaviors and policy rules"
category: "cs-process"
subcategory: "review-request"
tags: ["review", "prohibited", "Shopify policy", "incentive", "positive review", "5 stars", "pressure"]
applies_when: "CS needs to know what is and isn't allowed when requesting reviews"
priority: "high"
```

## Strictly Prohibited

- Offering anything in exchange for a review (discounts, free months, perks)
  - ❌ *"Get one month free by leaving us a review!"*
- Pre-screening for sentiment before asking (e.g. "are you happy?", "may I ask a favor?" as a filter)
  - ❌ *"Before you go — since things worked out well today, would you mind leaving a review?"*
  - ❌ *"If you're enjoying Chatty, we'd love a review!"*
  - ❌ *"If you're happy with the support so far, we'd really appreciate your feedback..."*
  - ❌ *"Since everything is resolved now, would you mind leaving a review?"*
  - ❌ *"If my support was helpful, we'd love a review!"*
- Asking only for positive reviews or 5-star reviews
  - ❌ *"Like our service? Leave us a positive review!"*
  - ❌ *"Positive feedback keeps us going!"*
- Telling the merchant what to write or guiding the content
- Pressuring or repeatedly asking after a decline
- Asking the merchant to edit, remove, or change an existing review when their issue hasn't been resolved

## Always Use Neutral Language

> *"We value feedback! It helps us improve our product and keeps us motivated. Let us know how we're doing."*

**Important:** CS can only use pre-approved review templates. If you want to change any template, get CSL approval before using it.

---

<!-- CHUNK: ref-ask-for-review-after-review -->
```yaml
chunk_id: "ref__ask-for-review-after-review"
doc_id: "cs-ref-ask-for-review"
title: "How to tag a conversation after a merchant leaves a review"
category: "cs-process"
subcategory: "review-request"
tags: ["review", "segment", "tag", "rv_yes", "after review", "conversation tag"]
applies_when: "A merchant has left a review and CS needs to tag the conversation"
priority: "medium"
```

## Tagging After a Review

After a merchant leaves a review, add a segment to the conversation:

`rv_yes_[appname]`

**Examples:**
- Joy Loyalty → `rv_yes_joy`
- Air Product Reviews → `rv_yes_air`
- Chatty → `rv_yes_chatty`

**Why this matters:**
- Prevents asking the same merchant for a review again
- Avoids annoying merchants who already reviewed
- Helps track review activity accurately per merchant

---

<!-- CHUNK: ref-ask-for-review-uninstall -->
```yaml
chunk_id: "ref__ask-for-review-uninstall"
doc_id: "cs-ref-ask-for-review"
title: "Can a merchant still leave a review after uninstalling Chatty?"
category: "cs-process"
subcategory: "review-request"
tags: ["review", "uninstall", "45 days", "Shopify App Store", "after uninstall"]
applies_when: "Merchant has uninstalled and CS wonders if they can still be asked for a review"
priority: "low"
```

## After Uninstalling

Yes. After uninstalling, a merchant has **45 days** to leave a review on the Shopify App Store before that option expires.
