circle-info

This feature is available in **All** plans

### [hashtag](#what-is-the-recharge-integration) What is the [Rechargearrow-up-right](https://getrecharge.com/) Integration

The Recharge Integration provides two key functionalities for subscription-based stores:

1. **Discount Code Synchronization**: Automatically syncs Joy Loyalty discount codes to Recharge, allowing customers to apply loyalty discounts to their subscription orders through the Recharge customer portal.
2. **Subscription Rewards**: Allows merchants to reward customers with loyalty points for subscription purchases and renewals, encouraging long-term subscription retention.

This integration ensures that customers receive loyalty rewards for their recurring subscription orders and can use their earned loyalty discounts on both one-time purchases and subscription orders seamlessly.

### [hashtag](#why-do-you-need-this-feature) Why do you need this feature?

The Recharge Integration creates a unified loyalty experience for your subscription customers, offering both rewards for subscription purchases and the ability to use loyalty discounts on recurring orders. Without this integration, subscription customers would be disconnected from your loyalty program benefits, missing out on earning and redeeming rewards for their most valuable purchases.

Enabling this integration creates a complete loyalty ecosystem where subscription customers can earn points for their recurring orders and apply their earned discounts seamlessly through the Recharge customer portal. This comprehensive approach significantly increases customer lifetime value, as subscription customers typically represent your most loyal segment and highest revenue potential.

### [hashtag](#how-the-integration-works) How the integration works

#### [hashtag](#discount-code-synchronization) Discount code synchronization

When a customer redeems loyalty points for a discount code:

1. **Discount Creation**: Joy creates the discount code as usual
2. **Sync to Recharge**: The system automatically syncs applicable discounts to Recharge
3. **Customer Access**: Customers can apply the discount in the Recharge customer portal
4. **Automatic Management**: The system manages discount lifecycle (activation, deactivation, deletion)

#### [hashtag](#subscription-rewards) Subscription rewards

When customers place subscription orders:

1. **Order Processing**: Recharge processes the subscription order
2. **Point Calculation**: Joy calculates loyalty points based on your configured rules
3. **Point Award**: Points are automatically added to the customer's loyalty account
4. **Notification**: Customers can be notified of their earned points (if email notifications are enabled)

### [hashtag](#how-to-integrate-recharge-subscriptions-with-joy-loyalty) How to integrate Recharge Subscriptions with Joy Loyalty

1

Go to "**Integrations**", and select "**Recharge Subscription**"

2

Click on "**Install Recharge Subscription**"

3

Install **Recharge Subscription app**

4

**Paste your API key** to connect with Recharge Subscription

5

Click "**Set up**" to reward points for customers purchasing subscription-based products

Set up the Subscription order to give rewards for customers who place an order

### [hashtag](#where-to-find-your-api-key) Where to find your API Key?

1

Go to **Recharge**, click on **Tools & Apps**, then choose **API tokens**

2

Click "**Create an API token**"

3

Name the API token and add your contact email

4

Choose the permission scopes to grant this token, including:

**Orders:**

- write\_orders
- read\_orders

**Subscription**

- write\_subscriptions
- read\_subscriptions

5

Click "**Save**"

6

Click on the new program to set up more permissions. Then click **"Save"**

7

**Copy the API key** then **paste it** in the API key of Recharge and Joy Loyalty Program integration to connect

### [hashtag](#setting-up-recharge-specific-coupons) Setting up Recharge-specific coupons

1

**Access coupon creation**

- From your Shopify admin, go to **Apps**
- Click on **Joy Loyalty**
- Navigate to **Reward Programs** → **Redeeming Programs**
- Click **Create New Coupon**
- Select your desired Recharge coupon type

2

**Configure basic coupon settings**

- **Coupon Name**: Give your coupon a descriptive name
- **Point Cost**: Set how many loyalty points customers need to redeem
- **Discount Value**: Enter the amount or percentage
- **Expiration**: Set when the coupon expires (optional)

### [hashtag](#best-practices-for-recharge-integration) Best practices for Recharge Integration

#### [hashtag](#setting-up-subscription-friendly-rewards) Setting up subscription-friendly rewards

- Configure loyalty rewards that work well with recurring orders
- Consider offering percentage discounts for variable subscription values
- Set up tier benefits that apply automatically to subscription orders

#### [hashtag](#managing-customer-expectations) Managing customer expectations

- Clearly communicate that loyalty discounts work on subscriptions
- Include subscription benefits in your loyalty program description
- Send notifications when discounts are applied to subscription orders

#### [hashtag](#monitoring-integration-performance) Monitoring integration performance

- Regularly check that discounts are syncing properly
- Monitor customer usage of loyalty discounts on subscription orders
- Track the impact on subscription retention and loyalty engagement

### [hashtag](#faqs) FAQs

#### [hashtag](#do-all-joy-loyalty-discounts-sync-to-recharge) Do all Joy loyalty discounts sync to Recharge?

No, only discounts configured for subscription use or both one-time and subscription use will sync to Recharge. One-time only discounts remain in Shopify only. The integration automatically identifies and syncs only subscription-applicable discounts.

#### [hashtag](#can-customers-earn-loyalty-points-for-subscription-orders) Can customers earn loyalty points for subscription orders?

Yes, when you configure subscription rewards in the integration settings, customers will automatically earn loyalty points for their subscription orders and renewals based on the rules you set up.

#### [hashtag](#how-do-i-get-my-recharge-api-key) How do I get my Recharge API key?

Go to your Recharge admin dashboard, navigate to Tools & Apps → API tokens, create a new token with appropriate permissions, and copy the generated API key to paste into Joy Loyalty's integration settings.

#### [hashtag](#can-customers-stack-loyalty-discounts-with-other-recharge-discounts) Can customers stack loyalty discounts with other Recharge discounts?

This depends on your Shopify discount stacking settings and Recharge configuration. Generally, only one discount per order type will be applied, with the system choosing the best available discount for the customer.

#### [hashtag](#what-happens-to-discounts-when-a-subscription-is-cancelled) What happens to discounts when a subscription is cancelled?

When a subscription is cancelled, any unused loyalty discounts associated with that subscription remain available for the customer's account but cannot be applied to the cancelled subscription.

#### [hashtag](#how-quickly-do-discounts-sync-to-recharge) How quickly do discounts sync to Recharge?

Discounts typically sync within a few minutes of creation in Joy Loyalty. However, it may take up to 10 minutes during high-traffic periods.

[PreviousJoy and Shopify Subscriptionchevron-left](/integrations/subscription/shopify-subscription)[NextInventory managementchevron-right](/integrations/inventory-management)

Last updated 19 days ago

Was this helpful?