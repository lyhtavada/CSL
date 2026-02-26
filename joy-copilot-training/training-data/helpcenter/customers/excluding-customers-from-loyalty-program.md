---
category: Customers
topic: Excluding Customers From Loyalty Program
source: helpcenter
---

Q: What is Excluding Customers From Loyalty Program in Joy Loyalty?
Q: How does Excluding Customers From Loyalty Program work?
A: This feature is available for **All** plans.

### What is this feature?

The customer exclusion feature lets you select specific Shopify customer segments to exclude from your loyalty program. Customers in excluded segments cannot earn or redeem points, participate in VIP tiers or referrals, and won't see any loyalty interface elements. Joy Loyalty automatically synchronizes with your Shopify segments, maintaining real-time eligibility management without requiring manual selection of individual customers.

### Requirements before using this feature

To use the customer exclusion feature, you need:

- check

  An active Joy Loyalty account
- check

  At least one customer segment has been created in your Shopify admin
- check

  Admin access to your Shopify store

### Why use this feature

This feature helps merchants who serve different customer types (like B2B and D2C) create appropriate loyalty experiences for each group. By implementing segment-based exclusions, you can prevent reward abuse from wholesale customers, create cleaner experiences by hiding irrelevant features, control program costs by focusing rewards on target segments, and simplify management by leveraging your existing Shopify segmentation rather than creating separate customer lists.

### Setting up customer exclusion

1

**Creating customer segments in Shopify**

Before you can exclude customers, you need to create segments in Shopify:

- From your Shopify admin, go to **Customers** > **Customer segments**
- Click **Create segment**
- Define your segment criteria (e.g., customers with the tag "B2B" or "Wholesale")
- Name your segment and save it
- Joy Loyalty will automatically synchronize this segment

2

**Excluding segments from your loyalty program**

Once your segments are created and synced:

- From your Shopify admin, navigate to **Apps** > **Joy Loyalty**
- In the left sidebar, click on **Settings**
- Find the **Pre-launch** section
- Under **Excluded segments**, click in the dropdown field
- Select the segments you want to exclude from your loyalty program
- The selected segments will appear as tags below the dropdown
- Click **Save changes** to apply your exclusions

#### Understanding the impact on customers

When you exclude segments:

1. Customers in excluded segments will have their member status set to "Left program"
2. These customers will no longer earn points from any actions
3. The loyalty widget and loyalty page will not be visible to them
4. Their points balance will be preserved but cannot be redeemed
5. They will not be able to access VIP tier benefits
6. They cannot participate in referral programs

### Managing excluded customers

#### Viewing customer status

You can identify excluded customers in your Joy Loyalty admin:


(See the full help center article for more details.)

---

Q: What happens to a customer's existing points when they're excluded?
A: Their points balance is preserved but cannot be redeemed while they remain in an excluded segment. If they're later removed from the excluded segment, they'll regain access to their points.

Q: Can I still see order history for excluded customers?
A: Yes, Joy Loyalty will continue to sync order data for all customers, but excluded customers will not earn points for their purchases.

Q: Can excluded customers still see the loyalty page if they have the direct URL?
A: No, excluded customers will not be able to view or interact with any loyalty program elements, even with direct URLs.

Q: What happens if a customer is in both an included and excluded segment?
A: Exclusion rules take precedence. If a customer belongs to any excluded segment, they will be excluded from the loyalty program regardless of other segment memberships.

Q: Can I manually override exclusions for specific customers?
A: No, segment-based exclusions apply to all customers in the segment. For individual exceptions, you would need to remove the customer from the excluded segment in Shopify.

[PreviousApple Wallet Loyalty Pass](/customers/generate-customer-qr-code/apple-wallet-loyalty-pass)[NextCollect customer birthday in registration form](/customers/collect-customer-birthday-in-registration-form)

Last updated 19 days ago

Was this helpful?
