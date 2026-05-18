# WhatsApp & Messenger Issues — FAQ

<!-- CHUNK: whatsapp-connection-requirements -->
```yaml
chunk_id: "faq__whatsapp-requirements"
doc_id: "chatty-whatsapp-messenger-issues"
title: "WhatsApp connection requirements checklist"
category: "whatsapp-messenger"
tags: ["WhatsApp", "connect WhatsApp", "requirements", "Meta Business Manager", "phone number", "OTP", "Business Admin"]
applies_when: "Merchant wants to connect WhatsApp to Chatty or is having connection issues"
```

## WhatsApp Connection Requirements

**1. Meta Business Manager**
- Must have valid Business Manager with **Business Admin** role
- Employee role is NOT sufficient
- Check at: business.facebook.com/settings/people

**2. Valid phone number**
- NOT currently registered on WhatsApp personal app
- Or an existing WhatsApp Business number migrated to Cloud API
- OTP verification must be via SMS or phone call (not WhatsApp app)

**3. Business information**
- Business name, type, legal address, website domain
- Meta may require Business Verification for full features

**4. OAuth permissions**
- Must select their Business Manager, WhatsApp Business Account, and phone number
- Must grant "AVADA group company limited" permission to manage the number

**5. Facebook login**
- Facebook account must be added to Business Manager with proper permissions
- Browser must not block popups or third-party cookies

**6. No other API provider**
- If number is with another provider (Twilio, 360dialog, etc.) → must be released/migrated first

---

<!-- CHUNK: whatsapp-connected-not-working -->
```yaml
chunk_id: "faq__whatsapp-connected-not-working"
doc_id: "chatty-whatsapp-messenger-issues"
title: "WhatsApp connected but not working"
category: "whatsapp-messenger"
tags: ["WhatsApp", "not working", "connection issues", "Business Admin", "business verification", "popup blocked"]
applies_when: "Merchant connected WhatsApp but messages are not coming through or features aren't working"
```

## WhatsApp Connected But Not Working

Common causes:
1. **Insufficient permissions** — connecting user must be Business Admin, not Employee
2. **Phone number in use** — already on WhatsApp personal app or another API provider
3. **Business verification pending** — Meta requires verification for full features
4. **Browser blocking popups** — OAuth popup blocked, try different browser or disable popup blocker

Verify each requirement in the checklist above before escalating.

---

<!-- CHUNK: whatsapp-pending-status -->
```yaml
chunk_id: "faq__whatsapp-pending-status"
doc_id: "chatty-whatsapp-messenger-issues"
title: "WhatsApp number showing as Pending after connecting"
category: "whatsapp-messenger"
tags: ["WhatsApp", "pending", "verification pending", "2FA", "Meta verification"]
applies_when: "WhatsApp number shows Pending status after connection"
```

## WhatsApp Number Showing as Pending

Pending = Meta verification still in progress (typically 24–48 hours).

Verify:
1. WhatsApp Business account is fully verified
2. Phone number is not registered with another WhatsApp Business API provider
3. Two-factor authentication (2FA) for the phone number is enabled

If pending beyond 48 hours → contact support for further help.

---

<!-- CHUNK: whatsapp-switch-from-another-provider -->
```yaml
chunk_id: "faq__whatsapp-switch-provider"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Switching WhatsApp number from another provider to Chatty"
category: "whatsapp-messenger"
tags: ["WhatsApp", "switch provider", "migrate", "Twilio", "360dialog", "BSP migration"]
applies_when: "Merchant's WhatsApp number is currently connected to another provider and they want to switch to Chatty"
```

## Switching From Another WhatsApp Provider

Meta policy: a WhatsApp Business API number can only be managed by one BSP at a time. To switch to Chatty:
1. Migrate the number: disconnect from current BSP via Meta Business Manager, reconnect to Chatty
2. Or create a new WhatsApp Business Account with the same phone number

Contact support for guidance on the migration process.

---

<!-- CHUNK: whatsapp-ai-without-widget -->
```yaml
chunk_id: "faq__whatsapp-ai-no-widget"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Use Chatty AI for WhatsApp without showing widget on website"
category: "whatsapp-messenger"
tags: ["WhatsApp AI", "AI WhatsApp", "no widget", "AI channel", "WhatsApp only"]
applies_when: "Merchant wants AI to answer WhatsApp messages but not show the chatbox on their website"
```

## AI for WhatsApp Without Website Widget

Yes — once WhatsApp is connected, go to **AI Assistant** → **Settings** → enable AI for the WhatsApp channel. Access WhatsApp conversations via **Inbox** → **WhatsApp** tab.

---

<!-- CHUNK: whatsapp-outbound-not-supported -->
```yaml
chunk_id: "faq__whatsapp-outbound"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Initiating outbound WhatsApp messages from Chatty"
category: "whatsapp-messenger"
tags: ["WhatsApp", "outbound", "send first", "initiate message", "proactive WhatsApp"]
applies_when: "Merchant wants to initiate (send first) WhatsApp messages to customers from Chatty"
```

## Initiating Outbound WhatsApp Messages

Not supported — Chatty currently only supports responding within existing WhatsApp conversations. You cannot initiate new outbound messages to contacts who haven't messaged first.

---

<!-- CHUNK: messenger-messages-not-showing -->
```yaml
chunk_id: "faq__messenger-not-showing"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Facebook Messenger messages not showing in Chatty inbox"
category: "whatsapp-messenger"
tags: ["Facebook Messenger", "messages not showing", "Messenger integration", "page permissions", "OAuth"]
applies_when: "Facebook Messenger is connected but messages don't appear in Chatty"
```

## Messenger Messages Not Showing in Chatty

1. **Integration incomplete** — verify all steps were completed in the Channels section
2. **Insufficient page permissions** — connecting user must have "Manage and access Page messages" permission (check Page Settings → Page Roles & Permissions)
3. **Deselected permissions during setup** — permissions may be incomplete
4. **Old messages** — only messages sent AFTER Chatty is connected will sync

---

<!-- CHUNK: instagram-messages-not-showing -->
```yaml
chunk_id: "faq__instagram-not-showing"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Instagram messages not showing in Chatty inbox"
category: "whatsapp-messenger"
tags: ["Instagram", "messages not showing", "Instagram integration", "admin access", "Meta OAuth"]
applies_when: "Instagram is connected but messages don't appear in Chatty"
```

## Instagram Messages Not Showing

1. Channel properly connected in Chatty → **Channels** settings
2. Connecting user must have admin access to the Facebook page
3. All permissions granted during OAuth
4. Only new messages (sent after connection) will appear

If all correct but messages don't sync → collect details, escalate to TS.

---

<!-- CHUNK: instagram-story-replies-error -->
```yaml
chunk_id: "faq__instagram-story-replies"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Instagram story replies showing error in Chatty inbox"
category: "whatsapp-messenger"
tags: ["Instagram", "story replies", "reel shares", "voice messages", "unsupported", "error"]
applies_when: "Instagram story replies or other message types show errors in Chatty"
```

## Instagram Story Replies Showing Error

Chatty currently supports Instagram text and image messages only. **Unsupported:** story replies, reel shares, voice messages, stickers, post shares, vanish mode messages.

The team is working on expanding support for these formats.

---

<!-- CHUNK: instagram-direct-replies-not-syncing -->
```yaml
chunk_id: "faq__instagram-direct-replies-sync"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Replies made directly in Instagram/Facebook not syncing to Chatty"
category: "whatsapp-messenger"
tags: ["Instagram", "Facebook", "replies not syncing", "direct reply", "outside Chatty", "sync"]
applies_when: "Replies sent directly in the Meta platform (not via Chatty) are not showing in Chatty inbox"
```

## Direct Replies in Meta Not Syncing to Chatty

Known limitation — replies made directly in the Meta platform (not via Chatty) may not sync back. A feature request has been filed to improve sync coverage for replies made outside of Chatty.

---

<!-- CHUNK: instagram-ai-not-responding -->
```yaml
chunk_id: "faq__instagram-ai-not-responding"
doc_id: "chatty-whatsapp-messenger-issues"
title: "AI not responding to Instagram messages"
category: "whatsapp-messenger"
tags: ["Instagram", "AI not responding", "AI channel toggle", "AI Instagram", "enable AI"]
applies_when: "AI is not responding to Instagram messages"
```

## AI Not Responding to Instagram Messages

Go to **AI Assistant** → **Settings** → check if AI is enabled for the Instagram channel — there is a per-channel toggle. Enable it and AI will start responding automatically.

---

<!-- CHUNK: instagram-24hr-reply-window -->
```yaml
chunk_id: "faq__instagram-24hr-window"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Cannot reply to Instagram message — Send button greyed out"
category: "whatsapp-messenger"
tags: ["Instagram", "can't reply", "greyed out", "send button", "24 hours", "messaging window", "expired"]
applies_when: "The Send button is greyed out in Chatty when trying to reply to an Instagram message"
```

## Instagram Reply Button Greyed Out

This is caused by **Instagram's 24-hour messaging window policy** — once 24 hours have passed since the customer's last message, you cannot reply via DM.

This is a **Meta platform restriction**, not a Chatty bug.

**Options after the window expires:**
- Use **Instagram message templates** if available for your account (requires Meta Business approval)
- Reply directly in the Instagram app/inbox outside of Chatty
- Encourage customers to send a follow-up message to reopen the window

---

<!-- CHUNK: whatsapp-contact-button -->
```yaml
chunk_id: "faq__whatsapp-contact-button"
doc_id: "chatty-whatsapp-messenger-issues"
title: "Add WhatsApp as a contact option button in the chatbox"
category: "whatsapp-messenger"
tags: ["WhatsApp button", "contact button", "WhatsApp shortcut", "chatbox button", "contact option"]
applies_when: "Merchant wants to add a WhatsApp button or link in the chatbox widget without fully connecting WhatsApp as a channel"
```

## Adding WhatsApp as a Contact Button

Go to **Chatbox → General → Contact Button** → enable **WhatsApp** → enter the WhatsApp Business number.

This adds a **WhatsApp shortcut button** in the widget — tapping it opens a WhatsApp chat with the merchant's number.

> **This is different from connecting WhatsApp as a full channel.** The contact button simply redirects customers to WhatsApp — it does NOT route messages into the Chatty inbox. For full WhatsApp message management, connect WhatsApp under **Settings → Channels**.
