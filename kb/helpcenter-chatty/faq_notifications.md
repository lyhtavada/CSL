# Notifications

<!-- CHUNK: notifications-web-push -->
```yaml
chunk_id: "faq__notifications-web-push"
doc_id: "chatty-notifications"
title: "How to set up web push notifications for new messages in Chatty"
category: "faq"
subcategory: "notifications"
tags: ["notifications", "web push", "browser notifications", "push notifications", "Chrome notifications", "Firefox notifications", "not receiving notifications"]
applies_when: "When a merchant asks how to set up web push notifications or why they are not receiving browser notifications"
priority: "high"
```

## Web Push Notifications

Web push sends browser notifications for new messages. You need to enable notifications in both the Chatty app AND in your browser.

**Step 1: Enable in Chatty app**
Go to **Notifications** → In "Notify me when", select **Web** for:
- A conversation is assigned to me
- New message from unassigned conversations
- New message from conversations assigned to me
- New message from AI assistant conversations
- No reply in 15 minutes from conversations assigned to me

**Step 2: Enable in your browser**

Supported browsers: Chrome, Microsoft Edge, Firefox, Opera, Samsung Internet.

- **Chrome:** In Notifications → Click **Manage** → Turn on Notifications → Back to Chatty → Click **Save** → Click **Send test** to verify
- **Microsoft Edge:** In Notifications → Click **Manage** → Turn on Notifications → Refresh page → Click **Save** → **Send test**
- **Firefox:** Firefox can't grant permission inside Shopify embed mode. Go to the Chatty web app instead: In the top banner, click **Set up in web app** → In web app, click **Enable** → Allow the browser popup → Refresh page → **Send test**
- **Opera:** Turn on web push notifications → Allow in popup → Refresh → **Save** → **Send test**

**Step 3: Enable on your device**

- **Windows:** Settings → System → Notifications → Find your browser → Turn on notifications
- **MacOS:** Apple menu → Notifications → Application Notifications → Find your browser → Turn on
- **Mobile:** Download and use the Chatty mobile app for mobile notifications.

---

<!-- CHUNK: notifications-email-sound -->
```yaml
chunk_id: "faq__notifications-email-sound"
doc_id: "chatty-notifications"
title: "How to set up email notifications and sound alerts in Chatty"
category: "faq"
subcategory: "notifications"
tags: ["email notifications", "sound notifications", "notification email", "spam notifications", "unanswered AI notification", "escalation notification"]
applies_when: "When a merchant asks how to set up email or sound notifications, or how to get notified when AI can't answer"
priority: "high"
```

## Email Notifications

Go to **Notifications** → Select **Email** for the events you want:
- A conversation is assigned to me
- New message from unassigned conversations
- New message from assigned conversations
- No reply in 15 minutes from assigned conversations

Click **Save**. Click **Send test** to check a sample email.

**To prevent Chatty emails from going to spam:**
- Add Chatty's email to your safe sender list, or
- Open a Chatty notification email → Click the three dots menu → Select "Filter messages like this" → "Never send to Spam" + "Always mark as important" → Create filter

## Sound Notifications

Turning on sound notifications plays an audio alert for new messages. Choose whether to play sound for only the first message or all messages.

## AI Escalation Email Notifications

To receive email notifications when the AI cannot answer or a customer needs help:

1. Go to **Settings** → **Notifications** → **Email Notifications**
2. Enable the **Unanswered by AI** or **Escalation** notifications
3. Enter the email address(es) that should receive alerts

You can also configure this per agent in Team Settings.

---

<!-- CHUNK: notifications-troubleshooting -->
```yaml
chunk_id: "faq__notifications-troubleshooting"
doc_id: "chatty-notifications"
title: "Troubleshooting missing push and email notifications in Chatty"
category: "faq"
subcategory: "notifications"
tags: ["notifications not working", "push notifications iPhone", "not receiving email notifications", "notification troubleshoot", "human transfer notification"]
applies_when: "When a merchant is not receiving push notifications on iPhone or not getting email notifications when a conversation is transferred"
priority: "high"
```

## Not Receiving Push Notifications on iPhone

Steps to fix:

1. Confirm the Chatty web app is opened from your Home Screen (not browser)
2. In the app, go to Settings → Notifications and tap **Allow** if not already done
3. Go to iPhone Settings → Notifications and verify Chatty is listed with Banners, Sounds, and Badges enabled
4. Check that Silent mode / Do Not Disturb is not blocking notifications
5. If still not working, remove the web app from Home Screen, re-add it, and repeat the steps to trigger a fresh notification prompt

## Not Receiving Email Notifications for Transferred Conversations

Check:

1. **Settings** → **Notifications** — email notifications must be enabled
2. If conversations are auto-assigned to a specific team member, that member must enable "There is a conversation assigned to me" in their own notification settings
3. Check spam/junk folder
4. Ensure you have not previously unsubscribed from Chatty notification emails
