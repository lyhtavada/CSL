---
category: Translations
problem: Loyalty blocks not translated on live store despite adding multiple languages in Translation settings
source: notion
---

Q: I added multiple languages in the Translation settings, but when I switch languages on my live store, some loyalty block content is not translated. What's going on?
Q: My loyalty program blocks are showing in the wrong language even though I set up translations. How do I fix this?
Q: The content on my loyalty page doesn't change when customers switch to a different language. I've already configured translations in Joy. Why isn't it working?
Q: Some of my loyalty blocks are not being translated on the storefront. I use Translate & Adapt alongside Joy. Could that be causing the issue?
Q: Translations work for most of my store, but the loyalty widget and blocks still show in the default language. What should I check?

A: This issue usually happens when an external translation app (such as Shopify's "Translate & Adapt" or similar apps) is being used alongside Joy's built-in translation feature. These external apps can overwrite the meta content of your pages, which prevents Joy's translations from displaying correctly.

Here's how to fix it:

1. **Check for external translation apps** -- Go to your Shopify admin and see if you have any third-party translation apps installed (e.g., Translate & Adapt, Langify, Weglot, etc.).
2. **Review overwritten meta content** -- If an external app is installed, it may have overwritten the meta content for the pages where your loyalty blocks appear. Open the external translation app and look for any entries related to your loyalty page content.
3. **Remove the overwritten content** -- Delete or clear the overwritten translation entries in the external app so that Joy's translations can take effect again.
4. **Test on your live store** -- After removing the overwritten content, switch between languages on your storefront to confirm that the loyalty blocks now display correctly in each language.
5. **Still not working?** -- If the translations are still not showing after clearing the external app data, please reach out to our support team so we can investigate further.

Escalate khi: Translations still do not display correctly after removing overwritten content from external translation apps.
