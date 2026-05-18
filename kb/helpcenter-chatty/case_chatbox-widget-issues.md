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
- If App Embed is enabled but widget still doesn't show → ask for the theme name
- Ask permission: *"To investigate further, our team may need to access your store. Would you allow us to send a collaborator access request?"*
- If yes → ask for their **collaborator code** (found in Shopify Admin → Settings → Users → Security → Collaborator request code) and escalate to TS team with theme name + collaborator code
- If no → create a card for TS with theme name only; TS will advise on next steps without store access

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

If it only happens on first load, it may be a timing issue or a theme-level JS conflict requiring deeper investigation.
- Ask permission: *"To investigate the JavaScript conflict, our team may need access to your store. Would you allow us to send a collaborator access request?"*
- If yes → ask for their **collaborator code** (Shopify Admin → Settings → Users → Security → Collaborator request code) and escalate with store URL, browser details, and collaborator code
- If no → escalate with store URL and browser details only

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

- Ask permission: *"To fix the CSS conflict, our team may need to access your store theme. Would you allow us to send a collaborator access request?"*
- If yes → ask for their **collaborator code** (Shopify Admin → Settings → Users → Security → Collaborator request code) and escalate with screenshot + collaborator code
- If no → escalate with screenshot only; TS will provide a CSS fix the merchant can apply manually

---

## Related
- faq_chatbox-settings (widget appearance and configuration)
- faq_embedded-chatbox (embedding chatbox on external sites)
