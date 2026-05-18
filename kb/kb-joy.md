# Joy Loyalty — Knowledge Base

> Betty's internal reference for understanding Joy's features, plans, and limitations.

---

## What Joy Does

Joy Loyalty is a Shopify loyalty program app. It helps merchants:
- Reward customers with points or store credit for purchases and activities
- Create VIP tier memberships with exclusive perks
- Run referral programs to grow their customer base
- Manage loyalty across online store and Shopify POS (in-store)

---

## Plans

| | Free | Professional | Advanced | Enterprise |
|---|---|---|---|---|
| Earning & redeeming | ✓ | ✓ | ✓ | ✓ |
| Referrals (basic) | ✓ | ✓ | ✓ | ✓ |
| Referrals (advanced + anti-cheat) | ✗ | ✓ | ✓ | ✓ |
| Analytics | ✓ | ✓ | ✓ | ✓ |
| Migration from other apps | ✗ | ✓ | ✓ | ✓ |
| VIP Tiers | ✗ | ✗ | ✓ | ✓ |
| POS integration | ✗ | ✗ | ✓ | ✓ |
| Multi-language (auto-detect) | ✗ | ✗ | ✓ | ✓ |

---

## Core Features

### 1. Earning Programs
How customers accumulate points or store credit:
- **Place Order**: Per amount spent, per item, per order, or at spend threshold
- **Sign Up / Newsletter**: For account creation or newsletter subscribe
- **Birthday Reward**: Automatic on customer birthday
- **Write Review**: For product reviews (integrates with review apps)
- **Social Activity**: For social shares, follows, Instagram comments
- **Referral**: When referring new customers
- **Visit Website**: For visiting the store
- **Custom / Submit Form / Submit Receipt**: Flexible for custom actions
- **Streak Bonus / Anniversary / Milestone**: Engagement-based rewards

Each program supports: date ranges, conditional rules, reward type (points or store credit), plan-based availability.

### 2. Redeeming Programs
How customers convert points into rewards:
- **Discount Amount**: Fixed $ off (e.g., 100 pts = $10 off)
- **Discount Percentage**: % off (e.g., 200 pts = 15% off)
- **Free Shipping**: Free shipping coupon
- **Free Gift**: Free product with purchase
- **Buy X Get Y**: Promotional offer

Settings: minimum points, max per redemption, coupon expiry, minimum order amount, product/collection restrictions.

### 3. Referral Program
Customers share a unique link. Both referrer and referee earn rewards when referee places an order.

Flow: Referrer shares link → Referee claims reward (7-day cookie) → Referee orders with same email → Both earn rewards.

Advanced (Professional+): anti-cheat (email, browser, IP detection), Shopify customer/order tagging.

### 4. VIP Tiers (Advanced+ only)
Tier-based membership with automatic progression.

Calculation methods: points earned, amount spent, or number of orders.

Per tier:
- **Entry Reward**: One-time reward when reaching the tier (discount, bonus points, free product)
- **Tier Privilege (Perk)**: Ongoing benefit on all future orders while in tier (auto-discount, free shipping, bonus points)
- **Tier Assessment**: Auto upgrade/downgrade based on rules

Important: Shopify allows max 25 automatic discounts across all tiers combined.

### 5. On-Site Content
Loyalty touchpoints on storefront:
- **Loyalty Widget**: Floating widget — points balance, available rewards
- **Loyalty Landing Page**: Full page — hero, how it works, earn/redeem, VIP benefits, FAQs, referral, activity
- **Account Page**: Loyalty dashboard, redemption, referral management, wallet pass
- **Product Page**: Point calculator, product referral
- **Cart Drawer**: Redeem points in cart
- **Checkout Page**: Quick redeem, available rewards, all discounts, referral block
- **Thank You Page**: Sign-up, referral, reward celebration

### 6. POS Integration (Advanced+ only)
In-store loyalty via Shopify POS:
- Customers earn points automatically on POS orders
- Cashiers can redeem points at checkout
- Apple Wallet loyalty pass supported
- Important: Cart must have customer assigned before redeeming. Always search for existing customer first to avoid duplicates.

### 7. Notifications
- Automated emails for loyalty events (points earned, tier change, birthday, etc.)
- Shopify Flow triggers for custom workflows
- Custom email sender domain

### 8. Customer Management
- Import customers via CSV
- Manage customer types and segments
- Generate QR codes and Apple Wallet passes
- Exclude specific customers or B2B customers from program
- Manual point adjustments
- Birthday collection via registration form

### 9. Migration (Professional+ only)
Migrate from: Smile, Rivo, Yotpo, Stamped, Appstle, LoyaltyLion, BON Loyalty.

Migrated data: customer name, email, points balance, VIP tier, birthday, status.

### 10. Integrations
- **Email/SMS**: Klaviyo, Omnisend, Mailchimp, Sendlane, Drip, PushOwl
- **Reviews**: Klaviyo Reviews, Judge.me, Yotpo, Fera, Air Reviews, Review Rocket
- **Chat**: Chatty, Gorgias — show loyalty data in support conversations
- **Subscriptions**: Joy Subscription, Shopify Subscription, Recharge
- **Shopify Flow**: Custom automations (Loox, Okendo, Stamped, Zigpoll, Growave, etc.)

---

## Key Terms

| Term | Meaning |
|---|---|
| Points | Virtual currency earned through activities, redeemable for rewards |
| Store Credit | Cash-value credits applied directly at checkout |
| Earning Program | Rules for how customers accumulate points |
| Redeeming Program | Rules for how customers convert points to discounts |
| Referrer | Existing customer who shares a referral link |
| Referee | New customer who uses a referral link |
| VIP Tier | Membership level with exclusive benefits |
| Entry Reward | One-time reward when reaching a new tier |
| Tier Privilege / Perk | Ongoing benefit while in a tier |
| Loyalty Widget | Floating on-site widget showing loyalty info |
| Sandbox Mode | Test mode for reward programs |
| Pending Points | Points awaiting order fulfillment/payment confirmation |
| Point Expiration | Auto-expiry of unused points after set period |

---

## Common Issues & What to Know

| Issue | Root cause / What to check |
|---|---|
| Points not earned after order | Earning program off, customer not a member, order doesn't meet conditions (min spend, products), or pending points setting |
| Discount not applying | Redeeming program off, insufficient points, coupon expired, or discount combination rules |
| Widget not showing | App not enabled, app embeds off in Shopify theme editor, or excluded on that page |
| Referral not working | Referee must use same email for claiming + ordering; App Pixel must be enabled in Shopify Settings > Customer Events; 7-day cookie may have expired |
| VIP tier not updating | Check tier assessment schedule, calculation method, and whether customer meets threshold |
| POS not loading | App installed on POS device? Cart has customer + products? Customer is a loyalty member? |
| Integration sync issues | API connection active? Triggers enabled in Joy settings? Check API rate limits (Klaviyo with 100k+ customers especially) |
