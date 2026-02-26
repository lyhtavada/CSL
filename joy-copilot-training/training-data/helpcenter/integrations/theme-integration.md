---
category: Integrations
topic: Theme Integration
source: helpcenter
---

Q: What is Theme Integration in Joy Loyalty?
Q: How does Theme Integration work?
Q: How do I connect Theme Integration with Joy Loyalty?
A: This feature is available for **All** plans.

### What is this feature?

The Joy Loyalty theme integration feature allows you to display customer point balances in strategic locations across your storefront, such as:

- Navigation menu
- Account page
- Cart page
- Product pages
- Custom page templates

By adding a simple code snippet to your theme files, you can show customers their current point balance without requiring them to open the loyalty widget. This creates a more integrated loyalty experience and keeps points top-of-mind during the shopping journey, and later on increase loyalty program visibility.

### Requirements before using this feature

To integrate Joy Loyalty points display into your theme, you need:

1. An active Joy Loyalty account
2. Basic understanding of Shopify Liquid code
3. Access to your Shopify theme code editor
4. Customer accounts are enabled in your store

### Why use this feature

Displaying loyalty points throughout your storefront increases program visibility and engagement. When customers can easily see their point balance while browsing products or checking their account, they're more likely to:

- Remember they have points to redeem
- Be motivated to earn additional points through purchases
- Feel recognized as loyal customers
- Experience a more integrated loyalty journey

This integration helps maximize the value of your loyalty program by keeping it visible throughout the customer experience rather than hidden behind a widget.

### Use case 1: Show on your header

#### Step 1: Add the snippet to your header

Add the below snippet code into `sections/header.liquid` file to show customer points and tier level on all pages of your store. Feel free to customize the information you want to show. You may want to greet the customer by Mr + last name, or you do not want to show the tier name, feel free to reach out to our chat support if you need any further customization.

Do not format the liquid code snippet, just copy and paste it into your theme file. If not, the point balance number formatting will not be displayed correctly.

#### Step 2: Mobile menu

Go to `snippets/header-drawer.liquid` and add the following snippet under your My Account link. This snippet does not set the color to white like the above snippet, because the cart drawer in this example has a dark background color.

#### **Step 3: View the result**

On the storefront, you should see the snippet is now showing. When you click on the snippet, it will open up the Joy loyalty widget. On mobile, the snippet will be hidden and only show the one in the header drawer.

### **Use case 2: Customer Account Page**

#### **Step 1:** Copy the code snippet

#### Step 2: Add the snippet to your theme


(See the full help center article for more details.)

---

Q: Will the points display update automatically when customers earn or redeem points?
A: Yes, the display pulls data from customer metafields that automatically update when point balances change.

Q: Can I display other loyalty information besides points?
A: Yes, you can access additional loyalty data through customer metafields. Contact Joy support for specific metafield references.

Q: Will this code work with all Shopify themes?
A: The code should work with most themes, but you may need to adjust it slightly for compatibility with specific theme structures.

Q: What happens if I update my theme?
A: Theme updates may overwrite your customizations. Make sure to back up your code and reapply it after updates.

Q: Can I make the points clickable to open the loyalty widget?
A: Yes, the provided code already includes the `avadaJoyTrigger()` function, which opens the loyalty widget when clicked.

[PreviousIntegrations](/integrations)[NextProduct reviews](/integrations/product-reviews)

Last updated 19 days ago

Was this helpful?
