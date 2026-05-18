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

**Before troubleshooting, collect:**
- What role the connecting Facebook user has in Meta Business Manager (Admin or Employee?)
- Whether the phone number was previously connected to another WhatsApp API provider
- Whether Meta Business verification is complete or still pending
- What browser was used during OAuth setup

**Then check in order:**
1. **Insufficient permissions** — connecting user must be a Business Admin (not Employee) in Meta Business Manager. Ask merchant to verify at business.facebook.com/settings/people
2. **Phone number already in use** — ask merchant to confirm the number is not active on WhatsApp personal app and not connected to another API provider (Twilio, 360dialog, etc.)
3. **Business verification pending** — Meta requires verification for full features; ask merchant to check Meta Business Manager for any pending verification prompts
4. **Browser blocking popups** — if OAuth popup was blocked, ask merchant to try reconnecting in a different browser with popup blockers disabled

If all items check out but still not working → escalate with: store URL, phone number last 4 digits, Meta Business Manager ID, which items from the checklist were confirmed.

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

If all settings are correct but messages still don't sync → escalate with: store URL, Facebook page name/ID, when connection was made, screenshot of Channels settings showing Instagram is connected.

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

**Collect before advising:**
- When did the merchant connect WhatsApp? (if < 48 hours ago → just wait)
- Is the phone number registered with another WhatsApp Business API provider?
- Has the merchant completed Meta Business Verification?

**Guide the merchant to verify:**
1. Check that **WhatsApp Business account** is fully verified in Meta Business Manager
2. Confirm the phone number is **not** already registered with another API provider
3. Ensure **Two-factor authentication (2FA)** is enabled for the phone number in WhatsApp Business settings

If still Pending beyond 48 hours after all above are confirmed → escalate with: phone number last 4 digits, Meta Business Manager ID, when connection was made, screenshot of pending status.

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

## Related
- case_email-channel-issues (email channel setup and verification)
- faq_channels (channel overview and setup)
