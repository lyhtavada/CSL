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
