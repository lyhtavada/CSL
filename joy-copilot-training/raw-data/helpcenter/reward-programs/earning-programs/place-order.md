circle-info

This feature is available in **All** plans

### [hashtag](#user-content-what-is-place-order-feature) What is "Place order" feature?

**Place Order** is a core component of Joy Loyalty that allows you to reward customers for their purchases. It automatically assigns **points** or **store credit** to customers when they complete an order on your store, based on rules you define.

### [hashtag](#user-content-why-do-you-need-this-feature) Why do you need this feature?

Place Order Rewards are a key component of your loyalty program, rewarding customers every time they make a purchase. This not only incentivizes repeat purchases but also helps build long-term loyalty by offering something extra each time a customer places an order.

### [hashtag](#user-content-how-to-set-up-this-feature-on-your-store) How to set up this feature on your store

#### [hashtag](#user-content-access-place-order) Access Place order

1. Click on **Reward programs**
2. Go to **Earning programs** and you can access the list of programs here

#### [hashtag](#user-content-program-information) Program information

- **Program name:** Enter a descriptive name
- **Description:** Define your reward formula using the format
- **Date range:**

  - **Static date:** Fixed start and end dates
  - **Dynamic date:** Enable earning rewards in 2 options:

    - The month of birth of customers, or
    - Specific date each month
  - Day of the week (Mon, Tue, Wed,...)

#### [hashtag](#user-content-reward-settings) Reward settings

**Reward type**

Choose what type of reward customers will earn:

Reward type

Description

**Points**

Customers earn loyalty points that can be redeemed for discounts

**Store credit**

Customers earn store credit (cash value) that can be applied directly at checkout

> **Note:** To use Store Credit, you must first grant Store Credit access permissions. Go to **Settings → Store Credit** and click **Grant Store Credit Access**.

**Rewarding method**

Choose how rewards are calculated:

Method

Description

Example

**Give X points/credits for every Y amount spent**

Rewards based on order total

1 point per $1 spent

**Give X points/credits once when spending reaches Y**

One-time reward at threshold

100 points when order ≥ $50

**Give X points/credits for every Y items purchased**

Rewards per item quantity

5 points per item

**Give X points/credits for each order**

Fixed reward per order

10 points per order

**Rewarding amount**

Enter the reward value:

- **If Points:** Enter number of points (e.g., `1` points)
- **If Store Credit:** Enter credit amount in your currency (e.g., `1` credits)

---

- **Apply for:** Choose the members that can earn rewards in the program
- **Rewarding method:** Choose the way customers can earn rewards
- **Check if:** Set up and select condition type for your program
- **Reward availability:** Choose how conditions apply

  - **All conditions are met:** Customer must satisfy every condition
  - **Any conditions are met:** Customer must satisfy at least one condition
- Set specific criteria for:

  - **Customer:** Target based on customer attributes
  - **Order:** Apply rules based on order details
  - **Product:** Set conditions for specific products
  - **Collection:** Apply rules to product collections

> Make sure to use the correct logic to ensure that your conditions work as intended

#### [hashtag](#user-content-rewarding-conditions) Rewarding conditions

- **Rounding and priority:** Choose rounding method
- **Reward for additional fee:** Include shipping/taxes in calculation (optional)

#### [hashtag](#user-content-fraud-prevention) Fraud prevention

Protect your program by Fraud prevention setup:

1. Click **Turn on**
2. **Maximum Earning By This Rule:** Set max rewards customers can earn from this rule
3. **Set earning limit:** Limit how often rewards can be earned
4. **Automatically revoke for cancelled/refunded orders:** Points or store credit will be revoked if order is cancelled/refunded

#### [hashtag](#user-content-save) Save

Click **Save** to apply your changes.

---

### [hashtag](#user-content-customer-experience) Customer Experience

#### [hashtag](#user-content-with-points) With Points

When a customer places an order, they will see their earned points in:

- Joy Widget
- Loyalty Page in their account
- Account page
- Order confirmation email (if notifications enabled)
- ...

#### [hashtag](#user-content-with-store-credit) With Store Credit

When a customer places an order and earns store credit:

1. Store credit is automatically added to their account
2. Store credit can be applied at checkout on their next purchase

---

### [hashtag](#user-content-faqs) FAQs

**What currency do you use to calculate the rewards?**

We work with the store's main currency which works in your Shopify admin. All rewards will be converted to the main currency and then the reward rate will be implemented to this total amount.

**Are shipping and taxes included in the calculation of rewards?**

If you choose the reward customer on the amount they spent, then: no, they are not. We will only add up the total price of the products matching the conditions (you can whitelist some of the products out of the program) in the order.

**How can I exclude orders from other platforms in my loyalty program?**

You can use the "Check if" conditions to exclude orders coming from non-Shopify sources. In your loyalty program settings:

1. Go to the **Check if** section
2. Select **Order**
3. Choose **Exclude orders by tags**
4. Add the tag that identifies non-Shopify orders or the platform you don't want to add rewards (e.g., "external-platform")

**Do I need to tag my external orders?**

Yes. You'll need to ensure all orders from external platforms are consistently tagged in your Shopify admin.

**What's the difference between Points and Store Credit?**

Aspect

Points

Store Credit

**Value**

Abstract units, redeemed for discounts

Real currency value ($)

**Redemption**

Must be converted to discount

Applied directly at checkout

**Best for**

Long-term loyalty building

Short-term retention, cashback programs

**Can I switch from Points to Store Credit mid-campaign?**

Yes, but existing earned rewards will remain in their original type. Only new orders will earn the updated reward type.

**Do I need special permissions for Store Credit?**

Yes. Store Credit requires additional Shopify permissions. Go to **Settings → Store Credit** and click **Grant Store Credit Access** before using this reward type.

[PreviousEarning programschevron-left](/reward-programs/earning-programs)[NextPlace subscriptionchevron-right](/reward-programs/earning-programs/place-subscription)

Last updated 19 days ago

Was this helpful?