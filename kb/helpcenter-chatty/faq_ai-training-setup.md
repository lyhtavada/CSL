# AI Training & Setup

<!-- CHUNK: ai-training-setup-first-time -->
```yaml
chunk_id: "ai-training__setup-first-time"
doc_id: "chatty-ai-training"
title: "How to set up AI training for the first time"
category: "ai-training"
tags: ["ai", "setup", "first time", "train", "get started", "onboarding"]
applies_when: "Merchant asks how to set up or get started with AI training"
```

## Setting Up AI Training for the First Time

Advanced AI features (Store Instructions, Scenarios, QnA, Data Source expansion) are only available on **paid plans**.

**Steps:**
1. Check the merchant's plan first — Free plan has limited AI features
2. Go to **AI Assistant** → **Instructions** to add custom instructions
3. Go to **AI Assistant** → **Data Sources** to add training data (products, FAQs, URLs, files)
4. Go to **AI Assistant** → **Test** to test responses before going live

For high-revenue stores (ARR > $200K on a paid plan), proactively offer help with initial setup and a demo call with PM.

---

<!-- CHUNK: ai-training-restore-instructions -->
```yaml
chunk_id: "ai-training__restore-instructions"
doc_id: "chatty-ai-training"
title: "Restore deleted AI instructions"
category: "ai-training"
tags: ["restore", "reset", "deleted", "recover", "AI instructions", "default instructions"]
applies_when: "Merchant accidentally deleted their AI instructions and wants to restore or recover them"
```

## Restoring Deleted AI Instructions

To recover deleted AI Instructions, contact support team for further help.

---

<!-- CHUNK: ai-training-test-feature -->
```yaml
chunk_id: "ai-training__test-feature"
doc_id: "chatty-ai-training"
title: "Test AI responses without using quota"
category: "ai-training"
tags: ["test", "testing", "quota", "AI replies", "check responses", "preview"]
applies_when: "Merchant wants to test AI responses, or asks how to check if AI is giving correct answers"
```

## Testing AI Responses

Use the built-in **Test** feature — it does **NOT** count against the merchant's AI replies quota.

1. Go to **AI Assistant** → **Test**
2. Enter questions and check AI responses

**Important:** Under the new pricing policy, each plan (except Plus) has limited AI Replies. Do not test directly on the merchant's live chat without permission.

---

<!-- CHUNK: ai-training-hide-support-email -->
```yaml
chunk_id: "ai-training__hide-support-email"
doc_id: "chatty-ai-training"
title: "Prevent AI from sharing store support email"
category: "ai-training"
tags: ["email", "support email", "hide email", "custom instruction", "contact email"]
applies_when: "Merchant does not want the AI to share or reveal the store's support email address in chat"
```

## Prevent AI from Sharing Support Email

1. Go to **AI Assistant** → **Instructions**
2. Add: `Do not provide Store Support Email addresses to customers.`
3. Save the changes
4. Test by asking "How can I contact support?" to confirm the email is no longer shown

---

<!-- CHUNK: ai-training-disable-followup -->
```yaml
chunk_id: "ai-training__disable-followup"
doc_id: "chatty-ai-training"
title: "Disable AI follow-up questions"
category: "ai-training"
tags: ["follow-up", "follow up questions", "disable", "AI behavior", "unnecessary questions"]
applies_when: "Merchant wants to stop the AI from asking follow-up questions after answering"
```

## Disabling AI Follow-Up Questions

1. Confirm the merchant wants the AI to answer directly without follow-ups
2. CS agent disable the feature in **DevZone**: toggle off the follow-up questions option
3. Explain the impact: responses may be shorter and less personalized after disabling
4. Ask the merchant to test again and confirm behavior matches expectations

---

<!-- CHUNK: ai-training-add-bonus-conversations -->
```yaml
chunk_id: "ai-training__add-bonus-conversations"
doc_id: "chatty-ai-training"
title: "Add bonus AI conversations for a merchant"
category: "ai-training"
tags: ["bonus", "AI conversations", "limit", "ran out", "add more", "DevZone"]
applies_when: "Merchant ran out of AI conversations and needs more added"
```

## Adding Bonus AI Conversations

1. Go to **DevZone** > **Testing**
2. Enter the number of conversations to add in the **Limit** field
3. Click **Set**

---

<!-- CHUNK: ai-training-wrong-support-email -->
```yaml
chunk_id: "ai-training__wrong-support-email"
doc_id: "chatty-ai-training"
title: "AI showing wrong contact email"
category: "ai-training"
tags: ["wrong email", "incorrect email", "contact email", "support email", "AI settings"]
applies_when: "AI is sending the wrong support email address to customers"
```

## AI Showing Wrong Support Email

The AI pulls the support email from **AI Assistant** → **Transfer** → **Contact Support Email**.

1. Check which email the AI sent to the customer
2. Go to **Chatty** > **AI Assistant** > **Transfer**, check the Contact Support Email field
3. If wrong, guide the merchant to update it with the correct one
4. After updating, the AI will automatically use the new email

---

<!-- CHUNK: ai-training-ai-not-replying-email -->
```yaml
chunk_id: "ai-training__ai-not-replying-email"
doc_id: "chatty-ai-training"
title: "AI not replying to emails in inbox"
category: "ai-training"
tags: ["email", "AI not replying", "email channel", "inbox", "auto-reply"]
applies_when: "AI is not responding to emails forwarded to the inbox"
```

## AI Not Replying to Emails

1. Verify AI email channel is enabled: **AI Assistant Settings** > **AI Channels** > **Email**
2. AI auto-replies after 5 minutes if no agent responds — only to genuine customer inquiries (not spam or system notifications)
3. If configured correctly but AI still doesn't reply, escalate to the dev team

---

<!-- CHUNK: ai-training-auto-transfer -->
```yaml
chunk_id: "ai-training__auto-transfer"
doc_id: "chatty-ai-training"
title: "AI not automatically transferring to human agents"
category: "ai-training"
tags: ["transfer", "human handover", "auto-assign", "unassigned", "talk to human"]
applies_when: "AI detected talk-to-human intent but did not assign the conversation to an agent"
```

## AI Not Transferring to Human Agents

- **Manual Assignment:** The system does not auto-assign. Merchant must manually assign conversations. Recommend switching to Automatic Assignment.
- **Automatic Assignment (round-robin):** Check "Reassign conversations" settings. If configured correctly but still showing "Unassigned," collect conversation details and escalate to TS/dev team.

---

<!-- CHUNK: ai-training-hide-product-card -->
```yaml
chunk_id: "ai-training__hide-product-card"
doc_id: "chatty-ai-training"
title: "Hide product preview card in AI chat"
category: "ai-training"
tags: ["product card", "preview card", "hide", "CSS", "product preview"]
applies_when: "Merchant does not want the product preview card to show in chat conversations"
```

## Hiding Product Preview Card

There is currently **no dedicated app setting** to disable product preview cards. The preview card shares CSS with the "Reply to" element — hiding via CSS would hide both.

- If merchant doesn't want AI to sell → suggest adjusting AI to focus on support skills instead
- If concerned about cluttered UI → explain the CSS limitation
- If they need more control → log feedback and escalate to the product team

---

<!-- CHUNK: ai-training-prechat-form -->
```yaml
chunk_id: "ai-training__prechat-form"
doc_id: "chatty-ai-training"
title: "AI responds before pre-chat form is filled"
category: "ai-training"
tags: ["pre-chat form", "AI responds first", "product assistant", "customer info", "form"]
applies_when: "Merchant enabled pre-chat form but customers still get AI responses before filling it out"
```

## AI Responds Before Pre-Chat Form

This happens when customers interact via the **AI Product Assistant** on the product page — it prioritizes quick answers without requiring customer info first.

If the merchant's priority is collecting customer info before any response, they should hide the **AI Product Assistant** on the storefront and rely solely on the pre-chat form.

---

<!-- CHUNK: ai-training-create-scenario -->
```yaml
chunk_id: "ai-training__create-scenario"
doc_id: "chatty-ai-training"
title: "Create an AI scenario / custom scenario"
category: "ai-training"
tags: ["scenario", "custom scenario", "flow", "AI flow", "create scenario", "add scenario"]
applies_when: "Merchant wants to make the AI follow a specific flow or handle a specific topic"
```

## Creating an AI Scenario

Go to **AI Assistant** → **Instructions** → **Assistant Skills** → **Custom Scenarios**, then click **Add Scenario** and define:

1. **Scenario name** — the topic your customers mention
2. **Instructions** — the messages or flow you want the AI to follow

Use this for returns, order lookups, discount requests, or any specific process you want the AI to handle consistently.

---

<!-- CHUNK: ai-training-product-limit -->
```yaml
chunk_id: "ai-training__product-limit"
doc_id: "chatty-ai-training"
title: "AI product sync limit by plan"
category: "ai-training"
tags: ["product limit", "SKU limit", "sync products", "plan limit", "how many products"]
applies_when: "Merchant asks how many products the AI can train on, or hits the product sync limit"
```

## AI Product Sync Limits

| Plan | Product limit |
|------|--------------|
| Free | 100 products |
| Basic | 500 products |
| Pro | 8,000 products |
| Plus | 20,000 products |

If the store exceeds the plan limit, Chatty trains on the most recently updated products first. For stores with more than 5,000 products, contact support — this requires manual backend configuration.

---

<!-- CHUNK: ai-training-inventory-sync -->
```yaml
chunk_id: "ai-training__inventory-sync"
doc_id: "chatty-ai-training"
title: "AI product inventory sync"
category: "ai-training"
tags: ["inventory", "stock", "sync", "product sync", "stock quantity", "out of stock"]
applies_when: "Merchant asks if AI syncs product inventory or stock quantity"
```

## AI Product Inventory Sync

Chatty syncs product data including inventory status from Shopify. However, **real-time automatic stock quantity updates are not supported**.

To sync the latest data manually: **AI** → **Training Data** → **Products** → click **Sync Products**.

---

<!-- CHUNK: ai-training-language -->
```yaml
chunk_id: "ai-training__language"
doc_id: "chatty-ai-training"
title: "Training data language for best AI accuracy"
category: "ai-training"
tags: ["language", "training data", "English", "multilingual", "AI accuracy"]
applies_when: "Merchant asks what language to write training data in for best AI results"
```

## Training Data Language

The AI performs best with training data in the same language your customers use. For multilingual audiences, you can add training data in multiple languages.

Avoid mixing languages in a single FAQ entry — it may reduce accuracy.

---

<!-- CHUNK: ai-training-multilingual-products -->
```yaml
chunk_id: "ai-training__multilingual-products"
doc_id: "chatty-ai-training"
title: "AI learning from multilingual product descriptions"
category: "ai-training"
tags: ["multilingual", "product descriptions", "language", "translations"]
applies_when: "Merchant asks how the AI handles product descriptions in multiple languages"
```

## Multilingual Product Descriptions

Chatty's AI reads Shopify product descriptions as written. If descriptions are available in multiple languages, the AI can answer in those languages.

For best results, ensure each product has complete descriptions in all supported languages. You can also add multilingual FAQs manually in **AI** → **Training Data**.

---

<!-- CHUNK: ai-training-page-context -->
```yaml
chunk_id: "ai-training__page-context"
doc_id: "chatty-ai-training"
title: "AI detects current product page context"
category: "ai-training"
tags: ["product page", "page context", "product-specific", "current page", "AI product assistant"]
applies_when: "Merchant asks if the AI can detect which product page the customer is on"
```

## AI Page Context Detection

Yes — Chatty automatically detects the current page URL and product context. When a customer asks a question on a product page, the AI uses that product's information to answer.

Make sure the **AI Product Assistant** feature is enabled in AI Settings.

---

<!-- CHUNK: ai-training-collection-recommendations -->
```yaml
chunk_id: "ai-training__collection-recommendations"
doc_id: "chatty-ai-training"
title: "AI recommending products from the same collection"
category: "ai-training"
tags: ["recommendations", "collection", "product recommendations", "smart recommendations"]
applies_when: "Merchant wants the AI to recommend products from the same collection as the page being viewed"
```

## Collection-Based Product Recommendations

Yes — if the AI detects the customer is on a product or collection page, it can use that context to make relevant recommendations.

Make sure **Products** data is enabled in Training Data. Use collection-specific scenarios to further improve accuracy.

---

<!-- CHUNK: ai-training-hide-phone -->
```yaml
chunk_id: "ai-training__hide-phone"
doc_id: "chatty-ai-training"
title: "Prevent AI from sharing store phone number"
category: "ai-training"
tags: ["phone number", "hide phone", "contact info", "custom instruction", "scenario"]
applies_when: "Merchant does not want the AI to share or mention the store's phone number"
```

## Prevent AI from Sharing Phone Number

1. Go to **AI** → **Training Data** and remove/replace any phone number mentions with a redirect message: `For phone inquiries, please contact us via email.`
2. Create a **Custom Scenario**: `Do not share the store phone number. Direct customers to contact us via email instead.`

---

<!-- CHUNK: ai-training-best-content -->
```yaml
chunk_id: "ai-training__best-content"
doc_id: "chatty-ai-training"
title: "What to include in AI training data for best results"
category: "ai-training"
tags: ["training data", "best practices", "what to include", "AI accuracy", "setup tips"]
applies_when: "Merchant asks what content to add for the best AI training results"
```

## Best AI Training Content

Include:
- **Accurate product descriptions** with measurements, materials, and key specifications
- **FAQs** covering common questions (shipping, returns, sizing, payments)
- **Custom Scenarios** for specific flows like order status, discount codes, return requests

Keep content clear, avoid conflicting information, and update regularly as products or policies change.

---

<!-- CHUNK: ai-training-size-recommendation -->
```yaml
chunk_id: "ai-training__size-recommendation"
doc_id: "chatty-ai-training"
title: "Set up size recommendation via AI"
category: "ai-training"
tags: ["size", "size guide", "sizing", "recommendation", "custom scenario", "size chart"]
applies_when: "Merchant wants the AI to recommend sizes or answer sizing questions"
```

## Size Recommendation Setup

1. Go to **AI** → **Training Data** → **Custom Scenarios**
2. Define triggers: `what size`, `size guide`, `how does it fit`
3. In the instructions, guide the AI to refer to the size chart or direct customers to the size guide page

Make sure product descriptions include clear size/measurement information.

On Pro plan or higher, you can also use the **Size Guide Agent** feature directly.

---

<!-- CHUNK: ai-training-wrong-product-links -->
```yaml
chunk_id: "ai-training__wrong-product-links"
doc_id: "chatty-ai-training"
title: "AI referencing products from wrong website or giving wrong links"
category: "ai-training"
tags: ["wrong product", "wrong link", "product link", "wrong catalog", "different website"]
applies_when: "AI is referencing products from a different website or giving incorrect product links"
```

## AI Giving Wrong Product Links

This usually means the AI matched a query to incorrect backend data (e.g., a collection lookup). Contact support with the **conversation ID** — the team will add an instruction hook to fix the response logic.

As a preventive step, ensure product descriptions are detailed and unambiguous.

---

<!-- CHUNK: ai-training-view-similar -->
```yaml
chunk_id: "ai-training__view-similar"
doc_id: "chatty-ai-training"
title: "Product FAQs and View Similar recommendations"
category: "ai-training"
tags: ["view similar", "recommendations", "product FAQs", "smart recommendations"]
applies_when: "Merchant asks if adding product FAQs will improve View Similar recommendations"
```

## Product FAQs and "View Similar" Recommendations

No — product FAQs do **not** influence the "View Similar" recommendation feature. Recommendations are handled through **Smart Recommendations** settings, not FAQ data.

---

<!-- CHUNK: ai-training-plan-product-limit -->
```yaml
chunk_id: "ai-training__plan-product-limit-exceeded"
doc_id: "chatty-ai-training"
title: "AI not syncing enough products due to plan limit"
category: "ai-training"
tags: ["plan limit", "product sync", "upgrade", "not syncing", "too few products"]
applies_when: "Merchant's plan limit is too low and AI is not syncing all their products"
```

## Plan Product Limit Too Low

Each plan has a product sync limit (Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000). If you've hit the limit:

- Contact support and share what you need — the team will review and confirm if a one-time extension is possible (subject to approval)
- For permanent higher limits, upgrade your plan
- If you have more than 5,000 products, contact support directly — this requires manual backend configuration

---

<!-- CHUNK: ai-training-wrong-catalog -->
```yaml
chunk_id: "ai-training__wrong-catalog"
doc_id: "chatty-ai-training"
title: "AI recommending products from a different store's catalog"
category: "ai-training"
tags: ["wrong catalog", "different store", "wrong products", "backend", "collection data"]
applies_when: "AI is recommending or referencing products from a different store's catalog"
```

## AI Using Wrong Store's Catalog

Contact support with the **conversation ID**. This is typically caused by the AI matching against backend collection data incorrectly. The team will add an instruction hook to prevent this behavior.

---

<!-- CHUNK: ai-training-website-content -->
```yaml
chunk_id: "ai-training__website-content"
doc_id: "chatty-ai-training"
title: "AI reading website content automatically"
category: "ai-training"
tags: ["website", "URL", "auto-read", "custom knowledge", "web content", "domain"]
applies_when: "Merchant asks if the AI automatically reads their website content"
```

## AI and Website Content

**Note:** This applies to external websites only. Shopify store pages (About us, Shipping policy, Return policy, Privacy policy, Terms of service, FAQ, Contact us) are automatically synced — no URL submission needed for these.

For external websites: No — the AI does **not** automatically read your website. You must submit specific page URLs to the **Custom Knowledge** section.

Submitting just the domain (e.g., `yourstore.com`) only trains on the homepage content — submit individual page URLs for full coverage.

---

<!-- CHUNK: ai-training-ai-model -->
```yaml
chunk_id: "ai-training__ai-model"
doc_id: "chatty-ai-training"
title: "What AI model does Chatty use"
category: "ai-training"
tags: ["AI model", "model", "GPT", "Claude", "underlying model", "LLM"]
applies_when: "Merchant asks what AI model or LLM Chatty is built on"
```

## What AI Model Does Chatty Use

Chatty uses its own AI assistant layer built on top of large language model technology. The specific underlying model is not publicly disclosed, but the AI is optimized for e-commerce support scenarios.

---

<!-- CHUNK: ai-training-wrong-language -->
```yaml
chunk_id: "ai-training__wrong-language"
doc_id: "chatty-ai-training"
title: "AI responding in the wrong language"
category: "ai-training"
tags: ["wrong language", "language detection", "Chinese", "Japanese", "language", "multilingual"]
applies_when: "AI is responding in the wrong language — not matching the language the customer used"
```

## AI Responding in Wrong Language

The AI is designed to respond in the customer's language. If it's getting confused (especially for very short or ambiguous messages), contact support with the **conversation ID**. The team can add an explicit instruction: `Always reply in the same language the customer is using.`

---

<!-- CHUNK: ai-training-repeat-faq -->
```yaml
chunk_id: "ai-training__repeat-faq"
doc_id: "chatty-ai-training"
title: "AI repeating auto-reply FAQ content in follow-up"
category: "ai-training"
tags: ["repeat", "auto-reply", "FAQ", "follow-up", "bug", "duplicate response"]
applies_when: "AI is repeating information from a previous auto-reply FAQ when answering a follow-up question"
```

## AI Repeating Auto-Reply FAQ Content

This is a **known bug**. Contact support with the **conversation ID** — the dev team can investigate and fix the response logic so the AI does not repeat content already shown in the auto-reply.

---

<!-- CHUNK: ai-training-suppress-atc -->
```yaml
chunk_id: "ai-training__suppress-atc"
doc_id: "chatty-ai-training"
title: "Suppress Add-to-Cart button in AI responses"
category: "ai-training"
tags: ["add to cart", "ATC", "suppress", "product button", "scenario", "custom scenario"]
applies_when: "Merchant wants to suppress or remove the Add-to-Cart button from AI responses"
```

## Suppressing Add-to-Cart Button

Scenario Instructions can set behavioral guidelines, but the Add-to-Cart button is a **system-level behavior** — it cannot be suppressed via scenario alone.

Contact support — the team can apply a custom instruction or CSS/code solution.

---

<!-- CHUNK: ai-training-provide-phone -->
```yaml
chunk_id: "ai-training__provide-phone"
doc_id: "chatty-ai-training"
title: "Make AI always provide contact phone number"
category: "ai-training"
tags: ["phone number", "contact", "always provide", "custom instruction", "scenario"]
applies_when: "Merchant wants the AI to always share a phone number when customers ask about contacting support"
```

## AI Always Providing Contact Phone Number

Two approaches:
1. Add the phone number to **General AI Instructions** so the AI references it broadly
2. Create a **Custom Scenario** (**AI Assistant** → **Instructions** → **Assistant Skills** → **Add Scenario**) triggered when customers ask about contacting the team

---

<!-- CHUNK: ai-training-loyalty-points -->
```yaml
chunk_id: "ai-training__loyalty-points"
doc_id: "chatty-ai-training"
title: "Can Chatty AI check customer loyalty points balance"
category: "ai-training"
tags: ["loyalty points", "rewards", "account", "customer data", "balance", "login"]
applies_when: "Merchant or customer asks if AI can check loyalty points or customer account data"
```

## AI and Loyalty Points / Customer Account Data

No — Chatty AI **cannot** access customer account data (login status, loyalty points balance, etc.).

As a workaround, create a **Custom Scenario** that directs customers to your login/registration page when they ask about rewards or account-specific questions.

---

<!-- CHUNK: ai-training-scenario-character-limit -->
```yaml
chunk_id: "ai-training__scenario-character-limit"
doc_id: "chatty-ai-training"
title: "Increase character limit for Custom Scenario instructions"
category: "ai-training"
tags: ["character limit", "scenario", "too long", "limit", "custom scenario"]
applies_when: "Merchant hits the character limit when writing Custom Scenario instructions"
```

## Custom Scenario Character Limit

Currently the character limit for individual scenario fields **cannot be increased**. Contact support — the team can help optimize and shorten the scenario text to fit within the limit.

---

<!-- CHUNK: ai-training-metafields -->
```yaml
chunk_id: "ai-training__metafields"
doc_id: "chatty-ai-training"
title: "Does AI read metafields from Shopify products"
category: "ai-training"
tags: ["metafields", "metaobject", "Shopify metafields", "product data", "sync metafields"]
applies_when: "Merchant asks whether the AI can read and use Shopify product metafields"
```

## AI and Shopify Metafields

Yes — metafields are synced if they are published and readable via the Shopify API. Go to **AI Assistant → Training Data → Products** to verify metafield data is available after syncing.

**Limitation:** Metaobject references (metafields that reference other metaobjects) are not yet fully supported — this feature is in development. Log all requests for this in the tracking sheet.

---

<!-- CHUNK: ai-training-file-upload-details -->
```yaml
chunk_id: "ai-training__file-upload-details"
doc_id: "chatty-ai-training"
title: "Upload bulk files (PDF, CSV) to train AI"
category: "ai-training"
tags: ["file upload", "PDF", "CSV", "bulk upload", "training file", "upload file", "2MB"]
applies_when: "Merchant wants to upload files to train the AI assistant"
```

## Uploading Files for AI Training

Go to **AI Assistant → Training Data → Add Data Source → Upload File**.

| Format | Notes |
|--------|-------|
| PDF | Supported; not ideal for structured data |
| CSV | **Recommended** for product catalogs and structured Q&A |
| TXT | Supported |
| JSON | Supported |

- Max file size: **2MB per file**
- For large product catalogs → CSV gives better results than PDF
- AI uses RAG — similar customer questions match the closest trained entry

---

<!-- CHUNK: ai-training-language-switching -->
```yaml
chunk_id: "ai-training__language-switching"
doc_id: "chatty-ai-training"
title: "AI switching language mid-conversation or responding in wrong language"
category: "ai-training"
tags: ["wrong language", "language switch", "mid-conversation", "translation", "store language", "respond in language"]
applies_when: "AI responds in English when the store or customer language is different, or switches language mid-conversation"
```

## AI Language Switching / Wrong Language Response

1. Go to **Settings → Translation** → confirm the correct **default language** is set
2. Go to **AI Assistant → Instructions → Custom Instructions** → add:
   > *"Always respond in the same language as the customer."*
3. For real-time translation between agent and customer in the inbox → requires **Pro or Plus plan**

> Free/Basic plans: AI responds based on training data language + customer input. Explicit instruction in step 2 is the most effective fix.

---

<!-- CHUNK: ai-training-brand-voice -->
```yaml
chunk_id: "ai-training__brand-voice"
doc_id: "chatty-ai-training"
title: "AI responding in generic tone not matching brand voice"
category: "ai-training"
tags: ["brand voice", "tone", "persona", "generic tone", "custom tone", "AI tone", "instructions"]
applies_when: "Merchant wants the AI to match their brand's tone and communication style"
```

## Setting AI Brand Voice / Tone

Go to **AI Assistant → Instructions → Custom Instructions** and add brand tone guidelines. Examples:

- *"You are a friendly assistant for [Brand]. Use warm, casual language."*
- *"Never say 'I apologize' — say 'I'm sorry' instead."*
- *"Write in UK English. Use formal but approachable language."*
- *"Keep responses concise — no more than 3 sentences unless the question requires detail."*

Many merchants skip the Instructions setup entirely — if AI sounds generic, this is the first thing to configure.

---

<!-- CHUNK: ai-training-disable-product-recommendations -->
```yaml
chunk_id: "ai-training__disable-product-recommendations"
doc_id: "chatty-ai-training"
title: "Reduce or disable AI product recommendations in chat"
category: "ai-training"
tags: ["disable recommendations", "product recommendations", "Smart Recommendations", "no recommendations", "turn off"]
applies_when: "Merchant wants to reduce or disable unsolicited product recommendations from the AI"
```

## Disabling AI Product Recommendations

**Option 1 — Toggle Smart Recommendations off:**
Go to **AI Assistant → Instructions → AI Skills → Smart Recommendations** → Toggle **OFF**

**Option 2 — Custom Instruction:**
Add to Custom Instructions: *"Do not recommend products unless the customer explicitly asks for a recommendation."*

> Smart Recommendations is a **Pro+ feature**. On lower plans, AI uses general product sync — disable via Custom Instructions.

---

<!-- CHUNK: ai-training-bot-name-avatar -->
```yaml
chunk_id: "ai-training__bot-name-avatar"
doc_id: "chatty-ai-training"
title: "Change AI bot name, welcome message, or avatar"
category: "ai-training"
tags: ["bot name", "AI name", "welcome message", "avatar", "greeting", "bot avatar", "AI branding"]
applies_when: "Merchant wants to change the AI assistant's display name, greeting message, or avatar image"
```

## Changing AI Bot Name / Welcome Message / Avatar

Go to **AI Assistant → Instructions**:

- **Bot name** → change the displayed assistant name (replaces default "Chatty AI")
- **Welcome message** → customize the opening greeting
- **Avatar** → upload a custom image (JPG or PNG, under 2MB)

Changes apply immediately. No republishing required.
