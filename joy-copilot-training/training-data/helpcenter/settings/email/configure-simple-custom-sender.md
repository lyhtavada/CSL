---
category: Settings
subcategory: Email
topic: Configure Simple Custom Sender
source: helpcenter
---

Q: What is Configure Simple Custom Sender in Joy Loyalty?
Q: How does Configure Simple Custom Sender work?
Q: Where can I find Configure Simple Custom Sender settings?
A: This guide covers setting up custom email senders in Joy to ensure your loyalty program emails are sent from your brand, improving deliverability and customer trust.

This feature is available for **Professional, Advanced, and Enterprise plans**. The Custom email sending domain is on Advanced only.

## Introduction

Joy offers flexible email sender customization options:

1. **Simple Custom Sender** - Use Joy's shared domain (send.avada.io) with your custom sender information. You can use this with a simple SPF, but a [DMARC](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/) policy to "none". This is okay for a personal email sender. But for business email, it is recommended to use a custom domain sender.
2. **Custom SMTP Integration** - Connect your own email service provider like Amazon SES for full control.
3. **Custom domain sending** - Verify your email domain with SPF, DKIM to send on behalf of your domain. This is so much better than the Simple Custom Sender option. View this in our [separate guide.](/settings/email/custom-email-sending-domain)

Here is a video for setting up a custom simple sender, sending domain, and SMTP with step-by-step instructions, along with detailed explanations. Browse to bookmarks to find your needed part:

## Simple custom sender setup

With this simple customer setup, it is recommended only to send on behalf of a personal email like Gmail or a domain that has the [DMARC](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/) policy set to "none". You still need to add an SPF record.

### Before we start

Once you verify your custom sender, by default, you will be sending emails via our shared domain. When using our shared domain **send.avada.io**, you can customize the display name and email address. This allows you to easily manage email communication without the need for a complex setup. However, because the sending domain will be **send.avada.io**, SPF alignment won’t be possible if your domain has a strict DMARC policy of "reject". It is not recommended to change your DMARC policy to "none" just to make this work.

Despite this, our domain has a strong reputation for reliable delivery. If you are just starting out, it is good to enjoy good sending results by using our domain.

Joy is a company of Avada. In Avada, we have many apps that send transactional emails with real human interactions. Our shared domain has a good reputation, and we often fight against spamming activities.

### Verify your sender


(See the full help center article for more details.)