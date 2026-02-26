circle-info

This feature is available in **Pro, Advanced, Enterprise plans**

### [hashtag](#what-is-this-feature) What is this feature?

Picture your customer with $150 of skincare products in their cart and 800 loyalty points. Instead of forcing them to navigate away and risk losing their shopping momentum, the Cart Drawer Redeem Block lets them redeem points instantly within their cart.

They see "Redeem your points: 800 points," select "$25 off for every 250 points," and watch their total drop to $100 in one click: no disruption, no confusion – just seamless value recognition embedded directly in their purchase flow.

### [hashtag](#why-you-should-use-this-feature) Why you should use this feature

Rising acquisition costs demand maximizing existing customer relationships over chasing new ones. Every redemption friction point represents lost revenue and weakened loyalty.

The Cart Drawer Redeem Block creates immediate gratification that builds psychological loyalty. When customers redeem points without disrupting their flow, they develop anticipation for future redemptions, shifting from price-shopping to loyalty-building.

### [hashtag](#setting-up-the-cart-drawer-redeem-block) Setting up the Cart Drawer Redeem Block

1

**Enabling the embedded content block**

To add the Cart Drawer Redeem Block to your store, you'll need to configure it through Joy's embedded content settings and then implement it in your theme.

1. From your Joy Loyalty dashboard, navigate to **Embedded content**
2. Select the **Product page** tab
3. Locate **Redeem in Cart Drawer** in the available blocks list
4. Click **Edit in Theme Editor** to access the configuration options

2

**Enable the App embed in the Theme editor**

After opening the Theme editor, you can find and turn on the new Joy's app embed named "**Joy: Redeem in line**"

1. Switch to the **"App embeds"** tab
2. Turn on Joy's new app embed "**Joy: Redeem in line**"
3. Click save

3

**Configuring display options**

The Cart Drawer Redeem Block includes several customization options to match your store's branding through the embedded content configuration panel.

**Button styling:**

- **Background color button apply** - Set the background color for the apply button
- **Text color button apply** - Configure the text color for the apply button
- **Border color button apply** - Customize the border color for the apply button

**Functional settings:**

- **Enable cancel discount** - Toggle to allow customers to remove applied discounts and restore their points
- **Reload page after applying coupon** - Enable page reload after discount application for theme compatibility, or disable for smoother AJAX-based updates
- **Hide block for guest users or Customers doesn't have enough points**
- **Minimal view layout/Detail view layout**

4

**Implementing the code snippet**

After enabling the block in your Joy dashboard, you'll need to add the redemption interface to your cart drawer template.

1. Access your Shopify theme editor
2. Navigate to your cart drawer template file: typically `cart-drawer.liquid` or similar
3. Insert the following code snippet where you want the redemption block to appear:

5

**Save changes and watch results**

The redemption interface will automatically appear in your cart drawer once the code is implemented and customers have points available for redemption.

### [hashtag](#frequently-asked-questions) Frequently Asked Questions

**Can customers redeem multiple reward types in a single transaction?**

The Cart Drawer Redeem Block supports one active redemption per cart session. Customers can change their selection before completing checkout, but multiple simultaneous redemptions are not supported to prevent confusion and maintain cart clarity.

**What happens if a customer removes items from their cart after redeeming points?**

The system automatically recalculates applicable discounts when cart contents change. If the cart total falls below the minimum requirement for the applied discount, the system will notify the customer and may remove the discount, restoring their redeemed points.

**How does the redemption block handle cart drawer updates?**

The interface includes options for both page reload and AJAX-based updates. The AJAX option provides a smoother experience by updating cart totals without refreshing the page, while the reload option ensures compatibility with all theme types.

**Can merchants customize error messages for their brand voice?**

Yes, all error messages can be customized through the embedded content settings. Merchants can modify text to match their brand voice while maintaining clarity about redemption requirements and limitations.

**What happens to redeemed points if a customer abandons their cart?**

Points are only permanently deducted when a customer completes their purchase. If they abandon their cart or navigate away without checking out, their points remain available for future redemptions. However, any applied discount codes may remain in their cart session until manually removed.

**How does the feature handle different point-to-currency conversion rates?**

The system automatically calculates discount values based on your configured reward program settings. Whether you use fixed rates (like 100 points = $10) or variable rates, the interface displays accurate discount amounts and point requirements for each option.

**Can customers see their redemption history through the cart drawer block?**

The Cart Drawer Redeem Block focuses on current redemption actions rather than historical data. Customers should visit their loyalty page or account dashboard to view their complete redemption history and point-earning activities.

[PreviousCart drawerchevron-left](/on-site-content/cart-drawer)[NextCheckout pagechevron-right](/on-site-content/checkout-page)

Last updated 19 days ago

Was this helpful?