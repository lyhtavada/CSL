# QA Feedback Corrections


---

# Chatty Knowledge Base

---

## Uninstalling Chatty

### What do I need to do after uninstalling the app?

In some cases, when the app is removed from your Shopify store, the code might remain in your store. This happens because Chatty loses access to the theme files immediately when you uninstall the app.

Follow these steps to ensure that your store continues to run smoothly.

### 1. Verify uninstallation process

Make sure that you've properly uninstalled Chatty from your store.

Go to **Settings** -> **Apps and sales channels** -> Double-check app list to confirm that Chatty is no longer available.

### 2. Delete FAQ page

- Get access to Shopify Admin -> Online store -> Pages
- Select page "Frequently Asked Question"
- Click **Actions** -> **Delete pages**

### 3. Handle lost conversations

The first thing to consider when uninstalling Chatty is that you will lose access to all chat conversations you have with customers.

- Before uninstalling, check important conversation data and manually save critical information from recent conversations
- Inform your team that chat data will no longer be accessible
- Create a plan for addressing customer concerns about previous conversations

### 4. Update new customer service

Chatty helps you provide customer service and support. Now that Chatty's uninstalled, consider:

- Setting up a new FAQs page to help answer customers' questions
- Updating your "Contact Us" page with clear instructions
- Implementing an alternative live chat solution

If you have any more concerns, please contact the support team.

---

## Getting Started - Intro to Chatty

**Who can use Chatty?**

- Chatty is available on Shopify App Store for all Shopify store plans

Chatty helps you communicate directly with visitors on your website, solve their problems, and guide them through their shopping experience towards making purchases.

Chatty is your best AI sales assistant.

Setting up Chatty is as straightforward as it gets. With a few simple steps, you'll be ready to:

#### Live chat

- Enable live chat with customers
- Set up various contact methods: WhatsApp, Messenger, etc.
- Invite team members to manage conversations together

#### AI chatbot

- Enable AI assistant for 24/7 support
- Train AI with data about your stores & products
- Customize your AI assistant with brand image, voice & tone

#### Help center

- Build a self-serve knowledge hub with common questions and answers
- Show FAQs page and section in chatbox with customized theme
- Translate FAQs into multiple languages

### For your kickstart

See the Quick Start guide to get started.

### Get more assistance

If you have any further concerns, search your topic on the help site or look through the Frequently Asked Questions list.

The Customer Success team also offers 24/7 assistance via email and live chat.

---

## About Chatty

Chatty is an AI-powered customer support and sales assistant for Shopify stores. It combines live chat, AI chatbot, and a self-serve help center (FAQs) to help merchants communicate with customers, answer questions, and drive sales.

Key capabilities: live chat with multiple channels (WhatsApp, Messenger, Instagram, email), AI assistant with product recommendations, FAQs/knowledge base, proactive chat campaigns, team collaboration, and analytics.

---

## Integrations - Chatty Public API

**Who can use this feature?**

- Available to all users on any plan.

### Overview

The Chatty Public API gives you direct access to your store's customer data — things like contact details, chat history timestamps, order counts, and total spend. It's useful when you want to:

- Sync Chatty contacts into a custom CRM
- Send customer segments to an email platform
- Pull data into a spreadsheet or BI tool
- Build a custom dashboard or internal integration

If you're looking for ready-made integrations, check out Klaviyo, Zendesk, or Joy instead.

### Generate your API key

Go to **Settings > API** in your Chatty dashboard.

Click **Generate key**. You'll immediately see two credentials:

| Credential | What it's for |
|---|---|
| **App ID** | Your store identifier. Include this in every API request. |
| **Secret key** | Your private authentication key. Never share this publicly. |

**Copy your Secret key right away.** It's only shown once. If you lose it, you'll need to generate a new one — which immediately deactivates the old key.

If your key is ever compromised, click **Generate key** again to rotate it. The previous key stops working instantly.

### Common use cases

**Export contacts to a spreadsheet**
Use the `customers` query with pagination to pull all contacts, then write them to a CSV.

**Sync high-value customers to an email platform**
Filter by `totalSpent` on your side and push matching customers to your email tool via its own API.

**Build a custom CRM view**
Use `ordersCount`, `totalSpent`, `lastChatAt`, and `channels` to segment and prioritize follow-ups.

**Track engagement over time**
Use `lastChatAt` and `createdAt` to measure how recently customers have been active in chat.

### Need help?

If you run into issues with your API key or requests, contact the Chatty support team from your dashboard. For ready-made integrations without any code, see Klaviyo, Zendesk, or Joy.


---

# Access & Login Issues

<!-- CHUNK: access-login-account-not-activated -->
```yaml
chunk_id: "case__access-login-account-not-activated"
doc_id: "cs-case-access-login-issues"
title: "Merchant sees 'Account not activated' when logging into Chatty"
category: "troubleshooting"
subcategory: "access-login"
tags: ["login", "account not activated", "app.meetchatty.com", "access", "activation"]
applies_when: "Merchant gets 'Account not activated' error when trying to log in to app.meetchatty.com"
priority: "high"
```

## Symptom

Merchant sees "Account not activated" error on app.meetchatty.com.

## Common Causes

1. Merchant has never opened Chatty from Shopify Admin after installing — no internal account was created.
2. App was uninstalled and reinstalled but the old account wasn't reactivated.
3. Merchant is trying to log in directly via external link instead of through Shopify Admin.
4. Browser has cached old data.

## Resolution

1. Guide the merchant to open Chatty from **Shopify Admin → Apps → Chatty** to activate the account.
2. After activation, they can use app.meetchatty.com normally.
3. If issue persists, suggest clearing browser cache and trying again.

---

<!-- CHUNK: access-login-incorrect-password -->
```yaml
chunk_id: "case__access-login-incorrect-password"
doc_id: "cs-case-access-login-issues"
title: "Merchant or team member gets 'Incorrect email or password' on Chatty web app"
category: "troubleshooting"
subcategory: "access-login"
tags: ["login", "incorrect password", "wrong password", "sign in", "web app", "team member"]
applies_when: "Merchant or agent can't log in to app.meetchatty.com due to wrong email/password"
priority: "high"
```

## Symptom

"Incorrect email or password" error on app.meetchatty.com.

## Resolution

Ask the merchant which sign-up method they used:

**If they used "Create account" (custom password):**
- Log in with email + the password created during sign-up.
- If forgotten → click "Forgot password" to reset.

**If they used "Sign up with Google":**
- Click "Sign in with Google" and use the same Gmail account they signed up with.

Ask the merchant/agent which method they used first, then guide accordingly.

---

<!-- CHUNK: access-login-dev-store-blocked -->
```yaml
chunk_id: "case__access-login-dev-store-blocked"
doc_id: "cs-case-access-login-issues"
title: "Development store is blocked or shows 'Not Found' in Chatty"
category: "troubleshooting"
subcategory: "access-login"
tags: ["dev store", "blocked", "not found", "blacklisted domain", "competitor"]
applies_when: "A development store or user from a blacklisted domain cannot access Chatty"
priority: "medium"
```

## Symptom

App shows "Not Found" or blocks access on a development store.

## Cause

Chatty automatically blocks access from development stores with emails from blacklisted domains (competitors and known testing accounts).

**Blacklisted domains:** @tidio.com, @intercom.com, @firegroup.io, @flowio.app, @beae.com, @fireapps.vn, @channelwill.cn, @bsscommerce.com, @amasty.com, @secomus.com, @appsfinal.com, @omegatheme.com, @loox.io, @samita.io.

## Resolution

If the merchant's email belongs to a blacklisted domain, CS does not need to continue support — resolve the conversation.

---

<!-- CHUNK: access-login-china-white-screen -->
```yaml
chunk_id: "case__access-login-china-white-screen"
doc_id: "cs-case-access-login-issues"
title: "Does Chatty work in China? Google Cloud blocked by Great Firewall — VPN required"
category: "troubleshooting"
subcategory: "access-login"
tags: ["china", "white screen", "blank screen", "Great Firewall", "VPN", "Google Cloud", "access blocked", "work in China", "China store", "regional availability"]
applies_when: "Merchant asks if Chatty works in China, or a merchant located in China sees a white/blank screen when opening Chatty"
priority: "medium"
```

## Chatty in China

Chatty may have limited functionality or not work at all in China because it is hosted on Google Cloud, which is commonly blocked by China's Great Firewall. Merchants in China should use a VPN to access the Chatty admin.

## Symptom

Merchant from China sees a blank white screen with console errors when opening Chatty.

## Cause

Chatty is hosted on Google Cloud, which is commonly blocked by China's Great Firewall.

## Resolution

1. Confirm the merchant is located in China.
2. If not using a VPN → guide them to use a reputable VPN that works in China.
3. If already using a VPN → suggest trying a different VPN or network.
4. Send the standalone link `https://app.meetchatty.com` and instruct them to try with VPN enabled.
5. If other apps work fine, explain Chatty's Google Cloud hosting limitation.
6. Escalate to dev only if VPN + standalone link still doesn't work.

---

<!-- CHUNK: access-login-multiple-stores -->
```yaml
chunk_id: "case__access-login-multiple-stores"
doc_id: "cs-case-access-login-issues"
title: "Managing multiple Shopify stores with one Chatty account"
category: "troubleshooting"
subcategory: "access-login"
tags: ["multiple stores", "multi-store", "switch store", "one account", "team member"]
applies_when: "Merchant asks how to manage or access Chatty across multiple Shopify stores"
priority: "low"
```

## How It Works

Each Shopify store requires its own Chatty installation. The merchant accesses each store's Chatty separately through their Shopify Admin.

For team members who work across multiple stores: they can be invited as team members on each store's Chatty installation and switch between them.


---

# AI Conversation Limit Extension Request

<!-- CHUNK: ai-conversation-limit-overview -->
```yaml
chunk_id: "case__ai-conversation-limit-overview"
doc_id: "cs-case-ai-conversation-limit"
title: "AI Conversation Limit Extension — Overview & Escalation Requirement"
category: "cs-process"
subcategory: "limit-extension"
tags: ["AI conversation", "limit", "extend", "monthly quota", "escalate", "PM", "sale-cs-success"]
applies_when: "Merchant hits their monthly AI conversation limit and asks CS to increase it"
priority: "high"
```

## Overview

AI conversation limits are a **monthly quota** (except Free plan: 50 lifetime). When a merchant hits their limit and needs more, CS **cannot self-extend** — escalation to PM is required before making any changes.

CS does **NOT** extend AI Conversations without PM approval — this affects billing and product strategy. Post in **#sale-cs-success** and tag PM.

## Plan Limits Reference

| Plan | AI Conversations |
|------|-----------------|
| Free | 50 lifetime (AI deactivates when reached) |
| Basic | 50/month + $0.40/extra |
| Pro | 300/month + $0.40/extra |
| Plus | 700/month + $0.40/extra |

---

<!-- CHUNK: ai-conversation-limit-flow -->
```yaml
chunk_id: "case__ai-conversation-limit-flow"
doc_id: "cs-case-ai-conversation-limit"
title: "AI Conversation Limit Extension — Step-by-Step Flow"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "escalate", "sale-cs-success", "PM", "upgrade", "flow", "AI conversation"]
applies_when: "CS needs to handle a merchant's request for more AI conversations"
priority: "high"
```

## Resolution Steps

### Step 1 — Gather information before escalating

Collect from the merchant or via their account:
- Store URL
- Current plan (Free / Basic / Pro / Plus)
- Average number of chats per month (ask merchant or check analytics)
- Which plan they're considering upgrading to (if any)
- Reason for needing more conversations

### Step 2 — Check if upgrade solves it first

If the merchant is on a lower plan and the next plan up covers their volume → recommend upgrading first. Manual limit extension is for cases where upgrading alone isn't sufficient or the merchant needs a temporary bridge.

### Step 3 — Escalate for approval

Post in **#sale-cs-success** and tag PM with:
- Store URL + current plan
- Monthly chat volume (estimated)
- Plan they're considering / reason they need more
- Requested extension amount (if merchant specified)

Wait for approval before making any changes.

### Step 4 — Follow up with merchant

Once approved, confirm the extension has been applied and advise on next steps (upgrade recommendation if applicable).

**Sample response to merchant while waiting:**

> Thank you for reaching out! To help you get more AI conversations, I'll need a little more information:
>
> - Approximately how many chats does your store handle per month?
> - Are you considering upgrading your plan, or are you looking for a temporary extension?
>
> Once I have these details, I'll check with our team and get back to you as soon as possible.

---

<!-- CHUNK: ai-conversation-limit-approval-timeline -->
```yaml
chunk_id: "case__ai-conversation-limit-approval-timeline"
doc_id: "cs-case-ai-conversation-limit"
title: "AI Conversation Limit Extension — Approval Timeline & Process"
category: "cs-process"
subcategory: "limit-extension"
tags: ["approval", "timeline", "escalate", "sale-cs-success", "PM", "wait"]
applies_when: "CS has escalated the request and the merchant is asking about timeline"
priority: "low"
```

## After Escalation

After CS posts in #sale-cs-success and tags PM with full details, the team will review and respond in the channel. CS should wait for explicit approval before applying any changes.

Timeline depends on team availability — if urgent, note that in the escalation message.


---

# Extend AI Training Data Limits (Products / Custom Answers / URL & File)

<!-- CHUNK: extend-ai-training-limits-overview -->
```yaml
chunk_id: "case__extend-ai-training-limits-overview"
doc_id: "cs-case-extend-ai-training-limits"
title: "Extend AI Training Data Limits — Overview & Who Handles What"
category: "cs-process"
subcategory: "limit-extension"
tags: ["limit", "extend", "products", "custom_answers", "url_file", "ai_training", "devzone", "plan"]
applies_when: "Merchant hits their Products, Custom Answers, or URL & File limit for AI training and asks CS to increase it"
priority: "high"
```

## Overview

CS can self-extend 3 types of AI training data limits — no escalation needed:
- **Products for AI training**
- **Custom Answers for AI training**
- **URL & File for AI training**

CS does **NOT** extend AI Conversations or AI Scenarios — those require PM approval via #sale-cs-success.

## Plan Limits Reference

| Feature | Free | Basic ($19.99) | Pro ($68.99) | Plus ($199) |
| --- | --- | --- | --- | --- |
| Products for AI training | 100 | 500 | 8,000 | 20,000 |
| Custom Answers | 100 | 1,000 | Unlimited | Unlimited |
| URL & File | 20 | 50 | 500 | 700 |

---

<!-- CHUNK: extend-ai-training-limits-flow -->
```yaml
chunk_id: "case__extend-ai-training-limits-flow"
doc_id: "cs-case-extend-ai-training-limits"
title: "Extend AI Training Data Limits — Step-by-Step Flow"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "devzone", "extended-limit", "tag", "flow", "products", "custom_answers", "url_file"]
applies_when: "CS needs to extend a merchant's Products, Custom Answers, or URL & File limit"
priority: "high"
```

## Resolution Steps

### Step 1 — Confirm the merchant's situation

Verify:
- What plan are they on? (Free / Basic / Pro / Plus)
- Which limit did they hit? (Products / Custom Answers / URL & File)
- How much do they need?

### Step 2 — Decide how much to extend

Extend up to the next plan's limit — **1 tier only, no more**.

| Merchant's plan | Products → extend to | Custom Answers → extend to | URL & File → extend to |
| --- | --- | --- | --- |
| Free | 500 (= Basic) | 1,000 (= Basic) | 50 (= Basic) |
| Basic | 8,000 (= Pro) | Unlimited (= Pro) | 500 (= Pro) |
| Pro | 20,000 (= Plus) | Already Unlimited | 700 (= Plus) |
| Plus | Max reached → escalate PM | Already Unlimited | Max reached → escalate PM |

### Step 3 — Apply the extension in DevZone

1. Go to DevZone
2. Adjust the relevant limit (Products / Custom Answers / URL & File)
3. Confirm the change is applied

### Step 4 — Tag the conversation

Add tag **`extended-limit`** to the conversation in Crisp. Mandatory — do not skip.

### Step 5 — Confirm with merchant

> Great news! I've extended your [Products/Custom Answers/URL & File] limit so you can continue setting up your AI assistant. You should now be able to [sync more products / add more custom answers / upload more files].
>
> Just so you know, if you need even more capacity in the future, upgrading to [next plan] would give you [limit of next plan] and also unlock [key feature of that plan]. Let me know if you need any help with that!

---

<!-- CHUNK: extend-ai-training-limits-edge-cases -->
```yaml
chunk_id: "case__extend-ai-training-limits-edge-cases"
doc_id: "cs-case-extend-ai-training-limits"
title: "Extend AI Training Data Limits — Edge Cases & Decision Points"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "repeat_request", "free_plan", "plus_plan", "multiple_limits", "escalate", "upgrade"]
applies_when: "Non-standard situations when handling a limit extension request"
priority: "medium"
```

## Edge Cases

### Merchant requests multiple limits at once
Extend each limit type separately, all following the 1-tier rule. Apply all changes in DevZone, tag `extended-limit` once, confirm everything in a single message.

### Merchant has been extended before and comes back asking for more
This is a strong signal the merchant needs to upgrade. Push the upgrade clearly. If merchant still refuses → escalate to CSL. Do not extend again without CSL input.

### Merchant is on Free plan
Still extend up to Basic limits (same 1-tier rule). Make the extension but highlight the benefits of upgrading — the goal is to help them see Chatty's value and convert, not give unlimited free access.

### Merchant is on Plus and needs more than Plus limit
CS cannot self-extend beyond Plus limits. Escalate to PM via #sale-cs-success with: store URL, current plan, which limit is hit, and how much the merchant needs.

## Notes

- **Purpose of extending:** let the merchant experience enough value to upgrade on their own — not a permanent free pass.
- **Always tag `extended-limit`** after every extension — no exceptions.
- **Never extend AI Conversations or AI Scenarios** — those affect billing and product strategy, require PM approval.


---

# AI Product Sync Issues

<!-- CHUNK: ai-product-sync-stuck -->
```yaml
chunk_id: "ai-product-sync__stuck"
doc_id: "chatty-ai-product-sync"
title: "AI product sync stuck or not making progress"
category: "ai-product-sync"
tags: ["sync stuck", "product sync", "hanging", "not progressing", "sync frozen", "resync"]
applies_when: "AI product sync is stuck and not making progress"
```

## Product Sync Stuck

1. Go to **AI Assistant** → **Data Source** and check the timestamp of the most recent sync
2. If sync has been running too long with no progress → support agent goes to **DevZone** → **Testing** → click **Start Auto Resync** to reset and restart (warning: this restarts sync from scratch)
3. After resync, update the merchant. When products are fully displayed, notify them
4. Advise the merchant not to make changes (editing product tags, etc.) during resync to avoid data conflicts

---

<!-- CHUNK: ai-product-sync-missing-products -->
```yaml
chunk_id: "ai-product-sync__missing-products"
doc_id: "chatty-ai-product-sync"
title: "AI not syncing all products — product count mismatch"
category: "ai-product-sync"
tags: ["not syncing", "missing products", "product count", "product mismatch", "fewer products", "sync count"]
applies_when: "AI is not syncing all products from the store, or product count in AI doesn't match Shopify"
```

## AI Not Syncing All Products

Only **published, in-stock** products are synced to the AI. Products sync daily at **12:00 AM PST**.

Common causes:
- Products are in draft status or out of stock
- The merchant has hit their plan's product limit (Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000)
- Sync hasn't run yet after recent product changes

1. Check the merchant's plan and product count against the plan limit
2. Verify products are published and in stock in Shopify
3. Wait for the next daily sync or trigger a manual resync
4. If issue persists, escalate to the dev team

---

<!-- CHUNK: ai-product-sync-deleted-products -->
```yaml
chunk_id: "ai-product-sync__deleted-products"
doc_id: "chatty-ai-product-sync"
title: "Deleted products still showing in AI sync"
category: "ai-product-sync"
tags: ["deleted products", "removed products", "old products", "ghost products", "still showing"]
applies_when: "Merchant deleted products from Shopify but the AI still answers questions about them or they still appear in sync"
```

## Deleted Products Still Showing in AI

The sync may not immediately reflect product deletions.

1. Suggest the merchant turn off product synchronization entirely
2. When they add products back later, they can re-enable sync
3. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync

---

<!-- CHUNK: ai-product-sync-extend-limits -->
```yaml
chunk_id: "ai-product-sync__extend-limits"
doc_id: "chatty-ai-product-sync"
title: "Extend product, URL, or file limits for AI training"
category: "ai-product-sync"
tags: ["extend limit", "increase limit", "product limit", "URL limit", "file limit", "plan limit", "hit limit"]
applies_when: "Merchant has hit their AI training data limits and needs them extended"
```

## Extending AI Training Data Limits

1. Check the merchant's current plan and what data type they need more of (Products/URLs/Files)
2. Explain plan limits and recommend an appropriate upgrade
3. If the merchant is not ready to upgrade → escalate internally to PM + CSL
4. For small increases (100–200 products, 10–20 URLs/Files) → CS can proactively extend in **DevZone** without requiring an upgrade
5. For stores with > 10,000 products → offer a demo call with the sales lead — requires manual backend configuration
6. Never promise beyond your authority — always say "I'll check internally" before confirming extensions


---

# AI Scenario Limit Extension Request

<!-- CHUNK: ai-scenario-limit-overview -->
```yaml
chunk_id: "case__ai-scenario-limit-overview"
doc_id: "cs-case-ai-scenario-limit"
title: "AI Scenario Limit — Plan Limits & Escalation Requirement"
category: "cs-process"
subcategory: "limit-extension"
tags: ["AI scenario", "scenario limit", "extend", "escalate", "PM", "sale-cs-success", "plan limit"]
applies_when: "Merchant hits their AI scenario limit and asks CS to increase it"
priority: "high"
```

## Overview

AI scenario limits are set per plan. CS **cannot self-extend** scenario limits — escalation to PM or CSL is required.

## Plan Limits Reference

| Plan | AI Scenarios |
|------|-------------|
| Free | Up to 5 scenarios |
| Basic | Up to 5 scenarios |
| Pro | Up to 15 scenarios |
| Plus | — |

**Note:** Existing stores created before limits were introduced keep their existing scenario count (no retroactive limit applied). New stores follow the limits above.

---

<!-- CHUNK: ai-scenario-limit-flow -->
```yaml
chunk_id: "case__ai-scenario-limit-flow"
doc_id: "cs-case-ai-scenario-limit"
title: "AI Scenario Limit Extension — Step-by-Step Flow"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "escalate", "flow", "sale-cs-success", "PM", "use case", "scenarios"]
applies_when: "CS needs to handle a merchant's request for more AI scenarios"
priority: "high"
```

## Resolution Steps

### Step 1 — Understand what they need

Ask the merchant:
- How many additional scenarios they need and why
- What use cases or customer situations the new scenarios will cover (the more specific, the better — helps with approval)
- Their current plan

### Step 2 — Escalate for approval

Post in **#sale-cs-success** and tag PM or CSL with:
- Store URL + current plan
- Current number of scenarios in use
- Number of additional scenarios requested
- Use cases / situations the new scenarios will handle

Wait for approval before making any changes.

### Step 3 — Follow up with merchant

Once approved, confirm the limit has been updated and let the merchant know they can proceed.

**Sample response to merchant while waiting:**

> Thanks for getting in touch! To help with your request, could you share a bit more about what you'd like to use the additional scenarios for — for example, what types of customer questions or situations you're looking to cover?
>
> This helps us process your request faster. I'll follow up once I have an update from our team.


---

# AI Wrong Responses

<!-- CHUNK: ai-wrong-responses-general -->
```yaml
chunk_id: "ai-wrong__general-fix"
doc_id: "chatty-ai-wrong-responses"
title: "AI giving wrong answers — how to diagnose and fix"
category: "ai-wrong-responses"
tags: ["wrong answer", "incorrect", "AI wrong", "fix AI", "wrong information", "AI mistake"]
applies_when: "Merchant reports the AI is giving wrong or incorrect answers to customer questions"
```

## AI Giving Wrong Answers

1. Ask the merchant for the specific **chat link/ID** where the AI responded incorrectly
2. Click **Review Sources** under the AI reply to see which data sources and instructions were used
3. Diagnose the root cause:
   - **Source data is wrong/incomplete** → update or correct the source content
   - **Source is correct but AI misinterprets** → rephrase content or add more detail; report to dev team
   - **Instructions are inappropriate** → review Custom and Scenario Instructions and edit
4. If issue persists after corrections, escalate to the product/dev team

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

This happens when the AI pulls pricing from the main domain instead of market-specific pricing.

1. Check if **Sync Markets** is enabled in **AI Assistant** settings
2. Visit the merchant's market domain and test the same question yourself
3. If Markets are **NOT set up** → guide the merchant to set up Markets in Shopify Admin and enable "Sync Markets" in AI Assistant settings
4. If Markets **ARE set up but issue persists** → request staff access, collect screenshots and reproduction steps, report to dev team

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

This is a known bug acknowledged by the dev team.

1. Ask the merchant for the specific chat with the incorrect link
2. Test in **AI Test** section to confirm the issue
3. Report the store URL and chat link in the internal bug thread for dev follow-up
4. Inform the merchant the dev team is investigating — suggest manually copying correct product links as a workaround
5. Follow up when the fix is deployed

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

This is a **known technical limitation** — the app currently only stores product data for the main domain. Multi-domain support per Shopify Market is in development.

1. Confirm which market domain the customer visited and what URL the AI returned
2. Verify the merchant's Shopify Markets setup (country, domain mapping)
3. Inform the merchant this is a known limitation — a fix is planned
4. Create a tracking card and follow up with the merchant

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

This is a **feature limitation** — variant-level links have not been fully implemented yet. The AI can describe variants but cannot link directly to them.

A feature to support variant-specific links is in development. Inform the merchant in the meantime.

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

Common causes: customer re-sending same question, network lag, or temporary system error.

1. Request the chat ID and review to determine if user error or system error
2. If system error → create a card for TS with conversation link, timestamp, and merchant name
3. Suggest "refresh chat" or switch to manual chat if duplication continues
4. Follow up when the technical team responds

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

This can happen when AI training data is incomplete or not synced properly.

1. Request the chat ID of the incorrect response
2. Check AI settings: ensure product recommendation is enabled and sync is complete
3. If settings are correct → reproduce on storefront, then escalate to dev team with full details
4. If settings are incomplete → guide the merchant to enable and sync, then test again

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

1. Go to **AI Assistant** → **Instructions** → **Assistant Skills** → **Human Handover** and review the configured triggers — adjust or remove rules causing unintended escalation
2. Check **Automation** tab for assignment method — if **Automatic assignment** is selected, conversations transfer when trigger keywords are detected

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

This may be due to the store theme not supporting Chatty's add-to-cart function. The cart count may not update in real-time with certain themes — refresh the page after the AI confirms a product was added.

If the issue persists, share your **store collaborator code** so our team can investigate — this may require a theme-level fix.

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

The AI needs to be trained to format links as markdown.

1. Go to **AI Assistant** → **Instructions**
2. Under **Behaviours**, add: `When sharing a link, format it as [Link Name](URL).`

Alternatively, contact support — the team can update the AI prompt to ensure links are always rendered as clickable hyperlinks.

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

This happens when deleted or unpublished products are still in Chatty's training data.

1. Go to **AI Assistant** → **Training Data** → **Products**
2. Click **Sync Products** to refresh the catalog
3. Remove any manually added product URLs that are outdated
4. Use **Test AI** to verify recommendations after syncing

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

The AI is pulling raw HTML from your training data.

1. Go to **AI** → **Training Data** and review FAQ or scenario content
2. Remove all HTML tags (`<div>`, `<p>`, `<br>`, etc.) and replace with plain text
3. Use simple markdown for formatting (bold, links) — Chatty handles markdown, not HTML
4. Save changes and test the response again

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

1. Merge the two overlapping FAQs into one comprehensive entry
2. Make trigger keywords more specific and distinct for each FAQ
3. Remove duplicate or redundant content from the knowledge base
4. Use **Test AI** to verify the AI picks the right response after changes

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

Check your **Pre-transfer message** in Human Handover settings — if it references an email option, the AI may interpret the customer's "yes" as agreement to contact via email rather than a live transfer.

Revise the pre-transfer message to guide the AI toward live transfer. Contact support for help adjusting the wording.

---

<!-- CHUNK: ai-wrong-email-instead-of-transfer -->
```yaml
chunk_id: "ai-wrong__email-instead-of-transfer"
doc_id: "chatty-ai-wrong-responses"
title: "Configure AI to send contact email instead of live transfer"
category: "ai-wrong-responses"
tags: ["email instead of transfer", "contact via email", "human handover", "email handover", "no live agent"]
applies_when: "Merchant wants AI to send contact details via email instead of doing a live transfer"
```

## AI to Send Email Instead of Live Transfer

Go to **AI Assistant** → **Instructions** → **Assistant Skills** → **Human Handover** and configure the handover to send conversation details to your support email instead of assigning to a live agent.

Contact support if you need help configuring this.

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

This is **not currently a built-in feature**. A feature request for "Auto-assign AI conversations to a human team after a fixed time" has been noted by the product team for consideration on the roadmap.


---

# Billing & Refund Playbook

<!-- CHUNK: billing-refund-case-types -->
```yaml
chunk_id: "case__billing-refund-case-types"
doc_id: "cs-case-billing-refund"
title: "Billing & Refund — Case Classification and Who Handles What"
category: "cs-process"
subcategory: "billing"
tags: ["billing", "refund", "cancel", "charge", "inquiry", "chargeback", "dispute", "subscription"]
applies_when: "Merchant contacts CS about billing, charges, cancellation, or refund"
priority: "high"
```

## Case Types

| Case Type | Who Handles |
|-----------|------------|
| General inquiry (plan comparison, how to upgrade) | CS handles directly |
| Charge confusion (why charged, unexpected amount) | CS explains + checks charge history |
| Cancellation request | CS handles + escalates if refund needed |
| Refund request | CS collects info → escalates to CS Leader |
| Dispute / Chargeback | Immediately escalate to CS Leader |

**⚠️ CS is NOT authorized to approve any refund without CS Leader approval.**

---

<!-- CHUNK: billing-refund-simple-cancellation -->
```yaml
chunk_id: "case__billing-refund-simple-cancellation"
doc_id: "cs-case-billing-refund"
title: "Billing — Simple Cancellation / Refund Request Flow"
category: "cs-process"
subcategory: "billing"
tags: ["refund", "cancel", "downgrade", "trello", "billing-details", "CS leader", "free plan"]
applies_when: "Merchant wants to cancel or requests a refund with no service complaint (subscribed by mistake or just doesn't want to continue)"
priority: "high"
```

## Resolution Steps — Simple Cancellation

**Step 1:** Guide merchant to downgrade to Free plan. Verify they've downgraded.

**Step 2:** Collect billing info using `!billing-details`:
- Screenshot of invoice showing: app name, billing cycle, amount
- Whether the invoice has been paid
- Where to find: **Shopify Admin → Settings → Billing**

**Step 3:** Create Trello card for CS Leader using `!refund-process`:
- Assign to CS Leader
- Include all details and refund reason

---

<!-- CHUNK: billing-refund-dissatisfaction -->
```yaml
chunk_id: "case__billing-refund-dissatisfaction"
doc_id: "cs-case-billing-refund"
title: "Billing — Refund Due to Dissatisfaction or Bug"
category: "cs-process"
subcategory: "billing"
tags: ["refund", "dissatisfied", "bug", "complaint", "cancel", "high-risk", "escalate", "CS leader"]
applies_when: "Merchant requests a refund because they're unhappy with the app or experienced a bug"
priority: "high"
```

## Resolution Steps — Dissatisfaction or Bug-Related Refund

**Step 1:** Understand their expectations — what were they trying to achieve?

**Step 2:** Proactively offer support:
- If setup/feature misunderstanding → guide them again
- If bug → help resolve it
- If resolved and merchant is satisfied → encourage continued use, consult CS Leader about next-month discount

**Step 3:** If merchant still wants to cancel:
- Apologize for the experience
- Collect billing info (`!billing-details`)
- Guide to downgrade to Free plan

**Step 4:** Create Trello card for CS Leader.

**High-risk cases:** If merchant doesn't accept your explanation after clear communication → do NOT argue. Escalate to CS Leader/CSM immediately.

---

<!-- CHUNK: billing-refund-common-questions -->
```yaml
chunk_id: "case__billing-refund-common-questions"
doc_id: "cs-case-billing-refund"
title: "Billing — Common Merchant Questions About Charges"
category: "cs-process"
subcategory: "billing"
tags: ["billing", "charged", "payment failed", "two bills", "refund timeline", "uninstall", "billing date"]
applies_when: "Merchant asks common questions about why they were charged, when they'll be charged, or why payment failed"
priority: "medium"
```

## Common Billing Questions

**How long does a refund take?**
7–10 business days. Depends on Shopify's refund process and the bank. If > 10 days, advise merchant to check with Shopify and their bank directly.

**Merchant was charged after uninstalling/downgrading. Why?**
If they uninstalled/downgraded after the billing cycle started, they'll receive a full invoice for that cycle but be refunded for unused days.

**Merchant shows Free plan but was charged. What happened?**
They may have uninstalled (auto-cancels subscription), then reinstalled (defaults to Free), but the final bill from the previous cycle was still pending.

**Two bills in the same month?**
Ask for charge breakdown screenshot. If different billing periods → explain. If same period → check with CS Leader. May be caused by exceeding billing threshold before regular billing date.

**When will the merchant be charged?**
On their regular Shopify billing date, together with Shopify subscription and other app charges.

**Where to see charges?**
Shopify Admin → Settings → Billing → Bills.

**Why did payment fail?**
Common reasons: expired card, no payment method, insufficient funds, card doesn't support recurring USD payments.

---

<!-- CHUNK: billing-refund-shortcuts -->
```yaml
chunk_id: "case__billing-refund-shortcuts"
doc_id: "cs-case-billing-refund"
title: "Billing — Key Shortcuts Reference"
category: "cs-process"
subcategory: "billing"
tags: ["shortcut", "billing-details", "refund-process", "cancel-reason", "crisp shortcut"]
applies_when: "CS needs to use billing-related message shortcuts in Crisp"
priority: "low"
```

## Key Shortcuts

| Shortcut | Purpose |
|----------|---------|
| `!cancel-reason` | Confirm cancellation reason with merchant |
| `!billing-details` | Request billing info (invoice screenshot, payment status) |
| `!refund-process` | Set expectations with merchant about refund timeline |


---

# Chatbox & Widget Issues

<!-- CHUNK: widget-not-showing -->
```yaml
chunk_id: "widget__not-showing"
doc_id: "chatty-chatbox-widget"
title: "Chat widget not showing on the store"
category: "chatbox-widget"
tags: ["not showing", "widget missing", "chatbox not visible", "live chat button", "app embed"]
applies_when: "The live chat button or chatbox widget is not appearing on the merchant's store"
```

## Chat Widget Not Showing

**Cause 1: App Embed not enabled**
- Go to **Shopify Admin** → **Online Store** → **Themes** → **Customize** → **App Embeds**
- Ensure Chatty is toggled **ON**

**Cause 2: Live chat not enabled in app**
- Go to **Chatbox** → **General** → **Blocks** → ensure **Live chat** is enabled

**Cause 3: Theme conflict**
- If App Embed is enabled but widget still doesn't show → ask for the theme name and create a card for the TS team to investigate

---

<!-- CHUNK: widget-faq-page-not-showing -->
```yaml
chunk_id: "widget__faq-page-not-showing"
doc_id: "chatty-chatbox-widget"
title: "FAQ page not showing on the store"
category: "chatbox-widget"
tags: ["FAQ page", "not showing", "FAQ not visible", "navigation menu", "pages"]
applies_when: "The Chatty FAQ page is not visible on the merchant's store"
```

## FAQ Page Not Showing

1. **FAQ page not enabled** → Guide the merchant to **Settings** → **Pages** → Enable FAQ page
2. **FAQ page URL not added to menu** → Help the merchant get the FAQ page URL from the app and add it to their store's navigation menu

Reference: https://help.chatty.net/build-faqs/faqs-page

Tip: Suggest adding the FAQ URL to the main navigation menu for better visibility.

---

<!-- CHUNK: widget-faq-overwriting-templates -->
```yaml
chunk_id: "widget__faq-overwriting-templates"
doc_id: "chatty-chatbox-widget"
title: "Chatty FAQ page overwriting other page templates"
category: "chatbox-widget"
tags: ["FAQ template", "page template", "overwriting", "About Us", "Contact page", "template conflict"]
applies_when: "Other pages (About Us, Contact) look wrong or broken after installing Chatty FAQ page"
```

## FAQ Page Overwriting Other Page Templates

The Chatty app assigns FAQ content to the default page template, which can affect other pages.

1. In Shopify theme editor → **Theme Templates**, create a new template (e.g., `chatty-faq`)
2. Go to **Shopify Admin** → **Online Store** → **Pages**
3. Select the FAQ page created by Chatty ("Frequently Asked Questions")
4. Assign the new template to this FAQ page only
5. In the Chatty app, set the correct FAQ page URL
6. Verify other content pages are no longer affected

---

<!-- CHUNK: widget-position -->
```yaml
chunk_id: "widget__position"
doc_id: "chatty-chatbox-widget"
title: "Move or change the position of the chat widget"
category: "chatbox-widget"
tags: ["position", "move widget", "button position", "alignment", "reposition", "widget location"]
applies_when: "Merchant wants to move the chat button to a different position on the page"
```

## Changing Widget Position

Go to **Chatbox** → **Appearance** → **Set chatbox button** → **Select button alignment** for basic alignment changes.

For custom positioning, use **Chatbox** → **Advanced** → **Custom CSS**. If the merchant can't do it themselves, create a ticket for the TS team.

---

<!-- CHUNK: widget-remove-branding -->
```yaml
chunk_id: "widget__remove-branding"
doc_id: "chatty-chatbox-widget"
title: "Remove Chatty branding or Powered by Chatty watermark"
category: "chatbox-widget"
tags: ["branding", "remove branding", "powered by Chatty", "watermark", "white label"]
applies_when: "Merchant wants to remove the 'Powered by Chatty' branding from the widget"
```

## Removing Chatty Branding

1. Go to **DevZone** → **General** → Enable **Remove branding**
2. Notify the merchant to check
3. Communicate: "Normally, this option is only available for paid plans. However, we've helped remove the branding for you this time as a special support."

**Important:** Do NOT ask for a review immediately after removing branding — Shopify considers this "exchange for review." Help with an additional task first, then request a review based on the support experience.

---

<!-- CHUNK: widget-javascript-control -->
```yaml
chunk_id: "widget__javascript-control"
doc_id: "chatty-chatbox-widget"
title: "Open or close Chatty widget with JavaScript"
category: "chatbox-widget"
tags: ["JavaScript", "JS", "open widget", "close widget", "programmatically", "trigger chatbox", "code"]
applies_when: "Merchant wants to open or close the chatbox widget programmatically via JavaScript"
```

## JavaScript Widget Control

- **Toggle open/close:** `avadaFaqTrigger()`
- **Close widget:** `ChattyJS.closeWidget()`
- **Open widget (general):** `ChattyJS.openWidget()`
- **Open to specific page:**
  - `ChattyJS.openWidget('#chatty-home')` — Home
  - `ChattyJS.openWidget('#chatty-chat')` — Live Chat
  - `ChattyJS.openWidget('#chatty-tracking')` — Order Tracking
  - `ChattyJS.openWidget('#chatty-help')` — Help/FAQ

---

<!-- CHUNK: widget-faq-category-icons -->
```yaml
chunk_id: "widget__faq-category-icons"
doc_id: "chatty-chatbox-widget"
title: "Enable FAQ category icons"
category: "chatbox-widget"
tags: ["FAQ icons", "category icons", "view more icons", "locked", "DevZone"]
applies_when: "FAQ category icons feature is locked or unavailable for the merchant"
```

## Enabling FAQ Category Icons

For newly installed apps, category icons are locked by default.

1. Get the merchant's Store URL
2. Go to **DevZone** and enable the category icons feature
3. Notify the merchant to check

---

<!-- CHUNK: widget-not-clickable -->
```yaml
chunk_id: "widget__not-clickable"
doc_id: "chatty-chatbox-widget"
title: "Chat widget not clickable or unresponsive on first page load"
category: "chatbox-widget"
tags: ["not clickable", "unresponsive", "first load", "JavaScript conflict", "button not working"]
applies_when: "The chat widget button is not clickable or unresponsive, especially on first page load"
```

## Widget Not Clickable

This is usually a JavaScript conflict with another app or theme.

1. Disable other chat or popup apps temporarily to test
2. Check browser console for JS errors
3. Clear browser cache

If it only happens on first load, it may be a timing issue. Contact support with your store URL and browser details.

---

<!-- CHUNK: widget-slow-mobile -->
```yaml
chunk_id: "widget__slow-mobile"
doc_id: "chatty-chatbox-widget"
title: "Chat widget slow to load on mobile or iPad"
category: "chatbox-widget"
tags: ["slow", "mobile", "iPad", "loading", "performance", "slow chat"]
applies_when: "The chat widget is slow to load on mobile devices or iPads"
```

## Chat Slow to Load on Mobile

Common causes:
- **Theme performance or app conflicts** — try temporarily disabling other apps
- **Slow or unstable internet** on the device
- **Widget loading conflicts** on the page

Clear browser/app cache and check on a different network. If issue persists, share your store URL and device/browser details with support for investigation.

---

<!-- CHUNK: widget-avatar-upload-not-working -->
```yaml
chunk_id: "widget__avatar-upload"
doc_id: "chatty-chatbox-widget"
title: "AI logo or avatar upload not working"
category: "chatbox-widget"
tags: ["avatar", "logo upload", "image upload", "upload not working", "AI avatar"]
applies_when: "AI logo or avatar image upload is not working — nothing happens when clicking upload"
```

## Avatar Upload Not Working

1. Use a different browser (Chrome is recommended)
2. Clear browser cache and reload the page
3. Make sure the image is JPG or PNG and under 2MB
4. Try uploading in an Incognito/Private window

If issue still persists, share a screenshot and the image file with support for investigation.

---

<!-- CHUNK: widget-wrong-shape-mobile -->
```yaml
chunk_id: "widget__wrong-shape-mobile"
doc_id: "chatty-chatbox-widget"
title: "Chat widget button shows wrong shape or icon on mobile"
category: "chatbox-widget"
tags: ["wrong shape", "wrong icon", "mobile", "CSS conflict", "button appearance"]
applies_when: "The chat widget button shows the wrong shape or icon on mobile devices"
```

## Wrong Shape/Icon on Mobile

This is usually caused by custom CSS in the app settings conflicting on mobile.

Contact support with a **screenshot** — the team will review and correct the CSS.


---

# Demo Call Request Flow

<!-- CHUNK: demo-call-eligibility -->
```yaml
chunk_id: "case__demo-call-eligibility"
doc_id: "cs-case-demo-call-flow"
title: "Demo Call — Eligibility Criteria and Who Qualifies"
category: "cs-process"
subcategory: "demo-call"
tags: ["demo call", "eligibility", "high potential", "AI training", "paid plan", "consultant"]
applies_when: "Merchant asks for a demo call or product walkthrough call"
priority: "high"
```

## Overview

Demo calls for Chatty are only available to eligible merchants.

## Eligibility Criteria (must meet ONE)

- **High potential merchant** — large GMV, high-value customer
- **Needs AI training guidance** — wants help with AI scripts, auto-reply, or chat scenarios
- **Considering a paid plan** — actively evaluating or comparing Chatty paid plans

---

<!-- CHUNK: demo-call-flow -->
```yaml
chunk_id: "case__demo-call-flow"
doc_id: "cs-case-demo-call-flow"
title: "Demo Call — Step-by-Step Handling Flow"
category: "cs-process"
subcategory: "demo-call"
tags: ["demo call", "flow", "booking link", "eligible", "not eligible", "redirect", "live chat", "insists"]
applies_when: "CS is handling a demo call request and needs to decide how to respond"
priority: "high"
```

## Resolution Steps

### Step 1 — Check eligibility

Does the merchant meet any eligibility criteria? (High GMV, needs AI training guidance, or considering paid plan)

### Step 2 — If eligible → send demo booking link

Send: https://cal.com/drake-q-fonihl/chatty-consultant

The sales/consultant team handles scheduling and conducting the demo. After the call, CS continues supporting the merchant if they have follow-up questions.

### Step 3 — If NOT eligible → redirect to live chat

> Thanks for your request. For troubleshooting or app setup, our support team will assist you directly via live chat so you can get step-by-step help in real time.

### Step 4 — If merchant insists on a call despite not being eligible

Send the booking link: https://calendly.com/lyht-avada/30min

If merchant is frustrated and insists, send this link and notify Liz in **#cs-group-2** for follow-up.

---

<!-- CHUNK: demo-call-after-call -->
```yaml
chunk_id: "case__demo-call-after-call"
doc_id: "cs-case-demo-call-flow"
title: "Demo Call — What CS Does After the Call Completes"
category: "cs-process"
subcategory: "demo-call"
tags: ["after demo", "post-call", "follow up", "sales team", "CS role"]
applies_when: "A demo call has been completed and CS needs to know what to do next"
priority: "low"
```

## After the Demo Call

- The **sales team** handles the call itself (scheduling, conducting the demo).
- **CS continues** to support the merchant if they have follow-up questions about usage, setup, or optimization.

No special action needed from CS unless the merchant reaches out again.


---

# Email Channel Issues

<!-- CHUNK: email-outlook-hotmail -->
```yaml
chunk_id: "email__outlook-hotmail"
doc_id: "chatty-email-channel"
title: "Outlook/Hotmail email forwarding not working with Chatty"
category: "email-channel"
tags: ["Outlook", "Hotmail", "email forwarding", "not working", "Microsoft", "Cloudflare"]
applies_when: "Emails from Hotmail or Outlook are not being forwarded to Chatty inbox"
```

## Outlook/Hotmail Forwarding Not Working

This is a known compatibility issue between Cloudflare and Microsoft's mail system.

**Workarounds:**
1. **Use an intermediate mailbox** — set up a Gmail to receive from Outlook/Hotmail, then forward to Chatty
2. **Switch email hosting** — consider Google Workspace or Zoho Mail, then forward to Chatty
3. **Enable alternative notifications** — turn on email notifications via Gmail or install the Chatty mobile app

Guide the merchant to test after setting up the workaround.

---

<!-- CHUNK: email-forwarding-verification-fails -->
```yaml
chunk_id: "email__forwarding-verification-fails"
doc_id: "chatty-email-channel"
title: "Email forwarding verification fails"
category: "email-channel"
tags: ["verification", "email forwarding", "verification fails", "not verified", "forwarding address"]
applies_when: "Merchant set up email forwarding but verification is failing or not completing"
```

## Email Forwarding Verification Fails

Common causes: incorrect forwarding address, email provider blocking automatic forwarding, or verification email going to spam.

1. Verify the forwarding address is entered correctly
2. Ask the merchant to check spam/junk folder for the verification email
3. If using Outlook/Hotmail, note the Cloudflare compatibility issue and suggest alternative providers
4. If issue persists, check if the email sender configuration is blocking forwarding

---

<!-- CHUNK: email-spf-verification -->
```yaml
chunk_id: "email__spf-verification"
doc_id: "chatty-email-channel"
title: "Email sender verification failing — SPF records"
category: "email-channel"
tags: ["SPF", "email sender", "verification", "DNS", "SPF record", "sender verification"]
applies_when: "Email sender verification is failing, possibly due to SPF record configuration"
```

## Email Sender Verification Failing (SPF)

Check if the email provider requires SPF record configuration.

1. Verify the merchant's email provider settings
2. If SPF records need updating, guide the merchant to add the SPF record to their DNS settings — refer to their email provider's documentation for exact values
3. Test again after DNS changes propagate (may take up to 48 hours)

---

<!-- CHUNK: email-verification-not-received -->
```yaml
chunk_id: "email__verification-not-received"
doc_id: "chatty-email-channel"
title: "Verification email for email channel setup never arrived"
category: "email-channel"
tags: ["verification email", "not received", "email setup", "no email", "missing verification"]
applies_when: "Merchant did not receive the verification email when setting up email channel"
```

## Verification Email Never Arrived

1. Ask the merchant to check spam/junk folders
2. Some corporate email providers block automated verification emails
3. Verify the email was entered correctly in settings
4. If none of the above, try resending the verification email or use an alternative email address

---

<!-- CHUNK: email-going-to-spam -->
```yaml
chunk_id: "email__going-to-spam"
doc_id: "chatty-email-channel"
title: "Chatty emails going to customers' spam"
category: "email-channel"
tags: ["spam", "junk", "email spam", "deliverability", "DKIM", "DMARC", "SPF"]
applies_when: "Chatty emails are landing in customers' spam or junk folders"
```

## Chatty Emails Going to Spam

This is typically caused by missing email authentication records.

1. Guide the merchant to add **SPF records** to their DNS settings
2. Verify **DKIM** and **DMARC** records are properly configured
3. Recommend using a **custom sender domain** instead of the default `noreply@chattyemail.com`
4. If the merchant uses a custom domain, verify the domain in Chatty settings

---

<!-- CHUNK: email-spf-setup -->
```yaml
chunk_id: "email__spf-setup"
doc_id: "chatty-email-channel"
title: "How to add SPF records for Chatty email"
category: "email-channel"
tags: ["SPF records", "DNS", "email authentication", "spam prevention", "configure SPF"]
applies_when: "Merchant needs to configure SPF records for Chatty email delivery"
```

## Adding SPF Records for Chatty Email

Guide the merchant to add SPF records in their DNS provider settings. This ensures emails sent through Chatty are authenticated and less likely to be flagged as spam.

The specific SPF record values depend on the merchant's email hosting provider — refer to their provider's documentation for exact configuration steps.

---

<!-- CHUNK: email-multiple-addresses -->
```yaml
chunk_id: "email__multiple-addresses"
doc_id: "chatty-email-channel"
title: "Using multiple email addresses with Chatty"
category: "email-channel"
tags: ["multiple emails", "alias email", "additional email", "multiple addresses", "email alias"]
applies_when: "Merchant wants to use multiple email addresses or alias emails with Chatty"
```

## Multiple Email Addresses

Chatty supports **one email per store** via forwarding. For additional email addresses, set up email forwarding from alias addresses to the connected Chatty email.

Contact support if you have specific needs around multiple email addresses or alias setups.

---

<!-- CHUNK: email-contact-button-wrong-client -->
```yaml
chunk_id: "email__contact-button-wrong-client"
doc_id: "chatty-email-channel"
title: "Email button in chatbox opens wrong email client"
category: "email-channel"
tags: ["email button", "contact us", "wrong email client", "email icon", "chatbox email button"]
applies_when: "Clicking the email icon in the Contact Us widget opens the wrong email client"
```

## Email Button Opens Wrong Client

The behavior depends on the merchant's chatbox configuration and the customer's device default email client settings.

Verify the email address is correctly set in the **Contact Us** block settings.

---

<!-- CHUNK: email-fail-to-deliver -->
```yaml
chunk_id: "email__fail-to-deliver"
doc_id: "chatty-email-channel"
title: "Merchant receiving Fail to Deliver error emails"
category: "email-channel"
tags: ["fail to deliver", "delivery failure", "bounce", "email error", "delivery error"]
applies_when: "Merchant is receiving delivery failure notification emails"
```

## Fail to Deliver Errors

These errors typically occur when the recipient email is invalid or the email provider rejects the message.

Verify the recipient email addresses and check email forwarding configuration for any issues.

---

<!-- CHUNK: email-change-admin -->
```yaml
chunk_id: "email__change-admin"
doc_id: "chatty-email-channel"
title: "Change admin email for Chatty account"
category: "email-channel"
tags: ["admin email", "change email", "store owner", "account email", "transfer admin"]
applies_when: "Merchant wants to change the admin email address for their Chatty account"
```

## Changing Admin Email

The admin email is tied to the Shopify store owner account.

1. Go to Chatty app settings → check **Team settings** for the current admin email
2. If the merchant needs to change the primary admin, they may need to update their Shopify store owner email first, then re-access Chatty

---

<!-- CHUNK: email-reply-to-field -->
```yaml
chunk_id: "email__reply-to-field"
doc_id: "chatty-email-channel"
title: "Forwarding email showing in Reply-To field"
category: "email-channel"
tags: ["reply-to", "forwarding email", "wrong sender", "reply-to header", "email sender"]
applies_when: "The forwarding email address is showing in the Reply-To field instead of the store's actual support email"
```

## Forwarding Email Showing in Reply-To

1. Go to **Chatty** → **Channels** → **Email**
2. Check the **Email sender** field — make sure it's set to your actual store support email, not the Chatty forwarding address
3. Save and send a test reply to yourself to confirm the correct email appears in Reply-To

---

<!-- CHUNK: email-ai-replies -->
```yaml
chunk_id: "email__ai-replies"
doc_id: "chatty-email-channel"
title: "Does AI reply to email conversations reach the customer"
category: "email-channel"
tags: ["AI email reply", "email reply", "customer receives", "noreply", "custom sender"]
applies_when: "Merchant asks whether AI or agent replies sent via Chatty are delivered to the customer's email"
```

## AI/Agent Email Replies Delivered to Customer

Yes — replies sent through Chatty (by AI or human agents) are delivered to the customer's email. The default sender address is `noreply@chattyemail.com` unless you have configured a custom sender domain.

---

<!-- CHUNK: email-klaviyo-reply-to -->
```yaml
chunk_id: "email__klaviyo-reply-to"
doc_id: "chatty-email-channel"
title: "Use Klaviyo to send outreach emails and have Chatty handle replies"
category: "email-channel"
tags: ["Klaviyo", "reply-to", "outreach", "email campaign", "Chatty inbox", "Klaviyo integration"]
applies_when: "Merchant wants to send Klaviyo campaign emails and have replies appear in Chatty inbox"
```

## Klaviyo Outreach + Chatty Reply Handling

Set up your Klaviyo campaign with a **Reply-To** address that is connected to a Chatty email channel. When leads reply to the email, their response will appear in Chatty's inbox as a new conversation, where AI or your team can take over.


---

# Notification Issues

<!-- CHUNK: notification-desktop-not-working -->
```yaml
chunk_id: "notification__desktop-not-working"
doc_id: "chatty-notification-issues"
title: "Desktop push notifications not working"
category: "notification-issues"
tags: ["desktop notifications", "push notifications", "not working", "no notifications", "browser notifications"]
applies_when: "Merchant is not receiving desktop push notifications when new messages arrive"
```

## Desktop Push Notifications Not Working

Check in order:

**Step 1: Verify app notification settings**
- Ensure push notification is enabled for new/unread messages in **App Settings**

**Step 2: Verify browser and device settings**
- Browser must have notifications allowed for `app.meetchatty.com`
- System settings must allow notifications (not in Silent/Do Not Disturb mode)
- Device must not be in presentation mode or screen recording mode

**Step 3: If settings are correct but still no notifications**
- Clear browser cache and cookies
- Restart the computer
- Open browser DevTools (F12) → **Application** → **Service Workers** → Update the `firebase-messaging-sw.js` service worker

**Step 4: If still not resolved**
- Escalate to dev team with detailed info

**Meanwhile:** Recommend email notifications or installing the Chatty mobile app as alternatives.

---

<!-- CHUNK: notification-mobile-not-working -->
```yaml
chunk_id: "notification__mobile-not-working"
doc_id: "chatty-notification-issues"
title: "Chatty mobile app push notifications not working"
category: "notification-issues"
tags: ["mobile notifications", "push notifications", "mobile app", "phone notifications", "app notifications"]
applies_when: "Merchant is not receiving push notifications on the Chatty mobile app"
```

## Mobile App Notifications Not Working

1. Verify the mobile app is installed and the merchant is logged in
2. Check device notification settings — Chatty must be **allowed** to send notifications
3. Ensure the phone is not in **Do Not Disturb** mode
4. Try uninstalling and reinstalling the mobile app
5. If issue persists, collect device model, OS version, and app version → escalate to dev team

---

<!-- CHUNK: notification-email-not-working -->
```yaml
chunk_id: "notification__email-not-working"
doc_id: "chatty-notification-issues"
title: "Email notifications for new chat messages not being sent"
category: "notification-issues"
tags: ["email notifications", "email alerts", "not receiving email", "new message alert", "notification email"]
applies_when: "Merchant is not receiving email notifications when new chat messages arrive"
```

## Email Notifications Not Being Sent

1. Verify email notifications are enabled in Chatty's notification settings
2. Check the merchant's email **spam/junk folder**
3. Verify the notification email address is correct
4. If using a corporate email, the organization may be blocking automated emails

---

<!-- CHUNK: notification-not-in-device-settings -->
```yaml
chunk_id: "notification__not-in-device-settings"
doc_id: "chatty-notification-issues"
title: "Chatty not showing in device notification settings"
category: "notification-issues"
tags: ["notification settings", "device settings", "phone settings", "can't find Chatty", "notification permission"]
applies_when: "Merchant can't find Chatty in their device's notification settings to enable it"
```

## Chatty Not in Device Notification Settings

This happens if:
1. The app was never opened after installation (permission was never requested)
2. Notification permission was denied on first prompt and needs to be manually re-enabled

**Solution:** Guide the merchant to manually find and enable Chatty notifications in their device settings, or clear app data and reopen to trigger the permission prompt again.

---

<!-- CHUNK: notification-permission-popup -->
```yaml
chunk_id: "notification__permission-popup"
doc_id: "chatty-notification-issues"
title: "Trigger the notification permission popup again on mobile"
category: "notification-issues"
tags: ["notification popup", "permission prompt", "dismissed popup", "notification permission", "re-enable"]
applies_when: "The notification permission popup was dismissed or denied and merchant wants to enable notifications"
```

## Triggering Notification Permission Popup Again

If the notification permission popup was dismissed or denied:

1. Go to **device Settings** → **Apps** → **Chatty** → **Notifications** → Enable notifications
2. Alternatively, uninstall and reinstall the app to trigger the permission prompt again

---

<!-- CHUNK: notification-app-pixel-disconnected -->
```yaml
chunk_id: "notification__app-pixel-disconnected"
doc_id: "chatty-notification-issues"
title: "Chatty app pixel disconnected in Shopify Customer Events"
category: "notification-issues"
tags: ["app pixel", "Customer Events", "disconnected", "Shopify pixel", "analytics pixel"]
applies_when: "The Chatty app pixel shows as disconnected in Shopify Customer Events"
```

## App Pixel Disconnected in Customer Events

The App Pixel may become disconnected due to theme changes or Shopify updates.

1. Go to **Shopify Admin** → **Settings** → **Customer Events**
2. Find Chatty in the list and **reconnect/re-enable** it
3. Verify the connection is active
4. If the merchant cannot reconnect, collect details and escalate to TS team


---

# Translation & Multi-language Issues

<!-- CHUNK: translation-faq-not-switching -->
```yaml
chunk_id: "case__translation-faq-not-switching"
doc_id: "cs-case-translation-issues"
title: "FAQ page translation not working — content doesn't change when switching language"
category: "troubleshooting"
subcategory: "translation"
tags: ["translation", "FAQ not translating", "language switch", "Translate & Adapt", "third-party translation", "meta content", "T Lab"]
applies_when: "Merchant reports FAQ page content doesn't change when customer switches language on the store"
priority: "high"
```

## Symptom

FAQ page content doesn't change when the customer switches language on the store.

## Cause

Commonly caused by a third-party translation app (e.g., Translate & Adapt, T Lab) overwriting Chatty's FAQ meta content.

## Resolution

1. Ask the merchant if they use any third-party translation app.
2. If using Translate & Adapt → check the meta content of the affected language for overridden Chatty rows.
3. Remove the overriding content from the third-party app.
4. If issue persists after removing overrides → create a tech support card for deeper investigation.
5. If unclear → request app permissions to investigate or escalate to TS.

---

<!-- CHUNK: translation-outdated-status -->
```yaml
chunk_id: "case__translation-outdated-status"
doc_id: "cs-case-translation-issues"
title: "Translation status shows 'Outdated' for a language in Chatty"
category: "troubleshooting"
subcategory: "translation"
tags: ["translation", "outdated", "translation status", "auto-translate", "FAQ translation", "update"]
applies_when: "Merchant sees 'Outdated' status for a language in Chatty's Translation settings"
priority: "medium"
```

## Symptom

A language shows as "Outdated" in the Translations section.

## Cause

FAQ content was updated after the last translation, or the FAQ was never translated for that language.

## Resolution

1. Go to **Settings → Translation** → find the affected language.
2. **Paid plan merchants:** Click "Auto-translate" to automatically translate the FAQ.
3. **Free plan merchants:** Must manually translate the FAQ content.
4. After translating, save and verify the status changes from "Outdated" to "Updated."


---

# WhatsApp & Messenger Issues

<!-- CHUNK: whatsapp-connection-requirements -->
```yaml
chunk_id: "whatsapp__connection-requirements"
doc_id: "chatty-whatsapp-messenger"
title: "Requirements to connect WhatsApp to Chatty"
category: "whatsapp-messenger"
tags: ["WhatsApp", "connect WhatsApp", "requirements", "Meta Business Manager", "setup", "checklist"]
applies_when: "Merchant asks what they need to connect WhatsApp to Chatty, or is setting up WhatsApp for the first time"
```

## WhatsApp Connection Requirements

The merchant needs all of the following:

1. **Meta Business Manager** — with **Business Admin** role (Employee role is NOT sufficient). Check at: business.facebook.com/settings/people
2. **Valid WhatsApp phone number** — not currently registered on WhatsApp personal app, OR an existing WhatsApp Business number migrated to Cloud API. OTP verification must be via SMS or phone call (not WhatsApp app)
3. **Valid business information** — business name, type, legal address, website domain. Meta may require Business Verification for full features
4. **Correct permissions during OAuth** — must select Business Manager, WhatsApp Business Account, and phone number; grant "AVADA group company limited" permission
5. **Correct Facebook login** — must be added to Business Manager with proper permissions; browser must not block popups or third-party cookies
6. **No other WhatsApp API provider** — if the number is connected to another provider (Twilio, 360dialog, etc.), it must be released/migrated first

---

<!-- CHUNK: whatsapp-not-working -->
```yaml
chunk_id: "whatsapp__not-working"
doc_id: "chatty-whatsapp-messenger"
title: "WhatsApp connected but not working"
category: "whatsapp-messenger"
tags: ["WhatsApp not working", "connection issues", "WhatsApp broken", "not receiving messages"]
applies_when: "Merchant connected WhatsApp but it's not working or messages are not coming through"
```

## WhatsApp Not Working After Connection

Common causes:
1. **Insufficient permissions** — connecting user must be a Business Admin (not Employee) in Meta Business Manager
2. **Phone number already in use** — active on WhatsApp personal app or connected to another API provider
3. **Business verification pending** — Meta requires verification for full features
4. **Browser blocking popups** — OAuth popup may be blocked; try a different browser or disable popup blockers

Verify each item on the connection requirements checklist before escalating.

---

<!-- CHUNK: whatsapp-messenger-messages-missing -->
```yaml
chunk_id: "whatsapp__messenger-messages-missing"
doc_id: "chatty-whatsapp-messenger"
title: "Facebook Messenger messages not showing in Chatty inbox"
category: "whatsapp-messenger"
tags: ["Messenger", "Facebook", "messages not showing", "inbox", "not syncing", "Messenger integration"]
applies_when: "Facebook Messenger messages are not appearing in Chatty inbox"
```

## Messenger Messages Not Showing in Inbox

1. **Integration incomplete** — ensure all steps are completed in the Channels section
2. **Insufficient page permissions** — connecting user must have "Manage and access Page messages" permission. Check **Page Settings** → **Page Roles & Permissions**
3. **Permission deselection during setup** — if the merchant deselected items during Facebook OAuth, permissions may be incomplete
4. **Old messages** — only messages sent **after** Chatty is connected will sync. Old messages must be handled directly in Facebook Messenger

---

<!-- CHUNK: whatsapp-instagram-messages-missing -->
```yaml
chunk_id: "whatsapp__instagram-messages-missing"
doc_id: "chatty-whatsapp-messenger"
title: "Instagram messages not appearing in Chatty inbox"
category: "whatsapp-messenger"
tags: ["Instagram", "Instagram DM", "messages not showing", "not syncing", "Instagram inbox"]
applies_when: "Instagram messages are not appearing in the Chatty inbox"
```

## Instagram Messages Not Showing

1. Verify Instagram channel is properly connected in **Chatty** → **Channels**
2. The connecting user must have admin access to the Facebook page
3. All permissions must have been granted during OAuth
4. Only new messages (sent after connection) will appear in Chatty

If all settings are correct but messages still don't sync, collect details and escalate to the TS team.

---

<!-- CHUNK: whatsapp-pending-status -->
```yaml
chunk_id: "whatsapp__pending-status"
doc_id: "chatty-whatsapp-messenger"
title: "WhatsApp number showing as Pending after connecting"
category: "whatsapp-messenger"
tags: ["pending", "WhatsApp pending", "verification pending", "Meta verification", "waiting"]
applies_when: "WhatsApp number is showing as Pending status after connecting to Chatty"
```

## WhatsApp Number Showing as Pending

Pending status means Meta verification is still in progress — typically takes 24–48 hours.

Make sure:
1. WhatsApp Business account is fully verified
2. The phone number is not already registered with another WhatsApp Business API provider
3. Two-factor authentication (2FA) for the phone number is enabled

If still Pending beyond 48 hours, contact support for assistance.

---

<!-- CHUNK: whatsapp-switch-bsp -->
```yaml
chunk_id: "whatsapp__switch-bsp"
doc_id: "chatty-whatsapp-messenger"
title: "Switch WhatsApp number from another provider to Chatty"
category: "whatsapp-messenger"
tags: ["switch BSP", "migrate WhatsApp", "another provider", "Twilio", "360dialog", "migrate number"]
applies_when: "Merchant's WhatsApp number is connected to another provider and they want to switch to Chatty"
```

## Switching WhatsApp BSP to Chatty

Meta policy allows a WhatsApp Business API number to be managed by **only one BSP at a time**. To switch to Chatty:
- Migrate the number (disconnect from current BSP and reconnect via Meta Business Manager), OR
- Create a new WhatsApp Business Account and associate the same phone number

Contact support for guidance on the migration process.

---

<!-- CHUNK: whatsapp-without-widget -->
```yaml
chunk_id: "whatsapp__without-widget"
doc_id: "chatty-whatsapp-messenger"
title: "Use Chatty AI to answer WhatsApp without showing widget on website"
category: "whatsapp-messenger"
tags: ["WhatsApp AI", "AI for WhatsApp", "without widget", "no widget", "WhatsApp only"]
applies_when: "Merchant wants AI to respond to WhatsApp without showing the chatbox widget on their website"
```

## AI for WhatsApp Without Website Widget

Yes — once WhatsApp is connected, go to **AI Assistant** → **Settings** and enable AI for the **WhatsApp channel**. The AI will respond to WhatsApp messages using the same training data as the website chatbox.

Access WhatsApp conversations via **Inbox** → **WhatsApp** tab.

---

<!-- CHUNK: whatsapp-outbound -->
```yaml
chunk_id: "whatsapp__outbound"
doc_id: "chatty-whatsapp-messenger"
title: "Initiating outbound WhatsApp messages from Chatty"
category: "whatsapp-messenger"
tags: ["outbound", "send first", "initiate message", "proactive WhatsApp", "first message"]
applies_when: "Merchant wants to send the first WhatsApp message to customers (outbound)"
```

## Outbound WhatsApp Messages

No — Chatty currently **only supports responding** within existing WhatsApp conversations. You cannot initiate new outbound WhatsApp messages to contacts who haven't messaged you first.

---

<!-- CHUNK: whatsapp-instagram-story-errors -->
```yaml
chunk_id: "whatsapp__instagram-story-errors"
doc_id: "chatty-whatsapp-messenger"
title: "Instagram story replies showing errors in Chatty inbox"
category: "whatsapp-messenger"
tags: ["Instagram story", "story reply", "error", "unsupported", "story error"]
applies_when: "Instagram story replies are showing errors in the Chatty inbox"
```

## Instagram Story Reply Errors

Chatty currently supports Instagram **text and image messages only**. Unsupported message types include: story replies, reel shares, voice messages/audio, stickers, post shares, and vanish mode messages.

The team is working on expanding support for these formats.

---

<!-- CHUNK: whatsapp-direct-reply-sync -->
```yaml
chunk_id: "whatsapp__direct-reply-sync"
doc_id: "chatty-whatsapp-messenger"
title: "Messages sent directly in Instagram/Facebook not syncing to Chatty"
category: "whatsapp-messenger"
tags: ["direct reply", "not syncing", "outside Chatty", "Meta platform", "sync", "Facebook reply"]
applies_when: "Replies made directly in Instagram or Facebook Messenger are not appearing in Chatty inbox"
```

## Direct Replies Not Syncing to Chatty

Replies made directly in the Meta platform (not via Chatty) may not sync back to the Chatty inbox. This is a **known limitation** — a feature request has been filed to improve sync coverage for replies made outside of Chatty.

---

<!-- CHUNK: whatsapp-ai-instagram -->
```yaml
chunk_id: "whatsapp__ai-instagram"
doc_id: "chatty-whatsapp-messenger"
title: "AI not responding to Instagram messages"
category: "whatsapp-messenger"
tags: ["AI Instagram", "Instagram AI", "AI not responding", "Instagram channel", "AI toggle"]
applies_when: "AI is not responding to Instagram DM messages"
```

## AI Not Responding to Instagram

Go to **AI Assistant** → **Settings** and check if AI is enabled for the **Instagram channel** — there is a per-channel toggle.

Enable it and the AI will start responding automatically. Previously unhandled messages will continue to be assigned to agents by default until the toggle is on.


---

---
category: Common Issues
topic: Access & Login Issues
source: notion/Chatty FAQs
---

Q: The merchant sees "Account not activated" when logging into app.meetchatty.com.
Q: Merchant can't log in — account not activated error.
A: Common causes:

1. The merchant has never opened Chatty from Shopify Admin after installing — no internal account was created.
2. The app was uninstalled and reinstalled but the old account wasn't reactivated.
3. The merchant is trying to log in directly via the external link instead of through Shopify Admin.
4. Browser has cached old data.

**Solution:**
- Guide the merchant to open Chatty from Shopify Admin first (Apps > Chatty) to activate the account.
- After activation, they can use app.meetchatty.com.
- If the issue persists, suggest clearing browser cache and trying again.

---

Q: The merchant or team member gets "Incorrect email or password" on app.meetchatty.com.
Q: Agent can't log in to the Chatty web app.
A: This depends on the sign-up method used:

1. **If they used "Create account" (custom password):**
   - Log in with email + the password they created during sign-up.
   - If forgotten, click "Forgot password" to reset.

2. **If they used "Sign up with Google":**
   - Click "Sign in with Google" and use the same Gmail account they originally signed up with.

Ask the merchant/agent which method they used to sign up, then guide accordingly.

---

Q: A development store is blocked from using Chatty.
Q: The app shows "Not Found" on a development store.
A: Chatty automatically blocks access from development stores with emails from blacklisted domains (competitors and known testing accounts).

**Blacklisted domains include:** @tidio.com, @intercom.com, @firegroup.io, @flowio.app, @beae.com, @fireapps.vn, @channelwill.cn, @bsscommerce.com, @amasty.com, @secomus.com, @appsfinal.com, @omegatheme.com, @loox.io, @samita.io.

If the merchant's email belongs to a blacklisted domain, CS does not need to continue support — resolve the conversation.

---

Q: A Chinese merchant can't access Chatty — the screen is blank/white.
Q: Merchant from China sees white screen and console errors.
A: Chatty is hosted on Google Cloud, which is commonly blocked by China's Great Firewall.

**Solution:**
1. Confirm the merchant is located in China.
2. If not using a VPN: guide them to use a reputable VPN that works in China.
3. If already using a VPN: suggest trying a different VPN or network.
4. Send the standalone link: `https://app.meetchatty.com` and instruct them to try with VPN enabled.
5. If other apps work fine, explain Chatty's Google Cloud hosting limitation.
6. Escalate to dev only if VPN + standalone link still doesn't work.

---

Q: How does a merchant manage multiple stores from one account?
Q: Can I use one Chatty account for multiple Shopify stores?
A: Each Shopify store requires its own Chatty installation. The merchant can access each store's Chatty separately through their Shopify Admin.

For team members who work across multiple stores, they can be invited as team members on each store's Chatty installation and switch between them.

---

# FAQ Categories

<!-- CHUNK: add-category-overview -->
```yaml
chunk_id: "faq__add-category-overview"
doc_id: "chatty-add-category"
title: "How to add, edit, and manage FAQ categories in Chatty"
category: "faq"
subcategory: "build-faqs"
tags: ["faq category", "add category", "organize faqs", "faq groups", "category management", "featured category"]
applies_when: "When a merchant asks how to create, edit, delete, or organize FAQ categories"
priority: "medium"
```

## FAQ Categories Overview

Categories help you group related FAQ questions together. Chatty includes two default categories with sample questions: "Order & Shipping" and "Exchange & Return". You can edit these or create your own.

## How to Add a New Category

1. Go to **FAQs**
2. Click **Add new** → **Add category**
3. Enter category information:
   - **Category name**: Title displayed on the FAQ page
   - **Icon**: Choose a relevant icon (click **View more** for additional options, or upload your own)
   - **Position**: Where the category appears on the FAQ page (top to bottom)
   - **Status**: Published (visible) or Draft (hidden)
   - **Feature category**: If enabled, the category shows on the first page of the chatbox. If you feature 2 categories, the one with the higher position appears first.
4. Click **Save**

## How to Manage Categories

- **Edit a category**: Hover over it and click the edit icon
- **Delete a category**: Hover over it and click the delete icon
- **Reorder categories**: Drag and drop to a new position
- **Feature/unfeature**: Star or unstar the category


---

# Adding and Managing FAQ Questions

<!-- CHUNK: add-questions-overview -->
```yaml
chunk_id: "faq__add-questions-overview"
doc_id: "chatty-add-questions"
title: "How to add, edit, and manage FAQ questions in Chatty"
category: "faq"
subcategory: "build-faqs"
tags: ["add faq", "create faq", "faq questions", "edit faq", "delete faq", "reorder faq", "featured question"]
applies_when: "When a merchant asks how to add or manage individual FAQ questions"
priority: "medium"
```

## How to Add a New Question

After creating a category, you can add questions to it.

1. Go to **FAQs**
2. Click **Add new** → **Add FAQ**
3. Enter the question and answer
4. Configure settings:
   - **Status**: Published or Draft
   - **Category**: Select which category this question belongs to (required)
   - **Featured question**: If enabled, the question shows on the first page of the chatbox
5. Click **Save**

## How to Manage Questions

- **Edit a question**: Hover over it and click the edit icon
- **Delete a question**: Hover over it and click the delete icon
- **Reorder questions**: Drag and drop within a category
- **Feature/unfeature**: Star or unstar the question

---

<!-- CHUNK: add-questions-import-export -->
```yaml
chunk_id: "faq__add-questions-import-export"
doc_id: "chatty-add-questions"
title: "Import and export FAQ questions in bulk using CSV"
category: "faq"
subcategory: "build-faqs"
tags: ["import faq", "export faq", "bulk faq", "csv import", "faq csv", "bulk upload"]
applies_when: "When a merchant asks how to import or export FAQs in bulk"
priority: "medium"
```

## Import FAQs in Bulk

You can import many questions at once using a CSV file.

**Get the sample file:**
Go to **FAQs** → **More actions** → **Import FAQs** → Download the sample CSV

**Fill in the CSV file:**
The file has 5 required fields (keep headers):
- Question
- Answer
- Category (name of the category the question belongs to)
- Published question: TRUE = published, FALSE = unpublished
- Featured question: TRUE = featured, FALSE = not featured

This CSV file is for importing FAQ questions only (not AI training data) — max file size: 1MB.

**Upload the file:**
Click **Import FAQs** → Drop your CSV file → Choose options:
- Overwrite FAQs that have the same questions
- Publish all new categories

## Export FAQs

Go to **FAQs** → **More actions** → **Export FAQs** → Select which FAQs to export → Click **Export**

The export file contains 7 fields: Question, Answer, Category, Published question, Featured question, Published category, Featured category.


---

# AI Compliance (GDPR and EU AI Act)

<!-- CHUNK: ai-compliance-roles -->
```yaml
chunk_id: "faq__ai-compliance-roles"
doc_id: "chatty-ai-compliance"
title: "GDPR compliance and merchant vs. Chatty data responsibilities"
category: "faq"
subcategory: "privacy-policy"
tags: ["GDPR", "compliance", "data controller", "data processor", "privacy", "EU AI Act", "data protection"]
applies_when: "When a merchant asks about GDPR compliance, EU AI Act, or their legal responsibilities when using Chatty's AI"
priority: "high"
```

## Your Role vs. Chatty's Role

Last updated: February 2025

**As a Shopify store owner (data controller), you:**
- Decide how customer data is used
- Set purposes for data collection
- Ensure proper customer notification
- Maintain an updated privacy policy

**Chatty (data processor):**
- Processes data according to your instructions
- Implements security measures
- Handles data per GDPR requirements
- Provides necessary compliance tools

## GDPR Compliance

The GDPR (General Data Protection Regulation) is Europe's primary data protection law. For Chatty users, this means:
- Only necessary customer data is collected
- Data usage is transparent
- User privacy rights are protected
- Data handling is secure

## EU AI Act Compliance

The AI Act is EU legislation governing AI systems like chatbots. Chatty's AI is designed to comply with:
- Clear disclosure of AI interaction
- Prevention of discriminatory decisions
- Transparency in AI operations
- Regular risk assessments

---

<!-- CHUNK: ai-compliance-data-security -->
```yaml
chunk_id: "faq__ai-compliance-data-security"
doc_id: "chatty-ai-compliance"
title: "What data Chatty collects and how it is secured"
category: "faq"
subcategory: "privacy-policy"
tags: ["data collection", "data security", "encryption", "security audit", "what data is stored", "data retention", "GDPR"]
applies_when: "When a merchant asks what data Chatty collects, how it is stored, or how long data is retained"
priority: "high"
```

## How Chatty Ensures Compliance

**Data collection:**
- Only essential information is collected
- No unnecessary personal data storage
- Clear purpose for all data points
- Transparent notification of AI usage

**Security measures:**
- End-to-end encryption
- Regular security audits
- Secure data storage
- Limited staff access with role-based permissions

## What Data Is Collected and Why

**For merchants:**
- Chat messages and conversations: stored to provide support history and improve AI
- Store information: basic Shopify data to enable app functionality
- Configuration settings: your chatbot preferences
- Anonymous usage data: to improve app performance

**For end users (store customers):**
- Chat messages sent through the widget
- Order information: only when provided for order tracking
- No emails, phone numbers, or personal info unless explicitly provided

## Common Compliance Questions

- **What data does Chatty collect?** Only chat messages and essential order information when provided. No additional personal data is collected unless explicitly needed for customer service.
- **How long is data stored?** Default retention is 90 days. You can adjust this in your settings.
- **How do I handle customer data deletion requests?** Chatty provides tools to export or delete customer data on request. Contact support for assistance.
- **Is Chatty's AI Act compliant?** Yes — Chatty's AI features are designed for transparency, fairness, and regular risk assessments.

> Note: Add a privacy disclaimer to your site before activating the chatbot to inform customers about AI usage.


---

---
category: Common Issues
topic: AI Product Sync Issues
source: notion/Chatty FAQs
---

Q: The AI product sync is stuck and not making progress.
Q: Product synchronization for AI data source is hanging.
A: When the product sync gets stuck:

**Step 1: Confirm the sync start time**
- Go to AI Assistant > Data Source and check the timestamp of the most recent sync.

**Step 2: If sync has been running too long with no progress**
- Go to DevZone > Testing and click "Start Auto Resync" to reset and restart the sync process.
- Warning: this restarts the sync from scratch.

**Step 3: Monitor and confirm**
- After resync, update the merchant. When products are fully displayed in the data source, notify them.
- Advise the merchant not to make changes in the app (editing product tags, etc.) during resync to avoid data conflicts.

---

Q: AI is not syncing all products from the store.
Q: The product count in AI data source doesn't match the Shopify product count.
A: Only published, in-stock products are synced to the AI. Products sync daily at 12:00 AM PST.

**Common causes:**
- Products are in draft status or out of stock.
- The merchant has hit their plan's product limit (Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000).
- Sync hasn't run yet after recent product changes.

**Support flow:**
1. Check the merchant's plan and product count against the plan limit.
2. Verify products are published and in stock in Shopify.
3. If needed, wait for the next daily sync or trigger a manual resync.
4. If the issue persists, escalate to the dev team.

---

Q: The merchant deleted all products in Shopify but old products still show in AI sync.
Q: Products were removed from Shopify but AI still answers questions about them.
A: The sync may not immediately reflect product deletions.

**Solution:**
1. Suggest the merchant turn off product synchronization entirely.
2. When they add products back later, they can re-enable sync.
3. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync at 7 AM.

---

Q: Merchant wants to extend the number of products, URLs, or files for AI training.
Q: The merchant has hit the AI training data limit on their plan.
A: Plan limits restrict the number of products/URLs/files for AI training.

**Support flow:**
1. Check the merchant's current plan and what data type they need more of (Products/URLs/Files).
2. Explain plan limits and recommend an appropriate upgrade.
3. If the merchant is not ready to upgrade (testing, small budget): escalate to `#sales-cs-success` tagging PM + CSL.
4. For small increases (100-200 products, 10-20 URLs/Files): CS can proactively extend limits in DevZone without requiring an upgrade.
5. For stores with > 10,000 products: offer a demo call with the sales lead — this requires manual backend configuration beyond standard limits.
6. Never promise beyond your authority — always say "I'll check internally" before confirming extensions.

---

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

- Contact support — they can extend up to the next plan's level as a one-time accommodation
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

---
category: Common Issues
topic: AI Giving Wrong Responses
source: notion/Chatty FAQs
---

Q: The AI assistant is giving wrong answers to customer questions. What should I do?
Q: AI is answering incorrectly. How do I fix it?
Q: A merchant says the AI chatbot responded with wrong information.
A: When the AI provides incorrect answers, follow this process:

**Step 1: Identify the issue**
- Ask the merchant for the specific chat link/ID where the AI responded incorrectly.
- Determine what information was wrong (product details, pricing, policy, etc.).

**Step 2: Review the AI's data sources**
- For live conversations: open the conversation and click "Review Sources" under each AI reply to see which data sources and instructions the AI used.
- For test conversations: go to Dev Zone to review test conversation history, check context, data sources, and instructions.

**Step 3: Diagnose the root cause**
- **(a) Source data is wrong or incomplete:** Recommend the merchant update or correct the source content. CS can assist with edits.
- **(b) Source is correct but AI misinterprets:** Confirm the source is accurate but AI inferred incorrectly. Report to dev team. Suggest rephrasing questions or adding more detailed documentation.
- **(c) Instructions are inappropriate:** Review App, Custom, and Scenario Instructions. Identify what causes the AI to misunderstand. Propose instruction edits and test.

**Step 4: Follow up**
- If the issue persists after corrections, escalate to the product/dev team.
- Continue following up with the merchant until resolved.

---

Q: The AI is showing wrong product prices. It doesn't match the customer's market.
Q: AI suggests wrong price — not matching the market the customer is visiting.
A: This happens when the AI pulls pricing from the main domain instead of the market-specific pricing.

**Step 1: Check Markets setup**
- Ask the merchant if they have set up Markets in Shopify Admin.
- Check if "Sync Markets" is enabled in AI Assistant settings.

**Step 2: CS reproduces the issue**
- Visit the merchant's market domain and test the same question.

**Step 3: Handle by scenario**
- **If Markets are NOT set up:** Guide the merchant to set up Markets in Shopify Admin and enable "Sync Markets" in AI Assistant settings. Test again afterward.
- **If Markets ARE set up but issue persists:** Request staff access to inspect Markets and Product settings. Report the issue to dev team with screenshots, reproduction steps, Market config, and product pricing per Market.

---

Q: The AI sends wrong product links — they lead to 404 pages or wrong products.
Q: AI product links are broken or incorrect.
A: This is a known bug that the dev team has acknowledged.

**Support flow:**
1. Ask the merchant for the specific chat with the incorrect link.
2. Go to the merchant's store and test in the AI Test section to confirm the issue.
3. Report the store URL and chat link in the internal Slack bug thread for dev team follow-up.
4. Inform the merchant that the dev team has acknowledged the bug and is investigating. Suggest manually copying correct product links as a workaround and apologize for the inconvenience.
5. Follow up when the fix is deployed.

---

Q: The AI suggests wrong domain for product URLs when customer visits a market-specific domain.
Q: Customer visits abc.fr but AI shows links to abc.com.
A: This is a current technical limitation — the app only stores product data for the main domain. Multi-domain support per Shopify Market is being developed.

**Support flow:**
1. Confirm which market domain the customer visited and what URL the AI returned.
2. Check the merchant's Shopify Markets setup: verify country is in Market setup and domain mapping is correct.
3. Reproduce the issue by visiting the market domain and testing the same question.
4. Notify the merchant that this is a known limitation — the app currently only stores product data for the main domain. Multi-domain support per Shopify Market is being developed and a fix is planned.
5. Create a tracking card and follow up with the merchant.

---

Q: The AI does not return variant-specific product links.
Q: AI only sends generic product links, not links for specific variants (size, color).
A: This is a feature limitation — variant-level links have not been fully implemented yet. The AI's data source does not store variant-specific URLs.

A feature is currently in development to support variant-specific links. In the meantime, inform the merchant that the AI can describe variants but cannot link directly to them.

---

Q: AI responses are duplicated — the same answer appears twice.
Q: The AI sends duplicate messages in the chat.
A: Duplicate AI responses can happen due to:
- Customer sending the same question multiple times (re-clicking or network lag).
- Slow or unstable network causing duplicate signals to the server.
- Temporary system-side processing error.

**Support flow:**
1. Request the chat ID and review the conversation to determine if it was user error or system error.
2. If system error: create a card for TS to investigate with conversation link, timestamp, and merchant name.
3. Suggest the merchant try "refresh chat" or switch to manual chat if duplication continues.
4. Follow up when the technical team responds.

---

Q: AI recommends products that don't belong to the merchant's store.
Q: The AI is suggesting products from other websites.
A: This can happen when AI training data is incomplete or not synced properly.

**Support flow:**
1. Request the chat ID of the incorrect response.
2. Check AI assistant settings: ensure AI product recommendation is enabled and sync is complete.
3. If settings are correct: reproduce the issue on the storefront. If confirmed, forward to dev team with full details.
4. If settings are incomplete: guide the merchant to enable and sync, then test again.
5. Monitor and update the merchant on progress.

---

Q: Why is the AI automatically transferring chats to a human agent when the customer did not ask?
A: This is usually triggered by the AI Human Handover and Automation settings.

1. Go to **AI Assistant** → **Instructions** → **Assistant skills** → **Human handover** and review your configured triggers. Common triggers include certain keywords or unanswered questions. Adjust or remove the rules causing unintended escalation.
2. Check **Automation** tab in Chatty settings for assignment method. If **Automatic assignment** is selected, conversations will be transferred to human agents when trigger keywords are detected.

---

Q: The AI is not adding products to the cart correctly (wrong quantity / not updating cart count).
A: This is a known integration issue that may be due to the store theme not supporting Chatty's add-to-cart function.

Currently, the **Add to Cart** feature operates on the backend. With certain store themes, the cart count or drawer may not update in real-time immediately after the AI performs the action. After the AI confirms a product was added, please refresh the page to verify.

If the issue persists, please share your store collaborator code so our team can investigate — this may require a fix at the theme level.

---

Q: Links in AI responses are not clickable / showing as plain text.
A: The AI needs to be trained to format links as markdown.

Steps:
1. Go to **AI Assistant** → **Instructions**
2. Under **Behaviours**, add an instruction: `When sharing a link, format it as [Link Name](URL).`

Alternatively, our team can update the AI prompt for your store to ensure links are always rendered as clickable hyperlinks. Contact support for assistance.

---

Q: The AI is recommending invalid products / products with broken links (404 errors).
A: This happens when products have been deleted or unpublished in Shopify but are still in Chatty's training data.

Steps:
1. Go to **AI Assistant** → **Training Data** → **Products**
2. Click **Sync Products** to refresh the catalog
3. Remove any manually added product URLs that are outdated

After syncing, use **Test AI** to verify recommendations.

---

Q: HTML is showing in chat responses instead of rendered text.
A: This means the AI is pulling raw HTML from your training data content.

Steps:
1. Go to **AI** → **Training Data** and review your FAQ or scenario content
2. Remove any HTML tags (such as `<div>`, `<p>`, `<br>`, etc.) and keep content in plain text
3. If you want to format responses, use simple markdown (e.g. bold text or links) instead of HTML — Chatty's AI handles markdown, not HTML
4. Save changes and test the response again.

---

Q: The AI is mixing up information from two similar FAQs (e.g. two policies with overlapping topics).
A: This happens when the AI finds conflicting or similar content across multiple FAQ entries.

How to fix:
1. Merge the two overlapping FAQs into one comprehensive entry
2. Make the trigger keywords more specific and distinct for each FAQ
3. Remove duplicate or redundant content from the AI knowledge base
4. Use the **Test AI** feature to verify the AI picks the right response after your changes.

---

Q: The AI is not transferring to a human agent even when the customer explicitly asks.
A: Check your **Pre-transfer message** in Human Handover settings — if it references an email option, the AI may interpret the customer's "yes" as agreement to contact via email rather than a live transfer. Revise the pre-transfer message to guide the AI toward the intended action. Contact support for help adjusting the wording.

---

Q: Can I configure the AI to send contact details via email instead of doing a live transfer?
A: Yes — go to **AI Assistant** → **Instructions** → **Assistant Skills** → **Human Handover** and configure the handover to send the conversation details to your support email instead of assigning to a live agent. Contact support if you need help configuring this.

---

Q: Can I set up the AI to transfer conversations to a human after a fixed time without a response?
A: This is not currently a built-in feature. A feature request for "Auto-assign AI conversations to a human team after a fixed time" has been noted by the product team for consideration on the roadmap.

---

# Air Reviews Integration

<!-- CHUNK: air-reviews-overview -->
```yaml
chunk_id: "faq__air-reviews-overview"
doc_id: "chatty-air-reviews"
title: "How Chatty integrates with Air Reviews to collect more product reviews"
category: "faq"
subcategory: "integrations"
tags: ["air reviews", "product reviews", "review integration", "prevent negative reviews", "review collection", "Air Product Reviews"]
applies_when: "When a merchant asks how to use Chatty with Air Reviews or how to collect more product reviews"
priority: "medium"
```

## Air Reviews Integration Overview

Chatty integrates with Air Reviews to turn positive customer conversations into reviews. By resolving issues quickly in chat, you create satisfied customers who are more likely to leave positive feedback.

Air Product Reviews is free to download from the Shopify App Store.

**How Chatty helps with review collection:**
- Capture customer concerns in real time before they become public negative reviews
- Resolve issues quickly to prevent negative reviews
- Create personalized touchpoints for requesting reviews after good interactions
- Provide 24/7 AI support to address questions instantly

---

<!-- CHUNK: air-reviews-setup -->
```yaml
chunk_id: "faq__air-reviews-setup"
doc_id: "chatty-air-reviews"
title: "How to set up Chatty and Air Reviews integration for review collection"
category: "faq"
subcategory: "integrations"
tags: ["air reviews setup", "review setup", "proactive chat reviews", "train AI reviews", "prevent bad reviews"]
applies_when: "When a merchant wants to set up the Air Reviews integration or asks for best practices to get more reviews"
priority: "medium"
```

## How to Set Up

**Step 1: Install both apps**
- Install Chatty (if not already done)
- Install Air Reviews from the Shopify App Store

**Step 2: Set up your customer support center**
- Enable chatbox
- Enable live chat
- Activate and train your AI assistant

**Step 3: Best practices for review collection**

**Train AI to encourage reviews:**
- Add Q&A to your data sources about leaving a review
- Create replies that politely guide satisfied customers to leave feedback

**Set up proactive chat for post-purchase customers:**
- Identify moments when customers are likely to leave a review (e.g., after delivery)
- Create proactive messages encouraging reviews at the right moment

**Add FAQs about reviews:**
- In your FAQs list, add content about the review process for post-purchase questions

**Respond quickly to prevent negative reviews:**
1. Set up notifications in Chatty so you don't miss new messages
2. Use quick replies for common questions to respond faster
3. Prioritize customers expressing frustration
4. Resolve issues completely before requesting a review


---

# Analytics

<!-- CHUNK: analytics-overview -->
```yaml
chunk_id: "faq__analytics-overview"
doc_id: "chatty-analytics"
title: "Overview of Chatty analytics — what's tracked and how to access it"
category: "faq"
subcategory: "analytics"
tags: ["analytics", "dashboard", "performance", "metrics", "conversations", "AI performance", "sales analytics", "FAQ analytics"]
applies_when: "When a merchant asks what analytics Chatty provides or how to view performance data"
priority: "medium"
```

## Analytics Overview

Chatty Analytics gives you insights into customer conversations, AI performance, sales contribution, and FAQ engagement.

**Analytics areas:**
1. **Dashboard overview**: Quick performance snapshot
2. **Human agent**: Metrics for conversations handled by your team
3. **AI assistant**: How your AI is handling inquiries
4. **Sales**: Revenue and conversion tracking
5. **FAQs**: Customer engagement with self-serve FAQ content

## How to Access Analytics

**Dashboard overview:**
Go to **Dashboard** → **Overview** to see:
- Total conversations
- Chat-to-sales rate (percentage of conversations where customers made an order)

Use the time range selector to filter, or click **Reload** to refresh.

**Detailed analytics:**
Go to **Analytics** → Use the time filter at the top → Compare with previous periods using the comparison toggle → Check trend charts → Click **Reload** to refresh.

---

<!-- CHUNK: analytics-metrics -->
```yaml
chunk_id: "faq__analytics-metrics"
doc_id: "chatty-analytics"
title: "Detailed breakdown of all analytics metrics in Chatty"
category: "faq"
subcategory: "analytics"
tags: ["analytics metrics", "resolution rate", "first response time", "AI resolution rate", "assisted revenue", "conversion rate", "chat to sales"]
applies_when: "When a merchant asks what specific metrics are available or what a particular metric means"
priority: "medium"
```

## What's Tracked

**Overview tab:**
- Total conversations
- Resolution rate
- Chat-to-sales rate
- Assisted revenue
- Total sales share contributed by Chatty

**Human agent tab:**
- Total conversations assigned to human agents
- New conversations started in the period
- Resolved conversations
- First response time (average time to first reply)
- Handling time (start to resolution)
- Resolution time (assignment to resolution)

**AI assistant tab:**
- AI involved rate (% of conversations where AI participated)
- AI resolution rate (% of AI-handled conversations resolved without human intervention)
- Answer rate (% of customer messages AI successfully answered)
- Time saved (estimated time saved by using AI)

**Sales tab:**
- Total sales from Chatty interactions
- Total store revenue share from Chatty
- Total orders from customers who interacted with Chatty
- AOV (Average Order Value) from Chatty-attributed sales
- Conversion rate (% who purchased after interacting with Chatty)
- Customer feedback (thumbs up/down on AI responses)

**FAQs tab:**
- Published FAQs count
- Total views
- FAQ views over time
- Top viewed FAQs


---

---
category: CS Process
topic: Asking for Shopify Reviews
source: cs-process
---

Q: When should I ask a merchant for a review?
Q: What's the right timing to request a Shopify App Store review?
Q: How do I know if it's a good time to ask for a review?
A: Ask for a review when the merchant has clearly experienced value. Use judgment — timing matters more than completing every single request.

**✅ Good times to ask:**
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

**Strictly prohibited:**
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

**Why this matters:**
- Prevents asking the same merchant for a review again
- Avoids annoying merchants who already reviewed
- Helps track review activity accurately per merchant

---

Q: Can a merchant still leave a review after uninstalling the app?
Q: How long does a merchant have to leave a review after uninstalling?
A: Yes. After uninstalling, a merchant has **45 days** to leave a review on the Shopify App Store before that option expires.


---

# Billing & Subscription Issues

<!-- CHUNK: billing-refund-request -->
```yaml
chunk_id: "billing__refund-request"
doc_id: "chatty-billing-subscription"
title: "Handling refund requests and subscription cancellations"
category: "billing"
tags: ["refund", "cancel", "subscription", "cancellation", "billing request", "money back"]
applies_when: "Merchant is requesting a refund or wants to cancel their subscription"
```

## Handling Refund Requests & Cancellations

**Step 1: Understand the reason**
- Why does the merchant want to cancel or get a refund?

**Step 2: If the issue is bugs or unmet expectations**
- Identify what the merchant expected
- Proactively offer to fix the issue, re-guide setup, or test the feature
- If resolved, encourage continued use. Consult CSL about offering a discount for next month
- Follow up to ensure the problem is fully resolved before processing any refund

**Step 3: If the merchant still wants to cancel/refund**
- Apologize and collect billing details — **ask for a screenshot of the invoice** showing app name, billing cycle, and amount
- Confirm whether the invoice has been paid
- Guide the merchant to downgrade to the **Free plan** to prevent further charges

**Step 4: Create escalation card**
- Assign to CSL with full details

**CRITICAL: CS must NEVER approve any refund without CSL approval. Unauthorized approvals make the CS agent personally liable.**

---

<!-- CHUNK: billing-charged-after-cancel -->
```yaml
chunk_id: "billing__charged-after-cancel"
doc_id: "chatty-billing-subscription"
title: "Merchant charged after cancelling subscription"
category: "billing"
tags: ["charged after cancel", "charge after cancellation", "billing after cancel", "Shopify billing", "cancel charge"]
applies_when: "Merchant cancelled their subscription but still sees charges"
```

## Charged After Cancelling

Shopify automatically charges when a subscription begins, even if cancelled afterward — the charge covers the billing period the merchant used before cancelling.

1. Verify the exact cancellation date and billing status
2. Determine if the charge belongs to the current or previous billing period
3. Explain the Shopify billing cycle to the merchant
4. If the merchant did not use the app after being charged, create a refund request and assign to Billing/CSL
5. Guide the merchant on proper cancellation timing to avoid future charges

---

<!-- CHUNK: billing-discount-request -->
```yaml
chunk_id: "billing__discount-request"
doc_id: "chatty-billing-subscription"
title: "Merchant requesting a discount to upgrade"
category: "billing"
tags: ["discount", "discount request", "upgrade discount", "promo", "offer discount"]
applies_when: "Merchant is asking for a discount to upgrade to a paid plan"
```

## Handling Discount Requests

**CS must NEVER independently offer discounts.** All offers require Sales team or CSL approval.

1. Confirm which plan the merchant is interested in
2. Offer a demo call with PM
3. If the merchant doesn't book a call, escalate to the sales/CS team with: store name, current plan, desired plan, reason for discount, desired discount level, and recent support history
4. If approved → send the offer and guide the upgrade process
5. If not approved → politely explain, emphasize app value, suggest continuing with the free trial

---

<!-- CHUNK: billing-linkedin-discount -->
```yaml
chunk_id: "billing__linkedin-discount"
doc_id: "chatty-billing-subscription"
title: "LinkedIn 40% discount promotion"
category: "billing"
tags: ["LinkedIn", "40% discount", "LinkedIn promotion", "discount code", "follow LinkedIn"]
applies_when: "Merchant is asking about a discount for following Chatty on LinkedIn"
```

## LinkedIn 40% Discount Promotion

This is a promotional campaign offering **40% off for 1 month** for following Chatty on LinkedIn.

- The banner displays on the Dashboard
- For merchants with average monthly orders > 40: request a screenshot of the LinkedIn follow, then send discount code `LINKEDIN-FOLLOWER-40OFF-1MO`
- For other merchants: the promotion does not apply

---

<!-- CHUNK: billing-legacy-plans -->
```yaml
chunk_id: "billing__legacy-plans"
doc_id: "chatty-billing-subscription"
title: "Enable legacy pricing plans for a merchant"
category: "billing"
tags: ["legacy plan", "old plan", "old pricing", "enable legacy", "DevZone"]
applies_when: "Merchant needs access to legacy or old pricing plans"
```

## Enabling Legacy Plans

Go to **DevZone** → **General** to enable legacy plans for the merchant.


---

# Billing & Refund Playbook

## Case Types

### General Inquiry (plan comparison, how to upgrade)

CS handles directly. Explain plan features and guide the merchant through the upgrade process in Shopify Admin.

### Charge Confusion (why charged, unexpected amount)

CS explains the charge. Check the merchant's charge history, review plan usage, and provide invoice details.

### Cancellation Request

1. Understand why they want to cancel
2. If possible, address their concerns
3. If they proceed → guide them through cancellation/downgrade

### Refund Request

**CS is NOT authorized to approve any refund request without CS Leader approval.**

#### Simple cancellation (merchant doesn't want to continue / subscribed by mistake)

**Step 1:** Guide merchant to downgrade to Free plan. Verify they've downgraded.

**Step 2:** Collect billing info using `!billing-details`:
- Screenshot of invoice showing: app name, billing cycle, amount
- Whether the invoice has been paid
- Where to find: Shopify Admin > Settings > Billing

**Step 3:** Create Trello card for CS Leader using `!refund-process`:
- Assign to CS Leader
- Include all details and refund reason

#### Dissatisfaction or bug-related refund

**Step 1:** Understand their expectations — what they were trying to achieve

**Step 2:** Proactively offer support:
- If setup/feature misunderstanding → guide them again
- If bug → help resolve it
- If resolved and merchant is satisfied → encourage continued use, consult CS Leader about next-month discount

**Step 3:** If merchant still wants to cancel:
- Apologize for the experience
- Collect billing info (`!billing-details`)
- Guide to downgrade to Free plan

**Step 4:** Create Trello card for CS Leader

**High-risk cases:** If merchant doesn't accept your explanation after clear communication → do NOT argue. Escalate to CS Leader/CSM immediately.

### Dispute / Chargeback

Immediately escalate to CS Leader with full context.

---

## Common Billing Questions

**Q: How long does a refund take?**
7–10 business days. Depends on Shopify's refund process and the bank. If > 10 days, advise merchant to check with Shopify and their bank directly.

**Q: Merchant was charged after uninstalling/downgrading. Why?**
If they uninstalled/downgraded after the billing cycle started, they'll receive a full invoice for that cycle but be refunded for unused days.

**Q: Merchant shows Free plan but was charged. What happened?**
They may have uninstalled (auto-cancels subscription), then reinstalled (defaults to Free), but the final bill from the previous cycle was still pending.

**Q: Two bills in the same month?**
Ask for charge breakdown screenshot. If different billing periods → explain. If same period → check with CS Leader. May be caused by exceeding billing threshold before regular billing date.

**Q: When will the merchant be charged?**
On their regular Shopify billing date, together with Shopify subscription and other app charges.

**Q: Where to see charges?**
Shopify Admin > Settings > Billing > Bills.

**Q: Why did payment fail?**
Common reasons: expired card, no payment method, insufficient funds, card doesn't support recurring USD payments.

---

## Key Shortcuts

| Shortcut | Purpose |
|----------|---------|
| `!cancel-reason` | Confirm cancellation reason with merchant |
| `!billing-details` | Request billing info (invoice screenshot, payment status) |
| `!refund-process` | Set expectations with merchant about refund timeline |


---

# Case Handling Playbook

## Case Classification

When a merchant reaches out, classify their request:

| Case Type | Examples | Handler |
|-----------|----------|---------|
| **How-to Questions** | "How do I set up X?", "Where can I find Y?" | CS Agent |
| **Bug/Issue Reports** | "Feature X is broken", "Widget not showing" | CS → TS → Dev |
| **Feature Requests** | "Can you add X?", "Integration with Y?" | CS Agent → PM |
| **Billing & Subscription** | "Why was I charged?", "How do I upgrade?" | CS Agent (CS Leader for refunds) |
| **Complaints** | "Your app is terrible!", "I've been waiting for days" | CS Agent → CS Leader |
| **Pre-sales Questions** | "Does your app do X?", "How much does it cost?" | CS Agent |
| **Integration Questions** | "Can this work with X?", "How do I connect Y?" | CS (basic) → TS (complex) |
| **Discount Requests** | "Can I get a discount on the plan?" | CS Agent → CS Leader/Sales |
| **Demo Requests** | "Can you show me how this works?" | CS Agent (schedule) |

First determine: does the merchant have a **question** or a **problem**? Then classify into the specific case type.

---

## How-to Questions

1. Check knowledge base for the answer
2. Provide step-by-step answer with navigation paths
3. Link to relevant helpcenter article
4. Follow up to confirm it worked

## Bug/Issue Reports

1. **Triage** — is it a bug or a configuration issue?
2. **Basic troubleshooting** — check settings, clear cache, try another browser
3. **Gather evidence** — screenshots, steps to reproduce, store URL, plan
4. **If config issue** → guide the merchant to fix it
5. **If confirmed bug** → escalate to TS via Trello card (see [escalation.md](escalation.md))

## Feature Requests

1. Understand what the merchant is trying to achieve
2. Check if an existing feature already solves their need
3. If no existing solution → document the request and forward to PM
4. Don't promise features or timelines — say "I'll pass this to our product team"

## Complaints

SLA: respond within **2 hours**.

1. Respond quickly — don't leave an angry merchant waiting
2. Stay professional — don't take it personally
3. Understand root cause — what actually went wrong?
4. Take ownership — apologize for their experience
5. Provide a solution — specific action plan with realistic timeline
6. Follow through — do what you promised, update proactively
7. Document and share with the team

**Escalate to CS Leader when:**
- After 2 attempts, merchant is still angry
- Merchant threatens legal action or public negative review
- Issue involves refund or compensation
- VIP merchant complaint

## Pre-sales Questions

SLA: respond within **4 hours**.

1. Respond fast — these are potential customers
2. Understand their needs
3. Be honest about capabilities — don't oversell
4. Guide them to free trial
5. Share relevant helpcenter links or demo

## Integration Questions

1. Identify the integration type (native, third-party, custom)
2. For native integrations → provide setup guide
3. For complex/custom integrations → escalate to TS

## Discount Requests

1. Listen to the merchant's reasoning
2. Escalate to CS Leader or Sales Manager — CS agents do not have authority to approve discounts


---

# Channels Overview

<!-- CHUNK: channels-overview -->
```yaml
chunk_id: "channels__overview"
doc_id: "chatty-channels"
title: "What channels can I connect to Chatty"
category: "channels"
tags: ["channels", "connect channels", "email", "Facebook", "Instagram", "WhatsApp", "Messenger", "unified inbox"]
applies_when: "Merchant asks what channels they can connect to Chatty or how to manage all messages in one place"
```

## Channels Overview

Chatty lets you manage conversations from multiple channels in one unified inbox: **live chat, email, Facebook Messenger, Instagram, and WhatsApp**.

Go to **Settings** → **Channels** to connect each channel. Once connected, messages from all channels appear in the Chatty inbox.

**Email:**
- Connect one email for forwarding to Chatty inbox
- Settings: email forwarding address, email sender (used for replies), email signature

**Facebook Messenger & Instagram:**
- Connect your Facebook account to receive and reply to Facebook and Instagram messages
- Only Instagram business accounts connected to a Facebook Page can be integrated

**WhatsApp:**
- Connect WhatsApp Business — you can connect multiple WhatsApp accounts
- Requires: a Facebook page, a WhatsApp Business account linked to that page, and admin access to both

---

<!-- CHUNK: channels-outlook-blocked -->
```yaml
chunk_id: "channels__outlook-blocked"
doc_id: "chatty-channels"
title: "Outlook email forwarding blocked — can't connect to Chatty"
category: "channels"
tags: ["Outlook", "blocked", "email forwarding", "organization", "IT admin", "forwarding blocked"]
applies_when: "Merchant can't connect their Outlook email because email forwarding is blocked"
```

## Outlook Email Forwarding Blocked

The most common reason is your organization's Outlook settings blocking automatic email forwarding for security reasons.

1. Contact your organization's IT administrator
2. Take a screenshot of the error message
3. Request permission to allow email forwarding to Chatty
4. Once permission is granted, go back to Chatty and reconnect your Outlook email

---

<!-- CHUNK: channels-unified-inbox -->
```yaml
chunk_id: "channels__unified-inbox"
doc_id: "chatty-channels"
title: "Manage all channels in one Chatty inbox"
category: "channels"
tags: ["unified inbox", "all channels", "Gmail", "Facebook", "Instagram", "WhatsApp", "one inbox"]
applies_when: "Merchant asks if they can manage all channels (Gmail, Facebook, Instagram, WhatsApp) in one inbox"
```

## Unified Inbox for All Channels

Yes — go to **Settings** → **Channels** and connect each channel. Once connected, messages from all channels appear in the unified Chatty inbox. A single team member can manage all channels from one place.


---

# Chatbox Settings & Customization

<!-- CHUNK: chatbox-settings-overview -->
```yaml
chunk_id: "chatbox__settings-overview"
doc_id: "chatty-chatbox-settings"
title: "Chatbox customization overview"
category: "chatbox-settings"
tags: ["chatbox", "customize", "appearance", "settings", "colors", "setup", "general settings"]
applies_when: "Merchant asks how to customize the chatbox or change its appearance and settings"
```

## Chatbox Customization Overview

**General settings** (**Chatbox** → **General**):
- Turn chatbox on/off
- **Chat focus mode** — chatbox takes focus when opened
- **Header** — upload logo, customize heading and description
- **Blocks** — turn on: Contact us, Order tracking, FAQs, Categories

**Appearance settings** (**Chatbox** → **Appearance**):
- **Brand colors** — presets, custom, or "Surprise me"
- **Chatbox button** — launcher type, icon, size, alignment
- **Chatbox style** — show/hide navigation, mobile ratio

**Advanced settings** (**Chatbox** → **Advanced**):
- **Deep links** — URLs that open specific sections
- **Display devices and pages** — choose which devices/pages show the chatbox
- **Continue as email** — customers can continue conversation by email
- **Custom code** — add custom CSS for advanced customization

**Chat page settings** (**Chatbox** → **Chat page**):
- Welcome message, conversation starters, chat avatar
- How customers start a chat: as guest (form required), anonymous (no form), or both
- Pre-chat form — collects customer info (email, name, phone)

---

<!-- CHUNK: chatbox-welcome-message -->
```yaml
chunk_id: "chatbox__welcome-message"
doc_id: "chatty-chatbox-settings"
title: "Change the welcome message or greeting in chatbox"
category: "chatbox-settings"
tags: ["welcome message", "greeting", "chat greeting", "first message", "opening message"]
applies_when: "Merchant wants to change the welcome message shown when customers open the chat"
```

## Changing the Welcome Message

Go to **Chatbox** → **Chat page** → **Welcome Message** to customize the greeting text. Changes take effect immediately after saving.

If using the AI Assistant, go to **AI Assistant** → **Settings** (top right) → **AI Identity** to customize the welcome message for the AI separately.

---

<!-- CHUNK: chatbox-widget-overlap -->
```yaml
chunk_id: "chatbox__widget-overlap"
doc_id: "chatty-chatbox-settings"
title: "Chat widget overlapping or blocking another element"
category: "chatbox-settings"
tags: ["overlap", "overlapping", "blocking", "cart button", "add to cart", "position", "z-index"]
applies_when: "The Chatty widget is overlapping or blocking another element on the store (e.g. cart button)"
```

## Widget Overlapping Another Element

1. Go to **Chatbox** → **Advanced** → **Custom CSS** to fine-tune the position with CSS
2. To hide the widget on specific pages, go to **Display pages** settings

---

<!-- CHUNK: chatbox-appearance-colors -->
```yaml
chunk_id: "chatbox__appearance-colors"
doc_id: "chatty-chatbox-settings"
title: "Change chatbox colors, text size, and font"
category: "chatbox-settings"
tags: ["colors", "appearance", "font", "text size", "brand color", "customize colors", "chatbox design"]
applies_when: "Merchant wants to change the chatbox colors, text size, or font"
```

## Changing Chatbox Colors & Appearance

Go to **Chatbox** → **Appearance** to customize: primary color, background color, and text color. Use pre-built presets for quick selection.

For advanced customization (font size, spacing), use **Custom CSS** under **Chatbox** → **Advanced**. Preview changes in real-time before saving.

---

<!-- CHUNK: chatbox-conversation-starters -->
```yaml
chunk_id: "chatbox__conversation-starters"
doc_id: "chatty-chatbox-settings"
title: "Set up conversation starters or predefined questions"
category: "chatbox-settings"
tags: ["conversation starters", "predefined questions", "quick questions", "starter buttons", "suggested questions"]
applies_when: "Merchant wants to add predefined questions or conversation starters to the chatbox"
```

## Setting Up Conversation Starters

Conversation Starters are clickable shortcut buttons (also called quick-access FAQ buttons) that appear when a customer opens the chatbox, letting them quickly ask common questions or jump to FAQ topics.

1. Go to **Chatbox** → **Chat page** → **Conversation Starters**
2. Click **Add Starter** and enter the question text

You can add up to 4–6 starters. Link each starter to a specific AI scenario for consistent responses.

---

<!-- CHUNK: chatbox-hide-icon-cart -->
```yaml
chunk_id: "chatbox__hide-icon-cart"
doc_id: "chatty-chatbox-settings"
title: "Hide Chatty icon when cart drawer is open"
category: "chatbox-settings"
tags: ["hide widget", "cart drawer", "cart popup", "widget visibility", "hide chatty"]
applies_when: "Merchant wants to hide the Chatty icon when the cart drawer or popup is open"
```

## Hide Widget When Cart Drawer Opens

1. Go to **Chatbox** → **Advanced** → **Custom CSS**
2. Add a custom CSS rule or use the **Hide Widget** trigger under Display settings

Alternatively, add custom JavaScript in your theme to detect when the cart drawer opens and dispatch a Chatty hide event. Contact support for the exact code snippet for your specific theme.

---

<!-- CHUNK: chatbox-disable-auto-open -->
```yaml
chunk_id: "chatbox__disable-auto-open"
doc_id: "chatty-chatbox-settings"
title: "Disable chatbox opening automatically on page load"
category: "chatbox-settings"
tags: ["auto open", "opens automatically", "page load", "chat focus mode", "disable auto open"]
applies_when: "The chatbox is opening automatically on every page load and merchant wants to disable it"
```

## Chatbox Opening Automatically

1. Go to **Chatbox** → **General**
2. Toggle off **Chat focus mode**

If the chatbox still opens on load, check if any **Proactive Chat** campaigns are configured to trigger immediately on page load and disable them in **Proactive Chat** settings.

---

<!-- CHUNK: chatbox-phone-button -->
```yaml
chunk_id: "chatbox__phone-button"
doc_id: "chatty-chatbox-settings"
title: "Add a phone or call button to the chatbox"
category: "chatbox-settings"
tags: ["phone button", "call button", "phone number", "contact", "add phone", "click to call"]
applies_when: "Merchant wants to add a phone or call button to the chatbox"
```

## Adding a Phone/Call Button

1. Go to **Chatbox** → **Channels**
2. Click **Add Channel** → select **Phone**
3. Enter your phone number and save

A call button will appear in the chatbox. On mobile, it opens the native dialer. Customize the button label and icon in Appearance settings.

---

<!-- CHUNK: chatbox-resize-bubble -->
```yaml
chunk_id: "chatbox__resize-bubble"
doc_id: "chatty-chatbox-settings"
title: "Resize the chat bubble icon"
category: "chatbox-settings"
tags: ["resize", "bubble size", "icon size", "chat bubble", "smaller bubble", "larger bubble"]
applies_when: "Merchant wants to resize the chat bubble icon"
```

## Resizing the Chat Bubble

Go to **Chatbox** → **Appearance** to adjust the icon size and style.

For a percentage-based resize (e.g., reduce to 60%), a custom CSS code can be added via **Chatbox** → **Advanced** → **Custom CSS**. Contact support to help apply this.

---

<!-- CHUNK: chatbox-embed-widget -->
```yaml
chunk_id: "chatbox__embed-widget"
doc_id: "chatty-chatbox-settings"
title: "Embed chat widget directly into a page section"
category: "chatbox-settings"
tags: ["embed", "embedded chatbox", "inline chat", "page section", "hero banner", "embed code"]
applies_when: "Merchant wants to embed the chat widget directly into a page section instead of a floating button"
```

## Embedding Chat Widget in a Page

Go to **Chatbox** → **Embedded** to get the embed code.

Note: embedding a fully functional AI chat widget into a Hero Banner or homepage section is in development. For now, the embedded option works within page content sections.

---

<!-- CHUNK: chatbox-disable-view-similar -->
```yaml
chunk_id: "chatbox__disable-view-similar"
doc_id: "chatty-chatbox-settings"
title: "Disable the View Similar button in AI product recommendations"
category: "chatbox-settings"
tags: ["View Similar", "view similar button", "disable", "product recommendation", "hide button"]
applies_when: "Merchant wants to disable or hide the View Similar button that appears in AI product recommendations"
```

## Disabling "View Similar" Button

Currently there is **no on/off toggle** for this button in settings.

Contact support — the team can hide it using custom CSS via **Chatbox** → **Advanced** → **Custom CSS**.

---

<!-- CHUNK: chatbox-away-mode -->
```yaml
chunk_id: "chatbox__away-mode"
doc_id: "chatty-chatbox-settings"
title: "What is Away Mode and how to use it"
category: "chatbox-settings"
tags: ["away mode", "offline", "unavailable", "away", "lunch break", "status"]
applies_when: "Merchant asks about Away Mode or how to appear offline without logging out"
```

## Away Mode

Away mode allows individual team members to appear offline to customers without logging out. When enabled:
- The storefront shows that staff member as unavailable
- If **all** staff have Away mode on, customers see the store as offline
- Resets automatically when the member logs out and back in

Activate it via the toggle at the top of the Chatty app interface.

---

<!-- CHUNK: chatbox-unread-counter -->
```yaml
chunk_id: "chatbox__unread-counter"
doc_id: "chatty-chatbox-settings"
title: "Unread message counter on chat button"
category: "chatbox-settings"
tags: ["unread counter", "notification badge", "red number", "unread messages", "message count"]
applies_when: "Merchant asks about the red number badge on the chat button"
```

## Unread Message Counter

A red number on the chat button shows visitors how many unread or welcome messages are waiting.

If you turn on Proactive Chat (Welcome teaser in Automation), those messages also count as unread.


---

---
category: Common Issues
topic: Chatbox & Widget Issues
source: notion/Chatty FAQs
---

Q: The live chat button is not showing on the store.
Q: Chatbox widget doesn't appear on the merchant's website.
A: Common causes and solutions:

**Cause 1: App Embed not enabled**
- Go to Shopify Admin > Online Store > Themes > Customize > App Embeds.
- Ensure Chatty is toggled ON.
- Ask the merchant for a screenshot to verify.

**Cause 2: Live chat not turned on in app settings**
- Go to Chatbox > General > Blocks > ensure "Live chat" is enabled.

**Cause 3: Theme conflict**
- If App Embed is enabled but the button still doesn't show, ask the merchant for their theme name.
- Create a card for the TS team to investigate the technical issue.
- Follow up with the merchant on progress.

---

Q: The FAQ page is not showing on the store.
Q: Merchant can't see the FAQ page on their website.
A: Common causes:

1. **FAQ page not enabled in app:** Guide the merchant to Settings > Pages > Enable FAQ page.
2. **FAQ page URL not added to menu:** Help the merchant get the FAQ page URL from the app and add it to their store's navigation menu.
3. CS can request access to Themes and Pages to assist directly.

Reference: https://help.chatty.net/build-faqs/faqs-page

**Tip:** Suggest adding the FAQ URL to the main navigation menu for better visibility.

---

Q: The Chatty FAQ page is overwriting other page templates.
Q: Other pages (About Us, Contact) look wrong after installing Chatty FAQ.
A: The Chatty app assigns FAQ content to the default page template, which can affect other pages.

**Solution:**
1. In Shopify theme editor > Theme Templates, create a new template (e.g., `chatty-faq`).
2. Go to Shopify Admin > Online Store > Pages.
3. Select the FAQ page created by Chatty (usually "Frequently Asked Questions").
4. Assign the new template to this FAQ page only.
5. In the Chatty app, set the correct FAQ page URL.
6. Verify other content pages are no longer affected.

---

Q: The merchant wants to move the live chat button to a different position.
Q: How to change the position of the chat widget on the store.
A: The chatbox button position can be adjusted in Chatbox > Appearance > Set chatbox button > Select button alignment.

If the merchant needs more specific positioning:
1. Ask the merchant for their desired position.
2. For basic alignment changes, use the built-in button alignment settings.
3. For custom positioning, suggest CSS customization (if the merchant has coding knowledge).
4. If the merchant can't do it themselves, create a ticket for the TS team.

---

Q: How do I remove Chatty branding from the widget?
Q: Merchant wants to remove the "Powered by Chatty" watermark.
A: To remove branding:

1. Go to DevZone > General > Enable "Remove branding."
2. Notify the merchant to check.
3. Communicate: "Normally, this option is only available for paid plans. However, we've helped remove the branding for you this time as a special support."
4. After removing branding, proactively offer to help with other features.

**Important:** Do NOT ask for a review immediately after offering branding removal — Shopify considers this "exchange for review." First help with an additional task, then request a review based on the support experience.

---

Q: How do I use JavaScript to open or close the Chatty widget programmatically?
Q: Can I trigger the chatbox to open via code?
A: Chatty provides JavaScript functions for widget control:

- **Toggle open/close:** `avadaFaqTrigger()`
- **Close widget:** `ChattyJS.closeWidget()`
- **Open widget (general):** `ChattyJS.openWidget()`
- **Open to specific page:**
  - `ChattyJS.openWidget('#chatty-home')` — Home
  - `ChattyJS.openWidget('#chatty-chat')` — Message/Live Chat
  - `ChattyJS.openWidget('#chatty-tracking')` — Order Tracking
  - `ChattyJS.openWidget('#chatty-help')` — Help/FAQ

Use these when deep links cannot be used or the trigger element is not a standard link.

---

Q: How do I enable FAQ category icons for a merchant?
Q: The "View more" icons option in FAQ categories is locked.
A: For newly installed apps, the category icons feature is locked by default.

**Solution:**
1. Get the merchant's Store URL.
2. Go to DevZone and enable the category icons feature.
3. Notify the merchant to check if icons are now available.

---

Q: Chat widget is not clickable / button unresponsive on the first page load.
A: This is usually a JavaScript conflict with another app or theme.

Steps to troubleshoot:
1. Disable other chat or popup apps temporarily to test
2. Check browser console for JS errors
3. Clear browser cache

If it only happens on first load, it may be a timing issue — contact our support team with your store URL and browser details.

---

Q: Chat is slow to load on mobile / iPad — conversations take too long.
A: Common causes:

- **Theme performance or app conflicts** — try temporarily disabling other apps to see if loading improves
- **Slow or unstable internet** on the device
- **Widget loading conflicts** on the page

As a quick test, clear the browser/app cache and check on a different network. If the issue persists consistently, share your store URL and device/browser details with our support team for investigation.

---

Q: The AI logo/avatar upload is not working — nothing happens when I click upload.
A: Steps to try:

1. Use a different browser (Chrome is recommended)
2. Clear your browser cache and reload the page
3. Make sure the image is JPG or PNG and under 2MB
4. Try uploading in an Incognito/Private window

If the issue still persists, please share a screenshot and the image file you're trying to upload so our team can investigate.

---

Q: The chat widget button shows the wrong shape or icon on mobile.
A: This is usually caused by custom CSS in the app settings that conflicts on mobile. Contact support with a screenshot — the team will review and correct the CSS.

---

# Contact Button

<!-- CHUNK: contact-button-overview -->
```yaml
chunk_id: "faq__contact-button-overview"
doc_id: "chatty-contact-button"
title: "How to add, configure, and remove the contact button in Chatty"
category: "faq"
subcategory: "chatbox"
tags: ["contact button", "add contact button", "remove contact button", "product page button", "cart page button", "theme editor"]
applies_when: "When a merchant asks how to add, configure, or remove the contact button on their store"
priority: "medium"
```

## Contact Button Overview

The contact button is a quick-access button you can add to your product or cart pages to provide instant support. It only works on **Product** and **Cart** pages.

## How to Add a Contact Button

1. Go to **Chatbox**
2. Click **Turn on** Contact button
3. Click **Go to theme** to add the button to your theme
4. In the theme editor, select where you want to add the contact button → Click **Add block**
5. Select **Contact button** by Chatty
6. Customize the contact button in the right panel

> Note: The contact button only shows your active contact methods — those you've set up in the Contact us block in Chatbox settings.

## How to Remove the Contact Button

Go to the theme editor → Click on the Contact button block → Click **Remove block**.

> If you delete a contact method in Chatty, the contact button won't be deleted automatically. You need to go to the theme editor and remove the block manually.


---

# Contacts Management

<!-- CHUNK: contacts-overview -->
```yaml
chunk_id: "faq__contacts-overview"
doc_id: "chatty-contacts"
title: "How to view and manage customer contacts in Chatty"
category: "faq"
subcategory: "live-chat"
tags: ["contacts", "customer contacts", "chat history", "contact management", "customer profile", "guest", "anonymous user"]
applies_when: "When a merchant asks how to view, manage, or understand customer contact records in Chatty"
priority: "medium"
```

## Contacts Overview

The Contacts section lets you view and manage all customer contact information in one place.

You can:
- View conversation history and customer behavior
- Edit contact details
- Delete contacts
- Export contacts

> Note: If you delete a contact, all their conversations are deleted too.

## Customer Types

| Type | Definition |
|---|---|
| Guest | Visitors who left their email to start a chat, or whose conversations are linked through email, Messenger, or Instagram |
| Customer | Someone who made an order or subscribed to your store |
| Anonymous user | Someone who chatted by clicking "Chat with us as anonymous" |

## What You Can See in a Contact's Profile

- Chat history
- Activity timeline
- Overview: total orders, total spent, customer since
- Profile: name, email, phone, address
- Tags and notes

You can edit the customer profile, tags, and notes. Click the profile icon to go to the customer's profile in Shopify.

---

<!-- CHUNK: contacts-export -->
```yaml
chunk_id: "faq__contacts-export"
doc_id: "chatty-contacts"
title: "How to export contacts from Chatty"
category: "faq"
subcategory: "live-chat"
tags: ["export contacts", "download contacts", "contact CSV", "export customer data"]
applies_when: "When a merchant asks how to export their contact list from Chatty"
priority: "low"
```

## How to Export Contacts

1. Go to **Contacts**
2. Select contacts to export (current page or all contacts)
3. Click **Export**

If you export all contacts, the file will be sent to your email.

The export file includes:
- Customer type (guest, customer, anonymous)
- Contact info (name, email, phone, address)
- Order info (total orders, total spent)
- Timestamps (customer since, last updated)
- Tags and notes


---

# Cookie Policy

<!-- CHUNK: cookie-policy-overview -->
```yaml
chunk_id: "faq__cookie-policy-overview"
doc_id: "chatty-cookie-policy"
title: "What cookies Chatty uses and whether customer consent is required"
category: "faq"
subcategory: "privacy-policy"
tags: ["cookie", "cookie policy", "GDPR cookie", "session cookie", "avada-chatty/session", "cookie consent", "privacy"]
applies_when: "When a merchant asks what cookies Chatty uses, whether consent is required, or what data cookies track"
priority: "medium"
```

## Chatty Cookie Policy

Chatty uses a single cookie called `avada-chatty/session`. This cookie is essential for the live chat service to function correctly.

## What This Cookie Does

1. **Maintains conversation history**: Keeps the chat session active across different pages. Without it, customers would start a new chat every time they navigate to a new page.
2. **Prevents duplicate messages**: Ensures trigger messages don't fire multiple times.
3. **Consistent chat experience**: Maintains the chatbox state as customers browse.
4. **Duration**: The cookie lasts 30 days and is automatically renewed each time a customer sends a new message.

## What Information the Cookie Stores

1. **User preferences**: Language settings, theme preferences, customization choices
2. **Session information**: Chat history, conversation context, user inputs during the session
3. **User behavior**: Customer actions such as adding products to cart, initiating checkout, viewing FAQs, tracking orders

## Do Customers Need to Consent?

The `avada-chatty/session` cookie is considered essential for the functioning of the Chatty service. Under GDPR and many other privacy regulations, essential cookies are exempt from requiring explicit user consent.

However, it's recommended to mention this cookie in your store's privacy policy for full transparency.


---

# AI Data Sources

<!-- CHUNK: data-sources-overview -->
```yaml
chunk_id: "data-sources__overview"
doc_id: "chatty-data-sources"
title: "What are AI data sources and what can I add"
category: "data-sources"
tags: ["data sources", "training data", "what to add", "AI training", "data types"]
applies_when: "Merchant asks about data sources for AI training or what information they can add"
```

## AI Data Sources Overview

Chatty automatically syncs Shopify store pages including Shipping policy, Return policy, Privacy policy, Terms of service, FAQ, Contact us, and About us — no manual re-sync needed for these pages.

Data sources are the information you provide to train your AI assistant. The AI uses this data to give accurate, personalized responses about your products, services, and policies.

**Store data (auto-synced):**
- Products: descriptions, variants, pricing, availability, inventory status, metafields
- Discounts: all active and inactive discounts from Shopify
- Markets: market settings including currency and exchange rates
- FAQs: your existing FAQs in Chatty

**Custom data sources (manually added):**
- Questions (Q&A pairs)
- URLs (website links — content is scraped and indexed)
- Files (.JSON, .TXT, .PDF, .CSV — max 2MB for AI training data; images and PDFs with tables not yet supported)

**Auto-synced Shopify pages:** Shipping policy, Return policy, Privacy policy, Terms of service, FAQ, Contact us, About us. If not synced, go to **Data Sources** → **Sync store pages** or re-activate AI.

Product information updates daily at **12:00 AM PST**.

---

<!-- CHUNK: data-sources-add-manage -->
```yaml
chunk_id: "data-sources__add-manage"
doc_id: "chatty-data-sources"
title: "How to add and manage AI data sources"
category: "data-sources"
tags: ["add data source", "manage data", "sync products", "Q&A", "upload file", "add URL"]
applies_when: "Merchant wants to add data sources or manage their existing AI training data"
```

## Adding & Managing Data Sources

Go to **AI Assistant** → **Data Sources**.

**Sync store data:** Turn on auto-sync for products, discounts, markets, and FAQs.

**Add custom data:**
- **Questions** — add Q&A pairs (edit, change status Active/Inactive, delete, export to CSV)
- **URLs** — add website links; click **Resync** if content has changed; preview content in plain text
- **Files** — upload .JSON, .TXT, .PDF, or .CSV (max 2MB); edit or change status Active/Inactive

After adding data, go to **Test** to verify AI responds correctly. You can test AI even before activating it.

**Bulk management:** Click any data type to see the full list. Select multiple items for bulk actions: set as active, set as inactive, or delete.

---

<!-- CHUNK: data-sources-smart-recommendations -->
```yaml
chunk_id: "data-sources__smart-recommendations"
doc_id: "chatty-data-sources"
title: "Set up smart product recommendations for AI"
category: "data-sources"
tags: ["smart recommendations", "bestseller", "new arrival", "product recommendations", "AI recommendations"]
applies_when: "Merchant wants to set up smart product recommendations for the AI assistant"
```

## Smart Recommendations Setup

Tell AI which products to recommend in specific situations:

1. Click **Smart Recommendations** in Data Sources
2. Select a collection to manage
3. Set up product list and keywords
4. Click **Add product** to add items, **Delete** to remove
5. Click **Save** and activate the recommendation

**Categories:**
- **Bestseller** — AI suggests when customers ask "What's popular?"
- **New arrival** — AI suggests when customers ask "What's new?"
- **Sales promotion** — AI suggests when customers ask about discounts or deals
- **Special occasions** — AI suggests when customers ask about gifts or special events

**Smart syncing (auto):** By default, Chatty selects the top 20 products based on sales from the last 30 days and updates daily. Max 20 products per collection.

---

<!-- CHUNK: data-sources-manage-products -->
```yaml
chunk_id: "data-sources__manage-products"
doc_id: "chatty-data-sources"
title: "Enable or disable specific products from AI training"
category: "data-sources"
tags: ["enable products", "disable products", "product status", "product FAQ", "manage products"]
applies_when: "Merchant wants to enable or disable specific products from AI training data"
```

## Managing Individual Products

After syncing products:
1. Go to **Data Sources** → **Products** tab
2. Set each product's status to **Enabled** or **Disabled**

Only published, in-stock products work with Chatty. Product subscriptions are not supported.

**Add product-specific FAQs:**
1. Click **Products** tab
2. Click **Add FAQs** or **Manage FAQs** on a specific product


---

# Deep Links

<!-- CHUNK: deep-links-overview -->
```yaml
chunk_id: "faq__deep-links-overview"
doc_id: "chatty-deep-links"
title: "What deep links are and how to use them to open specific chatbox tabs"
category: "faq"
subcategory: "chatbox"
tags: ["deep links", "deep link", "open chatbox", "chatbox link", "order tracking link", "direct link", "chatbox tab"]
applies_when: "When a merchant asks how to create a link or button that opens the chatbox directly or opens a specific tab"
priority: "low"
```

## Deep Links Overview

Deep links are special URLs that, when clicked, automatically open your Chatty chatbox — or a specific tab within it (like Order tracking).

You can add a deep link to a button, navigation link, or any clickable element on your website.

## How to Create and Use a Deep Link

1. Go to **Chatbox** → Click **Advanced**
2. Copy the deep link for the section you want to open (e.g., the Order tracking deep link opens the order tracking tab)
3. Add the link to a button or text element on your website

**Example:** Add a "Track my order" button in your store navigation that opens the chatbox directly to the Order tracking tab.


---

---
category: Common Issues
topic: Email Channel Issues
source: notion/Chatty FAQs
---

Q: Emails from Hotmail and Outlook are not being forwarded to Chatty.
Q: Outlook/Hotmail email forwarding doesn't work with Chatty.
A: This is a known compatibility issue between Cloudflare and Microsoft's mail system.

**Workarounds:**
1. **Use an intermediate mailbox:** Set up a Gmail or other domain email to receive from Outlook/Hotmail, then forward to Chatty.
2. **Switch email hosting:** Consider Google Workspace or Zoho Mail for the domain email, then forward to Chatty.
3. **Enable alternative notifications:** Turn on email notifications via Gmail or install the Chatty mobile app to avoid missing messages.

Guide the merchant to test after setting up the workaround.

---

Q: Email forwarding is not getting verified even after adding the forwarding address.
Q: The merchant set up email forwarding but verification fails.
A: Common causes include incorrect forwarding address, email provider blocking automatic forwarding, or verification email going to spam.

**Support flow:**
1. Verify the forwarding address is entered correctly.
2. Ask the merchant to check spam/junk folder for the verification email.
3. If using Outlook/Hotmail, note the Cloudflare compatibility issue and suggest alternative email providers.
4. If the issue persists, check if the email sender configuration is blocking forwarding.

---

Q: The merchant can't verify email forwarding because of email sender issues.
Q: Email sender verification is failing in Chatty.
A: Check if the email provider requires SPF record configuration.

**Solution:**
1. Verify the merchant's email provider settings.
2. If SPF records need updating, guide the merchant to add the SPF record to their DNS settings — refer to their email provider's documentation for the exact record values.
3. Test again after DNS changes propagate (may take up to 48 hours).

---

Q: The merchant didn't receive the verification email when setting up email channel.
Q: Verification email for Chatty email setup never arrived.
A: Check these common causes:

1. **Spam/junk folder:** Ask the merchant to check spam and junk folders.
2. **Email provider blocking:** Some corporate email providers block automated verification emails.
3. **Incorrect email address:** Verify the email was entered correctly in settings.
4. If none of the above, try resending the verification email or use an alternative email address.

---

Q: Email notifications from Chatty are going to the spam box.
Q: Merchant's customers say Chatty emails land in spam.
A: This is typically caused by missing or incorrect email authentication records.

**Solution:**
1. Guide the merchant to add SPF records to their DNS settings for their email provider.
2. Verify DKIM and DMARC records are properly configured.
3. Recommend using a custom sender domain instead of the default noreply@chattyemail.com.
4. If the merchant uses a custom domain, verify the domain in Chatty settings.

---

Q: How do I add SPF records for Chatty email?
Q: Merchant needs to configure SPF for email delivery.
A: Guide the merchant to add SPF records in their DNS provider settings. This ensures emails sent through Chatty are authenticated and less likely to be flagged as spam.

The specific SPF record values depend on the merchant's email hosting provider. Refer to the email provider's documentation for exact configuration steps.

---

Q: The merchant wants to add alias emails to channels.
Q: Can I use multiple email addresses with Chatty?
A: Chatty supports connecting one email to the channel. For additional email addresses, the merchant can set up email forwarding from alias addresses to the connected Chatty email.

---

Q: Clicking the email icon in the Contact Us widget opens the wrong email client.
Q: The email button in the chatbox doesn't work correctly.
A: The email contact button behavior depends on the merchant's chatbox configuration and the customer's device default email client settings. Verify the email address is correctly set in the Contact Us block settings.

---

Q: Merchant gets "Fail to deliver" error emails.
Q: The merchant keeps receiving delivery failure notifications.
A: These errors typically occur when the recipient email is invalid or the email provider rejects the message. Verify the recipient email addresses and check email forwarding configuration for any issues.

---

Q: The merchant wants to transfer the admin email to a different address.
Q: How do I change the admin email for a Chatty account?
A: The admin email is tied to the Shopify store owner account. To change it:

1. Go to the Chatty app settings.
2. Check Team settings for the current admin email.
3. If the merchant needs to change the primary admin, they may need to update their Shopify store owner email first, then re-access Chatty.

---

Q: The forwarding email address is showing in the Reply-To field when customers reply to Chatty emails.
A: This happens when the Reply-To header is not configured correctly.

1. Go to **Chatty** → **Channels** → **Email**
2. Check the **Email sender** field — make sure it's set to your actual store support email, not the Chatty forwarding address
3. Save the changes and send a test reply to yourself to confirm the correct email appears in the Reply-To field.

---

Q: Can I receive messages from multiple email addresses in Chatty?
A: Currently, Chatty supports one email per store via forwarding. Contact support if you have specific needs around multiple email addresses or alias setups.

---

Q: When the AI replies to an email conversation, does the customer receive the response?
A: Yes — replies sent through Chatty (by AI or human agents) are delivered to the customer's email. The default sender address is noreply@chattyemail.com unless you have configured a custom sender domain.

---

Q: How can I use Klaviyo to send outreach emails and have Chatty handle the replies?
A: Set up your Klaviyo campaign with a **Reply-To** address that is connected to a Chatty email channel. When leads reply to the email, their response will appear in Chatty's inbox as a new conversation, where AI or your team can take over.

---

# Embedded Chatbox

<!-- CHUNK: embedded-chatbox-overview -->
```yaml
chunk_id: "faq__embedded-chatbox-overview"
doc_id: "chatty-embedded-chatbox"
title: "What the embedded chatbox is and how it differs from the floating chatbox"
category: "faq"
subcategory: "chatbox"
tags: ["embedded chatbox", "inline chatbox", "floating chatbox", "chatbox on page", "contact page chatbox", "embedded chat widget"]
applies_when: "When a merchant asks about the embedded chatbox, how to add it to a page, or the difference between floating and embedded chatbox"
priority: "medium"
```

## Embedded Chatbox Overview

The embedded chatbox lets you add the full chatbox interface as a section directly on a specific page — instead of the floating popup button. Customers can chat without clicking anything to open a window.

| | Floating chatbox | Embedded chatbox |
|---|---|---|
| Display | Button that opens an overlay | Full interface built into the page |
| Visibility | Available on all pages | Only on pages where you add it |
| Space usage | Floats over content | Takes up section space on the page |
| Best for | Store-wide availability | Dedicated contact or support pages |

You can use both floating and embedded chatbox together — for example, have the floating chat everywhere plus an embedded one on your Contact page.

## How to Add the Embedded Chatbox

1. Go to **Chatbox** → **Advanced** tab → Find **Embedded chatbox**
2. Click **Go to theme**
3. In the theme editor, choose where to add the chatbox
4. Click **Add section**
5. Click **Save**


---

# FAQs Analytics

<!-- CHUNK: faqs-analytics-overview -->
```yaml
chunk_id: "faq__faqs-analytics-overview"
doc_id: "chatty-faqs-analytics"
title: "How to track FAQ views and engagement in Chatty"
category: "faq"
subcategory: "build-faqs"
tags: ["faq analytics", "faq views", "faq engagement", "faq performance", "which faqs are popular", "track faq"]
applies_when: "When a merchant asks how to see which FAQs are being read or how to track FAQ engagement"
priority: "low"
```

## FAQs Analytics Overview

FAQs analytics is available to all Chatty users. It shows how often customers view and interact with your FAQ content.

**What counts as a view:** Each time a user clicks to expand and read the answer to a question — on the FAQs page, in a FAQs block, or inside the chatbox.

## How to Check FAQ Analytics

- Go to **FAQs** → Check the total views displayed next to each question
- Go to **Dashboard** → Check the FAQs overview section, where you can filter by time range

Use this data to identify which questions are most popular and which ones might need better answers or more visibility.


---

# FAQs Block

<!-- CHUNK: faqs-block-overview -->
```yaml
chunk_id: "faq__faqs-block-overview"
doc_id: "chatty-faqs-block"
title: "What a FAQs block is and how to set one up on specific pages"
category: "faq"
subcategory: "build-faqs"
tags: ["faq block", "faqs block", "product page faq", "page-specific faq", "add faq to page", "faq section", "theme editor faq"]
applies_when: "When a merchant asks how to show FAQs on a specific page or how to create a FAQs block"
priority: "medium"
```

## FAQs Block Overview

A FAQs block lets you display a specific set of FAQs on any page of your store — for example, showing product-specific questions only on the relevant product page.

You can create multiple FAQs blocks with different questions for different products, collections, or pages.

## How to Set Up a FAQs Block

1. Go to **FAQs** → **FAQs block**
2. Set **General** information:
   - **Block name**: Internal name to identify this block (visible to admin only)
   - **Heading & Subheading**: Text shown in the block
3. Click **Browse** and select the FAQ questions to show
   - Turn on "Don't categorize FAQs" to show all questions in a flat list without category headers
4. Set display condition — choose where to show the block:
   - All pages
   - Specific product pages
   - All product pages of a collection
5. Customize appearance:
   - Heading size and alignment
   - Card corner radius
   - Colors
6. Click **Save**
7. Copy the **Block ID**
8. Go to your **Theme editor**:
   - Navigate to the page where you want to add the block
   - Click **Add section** → Search for **Chatty FAQs block** → Add it
   - Paste the Block ID in the settings
9. Click **Save** in the theme editor

You can also add the block using code: Go to **FAQs block code** → **Copy** → Add the HTML to your website's code.

---

<!-- CHUNK: faqs-block-manage -->
```yaml
chunk_id: "faq__faqs-block-manage"
doc_id: "chatty-faqs-block"
title: "How many FAQs blocks can be created and how to reuse FAQs across blocks"
category: "faq"
subcategory: "build-faqs"
tags: ["faq block limit", "multiple faq blocks", "reuse faq", "faq block management", "block id"]
applies_when: "When a merchant asks how many FAQs blocks they can create or whether the same FAQ can appear in multiple blocks"
priority: "low"
```

## Managing FAQs Blocks

In the FAQs block tab, you can:
- View all blocks with details (Block ID, name, number of FAQs, display conditions, status)
- Edit or delete blocks
- Create as many blocks as needed — **there's no limit**

There is no limit on the number of FAQs blocks you can create. Create separate blocks for each product or collection as needed.

To reuse the same FAQ in multiple blocks, include it when selecting questions for each block you create. The same FAQ question can appear in multiple blocks by using the same Block ID.


---

# FAQs Page

<!-- CHUNK: faqs-page-setup -->
```yaml
chunk_id: "faq__faqs-page-setup"
doc_id: "chatty-faqs-page"
title: "How to create and customize a dedicated FAQs page in Chatty"
category: "faq"
subcategory: "build-faqs"
tags: ["faq page", "dedicated faq page", "faq page setup", "faq page design", "faq page appearance", "contact us section", "custom css faq"]
applies_when: "When a merchant asks how to create a FAQ page, customize it, or add a Contact us section to it"
priority: "medium"
```

## FAQs Page Overview

The FAQs page is a dedicated page on your Shopify store where customers can browse and find answers without contacting support.

## How to Set Up the FAQs Page

1. In FAQs, go to **FAQ page**
2. Turn on **Display FAQs page**
3. Set up a URL for the page
4. Set up appearance:
   - Select layout
   - Set colors for title, questions, background, etc.
   - Tip: Make sure text and background colors have sufficient contrast. You can check contrast at https://coolors.co/contrast-checker
5. Set up the header:
   - Customize the heading and description text

## Set Up the Contact Us Section

The Contact us section on the FAQs page lets customers reach your team when they need more help.

1. Turn on **Display contact us**
2. Set up Heading and Description
3. Configure click behavior: what happens when customers click "Contact us"

## Advanced Settings

- **Branding removal**: Remove Chatty branding from the FAQs page
- **Custom CSS**: Add custom styling to match your store's design. Requires coding knowledge. Contact support via live chat in the app if you need help.

---

<!-- CHUNK: faqs-page-navigation -->
```yaml
chunk_id: "faq__faqs-page-navigation"
doc_id: "chatty-faqs-page"
title: "How to add the FAQs page to Shopify store navigation"
category: "faq"
subcategory: "build-faqs"
tags: ["faq page menu", "faq navigation", "add faq to menu", "main menu faq", "footer menu faq", "shopify menu"]
applies_when: "When a merchant asks how to add the FAQ page to their store's navigation menu"
priority: "low"
```

## How to Add the FAQs Page to Your Store Navigation

**Main menu:**
1. In Shopify admin, go to **Content** → **Menus** → **Main menu**
2. Click **Add menu item**
3. Name it (e.g., "FAQs")
4. In the link box, search for "Frequently Asked Questions" or paste your custom URL
5. Click **Add** → **Save menu**

**Footer menu:**
Follow the same steps using **Footer menu** instead of Main menu.


---

# General Settings

<!-- CHUNK: general-settings-store-profile -->
```yaml
chunk_id: "faq__general-settings-store-profile"
doc_id: "chatty-general-settings"
title: "How to update store name, avatar, and profile settings in Chatty"
category: "faq"
subcategory: "settings"
tags: ["store name", "avatar", "store profile", "general settings", "change avatar", "update store info"]
applies_when: "When a merchant asks how to change their store name, avatar, or general settings in Chatty"
priority: "low"
```

## Change Store Name and Avatar

1. Go to **Settings**
2. In General, click **Manage**
3. Update your store name and avatar
4. Click **Save**

Your avatar can be a custom uploaded image. Supported formats: .gif, .jpg, .png — max size 200KB.

---

<!-- CHUNK: general-settings-disclaimer -->
```yaml
chunk_id: "faq__general-settings-disclaimer"
doc_id: "chatty-general-settings"
title: "How to set up disclaimer consent and follow-up email in Chatty"
category: "faq"
subcategory: "settings"
tags: ["disclaimer consent", "privacy policy link", "follow-up email", "email consent", "data consent", "continue on email"]
applies_when: "When a merchant asks about the disclaimer consent setting or follow-up email feature"
priority: "medium"
```

## Disclaimer Consent

Disclaimer consent adds your privacy policy link under the email collection form in conversations. This informs customers how their data is used before they start chatting or subscribe.

1. Go to **Settings**
2. In General, click **Manage**
3. Set up your disclaimer consent message and privacy policy link

## Follow-Up Email

This helps customers continue a conversation by email instead of live chat.

Turn on this setting. Customers will see a "Continue on email" option in the chatbox, letting them keep the conversation going via their email.


---

---
category: CS Process
topic: Handling Sensitive Situations
source: cs-process/tinh-huong-nhay-cam
---

Q: A customer is asking for my personal information (social media, phone number). What should I do?
Q: How do I handle a merchant requesting personal details?
A: Never share personal information. Follow this escalation approach:

**1. Politely decline and redirect to app support:**
"Sorry, I can't share personal information. If you need help with the app, I'll be happy to assist."

**2. If they ask again, be firm:**
"As I mentioned, I cannot share personal information. Please keep the conversation related to the app."
"I can only respond to questions related to the app. Let's please keep the conversation focused on that."

**3. If they persist, end the conversation:**
"I can only support with the app. If you need help with the app later, please feel free to reach out again."
Then close the chat.

Q: A customer is using sexually harassing or seriously offensive language toward me. What should I do?
Q: How do I handle harassment or abusive language from a merchant?
A: This process applies when the customer is harassing or personally insulting the CS agent and there is no actual app/service issue. Follow these steps:

**1. Remind them to be respectful:**
"Your message is inappropriate. Please keep the conversation respectful so I can assist you."

**2. Warn if it continues:**
"This kind of language is not acceptable. If it continues, I will need to end this conversation."

**3. End and report:**
"I'm ending this chat due to repeated inappropriate language. If you need help with the app in the future, please contact us respectfully."

**Note:** In cases of sexual harassment, a female CS agent may transfer the case to a male colleague as a temporary measure. However, no one is required to continue supporting a harassing customer — always follow the warn → end chat flow if behavior is serious.

Q: A customer is spamming or repeatedly asking the same question. How should I handle the response pace?
Q: Do I need to reply immediately when a customer is spamming?
A: No, you do not need to reply immediately to spam or repeated personal questions. You can:

- **Slow down your response by 2–3 minutes** to reduce the conversation pace. This subtly signals that these are not priority questions.
- Reply with a short, consistent script — no need to change your reasoning each time.
- After 1–2 slow reminders, if they still persist → **warn and end the chat**.

Q: When can I block a customer after warnings, and when should I escalate?
Q: What's the difference between handling a dev store vs a real store for blocking?
A: It depends on whether it's a dev store or a real store:

**Dev store** (check CRM — cannot write reviews, no retention value):
- CS has the authority to **block immediately** after warning.
- Note the reason for blocking in the chat.
- Inform your leader for awareness.

**Real store** (can write reviews):
- CS should **report to the CS Leader** and let them decide the next steps.
- Do not block on your own — escalate first.

Q: What are the general principles for handling sensitive situations?
Q: What rules should I always follow when dealing with difficult or inappropriate customers?
A: Follow these core principles:

1. **Never reveal personal information** — keep all interactions professional and app-focused.
2. **Stay professional** — do not argue, do not respond to insults with insults.
3. **Give 2–3 reminders** → then warn and end the chat if behavior continues.
4. **When customers spam** → slow down your replies to reduce the conversation pace.
5. **Dev stores** → CS can block on their own after warning.
6. **Real stores** → always report to the CS Leader for further handling.


---

# Inbox and Conversation Issues

<!-- CHUNK: inbox-conversation-export -->
```yaml
chunk_id: "faq__inbox-conversation-export"
doc_id: "chatty-inbox-conversation-issues"
title: "How to export conversations from the Chatty inbox"
category: "faq"
subcategory: "inbox"
tags: ["export conversations", "download chat history", "conversation export", "inbox export", "plan limit"]
applies_when: "When a merchant asks how to export or download conversation history from Chatty"
priority: "medium"
```

## Exporting Conversations from the Inbox

Conversation export functionality may be limited depending on the plan. Check the merchant's current plan and available export options in the Inbox section.

If the feature is not available on their plan, they can upgrade or use alternative approaches (e.g., screenshots, manual copy).

---

<!-- CHUNK: inbox-conversation-anonymous -->
```yaml
chunk_id: "faq__inbox-conversation-anonymous"
doc_id: "chatty-inbox-conversation-issues"
title: "Why anonymous conversations appear even with pre-chat form enabled"
category: "faq"
subcategory: "inbox"
tags: ["anonymous conversations", "pre-chat form bypass", "chat as guest", "AI product page assistant", "proactive chat anonymous"]
applies_when: "When a merchant sees anonymous conversations even though they set up Chat as guest / pre-chat form"
priority: "medium"
```

## Anonymous Conversations with Pre-Chat Form Enabled

Two features can bypass the pre-chat form:

1. **AI Product Page Assistant:** When embedded on product pages, customers can chat immediately without providing email. The system prioritizes fast support.

2. **Proactive Chat:** When enabled, customers can reply to the proactive chat bubble without filling the pre-chat form first.

**Solution:** If you want to enforce info collection for all conversations, disable the AI Product Page Assistant embed and/or Proactive Chat features.

---

<!-- CHUNK: inbox-conversation-misc -->
```yaml
chunk_id: "faq__inbox-conversation-misc"
doc_id: "chatty-inbox-conversation-issues"
title: "Last activity calculation and managing chats across multiple stores"
category: "faq"
subcategory: "inbox"
tags: ["last activity", "inbox timestamp", "multiple stores", "multi-store inbox", "switch stores", "conversation timestamp"]
applies_when: "When a merchant asks about last activity timestamps or managing conversations across multiple Shopify stores"
priority: "low"
```

## How "Last Activity" Time Is Calculated

Last Activity shows the timestamp of the most recent message or action in a conversation. This includes messages from both the customer and the agent/AI, as well as system events like transfers.

## Managing Chats Across Multiple Stores

Each Shopify store has its own separate Chatty installation and inbox. Conversations from different stores cannot be merged into a single inbox.

Team members who work across multiple stores can be invited to each store's Chatty and switch between them via Shopify Admin or app.meetchatty.com.


---

# Inbox

<!-- CHUNK: inbox-overview -->
```yaml
chunk_id: "inbox__overview"
doc_id: "chatty-inbox"
title: "Chatty inbox overview — managing conversations"
category: "inbox"
tags: ["inbox", "conversations", "manage", "reply", "live chat", "WhatsApp", "Messenger", "email"]
applies_when: "Merchant asks about the inbox, how to reply to customers, or how to manage conversations"
```

## Chatty Inbox Overview

The Inbox is your central hub for managing all customer conversations across all connected channels — live chat, email, Facebook Messenger, Instagram, WhatsApp — in one place.

**Access inbox:** Go to Chatty in Shopify admin → click the **Inbox** tab.

**Reply to a conversation:**
1. Select a conversation from the list
2. Click the message input field at the bottom
3. Type your message → press **Enter** or click **Send**

For AI-assigned conversations: click **Join conversation** to start responding. You can reassign to AI anytime for auto-reply to resume.

**Filter conversations by:**
- Status: Open, Resolved, Starred, Blocked, Unread
- Channel: Online store, Live chat, Email, Messenger, Instagram, WhatsApp
- Assignee: Your inbox, Unassigned, or a specific team member

**While chatting you can see:**
- Contact info, order history, customer tags and notes
- Pages they've browsed
- Real-time behaviors: viewing FAQs, adding/removing products from cart, placing an order

---

<!-- CHUNK: inbox-anonymous-names -->
```yaml
chunk_id: "inbox__anonymous-names"
doc_id: "chatty-inbox"
title: "Anonymous users showing random names in inbox"
category: "inbox"
tags: ["anonymous", "random name", "anonymous user", "visitor name", "unknown user"]
applies_when: "Anonymous visitors are showing random names instead of 'Anonymous user' in the inbox"
```

## Anonymous Users Showing Random Names

This is a feature request currently under review. As a workaround, filter your inbox by segment to identify anonymous contacts.

The team is considering formats like "Anonymous user" or "Anonymous #1SG8" (with unique suffix). You will be notified once implemented.

---

<!-- CHUNK: inbox-blocked-customers -->
```yaml
chunk_id: "inbox__blocked-customers"
doc_id: "chatty-inbox"
title: "Blocked customers keep starting new conversations"
category: "inbox"
tags: ["blocked", "blacklist", "persistent block", "spam customer", "block visitor"]
applies_when: "Blocked customers keep starting new conversations after being blocked"
```

## Blocked Customers Starting New Conversations

Blocking in Chatty is currently **session-based** and does not permanently prevent a visitor from starting a new conversation.

For more persistent control:
- Block by IP address (if your store platform supports this)
- Use **Shopify customer tags** to flag or manage abusive customers

The dev team is researching improvements to this feature.

---

<!-- CHUNK: inbox-block-by-country -->
```yaml
chunk_id: "inbox__block-by-country"
doc_id: "chatty-inbox"
title: "Block visitors from a specific country"
category: "inbox"
tags: ["block country", "country block", "geolocation", "restrict country", "geo blocking"]
applies_when: "Merchant wants to block all visitors from a specific country from using the chatbox"
```

## Blocking Visitors by Country

Chatty doesn't currently support blocking all visitors from a specific country at once.

You can block individual visitors — open the conversation, click on the visitor profile, and select **Block**.

For country-level restrictions, consider using **Shopify's geo-blocking features** or a third-party geolocation app.

---

<!-- CHUNK: inbox-reassign-to-ai -->
```yaml
chunk_id: "inbox__reassign-to-ai"
doc_id: "chatty-inbox"
title: "Reassign a conversation back to the AI assistant"
category: "inbox"
tags: ["reassign", "back to AI", "AI assistant", "handover to AI", "auto-reply resume"]
applies_when: "Merchant wants to reassign a conversation from a human agent back to the AI assistant"
```

## Reassigning Conversation Back to AI

In the Inbox, open the conversation and look for the assign/reassign option — select the **AI assistant** as the assignee.

Note: the customer must send a **new message** after reassignment for the AI to start handling the conversation again.

---

<!-- CHUNK: inbox-reply-as-self -->
```yaml
chunk_id: "inbox__reply-as-self"
doc_id: "chatty-inbox"
title: "Reply as yourself instead of admin in Chatty inbox"
category: "inbox"
tags: ["reply as self", "agent name", "admin name", "team member name", "assigned to admin"]
applies_when: "Replies are showing as 'Admin' instead of the agent's name, or merchant wants agents to reply under their own name"
```

## Replying as Yourself (Not as Admin)

Each team member should log in with their own Chatty account.

If replies are showing as "Admin," check **Settings** → **Automation** — the assignment rule may be keeping conversations assigned to the admin. Change the setting to **"Assign to whoever replies"** to resolve this.

---

<!-- CHUNK: inbox-multi-store -->
```yaml
chunk_id: "inbox__multi-store"
doc_id: "chatty-inbox"
title: "Managing chats from multiple Shopify stores in one Chatty account"
category: "inbox"
tags: ["multiple stores", "multi-store", "unified inbox", "two stores", "store management"]
applies_when: "Merchant asks if they can manage conversations from multiple Shopify stores in one Chatty account"
```

## Multiple Shopify Stores

No — each Shopify store has its own separate Chatty app instance. You would need to log into each store's Chatty separately. There is no multi-store unified inbox at this time.

---

<!-- CHUNK: inbox-mark-all-read -->
```yaml
chunk_id: "inbox__mark-all-read"
doc_id: "chatty-inbox"
title: "Mark all messages as read at once"
category: "inbox"
tags: ["mark all read", "unread", "read all", "bulk read", "mass read"]
applies_when: "Merchant wants to mark all conversations or messages as read at once"
```

## Mark All as Read

A "Mark all as read" feature is **not available yet**. This has been submitted as a feature request to the product team.

---

<!-- CHUNK: inbox-export-history -->
```yaml
chunk_id: "inbox__export-history"
doc_id: "chatty-inbox"
title: "Export conversation history from Chatty"
category: "inbox"
tags: ["export", "export history", "download conversations", "CSV export", "conversation export"]
applies_when: "Merchant wants to export their conversation history from Chatty"
```

## Exporting Conversation History

Chatty does not currently support self-serve conversation export with date range filters from the app UI.

Contact support and provide the date range — the team can export data as a CSV/JSON file and send it to your email. For large exports, allow 2–3 business days.

---

<!-- CHUNK: inbox-api -->
```yaml
chunk_id: "inbox__api"
doc_id: "chatty-inbox"
title: "Save chat history via API"
category: "inbox"
tags: ["API", "chat history API", "public API", "save history", "Zendesk integration"]
applies_when: "Merchant asks about saving or accessing chat history via Chatty's API"
```

## Chat History via API

The Chatty Public API does not currently support saving chat history via API endpoint.

However, if you integrate with **Zendesk**, all Chatty conversations are automatically saved as Zendesk tickets when marked as resolved. The support team can also manually export transcripts.

---

<!-- CHUNK: inbox-star-icon -->
```yaml
chunk_id: "inbox__star-icon"
doc_id: "chatty-inbox"
title: "What the AI star icon on a conversation means"
category: "inbox"
tags: ["star icon", "AI icon", "star", "conversation icon", "AI handling", "inbox icon"]
applies_when: "Merchant asks what the star icon on a conversation in the Inbox means"
```

## Star Icon on Conversations

The **star icon** on a conversation indicates that the conversation is currently being handled by the **AI assistant**.


---

# Joy Loyalty Integration

<!-- CHUNK: joy-integration-overview -->
```yaml
chunk_id: "faq__joy-integration-overview"
doc_id: "chatty-joy"
title: "How to integrate Joy Loyalty with Chatty to see loyalty data in the inbox"
category: "faq"
subcategory: "integrations"
tags: ["joy", "joy loyalty", "loyalty points", "VIP tier", "rewards program", "loyalty integration", "customer loyalty"]
applies_when: "When a merchant asks how to integrate Joy Rewards with Chatty or how to see loyalty data in conversations"
priority: "medium"
```

## Joy Loyalty Integration Overview

Joy is a Shopify loyalty app offering rewards programs, points, VIP tiers, and referrals. By integrating Chatty with Joy, you can see customers' loyalty profiles directly inside Chatty — while you're chatting with them.

## What You Can See After Integrating

- Customer type (member, VIP, etc.)
- VIP tier
- Points balance
- Birthday
- Referral link

This information appears in:
- Customer details in Contacts
- Conversation details panel in Inbox

## How to Integrate

1. Go to **Settings** → **Integrations**
2. Find "Joy" → Click **Manage**
3. **Step 1**: Click **Go to Joy** and install the Joy app (skip if already installed)
4. **Step 2**: Click **Connect** to enable loyalty data sync between Joy and Chatty

After integrating, Joy loyalty info appears automatically in Customer details and Conversation details.


---

# Klaviyo & Integrations

<!-- CHUNK: klaviyo-connect -->
```yaml
chunk_id: "klaviyo__connect"
doc_id: "chatty-klaviyo"
title: "How to connect Klaviyo to Chatty"
category: "klaviyo"
tags: ["Klaviyo", "connect Klaviyo", "Klaviyo integration", "API key", "setup Klaviyo"]
applies_when: "Merchant wants to connect Klaviyo to Chatty or asks how to integrate them"
```

## Connecting Klaviyo to Chatty

**What gets synced to Klaviyo:**
- Contact information (name, email, phone, location, customer type)
- Tags
- Number of conversations
- Last chat timestamps

**How to integrate:**
1. Go to **Settings** → **Integrations** → Find Klaviyo → Click **Manage**
2. Click **Go to Klaviyo** and install the app (skip if already installed)
3. Enter your Klaviyo API key → Click **Connect**

**How to get your Klaviyo API key:**
1. Log in to Klaviyo → click your profile (bottom left) → **Settings**
2. Go to **API keys** → **Create Private API key**
3. Name it (e.g., "Chatty integration")
4. Select **Custom key** as the Access Level
5. In API scopes, enable **Read/Write Access** for: Lists and Profiles
6. Click **Create** → copy the key → paste into Chatty

---

<!-- CHUNK: klaviyo-hubspot -->
```yaml
chunk_id: "klaviyo__hubspot"
doc_id: "chatty-klaviyo"
title: "Does Chatty integrate with HubSpot"
category: "klaviyo"
tags: ["HubSpot", "CRM", "HubSpot integration", "Zapier", "custom integration"]
applies_when: "Merchant asks if Chatty integrates with HubSpot"
```

## HubSpot Integration

A direct native HubSpot integration is **not available yet**. You can use the Chatty Public API with a custom setup or tools like Zapier to sync data to HubSpot. The product team has noted this as a potential future integration.

---

<!-- CHUNK: klaviyo-public-api -->
```yaml
chunk_id: "klaviyo__public-api"
doc_id: "chatty-klaviyo"
title: "Does Chatty have a public API"
category: "klaviyo"
tags: ["public API", "API", "Chatty API", "custom integration", "developer", "API access"]
applies_when: "Merchant asks if Chatty has a public API for custom integrations"
```

## Chatty Public API

Yes — the Chatty Public API provides access to your store's customer data (contacts, chat history timestamps, order counts, total spend). It's primarily for custom integrations: syncing contacts to a CRM, pulling data into spreadsheets, or building internal dashboards.

See: https://help.chatty.net/integrations/chatty-public-api

---

<!-- CHUNK: klaviyo-whatsapp-api -->
```yaml
chunk_id: "klaviyo__whatsapp-api"
doc_id: "chatty-klaviyo"
title: "Connect Chatty to existing WhatsApp support system via API"
category: "klaviyo"
tags: ["WhatsApp API", "custom integration", "API", "WhatsApp integration", "custom WhatsApp"]
applies_when: "Merchant wants to connect Chatty to an existing WhatsApp support system via API"
```

## Custom WhatsApp Integration via API

The Chatty Public API provides data access but does not offer a full WhatsApp messaging API integration out of the box. For deep custom integrations, development work on your side would be needed. Contact support to discuss your use case.

---

<!-- CHUNK: klaviyo-size-guide -->
```yaml
chunk_id: "klaviyo__size-guide"
doc_id: "chatty-klaviyo"
title: "Size guide AI skill in Chatty"
category: "klaviyo"
tags: ["size guide", "AI skill", "size recommendation", "Pro plan", "sizing"]
applies_when: "Merchant asks about adding a size guide for AI training"
```

## Size Guide AI Skill

Available on **Pro plan and above**. Go to **AI Assistant** → **Train AI** → **AI Skills** → **Size Guide** to configure.

For Free/Basic plans, try uploading a size guide as a file (Excel/CSV) to Custom Knowledge — though this is less reliable for complex sizing logic than the dedicated feature.


---

# Chatty — Knowledge Base

## Product Overview

Chatty is a Shopify app that helps merchants communicate with store visitors via live chat, automate customer support with an AI chatbot (powered by ChatGPT), and build self-serve FAQ help centers. Chatty is designed as an AI-first chat platform specifically for eCommerce stores, turning customer conversations into sales opportunities.

Built for Shopify badge. Available on Shopify App Store. 4.9 stars with 1,700+ reviews.

## Plans

| Feature | Free | Basic ($19.99/mo) | Pro ($68.99/mo) | Plus ($199.99/mo) |
|---------|------|--------------------|------------------|---------------------|
| AI conversations | 50 lifetime | 50/month | 300/month | 700/month |
| Additional conversations | N/A | $0.40 each | $0.40 each | $0.40 each |
| Products for AI training | 100 | 500 | 8,000 | 20,000 |
| Team members | 1 | 5 | 10 | Unlimited |
| Auto-translation languages | 1 | 2 | 9 | Unlimited |
| Chat history | 90 days | Unlimited | Unlimited | Unlimited |
| Email channel | 1 | 1 | 1 | 1 |
| Smart product recommendations | No | No | Yes | Yes |
| CSAT survey | No | No | Yes | Yes |
| Cart booster | No | No | Yes | Yes |
| Dedicated AI consultant | No | No | No | Yes |

Annual billing: ~15% savings. 7-day free trial for paid plans. 30-day money-back guarantee.

## Core Features

### Live Chat
Real-time messaging between merchants and store visitors. Key capabilities:
- **Inbox**: Unified inbox to manage all conversations. Includes customer details panel, conversation details, chat zone with rich text editor.
- **Channels**: Email, Facebook Messenger, Instagram, WhatsApp — all synced into one inbox.
- **Contacts**: Customer management with tags, notes, and conversation history.
- **Team**: Invite team members, assign roles, manage conversation assignments.
- **Quick Replies**: Pre-saved response templates for faster replies.
- **Proactive Chat**: Behavior-triggered messages to engage visitors (e.g., time on page, specific page visit).
- **Real-time Translation**: Auto-translate messages between merchant and customer languages.

### AI Assistant
AI-powered chatbot that handles customer questions 24/7, trained on the merchant's store data:
- **AI Conversations**: Automatic responses to customer questions. AI shows as assignee in conversation details. Team can join AI conversations at any time.
- **Chat Summary**: When conversation transfers to human, AI summarizes the full conversation with language detection, issue highlights, and response suggestions.
- **Data Sources**:
  - *Store data* (auto-synced): Products (name, description, variants, pricing, inventory, metafields), discounts, markets, FAQs, policies (shipping, return, privacy, terms).
  - *Custom data* (manual): Individual questions, URLs/websites, files (.JSON, .TXT, .PDF, .CSV — max 2MB).
  - Products sync daily at 12:00 AM PST. Only published, in-stock products are trained.
- **AI Skills**:
  - *Shopping skills*: Smart recommendations (bestsellers, new arrivals, sales, special occasions — auto top 20 by sales, updated daily), size guide (upload images, per-product assignment), inventory status.
  - *Customer support skills*: Transfer to human, refund/return form, order tracking in chat.
- **AI Settings**: Bot name, avatar, welcome message, custom instructions (tone, response style, specific scenarios), AI availability (based on team online hours), AI channels.
- **Test & Optimize**: Test zone to preview AI responses before going live. Review unresolved questions to improve training.

### Chatbox
The chat widget displayed on the merchant's storefront:
- **General**: Turn on/off chatbox, enable chat focus mode, set header (logo, heading, description), configure blocks (Contact us, Order tracking, FAQs, Categories).
- **Appearance**: Brand colors (preset or custom), chatbox button (launcher icon, size, alignment), chatbox style (navigation mode, mobile ratio).
- **Advanced**: Deep links (open specific chatbox sections via URL), display rules (devices, pages), continue-as-email, custom CSS.
- **Contact Button**: Add contact methods — supports 11 methods: WhatsApp, Messenger, Phone, Email, Instagram, Telegram, Skype, Line, Zalo, TikTok, SMS.
- **Embedded Chatbox**: Embed chatbox directly in page content instead of floating widget.

### FAQ Builder
Build a self-serve knowledge hub:
- **Categories**: Organize questions into categories with icons and descriptions.
- **Questions**: Add questions with rich text answers, assign to categories.
- **FAQs Page**: Dedicated FAQ page on the storefront with customizable theme.
- **FAQs Block**: Show selected FAQs inside the chatbox.
- **FAQs Analytics**: Track views, clicks, and search queries.
- **Export**: Export questions as CSV file.
- **Translation**: Translate FAQs into multiple languages.

### Order Tracking
Customers can track orders directly in the chatbox. Supports Shopify order tracking and third-party tracking integrations.

### Mobile & Web App
- **Mobile App**: Manage conversations on the go (iOS/Android). Receive push notifications for new messages.
- **Web App**: Browser-based admin dashboard at app.chatty.net.

### Integrations
- **Klaviyo**: Sync customer data (contacts, tags, conversation counts, timestamps) to Klaviyo for targeted email/SMS campaigns. Requires Klaviyo API key with Read/Write access for Lists and Profiles.
- **Zendesk**: Connect Zendesk for unified helpdesk management.
- **Joy Loyalty**: Show loyalty data (points, tier) in customer conversations.
- **Air Reviews**: Connect product reviews for AI training context.
- **Powerful Contact Form**: Integrate contact form submissions.
- **Website**: Connect external website for AI data training.

### Notifications
Configure notification preferences for new messages, assignments, and other events.

### Analytics
Track conversation metrics, AI performance, response times, and customer satisfaction.

### Online Hours
Set business hours to control online/offline status. Affects chatbox display and AI availability settings.

### Translation
Translate app interface and FAQs into multiple languages. Number of languages depends on plan.

### General Settings
App-wide configuration: branding, defaults, display preferences.

## Channel Details

### Email Channel
- Connect one email to Chatty via email forwarding.
- Default sender: noreply@chattyemail.com (customizable with domain verification).
- "Continue as email" feature lets customers switch from live chat to email.
- Conversation history sent to customer when ticket is marked solved.

### Facebook Messenger & Instagram
- Connect via Facebook account — link fanpages to sync messages.
- Messages appear in Chatty inbox with platform icon indicators.
- Disconnecting doesn't remove existing conversations.

### WhatsApp
- Connect multiple WhatsApp accounts.
- Requires: Business Facebook page, WhatsApp Business account linked to that page, admin access to both.

## Key Terminology

| Term | Meaning |
|------|---------|
| AI conversation | A customer chat handled by AI assistant |
| Transfer | When AI hands off conversation to a human agent |
| Data source | Information used to train the AI (products, FAQs, custom data) |
| AI skill | Specialized capability for AI (recommendations, size guide, etc.) |
| Chatbox | The chat widget displayed on the storefront |
| Deep link | URL that opens a specific chatbox section directly |
| Proactive chat | Automated messages triggered by visitor behavior |
| Quick reply | Pre-saved response template for faster messaging |
| Contact button | Floating button with multiple contact method options |
| CSAT | Customer Satisfaction survey (Pro+ plans) |
| Smart recommendations | AI-powered product suggestions based on collections |

## Common Issues

- **Chatbox not showing on store**: Check if chatbox is turned on (Chatbox > General > Turn on), app embed is enabled in Shopify theme editor, and display rules (devices/pages) aren't excluding the page.
- **AI not responding**: Verify AI assistant is turned on, live chat block is enabled in chatbox, data sources are synced, and AI has been trained on sufficient data.
- **Email channel not connecting (Outlook)**: Organization's Outlook settings may block automatic email forwarding. Contact IT admin to allow email forwarding.
- **Online status not showing**: Contact Us block must be enabled. Go to Chatbox > General > Blocks > turn on "Contact us".
- **WhatsApp not connecting**: Ensure you have a Business Facebook page, WhatsApp Business account linked to it, and admin access to both accounts.
- **Translation not showing on store**: Website must support the language first. In Shopify Admin > Settings > Languages, add and publish the language before enabling it in Chatty.
- **AI recommending wrong products**: Check Smart Recommendations collections in AI Skills. Disable smart sync if auto-selected products aren't relevant. Manually curate product lists.
- **FAQ page not showing after uninstall/reinstall**: After uninstalling, Chatty's code may remain disabled. Check Shopify Admin > Online Store > Pages for orphaned FAQ pages.
- **Order tracking not working**: Ensure Order Tracking block is enabled in chatbox. Verify Shopify order tracking info is properly set up.
- **Products not appearing in AI training**: Only published, in-stock products are trained. Products sync daily at 12:00 AM PST. Check product count against plan limit.

## Privacy & Compliance

- **AI Compliance**: Chatty's AI follows data privacy standards. Customer conversation data is used only for AI training within the merchant's store scope.
- **Cookie Policy**: Chatty uses cookies for session management and chatbox functionality.
- **Data Access**: App accesses customer data (names, emails, addresses, browsing behavior), store owner info, product catalogs, orders, and discounts to function.

---

# Live Chat

<!-- CHUNK: live-chat-setup -->
```yaml
chunk_id: "faq__live-chat-setup"
doc_id: "chatty-live-chat"
title: "How to enable and configure live chat in Chatty"
category: "faq"
subcategory: "live-chat"
tags: ["live chat", "enable live chat", "pre-chat form", "anonymous chat", "chat setup", "chatbox live chat"]
applies_when: "When a merchant asks how to set up or enable live chat on their Shopify store"
priority: "high"
```

## Live Chat Overview

Live chat lets customers contact you directly while browsing your store. You can respond in real time and manage all conversations from the Chatty inbox.

## How to Enable Live Chat

1. Make sure the Chatbox is turned on: Go to **Chatbox** → In "General", click **Turn on** chatbox
2. In "Blocks", turn on **Live chat**
3. Click **Edit** to configure the pre-chat form

**Pre-chat form:**
The pre-chat form collects customer information before the chat starts. Email is required. You can optionally collect name and phone number.

**Anonymous chat option:**
If you allow chat as anonymous, customers can start chatting without submitting the form. In the pre-chat form, they'll see an option to "Chat with us as anonymous".

4. Click **Save**
5. Go to your storefront to preview the chatbox. Click **Chat now** to test a conversation.

To set your online/offline availability, configure your working hours in Online hours settings.


---

# Mobile App

<!-- CHUNK: mobile-app-install -->
```yaml
chunk_id: "faq__mobile-app-install"
doc_id: "chatty-mobile-app"
title: "How to download and install the Chatty mobile app on iOS and Android"
category: "faq"
subcategory: "mobile-app"
tags: ["mobile app", "download chatty", "install chatty", "iPhone chatty", "Android chatty", "home screen app", "QR code"]
applies_when: "When a merchant asks how to download or install the Chatty mobile app on their phone"
priority: "high"
```

## How to Download the Mobile App

The Chatty mobile app lets you answer customer questions and manage conversations from your phone or tablet — anywhere, anytime.

1. In the app dashboard, click **Install mobile app** in Setup guide (or go to Settings → Notifications → Download now)
2. Click **Download now**
3. Scan the QR code with your device
4. Your browser will open a link — follow the steps below for your device

## Installing on Each Browser

**Safari (iOS):**
Go to the link → Tap the share icon at the bottom → Select "Add to Home Screen" → Set up and confirm

**Chrome (iOS):**
Go to the link → Tap the share icon at the top right → Select "Add to Home Screen" → Set up and confirm

**Chrome (Android):**
Go to the link → Tap the menu icon (top right) → Select "Add to Home Screen" → Set up and confirm

**Firefox (iOS):**
Go to the link → Tap the bottom-right menu → Select "Share" → Select "Add to Home Screen" → Set up and confirm

For other browsers, contact support for assistance.

## What You Can Do in the Mobile App

- Reply to all conversations
- Set up main settings: general settings, notifications, online hours, and quick replies
- Send files, use quick replies, and access all chat functions
- View and manage conversation list

---

<!-- CHUNK: mobile-app-login-devices -->
```yaml
chunk_id: "faq__mobile-app-login-devices"
doc_id: "chatty-mobile-app"
title: "How to manage login devices and log out from other sessions"
category: "faq"
subcategory: "mobile-app"
tags: ["login devices", "manage sessions", "log out devices", "security", "unauthorized access", "active sessions"]
applies_when: "When a merchant asks how to view or manage their active login sessions or log out from other devices"
priority: "low"
```

## Managing Login Devices

If you've logged into Chatty on multiple devices, you can view and manage active sessions.

**How to view your login devices:**
1. Go to Web App
2. Click your account avatar in the top-right corner
3. Select **Manage Account**
4. Go to the **Login Devices** tab

Each session shows: device type, browser, approximate location, and last active time. Your current device is marked with a "Current device" badge.

**Remove a specific device:**
- On the Login Devices tab, find the session → click **Log out** next to it
- The session ends instantly; that device will need to log in again

**Log out all other devices:**
- On the Login Devices tab, scroll to the bottom → click **Log out all other devices**
- All sessions except your current device are ended immediately

If you suspect unauthorized access, log out all devices and update your password.


---

---
category: Common Issues
topic: Notification Issues
source: notion/Chatty FAQs
---

Q: The merchant is not receiving push notifications on desktop when new messages arrive.
Q: Desktop push notifications don't work for Chatty.
A: Check these settings in order:

**Step 1: Verify app notification settings**
- Ensure push notification is enabled for new/unread messages in App Settings.

**Step 2: Verify browser and device settings**
- Browser must have notifications allowed for Chatty/app.meetchatty.com.
- PC/laptop system settings must allow notifications (not in Silent/Do Not Disturb mode).
- Device must not be in presentation mode or screen recording mode.

**Step 3: If settings are correct but still no notifications**
- Clear browser cache and cookies.
- Restart the computer.
- Open browser DevTools (F12) > Application > Service Workers > Update the firebase-messaging-sw.js service worker.

**Step 4: If still not resolved**
- Offer to use TeamViewer/AnyDesk to directly check the merchant's settings.
- If the issue persists, forward to dev team with detailed info.

**Meanwhile:** Recommend email notifications or installing the Chatty mobile app as alternatives.

---

Q: The merchant is not receiving mobile app notifications.
Q: Chatty mobile app push notifications are not working.
A: Check these items:

1. Verify the mobile app is installed and the merchant is logged in.
2. Check device notification settings — Chatty must be allowed to send notifications.
3. Ensure the phone is not in Do Not Disturb mode.
4. Try uninstalling and reinstalling the mobile app.
5. If the issue persists, collect device model, OS version, and app version, then escalate to dev team.

---

Q: The merchant is not receiving email notifications when new messages arrive.
Q: Email alerts for new chat messages are not being sent.
A: Verify these settings:

1. Email notifications must be enabled in Chatty's notification settings.
2. Check the merchant's email spam/junk folder.
3. Verify the notification email address is correct.
4. If using a corporate email, the organization may be blocking automated emails.

---

Q: Chatty is not showing in the device's notification settings.
Q: I can't find Chatty in my phone/computer notification settings to enable it.
A: This can happen if:

1. The app was never opened after installation (notifications permission was never requested).
2. The notification permission was denied on first prompt and needs to be manually re-enabled.

**Solution:** Guide the merchant to manually find and enable Chatty notifications in their device settings, or clear app data and reopen to trigger the permission prompt again.

---

Q: How do I trigger the push notification permission popup again on mobile?
Q: The notification popup never appeared or was dismissed.
A: If the notification permission popup was dismissed or denied:

1. Go to device Settings > Apps > Chatty > Notifications > Enable notifications.
2. Alternatively, uninstall and reinstall the app to trigger the permission prompt again.

---

Q: Chatty is disconnected in Customer Events (App Pixel).
Q: The Chatty app pixel shows as disconnected in Shopify.
A: The App Pixel may become disconnected due to theme changes or Shopify updates.

**Solution:**
1. Go to Shopify Admin > Settings > Customer Events.
2. Find Chatty in the list and reconnect/re-enable it.
3. Verify the connection is active.
4. If the merchant cannot reconnect, collect details and escalate to TS team.

---

# Notifications

<!-- CHUNK: notifications-web-push -->
```yaml
chunk_id: "faq__notifications-web-push"
doc_id: "chatty-notifications"
title: "How to set up web push notifications for new messages in Chatty"
category: "faq"
subcategory: "notifications"
tags: ["notifications", "web push", "browser notifications", "push notifications", "Chrome notifications", "Firefox notifications", "not receiving notifications"]
applies_when: "When a merchant asks how to set up web push notifications or why they are not receiving browser notifications"
priority: "high"
```

## Web Push Notifications

Web push sends browser notifications for new messages. You need to enable notifications in both the Chatty app AND in your browser.

**Step 1: Enable in Chatty app**
Go to **Notifications** → In "Notify me when", select **Web** for:
- A conversation is assigned to me
- New message from unassigned conversations
- New message from conversations assigned to me
- New message from AI assistant conversations
- No reply in 15 minutes from conversations assigned to me

**Step 2: Enable in your browser**

Supported browsers: Chrome, Microsoft Edge, Firefox, Opera, Samsung Internet.

- **Chrome:** In Notifications → Click **Manage** → Turn on Notifications → Back to Chatty → Click **Save** → Click **Send test** to verify
- **Microsoft Edge:** In Notifications → Click **Manage** → Turn on Notifications → Refresh page → Click **Save** → **Send test**
- **Firefox:** Firefox can't grant permission inside Shopify embed mode. Go to the Chatty web app instead: In the top banner, click **Set up in web app** → In web app, click **Enable** → Allow the browser popup → Refresh page → **Send test**
- **Opera:** Turn on web push notifications → Allow in popup → Refresh → **Save** → **Send test**

**Step 3: Enable on your device**

- **Windows:** Settings → System → Notifications → Find your browser → Turn on notifications
- **MacOS:** Apple menu → Notifications → Application Notifications → Find your browser → Turn on
- **Mobile:** Download and use the Chatty mobile app for mobile notifications.

---

<!-- CHUNK: notifications-email-sound -->
```yaml
chunk_id: "faq__notifications-email-sound"
doc_id: "chatty-notifications"
title: "How to set up email notifications and sound alerts in Chatty"
category: "faq"
subcategory: "notifications"
tags: ["email notifications", "sound notifications", "notification email", "spam notifications", "unanswered AI notification", "escalation notification"]
applies_when: "When a merchant asks how to set up email or sound notifications, or how to get notified when AI can't answer"
priority: "high"
```

## Email Notifications

Go to **Notifications** → Select **Email** for the events you want:
- A conversation is assigned to me
- New message from unassigned conversations
- New message from assigned conversations
- No reply in 15 minutes from assigned conversations

Click **Save**. Click **Send test** to check a sample email.

**To prevent Chatty emails from going to spam:**
- Add Chatty's email to your safe sender list, or
- Open a Chatty notification email → Click the three dots menu → Select "Filter messages like this" → "Never send to Spam" + "Always mark as important" → Create filter

## Sound Notifications

Turning on sound notifications plays an audio alert for new messages. Choose whether to play sound for only the first message or all messages.

## AI Escalation Email Notifications

To receive email notifications when the AI cannot answer or a customer needs help:

1. Go to **Settings** → **Notifications** → **Email Notifications**
2. Enable the **Unanswered by AI** or **Escalation** notifications
3. Enter the email address(es) that should receive alerts

You can also configure this per agent in Team Settings.

---

<!-- CHUNK: notifications-troubleshooting -->
```yaml
chunk_id: "faq__notifications-troubleshooting"
doc_id: "chatty-notifications"
title: "Troubleshooting missing push and email notifications in Chatty"
category: "faq"
subcategory: "notifications"
tags: ["notifications not working", "push notifications iPhone", "not receiving email notifications", "notification troubleshoot", "human transfer notification"]
applies_when: "When a merchant is not receiving push notifications on iPhone or not getting email notifications when a conversation is transferred"
priority: "high"
```

## Not Receiving Push Notifications on iPhone

Steps to fix:

1. Confirm the Chatty web app is opened from your Home Screen (not browser)
2. In the app, go to Settings → Notifications and tap **Allow** if not already done
3. Go to iPhone Settings → Notifications and verify Chatty is listed with Banners, Sounds, and Badges enabled
4. Check that Silent mode / Do Not Disturb is not blocking notifications
5. If still not working, remove the web app from Home Screen, re-add it, and repeat the steps to trigger a fresh notification prompt

## Not Receiving Email Notifications for Transferred Conversations

Check:

1. **Settings** → **Notifications** — email notifications must be enabled
2. If conversations are auto-assigned to a specific team member, that member must enable "There is a conversation assigned to me" in their own notification settings
3. Check spam/junk folder
4. Ensure you have not previously unsubscribed from Chatty notification emails


---

# Online Hours

<!-- CHUNK: online-hours-setup -->
```yaml
chunk_id: "faq__online-hours-setup"
doc_id: "chatty-online-hours"
title: "How to set online hours, break times, holidays, and availability in Chatty"
category: "faq"
subcategory: "settings"
tags: ["online hours", "working hours", "offline hours", "break time", "holiday", "availability", "timezone", "online status", "offline message"]
applies_when: "When a merchant asks how to set their store's online/offline hours, break times, holidays, or availability display"
priority: "medium"
```

## Online Hours Overview

Online hours lets you define your working hours, break times, and holidays so customers know when to expect live support.

> Note: Online/offline status only works when the **Live chat** block is turned on in Chatbox settings.

## How to Set Up Online Hours

**Working hours:**
- **24/7**: Always available for chat
- **Custom time**: Set specific hours that match your schedule

**Add break time or holiday time:**
- **Break time**: Short offline periods during your working hours
- **Holiday time**: Days when you're fully offline

**Select timezone:**
Choose the timezone where most of your support is handled. This ensures your availability displays correctly to customers in your local time.

**Set status display:**
Choose when to show the online status in the chatbox:
- **During business hours**: Shows online only during your set hours
- **During business hours or when any agent is online**: Shows online during your set hours OR whenever any team member is logged in and available

**Customize online/offline messages:**
- Online message (default: "We are online")
- Offline message (default: "Usually reply in a few minutes")

Click **Save**. You can preview online and offline status on the chatbox before saving.


---

# Order Tracking

<!-- CHUNK: order-tracking-setup -->
```yaml
chunk_id: "faq__order-tracking-setup"
doc_id: "chatty-order-tracking"
title: "How to enable and configure order tracking in the Chatty chatbox"
category: "faq"
subcategory: "chatbox"
tags: ["order tracking", "track order", "order status", "enable order tracking", "17TRACK", "custom tracking", "default tracking"]
applies_when: "When a merchant asks how to set up order tracking in Chatty or which tracking method to use"
priority: "high"
```

## Order Tracking Overview

Order tracking is a self-service feature that lets customers check their order status directly through your chatbox — without emailing you or calling support.

Customers can track using either an order number or a tracking number.

## How to Enable Order Tracking

1. Go to **Chatbox** → **General** tab → Turn on **Order tracking** in the Blocks section
2. Go to **Settings** → **Integrations** → In Order tracking, click **Manage**
3. Select your preferred tracking method
4. Click **Save**

## Tracking Methods

- **Default tracking** — Best for stores using major carriers (DHL, FedEx, UPS). Redirects customers to the carrier's official tracking page.
- **Custom tracking** — Best for stores using local or private shipping carriers. Redirects customers to a custom tracking URL.
- **17TRACK** — Best for stores wanting to keep customers on-site. Embeds the 17TRACK tracking page directly on your store.

---

<!-- CHUNK: order-tracking-customer-experience -->
```yaml
chunk_id: "faq__order-tracking-customer-experience"
doc_id: "chatty-order-tracking"
title: "How customers track orders and what information is shown"
category: "faq"
subcategory: "chatbox"
tags: ["track order customer", "order tracking widget", "order status display", "tracking information", "AI order tracking", "order number lookup"]
applies_when: "When a merchant asks how customers use the order tracking feature or what information is displayed"
priority: "medium"
```

## How Customers Track Orders

**On your website:**
1. Click to open the chatbox → Click **Order tracking**
2. Enter an order number + email or phone, OR enter a tracking number
3. Click **Track**

**In AI conversation:**
Customers can ask the AI for order tracking. The AI will request tracking information and provide status directly in chat.

## What Customers See

**General order information:**
- Order number
- Order status (Confirmed, On its way, Delivered for physical orders; Confirmed, Completed for digital orders)
- Confirmation date
- Total items and amount

**Tracking information:**
- Product images and quantities
- Shipment status and update date
- Shipping carrier, tracking number, fulfillment date

---

<!-- CHUNK: order-tracking-issues -->
```yaml
chunk_id: "faq__order-tracking-issues"
doc_id: "chatty-order-tracking"
title: "Why order tracking may not show correct or updated information"
category: "faq"
subcategory: "chatbox"
tags: ["order tracking not updating", "wrong order status", "carrier not supported", "tracking issue", "order status incorrect"]
applies_when: "When a merchant reports that order tracking is not showing correct or updated information"
priority: "medium"
```

## Why Order Tracking May Not Be Updating

For Shopify-supported carriers (like DHL, FedEx, UPS), full tracking details update automatically in real time.

For unsupported carriers, only basic status updates appear: Confirmed, On its way, Delivered.

To check if your carrier is supported by Shopify, look it up in the Shopify carrier documentation. If not supported, consider switching to the **Custom tracking** method to link directly to your carrier's tracking page.


---

# Others — Resolve, Transcripts, Analytics, General

<!-- CHUNK: others-resolve-conversation -->
```yaml
chunk_id: "others__resolve-conversation"
doc_id: "chatty-others"
title: "How to resolve a conversation in Chatty"
category: "others"
tags: ["resolve", "close conversation", "mark resolved", "automatic resolution", "auto close"]
applies_when: "Merchant asks how to resolve or close a conversation, or wants to set up auto-resolution"
```

## Resolving Conversations

**Manually:**
1. Go to the conversation in Inbox
2. Handle the customer inquiry completely
3. Click **Resolve** — conversation moves to the Resolved filter

Best practice: Ask "Anything else I can help with?" before resolving. Don't resolve if still waiting for the customer's reply.

**Automatically:**
Go to **Settings** → **Automation** → Turn on **Automatic resolution**, then configure:
- **Auto resolve after** — how long to wait after inactivity
- **Time unit** — minutes, hours, or days
- **Notice message** — what customers see when conversation is auto-closed

Customers can always reopen a conversation by sending a new message.

---

<!-- CHUNK: others-conversation-transcript -->
```yaml
chunk_id: "others__conversation-transcript"
doc_id: "chatty-others"
title: "Send or set up conversation transcripts"
category: "others"
tags: ["transcript", "chat transcript", "email transcript", "conversation copy", "chat history email"]
applies_when: "Merchant or customer wants to receive a copy of the chat conversation by email"
```

## Conversation Transcripts

**Set up automatic transcripts:**
1. Go to **Settings** → **Channels** → **Email channel** → **Preferences**
2. In **Conversation transcript email**, turn on the feature
3. In **Forward to**, enter email addresses (separate multiple with commas)
4. Click **Save**

**Customer requests a transcript:**
1. In the chatbox, click the menu icon (three dots) at the top right
2. Select **Email transcript** — sent automatically to their email

**Team member sends a transcript:**
1. Open the conversation in inbox
2. Click the 3 dots at the top right → **Send transcript**
3. Choose recipient: yourself, the customer, or a custom email → **Done**

---

<!-- CHUNK: others-satisfaction-survey -->
```yaml
chunk_id: "others__satisfaction-survey"
doc_id: "chatty-others"
title: "Set up customer satisfaction survey (CSAT)"
category: "others"
tags: ["satisfaction survey", "CSAT", "rating", "feedback", "star rating", "emoji scale"]
applies_when: "Merchant wants to set up a customer satisfaction survey or rating after conversations"
```

## Satisfaction Survey Setup

1. Go to **Settings** → **Automation** → **Satisfaction survey** → **Manage**
2. Turn on **Survey**
3. Select format: **Star rating** (1–5 stars) or **Emoji scale** (5 faces)
4. Set **Intro** question and **Thank you** message
5. Set trigger: **Conversation is resolved** or **When specific keywords appear** (e.g., "thank you", "thanks", "got it", "perfect")
6. Click **Save**

---

<!-- CHUNK: others-company-name -->
```yaml
chunk_id: "others__company-name"
doc_id: "chatty-others"
title: "Official company name for privacy policy or GDPR"
category: "others"
tags: ["company name", "privacy policy", "GDPR", "legal name", "DPA", "Avada"]
applies_when: "Merchant needs the official company name for their privacy policy or GDPR data processing agreement"
```

## Official Company Name (Privacy Policy / GDPR)

The official company name is **Avada**, full legal name: **AVADA Commerce**.

You can reference this in your store's privacy policy when listing third-party apps that process customer data.

For DPA (Data Processing Agreement) requests, please contact our support team.

---

<!-- CHUNK: others-total-sales -->
```yaml
chunk_id: "others__total-sales"
doc_id: "chatty-others"
title: "How Total Sales in Analytics is calculated"
category: "others"
tags: ["total sales", "analytics", "sales tracking", "assisted sales", "revenue attribution"]
applies_when: "Merchant asks how the Total Sales figure in Chatty Analytics is calculated"
```

## Total Sales in Analytics

Analytics tracks orders placed by customers after they interacted via chat — these are "assisted" sales. If a customer chats and then completes a Shopify checkout, the order amount is included.

Payments made outside Shopify or through non-tracked channels may not be counted.

---

<!-- CHUNK: others-resolution-time -->
```yaml
chunk_id: "others__resolution-time"
doc_id: "chatty-others"
title: "Resolution time report per agent"
category: "others"
tags: ["resolution time", "handle time", "agent report", "analytics", "feature request"]
applies_when: "Merchant asks about average resolution time or handle time per agent in Analytics"
```

## Resolution Time Report

Not yet available as a built-in report. The product team has accepted a feature request to add **resolution time** and **handle time** to the Agent Report section. You will be notified once this is released.

---

<!-- CHUNK: others-agent-zero-resolved -->
```yaml
chunk_id: "others__agent-zero-resolved"
doc_id: "chatty-others"
title: "Agent showing zero resolved conversations in Analytics"
category: "others"
tags: ["zero resolved", "analytics", "agent report", "resolved count", "assignment setting"]
applies_when: "Agent's Analytics shows zero resolved conversations even though they replied to many chats"
```

## Agent Showing Zero Resolved Conversations

This is usually an assignment setting issue.

Go to **Settings** → **Automation** — if set to "Conversations stay with assigned member (or stay unassigned)," conversations handled by a specific agent won't be counted unless explicitly assigned.

Change to **"Conversations will be assigned to whoever replies"** so conversations are attributed correctly.

Note: this setting change does **not** retroactively update past Analytics data.

---

<!-- CHUNK: others-ai-metrics -->
```yaml
chunk_id: "others__ai-metrics"
doc_id: "chatty-others"
title: "What do AI engagement rate, resolution rate, and answer rate mean"
category: "others"
tags: ["AI metrics", "engagement rate", "resolution rate", "answer rate", "AI analytics", "AI stats"]
applies_when: "Merchant asks what the three AI metrics mean in Analytics"
```

## AI Metrics Explained

Answer Rate and AI Resolution Rate are two distinct metrics — do not conflate them.

- **Answer Rate** — percentage of customer messages the AI successfully responded to (reflects how many messages AI answered vs. passed to human). Check in Analytics.
- **AI Resolution Rate** — percentage of conversations the AI resolved without any human intervention. Check in Analytics.
- **AI Engagement Rate** — percentage of total conversations where the AI participated (including those later transferred to human)

In short: Answer Rate = % of messages AI answered. Resolution Rate = % of full conversations AI resolved alone. Engagement = did AI join at all?

---

<!-- CHUNK: others-ai-resolution-miscalculation -->
```yaml
chunk_id: "others__ai-resolution-miscalculation"
doc_id: "chatty-others"
title: "AI resolution rate seems to include human-intervened conversations"
category: "others"
tags: ["resolution rate", "miscalculation", "analytics bug", "AI resolution", "counting error"]
applies_when: "Merchant suspects the AI resolution rate is miscalculated or includes conversations where a human also intervened"
```

## AI Resolution Rate Miscalculation

This is a **known analytics calculation issue**. If your numbers don't add up, contact support with your date range — the team will investigate the counting logic.

---

<!-- CHUNK: others-headless-shopify -->
```yaml
chunk_id: "others__headless-shopify"
doc_id: "chatty-others"
title: "Does Chatty work on headless Shopify stores"
category: "others"
tags: ["headless", "headless Shopify", "headless store", "WAVE", "accessibility", "audio"]
applies_when: "Merchant asks if Chatty works on headless Shopify stores"
```

## Chatty on Headless Shopify

Yes, Chatty can be installed on headless stores. Some features (like audio notification sounds flagged by accessibility tools like WAVE) may behave differently. The audio element is used for customer notification sounds and is a standard, harmless functional element — WAVE flags it for accessibility review, not as an error.

---

<!-- CHUNK: others-404-error -->
```yaml
chunk_id: "others__404-error"
doc_id: "chatty-others"
title: "App not loading or showing a 404 error"
category: "others"
tags: ["404", "not loading", "app error", "page not found", "dashboard error"]
applies_when: "Merchant gets a 404 error or the Chatty app is not loading in their dashboard"
```

## App Not Loading / 404 Error

1. Hard reload the page (`Ctrl+Shift+R` / `Cmd+Shift+R`)
2. Clear browser cache and cookies
3. Try a different browser
4. Try incognito mode

If the issue persists across browsers, contact support — it may be a temporary backend issue.


---

# AI Assistant Overview

<!-- CHUNK: ai-overview-features -->
```yaml
chunk_id: "faq__ai-overview-features"
doc_id: "chatty-overview"
title: "What the Chatty AI assistant is and what it can do"
category: "faq"
subcategory: "ai-assistant"
tags: ["AI assistant", "AI overview", "what AI can do", "AI benefits", "chatbot", "24/7 support", "AI features"]
applies_when: "When a merchant asks what the AI assistant is, what it does, or what its capabilities are"
priority: "high"
```

## AI Assistant Overview

The AI assistant helps you answer customer questions automatically, 24/7, based on data you provide. It's trained on your store's products, FAQs, and custom information.

**Benefits:**
- Faster resolution times
- Happier customers without extra staffing
- Consistent brand voice across all conversations
- Works even when you're offline (great for solo entrepreneurs)

> To use the AI assistant, you need to have Live chat turned on. Go to Chatbox → Turn on Live chat block.

## What the AI Assistant Can Do

- Respond to customer questions instantly, 24/7
- Suggest and compare products based on customer needs
- Handle multi-language conversations
- Summarize conversations when transferring to your team
- Update shopping carts and send checkout links

---

<!-- CHUNK: ai-overview-setup -->
```yaml
chunk_id: "faq__ai-overview-setup"
doc_id: "chatty-overview"
title: "How to get the Chatty AI assistant ready — training, customization, and activation"
category: "faq"
subcategory: "ai-assistant"
tags: ["AI setup", "activate AI", "train AI", "AI not responding", "enable AI assistant", "AI data sources", "AI configuration"]
applies_when: "When a merchant asks how to set up, activate, or fix the AI assistant not responding"
priority: "high"
```

## How to Get Your AI Assistant Ready

**Step 1: Train your AI**

Chatty auto-syncs your existing store data. You can also add custom data sources:
- Products (auto-synced)
- Discounts (auto-synced)
- FAQs (auto-synced)
- Custom Q&A, URLs, and files

**Step 2: Customize your AI**

Go to AI assistant → Settings to configure:
- Bot name and avatar
- Welcome message
- Custom instructions (tone, response style, brand voice)
- AI availability (when AI responds vs. human agents)
- Transfer settings (how to hand off to your team)

**Step 3: Test and optimize**

Use the Test zone to simulate customer interactions before going live.

**Step 4: Activate**

Click **Turn on** to activate the AI assistant.

## When AI Is Active

- All conversations are answered automatically by AI. You'll see AI assistant listed as the assignee.
- You can always click **Join conversation** to take over from AI.
- When a conversation is transferred to your team, AI generates a chat summary with detected language, main issues, and suggested responses.

## AI Not Responding — Checklist

If AI is not responding, check:
- Live chat block is turned on in Chatbox
- AI assistant status is set to active (not paused)
- You have at least some data sources added


---

# Powerful Contact Form Integration

<!-- CHUNK: powerful-contact-form-overview -->
```yaml
chunk_id: "faq__powerful-contact-form-overview"
doc_id: "chatty-powerful-contact-form"
title: "How to integrate Powerful Contact Form with Chatty to convert form submissions into inbox conversations"
category: "faq"
subcategory: "integrations"
tags: ["powerful contact form", "contact form", "form to inbox", "form submission", "form integration", "forwarding email"]
applies_when: "When a merchant asks how to connect a contact form to Chatty or how form submissions become inbox conversations"
priority: "medium"
```

## Powerful Contact Form Integration Overview

The Powerful Contact Form integration connects your contact form to Chatty inbox. Each form submission automatically becomes a conversation in your inbox, so you can reply to customers directly from Chatty.

Powerful Contact Form is free to install from the Shopify App Store.

> **Requirement:** Forms must include either an email or phone number field to create conversations.

## How to Set Up

**Step 1: Set up a forwarding email in Chatty** (skip if already connected)
1. From Chatty, go to **Channels**
2. Click **Add email**
3. Add your email as a forwarding email
4. Click **Send verification email** to confirm

**Step 2:** Copy your forwarding email from Chatty Channels settings

**Step 3:** Open Powerful Contact Form

**Step 4:** Open the form you want to connect

**Step 5: Add your Chatty forwarding email**
1. Open the form builder
2. Click **Mail**
3. Add the forwarding email as the form notification email

**Step 6:** Click **Save**

## What Happens When a Customer Submits a Form

Chatty automatically creates a conversation in your inbox with:
- A customer profile (name, email, phone from the form)
- The form content as the first message
- The ability to reply directly from Chatty inbox

> Note: Form notification emails won't create duplicate conversations.


---

# Pricing & Plans

<!-- CHUNK: pricing-plans-overview -->
```yaml
chunk_id: "pricing__plans-overview"
doc_id: "chatty-pricing"
title: "Chatty pricing plans overview"
category: "pricing"
tags: ["pricing", "plans", "cost", "free plan", "basic", "pro", "plus", "enterprise", "how much"]
applies_when: "Merchant asks about Chatty's pricing, plans, or how much it costs"
```

## Chatty Plans & Pricing

- **Free** — $0/month: 50 AI conversations (lifetime), 100 products, 1 team member, 1 email channel, 90 days chat history, all channels & integrations.
- **Basic** — $19.99/month (or $16.99/month annual): 50 AI conversations/month + $0.40/extra, 500 products, 5 team members, unlimited email channels, 12 months history, full chatbox customization.
- **Pro** — $68.99/month (or $58.99/month annual): 300 AI conversations/month + $0.40/extra, 8,000 products, 10 team members, unlimited history, full AI channels, full analytics.
- **Plus** — $199/month (or $169.99/month annual): 700 AI conversations/month + $0.40/extra, 20,000 products, unlimited team members, advanced analytics, dedicated AI consultant.
- **Enterprise** — Custom pricing for larger stores. Contact Chatty to build a custom plan.

---

<!-- CHUNK: pricing-plan-comparison -->
```yaml
chunk_id: "pricing__plan-comparison"
doc_id: "chatty-pricing"
title: "Which Chatty plan should I choose"
category: "pricing"
tags: ["compare plans", "which plan", "plan difference", "features", "free vs paid", "upgrade"]
applies_when: "Merchant asks which plan to choose or wants to compare plan features"
```

## Plan Feature Comparison

**Free:** AI conversations 50 lifetime, products 100, custom answers 100, URLs & files 20, team members 1, chat history 90 days, email channels 1, chatbox customization default.

**Basic:** AI conversations 50/month + $0.40/extra, products 500, custom answers 1,000, URLs & files 50, team members 5, chat history 12 months, email channels unlimited, chatbox customization full.

**Pro:** AI conversations 300/month + $0.40/extra, products 8,000, custom answers unlimited, URLs & files 500, team members 10, chat history unlimited, AI channels full, analytics full.

**Plus:** AI conversations 700/month + $0.40/extra, products 20,000, custom answers unlimited, URLs & files 700, team members unlimited, chat history unlimited, dedicated AI consultant included.

---

<!-- CHUNK: pricing-free-trial-refund -->
```yaml
chunk_id: "pricing__free-trial-refund"
doc_id: "chatty-pricing"
title: "Free trial and refund policy"
category: "pricing"
tags: ["free trial", "trial", "refund", "money back", "cancel trial", "30 day", "7 day"]
applies_when: "Merchant asks about free trial, refund policy, or money-back guarantee"
```

## Free Trial & Refund Policy

**Free trial:** All paid plans include a **7-day free trial**. Cancel anytime during the trial.

**30-day Money Back Guarantee** applies when:
- You don't wish to continue after the first month
- You cancel before the first billing cycle ends
- You forgot to cancel the trial or accidentally chose a paid plan without using it in the first month

For a refund, contact support with a **screenshot of the Shopify charge** (showing app name, billing cycle, and amount).

---

<!-- CHUNK: pricing-ai-conversation-limits -->
```yaml
chunk_id: "pricing__ai-conversation-limits"
doc_id: "chatty-pricing"
title: "AI conversation limits per plan"
category: "pricing"
tags: ["AI conversation limit", "conversation limit", "quota", "limit reached", "extra conversations", "overage"]
applies_when: "Merchant asks about AI conversation limits, or has reached their limit"
```

## AI Conversation Limits

- **Free:** 50 lifetime — AI deactivated when reached
- **Basic:** 50/month — extra at $0.40/conversation
- **Pro:** 300/month — extra at $0.40/conversation
- **Plus:** 700/month — extra at $0.40/conversation

**When Free plan limit is reached:** AI assistant is deactivated. Conversations can still be handled manually in Inbox.

**When paid plan limit is reached:** Extra conversations are charged at $0.40 each (unless a spending limit is set).

---

<!-- CHUNK: pricing-check-usage-spending-limit -->
```yaml
chunk_id: "pricing__check-usage-spending-limit"
doc_id: "chatty-pricing"
title: "Check AI usage and set spending limit"
category: "pricing"
tags: ["check usage", "spending limit", "usage limit", "billing", "overage control", "AI usage"]
applies_when: "Merchant wants to check their AI conversation usage or set a spending cap"
```

## Checking Usage & Setting a Spending Limit

**Check usage:**
1. Go to **Subscription**
2. Check **AI conversation** usage in Subscription details
3. Usage resets on your billing cycle date (not calendar month)
4. Email notifications sent at 80% and 100% of limit

**Set a spending limit:**
1. Go to **Subscription** → **Set usage limit** → **Edit**
2. Enter your budget limit → **Save**

Once the limit is reached, AI stops responding until the next billing cycle. Human agents can still handle conversations.

Tip: Set limit 15–20% above expected usage to handle busy periods.

---

<!-- CHUNK: pricing-extra-charges -->
```yaml
chunk_id: "pricing__extra-charges"
doc_id: "chatty-pricing"
title: "Extra charges beyond monthly plan fee"
category: "pricing"
tags: ["extra charge", "additional charge", "overage", "unexpected charge", "billing", "AI conversations"]
applies_when: "Merchant asks about extra charges or received an unexpected bill"
```

## Extra Charges

Extra charges appear when AI conversations exceed your monthly plan limit — charged at **$0.40 per extra conversation**.

Set a spending cap in **Subscription** settings to control this. Human agent responses have no per-conversation charge.

If you believe a charge was incorrect (e.g., system miscalculation), contact support with a **screenshot of the Shopify billing section** — the team will investigate and process a refund if the charge was an error.

---

<!-- CHUNK: pricing-charged-unexpectedly -->
```yaml
chunk_id: "pricing__charged-unexpectedly"
doc_id: "chatty-pricing"
title: "Charged unexpectedly or forgot to cancel trial"
category: "pricing"
tags: ["unexpected charge", "forgot cancel", "trial charge", "charged", "free plan", "downgrade"]
applies_when: "Merchant was charged unexpectedly or forgot to cancel a paid trial"
```

## Charged Unexpectedly / Forgot to Cancel Trial

Chatty does not automatically upgrade plans. However, if you signed up for a paid trial and did not downgrade before the trial ended, Shopify charged you when the new cycle began.

**To stop future charges:** Go to **Settings** → **Subscription** → select the **Free plan**.

**For a refund:** Contact support with a screenshot of the Shopify charge (showing app name, billing cycle, and amount) — the team will review and process a refund if applicable.

---

<!-- CHUNK: pricing-cancel-downgrade -->
```yaml
chunk_id: "pricing__cancel-downgrade"
doc_id: "chatty-pricing"
title: "Cancel subscription or downgrade to Free"
category: "pricing"
tags: ["cancel", "downgrade", "free plan", "subscription", "stop charges", "unsubscribe"]
applies_when: "Merchant wants to cancel their subscription or downgrade to Free plan"
```

## Cancelling / Downgrading to Free

Go to **Settings** → **Subscription** → **Plan** → **Select Free Plan** → confirm.

Do this before your next billing cycle to avoid charges. Downgrading does not delete your data or settings.

---

<!-- CHUNK: pricing-discount-code -->
```yaml
chunk_id: "pricing__discount-code"
doc_id: "chatty-pricing"
title: "How to apply a discount code"
category: "pricing"
tags: ["discount code", "promo code", "coupon", "apply discount", "code invalid"]
applies_when: "Merchant wants to apply a discount or promo code to their subscription"
```

## Applying a Discount Code

Go to **Settings** → **Subscription** and enter the code in the **Discount Code** field before upgrading.

If the code shows as invalid, make sure you are on the correct plan (some codes are plan-specific). Contact support if the code still doesn't work.

---

<!-- CHUNK: pricing-annual-billing -->
```yaml
chunk_id: "pricing__annual-billing"
doc_id: "chatty-pricing"
title: "Annual billing discount"
category: "pricing"
tags: ["annual", "yearly", "discount", "save", "annual billing", "annual plan"]
applies_when: "Merchant asks about annual billing or saving money on their subscription"
```

## Annual Billing Discount

Save approximately **15%** by choosing annual billing:
- Basic: $16.99/month
- Pro: $58.99/month
- Plus: $169.99/month

---

<!-- CHUNK: pricing-legacy-plan -->
```yaml
chunk_id: "pricing__legacy-plan"
doc_id: "chatty-pricing"
title: "Legacy pricing plan changed without notice"
category: "pricing"
tags: ["legacy plan", "old pricing", "price changed", "billing history", "previous pricing"]
applies_when: "Merchant was on a legacy pricing plan and their price changed"
```

## Legacy Plan Price Changed

Contact support with a **screenshot of your Shopify billing history**. If you had an active discount or legacy pricing that should have been honored, the team can escalate to the billing team to review and restore your previous pricing. Refunds for the price difference can be requested if applicable.

---

<!-- CHUNK: pricing-app-credits -->
```yaml
chunk_id: "pricing__app-credits"
doc_id: "chatty-pricing"
title: "Shopify app credits for Chatty"
category: "pricing"
tags: ["app credits", "Shopify credits", "billing credits", "credit"]
applies_when: "Merchant asks where to find or how to use their Shopify app credits for Chatty"
```

## Shopify App Credits

Go to **Shopify Admin** → **Settings** → **Billing** → **App credits**. Credits appear here and can offset future app usage charges.

---

<!-- CHUNK: pricing-billing-date-format -->
```yaml
chunk_id: "pricing__billing-date-format"
doc_id: "chatty-pricing"
title: "How to read the billing date format in Chatty"
category: "pricing"
tags: ["billing date", "date format", "renews on", "MM/DD/YYYY"]
applies_when: "Merchant is confused about the billing date format shown in Chatty"
```

## Billing Date Format

Chatty uses **MM/DD/YYYY** format. "Renews on 04/12/2026" means **April 12, 2026** — not December 4.

---

<!-- CHUNK: pricing-scenario-limit -->
```yaml
chunk_id: "pricing__scenario-limit"
doc_id: "chatty-pricing"
title: "AI Scenario limit per plan"
category: "pricing"
tags: ["scenario limit", "AI scenarios", "how many scenarios", "extend scenarios"]
applies_when: "Merchant asks about the scenario limit or wants to extend it"
```

## AI Scenario Limits

| Plan | Scenarios |
|------|-----------|
| Free / Basic | 5 |
| Pro | 15 |
| Plus | Unlimited |

Extensions beyond plan limits require PM approval. Contact support and explain your use cases — the more specific you are, the faster the request can be processed.

---

<!-- CHUNK: pricing-10k-products -->
```yaml
chunk_id: "pricing__10k-products"
doc_id: "chatty-pricing"
title: "AI product recommendations for stores with 10,000+ products"
category: "pricing"
tags: ["10000 products", "large catalog", "product limit", "backend configuration", "demo call"]
applies_when: "Merchant has more than 10,000 products and wants to use AI product recommendations"
```

## Stores with 10,000+ Products

Yes, AI product recommendations work — but it requires manual backend configuration beyond the standard 5,000-product limit.

Contact support with your total product count and monthly order volume. For stores with 10,000+ products and 100+ orders/month, a demo call with the product team is recommended.

---

<!-- CHUNK: pricing-extend-limits -->
```yaml
chunk_id: "pricing__extend-limits"
doc_id: "chatty-pricing"
title: "Extend product, URL, or custom answer limits"
category: "pricing"
tags: ["extend limit", "increase limit", "product limit", "URL limit", "custom answer limit", "one-time"]
applies_when: "Merchant needs their product, URL/file, or custom answer limits extended beyond their plan"
```

## Extending Plan Limits

CS agents can extend these limits up to the next plan's level as a **one-time accommodation**. For example, a Basic store can be extended to Pro limits (8,000 products, 500 URLs).

Contact support and specify what you need.


---

# Proactive Chat

<!-- CHUNK: proactive-chat-overview -->
```yaml
chunk_id: "faq__proactive-chat-overview"
doc_id: "chatty-proactive-chat"
title: "What proactive chat is and what templates are available"
category: "faq"
subcategory: "live-chat"
tags: ["proactive chat", "automated messages", "popup chat", "welcome message", "cart booster", "abandoned cart", "newsletter subscribe", "product recommendation"]
applies_when: "When a merchant asks what proactive chat is or what campaign templates are available"
priority: "high"
```

## Proactive Chat Overview

Proactive chat lets you send targeted messages to website visitors before they ask questions. Instead of waiting for customers to reach out, you can engage them at key moments in their shopping journey.

**Use cases:**
- Greet new visitors and guide them to products
- Recover abandoned carts with incentives
- Grow your email list with exclusive discount offers
- Recommend bestsellers when customers show buying intent

## Proactive Chat Templates

Chatty provides pre-built templates for common scenarios:

| Template | Purpose | Best for |
|---|---|---|
| Welcome visitors | Greet new visitors with personalized messages | First-time visitors, high-traffic pages |
| Subscribe newsletter | Capture emails with exclusive offers | Lead generation, building email lists |
| Product recommendation | Boost sales by recommending relevant products | Cross-selling, showcasing bestsellers |
| Cart booster | Convert cart abandoners with incentives | Cart recovery, increasing order completion |
| Abandoned cart reminder | Remind customers about items left in cart | Reducing cart abandonment |
| Collection boost | Boost engagement on collection pages | Seasonal promotions, new launches |

---

<!-- CHUNK: proactive-chat-setup -->
```yaml
chunk_id: "faq__proactive-chat-setup"
doc_id: "chatty-proactive-chat"
title: "How to set up and configure a proactive chat campaign"
category: "faq"
subcategory: "live-chat"
tags: ["proactive chat setup", "create campaign", "targeting", "display time", "campaign priority", "double opt-in", "marketing opt-in"]
applies_when: "When a merchant asks how to create or configure a proactive chat campaign"
priority: "high"
```

## How to Set Up Proactive Chat

1. Go to **Proactive chat**
2. Click **Create proactive chat**
3. Choose your campaign type
4. Configure settings:

**Campaign details:**
- Campaign name
- Activate campaign toggle

**Targeting:**
- Trigger options: when to send the message
- Pages: which pages show this campaign (press Enter after each URL to add)
- Audience: all visitors or returning customers
- Devices: desktop, mobile, or both
- Display time: after page load, after scroll percentage, or after time delay
- Display duration: how long the campaign stays visible

**Message content:**
- Proactive message: text shown above the chatbox
- Rich content: include product suggestions (available for Product recommendations and Cart booster)
- Chat message: message sent when customers click the teaser (discount sent with message for Subscribe newsletter and Cart booster)

5. Check **Preview** to see how the campaign looks on your storefront
6. Click **Activate** to make it live

## Campaign Priority

When multiple campaigns could show at the same time:
1. Highest priority campaigns show first
2. Multiple campaigns can display per visitor per session
3. Set priorities in campaign settings (1 = highest priority)

## Marketing Double Opt-In (Subscribe Newsletter)

When enabled, customers receive a confirmation email before getting their discount.

## Timing Best Practices

- Welcome messages: 5-10 seconds after page load
- Product recommendations: After 30-50% page scroll
- Cart boosters: 2-3 minutes after adding items to cart
- Newsletter signup: Before exit intent or after browsing multiple products

---

<!-- CHUNK: proactive-chat-advanced -->
```yaml
chunk_id: "faq__proactive-chat-advanced"
doc_id: "chatty-proactive-chat"
title: "Advanced proactive chat use cases — post-order messages and CTA customization"
category: "faq"
subcategory: "live-chat"
tags: ["post-order message", "order confirmation proactive chat", "add to cart button", "learn more button", "proactive chat CTA", "Klaviyo post-purchase"]
applies_when: "When a merchant asks about sending automatic messages after an order or customizing CTA buttons in proactive chat"
priority: "medium"
```

## Automatic Message After Order Placement

At the moment, Chatty doesn't support sending an automatic message directly after a customer places an order.

However, as a workaround, you can set up a **Proactive Chat** trigger that activates when a customer visits the order confirmation page, and pair it with a **Custom AI Scenario** to send a personalized follow-up message.

For a more fully automated post-order workflow, consider integrating with **Klaviyo** to handle post-purchase email automation.

## Customizing Product Recommendation CTA Buttons

Yes, you can customize the CTA button when setting up a Proactive Chat campaign with product recommendations — for example, configuring buttons such as **Add to Cart** or **Learn More** that link customers to the product page.

If you need more specific customization for these buttons, share how you'd like them to work and our team can check what's possible.


---

# Quick Replies

<!-- CHUNK: quick-replies-overview -->
```yaml
chunk_id: "faq__quick-replies-overview"
doc_id: "chatty-quick-replies"
title: "How to set up and use quick replies for common customer questions"
category: "faq"
subcategory: "live-chat"
tags: ["quick replies", "pre-written responses", "canned responses", "shortcut replies", "quick reply setup", "chat shortcut"]
applies_when: "When a merchant asks how to set up or use quick replies during customer conversations"
priority: "medium"
```

## Quick Replies Overview

Quick replies are pre-written messages your team can send quickly during customer conversations — great for common questions like shipping policies, return procedures, or greetings.

## How to Set Up Quick Replies

1. Go to **Settings** → In Quick replies, click **Manage**
2. Turn on Quick replies to enable them in chat
3. Click **Create quick reply**
4. Enter a shortcut, category, and your response text
   - To add a new category: enter the category name and click **Add**
5. Click **Save**
6. Edit or delete quick replies as needed

## How to Use Quick Replies in Chat

In any conversation, either:
- Click the quick replies icon in the chat toolbar
- Type `/` in the message box

Then click to select the quick reply you want to send.

You can also add new quick replies directly from the chat zone without going to Settings.


---

# Quick Start Guide

<!-- CHUNK: quick-start-setup -->
```yaml
chunk_id: "faq__quick-start-setup"
doc_id: "chatty-quick-start"
title: "Getting started with Chatty — 5 steps to set up your store"
category: "faq"
subcategory: "getting-started"
tags: ["quick start", "getting started", "setup guide", "first steps", "new install", "Chatty setup", "onboarding"]
applies_when: "When a merchant just installed Chatty and asks what to do next or how to get started"
priority: "high"
```

## Quick Start Overview

Chatty is a platform that helps Shopify merchants engage with customers through live chat, AI assistant, and FAQs. Here are 5 steps to get your store ready.

## Step 1: Enable the App in Your Theme

Chatty shows a chatbox on your storefront, so you need to enable it in your theme editor first.

1. In the app dashboard, click **Enable app**
2. You'll be redirected to your theme editor
3. Enable Chatty in App embed and click **Save**

## Step 2: Set Up FAQs

- **Build your FAQs hub** — Add categories and questions to organize your FAQs
- **Create a FAQs page** — Show a dedicated FAQs page on your Shopify site
- **Add a FAQs block** — Show FAQs on any specific page of your store (product pages, homepage, etc.)

## Step 3: Set Up Live Chat

1. Go to Chatbox → In "General", click **Turn on** chatbox
2. In "Blocks", turn on **Live chat**
3. Click **Edit** to configure the pre-chat form (collects customer info before chat starts)

## Step 4: Connect Channels

Connect email, Facebook Messenger, Instagram, or WhatsApp to manage all conversations in one place.

## Step 5: Install the Mobile App

Answer customer questions from anywhere with the Chatty mobile app.

1. In the app dashboard, click **Install mobile app** in Setup guide (or go to Settings → Notifications → Download now)
2. Scan the QR code with your device
3. In your browser settings, tap "Add to Home Screen" to install the app

---

<!-- CHUNK: quick-start-enable-theme -->
```yaml
chunk_id: "faq__quick-start-enable-theme"
doc_id: "chatty-quick-start"
title: "How to enable Chatty on your Shopify theme — App embed setup"
category: "faq"
subcategory: "getting-started"
tags: ["enable app", "app embed", "chatbox not showing", "theme editor", "chatty not visible", "enable chatty"]
applies_when: "When a merchant says Chatty is installed but not showing on their store, or asks how to enable it in the theme"
priority: "high"
```

## Enabling Chatty on Your Shopify Theme

Chatty needs to be enabled in your Shopify theme editor to appear on your storefront.

1. In the Chatty app dashboard, click **Enable app**
2. You'll be redirected to your theme editor
3. Find Chatty under **App embeds** and turn on the toggle
4. Click **Save**

If the chatbox still doesn't appear, make sure the correct theme is selected in your theme editor and that you saved after enabling the app embed.


---

# AI Assistant Settings

<!-- CHUNK: ai-settings-appearance -->
```yaml
chunk_id: "faq__ai-settings-appearance"
doc_id: "chatty-settings"
title: "How to customize the AI assistant's name, avatar, and welcome message"
category: "faq"
subcategory: "ai-assistant"
tags: ["AI name", "bot name", "AI avatar", "chatbot appearance", "welcome message", "AI branding", "customize AI"]
applies_when: "When a merchant asks how to change the AI assistant's name, avatar, or welcome message"
priority: "medium"
```

## AI Assistant Appearance Settings

Go to **AI assistant** → **Settings** (or the Instruction tab).

**Appearance:**
- **Bot name**: The name shown to customers in the chatbox
- **Avatar**: Upload a custom image for your AI assistant

**Welcome message:**
The first message customers see when they click Contact us. Customize this to match your brand tone.

---

<!-- CHUNK: ai-settings-custom-instructions -->
```yaml
chunk_id: "faq__ai-settings-custom-instructions"
doc_id: "chatty-settings"
title: "How to write custom instructions to control AI tone, style, and behavior"
category: "faq"
subcategory: "ai-assistant"
tags: ["custom instructions", "AI tone", "brand voice", "AI personality", "AI response style", "AI boundaries", "generate instructions"]
applies_when: "When a merchant asks how to write custom instructions for the AI or how to control how the AI responds"
priority: "high"
```

## Custom Instructions for AI

Custom instructions let you guide how your AI assistant behaves — its tone, style, boundaries, and how it handles specific situations.

**To add custom instructions:**
Go to **AI assistant** → **Instruction tab** → Enter your **Custom instruction**

You can also click **Generate with AI** to auto-generate instructions based on your business type.

**What to include in custom instructions:**

- **Role & identity**: Who the AI represents (sales assistant, customer support, product expert)
- **Knowledge boundaries**: What topics the AI should know about, and how to handle questions outside its scope
- **Response style**: Length, format, level of detail
- **Tone & language**: Formal vs. casual, specific vocabulary to use or avoid
- **Conversation flow**: When to ask clarifying questions, how to guide customers toward purchases
- **Boundaries**: What the AI should NOT say or do

**Tips for effective instructions:**
1. Be specific — use clear examples rather than vague guidelines
2. Organize by categories (knowledge, tone, approach)
3. Define what the AI should not do
4. Consider the full customer journey (browsing, pre-purchase, post-purchase)
5. Test and refine regularly

You can include multiple instruction blocks in the same text box — organize them clearly by topic.

**Example (clothing store):**

```
You are a knowledgeable sales assistant for [Store Name].

ROLE: Act as a friendly, fashion-forward associate. Refer to yourself as "I".

APPROACH: Be conversational and positive. Suggest complementary items to create complete outfits.

SIZING: Provide guidance on sizing and suggest checking our size guide for detailed measurements.

AVOID: Don't make definitive claims about stock levels or delivery dates.
```


---

# Team Management

<!-- CHUNK: team-invite-members -->
```yaml
chunk_id: "team__invite-members"
doc_id: "chatty-team"
title: "Invite team members to Chatty"
category: "team"
tags: ["invite", "team member", "add staff", "team", "seats", "how many members"]
applies_when: "Merchant wants to invite team members or asks how many team members they can have"
```

## Inviting Team Members

Team member limits by plan:
- **Free**: 1 seat (admin only)
- **Basic**: 2 additional members (3 total)
- **Pro**: 4 additional members (5 total)
- **Plus**: Unlimited members

**How to invite:**
1. Go to **Settings** → **Manage** in Teams
2. Click **Invite member**
3. Enter the member's name and email (email cannot be changed later)
4. Click **Invite** — invitation email is sent
5. Ask the member to check their email and click **Create account**

---

<!-- CHUNK: team-assign-conversations -->
```yaml
chunk_id: "team__assign-conversations"
doc_id: "chatty-team"
title: "Assign conversations to team members"
category: "team"
tags: ["assign", "conversation assignment", "auto assign", "round robin", "manual assign"]
applies_when: "Merchant wants to assign conversations to team members manually or automatically"
```

## Assigning Conversations

**Manually:**
1. Go to **Inbox** → select a conversation
2. In conversation details, go to **Assignee** → click **Assign** → select a team member

**Automatically (round-robin):**
Go to **Settings** → **Automation** → **Assignment** → **Automatic**

Chatty rotates new conversations to available team members in sequence. These auto-assignment settings also apply to conversations transferred from the AI assistant.

---

<!-- CHUNK: team-internal-notes -->
```yaml
chunk_id: "team__internal-notes"
doc_id: "chatty-team"
title: "Leave internal notes and mention teammates in conversations"
category: "team"
tags: ["internal notes", "notes", "mention", "@mention", "team notes", "private comment"]
applies_when: "Merchant wants to leave internal notes or mention teammates in a conversation"
```

## Internal Notes & Mentions

Internal notes are private comments visible only to your team — customers cannot see them. Use internal notes to leave instructions, flag issues, or coordinate with teammates inside a conversation.

**Leave a note:**
1. In a conversation, click the **Notes** tab
2. Type your note
3. To mention a teammate, type `@` followed by their name
4. Click **Send**

When you mention someone with `@`, they receive a push notification and email notification.

---

<!-- CHUNK: team-deactivate-member -->
```yaml
chunk_id: "team__deactivate-member"
doc_id: "chatty-team"
title: "Deactivated team member access"
category: "team"
tags: ["deactivate", "remove member", "access", "revoke access", "deactivated"]
applies_when: "Merchant asks if a deactivated team member can still access Chatty"
```

## Deactivated Team Members

Once a member is deactivated or removed, they **lose access** to the Chatty inbox. The only exception is the Admin account, which cannot be deactivated.

---

<!-- CHUNK: team-notification-human-request -->
```yaml
chunk_id: "team__notification-human-request"
doc_id: "chatty-team"
title: "Get notified when a customer wants to speak to a human"
category: "team"
tags: ["notification", "human request", "talk to human", "escalation notification", "assigned notification"]
applies_when: "Merchant wants to receive notifications when a customer asks to speak to a human agent"
```

## Notifications for Human Escalation Requests

Go to **Settings** → **Notifications** and enable email notifications.

Also ensure the agent handling escalations has **"There is a conversation assigned to me"** enabled in their personal Notification settings.

If using automatic assignment to a specific agent, that agent must have notifications enabled.


---

# Test and Optimize AI

<!-- CHUNK: test-and-optimize-test-zone -->
```yaml
chunk_id: "faq__test-and-optimize-test-zone"
doc_id: "chatty-test-and-optimize-ai"
title: "How to use the AI test zone to verify responses before going live"
category: "faq"
subcategory: "ai-assistant"
tags: ["test AI", "AI test zone", "test chatbot", "simulate customer", "test before activate", "AI preview"]
applies_when: "When a merchant asks how to test the AI assistant before turning it on for customers"
priority: "high"
```

## AI Test Zone

You can test your AI assistant without enabling it for customers. The test zone simulates customer interactions so you can verify responses before going live.

**Before testing, make sure you've:**
- Added data sources (FAQs, product info, etc.)
- Added custom instructions (tone, voice, response length)
- Set up other settings (bot name, avatar)

**To access the test zone:**
Go to **AI assistant** → **Test**

**How to test:**
1. In the chatbox, ask questions as if you were a customer
2. Use the provided question examples (click **Regenerate questions** for more)
3. Check each response carefully

**What to check:**
- Is the information correct?
- Is the tone friendly but professional?
- Are product details accurate?
- Are prices and availability correct?
- Is the response length appropriate (not too long or too short)?

**Testing tips:**
- Test one topic at a time
- Ask the same question in different ways
- Try edge cases and unusual phrasings

You can also review which data sources the AI used to answer each question.

---

<!-- CHUNK: test-and-optimize-unresolved -->
```yaml
chunk_id: "faq__test-and-optimize-unresolved"
doc_id: "chatty-test-and-optimize-ai"
title: "How to fix AI responses using unresolved questions and response review"
category: "faq"
subcategory: "ai-assistant"
tags: ["unresolved questions", "AI wrong answers", "AI incomplete answers", "fix AI", "improve AI", "add answer", "AI review sources"]
applies_when: "When a merchant asks how to fix incorrect AI responses or improve the AI using unresolved questions"
priority: "high"
```

## Unresolved Questions

Unresolved questions are customer inquiries the AI couldn't answer effectively. They appear when customers click "Talk to a person" (or equivalent reply button).

Only questions from the past 30 days are shown.

**How to optimize unresolved questions:**

1. Go to **AI assistant** → **Unresolved questions**
2. Look for patterns — group similar questions to identify gaps in training data
3. For each question, click **Add answer** → Enter your answer
4. Answers are added to your data sources (in the Questions list)
5. Go back to **Test zone** and ask the same question to confirm AI can now handle it

For spam or duplicate questions, click **Ignore** to remove from the list.

## AI Response Review

Each AI response in the test zone includes a **Review sources** button showing what data was used.

Use this to:
- Add missing product information
- Correct inaccurate policy details
- Expand on partial answers
- Add question variations that weren't understood

**What to do when you spot a problem:**
1. Click **Add relevant data** in the response
2. You'll be redirected to data sources to add the right information
3. Watch for patterns — if you're repeatedly adding the same type of info, create comprehensive entries on that topic


---

# Train AI

<!-- CHUNK: train-ai-planning -->
```yaml
chunk_id: "faq__train-ai-planning"
doc_id: "chatty-train-ai"
title: "How to plan and organize AI training content for best results"
category: "faq"
subcategory: "ai-assistant"
tags: ["train AI", "AI training", "training data", "AI data sources", "AI wrong answers", "improve AI accuracy", "AI best practices"]
applies_when: "When a merchant asks how to train their AI assistant effectively or why their AI gives wrong answers"
priority: "high"
```

## AI Training Overview

AI training is the process of teaching your AI assistant to understand your business and respond accurately to customer questions. High-quality, relevant data produces the best results.

## Step 1: Plan Your Training Content

Organize information into categories before you start adding data:

| Content category | What to include | How to add |
|---|---|---|
| Product information | Details, specs, variants, pricing | Sync products; add FAQs per product |
| Store information | Business hours, contact details, locations | Sync store data |
| Shipping & delivery | Methods, costs, delivery times | Sync FAQs or add custom Q&A |
| Returns & refunds | Policy details, steps, timeframes | Sync FAQs or add custom Q&A |
| Product-specific topics | Care instructions, warranties, compatibility | Add Q&A to custom data source or per product |
| Special scenarios | Holiday shipping, seasonal sales, event policies | Go to Instructions → Add custom scenarios |

## Step 2: Best Practices per Data Source

**Products:**
- Write detailed product descriptions with specifications
- Use consistent naming for variants
- Keep pricing updated
- For specific product recommendations, create Smart recommendations

If you sync Markets data, AI can answer region-specific questions about pricing and availability, and send product links with regional variations.

**Limitations to be aware of:**
- AI cannot identify bestsellers without Smart recommendations
- AI can only suggest complementary products if they're mentioned in product descriptions

---

<!-- CHUNK: train-ai-instructions -->
```yaml
chunk_id: "faq__train-ai-instructions"
doc_id: "chatty-train-ai"
title: "How to add custom instructions and scenario instructions to the AI"
category: "faq"
subcategory: "ai-assistant"
tags: ["custom instructions", "scenario instructions", "AI personality", "AI tone", "keyword triggers", "AI scenarios", "complaint handling"]
applies_when: "When a merchant asks how to add custom instructions or scenario-based instructions to control AI behavior"
priority: "high"
```

## Step 3: Add Custom Instructions

After adding data sources, customize how AI communicates:

- **Name & avatar**: How your bot appears to customers
- **Welcome message**: First message in chat
- **Custom instructions**: AI's personality, tone, role, and response boundaries
- **AI skills**: Shopping skills and customer support skills

## Step 4: Add Scenario Instructions

Scenario instructions train AI to handle specific situations when customers use certain keywords.

**How to add a scenario:**

1. Go to Instructions → Scenarios
2. **Name your scenario** — e.g., "Product return request", "Shipping delays"
3. **Set keywords** — words that trigger this scenario (include variations and synonyms): e.g., "refund", "return", "money back", "send back"
4. **Write instructions** — specific guidance for AI when this scenario triggers (max 1000 characters)
5. **Set status** — Active or Inactive

**Common scenarios to set up:**
- Product recommendations
- Order returns and refunds
- Shipping inquiries
- Complaint handling
- Promotional offers
- Technical support

**Example scenario — Customer expressing strong dissatisfaction:**

Instructions:
1. Acknowledge frustration: "I understand how disappointing this must be"
2. Apologize sincerely
3. Offer immediate solutions: refund, exchange, or store credit
4. Escalate to human: connect with a team member who can resolve this personally
5. Never argue — focus only on solutions

---

<!-- CHUNK: train-ai-custom-instructions-writing -->
```yaml
chunk_id: "faq__train-ai-custom-instructions-writing"
doc_id: "chatty-train-ai"
title: "How to write good custom instructions — structure and example"
category: "faq"
subcategory: "ai-assistant"
tags: ["write AI instructions", "custom instructions example", "AI role", "AI knowledge", "AI avoid", "AI instruction format", "generate with AI"]
applies_when: "When a merchant asks how to write good custom instructions or what format to use"
priority: "medium"
```

## How to Write Good Custom Instructions

Yes — custom instructions let you shape AI's personality, role, response style, and what it should or shouldn't say.

**Structure your instructions clearly, for example:**

```
ROLE:
- Act as a helpful customer support associate for [Store Name]
- Refer to yourself as "I" and the store as "we"

KNOWLEDGE:
- You know about our products, policies, and pricing
- If you don't know something, say so and suggest contacting our team

APPROACH:
- Keep responses conversational but professional
- Include product details (dimensions, materials, colors) when relevant
- Suggest complementary products when appropriate

AVOID:
- Don't make definitive claims about exact stock levels
- Don't promise specific delivery dates
- Don't make up product specifications
```

You can manually write instructions or use the **Generate with AI** button to create a starting point based on your business type.


---

---
category: Common Issues
topic: Translation & Multi-language Issues
source: notion/Chatty FAQs
---

Q: FAQ page translation is not working when switching languages on the store.
Q: The FAQ content doesn't change when the customer switches language.
A: This is commonly caused by a third-party translation app (e.g., Translate & Adapt, T Lab) overwriting Chatty's FAQ meta content.

**Support flow:**
1. Ask the merchant if they use any third-party translation app.
2. If using Translate & Adapt: check the meta content of the affected language for overwritten Chatty rows.
3. Remove the overriding content from the third-party app.
4. If the issue persists after removing overrides, create a tech support card for deeper investigation.
5. If unclear, request app permissions to investigate or escalate to TS.

---

Q: Translation status shows "Outdated" for a language in the Translations section.
Q: Why does a language show as Outdated in Chatty translations?
A: The FAQ content hasn't been translated after the app updated its content, or the FAQ was never translated for that language.

**Solution:**
1. Go to the FAQ section in Translations.
2. **Paid plan merchants:** Use "Auto-translate" to automatically translate the FAQ.
3. **Free plan merchants:** Must manually translate the FAQ content.
4. After translating, save and verify the status changes from "Outdated" to "Updated."

---

# Translation

<!-- CHUNK: translation-overview -->
```yaml
chunk_id: "translation__overview"
doc_id: "chatty-translation"
title: "How translation works in Chatty — multilingual chatbox"
category: "translation"
tags: ["translation", "multilingual", "language", "chatbox language", "add language", "supported languages"]
applies_when: "Merchant asks how translation works or how to show the chatbox in different languages"
```

## Translation Overview

The Translation feature automatically translates all chatbox content (FAQs labels and chatbox UI) into your selected languages. Available for all Chatty users.

**How it works:** The chatbox shows in the Default language for all users. If you publish additional languages, visitors whose browser language matches will see the chatbox in their language automatically.

**Supported languages (19):** English, Spanish, French, Portuguese, German, Dutch, Italian, Turkish, Vietnamese, Hindi, Urdu, Chinese (Simplified), Chinese (Traditional), Arabic, Malay, Japanese, Greek, Romanian, Norwegian. For languages not in this list, select **Custom** to add translations manually.

**How to publish a new language:**
1. Go to **Settings** → **Translation** → click **Add language**
2. The language appears in "Unpublished language" and is auto-translated
3. Click **Edit** to review and modify the translation (Chatbox, FAQs page, FAQ questions/answers)
4. Click **Auto-translate** to translate all at once, or edit manually
5. After editing, click **Save** → settings icon → **Publish** → Confirm

**Set the default language:**
Go to **Settings** → **Translation** → click the settings icon next to the language → **Change default** → **Save**.

**Keep translations up to date:** When you add new FAQ categories or questions, translations are **NOT** updated automatically. Chatty will show a banner and mark outdated languages. Click **Edit** on the language and re-translate the new content.

---

<!-- CHUNK: translation-realtime -->
```yaml
chunk_id: "translation__realtime"
doc_id: "chatty-translation"
title: "Real-time translation for conversations between agents and customers"
category: "translation"
tags: ["real-time translation", "live translation", "agent translation", "conversation translation", "Pro plan"]
applies_when: "Merchant asks about real-time translation of conversations in the inbox"
```

## Real-Time Conversation Translation

**Real-time Translation** is available on **Pro and Plus plans**. It allows automatic translation between the agent's language and the customer's language within the Inbox.

Go to **Settings** → **Translation** to configure languages.

---

<!-- CHUNK: translation-language-limits -->
```yaml
chunk_id: "translation__language-limits"
doc_id: "chatty-translation"
title: "How many languages does auto-translation support per plan"
category: "translation"
tags: ["language limit", "auto-translation", "how many languages", "plan limit", "translation limit"]
applies_when: "Merchant asks how many languages are supported for translation per plan"
```

## Translation Language Limits

| Plan | Languages |
|------|-----------|
| Free | 1 language |
| Basic | 2 languages |
| Pro | 9 languages |
| Plus | Unlimited |

Languages must be added in **Shopify Admin** → **Settings** → **Languages** first before they appear in Chatty's translation settings.


---

# Web App

<!-- CHUNK: web-app-overview -->
```yaml
chunk_id: "faq__web-app-overview"
doc_id: "chatty-web-app"
title: "What the Chatty web app is and how to access it without Shopify"
category: "faq"
subcategory: "web-app"
tags: ["web app", "app.meetchatty.com", "access chatty", "standalone app", "team access", "non-shopify access"]
applies_when: "When a merchant or team member asks how to access Chatty outside of Shopify admin or what the web app is"
priority: "high"
```

## Chatty Web App Overview

The Chatty web app is a standalone version you can access directly at https://app.meetchatty.com/ — without logging into Shopify admin. It's ideal for team members who don't have Shopify admin access.

Both Shopify admins and invited team members can use the web app once they have a Chatty account.

You can also access Chatty from the Shopify Apps section or directly at https://app.chatty.net. The web app offers a more complete experience and is recommended for full inbox management.

---

<!-- CHUNK: web-app-login -->
```yaml
chunk_id: "faq__web-app-login"
doc_id: "chatty-web-app"
title: "How to log in to the Chatty web app as admin or team member"
category: "faq"
subcategory: "web-app"
tags: ["login web app", "activate web app", "team member login", "create account", "web app password", "change password", "Google login"]
applies_when: "When a merchant or team member asks how to log in to the Chatty web app or how to set up their account"
priority: "high"
```

## How to Log In as an Admin

1. In the Chatty app, look for the **Web app activation** notice in:
   - Dashboard
   - Settings → Team
   - Chatbox → Live chat in Blocks
2. Click **Activate**
3. Create a password for your Chatty account
   - Your login email is your Shopify default email (contact support to change this)
4. Go to https://app.meetchatty.com/ and log in

If your email is linked to another store, click **Activate** to use the same account for both stores. You can switch between stores in the web app.

## How to Log In as a Team Member

1. Check your email for the invitation from Chatty
2. Click **Create account**
3. Create your password
4. Go to https://app.meetchatty.com/ and log in

## How to Change Your Password

1. Log in to https://app.meetchatty.com/
2. Click the icon in the top-right corner → **My account**
3. Click **Change password** and enter a new one

If you logged in with Google and haven't set a password before, click **Reset password** to create one.

---

<!-- CHUNK: web-app-two-step-verification -->
```yaml
chunk_id: "faq__web-app-two-step-verification"
doc_id: "chatty-web-app"
title: "Two-step verification when logging into Chatty from a new device"
category: "faq"
subcategory: "web-app"
tags: ["two-step verification", "2FA", "verification code", "new device login", "security code", "resend code"]
applies_when: "When a merchant or team member asks about the verification code they receive when logging in from a new device"
priority: "medium"
```

## Two-Step Verification

When logging in from a new device or browser, Chatty sends a verification code to your registered email for security.

1. Log in with email and password
2. Check your email for the verification code
3. Enter the code to complete login

If you don't receive the code:
- Check your spam/junk folder
- Click "Resend code" on the verification screen
- Make sure you're using the email registered with Chatty

## Accessing Chatty from Mobile

In the Chatty app dashboard, go to **Inbox** and click the "Open Web App" or "Download Chatty App" button. You can also access app.chatty.net directly from your mobile browser.


---

# Website Integration

<!-- CHUNK: website-integration-overview -->
```yaml
chunk_id: "faq__website-integration-overview"
doc_id: "chatty-website"
title: "How to add Chatty to a non-Shopify website using a code snippet"
category: "faq"
subcategory: "integrations"
tags: ["website integration", "non-shopify", "external website", "blog chatty", "install chatty website", "code snippet", "HTML embed", "WordPress", "Wix"]
applies_when: "When a merchant asks how to add Chatty to a website that is not on Shopify, like a blog or landing page"
priority: "medium"
```

## Website Integration Overview

Website integration lets you add Chatty to any website you own — not just your Shopify store. Customers on your blog, landing page, or any custom website can chat with you, and all those conversations flow into the same Chatty inbox.

## How to Add Chatty to Your Website

1. From Chatty admin, go to **Settings** → **Integrations** → **Manage** in Website integration
2. Your unique code snippet is automatically generated
3. Select code type: `HTML` or `Liquid`
4. Click **Copy**
5. In your website's HTML, locate the `<body>` section
6. Paste the code snippet just before the closing `</body>` tag
7. Save your changes

The Chatty chat widget will appear on your website within a few minutes.

## How It Works

- Customers see the same Chatty widget as on your Shopify store
- AI assistant responds using your trained data sources
- All conversations from external websites flow into your single Chatty inbox

## Common Questions

- **Can I add Chatty to multiple websites?** Yes — use the same code snippet on as many websites as you want. All conversations flow into one inbox.
- **Will this slow down my website?** No — the Chatty widget loads asynchronously and doesn't affect page loading speed.
- **What if I need to remove Chatty from my website?** Simply delete the code snippet from your HTML.
- **Does this work with WordPress, Wix, or other website builders?** Yes — as long as you can add custom HTML code, the integration will work. Most website builders have a "Custom code" section where you can paste the snippet.


---

---
category: Common Issues
topic: WhatsApp & Messenger Channel Issues
source: notion/Chatty FAQs
---

Q: What does a merchant need to connect WhatsApp to Chatty?
Q: WhatsApp connection requirements checklist.
A: The merchant needs all of the following:

**1. Meta Business Manager account**
- Must have a valid Meta Business Manager with **Business Admin** role.
- Employee role is NOT sufficient — admin access is required.
- Check at: business.facebook.com/settings/people

**2. Valid WhatsApp phone number**
- A phone number NOT currently registered on WhatsApp personal app.
- Or an existing WhatsApp Business number that has been migrated to Cloud API.
- OTP verification must be via SMS or phone call (not WhatsApp app).

**3. Valid business information**
- Business name, type, legal address, website domain.
- Meta may require Business Verification for full features.

**4. Permissions during OAuth**
- Must select their Business Manager, WhatsApp Business Account, and phone number.
- Must grant "AVADA group company limited" permission to manage the number.

**5. Correct Facebook login**
- Facebook account must be added to the Business Manager with proper permissions.
- Browser must not block popups or third-party cookies.

**6. No other WhatsApp API provider**
- If the number is currently connected to another provider (Twilio, 360dialog, etc.), it must be released/migrated first before connecting to Chatty.

---

Q: The merchant connected WhatsApp but it's not working.
Q: WhatsApp connection issues with Chatty.
A: Common WhatsApp connection issues:

1. **Insufficient permissions:** The person connecting must be a Business Admin (not Employee) in Meta Business Manager.
2. **Phone number already in use:** The number is active on WhatsApp personal app or connected to another API provider.
3. **Business verification pending:** Meta requires business verification for full features.
4. **Browser blocking popups:** The OAuth popup may be blocked — advise trying a different browser or disabling popup blockers.

For all WhatsApp issues, verify each item on the checklist above before escalating.

---

Q: Facebook Messenger is connected but new messages don't appear in Chatty.
Q: Messages from Facebook are not showing in Chatty inbox.
A: Check these common causes:

1. **Integration not complete:** Ensure the merchant has fully integrated Messenger with Chatty (all steps completed in the Channels section).
2. **Insufficient page permissions:** The person who connected must have "Manage and access Page messages" permission. Check Page Settings > Page Roles & Permissions.
3. **Permission deselection during setup:** If the merchant deselected items during the Facebook OAuth popup, permissions may be incomplete.
4. **Messages sent before connection:** Only messages sent AFTER Chatty is connected will sync. Old messages must be handled directly in Facebook Messenger.

---

Q: Messages from Meta (Facebook/Instagram) are not showing in Chatty.
Q: Instagram messages not appearing in the Chatty inbox.
A: Similar to Messenger issues — verify:

1. The channel (Messenger or Instagram) is properly connected in Chatty's Channel settings.
2. The connecting user has admin access to the Facebook page.
3. All permissions were granted during the OAuth connection process.
4. Only new messages (sent after connection) will appear in Chatty.

If all settings are correct but messages still don't sync, collect the details and escalate to the TS team.

---

Q: My WhatsApp number is showing as "Pending" after connecting. What do I do?
A: Pending status means the Meta verification is still in progress. This typically takes 24–48 hours.

To resolve this, make sure:
1. Your WhatsApp Business account is fully verified
2. The phone number is not already registered with another WhatsApp Business API provider
3. Two-factor authentication (2FA) for your phone number is enabled

If it stays Pending beyond 48 hours, please contact our support team so we can help further.

---

Q: My WhatsApp number is already connected to another app. Can I switch to Chatty?
A: Meta policy allows a WhatsApp Business API number to be managed by only one Business Solution Provider (BSP) at a time. To switch to Chatty, you must either migrate the number (disconnect from the current BSP and reconnect via Meta Business Manager) or create a new WhatsApp Business Account and associate the same phone number with it. Contact support for guidance on the migration process.

---

Q: Can I use Chatty AI to answer WhatsApp messages without showing the widget on my website?
A: Yes — once WhatsApp is connected, go to **AI Assistant** → **Settings** and enable the AI for the WhatsApp channel. The AI will respond to WhatsApp messages using the same training data and settings as the website chatbox. Access WhatsApp conversations via the Inbox → WhatsApp tab.

---

Q: Can I initiate (send first) WhatsApp messages to customers from Chatty?
A: No — Chatty currently only supports responding within existing WhatsApp conversations. You cannot initiate new outbound WhatsApp messages from Chatty to contacts who haven't messaged you first.

---

Q: Instagram story replies are showing an error in Chatty's Inbox.
A: Chatty currently supports Instagram text and image messages only. Unsupported message types include: story replies, reel shares, voice messages/audio, stickers, post shares, and vanish mode messages. The team is working on expanding support for these formats.

---

Q: Messages I send directly in Instagram/Facebook Messenger are not showing in Chatty Inbox.
A: Replies made directly in the Meta platform (not via Chatty) may not sync back to the Chatty inbox. This is a known limitation — a feature request has been filed to improve sync coverage for replies made outside of Chatty.

---

Q: The AI is not responding to Instagram messages.
A: Go to **AI Assistant** → **Settings** and check if the AI is enabled for the Instagram channel — there is a per-channel toggle. Enable it and the AI will start responding automatically. Previously unhandled messages will continue to be assigned to agents by default until the toggle is on.

---

# Zendesk Integration

<!-- CHUNK: zendesk-integration-overview -->
```yaml
chunk_id: "faq__zendesk-integration-overview"
doc_id: "chatty-zendesk"
title: "How Chatty integrates with Zendesk to save resolved conversations as tickets"
category: "faq"
subcategory: "integrations"
tags: ["zendesk", "zendesk integration", "support tickets", "conversation history", "zendesk sync", "resolved conversations", "ticket creation"]
applies_when: "When a merchant asks how to connect Zendesk to Chatty or how conversations are saved to Zendesk"
priority: "medium"
```

## Zendesk Integration Overview

The Zendesk integration automatically saves resolved Chatty conversations to Zendesk as support tickets. When you resolve a conversation in Chatty, a ticket is created in Zendesk with the full conversation transcript and customer details.

**Why integrate Zendesk:**
- Automatically save all resolved conversations as Zendesk tickets
- Keep complete conversation history in one central system
- Track support performance across all channels
- Access customer records without manual work

## How to Connect

1. Go to **Settings** → **Integrations** → Find Zendesk → Click **Manage**
2. Enter your **Zendesk subdomain** (the first part of your Zendesk URL — e.g., if your URL is `yourstore.zendesk.com`, the subdomain is `yourstore`)
3. Click **Connect** → You'll be redirected to Zendesk's OAuth page
4. Click **Allow** to authorize Chatty
5. You'll be redirected back to Chatty with connection status showing **Connected**

## How It Works

**Automatic ticket creation:** When you resolve a conversation in Chatty, a ticket is created in Zendesk containing:
- Customer profile (name, email, contact details)
- Full conversation transcript
- Timestamp of the conversation

**Reopened conversations:** If you reopen and re-resolve a conversation, Chatty creates a new ticket instead of updating the existing one, so each support interaction is tracked separately.

> Note: Sync happens on resolution, not in real-time. To use Zendesk as long-term chat history storage, resolve conversations in Chatty to trigger the sync.


---

# Asking for Shopify Reviews — CS Process Guide

<!-- CHUNK: ref-ask-for-review-timing -->
```yaml
chunk_id: "ref__ask-for-review-timing"
doc_id: "cs-ref-ask-for-review"
title: "When to ask (and when not to ask) for a Shopify App Store review"
category: "cs-process"
subcategory: "review-request"
tags: ["review", "ask for review", "timing", "Shopify review", "high_risk", "don't_ask_for_review"]
applies_when: "CS is deciding whether it's appropriate to ask a merchant for a review"
priority: "high"
```

## When to Ask

- Merchant has used the app and seen value from it
- Merchant expresses satisfaction, says thank you, or compliments the support
- After successfully resolving a specific issue or question
- After handling 1–2 initial requests successfully — don't wait to finish everything if the merchant is already happy
- Remaining requests are customization or nice-to-haves (not blockers)
- All main questions have been answered

## When NOT to Ask

- Merchant hasn't seen value yet / still in early setup
- Conversation is tagged `high_risk` or `don't_ask_for_review`
- During onboarding (before they've had a chance to experience the app)
- Merchant is frustrated, has an unresolved issue, or complained
- You just unlocked a feature from DevZone or removed branding (unless told otherwise by CSL)
- Merchant already declined or didn't respond after the first ask — don't repeat

---

<!-- CHUNK: ref-ask-for-review-flow -->
```yaml
chunk_id: "ref__ask-for-review-flow"
doc_id: "cs-ref-ask-for-review"
title: "How to ask for a Shopify review — 3-step process"
category: "cs-process"
subcategory: "review-request"
tags: ["review", "ask for review", "template", "shortcut", "rv-done", "3 steps", "review link"]
applies_when: "CS is ready to ask a merchant for a review and needs to know the correct process"
priority: "high"
```

## 3-Step Review Request Flow

**Step 1: Ask permission first**

Don't send the review link out of nowhere. Start with:
> *"While you're here, may I ask for a quick favor?"*

This makes the merchant feel respected rather than pushed.

**Step 2: Send the review template**

After they agree, use the pre-approved shortcut (`!chatty-rv`, `!joy-rv`, etc.) from the **Ask for reviews** category in Message Shortcuts. Don't write your own — use the prepared template.

Example of what the template looks like:
> *"Would you mind leaving a quick review for our support and app via this link? It only takes a few seconds and we really appreciate your feedback!"*

**Step 3: Follow up after sending**

After sending the link, use shortcut `!rv-done`:
> *"I'd be so grateful if you could update me once it's done so I can thank you in time!"*

Or more casual: *"I can't wait to see it!"* / *"So excited to see your review!"*

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


---

# Case Handling Playbook

<!-- CHUNK: ref-case-handling-classification -->
```yaml
chunk_id: "ref__case-handling-classification"
doc_id: "cs-ref-case-handling"
title: "Case Classification — How to categorize incoming merchant requests"
category: "cs-process"
subcategory: "case-handling"
tags: ["case classification", "how-to", "bug", "feature request", "billing", "complaint", "pre-sales", "discount", "demo"]
applies_when: "CS receives a new merchant request and needs to classify it"
priority: "high"
```

## Case Classification

When a merchant reaches out, first determine: does the merchant have a **question** or a **problem**? Then classify:

| Case Type | Examples | Handler |
|-----------|----------|---------|
| **How-to Questions** | "How do I set up X?", "Where can I find Y?" | CS Agent |
| **Bug/Issue Reports** | "Feature X is broken", "Widget not showing" | CS → TS → Dev |
| **Feature Requests** | "Can you add X?", "Integration with Y?" | CS Agent → PM |
| **Billing & Subscription** | "Why was I charged?", "How do I upgrade?" | CS Agent (CS Leader for refunds) |
| **Complaints** | "Your app is terrible!", "I've been waiting for days" | CS Agent → CS Leader |
| **Pre-sales Questions** | "Does your app do X?", "How much does it cost?" | CS Agent |
| **Integration Questions** | "Can this work with X?", "How do I connect Y?" | CS (basic) → TS (complex) |
| **Discount Requests** | "Can I get a discount on the plan?" | CS Agent → CS Leader/Sales |
| **Demo Requests** | "Can you show me how this works?" | CS Agent (schedule) |

---

<!-- CHUNK: ref-case-handling-how-to -->
```yaml
chunk_id: "ref__case-handling-how-to"
doc_id: "cs-ref-case-handling"
title: "How to handle How-to Questions from merchants"
category: "cs-process"
subcategory: "case-handling"
tags: ["how-to", "knowledge base", "step-by-step", "helpcenter", "confirm"]
applies_when: "Merchant asks a how-to question (setup, navigation, feature usage)"
priority: "medium"
```

## How-to Questions

1. Check knowledge base for the answer
2. Provide step-by-step answer with navigation paths
3. Link to relevant helpcenter article
4. Follow up to confirm it worked

---

<!-- CHUNK: ref-case-handling-bugs -->
```yaml
chunk_id: "ref__case-handling-bugs"
doc_id: "cs-ref-case-handling"
title: "How to handle Bug and Issue Reports from merchants"
category: "cs-process"
subcategory: "case-handling"
tags: ["bug", "issue", "triage", "troubleshooting", "escalate", "TS", "Trello", "evidence", "reproduce"]
applies_when: "Merchant reports a bug or technical issue"
priority: "high"
```

## Bug/Issue Reports

1. **Triage** — is it a bug or a configuration issue?
2. **Basic troubleshooting** — check settings, clear cache, try another browser
3. **Gather evidence** — screenshots, steps to reproduce, store URL, plan
4. **If config issue** → guide the merchant to fix it
5. **If confirmed bug** → escalate to TS via Trello card

---

<!-- CHUNK: ref-case-handling-feature-requests -->
```yaml
chunk_id: "ref__case-handling-feature-requests"
doc_id: "cs-ref-case-handling"
title: "How to handle Feature Requests from merchants"
category: "cs-process"
subcategory: "case-handling"
tags: ["feature request", "PM", "product team", "no promise", "timeline", "forward"]
applies_when: "Merchant requests a new feature or integration"
priority: "medium"
```

## Feature Requests

1. Understand what the merchant is trying to achieve
2. Check if an existing feature already solves their need
3. If no existing solution → document the request and forward to PM
4. Don't promise features or timelines — say "I'll pass this to our product team"

---

<!-- CHUNK: ref-case-handling-complaints -->
```yaml
chunk_id: "ref__case-handling-complaints"
doc_id: "cs-ref-case-handling"
title: "How to handle Complaints — SLA, escalation triggers, and approach"
category: "cs-process"
subcategory: "case-handling"
tags: ["complaint", "SLA", "2 hours", "escalate", "CS Leader", "VIP", "legal threat", "negative review", "refund"]
applies_when: "Merchant is complaining, angry, or escalating an issue"
priority: "high"
```

## Complaints

**SLA: respond within 2 hours.**

1. Respond quickly — don't leave an angry merchant waiting
2. Stay professional — don't take it personally
3. Understand root cause — what actually went wrong?
4. Take ownership — apologize for their experience
5. Provide a solution — specific action plan with realistic timeline
6. Follow through — do what you promised, update proactively
7. Document and share with the team

**Escalate to CS Leader when:**
- After 2 attempts, merchant is still angry
- Merchant threatens legal action or public negative review
- Issue involves refund or compensation
- VIP merchant complaint

---

<!-- CHUNK: ref-case-handling-presales -->
```yaml
chunk_id: "ref__case-handling-presales"
doc_id: "cs-ref-case-handling"
title: "How to handle Pre-sales Questions — SLA and approach"
category: "cs-process"
subcategory: "case-handling"
tags: ["pre-sales", "SLA", "4 hours", "potential customer", "free trial", "honest", "capabilities"]
applies_when: "A potential merchant asks about Chatty features, pricing, or capabilities before installing"
priority: "medium"
```

## Pre-sales Questions

**SLA: respond within 4 hours.**

1. Respond fast — these are potential customers
2. Understand their needs
3. Be honest about capabilities — don't oversell
4. Guide them to free trial
5. Share relevant helpcenter links or demo

---

<!-- CHUNK: ref-case-handling-other -->
```yaml
chunk_id: "ref__case-handling-other"
doc_id: "cs-ref-case-handling"
title: "How to handle Integration Questions and Discount Requests"
category: "cs-process"
subcategory: "case-handling"
tags: ["integration", "native", "third-party", "custom", "TS", "discount", "CS Leader", "sales manager"]
applies_when: "Merchant asks about integrations or requests a discount"
priority: "medium"
```

## Integration Questions

1. Identify the integration type (native, third-party, custom)
2. For native integrations → provide setup guide
3. For complex/custom integrations → escalate to TS

## Discount Requests

1. Listen to the merchant's reasoning
2. Escalate to CS Leader or Sales Manager — CS agents do not have authority to approve discounts


---

# Handling Sensitive Situations

<!-- CHUNK: ref-sensitive-personal-info -->
```yaml
chunk_id: "ref__sensitive-personal-info"
doc_id: "cs-ref-handle-sensitive-situations"
title: "How to handle a customer asking for CS agent's personal information"
category: "cs-process"
subcategory: "sensitive-situations"
tags: ["personal info", "personal information", "privacy", "social media", "phone number", "decline", "redirect"]
applies_when: "A customer asks for the CS agent's personal information (social media, phone number, etc.)"
priority: "high"
```

## Resolution Steps

**1. Politely decline and redirect to app support:**
> "Sorry, I can't share personal information. If you need help with the app, I'll be happy to assist."

**2. If they ask again, be firm:**
> "As I mentioned, I cannot share personal information. Please keep the conversation related to the app."
> "I can only respond to questions related to the app. Let's please keep the conversation focused on that."

**3. If they persist, end the conversation:**
> "I can only support with the app. If you need help with the app later, please feel free to reach out again."

Then close the chat.

---

<!-- CHUNK: ref-sensitive-harassment -->
```yaml
chunk_id: "ref__sensitive-harassment"
doc_id: "cs-ref-handle-sensitive-situations"
title: "How to handle harassment or abusive language from a customer"
category: "cs-process"
subcategory: "sensitive-situations"
tags: ["harassment", "abusive language", "insults", "offensive", "end chat", "warn", "sexual harassment"]
applies_when: "A customer is using harassing, insulting, or sexually offensive language toward the CS agent"
priority: "high"
```

## Resolution Steps

**1. Remind them to be respectful:**
> "Your message is inappropriate. Please keep the conversation respectful so I can assist you."

**2. Warn if it continues:**
> "This kind of language is not acceptable. If it continues, I will need to end this conversation."

**3. End and report:**
> "I'm ending this chat due to repeated inappropriate language. If you need help with the app in the future, please contact us respectfully."

**Note:** In cases of sexual harassment, a female CS agent may transfer the case to a male colleague as a temporary measure. However, no one is required to continue supporting a harassing customer — always follow the warn → end chat flow if behavior is serious.

---

<!-- CHUNK: ref-sensitive-spam -->
```yaml
chunk_id: "ref__sensitive-spam"
doc_id: "cs-ref-handle-sensitive-situations"
title: "How to handle a customer spamming or repeatedly asking the same question"
category: "cs-process"
subcategory: "sensitive-situations"
tags: ["spam", "repeated messages", "slow response", "pacing", "end chat"]
applies_when: "A customer is spamming or repeatedly asking the same off-topic questions"
priority: "medium"
```

## Resolution Steps

You do not need to reply immediately to spam or repeated personal questions:

- **Slow down your response by 2–3 minutes** to reduce the conversation pace. This subtly signals these are not priority questions.
- Reply with a short, consistent script — no need to change reasoning each time.
- After 1–2 slow reminders, if they still persist → **warn and end the chat**.

---

<!-- CHUNK: ref-sensitive-blocking -->
```yaml
chunk_id: "ref__sensitive-blocking"
doc_id: "cs-ref-handle-sensitive-situations"
title: "When CS can block a customer vs. when to escalate — dev store vs. real store"
category: "cs-process"
subcategory: "sensitive-situations"
tags: ["block", "dev store", "real store", "escalate", "CS Leader", "after warning"]
applies_when: "CS is deciding whether to block a customer after repeated violations"
priority: "high"
```

## Blocking Decision

**Dev store** (check CRM — cannot write reviews, no retention value):
- CS has the authority to **block immediately** after warning.
- Note the reason for blocking in the chat.
- Inform your leader for awareness.

**Real store** (can write reviews):
- CS should **report to the CS Leader** and let them decide the next steps.
- Do not block on your own — escalate first.

---

<!-- CHUNK: ref-sensitive-principles -->
```yaml
chunk_id: "ref__sensitive-principles"
doc_id: "cs-ref-handle-sensitive-situations"
title: "Core principles for handling all sensitive situations"
category: "cs-process"
subcategory: "sensitive-situations"
tags: ["principles", "professional", "personal info", "spam", "dev store", "real store", "guidelines"]
applies_when: "General reference for how to behave in any sensitive or difficult conversation"
priority: "medium"
```

## Core Principles

1. **Never reveal personal information** — keep all interactions professional and app-focused.
2. **Stay professional** — do not argue, do not respond to insults with insults.
3. **Give 2–3 reminders** → then warn and end the chat if behavior continues.
4. **When customers spam** → slow down replies to reduce the conversation pace.
5. **Dev stores** → CS can block on their own after warning.
6. **Real stores** → always report to the CS Leader for further handling.


---

# Chatty — Knowledge Base

<!-- CHUNK: ref-kb-overview -->
```yaml
chunk_id: "ref__kb-overview"
doc_id: "cs-ref-knowledge-base"
title: "Chatty product overview — what it is, key stats, plans"
category: "product-knowledge"
subcategory: "overview"
tags: ["overview", "Chatty", "Shopify app", "AI chatbot", "live chat", "plans", "pricing", "4.9 stars"]
applies_when: "CS needs a product overview or plan reference for Chatty"
priority: "high"
```

## Product Overview

Chatty is a Shopify app that helps merchants communicate with store visitors via live chat, automate customer support with an AI chatbot (powered by ChatGPT), and build self-serve FAQ help centers. Designed as an AI-first chat platform for eCommerce. Built for Shopify badge. 4.9 stars with 1,700+ reviews.

## Plans

| Feature | Free | Basic ($19.99/mo) | Pro ($68.99/mo) | Plus ($199.99/mo) |
|---------|------|--------------------|------------------|---------------------|
| AI conversations | 50 lifetime | 50/month | 300/month | 700/month |
| Additional conversations | N/A | $0.40 each | $0.40 each | $0.40 each |
| Products for AI training | 100 | 500 | 8,000 | 20,000 |
| Team members | 1 | 5 | 10 | Unlimited |
| Auto-translation languages | 1 | 2 | 9 | Unlimited |
| Chat history | 90 days | Unlimited | Unlimited | Unlimited |
| Email channel | 1 | 1 | 1 | 1 |
| Smart product recommendations | No | No | Yes | Yes |
| CSAT survey | No | No | Yes | Yes |
| Cart booster | No | No | Yes | Yes |
| Dedicated AI consultant | No | No | No | Yes |

Annual billing: ~15% savings. 7-day free trial for paid plans. 30-day money-back guarantee.

---

<!-- CHUNK: ref-kb-live-chat -->
```yaml
chunk_id: "ref__kb-live-chat"
doc_id: "cs-ref-knowledge-base"
title: "Chatty Live Chat features — inbox, channels, contacts, team, quick replies"
category: "product-knowledge"
subcategory: "live-chat"
tags: ["live chat", "inbox", "channels", "contacts", "team", "quick replies", "proactive chat", "real-time translation", "Messenger", "Instagram", "WhatsApp", "email"]
applies_when: "CS needs a reference on live chat features in Chatty"
priority: "medium"
```

## Live Chat

Real-time messaging between merchants and store visitors.

- **Inbox**: Unified inbox to manage all conversations. Includes customer details panel, conversation details, chat zone.
- **Channels**: Email, Facebook Messenger, Instagram, WhatsApp — all synced into one inbox.
- **Contacts**: Customer management with tags, notes, and conversation history.
- **Team**: Invite team members, assign roles, manage conversation assignments.
- **Quick Replies**: Pre-saved response templates for faster replies.
- **Proactive Chat**: Behavior-triggered messages to engage visitors (time on page, specific page visit).
- **Real-time Translation**: Auto-translate messages between merchant and customer languages (Pro+ only).

---

<!-- CHUNK: ref-kb-ai-assistant -->
```yaml
chunk_id: "ref__kb-ai-assistant"
doc_id: "cs-ref-knowledge-base"
title: "Chatty AI Assistant features — data sources, skills, settings, test zone"
category: "product-knowledge"
subcategory: "ai-assistant"
tags: ["AI assistant", "data sources", "products", "custom answers", "URL", "file", "AI skills", "smart recommendations", "size guide", "order tracking", "AI settings", "test"]
applies_when: "CS needs a reference on AI assistant features in Chatty"
priority: "medium"
```

## AI Assistant

AI-powered chatbot that handles customer questions 24/7, trained on the merchant's store data.

**Data Sources:**
- *Store data (auto-synced)*: Products, discounts, markets, FAQs, policies (shipping, return, privacy, terms). Products sync daily at 12:00 AM PST. Only published, in-stock products are trained.
- *Custom data (manual)*: Individual questions, URLs/websites, files (.JSON, .TXT, .PDF, .CSV — max 2MB).

**AI Skills:**
- *Shopping*: Smart recommendations (bestsellers, new arrivals, sales, special occasions — auto top 20 by sales, updated daily), size guide, inventory status.
- *Customer support*: Transfer to human, refund/return form, order tracking in chat.

**AI Settings:** Bot name, avatar, welcome message, custom instructions, AI availability, AI channels.

**Test & Optimize:** Test zone to preview AI responses without affecting AI quota. Review unresolved questions to improve training.

---

<!-- CHUNK: ref-kb-chatbox -->
```yaml
chunk_id: "ref__kb-chatbox"
doc_id: "cs-ref-knowledge-base"
title: "Chatty Chatbox features — appearance, advanced, contact button, embedded"
category: "product-knowledge"
subcategory: "chatbox"
tags: ["chatbox", "appearance", "display rules", "deep links", "contact button", "embedded chatbox", "advanced", "CSS", "launcher"]
applies_when: "CS needs a reference on chatbox features and settings"
priority: "medium"
```

## Chatbox

The chat widget displayed on the merchant's storefront.

- **General**: Turn on/off chatbox, enable chat focus mode, set header, configure blocks (Contact us, Order tracking, FAQs, Categories).
- **Appearance**: Brand colors (preset or custom), chatbox button (launcher icon, size, alignment), chatbox style (navigation mode, mobile ratio).
- **Advanced**: Deep links (open specific chatbox sections via URL), display rules (devices, pages), continue-as-email, custom CSS.
- **Contact Button**: Add contact methods — supports 11 methods: WhatsApp, Messenger, Phone, Email, Instagram, Telegram, Skype, Line, Zalo, TikTok, SMS.
- **Embedded Chatbox**: Embed chatbox directly in page content instead of as a floating widget.

---

<!-- CHUNK: ref-kb-faq-builder -->
```yaml
chunk_id: "ref__kb-faq-builder"
doc_id: "cs-ref-knowledge-base"
title: "Chatty FAQ Builder features — categories, questions, analytics, translation"
category: "product-knowledge"
subcategory: "faq-builder"
tags: ["FAQ builder", "categories", "questions", "FAQs page", "FAQs block", "FAQ analytics", "export", "translation"]
applies_when: "CS needs a reference on the FAQ builder feature"
priority: "medium"
```

## FAQ Builder

Build a self-serve knowledge hub:
- **Categories**: Organize questions with icons and descriptions.
- **Questions**: Add questions with rich text answers, assign to categories.
- **FAQs Page**: Dedicated FAQ page on the storefront with customizable theme.
- **FAQs Block**: Show selected FAQs inside the chatbox.
- **FAQs Analytics**: Track views, clicks, and search queries.
- **Export**: Export questions as CSV file.
- **Translation**: Translate FAQs into multiple languages.

---

<!-- CHUNK: ref-kb-channels -->
```yaml
chunk_id: "ref__kb-channels"
doc_id: "cs-ref-knowledge-base"
title: "Chatty channel details — Email, Facebook Messenger, Instagram, WhatsApp"
category: "product-knowledge"
subcategory: "channels"
tags: ["email channel", "Messenger", "Instagram", "WhatsApp", "connect", "forwarding", "noreply", "Facebook"]
applies_when: "CS needs details on how each channel works in Chatty"
priority: "medium"
```

## Channel Details

### Email Channel
- Connect one email to Chatty via email forwarding.
- Default sender: noreply@chattyemail.com (customizable with domain verification).
- "Continue as email" feature lets customers switch from live chat to email.
- Conversation history sent to customer when ticket is marked solved.

### Facebook Messenger & Instagram
- Connect via Facebook account — link fanpages to sync messages.
- Messages appear in Chatty inbox with platform icon indicators.
- Disconnecting doesn't remove existing conversations.

### WhatsApp
- Connect multiple WhatsApp accounts.
- Requires: Business Facebook page, WhatsApp Business account linked to that page, admin access to both.

---

<!-- CHUNK: ref-kb-integrations -->
```yaml
chunk_id: "ref__kb-integrations"
doc_id: "cs-ref-knowledge-base"
title: "Chatty integrations — Klaviyo, Zendesk, Joy, Air Reviews, Web"
category: "product-knowledge"
subcategory: "integrations"
tags: ["Klaviyo", "Zendesk", "Joy Loyalty", "Air Reviews", "Powerful Contact Form", "website", "integration"]
applies_when: "CS needs reference on what third-party integrations Chatty supports"
priority: "medium"
```

## Integrations

- **Klaviyo**: Sync customer data (contacts, tags, conversation counts, timestamps) to Klaviyo. Requires Klaviyo API key with Read/Write access for Lists and Profiles.
- **Zendesk**: Connect Zendesk for unified helpdesk management.
- **Joy Loyalty**: Show loyalty data (points, tier) in customer conversations.
- **Air Reviews**: Connect product reviews for AI training context.
- **Powerful Contact Form**: Integrate contact form submissions.
- **Website**: Connect external website for AI data training.

---

<!-- CHUNK: ref-kb-common-issues -->
```yaml
chunk_id: "ref__kb-common-issues"
doc_id: "cs-ref-knowledge-base"
title: "Chatty common issues quick reference"
category: "product-knowledge"
subcategory: "troubleshooting"
tags: ["chatbox not showing", "AI not responding", "email channel", "online status", "WhatsApp", "translation", "wrong products", "FAQ page", "order tracking", "products not appearing"]
applies_when: "Quick reference for diagnosing the most common Chatty issues"
priority: "high"
```

## Common Issues Quick Reference

- **Chatbox not showing**: Check chatbox is turned on (Chatbox → General → Turn on), app embed enabled in Shopify theme editor, display rules not excluding the page.
- **AI not responding**: Verify AI assistant is on, live chat block is enabled in chatbox, data sources are synced, AI has sufficient training data.
- **Email channel not connecting (Outlook)**: Organization's Outlook settings may block automatic email forwarding. Contact IT admin to allow it.
- **Online status not showing**: Contact Us block must be enabled — Chatbox → General → Blocks → turn on "Contact us".
- **WhatsApp not connecting**: Must have a Business Facebook page, WhatsApp Business account linked to it, and admin access to both.
- **Translation not showing on store**: Add and publish the language in Shopify Admin → Settings → Languages before enabling in Chatty.
- **AI recommending wrong products**: Check Smart Recommendations collections in AI Skills. Disable smart sync if auto-selected products aren't relevant.
- **FAQ page not showing after reinstall**: Check Shopify Admin → Online Store → Pages for orphaned FAQ pages.
- **Order tracking not working**: Ensure Order Tracking block is enabled in chatbox. Verify Shopify order tracking is set up.
- **Products not appearing in AI training**: Only published, in-stock products are trained. Products sync daily at 12:00 AM PST. Check count against plan limit.

---

<!-- CHUNK: ref-kb-navigation -->
```yaml
chunk_id: "ref__kb-navigation"
doc_id: "cs-ref-knowledge-base"
title: "Chatty correct UI navigation paths — where to find each setting"
category: "product-knowledge"
subcategory: "navigation"
tags: ["navigation", "UI path", "settings", "where to find", "AI assistant", "chatbox", "translation", "subscription", "data sources", "test AI", "away mode", "discount code"]
applies_when: "CS needs the exact navigation path to guide a merchant to a specific setting"
priority: "high"
```

## Correct Navigation Paths

Never invent UI labels. If unsure, say "Let me check that for you" — do not guess.

- Custom instructions & scenarios: **AI Assistant → Instructions**
- Training data: **AI Assistant → Data Sources**
- Testing AI: **AI Assistant → Test** *(does NOT count against AI quota)*
- Chatbox colors/appearance: **Chatbox → Appearance**
- Hide on pages / device visibility: **Chatbox → Advanced → Display devices and pages**
- Welcome message: **Chatbox → Chat page → Welcome Message**
- Away mode: toggle at the **top of the Chatty app interface** (per-member status, not business hours)
- Language/translation: **Settings → Translation**
- Subscription & plan: **Settings → Subscription**
- Discount code: **Settings → Subscription → Discount Code field**

---

<!-- CHUNK: ref-kb-terminology -->
```yaml
chunk_id: "ref__kb-terminology"
doc_id: "cs-ref-knowledge-base"
title: "Chatty key terminology reference"
category: "product-knowledge"
subcategory: "terminology"
tags: ["terminology", "glossary", "AI conversation", "transfer", "data source", "AI skill", "chatbox", "deep link", "proactive chat", "quick reply", "CSAT"]
applies_when: "CS needs to look up or explain a Chatty-specific term"
priority: "low"
```

## Key Terminology

| Term | Meaning |
|------|---------|
| AI conversation | A customer chat handled by AI assistant |
| Transfer | When AI hands off conversation to a human agent |
| Data source | Information used to train the AI (products, FAQs, custom data) |
| AI skill | Specialized capability for AI (recommendations, size guide, etc.) |
| Chatbox | The chat widget displayed on the storefront |
| Deep link | URL that opens a specific chatbox section directly |
| Proactive chat | Automated messages triggered by visitor behavior |
| Quick reply | Pre-saved response template for faster messaging |
| Contact button | Floating button with multiple contact method options |
| CSAT | Customer Satisfaction survey (Pro+ plans) |
| Smart recommendations | AI-powered product suggestions based on collections |