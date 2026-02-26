### [hashtag](#introduction-to-joy-loyalty-widget-integration-with-hydrogen) Introduction to Joy Loyalty Widget Integration with Hydrogen

The Joy Loyalty Widget Integration is your bridge to creating a seamless, engaging loyalty experience in a Hydrogen-powered Shopify store. It's a comprehensive solution that transforms customer interactions into valuable, rewarding moments.

You can find a complete guide on our [npm package here.arrow-up-right](https://npmjs.com/joyso-hydrogen-sdk)

### [hashtag](#why-do-you-need-to-integrate) Why do you need to integrate

Building your Shopify store with Hydrogen and integrating Joy Loyalty is a game-changer. A loyalty program boosts customer retention, increases average order value, and strengthens brand loyalty. With Joy Loyalty, you can incentivize repeat purchases, stand out from competitors, and gain insights into shopper behavior—all while delivering a seamless experience.

### [hashtag](#how-to-enable-custom-storefront-development) How to enable custom storefront development

Go to **Settings > Developers > Enable Custom Storefront development**

### [hashtag](#how-to-set-up-your-hydrogen-store) How to set up your Hydrogen store

If you've already developed your Hydrogen store, you're all set! However, if you haven't started yet or are looking to test a Hydrogen store with Joy Loyalty, don't worry. You can easily set up a quick-start Hydrogen store by following this guide: [Getting Started with Hydrogenarrow-up-right](https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started).

If you are not on Shopify Plus plan but still want to test this out with development store first. You can update your `.env` file with Storefront API key from your Custom App

### [hashtag](#installation) Installation

### [hashtag](#implementation) Implementation

#### [hashtag](#id-1.-load-joy-loyalty-data) 1. Load Joy Loyalty Data

In your `app/root.jsx` or `app/layout.jsx` loader:

#### [hashtag](#id-2.-initialize-joy-loyalty-in-root-layout) 2. Initialize Joy Loyalty in Root Layout

In your `app/root.jsx` or `app/layout.jsx`:

#### [hashtag](#id-3.-add-csp-whitelist) 3. Add CSP whitelist

Update your entry.server.jsx to include the CSP whitelist for Joy Loyalty:

After this, you should be able to see the Joy Loyalty widget in your storefront. Besides, the quickstart template of Hydrogen has `box-sizing: content-box` so the floating button may look a bit weird. You can add this CSS to `app. css` to fix it. Otherwise, there should be no CSS issues.

### [hashtag](#id-3.-point-calculator) 3. Point Calculator

**GraphQL Query and Loader**

First, update your product page loader and query:

#### [hashtag](#component-implementation) **Component Implementation**

In your product page (e.g., `app/routes/products.$handle.jsx`):

### [hashtag](#test-the-widget) Test the widget

After these are implemented, you will see the widget display on your custom storefront according to your settings. However, you can compare the widgets on the custom storefront and the Online Store channel to make sure both are working properly. With the widget, you can earn points, redeem points, and use coupons seamlessly on your store.

### [hashtag](#wrap-up) Wrap up

Our app has other features such as Joy Point Calculator, Joy Rewards Page, etc. If you want to build your own Rewards page using Hydrogen, we will have another post showing how to implement this Rewards page using our Public API and JavaScript SDK.

We hope that this guide provides you with the first step on how to integrate the Joy Loyalty Program widget into your Headless Commerce store.

[PreviousDeveloperschevron-left](/settings/developers)[NextMagic tagschevron-right](/settings/developers/magic-tags)

Last updated 19 days ago

Was this helpful?