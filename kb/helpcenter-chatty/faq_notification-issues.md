# Notification Issues — FAQ

<!-- CHUNK: notif-desktop-push-not-working -->
```yaml
chunk_id: "faq__notif-desktop-push-not-working"
doc_id: "chatty-notification-issues"
title: "Desktop push notifications not working"
category: "notifications"
tags: ["push notifications", "desktop", "browser notifications", "not receiving", "service worker"]
applies_when: "Merchant is not receiving push notifications on desktop when new messages arrive"
```

## Desktop Push Notifications Not Working

**Step 1: Check app notification settings**
- Ensure push notifications are enabled for new/unread messages in App Settings

**Step 2: Check browser and device settings**
- Browser must have notifications allowed for Chatty / app.meetchatty.com
- PC/laptop system settings must allow notifications (not in Silent/Do Not Disturb mode)
- Device must not be in presentation mode or screen recording mode

**Step 3: If settings correct but still not working**
- Clear browser cache and cookies
- Restart the computer
- Open browser DevTools (F12) → **Application** → **Service Workers** → Update `firebase-messaging-sw.js`

**Step 4: If still not resolved**
- Offer to use TeamViewer/AnyDesk to check settings directly
- If persists → escalate to dev team with detailed info

Alternative: recommend email notifications or Chatty mobile app.

---

<!-- CHUNK: notif-mobile-app-not-working -->
```yaml
chunk_id: "faq__notif-mobile-app-not-working"
doc_id: "chatty-notification-issues"
title: "Chatty mobile app push notifications not working"
category: "notifications"
tags: ["mobile app", "push notifications", "mobile notifications", "Do Not Disturb", "reinstall"]
applies_when: "Merchant is not receiving push notifications on the Chatty mobile app"
```

## Mobile App Notifications Not Working

1. Verify mobile app is installed and merchant is logged in
2. Check device notification settings — Chatty must be allowed to send notifications
3. Ensure phone is not in Do Not Disturb mode
4. Try uninstalling and reinstalling the mobile app
5. If persists → collect device model, OS version, app version, escalate to dev team

---

<!-- CHUNK: notif-email-notifications-not-working -->
```yaml
chunk_id: "faq__notif-email-notifications-not-working"
doc_id: "chatty-notification-issues"
title: "Email notifications for new chat messages not being sent"
category: "notifications"
tags: ["email notifications", "email alerts", "not receiving emails", "spam folder", "notification email"]
applies_when: "Merchant is not receiving email alerts when new messages arrive"
```

## Email Notifications Not Working

1. Verify email notifications are enabled in Chatty's notification settings
2. Check spam/junk folder
3. Verify the notification email address is correct
4. If using corporate email → organization may be blocking automated emails

---

<!-- CHUNK: notif-not-in-device-settings -->
```yaml
chunk_id: "faq__notif-not-in-device-settings"
doc_id: "chatty-notification-issues"
title: "Chatty not showing in device notification settings"
category: "notifications"
tags: ["device settings", "notification settings", "permission denied", "not showing in settings"]
applies_when: "Merchant can't find Chatty in their device notification settings to enable it"
```

## Chatty Not in Device Notification Settings

Causes:
- App was never opened after install (notification permission was never requested)
- Permission was denied on first prompt and must be manually re-enabled

Guide merchant to: **Device Settings** → **Apps** → **Chatty** → **Notifications** → Enable

Or: clear app data and reopen to trigger the permission prompt again.

---

<!-- CHUNK: notif-permission-popup-not-appearing -->
```yaml
chunk_id: "faq__notif-permission-popup-not-appearing"
doc_id: "chatty-notification-issues"
title: "Notification permission popup never appeared or was dismissed"
category: "notifications"
tags: ["permission popup", "notification popup", "dismissed", "re-enable notifications"]
applies_when: "The notification permission popup was never shown or was dismissed by the merchant"
```

## Re-triggering Notification Permission Popup

1. Go to **Device Settings** → **Apps** → **Chatty** → **Notifications** → Enable notifications
2. Or: uninstall and reinstall the app to trigger the permission prompt again

---

<!-- CHUNK: notif-app-pixel-disconnected -->
```yaml
chunk_id: "faq__notif-app-pixel-disconnected"
doc_id: "chatty-notification-issues"
title: "Chatty disconnected in Customer Events (App Pixel)"
category: "notifications"
tags: ["App Pixel", "Customer Events", "disconnected", "Shopify pixel", "reconnect"]
applies_when: "The Chatty app pixel shows as disconnected in Shopify Customer Events"
```

## App Pixel Disconnected

May disconnect due to theme changes or Shopify updates.

1. Go to **Shopify Admin** → **Settings** → **Customer Events**
2. Find Chatty → reconnect/re-enable
3. Verify the connection is active
4. If merchant cannot reconnect → collect details and escalate to TS team
