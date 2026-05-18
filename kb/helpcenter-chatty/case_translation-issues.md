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
2. If using Translate & Adapt → guide the merchant to check the meta content of the affected language for overridden Chatty rows and remove them.
3. If the merchant is unsure how to do this or issue persists after they attempt it:
   - Ask permission: *"To investigate the translation conflict directly, our team may need collaborator access to your store. Would you allow us to send a collaborator access request?"*
   - If yes → ask for their **collaborator code** (Shopify Admin → Settings → Users → Security → Collaborator request code). Also collect: which language is affected, name of translation app used, screenshot of the incorrect FAQ display.
   - If no → collect the same info (language affected, translation app, screenshot) and escalate to TS to provide step-by-step fix instructions the merchant can apply themselves.
4. If issue persists after overrides are removed → create a tech support card with: language affected, translation app name, screenshot, and collaborator code if provided.

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
