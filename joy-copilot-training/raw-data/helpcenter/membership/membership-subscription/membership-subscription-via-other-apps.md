circle-info

This feature is available for merchants on **Joy Advanced** plans and above who have exclusive tiers configured in their loyalty program.

### [hashtag](#introduction) Introduction

Subscription membership automatically assigns customers to exclusive tiers when they purchase membership subscriptions. Instead of earning VIP tier status through spending, customers can pay for instant access to exclusive benefits throughout their subscription period.

### [hashtag](#our-approach) Our approach

To us, the membership is treated as a kind of VIP tier program, which also comes with perks, entry rewards, membership card display like what we have already built with VIP tiers. So, with flexibility at heart, we want to craft a solution that fits seamlessly with the existing Shopify ecosystem. That is why our tech stack utilizes the Shopify Flow, along with any Shopify-friendly subscription apps (which use the [Shopify selling plans APIarrow-up-right](https://shopify.dev/docs/api/admin-graphql/latest/objects/sellingplan)).

circle-info

See our existing guide on the [Exclusive tier featurearrow-up-right](https://help.joy.so/membership/exclusive-tier)

### [hashtag](#why-you-should-use-subscription-membership) Why you should use subscription membership

Subscription membership creates a **consistent touchpoint that keeps customers actively engaged** with your brand month after month. Rather than waiting for customers to make their next purchase, you're providing ongoing value that gives them regular reasons to return, interact, and stay connected with your business.

The predictable monthly recurring revenue is a valuable byproduct, but the real power lies in transforming occasional buyers into consistently engaged community members. Unlike spending-based tiers where customers might lose benefits during natural purchase lulls, subscription members maintain their connection to your brand regardless of their buying cycles. This sustained engagement means they're more likely to think of you first when they are ready to purchase, recommend you to others, and develop genuine loyalty that goes beyond individual transactions.

This approach turns customer retention from a reactive challenge into a proactive relationship-building strategy, where the subscription itself becomes a bridge that keeps customers connected between purchases.

### [hashtag](#setting-up-subscription-membership) Setting up subscription membership

Here is the video guide for hands-on guidance if you want a more interactive experience:

#### [hashtag](#step-1-create-exclusive-tiers) Step 1: Create exclusive tiers

1. In Joy admin, go to **Membership** > **New tier**
2. Check the **"Exclusive tier (Manual only)"** checkbox
3. Set up tier perks like percentage discounts, free shipping, bonus points multipliers, and entry rewards
4. Click **Save**

circle-info

You can have many exclusive tiers just for a subscription-membership-only program. We are giving a demo for the hydbrid option.

#### [hashtag](#step-2-install-a-subscription-app) Step 2: Install a subscription app

Install Shopify Subscriptions, Joy Subscriptions, or any app that supports [Shopify selling plansarrow-up-right](https://shopify.dev/docs/api/admin-graphql/latest/objects/sellingplan).

#### [hashtag](#step-3-create-membership-products) Step 3: Create membership products

Set up products with subscription selling plans (monthly/yearly) and add subscription selling plans to these products through your subscription app to enable recurring billing.

#### [hashtag](#step-4-configure-shopify-flow-workflows) Step 4: Configure Shopify Flow workflows

Create 2 workflows that assign/unassign exclusive tiers when subscription contracts are created, updated, paused, or cancelled. Shopify Flow handles the automation and communicates tier changes to Joy.

You can simply go to **Shopify Flow templates**, search for the keyword **"Joy"** and the below templates will be shown:

1. [**Assign VIP tier when subscription membership is purchased**arrow-up-right](https://shopify.com/admin/apps/flow/editor/templates/0198ce00-b062-76ad-9830-959c8c8f0867)
2. [**Manage VIP tier on subscription membership status changes**arrow-up-right](https://shopify.com/admin/apps/flow/editor/templates/0198ce00-b062-76ad-9830-959c8c8f0867)

👉 Click on the template you want to use, then:

- **Install** the template
- **Configure** the workflow:

  - Enter the correct **Variant ID** of your subscription product
  - (For status change workflow) Set the correct **subscription status** conditions: *ACTIVE*, *PAUSED*, *CANCELLED*
- **Save** the workflow, and you’re done! From now on, the workflow will automatically assign or unassign customers based on your settings.”

### [hashtag](#example-setup) Example setup

**Luxury skincare brand with seasonal launches:**

**Premium Partner Membership ($29/month):**

- Creates "Premium Partner" subscription product
- Assigns customers to the "Premium Partner" exclusive tier when they purchase $200+ on premium skincare products 3-4 times
- Unassigns the tier when the subscription is cancelled/paused
- Benefits: 20% discount, free shipping, exclusive product access

**Why this works**: Customers spending $200+ on premium skincare products 3-4 times per year get better value through membership ($348/year) than waiting to earn VIP status through spending thresholds, while the brand gets predictable revenue and deeper customer commitment.

### [hashtag](#frequently-asked-questions) Frequently asked questions

**What happens when a subscription expires?**

Customers are manually removed from their exclusive tier via Shopify Flow automation and no longer receive exclusive tier benefits.

**Where can customer manage their membership?**

Each subscription app comes with a subscription portal. Customer can manage their membership package in the same place.

**Can customers have both VIP tiers and exclusive tiers?**

No, exclusive tiers take priority. When customers have an active subscription membership, they only receive benefits from their exclusive tier, not from any VIP tier they might have earned through spending.

**Do subscription members still earn points?**

Yes, they earn points according to regular rules plus any tier bonus multipliers from their exclusive tier.

**Can I offer different subscription periods?**

Yes, subscription periods depend on your subscription app settings. Most apps support monthly, quarterly, or yearly billing cycles.

**When being unassigned from the exclusive tier, what tier will the customer become?**

That customer will be recalculated based on your current VIP tier setting, whether it is points or amount spent.

[PreviousMembership subscription (via Joy Subscription)chevron-left](/membership/membership-subscription/membership-subscription-via-joy-subscription)[NextPartner Tiers (B2B)chevron-right](/membership/partner-tiers-b2b)

Last updated 19 days ago

Was this helpful?