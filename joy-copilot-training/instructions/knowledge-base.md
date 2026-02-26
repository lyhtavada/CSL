# Joy Loyalty — Knowledge Base

## Product Overview

Joy Loyalty is a Shopify app that helps merchants create and manage customer loyalty programs. It supports points-based rewards, VIP tier memberships, referral programs, and integrations with popular Shopify ecosystem tools. Joy works on both online stores and Shopify POS for in-store experiences.

## Plans

| Feature | Free | Professional | Advanced | Enterprise |
|---------|------|-------------|----------|-----------|
| Earning & redeeming programs | Yes | Yes | Yes | Yes |
| Referrals (basic) | Yes | Yes | Yes | Yes |
| Referrals (advanced + anti-cheat) | No | Yes | Yes | Yes |
| Analytics | Yes | Yes | Yes | Yes |
| Migration from other apps | No | Yes | Yes | Yes |
| VIP Tiers | No | No | Yes | Yes |
| POS integration | No | No | Yes | Yes |
| Multi-language (Detect Language) | No | No | Yes | Yes |

## Core Features

### Earning Programs
Merchants define how customers earn points or store credit. Types:
- **Place Order**: Earn per amount spent, per item, per order, or at spend threshold.
- **Sign Up / Newsletter**: Earn for creating account or subscribing.
- **Birthday Reward**: Automatic reward on customer's birthday.
- **Write Review**: Earn for product reviews (integrates with review apps).
- **Social Activity**: Earn for social shares, follows, Instagram comments.
- **Google Reviews**: Earn for Google review submissions.
- **Referral**: Earn when referring new customers.
- **Visit Website**: Earn for visiting the store.
- **Custom Program / Submit Form / Submit Receipt**: Flexible earning for custom actions.
- **Streak Bonus Challenge / Member Anniversary / Milestone**: Engagement-based rewards.

Each program supports: date ranges (static/dynamic), conditional rules, reward type (points or store credit), and plan-based availability.

### Redeeming Programs
Customers convert points into rewards:
- **Discount Amount**: Fixed dollar discount (e.g., 100 points = $10 off).
- **Discount Percentage**: Percentage discount (e.g., 200 points = 15% off).
- **Free Shipping**: Free shipping coupon.
- **Free Gift**: Free product with purchase.
- **Buy X Get Y**: Promotional offer.

Settings include: minimum points required, max points per redemption, coupon expiration, minimum order amount, and applicable product/collection restrictions.

### Referral Program
Customers share unique referral links. When a new customer (referee) makes a purchase, both referrer and referee earn rewards. The referral flow:
1. Referrer shares link → 2. Referee claims reward (7-day cookie) → 3. Referee places order with same email → 4. Both earn rewards.

Advanced features (Professional+): anti-cheat (email, browser, IP detection), Shopify customer/order tagging.

### VIP Tiers (Advanced+ plans)
Tier-based membership with automatic progression. Calculation methods: points earned, amount spent, or number of orders.

Components per tier:
- **Entry Rewards**: One-time reward when reaching a tier (discount, bonus points, free product, etc.).
- **Tier Privileges (Perks)**: Ongoing benefits applied to all future orders (auto-discount, free shipping, bonus points).
- **Tier Assessment**: Automatic tier upgrades/downgrades based on rules.

Important: Tier Privileges apply to all orders while in the tier. Entry Rewards are one-time use only. Shopify allows max 25 automatic discounts across all tiers.

### Integrations
- **Email Marketing & SMS**: Klaviyo, Omnisend, Mailchimp, Sendlane, Drip, PushOwl. Sync customer data (points, tier, referral URL) and trigger automations on loyalty events.
- **Product Reviews**: Klaviyo Reviews, Judge.me, Yotpo, Fera, Air Reviews, Review Rocket. Reward customers for writing reviews.
- **Chat Apps**: Chatty, Gorgias. Show loyalty data in support conversations.
- **Subscription**: Joy Subscription, Shopify Subscription, Recharge. Earn points on subscription orders.
- **Shopify Flow**: Trigger-based automations (e.g., earn points from Loox, Okendo, Stamped, Zigpoll, Growave, etc.).
- **Theme Integration**: Works with Shopify Online Store 2.0 themes.

### On-Site Content
Customizable loyalty touchpoints on the storefront:
- **Loyalty Widget**: Floating widget showing points balance, available rewards.
- **Loyalty Landing Page**: Full page with sections — hero banner, how it works, ways to earn/redeem, VIP benefits, FAQs, referral, rewards activity.
- **Account Page**: Loyalty dashboard, rewards redemption, referral management, wallet pass.
- **Product Page**: Point calculator, product referral.
- **Cart Drawer**: Redeem points in cart.
- **Checkout Page**: Quick redeem, available rewards, all discounts, referral block.
- **Thank You Page**: Sign-up block, referral block, reward celebration.

### POS (Advanced+ plans)
Joy integrates with Shopify POS for in-store loyalty:
- Customers earn points automatically on POS orders.
- Cashiers can redeem points at POS checkout.
- Supports Apple Wallet loyalty pass.
- Important: Cart must have customer assigned before redeeming. Always search for existing customer first to avoid duplicates.

### Notifications
- Automated email notifications for loyalty events (points earned, tier change, birthday, etc.).
- Shopify Flow triggers for custom automation workflows.
- Custom email sender domain support.

### Customer Management
- Import customer data (CSV).
- Manage customer types and segments.
- Generate customer QR codes and Apple Wallet passes.
- Exclude specific customers or B2B customers from the program.
- Manual point adjustments.
- Birthday collection via registration form.

### Migration (Professional+ plans)
Migrate from: Smile, Rivo, Yotpo, Stamped, Appstle, LoyaltyLion, BON Loyalty.
Migrated data: customer name, email, points balance, VIP tier, birthday, status.

### Settings
- **General**: Enable/disable app, point label customization, point exchange rate, discount code prefix, customer behavior settings.
- **Color**: Widget and loyalty page color customization.
- **Email**: Custom sender email, sending domain verification.
- **Order**: Display awaiting points, lock earning conditions at order creation, auto-tagging.
- **Languages**: Multi-language support with auto-detection (Advanced+).
- **Developers**: Hydrogen widget integration, magic tags, deep links, API.

## Key Terminology

| Term | Meaning |
|------|---------|
| Points | Virtual currency earned through activities, redeemable for rewards |
| Store Credit | Cash value credits applied directly at checkout |
| Earning Program | Rules for how customers accumulate points |
| Redeeming Program | Rules for how customers convert points to discounts |
| Referrer | Existing customer who shares a referral link |
| Referee | New customer who uses a referral link |
| VIP Tier | Membership level with exclusive benefits |
| Entry Reward | One-time reward when reaching a new tier |
| Tier Privilege (Perk) | Ongoing benefit while in a tier |
| Loyalty Widget | Floating on-site widget showing loyalty info |
| Sandbox Mode | Test mode for reward programs |
| Pending Points | Points awaiting order fulfillment/payment confirmation |
| Point Expiration | Automatic expiry of unused points after set period |

## Common Issues

- **Points not earned after order**: Check if earning program is active, customer is a member, order meets conditions (minimum spend, applicable products), and pending points settings.
- **Discount not applying at checkout**: Verify redeeming program is active, customer has enough points, coupon hasn't expired, and discount combination settings.
- **Widget not showing**: Check if app is enabled, theme integration is complete (app embeds turned on in Shopify theme editor), and widget isn't excluded on that page.
- **Referral not working**: Ensure referee uses same email for claiming and ordering, App Pixel is enabled in Shopify Settings > Customer Events, and 7-day cookie hasn't expired.
- **VIP tier not updating**: Check tier assessment schedule, calculation method, and whether customer meets threshold requirements.
- **POS not loading**: Verify app is installed on POS device, cart has customer and products added, and customer is a loyalty member for redemption.
- **Integration sync issues**: Confirm API connection is active, triggers are enabled in Joy settings, and check for API rate limits (especially Klaviyo with 100k+ customers).
