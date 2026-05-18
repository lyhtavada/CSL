# Translation Issues — FAQ

<!-- CHUNK: translation-faq-not-switching -->
```yaml
chunk_id: "faq__translation-faq-not-switching"
doc_id: "chatty-translation-issues"
title: "FAQ page translation not working when switching languages"
category: "translation"
tags: ["translation", "FAQ translation", "language switch", "third-party translation app", "Translate & Adapt", "T Lab", "meta content overwrite"]
applies_when: "FAQ content doesn't change when customer switches language on the store"
```

## FAQ Translation Not Working When Switching Language

Commonly caused by a third-party translation app (e.g., Translate & Adapt, T Lab) overwriting Chatty's FAQ meta content.

1. Ask merchant if they use a third-party translation app
2. If using Translate & Adapt → check meta content of affected language for overwritten Chatty rows
3. Remove the overriding content from the third-party app
4. If persists after removing overrides → create a TS card for deeper investigation
5. If unclear → request app permissions to investigate or escalate to TS

---

<!-- CHUNK: translation-status-outdated -->
```yaml
chunk_id: "faq__translation-status-outdated"
doc_id: "chatty-translation-issues"
title: "Translation status shows Outdated for a language"
category: "translation"
tags: ["translation outdated", "outdated status", "auto-translate", "manual translate", "FAQ translation status"]
applies_when: "A language shows as Outdated in the Chatty Translations section"
```

## Translation Status Shows "Outdated"

The FAQ content hasn't been translated after the app updated its content, or was never translated for that language.

1. Go to **FAQ section** in **Translations**
2. **Paid plan merchants** → use **Auto-translate** to automatically translate
3. **Free plan merchants** → must manually translate the FAQ content
4. After translating → save and verify status changes from "Outdated" to "Updated"

---

<!-- CHUNK: translation-save-and-publish -->
```yaml
chunk_id: "faq__translation-save-and-publish"
doc_id: "chatty-translation-issues"
title: "Translation not showing or reverting — must click Save then Publish"
category: "translation"
tags: ["translation not showing", "translation reverting", "save and publish", "publish translation", "2-step", "translation not live"]
applies_when: "Merchant saved a translation but it's not showing on the storefront or reverted to default"
priority: "medium"
```

## Translation Not Showing / Reverting to Default

The translation process requires **two steps** — just clicking Save is not enough:

1. After editing translation → click **Save**
2. Then click the **settings icon** → **Publish** → Confirm

> This is very common — merchants save changes but forget to click Publish. The storefront still shows the old/default version until published.

**Additional checks if still not showing after publishing:**
- Ensure the language is also added in **Shopify Admin → Settings → Languages** and is active
- Clear browser cache or test in an incognito window (cached version may show old translation)

---

<!-- CHUNK: translation-faq-not-auto-updating -->
```yaml
chunk_id: "faq__translation-faq-not-auto-updating"
doc_id: "chatty-translation-issues"
title: "FAQ translations not updating when new questions are added"
category: "translation"
tags: ["translation not updating", "new FAQ", "outdated translation", "FAQ translation", "auto-update"]
applies_when: "Merchant added new FAQ questions but existing language translations didn't update automatically"
```

## FAQ Translations Not Auto-Updating

Translations are **NOT automatically updated** when new FAQ content is added.

Chatty shows a banner when translations are outdated. To update:

1. Go to **Settings → Translation → Edit** for the affected language
2. Re-translate the new content (use Auto-translate or translate manually)
3. Click **Save** → then **settings icon → Publish**

> Merchants need to manually re-translate whenever FAQ content changes. Encourage them to check the Translation section after adding new FAQs.
