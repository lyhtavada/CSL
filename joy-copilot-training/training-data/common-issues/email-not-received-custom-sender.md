---
category: Notifications
problem: Emails not received after verifying Custom Sender (Simple Custom Sender)
source: notion
---

Q: I verified my custom sender email in Joy but customers aren't receiving emails. What's wrong?
Q: My Joy notification emails stopped working after I set up a custom sender. How do I fix this?
Q: Emails from Joy aren't being delivered even though my custom sender shows as verified. What should I check?
Q: Why are my Joy loyalty emails not arriving in my customers' inboxes after setting up Simple Custom Sender?
Q: I configured the custom email sender in Joy but no emails are going through. Help!

A: When using the **Simple Custom Sender** in Joy, emails are sent through the `send.avada.io` domain. If your emails aren't being delivered even though the sender is verified, it's usually related to your domain's email authentication settings. Let's troubleshoot:

### Step 1: Verify Sender Status
Go to your Joy email settings and confirm that your custom sender shows as **"Verified"**. If it's not verified, the emails won't send at all.

### Step 2: Check Your SPF Record
Your domain's SPF record needs to include `mailgun.org` (the email service used by Joy). You can check this using a tool like [MXToolbox](https://mxtoolbox.com/).

- Look for your SPF record (TXT record starting with `v=spf1`).
- Make sure it includes `include:mailgun.org`.
- If it's missing, add it to your domain's DNS settings.

### Step 3: Check Your DMARC Policy
This is the most common cause! If your domain has a strict **DMARC policy** set to `p=reject`, emails sent through `send.avada.io` on behalf of your domain will be blocked by receiving mail servers.

You can check your DMARC record using [MXToolbox DMARC Lookup](https://mxtoolbox.com/dmarc.aspx).

### Step 4: Fix DMARC Issues
If your DMARC policy is `p=reject`, you have two options:
- **Option A (Recommended):** Upgrade to **Custom SMTP** (available on Advanced/Enterprise plans), which sends emails directly from your own domain and avoids DMARC issues entirely.
- **Option B:** Change your DMARC policy to `p=none` (less secure, but allows third-party senders).

### Step 5: Test Your Emails
After making changes:
1. Go to **Email notification** settings in Joy.
2. Send a test email to yourself.
3. Check your **inbox**, **spam**, and **promotions** folders.

If emails still aren't being delivered after following these steps, please share your domain name and we'll investigate further!
