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
