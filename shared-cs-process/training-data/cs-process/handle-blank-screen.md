---
category: CS Process
topic: Handling Blank Screen Issue After App Update
source: cs-process/blank-screen-issue
---

Q: A merchant reports a blank screen when opening the app. What should I do?
Q: How do I handle the blank screen issue after an app update?
A: This is a known issue that occurs after app updates that require new permissions from Shopify. The update message may not display immediately, causing a blank screen.

**Important: Even though the merchant cannot access the app admin, the app's features (widget, points, rewards) continue to work on their storefront.**

**Step 1: Guide the merchant to update permissions**
Use shortcut `!accessibility` or `!update-app` and send this message:

"We recently released new features that require additional permissions to function correctly. Occasionally, due to an issue from Shopify's end, the message to update these permissions does not display immediately, resulting in a blank screen.

To resolve this, please:
1. Clear your browser cache or reload the app page a few times until you see the update message.
2. You might need to open the app from Shopify Admin > Settings > Apps and sales channels.
3. Once the update message appears, approve the permissions and the app should be accessible."

**Step 2: If the above doesn't work, request store access**
Ask the merchant to share their collaborator code so you can send an access request and update the app for them.

- Request **Full permission** to update the app.
- After updating, **remove your access** to ensure the store's security.

**Critical: NEVER ask the merchant to uninstall and reinstall the app. This will cancel their subscription.**

Q: A merchant sees a blank screen but I've already guided them to update. What else can I do?
Q: The merchant can't see the update message even after clearing cache. What should I do?
A: If clearing the browser cache and reloading doesn't work:

1. Ask them to try opening the app directly from Shopify Admin > Settings > Apps and sales channels (not from the sidebar).
2. If the update message still doesn't appear, request store access via collaborator code.
3. Update the app yourself with Full permission, then remove your access afterward.
4. Reassure the merchant that even though they can't access the app admin, the app features continue to work on their store.
