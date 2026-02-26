---
category: Integrations
subcategory: Integrate With Shopify Flow
topic: Shopify Flow Store Credit
source: helpcenter
---

Q: What is Shopify Flow Store Credit in Joy Loyalty?
Q: How do I set up Shopify Flow Store Credit?
Q: How do I connect Shopify Flow Store Credit with Joy Loyalty?
A: This feature is available for: **Professional, Advanced, and Enterprise plans**

### What is Store Credit?

Store Credit is a cashback system that works alongside your loyalty program:

- **Direct Cashback**: Customers earn actual monetary value they can spend immediately
- **Flexible Spending**: Any amount can be used (even small amounts like $0.10)
- **Seamless Checkout**: Works directly in Shopify's native checkout process
- **Customer Account Integration**: Visible in customer accounts without additional configuration

### Why do you need Store Credit?

Store Credit transforms your loyalty program by offering real money instead of abstract points. Customers appreciate the transparent value they can spend instantly at checkout without conversion complexities.

This streamlined approach improves retention, encourages additional spending (customers often spend more than their credit amount), and keeps revenue within your business when handling returns.

Unlike traditional points systems, Store Credit leverages Shopify's native functionality for a simpler, more effective loyalty solution that benefits both you and your customers.

### Connect with Shopify flow and grant Store Credit access

Make sure you enabled the [Shopify Customer Account](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts/manage) before start iusing this feature.

1

Open **Joy: Loyalty Program**, go to **Integrations**, and select **Shopify flow**

2

Turn on **Shopify flow**

3

Click on "**Grant Store Credit access**"

To use the Store Credit feature in Shopify Flow, you need to grant additional access permissions to the app. This is an optional feature and only necessary if you want to use Store Credit.

### How to set up Store Credit?

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

### Store credit formula cheat sheet

Setting your cashback rate can be calculated by normal mathematical operations or [Shopify Liquid syntax](https://shopify.dev/docs/api/liquid/filters/math-filters). Both can be used, but the Liquid syntax opens more flexibility because Shopify Flow support this right out of the box.

You can try out a few of these examples and tweak them to match your use case:

Description

Syntax

2% cashback on subtotal (using math)

{{order.subtotalPriceSet.shopMoney. amount}} / 50

2% cashback on subtotal (using Liquid)

{{order.subtotalPriceSet.shopMoney. amount | divided\_by: 50}}


(See the full help center article for more details.)