## [hashtag](#overview) Overview

A successful loyalty program isn’t just about earning points and rewards—it’s also about **visibility**. Customers need to see and remember your program if you want them to use it. The widget gives them in-store access, but notifications extend that visibility beyond your site.

That’s where **automated notifications** come in. They deliver timely reminders straight to customers’ inboxes—letting them know when they’ve earned points, reminding them of unused rewards, or celebrating milestones like birthdays. This keeps your program visible, personal, and hard to forget.

## [hashtag](#why-notifications-matter) Why notifications matter

Think of notifications as gentle nudges that **make your program visible outside your storefront**. They keep loyalty top of mind and encourage customers to come back, redeem, or engage further. A well-timed email can turn a one-time shopper into a repeat buyer.

Notifications also build **transparency and trust**. Customers don’t need to worry about forgetting a coupon code or missing a reward in the widget. For example, if someone signs up and forgets to copy their welcome coupon, they can always find it again in their email. This reduces support questions and makes your program feel more reliable.

To make sure you don’t overwhelm or spam your customers, notifications in Joy are **off by default**. You’re in control of which ones to activate. The idea is simple: only send messages that truly matter—like reward coupons, referral confirmations, or reminders about expiring points. This way, every email feels important and valuable.

## [hashtag](#where-notifications-apply) Where notifications apply

Notifications aren’t one-size-fits-all. They apply across different parts of your program:

- **Reward programs**: Earn points, redeem points, birthday rewards, and POS point redemption.
- **Referral programs**: Send coupons to both referrers and their friends.
- **VIP tiers**: Notify customers when they unlock or move up to a new VIP status.
- **Points expiry**: Remind customers when their points are about to expire.

Each notification type serves a different purpose, but together they keep customers engaged at every stage of their journey.

## [hashtag](#how-to-set-up) How to set up

### [hashtag](#email-sender-options) Email sender options

Choose how to send notification emails for best deliverability for your brand.

- Use a [**simple customer sender**](/settings/email/configure-simple-custom-sender) with SPF
- **Custom sender address**.
- **Own SMTP** for full control.
- Use your [custom email sending domain](/settings/email/custom-email-sending-domain)

### [hashtag](#brand-logo) Brand logo

Change your brand logo at Settings > Email > Logo. You can just change in one place and get it to applied to all notification email.

### [hashtag](#email-content) Email content

#### [hashtag](#choose-content) Choose content

To set up notifications, open **Settings > Notifications** in your Joy dashboard. Use the global toggle to enable notifications, then manage each program individually. Start with high-value options such as coupons and expiry reminders, and add more as you see fit.

Each template can be customized. You can edit subject lines, update the content, upload your logo, change color, and add personalized variables like customer name or point balance. Before activating, preview the message or send yourself a test email to make sure it feels right.

circle-info

Use color wisely. Should only use the primary color of your brand for the button, header section, which makes the email look consistent. The transactional email should look clean, informative, and transparent in favor of aesthetic design.

#### [hashtag](#variables) Variables

Also, use variables shown in the editor to make the content more dynamic. See the next section for variable reference.

#### [hashtag](#preview-and-test) Preview & Test

Click **Send Test**, input your email, and check how it looks before going live. Make sure to test where the emails land, the inbox or spam.

circle-info

Use a sender that customers have previously interacted with, such as: sign-up email, welcome email, etc. This will improve the deliverability.

### [hashtag](#shared-variables) Variable reference

Variable

Description

Redeem Points

POS Redeem

Reward Points

Points + Discount

Birthday

Sign Up

Pending Points

Referee

Referrer

Link Invite

VIP Tier

Pre-Tier

Points Expire

`{{shop_name}}`

Shop name

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

`{{customer_name}}`

Customer name

✓

-

✓

✓

✓

✓

✓

-

-

-

✓

✓

✓

`{{customer_email}}`

Customer email

✓

-

✓

✓

✓

✓

✓

-

-

-

✓

✓

✓

`{{points_balance}}`

Points balance\*

✓

✓

✓

✓

✓

✓

✓

✓

✓

-

✓

✓

✓

`{{coupon_expiry_date}}`

Coupon expiration

✓

✓

✓

✓

✓

✓

✓

✓

✓

-

-

-

-

`{{point_expired_at}}`

Points expiration

-

-

✓

✓

✓

✓

✓

✓

✓

-

-

-

✓

`{{earning_point_raw}}`

Raw points earned

-

-

✓

✓

✓

✓

✓

✓

-

-

-

-

-

`{{loyalty_point}}`

Loyalty points

-

✓

✓

✓

✓

✓

✓

✓

-

-

-

-

-

`{{earning_discount}}`

Discount earned

✓

✓

-

-

-

-

-

-

-

-

-

-

-

`{{points_per_discount}}`

Points per discount

✓

✓

-

-

-

-

-

-

-

-

-

-

-

`{{discount_per_points}}`

Discount per points

✓

✓

-

-

-

-

-

-

-

-

-

-

-

`{{discount_code}}`

Discount code

-

-

-

✓

✓

✓

-

-

-

-

-

✓

-

**Unique to Redemption**

`{{redeem_points}}`

Points redeemed

✓

-

-

-

-

-

-

-

-

-

-

-

-

`{{redeeming_program}}`

Redeeming program

✓

-

-

-

-

-

-

-

-

-

-

-

-

`{{redeemed_point_raw}}`

POS points redeemed

-

✓

-

-

-

-

-

-

-

-

-

-

-

**Unique to Earning**

`{{earning_program}}`

Earning program

-

-

✓

✓

✓

✓

✓

-

-

-

-

-

-

`{{birthday_reward}}`

Birthday reward

-

-

-

-

✓

-

-

-

-

-

-

-

-

`{{sign_up_reward}}`

Sign up reward

-

-

-

-

-

✓

-

-

-

-

-

-

-

`{{date}}`

Pending date

-

-

-

-

-

-

✓

-

-

-

-

-

-

**Unique to Referral**

`{{referee_discount}}`

Referee discount

-

-

-

-

-

-

-

✓

-

✓

-

-

-

`{{referrer_discount}}`

Referrer discount

-

-

-

-

-

-

-

-

✓

-

-

-

-

`{{referrer_name}}`

Referrer name

-

-

-

-

-

-

-

-

-

✓

-

-

-

`{{referral_link}}`

Referral link

-

-

-

-

-

-

-

-

-

✓

-

-

-

**Unique to VIP**

`{{tier_name}}`

Current tier

-

-

-

-

-

-

-

-

-

-

✓

✓

-

`{{next_tier}}`

Next tier

-

-

-

-

-

-

-

-

-

-

-

✓

-

`{{coupon_code}}`

Tier reward code

-

-

-

-

-

-

-

-

-

-

-

✓

-

**Unique to Expiration**

`{{send_email_before}}`

Days before expiry

-

-

-

-

-

-

-

-

-

-

-

-

✓

### [hashtag](#managing-sent-emails) Managing sent emails

Go to Customer > Notifications to manage your sent emails along with their status.

- Search by customer email
- Filter by status: Sent, Opened, Clicked, Failed.

Monitor and optimize email performance easily

### [hashtag](#best-practices) Best practices

Start small by enabling the most essential notifications first. Keep subject lines simple and clear, while making sure the body reflects your brand’s voice. Send notifications soon after the trigger event so they feel relevant. Remember that emails are not just reminders but also a **track log** customers can return to, making your program more transparent and dependable.

Always use a trusted sender to improve deliverability and avoid the spam folder. Verified domains, SMTP, or integrations with Klaviyo and Omnisend are the best ways to build long-term reliability.

### [hashtag](#faqs) FAQs

**Why are notifications off by default?**
They are off to ensure you don’t spam customers. You choose when and how to start, focusing on valuable messages such as coupons or expiry reminders.

**Which programs support notifications?**
Notifications are available for Reward programs (earn/redeem, birthday, POS), Referral programs, VIP tiers, and Points expiry.

**Can I customize the email content?**
Yes. You can edit the subject, body, logo, and CTAs, and add variables like {{customer\_name}} or {{earning\_points}} for personalization.

**What sender options do I have?**
You can use Joy’s default domain, your own verified domain, an SMTP provider (Amazon SES, SendGrid), or integrations with Klaviyo and Omnisend.

**Can customers track their rewards through email?**
Yes. Notifications give them a permanent record of coupons and rewards, or a snapshot of their current balance, so even if they forget to copy a code from the widget, they can always find it in their inbox or trace back history.

**Why does my email land in the spam box?**

If you use a [simple customer sender](/settings/email/configure-simple-custom-sender) with SPF, maybe you have not set a DMARC record, which is required by email service providers (ESP), and it may land in spam. If you add a DMARC record (probably "none" policy one), and it still gets in the spam box, your email sender has probably been marked with a low reputation score; you may need to use a custom sending domain or SMTP to rectify the issue.

With a custom sending domain and SMTP, you are completely in control of your reputation score. If you use the custom sending domain, check your reputation score [herearrow-up-right](https://senderscore.org/).

[PreviousNotificationschevron-left](/notifications)[NextJoy notications with Shopify Flow triggerschevron-right](/notifications/joy-notications-with-shopify-flow-triggers)

Last updated 19 days ago

Was this helpful?