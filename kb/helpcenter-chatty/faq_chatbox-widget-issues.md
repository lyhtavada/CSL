# Chatbox & Widget Issues — FAQ

<!-- CHUNK: chatbox-widget-not-showing -->
```yaml
chunk_id: "faq__chatbox-widget-not-showing"
doc_id: "chatty-chatbox-widget-issues"
title: "Live chat button not showing on the store"
category: "chatbox-widget"
tags: ["not showing", "widget missing", "live chat button", "app embed", "theme conflict", "chatbox not visible"]
applies_when: "Live chat button or chatbox widget is not appearing on the merchant's store"
```

## Live Chat Widget Not Showing

**Cause 1: App Embed not enabled**
- Go to **Shopify Admin** → **Online Store** → **Themes** → **Customize** → **App Embeds**
- Ensure Chatty is toggled **ON** — ask merchant for a screenshot to verify

**Cause 2: Live chat not enabled in app**
- Go to **Chatbox** → **General** → **Blocks** → ensure **Live chat** is enabled

**Cause 3: Theme conflict**
- If App Embed is enabled but button still doesn't show → ask for theme name, create a TS card to investigate

---

<!-- CHUNK: chatbox-faq-page-not-showing -->
```yaml
chunk_id: "faq__chatbox-faq-page-not-showing"
doc_id: "chatty-chatbox-widget-issues"
title: "FAQ page not showing on the store"
category: "chatbox-widget"
tags: ["FAQ page", "not showing", "navigation menu", "pages", "FAQ not visible"]
applies_when: "The Chatty FAQ page is not visible on the merchant's store"
```

## FAQ Page Not Showing

1. **FAQ page not enabled** → **Settings** → **Pages** → Enable FAQ page
2. **URL not added to menu** → Get FAQ page URL from app → add to store navigation menu

Reference: https://help.chatty.net/build-faqs/faqs-page

Tip: Suggest adding the FAQ URL to the main navigation menu.

---

<!-- CHUNK: chatbox-faq-overwriting-templates -->
```yaml
chunk_id: "faq__chatbox-faq-overwriting-templates"
doc_id: "chatty-chatbox-widget-issues"
title: "Chatty FAQ page overwriting other page templates"
category: "chatbox-widget"
tags: ["FAQ template", "page template", "overwriting", "About Us", "Contact page", "template conflict"]
applies_when: "Other pages (About Us, Contact) look wrong or broken after installing Chatty FAQ page"
```

## FAQ Page Overwriting Other Page Templates

Chatty assigns FAQ content to the default page template, which can affect other pages.

1. In Shopify theme editor → **Theme Templates** → create new template (e.g., `chatty-faq`)
2. Go to **Shopify Admin** → **Online Store** → **Pages**
3. Select the FAQ page created by Chatty → assign the new template
4. In Chatty app, set the correct FAQ page URL
5. Verify other pages are no longer affected

---

<!-- CHUNK: chatbox-widget-position -->
```yaml
chunk_id: "faq__chatbox-widget-position"
doc_id: "chatty-chatbox-widget-issues"
title: "Change the position of the chat widget button"
category: "chatbox-widget"
tags: ["widget position", "button position", "move chatbox", "alignment", "custom position", "overlapping", "ATC", "add to cart"]
applies_when: "Merchant wants to move the chat button, or the widget is overlapping other page elements"
priority: "very-high"
```

## Changing Widget Button Position / Fixing Overlaps

**Quick fix:** Go to **Chatbox → Appearance → Set chatbox button → Select button alignment** to reposition using built-in options.

**For precise CSS positioning** (e.g., widget overlapping sticky Add-to-Cart bar, BOGOS gift icon, scroll-to-top button):
1. Go to **Chatbox → Advanced → Custom CSS**
2. Adjust `bottom` and `right` values to move the widget away from other elements
3. Common pattern: `#chatty-widget { bottom: 80px !important; right: 20px !important; }`

**If merchant can't apply CSS themselves:**
- Request collaborator access → TS team creates the CSS fix directly

> Extremely common on mobile with sticky ATC bars. Always ask which element is conflicting and on which device.

---

<!-- CHUNK: chatbox-remove-branding -->
```yaml
chunk_id: "faq__chatbox-remove-branding"
doc_id: "chatty-chatbox-widget-issues"
title: "Remove Chatty branding / Powered by Chatty watermark"
category: "chatbox-widget"
tags: ["branding", "remove branding", "powered by Chatty", "watermark", "DevZone"]
applies_when: "Merchant wants to remove the Chatty branding from the widget"
```

## Removing Chatty Branding

1. Go to **DevZone** → **General** → Enable **Remove branding**
2. Notify the merchant to check
3. Communicate: *"Normally available on paid plans only — we've helped remove it for you as a special support."*

**Important:** Do NOT ask for a review immediately after branding removal — Shopify considers this "exchange for review." Help with another task first, then ask based on the support experience.

---

<!-- CHUNK: chatbox-javascript-control -->
```yaml
chunk_id: "faq__chatbox-javascript-control"
doc_id: "chatty-chatbox-widget-issues"
title: "Open or close the Chatty widget using JavaScript"
category: "chatbox-widget"
tags: ["JavaScript", "open widget", "close widget", "programmatic", "trigger chatbox", "deep link"]
applies_when: "Merchant wants to trigger the chatbox open/close via code or JavaScript"
```

## JavaScript Widget Control

- **Toggle open/close:** `avadaFaqTrigger()`
- **Close widget:** `ChattyJS.closeWidget()`
- **Open widget:** `ChattyJS.openWidget()`
- **Open to specific page:**
  - `ChattyJS.openWidget('#chatty-home')` — Home
  - `ChattyJS.openWidget('#chatty-chat')` — Live Chat
  - `ChattyJS.openWidget('#chatty-tracking')` — Order Tracking
  - `ChattyJS.openWidget('#chatty-help')` — Help/FAQ

Use these when deep links cannot be used or the trigger element is not a standard link.

---

<!-- CHUNK: chatbox-faq-category-icons -->
```yaml
chunk_id: "faq__chatbox-faq-category-icons"
doc_id: "chatty-chatbox-widget-issues"
title: "Enable FAQ category icons"
category: "chatbox-widget"
tags: ["FAQ category icons", "locked", "DevZone", "category icons", "view more icons"]
applies_when: "The FAQ category icons option is locked or not available for the merchant"
```

## Enabling FAQ Category Icons

Category icons are locked by default for newly installed apps.

1. Get the merchant's Store URL
2. Go to **DevZone** → enable the category icons feature
3. Notify the merchant to check

---

<!-- CHUNK: chatbox-widget-not-clickable -->
```yaml
chunk_id: "faq__chatbox-widget-not-clickable"
doc_id: "chatty-chatbox-widget-issues"
title: "Chat widget button not clickable or unresponsive on first page load"
category: "chatbox-widget"
tags: ["not clickable", "unresponsive", "JavaScript conflict", "first load", "button not working"]
applies_when: "The chat button is visible but unresponsive or not clickable"
```

## Widget Button Not Clickable

Usually a JavaScript conflict with another app or theme.

1. Disable other chat or popup apps temporarily to test
2. Check browser console for JS errors
3. Clear browser cache

If only happens on first load → collect store URL and browser details, escalate to TS.

---

<!-- CHUNK: chatbox-slow-mobile -->
```yaml
chunk_id: "faq__chatbox-slow-mobile"
doc_id: "chatty-chatbox-widget-issues"
title: "Chat slow to load on mobile or iPad"
category: "chatbox-widget"
tags: ["slow", "mobile", "iPad", "loading", "performance", "chat lag"]
applies_when: "Chat takes too long to load on mobile devices or iPad"
```

## Chat Slow on Mobile

Common causes: theme performance issues, app conflicts, slow internet, widget loading conflicts.

Quick test: clear browser/app cache, check on different network. If persists → collect store URL and device/browser details for TS.

---

<!-- CHUNK: chatbox-avatar-upload-not-working -->
```yaml
chunk_id: "faq__chatbox-avatar-upload-not-working"
doc_id: "chatty-chatbox-widget-issues"
title: "AI logo or avatar upload not working"
category: "chatbox-widget"
tags: ["avatar upload", "logo upload", "AI avatar", "upload not working", "image upload"]
applies_when: "Merchant can't upload an AI logo or avatar"
```

## Avatar Upload Not Working

1. Use Chrome (recommended)
2. Clear browser cache and reload
3. Image must be JPG or PNG, under 2MB
4. Try in Incognito/Private window

If still failing → collect screenshot and image file, escalate to TS.

---

<!-- CHUNK: chatbox-wrong-shape-mobile -->
```yaml
chunk_id: "faq__chatbox-wrong-shape-mobile"
doc_id: "chatty-chatbox-widget-issues"
title: "Chat widget button shows wrong shape or icon on mobile"
category: "chatbox-widget"
tags: ["wrong shape", "wrong icon", "mobile", "CSS conflict", "button appearance"]
applies_when: "The chat button displays incorrectly on mobile devices"
```

## Wrong Widget Shape on Mobile

Usually caused by custom CSS conflicting on mobile. Collect a screenshot → escalate to TS for CSS fix.

---

<!-- CHUNK: chatbox-widget-blocking-other-apps -->
```yaml
chunk_id: "faq__chatbox-widget-blocking-other-apps"
doc_id: "chatty-chatbox-widget-issues"
title: "Chat widget blocking another app's button or element"
category: "chatbox-widget"
tags: ["blocking", "other app", "BOGOS", "gift icon", "scroll to top", "conflict", "overlap", "collaborator access"]
applies_when: "The Chatty widget is overlapping or blocking a button from another app"
priority: "high"
```

## Widget Blocking Another App's Button

Common conflicting elements: BOGOS gift icon, sticky add-to-cart bars, scroll-to-top buttons, loyalty widgets.

**Resolution:**
1. Identify the conflicting app and element (ask merchant to share a screenshot)
2. Apply Custom CSS in **Chatbox → Advanced → Custom CSS** to offset Chatty's position:
   - Adjust `bottom` and `right` values to move Chatty away from the conflicting element
3. If merchant cannot apply CSS themselves → request **collaborator access** so the TS team can create the fix

> Coordinate with the merchant to identify which app's element is conflicting before writing the CSS fix.

---

<!-- CHUNK: chatbox-hide-specific-pages -->
```yaml
chunk_id: "faq__chatbox-hide-specific-pages"
doc_id: "chatty-chatbox-widget-issues"
title: "Hide the chat widget on specific pages"
category: "chatbox-widget"
tags: ["hide widget", "specific pages", "display rules", "page rules", "exclude pages", "URL rules"]
applies_when: "Merchant wants to hide the chat widget on certain pages of their store"
```

## Hiding Widget on Specific Pages

Go to **Chatbox → Advanced → Display Rules → Page Rules** → add page URLs to exclude.

**Options:**
- Exact URL → hide on one specific page
- URL pattern → e.g., hide on all pages starting with `/a/ush_bundles/` (use a wildcard pattern)
- Page type → hide on all collection pages, product pages, etc. (if supported)

Add each exclusion URL and save.

---

<!-- CHUNK: chatbox-faq-formatting-bullets -->
```yaml
chunk_id: "faq__chatbox-faq-formatting-bullets"
doc_id: "chatty-chatbox-widget-issues"
title: "FAQ page bullet points or formatting not rendering correctly"
category: "chatbox-widget"
tags: ["FAQ formatting", "bullet points", "rich text", "rendering", "HTML", "formatting bug"]
applies_when: "FAQ answers are showing broken formatting, missing bullet points, or incorrect rendering on the FAQ page"
```

## FAQ Page Formatting Issues

This is a **known issue** with rich text rendering on the FAQ page.

**Immediate fix:** The CS team can apply a CSS fix — create a TS ticket with a screenshot showing the broken formatting.

**Prevention:** Avoid using HTML in FAQ answers. Use plain text only — the FAQ editor's native formatting is safer than pasting HTML.

If the issue persists after CSS fix → escalate to TS with screenshot.
