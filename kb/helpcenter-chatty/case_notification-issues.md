# Notification Issues

<!-- CHUNK: notification-desktop-not-working -->
```yaml
chunk_id: "notification__desktop-not-working"
doc_id: "chatty-notification-issues"
title: "Desktop push notifications not working"
category: "notification-issues"
tags: ["desktop notifications", "push notifications", "not working", "no notifications", "browser notifications"]
applies_when: "Merchant is not receiving desktop push notifications when new messages arrive"
```

## Desktop Push Notifications Not Working

Check in order:

**Step 1: Verify app notification settings**
- Ensure push notification is enabled for new/unread messages in **App Settings**

**Step 2: Verify browser and device settings**
- Browser must have notifications allowed for `app.meetchatty.com`
- System settings must allow notifications (not in Silent/Do Not Disturb mode)
- Device must not be in presentation mode or screen recording mode

**Step 3: If settings are correct but still no notifications**
- Clear browser cache and cookies
- Restart the computer
- Open browser DevTools (F12) → **Application** → **Service Workers** → Update the `firebase-messaging-sw.js` service worker

**Step 4: If still not resolved**
- Escalate to dev team with detailed info

**Meanwhile:** Recommend email notifications or installing the Chatty mobile app as alternatives.

---

<!-- CHUNK: notification-mobile-not-working -->
```yaml
chunk_id: "notification__mobile-not-working"
doc_id: "chatty-notification-issues"
title: "Chatty mobile app push notifications not working"
category: "notification-issues"
tags: ["mobile notifications", "push notifications", "mobile app", "phone notifications", "app notifications"]
applies_when: "Merchant is not receiving push notifications on the Chatty mobile app"
```

## Mobile App Notifications Not Working

1. Verify the mobile app is installed and the merchant is logged in
2. Check device notification settings — Chatty must be **allowed** to send notifications
3. Ensure the phone is not in **Do Not Disturb** mode
4. Try uninstalling and reinstalling the mobile app
5. If issue persists, collect device model, OS version, and app version → escalate to dev team

---

<!-- CHUNK: notification-email-not-working -->
```yaml
chunk_id: "notification__email-not-working"
doc_id: "chatty-notification-issues"
title: "Email notifications for new chat messages not being sent"
category: "notification-issues"
tags: ["email notifications", "email alerts", "not receiving email", "new message alert", "notification email"]
applies_when: "Merchant is not receiving email notifications when new chat messages arrive"
```

## Email Notifications Not Being Sent

1. Verify email notifications are enabled in Chatty's notification settings
2. Check the merchant's email **spam/junk folder**
3. Verify the notification email address is correct
4. If using a corporate email, the organization may be blocking automated emails

---

<!-- CHUNK: notification-not-in-device-settings -->
```yaml
chunk_id: "notification__not-in-device-settings"
doc_id: "chatty-notification-issues"
title: "Chatty not showing in device notification settings"
category: "notification-issues"
tags: ["notification settings", "device settings", "phone settings", "can't find Chatty", "notification permission"]
applies_when: "Merchant can't find Chatty in their device's notification settings to enable it"
```

## Chatty Not in Device Notification Settings

This happens if:
1. The app was never opened after installation (permission was never requested)
2. Notification permission was denied on first prompt and needs to be manually re-enabled

**Solution:** Guide the merchant to manually find and enable Chatty notifications in their device settings, or clear app data and reopen to trigger the permission prompt again.

---

<!-- CHUNK: notification-permission-popup -->
```yaml
chunk_id: "notification__permission-popup"
doc_id: "chatty-notification-issues"
title: "Trigger the notification permission popup again on mobile"
category: "notification-issues"
tags: ["notification popup", "permission prompt", "dismissed popup", "notification permission", "re-enable"]
applies_when: "The notification permission popup was dismissed or denied and merchant wants to enable notifications"
```

## Triggering Notification Permission Popup Again

If the notification permission popup was dismissed or denied:

1. Go to **device Settings** → **Apps** → **Chatty** → **Notifications** → Enable notifications
2. Alternatively, uninstall and reinstall the app to trigger the permission prompt again

---

<!-- CHUNK: notification-app-pixel-disconnected -->
```yaml
chunk_id: "notification__app-pixel-disconnected"
doc_id: "chatty-notification-issues"
title: "Chatty app pixel disconnected in Shopify Customer Events"
category: "notification-issues"
tags: ["app pixel", "Customer Events", "disconnected", "Shopify pixel", "analytics pixel"]
applies_when: "The Chatty app pixel shows as disconnected in Shopify Customer Events"
```

## App Pixel Disconnected in Customer Events

The App Pixel may become disconnected due to theme changes or Shopify updates.

1. Go to **Shopify Admin** → **Settings** → **Customer Events**
2. Find Chatty in the list and **reconnect/re-enable** it
3. Verify the connection is active
4. If the merchant cannot reconnect, collect details and escalate to TS team

---

## Related
- case_email-channel-issues (email notification setup and verification)

---

<!-- CHUNK: notification-mobile-pwa-setup -->
```yaml
chunk_id: "notification__mobile-pwa-setup"
doc_id: "chatty-notification-issues"
title: "How to install the Chatty mobile app and receive notifications"
category: "notification-issues"
tags: ["mobile app", "PWA", "install app", "iOS", "Android", "Safari", "add to home screen", "push notifications mobile"]
applies_when: "Merchant asks how to get Chatty notifications on mobile, or doesn't know how to install the mobile app"
```

## Installing Chatty Mobile App (PWA) for Notifications

Chatty uses a **PWA (Progressive Web App)** — there is no native iOS/Android app in the App Store.

**How to install:**
1. Open **app.chatty.net** in a browser
2. Use **"Add to Home Screen"** (iOS: tap Share → Add to Home Screen; Android: tap browser menu → Install app)
3. Enable notifications in device settings when prompted

> **iOS users must use Safari** — Chrome/Firefox on iOS cannot install PWAs with push notifications.

After installation, ensure notifications are allowed in device settings for the Chatty app.

---

<!-- CHUNK: notification-too-many-duplicates -->
```yaml
chunk_id: "notification__too-many-duplicates"
doc_id: "chatty-notification-issues"
title: "Receiving too many or duplicate notifications per chat"
category: "notification-issues"
tags: ["too many notifications", "duplicate notifications", "notification spam", "multiple alerts", "redundant notifications"]
applies_when: "Merchant is getting multiple notifications for a single chat or too many alerts overall"
```

## Too Many / Duplicate Notifications

1. Go to **Settings → Notifications** → review which notification triggers are enabled
2. **Reduce duplicates:** Configure "notify only when unread" rather than "every message"
3. **Check for multiple channels:** If 4 notifications arrive per chat, multiple notification channels (email + mobile + browser) may all be enabled simultaneously — disable the redundant ones
4. **Test:** Send a test message and count how many notifications arrive, then trace which channels fired

> Most cases of duplicate notifications are caused by having email, desktop push, and mobile push all enabled at once for the same trigger.
