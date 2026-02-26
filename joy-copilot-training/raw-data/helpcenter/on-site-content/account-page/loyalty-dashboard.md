circle-info

This feature is available in **Advanced, Enterprise plans**

### [hashtag](#what-is-a-loyalty-dashboard) **What is a Loyalty Dashboard?**

A Loyalty Dashboard is a centralized section on a customer's account page that displays their complete loyalty program status. It shows their current points balance, tier level, available rewards, earning history, and progress toward the next tier or reward. This dashboard serves as the customer's personal command center for all loyalty-related information.

### [hashtag](#why-do-you-need-this-feature) Why do you need this feature?

The enhanced dashboard with discount values transforms how customers perceive and interact with your loyalty program. By showing specific discount amounts (like "50% off" or "$20 off") instead of just program descriptions, customers can immediately understand the real monetary value of their rewards.

This transparency increases program engagement by helping customers make strategic decisions about when and how to redeem their points. When customers see concrete savings opportunities, they're more motivated to participate actively in your loyalty program and make additional purchases to reach higher-value rewards.

### [hashtag](#loyalty-dashboard-display-rules) Loyalty dashboard display rules

#### [hashtag](#block-settings-progress) Block settings/Progress

For the "Progress" field in the Block settings. We suggest using dynamic variables based on your VIP tier caculation method

Tier caculation method

Suggested value

Examples

by Point

Earn {{remaining\_points}} {loyalty\_point}} to {{next\_rank}}

Earn 150 points to Gold

by Spent amount

Spend {{remaining\_spend}} to {{next\_rank}}

Spend $220 to Silver

by Order amount

Place {{remaining\_orders}} {{loyalty\_orders}} to {{next\_rank}}

Place 5 orders to Gold

**Note:** The table above is for reference only. After you select your Tier calculation method, our app will automatically update the Progress field value for you.

#### [hashtag](#discount-value-column) Discount Value Column

The dashboard now displays a dedicated "Discount Value" column showing:

Reward Type

Discount Value Display

Example

**Percentage discounts**

Shows percentage with "off"

"50% off", "20% off"

**Fixed amount discounts**

Shows dollar amount with "off"

"$30 off", "$10 off"

**Free shipping**

Displayed as "-"

"-" (with clear program description)

**Free gifts**

Displayed as "-"

"-" (with program details)

**Buy X Get Y offers**

Displayed as "-"

"-" (value varies by cart contents)

#### [hashtag](#enhanced-program-descriptions) Enhanced Program Descriptions

All program descriptions now show proper names and details:

Program Type

Description Format

Example Display

**Percentage discounts**

"Discount X% for Y points"

"Discount 10% for 100 points"

**Fixed amount**

"Discount $X for Y points"

"Discount $10 for 100 points"

**Dynamic amounts**

"Discount $X for every Y points"

"Discount $10 for every 100 points"

**Buy X Get Y**

Shows actual program name set by merchant

"Buy 2, Get 50% off the third items"

**Free gifts**

Shows free gift program name

"Free product"

**Entry rewards**

Shows tier entry reward name

"Gold tier entry reward"

**Referral rewards**

Standard referral text

"Referral program"

**Milestone rewards**

Shows rule name set by merchant

"Earned points milestone"

### [hashtag](#how-to-set-up-loyalty-dashboard) How to set up **Loyalty Dashboard**

1

**Access Embedded Content**

- Open the **Joy Loyalty** app.
- Navigate to **Embedded Content** from the dashboard.

2

**Click Account page, select Loyalty Dashboard**

- Click **Edit in Theme Editor**

3

**Add the Block to Your Loyalty Page**

- Open the **Theme Editor**
- Select **Add Block**, then find **Joy: loyalty dashboard** under the **Apps** section

4

Click save

### [hashtag](#faqs) FAQs

#### [hashtag](#will-existing-customer-coupons-automatically-show-discount-values) Will existing customer coupons automatically show discount values?

Yes, the system automatically calculates and displays discount values for all existing coupons based on their configured reward amounts.

#### [hashtag](#can-i-customize-the-discount-value-format) Can I customize the discount value format?

Yes, you can customize the format through the translation settings, including currency symbols and text like "off" or "discount".

#### [hashtag](#what-happens-if-a-coupon-has-multiple-discount-types) What happens if a coupon has multiple discount types?

The system displays the primary discount value. For complex offers like "Buy X Get Y", it shows "-" since the value depends on cart contents.

#### [hashtag](#can-customers-see-expired-coupons-in-the-dashboard) Can customers see expired coupons in the dashboard?

You can configure whether to show expired coupons. If shown, they typically appear with clear expiration indicators and disabled apply buttons.

#### [hashtag](#does-the-enhanced-dashboard-work-with-all-loyalty-program-types) Does the enhanced dashboard work with all loyalty program types?

Yes, the dashboard supports all Joy Loyalty program types including percentage discounts, fixed amounts, free gifts, free shipping, referral rewards, and milestone rewards.

[PreviousAccount pagechevron-left](/on-site-content/account-page)[NextRewards Redemptionchevron-right](/on-site-content/account-page/rewards-redemption)

Last updated 19 days ago

Was this helpful?