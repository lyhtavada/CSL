---
category: Settings
subcategory: Email
topic: Custom Email Sending Domain
source: helpcenter
---

Q: What is Custom Email Sending Domain in Joy Loyalty?
Q: How do I set up Custom Email Sending Domain?
Q: Where can I find Custom Email Sending Domain settings?
A: Set up a custom sending domain in Joy to send loyalty program emails from your own domain (e.g., [[email protected]](/cdn-cgi/l/email-protection)), providing the highest level of email authentication and brand consistency.

This feature is available for **Advanced, and Enterprise plans**.

## Introduction

Enhance your brand’s professionalism and email deliverability by sending loyalty emails directly from your own domain. This approach gives you:

- **Stronger email authentication** through proper SPF, DKIM, and DMARC alignment.
- **Reliable email delivery** by establishing your own sending reputation.
- **A cohesive brand experience**, instilling trust by maintaining consistency from inbox to website.

Here is a video for setting up a custom simple sender, sending domain, and SMTP with step-by-step instructions, along with detailed explanations. Browse to bookmarks to find your needed part:

## Step-by-step setup

Let's dive in step by step-by-step guide to add your domain as an email sending domain. If you have already done this in other email marketing apps, this bears a resemblance.

### Step 1: Add your domain

Email service providers consider your sending domain as an identity for scoring reputation. It is a best practice to send your email using your subdomain dedicated for emailing; if not, once your sending reputation gets low, only the subdomain gets flagged, not the root one.

Go to the Joy app, open the `Settings > Email page`, and find `Custom sending domain` section. Click on the button to add a domain. Choose your subdomain nicely, like `rewards.example.com` or `loyalty.example.com`

Fill your domain in the first input and the sub in the second.

### Step 2: Verify your domain

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


(See the full help center article for more details.)