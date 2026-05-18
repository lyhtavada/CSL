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

<!-- CHUNK: live-chat-human-handover-email -->
```yaml
chunk_id: "faq__live-chat-human-handover-email"
doc_id: "chatty-live-chat"
title: "Human handover not working — chat not forwarded to agent email"
category: "faq"
subcategory: "live-chat"
tags: ["human handover", "handover email", "chat not forwarded", "agent email", "human transfer", "forwarding not working"]
applies_when: "Merchant says customer chats are not being forwarded to their email or agents are not receiving handover notifications"
priority: "high"
```

## Human Handover Not Working

1. Go to **AI Assistant → Instructions → Assistant Skills → Human Handover**
2. Verify the **handover email** is configured correctly
3. Check if **"Only assign to online members"** is checked — if yes, agents must be online for assignment to occur
   - To always forward regardless of agent status → configure handover to send to support email unconditionally
4. For **email notification** of handover events: go to **Notifications → Email** → enable notifications

> Very common frustration — merchants often expect email forwarding to work by default without configuring the handover email.

---

<!-- CHUNK: live-chat-holiday-message-limitation -->
```yaml
chunk_id: "faq__live-chat-holiday-message-limitation"
doc_id: "chatty-live-chat"
title: "Holiday offline message — cannot set unique message per holiday period"
category: "faq"
subcategory: "live-chat"
tags: ["holiday", "offline message", "holiday message", "custom message", "holiday hours", "limitation"]
applies_when: "Merchant wants to set a specific offline message for each holiday period"
```

## Holiday Offline Message

Go to **Settings → Online Hours → Holidays** → add a holiday date range.

**Limitation:** It is NOT possible to set a unique offline message per holiday period. The general offline message (from Online Hours settings) applies to all holiday periods. There is currently no per-holiday custom message field.

If the merchant needs different messages for different holidays → feature request; log it.

---

<!-- CHUNK: live-chat-ai-not-resume-after-human -->
```yaml
chunk_id: "faq__live-chat-ai-not-resume"
doc_id: "chatty-live-chat"
title: "AI does not resume after a human agent takes over a conversation"
category: "faq"
subcategory: "live-chat"
tags: ["AI resume", "AI pause", "human takeover", "re-enable AI", "AI stopped", "assign to AI"]
applies_when: "After a human agent handles a conversation, the AI no longer responds to that customer on their next visit"
```

## AI Not Resuming After Human Takeover

This is **expected behavior** — once a human takes over a conversation, AI is paused for that specific contact to avoid conflicting responses.

**To re-enable AI for that conversation:**
- Go to the conversation in **Inbox** → click **Assign to AI**

**To configure automatic re-assignment:**
- Check **AI Assistant → Settings** for automatic re-assignment options (if available on the merchant's plan)

> Proactively explain this behavior to merchants who expect AI to auto-resume.

---

<!-- CHUNK: live-chat-customer-reset-conversation -->
```yaml
chunk_id: "faq__live-chat-customer-reset"
doc_id: "chatty-live-chat"
title: "Allow customers to reset or start a new conversation"
category: "faq"
subcategory: "live-chat"
tags: ["reset conversation", "new conversation", "start over", "customer reset", "clear chat"]
applies_when: "Merchant wants to let customers reset their chat history and start fresh"
```

## Customer Conversation Reset

Go to **Chatbox → General → Chatbox Style** → enable **"Allow users to reset conversation"**.

This adds a reset button visible to the customer inside the widget. When clicked, the chat history is cleared and the customer can start a new conversation.
