# Email Channel Issues — FAQ

<!-- CHUNK: email-outlook-hotmail-not-forwarding -->
```yaml
chunk_id: "faq__email-outlook-hotmail"
doc_id: "chatty-email-channel-issues"
title: "Outlook and Hotmail emails not forwarding to Chatty"
category: "email-channel"
tags: ["Outlook", "Hotmail", "forwarding", "Cloudflare", "Microsoft", "email compatibility"]
applies_when: "Email forwarding from Outlook or Hotmail is not working with Chatty"
```

## Outlook/Hotmail Forwarding Not Working

Known compatibility issue between Cloudflare and Microsoft's mail system.

**Workarounds:**
1. Use an intermediate mailbox: set up Gmail to receive from Outlook/Hotmail, then forward to Chatty
2. Switch email hosting to Google Workspace or Zoho Mail, then forward to Chatty
3. Enable email notifications via Gmail or install Chatty mobile app as alternative

Guide the merchant to test after setting up the workaround.

---

<!-- CHUNK: email-forwarding-verification-fails -->
```yaml
chunk_id: "faq__email-forwarding-verification-fails"
doc_id: "chatty-email-channel-issues"
title: "Email forwarding verification fails or not getting verified"
category: "email-channel"
tags: ["verification", "forwarding verification", "email verification", "spam folder", "verification email"]
applies_when: "Merchant set up email forwarding but verification fails or verification email never arrives"
```

## Email Forwarding Verification Failing

1. Verify forwarding address is entered correctly
2. Ask merchant to check spam/junk folder for the verification email
3. If using Outlook/Hotmail → suggest alternative email provider (known Cloudflare issue)
4. If persists → check if email sender configuration is blocking forwarding

---

<!-- CHUNK: email-spf-records -->
```yaml
chunk_id: "faq__email-spf-records"
doc_id: "chatty-email-channel-issues"
title: "SPF record configuration for Chatty email"
category: "email-channel"
tags: ["SPF", "SPF record", "DNS", "email authentication", "delivery", "DKIM", "DMARC"]
applies_when: "Merchant needs to configure SPF records for email delivery or is having email authentication issues"
```

## SPF Record Configuration

Guide the merchant to add SPF records in their DNS provider settings. The specific values depend on the merchant's email hosting provider — refer to their email provider's documentation.

For spam issues, also verify:
- DKIM and DMARC records are configured
- Using a custom sender domain instead of the default `noreply@chattyemail.com`
- Custom domain is verified in Chatty settings

DNS changes can take up to 48 hours to propagate.

---

<!-- CHUNK: email-verification-email-not-received -->
```yaml
chunk_id: "faq__email-verification-not-received"
doc_id: "chatty-email-channel-issues"
title: "Verification email for email channel setup never arrived"
category: "email-channel"
tags: ["verification email", "not received", "setup", "email channel setup", "spam"]
applies_when: "Merchant didn't receive the verification email when setting up email channel"
```

## Verification Email Not Received

1. Check spam/junk folder
2. Some corporate email providers block automated verification emails
3. Verify email was entered correctly in settings
4. If none of the above → try resending verification or use an alternative email address

---

<!-- CHUNK: email-going-to-spam -->
```yaml
chunk_id: "faq__email-going-to-spam"
doc_id: "chatty-email-channel-issues"
title: "Chatty emails going to spam"
category: "email-channel"
tags: ["spam", "junk", "email deliverability", "SPF", "DKIM", "DMARC", "custom sender domain"]
applies_when: "Customers receive Chatty emails in spam or junk folder"
```

## Chatty Emails Going to Spam

Typically caused by missing or incorrect email authentication records.

1. Add SPF records in DNS settings
2. Verify DKIM and DMARC records are configured
3. Use a custom sender domain instead of `noreply@chattyemail.com`
4. Verify custom domain in Chatty settings

---

<!-- CHUNK: email-alias-multiple -->
```yaml
chunk_id: "faq__email-alias-multiple"
doc_id: "chatty-email-channel-issues"
title: "Using multiple email addresses or aliases with Chatty"
category: "email-channel"
tags: ["alias email", "multiple emails", "email channels", "forwarding alias"]
applies_when: "Merchant wants to use multiple email addresses or aliases with Chatty"
```

## Multiple Email Addresses / Aliases

Chatty supports one email per channel. For additional addresses, set up email forwarding from alias addresses to the connected Chatty email.

---

<!-- CHUNK: email-wrong-client-opens -->
```yaml
chunk_id: "faq__email-wrong-client"
doc_id: "chatty-email-channel-issues"
title: "Email icon in chatbox opens wrong email client"
category: "email-channel"
tags: ["email icon", "wrong email client", "contact us", "chatbox button", "email client"]
applies_when: "Clicking the email icon in the chatbox widget opens the wrong email client"
```

## Email Button Opens Wrong Client

The email contact button behavior depends on the customer's device default email client. Verify the email address is correctly set in the **Contact Us** block settings.

---

<!-- CHUNK: email-fail-to-deliver -->
```yaml
chunk_id: "faq__email-fail-to-deliver"
doc_id: "chatty-email-channel-issues"
title: "Merchant gets Fail to Deliver error emails"
category: "email-channel"
tags: ["fail to deliver", "delivery failure", "bounce", "error email", "invalid email"]
applies_when: "Merchant receives delivery failure notifications"
```

## Fail to Deliver Errors

Typically the recipient email is invalid or the email provider rejected the message. Verify recipient email addresses and check email forwarding configuration.

---

<!-- CHUNK: email-change-admin-email -->
```yaml
chunk_id: "faq__email-change-admin"
doc_id: "chatty-email-channel-issues"
title: "Change admin email for a Chatty account"
category: "email-channel"
tags: ["admin email", "change email", "account email", "store owner email"]
applies_when: "Merchant wants to change the admin email for their Chatty account"
```

## Changing Admin Email

The admin email is tied to the Shopify store owner account.

1. Check **Team** settings for current admin email
2. To change primary admin → update Shopify store owner email first, then re-access Chatty

---

<!-- CHUNK: email-reply-to-forwarding-address -->
```yaml
chunk_id: "faq__email-reply-to-wrong"
doc_id: "chatty-email-channel-issues"
title: "Forwarding email address showing in Reply-To field"
category: "email-channel"
tags: ["Reply-To", "forwarding address", "email sender", "reply address", "wrong reply-to"]
applies_when: "The Chatty forwarding address is showing in the Reply-To field instead of the store's support email"
```

## Wrong Reply-To Address

1. Go to **Chatty** → **Channels** → **Email**
2. Check **Email sender** field — set it to actual store support email, not the Chatty forwarding address
3. Save → send a test reply to confirm correct email appears in Reply-To

---

<!-- CHUNK: email-ai-replies-to-email -->
```yaml
chunk_id: "faq__email-ai-replies"
doc_id: "chatty-email-channel-issues"
title: "AI replies to email conversations"
category: "email-channel"
tags: ["AI email reply", "email channel AI", "auto-reply email", "AI response email"]
applies_when: "Merchant asks if AI replies to email conversations or if customers receive AI responses via email"
```

## AI Replies to Email Conversations

Yes — replies sent through Chatty (by AI or human agents) are delivered to the customer's email. Default sender: `noreply@chattyemail.com` unless a custom sender domain is configured.

---

<!-- CHUNK: email-klaviyo-reply-tracking -->
```yaml
chunk_id: "faq__email-klaviyo-reply"
doc_id: "chatty-email-channel-issues"
title: "Use Klaviyo for outreach and Chatty to handle replies"
category: "email-channel"
tags: ["Klaviyo", "outreach email", "reply tracking", "Reply-To", "email campaign", "inbox replies"]
applies_when: "Merchant wants to send Klaviyo campaigns but have replies appear in Chatty"
```

## Klaviyo Outreach + Chatty Inbox

Set up the Klaviyo campaign with a **Reply-To** address connected to a Chatty email channel. When leads reply, their response appears in Chatty's inbox as a new conversation where AI or agents can take over.
