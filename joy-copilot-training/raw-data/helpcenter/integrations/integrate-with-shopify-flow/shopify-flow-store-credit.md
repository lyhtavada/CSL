circle-info

This feature is available for: **Professional, Advanced, and Enterprise plans**

### [hashtag](#what-is-store-credit) What is Store Credit?

Store Credit is a cashback system that works alongside your loyalty program:

- **Direct Cashback**: Customers earn actual monetary value they can spend immediately
- **Flexible Spending**: Any amount can be used (even small amounts like $0.10)
- **Seamless Checkout**: Works directly in Shopify's native checkout process
- **Customer Account Integration**: Visible in customer accounts without additional configuration

### [hashtag](#why-do-you-need-store-credit) Why do you need Store Credit?

Store Credit transforms your loyalty program by offering real money instead of abstract points. Customers appreciate the transparent value they can spend instantly at checkout without conversion complexities.

This streamlined approach improves retention, encourages additional spending (customers often spend more than their credit amount), and keeps revenue within your business when handling returns.

Unlike traditional points systems, Store Credit leverages Shopify's native functionality for a simpler, more effective loyalty solution that benefits both you and your customers.

### [hashtag](#connect-with-shopify-flow-and-grant-store-credit-access) Connect with Shopify flow and grant Store Credit access

circle-info

Make sure you enabled the [Shopify Customer Accountarrow-up-right](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts/manage) before start iusing this feature.

1

Open **Joy: Loyalty Program**, go to **Integrations**, and select **Shopify flow**

2

Turn on **Shopify flow**

3

Click on "**Grant Store Credit access**"

To use the Store Credit feature in Shopify Flow, you need to grant additional access permissions to the app. This is an optional feature and only necessary if you want to use Store Credit.

### [hashtag](#how-to-set-up-store-credit) How to set up Store Credit?

1

Click on "**Flow**", choose "**Create workflow**" and "**Select a trigger**"

2

Insert a new step: Choose **Shopify** and select "**order created**"

3

Insert a new step click the "**+**" button and choose "**action**"

4

In the next step, choose "**Joy: Loyalty program**" then select "**Adjust store credit**"

5

Configure the reward amount and conditions

6

Click "**Turn on workflow**" to save

### [hashtag](#store-credit-formula-cheat-sheet) Store credit formula cheat sheet

Setting your cashback rate can be calculated by normal mathematical operations or [Shopify Liquid syntaxarrow-up-right](https://shopify.dev/docs/api/liquid/filters/math-filters). Both can be used, but the Liquid syntax opens more flexibility because Shopify Flow support this right out of the box.

You can try out a few of these examples and tweak them to match your use case:

Description

Syntax

2% cashback on subtotal (using math)

{{order.subtotalPriceSet.shopMoney. amount}} / 50

2% cashback on subtotal (using Liquid)

{{order.subtotalPriceSet.shopMoney. amount | divided\_by: 50}}

2% cashback on subtotal, round down (using Liquid)

{{order.subtotalPriceSet.shopMoney. amount | divided\_by: 50 | floor }}

2% cashback on subtotal, round up (using Liquid)

{{order.subtotalPriceSet.shopMoney. amount | divided\_by: 50 | ceil }}

2% cashback on grand total (using Liquid)

{{order.totalPriceSet.shopMoney.amount}} / 50

2% cashback on subtotal + shipping

({{order.subtotalPriceSet.shopMoney.amount}}+ {{order.totalShippingPriceSet.shopMoney.amount}}) / 50

### [hashtag](#how-to-check-store-credit-balance-in-customer-profile) How to check store credit balance in customer profile

There are 2 ways for you to check:

**View Customer Store Credit on Cutomers of Shopify**

1

Go to **Customers** in your Shopify admin

2

Select a **customer profile**

3

View customers' store credit balance

**View Customer Store Credit on Joy: Loyalty program**

1

Go to **Customers** in **Joy: Loyalty program app**

2

Select **a customer profile**

3

Scroll down to view customers' store credit balance

### [hashtag](#frequently-asked-questions) Frequently Asked Questions

1. **Does store credit expire?**

Store credit expiration is configurable by the merchant. You can set credit to expire after a specific time period or keep it valid indefinitely. Setting expiration dates can encourage customers to make purchases sooner.

1. **Can customers see how they earned their store credit?**

Yes, if you enable shopify customer account extensibility, customers can see their store credit history right out of the box — no extra setup needed.

1. **Will store credit work with my existing loyalty points program?**

Yes, you can use both store credit and points at the same time. But **we recommend focusing on one to keep it simple**. Points are great for long-term loyalty and brand building, while store credit works like cashback, giving customers clear incentives to return.

1. **How do I explain store credit to my customers?**

Consider adding information about your store credit program to your loyalty program FAQs or creating an automated email that explains how it works when customers receive credit for the first time.

[PreviousShopify Flow: Yotpo and Joy Loyaltychevron-left](/integrations/integrate-with-shopify-flow/shopify-flow-yotpo-and-joy-loyalty)[NextShopify Flow: Zigpoll and Joy Loyaltychevron-right](/integrations/integrate-with-shopify-flow/shopify-flow-zigpoll-and-joy-loyalty)

Last updated 19 days ago

Was this helpful?