circle-info

This feature is available for merchants on **Joy Advanced** plans and above who have exclusive tiers configured in their loyalty program.

Previously, creating a paid membership program required complex setups using Shopify Flow. Now, with the deep integration between **Joy: Loyalty Program** and **Joy: Subscription App**, you can build a seamless "Subscribe for exclusive Benefits" program directly within the app.

This guide walks you through the complete setup: from creating the Exclusive tier to displaying the subscription widget on your store.

### [hashtag](#how-to-set-up) How to set up

#### [hashtag](#step-1-create-an-exclusive-tier) Step 1: Create an Exclusive Tier

1. In Joy admin, go to **Membership** > **New tier**
2. Check the **"Exclusive tier (Manual only)"** checkbox
3. Set up tier perks like percentage discounts, free shipping, bonus points multipliers, and entry rewards
4. Click **Save**

*Note: Exclusive tiers are not achievable by earning points; customers can only enter via specific actions like purchasing a subscription, manually assigned, shopify flow...*

#### [hashtag](#step-2-access-subscription-membership-and-connect-apps) Step 2: Access Subscription Membership & Connect Apps

1. Navigate to **Membership** > **Subscription membership**.
2. You will see an integration banner. Click **Connect now**

*Note: If you've not installed Joy subscription, please install it first before click "Connect now"*

> **🎁 Great News:** If you are on the **Joy Loyalty Advanced plan**, connecting the apps will automatically upgrade your Joy Subscription account to the **Advanced plan for FREE** (no double charge).

#### [hashtag](#step-3-create-a-membership-plan) Step 3: Create a Membership Plan

Now, define which product triggers the exclusive tier status.

1. Click **Add subscription plan**.
2. **Select Product:** Search for and select the product you want to sell as a membership (e.g., "The Collection Snowboard").

1. **Configure Plan Settings:**

   - **Assign to exclusive tier:** Select the Tier created in Step 1.
   - **Billing Frequency:** Set how often the customer pays (e.g., "Every 1 Month").
   - **Payment Type:** Choose between "Pay as you go" or "Prepaid".
   - ...

1. Click **Save**. *(Result: The plan is created in Joy Loyalty and automatically synced to Joy Subscription).*

#### [hashtag](#step-4-enable-joy-subscription-and-add-widget-crucial-step) Step 4: Enable Joy Subscription & Add Widget (Crucial Step)

For customers to buy this plan, you must display the subscription option on your storefront.

1. Go to **Joy Subscription app, you will see a warning banner, click "Activate"**

1. Hit **"Save"** to activate the app

1. **Add Widget:**

- In Joy subscription, click menu **"Widget"**
- Click **"Add widget"** and hit **"Save"**

### [hashtag](#how-it-works-the-customer-experience) How it Works: The Customer Experience

Once you have completed the steps above, here is exactly what happens on your live store:

1. **Customer Subscribes:** A customer visits your product page. Thanks to the widget (Step 4), they see the subscription option. They select the plan and complete the checkout.
2. **Automatic Tier Assignment:** Immediately after the order is placed, Joy Loyalty detects the subscription purchase. The system **automatically assigns the customer to the Exclusive Tier** you selected.
3. **Instant Perks:** The customer instantly unlocks all benefits associated with that tier (e.g., **2x Point Earning**, **Free Shipping**, **Special Discounts**) without you lifting a finger.
4. **Subscription Management:**

   - **Updates:** Any changes to the plan in Joy Loyalty will sync to Joy Subscription.
   - **Cancellation:** If the customer cancels their subscription or a payment fails, Joy Loyalty will automatically **remove** them from the Exclusive Tier, and they will lose their perks.

### [hashtag](#frequently-asked-questions) Frequently Asked Questions

**Q: Do I still need Shopify Flow for this?** A: No. This direct integration handles the assignment and removal of tiers automatically. You only need Shopify Flow if you are using a *third-party* subscription app (not Joy Subscription).

**Q: Can I edit the subscription settings later?** A: Yes. You can edit the plan details in Joy Loyalty, or for more advanced subscription management (like email notifications or dunning management), you can edit the settings inside the Joy Subscription app.

[PreviousMembership subscriptionchevron-left](/membership/membership-subscription)[NextMembership subscription (via other apps)chevron-right](/membership/membership-subscription/membership-subscription-via-other-apps)

Last updated 19 days ago

Was this helpful?