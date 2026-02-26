---
category: On Site Content
subcategory: Account Page
topic: Loyalty Dashboard
source: helpcenter
---

Q: What is Loyalty Dashboard in Joy Loyalty?
Q: How do I set up Loyalty Dashboard?
Q: How do I customize Loyalty Dashboard on my store?
A: This feature is available in **Advanced, Enterprise plans**

### **What is a Loyalty Dashboard?**

A Loyalty Dashboard is a centralized section on a customer's account page that displays their complete loyalty program status. It shows their current points balance, tier level, available rewards, earning history, and progress toward the next tier or reward. This dashboard serves as the customer's personal command center for all loyalty-related information.

### Why do you need this feature?

The enhanced dashboard with discount values transforms how customers perceive and interact with your loyalty program. By showing specific discount amounts (like "50% off" or "$20 off") instead of just program descriptions, customers can immediately understand the real monetary value of their rewards.

This transparency increases program engagement by helping customers make strategic decisions about when and how to redeem their points. When customers see concrete savings opportunities, they're more motivated to participate actively in your loyalty program and make additional purchases to reach higher-value rewards.

### Loyalty dashboard display rules

#### Block settings/Progress

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

#### Discount Value Column

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

#### Enhanced Program Descriptions

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

(See the full help center article for more details.)