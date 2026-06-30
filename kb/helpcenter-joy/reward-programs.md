# Reward Programs

## Earning Programs
10 program types:
1. **Place Order**: Per amount spent, per item, per order, or at spend threshold
2. **Sign Up**: For creating account
3. **Sign Up for Newsletters**: For subscribing
4. **Birthday Reward**: Automatic on birthday
5. **Write Review**: For product reviews (integrates with review apps)
6. **Social Activity**: For shares, follows, Instagram comments
7. **Google Reviews**: For Google review submissions
8. **Fill Out a Survey**: For survey completion
9. **Visit Website**: For visiting the store
10. **Custom Program**: Flexible for custom actions

Each supports: date ranges (static/dynamic), conditional rules, reward type (points or store credit).

### Sign Up Reward — How a customer actually earns it

The Sign Up reward is **not** granted automatically the moment a Shopify customer account is created. It is awarded through one of 3 trigger paths. The customer must hit one of these paths AND pass the eligibility rules below.

**Conditions (must ALL be true):**
1. Sign Up program is **active**.
2. Customer has **not earned it before** (one-time only; protected by an atomic check against double-earn).
3. **Account created on/after the program start** — customer's `createdAt` must be ≥ the program's start date (or its created date if no start date is set).
   - ⚠️ This is why **customers who signed up before the program was turned on do NOT earn it.**
   - Override: if the shop enables **"Earn sign up for all members" (`enableEarnSignUpForAllMember`)**, the date check is skipped and all members earn it regardless of account age.
4. Not blocked by shop config: **manual member assignment** mode or **excluded segment** will skip the reward.

**The 3 trigger paths:**

| # | Path | How it fires |
|---|------|--------------|
| 1 | **Online store (widget fetch)** | Customer **logs into the Shopify store**, then loads any page with the Joy widget. The widget auto-fetches with the logged-in `customerId` → syncs/checks the customer → earns. No button click needed. **Guest (not logged in) = no `customerId` = no earn.** |
| 2 | **Widget popup "Join / Earn sign up"** | Customer opens the Joy widget popup and the join action sends `isEarnSignup=true` → queues `handleEarnSignupTask` → earns (skipped if manual-assign or opt-in guest). |
| 3 | **POS (guest → member)** | Customer buys at POS and is identified (guest converted to member) → `handleEarnSignUp`. Separate path from the storefront. |

**Important notes for CS:**
- Creating a Shopify account via webhook (`customers/create` / `customers/update`) does **NOT** earn the reward on its own (changed June 2026, ticket JOY-260605-9TSk8J). The record is synced but the customer earns later via one of the 3 paths above.
- Online store path has a built-in ~5s retry (up to 3×) to wait for the create webhook and avoid duplicate customers — so the reward may land a few seconds after the customer first appears, not instantly.

**Most common merchant complaint:** *"My customer signed up but didn't get the sign-up points."*
Usual causes: (a) customer signed up **before** the program was active → enable "Earn sign up for all members"; (b) customer **created the account but hasn't logged back in / returned to a page with the widget**; (c) shop is on **manual member assignment**; (d) customer is in an **excluded segment**.

## Redeeming Programs
3 types:
1. **Discount Program**: Fixed $ off or % off
2. **Free Gift Program**: Free product with purchase
3. **Free Shipping Program**: Free shipping coupon

Settings: minimum points required, max per redemption, coupon expiry, minimum order amount, product/collection restrictions.

## Referral Program
Customers share unique links. Both referrer and referee earn rewards when referee places order.

**Flow**: Referrer shares link → Referee claims reward (7-day cookie) → Referee orders with same email → Both earn.

**Referee rewards**: Points, store credit, % discount, or fixed discount.
**Referrer rewards**: Points, store credit (fixed or %), or discount coupons. Supports tier-based rewards by VIP status.

**Advanced (Professional+)**:
- Anti-cheat: email similarity, browser tracking, IP monitoring, purchase history verification
- Auto order tagging for tracking
- Customer tagging for referrers and new customers

## Milestone Programs (Advanced+ only)
6 types:
1. Number of orders
2. Amount spent
3. Earned points
4. Number of reviews
5. Inactivity (re-engage dormant customers)
6. Subscription milestones

Rewards: points, store credit, fixed/% discount, free shipping, free product.

## Advanced Settings
5 configuration areas:
1. **Point Expiration**: Set timeframes for when points expire
2. **Refund Points**: Manage point adjustments on returns
3. **Pending Points**: Control points awaiting fulfillment/verification
4. **Discount Combination**: Configure how rewards interact with other promos
5. **Channels for Reward Programs**: Which sales channels participate
