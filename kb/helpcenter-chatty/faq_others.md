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
clarify_first: true
```

## App Not Loading / 404 Error

**Important**: "404 page" is ambiguous — always clarify before troubleshooting.

Ask first: "Could you tell me a bit more — is this 404 error appearing inside the Chatty app dashboard, or on your Shopify store pages?"

- If the 404 is **inside the Chatty app / dashboard** → apply the steps below
- If the 404 is on their **Shopify store** (product pages, collections, etc.) → this is outside Chatty's scope, direct merchant to Shopify support or their theme developer
- If the 404 is from **AI sending broken product links** → refer to the AI wrong responses case

**Steps (Chatty app 404 only):**

1. Hard reload the page (`Ctrl+Shift+R` / `Cmd+Shift+R`)
2. Clear browser cache and cookies
3. Try a different browser
4. Try incognito mode

If the issue persists across browsers, escalate to technical team — it may be a backend issue.
