This guide covers setting up custom email senders in Joy to ensure your loyalty program emails are sent from your brand, improving deliverability and customer trust.

circle-info

This feature is available for **Professional, Advanced, and Enterprise plans**. The Custom email sending domain is on Advanced only.

## [hashtag](#introduction) Introduction

Joy offers flexible email sender customization options:

1. **Simple Custom Sender** - Use Joy's shared domain (send.avada.io) with your custom sender information. You can use this with a simple SPF, but a [DMARCarrow-up-right](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/) policy to "none". This is okay for a personal email sender. But for business email, it is recommended to use a custom domain sender.
2. **Custom SMTP Integration** - Connect your own email service provider like Amazon SES for full control.
3. **Custom domain sending** - Verify your email domain with SPF, DKIM to send on behalf of your domain. This is so much better than the Simple Custom Sender option. View this in our [separate guide.](/settings/email/custom-email-sending-domain)

Here is a video for setting up a custom simple sender, sending domain, and SMTP with step-by-step instructions, along with detailed explanations. Browse to bookmarks to find your needed part:

## [hashtag](#simple-custom-sender-setup) Simple custom sender setup

With this simple customer setup, it is recommended only to send on behalf of a personal email like Gmail or a domain that has the [DMARCarrow-up-right](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/) policy set to "none". You still need to add an SPF record.

### [hashtag](#before-we-start) Before we start

Once you verify your custom sender, by default, you will be sending emails via our shared domain. When using our shared domain **send.avada.io**, you can customize the display name and email address. This allows you to easily manage email communication without the need for a complex setup. However, because the sending domain will be **send.avada.io**, SPF alignment won’t be possible if your domain has a strict DMARC policy of "reject". It is not recommended to change your DMARC policy to "none" just to make this work.

Despite this, our domain has a strong reputation for reliable delivery. If you are just starting out, it is good to enjoy good sending results by using our domain.

circle-info

Joy is a company of Avada. In Avada, we have many apps that send transactional emails with real human interactions. Our shared domain has a good reputation, and we often fight against spamming activities.

### [hashtag](#verify-your-sender) Verify your sender

Even if you use a shared domain or custom SMTP, you both need to verify that your email sender is a valid email address. First, fill in the email address and the name of the sender (which shows in the email). Click on the **Verify** button to send a verification email to your email address > check your mailbox and find the verification email.

You will receive an email like this. Click on the "Verify your email" CTA to verify your sender.

Back to our app, hit the reload button to see the updated verification status. Then you can now **turn on** the Customer email sender.

### [hashtag](#what-youll-need) Add your SPF record

In order to allow our app to send the email on your behalf, please add our domain mailgun.org to your existing SPF record, for example:

My current SPF value is: `v=spf1 include:_spf.google.com include:_spf.protection.outlook.com include:secureserver.net ~all`

I need to change to `v=spf1 include:mailgun.org include:_spf.google.com include:_spf.protection.outlook.com include:secureserver.net ~all`

Also, to make sure that we update the existing SPF if it has one, try not to end up having multiple SPF records. You can go to [MX toolboxarrow-up-right](https://mxtoolbox.com/SuperTool.aspx), use the SPF tool to check your domain's SPF record:

### [hashtag](#what-youll-need-1) Test your sending

Once done, you can go to a notification email and send a test email. Here is how it looks when you see the email in the inbox. The image below is a personal sender email, sent via **send.avada.io**.

## [hashtag](#custom-smtp-integration) Custom SMTP Integration

For full control over your email delivery and authentication, you can configure your own SMTP server. This option allows you to send emails directly from your own domain, ensuring SPF and DKIM alignment for better email authentication.

Recommended SMTP services:

- **Amazon SES**: A highly scalable and cost-effective option for sending transactional emails.
- **SendGrid**: Known for its reliable delivery and user-friendly interface.
- **Mailgun**: Great for developers who need flexibility and detailed analytics.
- **Google Workspace SMTP**: Ideal if you already use Google Workspace for business email.

For ease of setup and reliable delivery, using our shared domain is a great option. However, if you want full control over email authentication and domain alignment, configuring your own SMTP server—such as Amazon SES or SendGrid—will provide that flexibility.

circle-info

With SMTP, your sending reputation relies completely on your infrastructure.

## [hashtag](#wrap-up) Custom domain email sender

Please refer to our [dedicated guide](/settings/email/custom-email-sending-domain) on configuring a custom email sending domain

## [hashtag](#wrap-up-1) Wrap up

Customizing your email sender helps reinforce your brand and ensure reliable communication. Whether you choose Joy’s shared domain for simplicity or your own SMTP for full control and authentication, both options allow you to tailor email delivery to your business needs. Verify your sender, set up the configuration, and start sending branded, professional emails your customers can trust.

## [hashtag](#faqs) FAQs

#### [hashtag](#what-if-my-email-provider-is-not-on-your-provider-list) **What if my email provider is not on your provider list?**

It is okay. The list is just a template for you to start more easily. If your SMTP provider gives you a host, port, username, and password, then you can just fill them in. Then you are good to go.

#### [hashtag](#cannot-see-emails-in-the-inbox-with-the-custom-sender-even-though-i-set-up-the-spf) Cannot see emails in the inbox with the custom sender, even though I set up the SPF?

Probably you have your DMARC policy to reject or quarantine. As you mentioned that with a simple sender, we will send emails via our domain send.avada.io. But our sending domain is send.avada.io, it does not match your from address, like "[[email protected]](/cdn-cgi/l/email-protection)" so according to DMARC policy, the email is bounced. In that case, you can set an unsafe DMARC policy as "none" and monitor your DMARC policy violation via the mailto config.

Many apps like [Klaviyoarrow-up-right](http://klaviyo.com/), Omnisend do support this method, but also strongly recommend not to. Why? Because with SPF record allows mailgun.org, anyone who registers [Mailgunarrow-up-right](https://www.mailgun.com/) email sending service can just fill your email address as their from address and send on your behalf, even though it still requires some efforts.

The second way to improve your sending reputation is to use [our custom email sending domain](/settings/email/custom-email-sending-domain).

[PreviousEmailchevron-left](/settings/email)[NextCustom email sending domainchevron-right](/settings/email/custom-email-sending-domain)

Last updated 19 days ago

Was this helpful?