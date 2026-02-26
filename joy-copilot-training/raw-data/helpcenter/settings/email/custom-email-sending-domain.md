Set up a custom sending domain in Joy to send loyalty program emails from your own domain (e.g., [[email protected]](/cdn-cgi/l/email-protection)), providing the highest level of email authentication and brand consistency.

circle-info

This feature is available for **Advanced, and Enterprise plans**.

## [hashtag](#introduction) Introduction

Enhance your brand’s professionalism and email deliverability by sending loyalty emails directly from your own domain. This approach gives you:

- **Stronger email authentication** through proper SPF, DKIM, and DMARC alignment.
- **Reliable email delivery** by establishing your own sending reputation.
- **A cohesive brand experience**, instilling trust by maintaining consistency from inbox to website.

Here is a video for setting up a custom simple sender, sending domain, and SMTP with step-by-step instructions, along with detailed explanations. Browse to bookmarks to find your needed part:

## [hashtag](#step-by-step-setup) Step-by-step setup

Let's dive in step by step-by-step guide to add your domain as an email sending domain. If you have already done this in other email marketing apps, this bears a resemblance.

### [hashtag](#step-1-add-your-domain) Step 1: Add your domain

Email service providers consider your sending domain as an identity for scoring reputation. It is a best practice to send your email using your subdomain dedicated for emailing; if not, once your sending reputation gets low, only the subdomain gets flagged, not the root one.

Go to the Joy app, open the `Settings > Email page`, and find `Custom sending domain` section. Click on the button to add a domain. Choose your subdomain nicely, like `rewards.example.com` or `loyalty.example.com`

Fill your domain in the first input and the sub in the second.

### [hashtag](#step-2-verify-your-domain) Step 2: Verify your domain

This step will get a little technical, but stay tuned. We will make it as intuitive as possible. Once the domain is added, you will see this guide on how to fill in your DNS settings:

Here is the breakdown of those record values with their purpose. Bare in mind that the value in your app is what you should be input to your DNS settings, below are just for example.

Record Type

Name

Value (Example)

Purpose

**SPF (TXT)**

`send` or `loyalty` or `rewards` based on your setting domain.

`v=spf1 include:mailgun.org ~all`

Authorizes Joy to send emails based on your domain.

**DKIM (TXT)**

`[generated-key]`

`[generated-value]`

Your signature that proof that this email is sent on your behalf.

**DMARC (TXT)**

`_dmarc.[subdomain value]`

`v=DMARC1; p=none; rua=mailto:[email protected]`

Policy for authentication failures

**CNAME**

`email`

`mailgun.org`

Routes email through Joy's infrastructure

**MX**

`send`

`mxa.mailgun.org` (Priority: 10)

Mail exchange record

**MX**

`send`

`mxb.mailgun.org` (Priority: 10)

Backup mail exchange

circle-info

If it already has an existing SPF record, just append our "include:mailgun.org" to your SPF value. But with the case of a subdomain, it perhaps does not yet have an existing value.

### [hashtag](#step-3-fill-in-your-dns) Step 3: Fill in your DNS

If you verify your domain to connect to Shopify, you probably know how to find your DNS settings, but let us still list out how to find the most common DNS settings.

Provider

Guide

Note

Shopify

[Editing the DNS settings for your Shopify-managed domainarrow-up-right](https://help.shopify.com/en/manual/domains/managing-domains/edit-dns-settings)

GoDaddy

[Manage DNS recordsarrow-up-right](https://www.godaddy.com/en/help/manage-dns-records-680)

Cloudflare

[Manage DNS recordsarrow-up-right](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)

Google Domains

[DNS basicsarrow-up-right](https://support.google.com/a/answer/48090?src=supportwidget0&hl=en&authuser=0)

Cannot really find a official guide on this. But this guide can take you there

Namecheap

[How do I set up host records for a domain?arrow-up-right](https://www.namecheap.com/support/knowledgebase/article.aspx/434/2237/how-do-i-set-up-host-records-for-a-domain/)

Each provider may provide a different DNS management UI/UX. But key concepts stay the same because every record has the type, name, value, and priority. You may find they call it with a similar name, but rest assured, it has the same effect.

You can go to [MX toolboxarrow-up-right](https://mxtoolbox.com/SuperTool.aspx), use the SPF tool to check your domain's records.

### [hashtag](#step-4-verify-your-domain) Step 4: Verify your domain

Once all DNS settings are set, you can click on the verify button in our app to check if the DNS setting is propagated or not.

circle-info

It may take up to 24 hours to propagate the DNS setting; you may need to check again after a while.

### [hashtag](#step-5-add-your-sender) Step 5: Add your sender

If you have a verified sending domain like `rewards.canyoncomestic.store` then you can add a sender of that domain without verifying with email confirmation. You can add like `[email protected]` a sender (not a subdomain email).

### [hashtag](#faqs) FAQs

#### [hashtag](#if-i-remove-and-add-a-domain-again-do-i-have-to-add-every-record-again) If I remove and add a domain again, do I have to add every record again?

If the subdomain is the same, then you only need to add the DKIM record again. You may end up having many DKIM records on your DNS settings; you can remove them or keep them.

#### [hashtag](#if-i-enable-the-smtp-will-it-send-using-smtp-or-the-domain) If I enable the SMTP, will it send using SMTP or the domain?

It will use the SMTP. The SMTP will override every other sending method.

#### [hashtag](#why-use-a-subdomain-can-i-use-my-root-domain) Why use a subdomain? Can I use my root domain?

It is strongly recommended not to, because of the domain reputation. It will hurt your root domain reputation in case your email sending is flagged as spam by ESP. This is our safeguard, so please follow it.

#### [hashtag](#can-i-change-the-dmarc-value-of-the-subdomain-to-reject) Can I change the DMARC value of the subdomain to reject?

Yes, you can. Because it aligns, so you can change it. Our app, by default, generates the policy value as "none". You can also change your mailto DMARC report email address.

[PreviousConfigure simple custom senderchevron-left](/settings/email/configure-simple-custom-sender)[NextOrderchevron-right](/settings/order)

Last updated 19 days ago

Was this helpful?