---
category: Settings
subcategory: Developers
topic: Magic Tags
source: helpcenter
---

Q: What is Magic Tags in Joy Loyalty?
Q: How do I set up Magic Tags?
Q: Where can I find Magic Tags settings?
A: This feature is available on the **Advanced plan and above**.

### Introduction

With our new **Magic Tagging** feature, we drew inspiration from Shopify Flow, which allows actions to be triggered based on conditions and events. However, while Shopify Flow can automate actions like adding tags to customers, it doesn’t support dynamic value extraction from the tag content for loyalty activities.

To bridge this gap, we’ve introduced Magic Tagging within the Joy Loyalty app, providing an alternative way to manipulate customer point balances without needing to use [our API.](https://devdocs.joy.so/joy-rest-api/customers)

### How Magic Tagging works

Magic Tagging allows you to add or remove points from a customer's balance by simply adding a tag to their profile. For example, you can use a tag like: **"Joy: Add 500 - Place order #111 via POS"** This format will adjust the customer's balance by 500 points, and the comment section helps track the reason for the adjustment.

This feature gives you an alternate method for managing customer balances, especially useful if you're looking for flexibility beyond the [Joy API](https://devdocs.joy.so/joy-rest-api/customers).

### How to set up Magic Tagging

To enable this feature, you’ll need to first turn on the **Manage Tags** option in your settings:

1

Navigate to **Settings > Developer** within the Joy Loyalty app

2

Enable the **Manage Tags** feature

Once enabled, you can add a tag to a customer using the following format: **"Joy: Add 100 - Place order #111 via POS".** This will add 100 points to the customer’s balance and include a comment for easy tracking.

### **Magic tag supported types**

**Type**

**Goal**

**Syntax**

**Add/Subtract point**

Add/ subtract customer's point balance

Joy: Add <Points> - <comment reason>

For example: Joy: Add 100 - Place order #111 via POS

**Exclude customer**

Exclude customer out of loyalty program

Joy: Exclude - <comment reason>

For example: Joy: Exclude - Internal staff

**Change tier**

Change customer's VIP tier

Syntax: Joy: Tier = <New Tier name>

For example: Joy: Tier = Gold

By default, Customer will receive new tier's entry rewards. If you don't want to give entry rewards, try this syntax:
Joy: Tier = <New tier name> (No entry reward)

For example: Joy: Tier = Gold (No entry reward)

### **Important usage notes**

- **Triggering the Action**: The tag will only trigger the balance adjustment when you add the tag and hit save on the customer profile.

(See the full help center article for more details.)