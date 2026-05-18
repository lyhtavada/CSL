# AI Wrong Responses

<!-- CHUNK: ai-not-responding -->
```yaml
chunk_id: "ai-wrong__not-responding"
doc_id: "chatty-ai-wrong-responses"
title: "AI not responding / giving no answer to customer questions"
category: "ai-wrong-responses"
tags: ["no answer", "AI not responding", "AI silent", "no reply", "conversation limit", "AI disabled"]
applies_when: "Customer sends a message but AI gives no response at all"
priority: "very-high"
```

## AI Not Responding at All

1. **Verify AI Assistant is enabled** — toggle must be ON in AI Assistant settings
2. **Check training data is added and synced** — AI cannot reply if no data sources are active
3. **Ensure Live Chat block is enabled** — go to **Chatbox → General → Blocks** → enable **Live chat**
4. **Check plan's AI conversation limit:**
   - Free plan = 50 lifetime conversations (not monthly) — once hit, AI deactivates
   - Paid plans = monthly quota; when quota is exhausted AI stops until billing reset
   - Guide merchant to upgrade or wait for monthly reset if limit is the cause

> ⚠️ Check plan limits **first** — this is the most common cause for AI suddenly stopping.

---

<!-- CHUNK: ai-hallucination-over-promising -->
```yaml
chunk_id: "ai-wrong__hallucination-over-promising"
doc_id: "chatty-ai-wrong-responses"
title: "AI offers refunds, returns, or makes up store info it shouldn't"
category: "ai-wrong-responses"
tags: ["hallucination", "refund promise", "over-promise", "AI making up", "wrong commitment", "return promise"]
applies_when: "AI is offering refunds, replacements, or making commitments it shouldn't"
priority: "high"
```

## AI Hallucinating / Over-Promising

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- What the AI promised or said (wrong answer)
- What the correct response should have been

This is a known behavior — the AI may over-promise based on general knowledge if not explicitly restricted.

1. **Review the specific chat** — click **Review Sources** to see what data triggered the response
2. **Add a Scenario instruction:**
   - Go to **AI Assistant → Instructions → Scenarios** → add scenario with keywords: "refund", "return", "replacement"
   - Instruction: *"Ask the customer for photos and direct them to support email instead of promising any action."*
3. **Add to Custom Instructions:**
   > *"Never confirm refunds, replacements, or exchanges. Always ask the customer to email [support email] with photos."*
4. **Use AI Feedback button** on incorrect replies to flag for improvement
5. **If persists** after adding instructions → escalate to dev team with chat link and screenshot

> Known limitation — AI must be explicitly restricted via instructions. The restriction does not apply automatically.

---

<!-- CHUNK: ai-wrong-reverts-to-default -->
```yaml
chunk_id: "ai-wrong__reverts-to-default"
doc_id: "chatty-ai-wrong-responses"
title: "AI reverts to default behavior or forgets training after a while"
category: "ai-wrong-responses"
tags: ["reverts", "forgets training", "default behavior", "instructions reset", "training lost"]
applies_when: "AI was working correctly but reverted to generic/default responses without the merchant changing anything"
```

## AI Reverts to Default Behavior

1. **Check Instructions are saved** — not just edited; confirm the save button was clicked after changes
2. **Verify data sources are still active** — go to **Training Data** and check that Q&A entries and URL sources have not been accidentally disabled
3. **Review Scenario keywords** — make sure keywords are specific enough to trigger correctly; overly broad keywords may fail to match
4. **If instructions keep resetting without merchant changes** → this is a possible product bug — escalate to dev team with: store URL, description of what reverted, timestamp when issue was noticed

---

<!-- CHUNK: ai-wrong-responses-general -->
```yaml
chunk_id: "ai-wrong__general-fix"
doc_id: "chatty-ai-wrong-responses"
title: "AI giving wrong answers — how to diagnose and fix"
category: "ai-wrong-responses"
tags: ["wrong answer", "incorrect", "AI wrong", "fix AI", "wrong information", "AI mistake"]
applies_when: "Merchant reports the AI is giving wrong or incorrect answers to customer questions"
```

## AI Giving Wrong Answers — General Diagnostic Flow

**Before anything else, collect:**
- Conversation ID, or the customer's name/email in that chat
- What the AI said (wrong answer)
- What the correct answer should be

Then run this triage:

1. Ask the merchant for the **specific chat link/ID** where the AI responded incorrectly
2. Click **Review Sources** under the AI reply to see which data sources and instructions were used
3. Identify root cause:

| What you see in Review Sources | Root cause | Action |
|---|---|---|
| Source data is incorrect or outdated | Bad training data | Update/correct source content |
| Source is correct but AI misinterprets | Ambiguous wording | Rephrase or add more detail to the FAQ/scenario |
| Wrong source was pulled | Overlapping content | Merge or differentiate FAQs → see *Mixed FAQs* below |
| No sources shown | AI is hallucinating | Check if AI Training Data was synced; report to dev if empty |
| Instructions conflict with source | Bad instruction override | Review Custom Instructions and Scenario Instructions |

4. Make the change, then use **Test AI** to verify the fix
5. If issue persists after correction → gather and escalate: store URL, chat link, screenshot of Review Sources, what the AI said vs. what was expected

---

<!-- CHUNK: ai-feature-shopify-markets -->
```yaml
chunk_id: "ai-feature__shopify-markets"
doc_id: "chatty-ai-wrong-responses"
title: "Does Chatty support Shopify Markets?"
category: "ai-wrong-responses"
tags: ["Shopify Markets", "multi-market", "market support", "market pricing", "regional pricing", "Sync Markets", "does Chatty work with Markets"]
applies_when: "Merchant asks if Chatty works with or supports Shopify Markets"
```

## Chatty and Shopify Markets

Yes — Chatty supports Shopify Markets. Enable **Sync Markets** in **AI Assistant** → **Settings** to sync market-specific pricing and domains. Without this setting, the AI may show main-domain prices instead of market-specific prices.

If the AI is already showing wrong prices or wrong domain links for a market, see the troubleshooting entries below.

---

<!-- CHUNK: ai-wrong-market-price -->
```yaml
chunk_id: "ai-wrong__market-price"
doc_id: "chatty-ai-wrong-responses"
title: "AI showing wrong price for customer's market"
category: "ai-wrong-responses"
tags: ["wrong price", "market price", "Shopify Markets", "currency", "pricing mismatch", "wrong market"]
applies_when: "AI is showing the wrong price — not matching the customer's market or region"
```

## AI Showing Wrong Market Price

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- What price the AI showed (wrong answer)
- What the correct price should be for that market

This happens when the AI pulls pricing from the main domain instead of market-specific pricing.

**Step 1 — Check Sync Markets setting:**
- Go to **AI Assistant** → **Settings** → confirm **Sync Markets** is enabled

**Step 2 — Verify Markets are set up in Shopify:**
- Ask: "Have you set up Shopify Markets with separate pricing per region?"
- If NO → guide merchant to set up Shopify Markets first, then enable Sync Markets in Chatty
- If YES → continue to Step 3

**Step 3 — Test the market domain directly:**
- Visit the merchant's market-specific domain (e.g. `store.fr`) and ask the same question
- If price is wrong on that domain too → the market pricing in Shopify itself may be incorrect — verify in Shopify Admin → Markets

**Step 4 — If all settings are correct but issue persists:**
- Ask permission: *"To investigate the pricing issue, our team may need access to your store. Would you allow us to send a collaborator access request?"*
- If yes → ask for their **collaborator code** (Shopify Admin → Settings → Users → Security → Collaborator request code)
- Collect: which market domain, the incorrect price shown, screenshot of Shopify Market pricing, collaborator code
- Escalate to dev team with full details
- If no → escalate with screenshots only

---

<!-- CHUNK: ai-wrong-product-links -->
```yaml
chunk_id: "ai-wrong__product-links"
doc_id: "chatty-ai-wrong-responses"
title: "AI sending wrong or broken product links (404)"
category: "ai-wrong-responses"
tags: ["wrong link", "broken link", "404", "product link", "incorrect URL", "bad link"]
applies_when: "AI product links lead to 404 pages or wrong products"
```

## AI Sending Wrong/Broken Product Links

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- The wrong/broken link the AI sent
- What the correct link should be

**Step 1 — Check if products are still published:**
- Ask: "Was this product recently deleted, unpublished, or its URL/handle changed?"
- If YES → go to **AI Assistant** → **Training Data** → **Products** → click **Sync Products**, then test again

**Step 2 — Check for handle mismatch:**
- Visit the broken link directly — does the product exist at a different URL?
- If the product exists but at a different handle → the old URL is cached; force a sync

**Step 3 — Reproduce in AI Test:**
- Go to **AI Test** and ask the same question — does it return the same broken link?
- If reproduced in AI Test → this is a system bug

**Step 4 — If sync doesn't fix it:**
- Gather: store URL, specific broken link, screenshot of the AI response, AI Test reproduction
- Report in the internal bug thread for dev follow-up
- Workaround for merchant: manually copy correct product links until fix is deployed

---

<!-- CHUNK: ai-wrong-market-domain -->
```yaml
chunk_id: "ai-wrong__market-domain"
doc_id: "chatty-ai-wrong-responses"
title: "AI shows main domain links instead of market domain links"
category: "ai-wrong-responses"
tags: ["wrong domain", "market domain", "abc.fr", "abc.com", "multi-domain", "Shopify Markets"]
applies_when: "Customer visits a market-specific domain (e.g. abc.fr) but AI shows links to the main domain (abc.com)"
```

## AI Showing Main Domain Instead of Market Domain

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- The wrong domain link the AI showed
- What the correct domain/link should be

**Known limitation:** The app currently stores product data for the main domain only. Market-specific domain links are in development.

**What to tell the merchant:**
> "This is a known limitation we're actively working on. The AI currently links to your main store domain even when a customer is browsing a regional domain. A fix is planned — I'll create a tracking card and follow up once it's deployed."

**Workaround options:**
1. Add a Custom Instruction: *"When sharing product links, remind customers to switch to their regional domain if they see a different currency."*
2. If markets redirect automatically (same products, just different currency display) — the links may still work even if they show the main domain

**Escalation info to collect:**
- Which market domain (e.g. `store.fr`) vs. main domain
- Example of incorrect link shown by AI
- Whether the product exists on both domains or only one

---

<!-- CHUNK: ai-wrong-variant-links -->
```yaml
chunk_id: "ai-wrong__variant-links"
doc_id: "chatty-ai-wrong-responses"
title: "AI not returning variant-specific product links"
category: "ai-wrong-responses"
tags: ["variant link", "specific variant", "size", "color", "product variant", "variant URL"]
applies_when: "AI only sends generic product links, not links for specific variants (size, color)"
```

## AI Not Linking to Specific Variants

**Known limitation:** Variant-level deep links are not fully implemented. The AI can describe and recommend variants but links go to the main product page.

**Workaround:**
- Add a Custom Instruction: *"When recommending a specific variant, include the variant name clearly in your response so the customer can select it on the product page."*
- This won't give a direct link but improves the experience until the feature ships

**If merchant needs deep variant links urgently:**
- Gather: store URL, example of a variant they need linked
- Log as a feature priority request — include merchant's use case

---

<!-- CHUNK: ai-wrong-duplicate-messages -->
```yaml
chunk_id: "ai-wrong__duplicate-messages"
doc_id: "chatty-ai-wrong-responses"
title: "AI sending duplicate messages"
category: "ai-wrong-responses"
tags: ["duplicate", "duplicate message", "same answer twice", "repeated response"]
applies_when: "AI is sending the same response twice in the chat"
```

## AI Sending Duplicate Messages

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- The duplicated message content
- Whether it happens consistently or only in certain cases

**Step 1 — Identify the cause:**
Ask the merchant: "Did the customer send the same message twice, or did the AI respond twice to a single message?"

- **Customer double-sent** → not a bug, expected behavior
- **AI responded twice to one message** → system issue, continue to Step 2

**Step 2 — Check if it's reproducible:**
- Go to **AI Test** and send the same message — does it duplicate there too?
- If YES → system-level bug

**Step 3 — Check for automation overlap:**
- Go to **Automation** tab — is there a rule that also triggers a reply for the same condition?
- If YES → disable or adjust the conflicting automation rule

**Step 4 — If no automation conflict and still duplicating:**
- Gather: chat link, timestamp, screenshot showing the duplicate, whether it happens consistently or intermittently
- Create a card for TS with all details
- Workaround: switch conversation to manual mode temporarily

---

<!-- CHUNK: ai-wrong-foreign-products -->
```yaml
chunk_id: "ai-wrong__foreign-products"
doc_id: "chatty-ai-wrong-responses"
title: "AI recommending products from other stores or websites"
category: "ai-wrong-responses"
tags: ["wrong products", "other store", "foreign products", "different catalog", "wrong recommendations"]
applies_when: "AI is recommending or suggesting products that don't belong to the merchant's store"
```

## AI Recommending Products from Other Stores

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- Which foreign product the AI recommended
- What the correct product/response should have been

**Step 1 — Check sync status:**
- Go to **AI Assistant** → **Training Data** → **Products**
- Is the sync complete? When was the last sync?
- If sync is stale or incomplete → click **Sync Products** and wait for it to finish, then test

**Step 2 — Check for external URLs in training data:**
- Go to **Training Data** → **FAQ** and **Scenarios** — are there any manually added URLs pointing to external sites?
- If YES → remove them, they may be polluting the AI's product knowledge

**Step 3 — Check Custom Instructions:**
- Go to **Instructions** — is there any instruction referencing external websites or product catalogs?
- If YES → remove or correct it

**Step 4 — Reproduce the issue:**
- Use **Test AI** with the same question — does it still recommend foreign products?
- If YES after all the above checks → escalate with: store URL, chat link, exact foreign product name/URL the AI recommended, screenshot of Training Data sync status

---

<!-- CHUNK: ai-wrong-unwanted-human-transfer -->
```yaml
chunk_id: "ai-wrong__unwanted-human-transfer"
doc_id: "chatty-ai-wrong-responses"
title: "AI transferring to human agent when customer didn't ask"
category: "ai-wrong-responses"
tags: ["unwanted transfer", "auto transfer", "human handover", "transfer trigger", "AI escalating"]
applies_when: "AI is automatically transferring conversations to a human agent when the customer did not request it"
```

## AI Transferring Without Being Asked

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- What the customer said that triggered the transfer
- What should have happened instead

**Step 1 — Review Human Handover triggers:**
- Go to **AI Assistant** → **Instructions** → **Assistant Skills** → **Human Handover**
- Look at the configured trigger keywords or conditions — are any too broad? (e.g. "help", "problem", "issue" would match almost everything)
- Narrow or remove the triggers causing unintended escalation

**Step 2 — Check Automation rules:**
- Go to **Automation** tab → check if any rule is set to auto-assign or transfer conversations
- If **Automatic assignment** is on, it may transfer when broad keywords are detected — tighten the conditions

**Step 3 — Review the pre-transfer message:**
- If the pre-transfer message gives customers an option (e.g. "Would you like to talk to a human or email us?"), the AI may misread a "yes" as confirmation to transfer
- Revise to make the intent unambiguous

**If issue persists after adjusting triggers and automation:**
- Gather: example chat link where unintended transfer happened, screenshot of current trigger settings
- Escalate with those details

---

<!-- CHUNK: ai-wrong-add-to-cart -->
```yaml
chunk_id: "ai-wrong__add-to-cart"
doc_id: "chatty-ai-wrong-responses"
title: "AI not adding products to cart correctly"
category: "ai-wrong-responses"
tags: ["add to cart", "ATC", "cart count", "wrong quantity", "cart not updating"]
applies_when: "AI is not adding products to cart correctly, or cart count is not updating"
```

## AI Add-to-Cart Issues

**Step 1 — Check if add-to-cart feature is enabled:**
- Go to **AI Assistant** → **Settings** — is add-to-cart functionality turned on?

**Step 2 — Test on storefront:**
- Ask the merchant: "What theme are you using?"
- Some themes (especially heavily customized or headless themes) don't support Chatty's cart integration
- Test on the live storefront — does the cart count update after AI adds a product?

**Step 3 — Cart count not updating vs. product not added:**
- If product is in cart but count doesn't update → theme rendering issue; refreshing page is the workaround
- If product is NOT in cart at all → likely a theme compatibility issue

**Step 4 — If theme compatibility confirmed as the issue:**
- Ask permission: *"To investigate the theme compatibility issue, our team may need access to your store. Would you allow us to send a collaborator access request?"*
- If yes → ask for their **collaborator code** (Shopify Admin → Settings → Users → Security → Collaborator request code)
- Gather: theme name and version, specific product tested, screenshot showing cart before/after, collaborator code
- Escalate to TS team with those details
- If no → escalate without store access; TS will provide manual fix instructions based on theme name

---

<!-- CHUNK: ai-wrong-links-not-clickable -->
```yaml
chunk_id: "ai-wrong__links-not-clickable"
doc_id: "chatty-ai-wrong-responses"
title: "Links in AI responses are not clickable"
category: "ai-wrong-responses"
tags: ["not clickable", "plain text link", "link format", "markdown link", "unclickable"]
applies_when: "Links in AI responses show as plain text instead of clickable hyperlinks"
```

## Links Not Clickable in AI Responses

**Step 1 — Add a formatting instruction:**
- Go to **AI Assistant** → **Instructions** → **Behaviours**
- Add: `When sharing a link, always format it as [Link Name](URL).`
- Save and test with **Test AI**

**Step 2 — Check existing training data:**
- Go to **Training Data** → **FAQ** — are links in FAQ entries formatted as plain URLs (not markdown)?
- If YES → update FAQ entries to use markdown format: `[text](URL)`

**Step 3 — If links are formatted correctly but still not clickable in chat widget:**
- This may be a widget rendering issue — test in a different browser
- Gather: browser/OS used by customer, screenshot showing the plain-text link, whether it appears formatted in AI Test
- Escalate to TS with those details

---

<!-- CHUNK: ai-wrong-invalid-products -->
```yaml
chunk_id: "ai-wrong__invalid-products"
doc_id: "chatty-ai-wrong-responses"
title: "AI recommending deleted or unpublished products (404 links)"
category: "ai-wrong-responses"
tags: ["deleted product", "unpublished", "404 product", "invalid product", "outdated catalog"]
applies_when: "AI is recommending products that have been deleted or unpublished and showing 404 links"
```

## AI Recommending Deleted/Unpublished Products

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- Which deleted/unpublished product the AI recommended
- What the correct response should have been

**Step 1 — Force a product sync:**
- Go to **AI Assistant** → **Training Data** → **Products**
- Click **Sync Products** — wait for it to complete
- Use **Test AI** to verify the deleted product no longer appears

**Step 2 — If still appearing after sync:**
- Check if the product was manually added to **FAQ** or **Scenarios** (not just the product catalog)
- Search FAQ/Scenario content for the product name or URL and remove it

**Step 3 — If issue persists after sync + manual cleanup:**
- Gather: product name/URL that still appears, screenshot from Test AI showing it recommended, sync timestamp
- Escalate to dev — this may indicate a caching issue in the training data pipeline

---

<!-- CHUNK: ai-wrong-html-in-chat -->
```yaml
chunk_id: "ai-wrong__html-in-chat"
doc_id: "chatty-ai-wrong-responses"
title: "HTML showing in chat responses instead of rendered text"
category: "ai-wrong-responses"
tags: ["HTML", "raw HTML", "div tag", "p tag", "code in chat", "HTML showing"]
applies_when: "AI responses show raw HTML tags instead of formatted text"
```

## HTML Showing in Chat Responses

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- Screenshot or copy of the response showing raw HTML
- What the response should look like

**Step 1 — Find the source of HTML:**
- Go to **AI** → **Training Data** → open each FAQ entry and Scenario that's relevant to the affected topic
- Look for `<div>`, `<p>`, `<br>`, `<strong>`, `<ul>` tags — these will be returned as raw text by the AI

**Step 2 — Clean the training data:**
- Remove all HTML tags and replace with plain text or markdown equivalents:
  - `<strong>text</strong>` → `**text**`
  - `<br>` → new line
  - `<ul><li>` → `- item`
  - `<p>` → remove, just use line breaks

**Step 3 — Save and verify:**
- Save changes and use **Test AI** with the same question
- If HTML still appears → check Custom Instructions for any HTML content as well

**Step 4 — If HTML is not in training data but still appearing:**
- This may be a rendering bug — gather: screenshot of the raw HTML in chat, which question triggered it, Test AI screenshot
- Escalate to dev team

---

<!-- CHUNK: ai-wrong-mixed-faqs -->
```yaml
chunk_id: "ai-wrong__mixed-faqs"
doc_id: "chatty-ai-wrong-responses"
title: "AI mixing up information from two similar FAQs"
category: "ai-wrong-responses"
tags: ["mixed up", "confused", "overlapping", "two policies", "similar FAQs", "conflicting content"]
applies_when: "AI is confusing or mixing content from two similar or overlapping FAQ entries"
```

## AI Mixing Up Similar FAQs

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- What the AI said (wrong answer)
- What the correct answer should be

**Step 1 — Identify the conflicting entries:**
- Go to **AI** → **Training Data** → **FAQ**
- Search for the topic keywords — find the two (or more) entries that overlap
- Use **Review Sources** on the incorrect chat to confirm which entries were pulled

**Step 2 — Fix the overlap:**

| Situation | Fix |
|---|---|
| Two entries cover the same topic | Merge into one comprehensive entry |
| Two policies that are genuinely different | Make trigger keywords more specific and non-overlapping |
| One entry is outdated | Delete the old one, keep only the updated one |

**Step 3 — Make trigger keywords distinct:**
- Each FAQ should have unique trigger keywords that don't appear in the other entry
- Avoid generic keywords like "shipping" or "return" — be specific: "international shipping" vs "domestic return policy"

**Step 4 — Verify:**
- Use **Test AI** with the exact customer question that was being mixed up
- Check **Review Sources** — does it now pull only the correct entry?

---

<!-- CHUNK: ai-wrong-no-human-transfer -->
```yaml
chunk_id: "ai-wrong__no-human-transfer"
doc_id: "chatty-ai-wrong-responses"
title: "AI not transferring to human when customer explicitly asks"
category: "ai-wrong-responses"
tags: ["not transferring", "human handover", "talk to human", "AI not escalating", "handover not working"]
applies_when: "Customer explicitly asks to speak to a human but the AI does not transfer"
```

## AI Not Transferring When Asked

**First, collect from the merchant:**
- Conversation ID, or customer name/email in that chat
- Exact phrase the customer used to request a human
- What the AI responded instead of transferring

**Step 1 — Check Human Handover is enabled:**
- Go to **AI Assistant** → **Instructions** → **Assistant Skills** → **Human Handover**
- Is it toggled on? If no → enable it

**Step 2 — Check the pre-transfer message:**
- If the pre-transfer message offers both email and live transfer options, the AI may interpret the customer's intent as email contact
- Example of ambiguous message: *"Would you like to speak to a human or receive help via email?"*
- Fix: simplify to just confirm the transfer — *"I'll connect you with a support agent now."*

**Step 3 — Check trigger phrases:**
- Are "talk to human", "speak to agent", "real person" in the trigger list?
- If the merchant's customers write in another language → add translated trigger phrases

**Step 4 — If handover is configured correctly but still not triggering:**
- Gather: exact phrase the customer used, chat link, screenshot of current Human Handover settings
- Escalate with those details — may need a prompt-level fix

---

<!-- CHUNK: ai-wrong-email-instead-of-transfer -->
```yaml
chunk_id: "ai-wrong__email-instead-of-transfer"
doc_id: "chatty-ai-wrong-responses"
title: "Configure AI to send contact email instead of live transfer"
category: "ai-wrong-responses"
tags: ["email instead of transfer", "contact via email", "human handover", "email handover", "no live agent"]
applies_when: "Merchant wants AI to configure handover to send contact details via email instead of doing a live transfer"
```

## Configure AI to Send Email Instead of Live Transfer

Go to **AI Assistant** → **Instructions** → **Assistant Skills** → **Human Handover** and configure:
- Set handover method to **email** (not live agent assignment)
- Enter the support email address to receive conversation details
- Update the pre-transfer message to set correct expectation: *"I'll send your question to our team and they'll reply by email."*

If the setting is not available or unclear, contact support with: current handover setup screenshot and which email should receive the notifications.

---

<!-- CHUNK: ai-wrong-auto-transfer-timer -->
```yaml
chunk_id: "ai-wrong__auto-transfer-timer"
doc_id: "chatty-ai-wrong-responses"
title: "Auto-transfer to human after fixed time without response"
category: "ai-wrong-responses"
tags: ["auto-assign", "timer", "time-based transfer", "fixed time", "no response", "auto escalate"]
applies_when: "Merchant wants AI to automatically transfer to a human after a fixed time without a response"
```

## Auto-Transfer After Fixed Time

**Not a built-in feature yet** — time-based auto-transfer is on the roadmap.

**Available workaround:**
- Go to **Automation** → create a rule: *"If conversation has no reply for X hours → assign to [team/agent]"*
- This is not an AI-specific rule but covers the use case at the automation level

**If the automation workaround doesn't fit the merchant's needs:**
- Log a feature request with: merchant's store URL, their specific use case (e.g. "transfer after 2 hours if AI hasn't resolved")
- Add to the product team's feature request tracker

---

## Related
- [case_ai-product-sync](case_ai-product-sync.md) — product sync stuck, missing or deleted products
- [case_ai-wrong-responses](case_ai-wrong-responses.md) — this file
- faq_data-sources — file upload limits, training data types
- faq_train-ai — how to fix AI training data
