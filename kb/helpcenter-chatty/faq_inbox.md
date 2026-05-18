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

<!-- CHUNK: inbox-cannot-find-messages -->
```yaml
chunk_id: "inbox__cannot-find-messages"
doc_id: "chatty-inbox"
title: "Cannot find or see messages in the Chatty inbox"
category: "inbox"
tags: ["missing messages", "can't find", "inbox empty", "messages not showing", "error code", "failed pre-conditioning"]
applies_when: "Merchant says they cannot find or see messages in their inbox"
```

## Cannot Find Messages in Inbox

1. **Check all tabs** — inbox has: All / Unread / Resolved / Mine — conversations may be in the **Resolved** tab
2. **Check channel filter** — message may be from a different channel (email vs. web chat); use the channel filter to switch views
3. **If inbox shows error code** (e.g., "9 Failed Pre-conditioning") → clear browser cache, refresh the page; if error persists → escalate to TS with the error code
4. **If using search** → try browsing manually instead; search may miss recently received messages

---

<!-- CHUNK: inbox-mark-all-resolved -->
```yaml
chunk_id: "inbox__mark-all-resolved"
doc_id: "chatty-inbox"
title: "Mark all conversations as resolved at once"
category: "inbox"
tags: ["mark all resolved", "bulk resolve", "resolve all", "mass resolve", "bulk action"]
applies_when: "Merchant wants to bulk-resolve all open conversations at once"
```

## Mark All Conversations as Resolved

There is currently **no bulk "resolve all" button** in the inbox. Conversations must be resolved individually.

**Feature request:** This has been logged with the product team.

**For large volumes:** Contact support — the team may be able to help with a backend bulk resolve for your account.

---

<!-- CHUNK: inbox-replies-back-to-chatty -->
```yaml
chunk_id: "inbox__replies-back-to-chatty"
doc_id: "chatty-inbox"
title: "Customer replies go back to Chatty inbox, not to support email directly"
category: "inbox"
tags: ["replies to inbox", "email reply", "reply routing", "chatty inbox", "threaded", "reply-to"]
applies_when: "Merchant expected customer email replies to go directly to their email client but they appear in Chatty inbox instead"
```

## Customer Replies Go to Chatty Inbox

This is **expected behavior** for the email channel — all replies are threaded in Chatty's inbox for unified management.

**If the merchant wants replies to go directly to their email client:**
1. Go to **Channels → Email → Email sender** settings → check the **Reply-To** field
2. Set the Reply-To address to the merchant's actual support email
3. Customers' replies will then arrive at both Chatty and the configured email client

> Explain to merchants that the Chatty inbox is the intended management hub. The Reply-To field workaround is for merchants who prefer their traditional email workflow.
