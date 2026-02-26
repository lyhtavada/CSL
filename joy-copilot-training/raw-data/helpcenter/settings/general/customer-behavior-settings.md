circle-info

This feature is available for **All** plans.

### [hashtag](#what-is-customer-behavior-settings) What is Customer Behavior Settings

Customer Behavior Settings allows you to control what happens after a customer applies a discount code from your loyalty program. By default, when customers redeem a reward and apply a discount code, they're redirected to the cart page. With this feature, you can now choose what happens next: stay on the current page, go to the cart page, or trigger a cart drawer.

This feature works across multiple areas of your loyalty program, including:

- The loyalty widget (both V2 and V3)
- The loyalty page
- Redeeming blocks
- My rewards blocks
- Ways to redeem blocks
- Dashboard blocks

By configuring these settings, you can create a smoother shopping experience that encourages customers to continue browsing your store even after applying a discount, potentially increasing cart value and improving conversion rates.

### [hashtag](#requirements-before-using-this-feature) Requirements before using this feature

Before using Customer Behavior Settings, you should:

1. Have an active Joy Loyalty program set up on your Shopify store
2. Have at least one reward that customers can redeem for a discount code
3. If you plan to use the cart drawer option, you'll need to know the CSS selector for your theme's cart drawer button

### [hashtag](#why-you-should-use-customer-behavior-settings) Why you should use Customer Behavior Settings

When customers redeem points for discount codes, the default behavior of redirecting them to the cart page can feel like pressuring them to complete their purchase immediately. This might prevent customers from adding more items to their cart, potentially reducing your average order value.

### [hashtag](#configuring-customer-behavior-settings) Configuring Customer Behavior Settings

#### [hashtag](#access-customer-behavior-settings) Access Customer Behavior Settings

1. From your Shopify admin, go to **Apps**
2. Click on **Joy Loyalty**
3. In the Joy Loyalty dashboard, click **Settings** in the left navigation
4. Select the **General** tab
5. Scroll down to find the **Customer Behavior Settings** card

#### [hashtag](#choose-what-happens-when-customers-apply-discounts) Choose what happens when customers apply discounts

In the Customer Behavior Settings section, you'll see options for controlling what happens after customers apply a discount code:

1

**Option 1: Stay on the current page**

This option keeps customers on the same page after applying a discount code. The discount is still added to their cart, and a success message appears, but they aren't redirected anywhere.

1. Under "Trigger: Apply discount," select **Stay on current page**
2. Click **Save**

This is ideal for merchants who want to encourage customers to continue browsing and potentially add more items to their cart after redeeming a discount.

2

**Option 2: Go to the cart page**

This is the default option. When selected, customers are redirected to the cart page after applying a discount code.

1. Under "Trigger: Apply discount," select **Go to cart page**
2. Click **Save**

This option works well if you want customers to immediately review their cart and proceed to checkout after applying a discount.

3

**Option 3: Show cart drawer**

This option opens your store's cart drawer/sidebar after a customer applies a discount code, allowing them to see their updated cart without leaving the current page.

1. Under "Trigger: Apply discount," select **Show cart drawer**
2. In the "Cart drawer button selector" field, enter the CSS selector that your theme uses for the cart button or icon

   - For example: `.cart-icon` or `#cart-toggle`
3. Click **Save**

The cart drawer selector is the CSS class or ID that your theme uses to trigger the cart drawer. If you're unsure what selector to use, you can:

- Check your theme documentation
- Ask your theme developer
- Inspect the cart button element using your browser's developer tools

#### [hashtag](#testing-your-settings) Testing your settings

After configuring your Customer Behavior Settings, it's important to test how they work:

1. Visit your store's frontend as a customer
2. Sign in to your loyalty account or create one
3. Earn enough points to redeem a discount reward
4. Redeem the points for a discount code
5. Apply the discount and observe whether the behavior matches your selected setting

### [hashtag](#faqs) FAQs

#### [hashtag](#will-these-settings-affect-all-discount-codes-in-my-store) Will these settings affect all discount codes in my store?

No, these settings only apply to discount codes that customers redeem through your Joy Loyalty program. They won't affect other discount codes applied manually or from other apps.

#### [hashtag](#what-happens-if-i-select-show-cart-drawer-but-dont-provide-a-selector) What happens if I select "Show cart drawer" but don't provide a selector?

If you don't provide a valid cart drawer selector, the system will default to keeping customers on the current page when they apply a discount.

#### [hashtag](#can-i-have-different-settings-for-different-parts-of-my-loyalty-program) Can I have different settings for different parts of my loyalty program?

Currently, the Customer Behavior Settings apply globally to all areas of your loyalty program where customers can apply discount codes.

#### [hashtag](#can-customers-still-go-to-their-cart-after-applying-a-discount-if-i-select-stay-on-current-page) Can customers still go to their cart after applying a discount if I select "Stay on current page"?

Yes, customers can still navigate to their cart manually using your store's regular cart button or icon.

#### [hashtag](#what-if-my-theme-doesnt-have-a-cart-drawer) What if my theme doesn't have a cart drawer?

If your theme doesn't have a cart drawer feature, you should choose either the "Stay on current page" or "Go to cart page" options instead.

[PreviousManually select who can join loyalty programchevron-left](/settings/general/manually-select-who-can-join-loyalty-program)[NextCustom point labelchevron-right](/settings/general/custom-point-label)

Last updated 19 days ago

Was this helpful?