circle-info

This feature is available for: **Advanced and Enterprise plan**

### [hashtag](#overview) **Overview**

The Rule Engine introduces a multi-program system that allows you to create several earning programs, each with its own conditions, filters, and reward logic. Instead of adding extra checkboxes or tabs inside the default **Place order** program, you simply create new programs — each one functioning as an independent earning rule. Whenever a customer places an order, Joy evaluates all active programs and applies every program whose conditions are met.

This structure gives your loyalty program far greater flexibility. You can build dynamic earning rules that respond to real business scenarios: seasonal promotions, high-value order incentives, product-specific multipliers, weekend or after-hours bonuses, birthday-month boosters, or targeted campaigns for selected customer segments.

With multiple programs running side by side, your loyalty strategy becomes more adaptive, more precise, and significantly more effective.

### [hashtag](#how-multi-program-logic-works) **How Multi-Program Logic Works**

Every earning rule you create acts as its own program. When a customer performs an action such as placing an order, Joy evaluates all active programs and applies every program whose conditions are met.

This means:

- Customers can earn points from **multiple programs at the same time**
- Programs can be targeted to **specific customers, collections, or time frames**
- Rules do not replace each other — they **stack** unless conditions prevent overlap
- Merchants can run **always-on programs** alongside **temporary or seasonal campaigns**

This gives you complete freedom to design layered earning logic.

### [hashtag](#what-you-can-build-with-the-rule-engine) **What You Can Build With the Rule Engine**

Below are common use cases that show how flexible and powerful the Rule Engine can be when designing your loyalty experience.

#### [hashtag](#id-1.-standard-purchase-program-always-on-base-rule) **1. Standard Purchase Program (Always-On Base Rule)**

A foundational program that awards a default earning rate for every completed purchase, such as:

- Earn 1 point per $1 spent on every order

This forms your primary earning structure and runs continuously unless disabled.

#### [hashtag](#id-2.-collection-specific-bonus-programs) **2. Collection-Specific Bonus Programs**

Create extra multipliers for products or collections that you want to highlight or drive traffic toward. For example:

- Earn 2× points on the “Summer Collection”
- Earn 50 bonus points on eco-friendly tagged products
- Earn 3× points on clearance items to accelerate sell-through
- Return can at POS for recycle, bonus X point. You can place an order, create a custom sale item, add the product title condition.

These programs only activate when the order includes eligible items.

circle-info

Combine with a [product label apparrow-up-right](https://apps.shopify.com/search?q=product%20label) to make the offer noticable on the collections page.

#### [hashtag](#id-3.-high-value-order-incentive-programs) **3. High-Value Order Incentive Programs**

Encourage larger carts by rewarding customers who spend more or buy more items:

- Earn 100 bonus points on orders over $100
- Earn 3× points on orders above $300
- Earn 500 bonus points when purchasing 5+ items

By combining subtotal, item count, and multipliers, you can design targeted upsell incentives.

#### [hashtag](#id-4.-time-based-or-seasonal-campaigns) **4. Time-Based or Seasonal Campaigns**

Run temporary promotions tied to specific dates, holidays, or peak shopping hours:

- Weekend double points
- 3× points during Black Friday week
- Bonus points every weekend
- Holiday season multiplier (Dec 1–31)

Joy supports exact dates, date ranges, recurring schedules, and weekly cycles.

#### [hashtag](#id-5.-birthday-and-anniversary-enhancements) **5. Birthday & Anniversary Enhancements**

Use customer attributes to create personalized moments that feel meaningful:

- Earn 3× points during the customer’s birthday month
- Bonus points on the member’s program anniversary
- Extra points during the customer’s birthday week

These programs rely on attributes like birthday or join date synced to Joy.

#### [hashtag](#id-6.-vip-tier-exclusive-programs) **6. VIP Tier-Exclusive Programs**

Design earning rules that apply only to customers in specific VIP tiers. This lets you create a clear progression path where rewards improve as customers level up.

For example, Bronze members can earn the base rate, Silver receives a modest boost, and Gold or Platinum unlock higher multipliers or exclusive earning campaigns.

These programs activate only for customers in the targeted tier, allowing you to recognize high-value shoppers and give them a richer experience.

Tier-exclusive rules are ideal for:

- Rewarding top-tier customers with higher point multipliers
- Creating member-only bonus events for Silver/Gold
- Offering seasonal boosts exclusive to upper tiers
- Building excitement around leveling up

This makes your VIP ladder feel more intentional and motivating.

### [hashtag](#how-programs-work-together) **How Programs Work Together**

Because each rule is independent, customers can qualify for multiple programs in a single order. For example, a customer placing an order during their birthday month could simultaneously receive:

- Base earning rate
- Collection-specific bonus
- High-value order bonus
- Birthday month multiplier

This stacking behavior is intentional and provides merchants with powerful flexibility. You may limit stacking by applying narrower conditions or audience filters.

### [hashtag](#managing-programs) **Managing Programs**

You can create, edit, disable, or delete programs at any time. When a program is enabled:

- All customers who meet its conditions automatically qualify
- You do not need to migrate or adjust existing customer data
- Programs take effect immediately upon activation

To test a rule, place a test order and review the customer’s activity log.

### [hashtag](#frequently-asked-questions) **Frequently Asked Questions**

**Can I run multiple earning programs at the same time?**
Yes. The Rule Engine allows multiple earning programs to run simultaneously. Each program works with its own conditions and filters, and Joy will evaluate all active programs whenever a customer places an order.

**Do customers earn points from all programs or just one?**
Customers earn points from every program whose conditions they meet. All rewards will stack unless you configure a rule to stop further processing.

**Can programs overlap?**
Yes. Programs can overlap in both timing and conditions. If a customer qualifies for several programs, Joy will apply each one unless you narrow the audience or use priority settings.

**Can I limit programs to specific customer segments or VIP tiers?**
Yes. Any earning rule can be restricted to selected segments or specific VIP tiers, giving you full control over who receives which incentives.

**Can I schedule programs for specific times or seasons?**
Yes. You can create programs that run during exact dates, seasonal windows, weekly cycles, or recurring time ranges.

**Can I create collection-based or product-based rules?**
Yes. Programs can target individual products, collections, or product tags depending on your needs.

**Does the Rule Engine support conditions like order value or item quantity?**
Yes. You can define minimum or maximum order value, required subtotal ranges, or specific item quantities.

**Can I combine multiple conditions into a single program?**
Yes. Conditions such as date, product, customer segment, order value, and time can all be combined to build precise and highly targeted earning rules.

**Do birthday or seasonal programs stack with other programs?**
Yes. Joy will apply every qualifying program unless you intentionally restrict stacking through rule settings.

**Can I filter earning programs by order tag?**
Yes. You can filter programs based on order tags, but this works best when the reward is set to trigger on fulfillment. Orders usually do not have tags at the moment of creation or payment, so Joy may process the rule before tags are added. If tags are added later, the program will not re-evaluate.

**Can I stop Joy from processing the next earning programs once a program is applied?**

Yes. Each program includes a “Stop further rules processing” option. When enabled, Joy will skip all lower-priority programs if this rule successfully gives a reward. If no reward is granted, Joy continues evaluating the rest of the rules. This is useful when you want only one program to apply, such as tier-exclusive rewards or a special campaign that should override the base earning rate.

[PreviousRedeem at checkout pagechevron-left](/reward-programs/redeeming-programs/redeem-at-checkout-page)[NextReferralschevron-right](/reward-programs/referrals)

Last updated 19 days ago

Was this helpful?