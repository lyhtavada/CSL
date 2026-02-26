circle-info

**Who can use this feature?**

This feature is available for **Professional, Advanced, and Enterprise** plans.

### [hashtag](#introduction) Introduction

The Point Calculator is your secret weapon for turning every purchase into an exciting rewards journey. It's like a digital scoreboard that shows customers exactly how many points they'll earn, transforming shopping from a transaction into a rewarding experience.

In today’s competitive e-commerce market, driving repeat purchases and customer loyalty is essential. The Point Calculator feature in our Joy Loyalty App does more than just track rewards—it motivates customers to make purchases by showing how many points they can earn with each order. This encourages immediate buying and helps build long-term loyalty, making it a crucial tool for boosting repeat sales and engagement.

### [hashtag](#how-to-set-up-the-point-calculator) How to set up the point calculator

1

Open **Point calculator setting**

- On the left menu of Joy, go to **Branding > Point calculator > Setup**.

- There are three sections: **Choose positions, Point calculator settings, Advanced settings.**

More specifically:

- **Position of the Point calculator:** Choose the location of the Point Calculator on the product information page.
- **Design Settings of the Point calculator:** Customize the appearance of the point calculator:

  - **Font:** Choose a text font that matches your brand style.
  - **Size:** Adjust the text size for optimal readability.
  - **Icon:** Select an icon that complements the design.
  - **Icon Color:** Define the color of the icon to align with your theme.
  - **Text Color:** Set the text color to ensure clear visibility.
- **Advanced settings:** Customize the point calculator according to your preferences.

2

Set **the position of the Point calculator** in the theme settings

- Click on "**Go to theme**", you will be directed to the Shopify theme settings page.

- At this point, **select any product > open its product details page**. In the image, I have chosen "3 Decorative Glass Vases Set."

- On the left sidebar, in the template settings, **Add block > Apps > Joy: Point calculator**.

- After completing the setup, the Point calculator will be displayed as shown in the image below. If you are satisfied with the design and position, click **Save**. You have successfully added the Point calculator to your store.

### [hashtag](#how-to-set-up-point-calculation-display-on-the-cart-page) How to set up point calculation display on the Cart page

In addition to the default display on the product detail page, the point calculator block can also **be shown on the cart page**. To enable this feature, `activate "Also use on Cart Page"` and then go to the theme settings to add the Point Calculator to the cart page. Adding the Point calculator to the cart page is similar to adding this feature to the product detail page.

We have also prepared an animation for you to view and follow. We hope this GIF will be helpful. If you have any issues, please do not hesitate to contact us for support.

The process of adding the Point Calculator block to the cart page

### [hashtag](#how-to-set-up-the-point-calculator-in-the-cart-drawer) How to set up the point calculator in the cart drawer

First of all, you will need to enable the Point Calculator App embeds to make sure that the SDK is running on every page of your store, unlike the App block, which runs on the product page and cart page only.

With the cart drawer, we cannot directly use the Asset API to edit your theme code, so if you want to implement it, you have to do it manually via the theme code editor. If you are not sure of how to do it, feel free to reach out to our support team.

You can go to your theme code editor, find the `snippets/cart-drawer.liquid` or `snippets/mini-cart.liquid` , the name depends on your theme code structure. Then, place this snippet in your cart drawer:

You should be seeing the point calculator for the order showing in the cart drawer. This calculator will reflect on the change of the cart quantity and items.

### [hashtag](#faq) FAQ

#### [hashtag](#when-i-change-the-product-variant-the-points-calculator-is-not-recalculated) When I change the product variant, the points calculator is not recalculated

Each theme has different ways to identify the variant selector on the product page. Most of the time, they seem to have a similar pattern that we can cover in our code. But in some scenarios, we will require some manual work to fill the product variant selector in the Advanced settings.

For example, some themes may have the selector identifier to be `.product-form__input select`. Once you fill in the selector, on the change of the variant, our widget will recalculate the points.

### [hashtag](#how-to-set-up-in-the-vintage-theme) How to set up in the Vintage theme

As you may know, the [Vintage themearrow-up-right](https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions) does not support you to add an App Block to a nested position within the product page. In order to implement our feature, you may need to add our snippet just like you did with the cart drawer.

#### [hashtag](#step-1-input-the-code-snippet) Step 1: Input the code snippet

You can go to your theme code edit, for example, in my case it is the Debut theme, I need to find the file `sections/product-template.liquid` look for the desired position to input the snippet below:

#### [hashtag](#step-2-turn-on-the-app-embed-block) Step 2: Turn on the App embed block

Go to your theme's App embeds section, make sure the Joy: Point Calculator app embed is turned on, and then hit the save button. The reason why you need to do this is that the App Embed is the only thing that is supported in the Vintage theme, not the App block.

### [hashtag](#add-product-calculator-to-checkout-page) Add product calculator to checkout page

circle-info

In order to edit the checkout, you need to be on [Shopify Plusarrow-up-right](https://www.shopify.com/plus). This is an exclusive feature of Shopify Plus.

Just like the [Redeem at checkout block](/reward-programs/redeeming-programs/redeem-at-checkout-page), you need to customize the checkout page via Settings or from your theme editor. Then, make sure to click on the Add block in the Order summary section, this is the only section we support adding the point calculator at the checkout page.

Once done, go out to your online store to test this out.

### [hashtag](#add-the-point-calculator-to-the-thank-you-page) Add the point calculator to the Thank you page

Unlike the checkout page, the Thank you page is mostly for everyone. You can add the point calculator, also known as the Reward celebration block, to the Thank you page. See our [dedicated guide](/on-site-content/branding/reward-reminder) for this.

### [hashtag](#wrap-up) Wrap-up

Adding a Point calculator to your store is a way to engage customers by showing them the value they can gain from their purchases. By following the steps outlined in this guide, you can easily set up and customize the Point Calculator to match your store's aesthetic and position it where it will be most effective.

This not only enhances the shopping experience but also encourages repeat purchases, helping to build long-term customer loyalty. Start implementing the Point calculator today and see the positive impact it has on your store's performance!
If you have any questions, feel free to contact our support team on live chat or email us at [[email protected].envelope](/cdn-cgi/l/email-protection#44373134342b36300425322520256a2d2b6a) Happy supporting!

### [hashtag](#faqs) FAQs

#### [hashtag](#if-i-enable-the-app-embeds-instead-of-the-app-block-is-it-ok) If I enable the App Embeds instead of the App block, is it ok?

If you are implementing the Cart drawer calculator and you are on the OS 2.0 theme, then it is ok. But with the OS 2.0 theme, you want to add to the product page, you need to use the app block.

#### [hashtag](#why-are-there-two-blocks-app-embed-and-app-block) Why are there two blocks: App embed and App block?

It is because we support the cart drawer and cart page as well. We have to register the App embeds block, which runs on every page of the store (the cart drawer is on every page). If you only want the product page, then implement it with the app block, and no need to be confused about whether to enable the App Embeds or not.

This banner will tell you whether you have enabled the needed or not:

[PreviousProduct referralchevron-left](/on-site-content/product-page/product-referral)[NextCart drawerchevron-right](/on-site-content/cart-drawer)

Last updated 19 days ago

Was this helpful?