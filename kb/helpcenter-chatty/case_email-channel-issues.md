# Email Channel Issues

<!-- CHUNK: email-outlook-hotmail -->
```yaml
chunk_id: "email__outlook-hotmail"
doc_id: "chatty-email-channel"
title: "Outlook/Hotmail email forwarding not working with Chatty"
category: "email-channel"
tags: ["Outlook", "Hotmail", "email forwarding", "not working", "Microsoft", "Cloudflare"]
applies_when: "Emails from Hotmail or Outlook are not being forwarded to Chatty inbox"
```

## Outlook/Hotmail Forwarding Not Working

This is a known compatibility issue between Cloudflare and Microsoft's mail system.

**Workarounds:**
1. **Use an intermediate mailbox** — set up a Gmail to receive from Outlook/Hotmail, then forward to Chatty
2. **Switch email hosting** — consider Google Workspace or Zoho Mail, then forward to Chatty
3. **Enable alternative notifications** — turn on email notifications via Gmail or install the Chatty mobile app

Guide the merchant to test after setting up the workaround.

---

<!-- CHUNK: email-forwarding-verification-fails -->
```yaml
chunk_id: "email__forwarding-verification-fails"
doc_id: "chatty-email-channel"
title: "Email forwarding verification fails"
category: "email-channel"
tags: ["verification", "email forwarding", "verification fails", "not verified", "forwarding address"]
applies_when: "Merchant set up email forwarding but verification is failing or not completing"
```

## Email Forwarding Verification Fails

Common causes: incorrect forwarding address, email provider blocking automatic forwarding, or verification email going to spam.

1. Verify the forwarding address is entered correctly
2. Ask the merchant to check spam/junk folder for the verification email
3. If using Outlook/Hotmail, note the Cloudflare compatibility issue and suggest alternative providers
4. If issue persists, check if the email sender configuration is blocking forwarding

---

<!-- CHUNK: email-spf-verification -->
```yaml
chunk_id: "email__spf-verification"
doc_id: "chatty-email-channel"
title: "Email sender verification failing — SPF records"
category: "email-channel"
tags: ["SPF", "email sender", "verification", "DNS", "SPF record", "sender verification"]
applies_when: "Email sender verification is failing, possibly due to SPF record configuration"
```

## Email Sender Verification Failing (SPF)

**Before advising, collect:**
- What email provider the merchant uses (Gmail, Cloudflare, GoDaddy, Namecheap, etc.)
- Whether they have access to their DNS settings (some merchants' DNS is managed by their web developer or IT team)

**Then guide:**
1. Ask the merchant (or their IT/DNS admin) to log in to their DNS provider and add the SPF record for Chatty
2. Refer them to their email provider's documentation for exact SPF record values — DNS configuration varies per provider
3. Warn: DNS changes can take up to 48 hours to propagate
4. Follow up after 48 hours to confirm verification passed

> Note: Support agents cannot access a merchant's DNS settings — the merchant or their DNS admin must make this change themselves.

---

<!-- CHUNK: email-verification-not-received -->
```yaml
chunk_id: "email__verification-not-received"
doc_id: "chatty-email-channel"
title: "Verification email for email channel setup never arrived"
category: "email-channel"
tags: ["verification email", "not received", "email setup", "no email", "missing verification"]
applies_when: "Merchant did not receive the verification email when setting up email channel"
```

## Verification Email Never Arrived

1. Ask the merchant to check spam/junk folders
2. Some corporate email providers block automated verification emails
3. Verify the email was entered correctly in settings
4. If none of the above, try resending the verification email or use an alternative email address

---

<!-- CHUNK: email-going-to-spam -->
```yaml
chunk_id: "email__going-to-spam"
doc_id: "chatty-email-channel"
title: "Chatty emails going to customers' spam"
category: "email-channel"
tags: ["spam", "junk", "email spam", "deliverability", "DKIM", "DMARC", "SPF"]
applies_when: "Chatty emails are landing in customers' spam or junk folders"
```

## Chatty Emails Going to Spam

This is typically caused by missing email authentication records.

**Before advising, collect:**
- Which email/domain the merchant is sending from (custom domain or default `noreply@chattyemail.com`?)
- Who manages their DNS (merchant themselves, web developer, or IT admin?)

**Then guide:**
1. Ask the merchant (or DNS admin) to add **SPF records** in their DNS provider
2. Verify **DKIM** and **DMARC** records are also properly configured — all three are needed for good deliverability
3. Recommend using a **custom sender domain** instead of the default `noreply@chattyemail.com` if they haven't already
4. If the merchant uses a custom domain, verify the domain is confirmed in Chatty → Channels → Email settings

> Note: Support agents cannot access a merchant's DNS settings. The merchant or their DNS admin must make these changes. DNS propagation can take up to 48 hours.

---

<!-- CHUNK: email-spf-setup -->
```yaml
chunk_id: "email__spf-setup"
doc_id: "chatty-email-channel"
title: "How to add SPF records for Chatty email"
category: "email-channel"
tags: ["SPF records", "DNS", "email authentication", "spam prevention", "configure SPF"]
applies_when: "Merchant needs to configure SPF records for Chatty email delivery"
```

## Adding SPF Records for Chatty Email

Guide the merchant to add SPF records in their DNS provider settings. This ensures emails sent through Chatty are authenticated and less likely to be flagged as spam.

The specific SPF record values depend on the merchant's email hosting provider — refer to their provider's documentation for exact configuration steps.

---

<!-- CHUNK: email-multiple-addresses -->
```yaml
chunk_id: "email__multiple-addresses"
doc_id: "chatty-email-channel"
title: "Using multiple email addresses with Chatty"
category: "email-channel"
tags: ["multiple emails", "alias email", "additional email", "multiple addresses", "email alias"]
applies_when: "Merchant wants to use multiple email addresses or alias emails with Chatty"
```

## Multiple Email Addresses

Chatty supports **one email per store** via forwarding. For additional email addresses, set up email forwarding from alias addresses to the connected Chatty email.

Contact support if you have specific needs around multiple email addresses or alias setups.

---

<!-- CHUNK: email-contact-button-wrong-client -->
```yaml
chunk_id: "email__contact-button-wrong-client"
doc_id: "chatty-email-channel"
title: "Email button in chatbox opens wrong email client"
category: "email-channel"
tags: ["email button", "contact us", "wrong email client", "email icon", "chatbox email button"]
applies_when: "Clicking the email icon in the Contact Us widget opens the wrong email client"
```

## Email Button Opens Wrong Client

The behavior depends on the merchant's chatbox configuration and the customer's device default email client settings.

Verify the email address is correctly set in the **Contact Us** block settings.

---

<!-- CHUNK: email-fail-to-deliver -->
```yaml
chunk_id: "email__fail-to-deliver"
doc_id: "chatty-email-channel"
title: "Merchant receiving Fail to Deliver error emails"
category: "email-channel"
tags: ["fail to deliver", "delivery failure", "bounce", "email error", "delivery error"]
applies_when: "Merchant is receiving delivery failure notification emails"
```

## Fail to Deliver Errors

These errors typically occur when the recipient email is invalid or the email provider rejects the message.

Verify the recipient email addresses and check email forwarding configuration for any issues.

---

<!-- CHUNK: email-change-admin -->
```yaml
chunk_id: "email__change-admin"
doc_id: "chatty-email-channel"
title: "Change admin email for Chatty account"
category: "email-channel"
tags: ["admin email", "change email", "store owner", "account email", "transfer admin"]
applies_when: "Merchant wants to change the admin email address for their Chatty account"
```

## Changing Admin Email

The admin email is tied to the Shopify store owner account.

1. Go to Chatty app settings → check **Team settings** for the current admin email
2. If the merchant needs to change the primary admin, they may need to update their Shopify store owner email first, then re-access Chatty

---

<!-- CHUNK: email-reply-to-field -->
```yaml
chunk_id: "email__reply-to-field"
doc_id: "chatty-email-channel"
title: "Forwarding email showing in Reply-To field"
category: "email-channel"
tags: ["reply-to", "forwarding email", "wrong sender", "reply-to header", "email sender"]
applies_when: "The forwarding email address is showing in the Reply-To field instead of the store's actual support email"
```

## Forwarding Email Showing in Reply-To

1. Go to **Chatty** → **Channels** → **Email**
2. Check the **Email sender** field — make sure it's set to your actual store support email, not the Chatty forwarding address
3. Save and send a test reply to yourself to confirm the correct email appears in Reply-To

---

<!-- CHUNK: email-ai-replies -->
```yaml
chunk_id: "email__ai-replies"
doc_id: "chatty-email-channel"
title: "Does AI reply to email conversations reach the customer"
category: "email-channel"
tags: ["AI email reply", "email reply", "customer receives", "noreply", "custom sender"]
applies_when: "Merchant asks whether AI or agent replies sent via Chatty are delivered to the customer's email"
```

## AI/Agent Email Replies Delivered to Customer

Yes — replies sent through Chatty (by AI or human agents) are delivered to the customer's email. The default sender address is `noreply@chattyemail.com` unless you have configured a custom sender domain.

---

<!-- CHUNK: email-klaviyo-reply-to -->
```yaml
chunk_id: "email__klaviyo-reply-to"
doc_id: "chatty-email-channel"
title: "Use Klaviyo to send outreach emails and have Chatty handle replies"
category: "email-channel"
tags: ["Klaviyo", "reply-to", "outreach", "email campaign", "Chatty inbox", "Klaviyo integration"]
applies_when: "Merchant wants to send Klaviyo campaign emails and have replies appear in Chatty inbox"
```

## Klaviyo Outreach + Chatty Reply Handling

Set up your Klaviyo campaign with a **Reply-To** address that is connected to a Chatty email channel. When leads reply to the email, their response will appear in Chatty's inbox as a new conversation, where AI or your team can take over.

---

## Related
- case_notification-issues (push and email notification problems)
- case_whatsapp-messenger-issues (other channel issues)

---

<!-- CHUNK: email-corporate-it-restriction -->
```yaml
chunk_id: "email__corporate-it-restriction"
doc_id: "chatty-email-channel"
title: "Corporate email IT admin must allow forwarding to Chatty"
category: "email-channel"
tags: ["corporate email", "IT admin", "forwarding blocked", "organization policy", "email forwarding", "IT restriction"]
applies_when: "Merchant uses a corporate or organization-managed email and forwarding to Chatty is blocked"
priority: "high"
```

## Corporate Email — IT Admin Approval Required

If the merchant's email is managed by their organization's IT department, **auto-forwarding to external addresses may be blocked by policy**.

**Resolution:**
1. Confirm with the merchant whether their email is corporate/IT-managed
2. Ask them to contact their **IT administrator** to allow auto-forwarding to Chatty's forwarding address (`xxxx.forward@chatty.email`)
3. Once IT unlocks forwarding → the merchant can complete the email channel setup in Chatty
4. If IT won't allow it → suggest using a personal Gmail account to forward emails, then route those to Chatty

> This is separate from the Outlook/Cloudflare issue. IT-managed email forwarding blocks affect all email providers (Gmail Workspace, Outlook, custom domains) when IT policies restrict outbound forwarding.
