---
category: Settings
subcategory: Developers
topic: Integrate The Joy Loyalty Widget To Hydrogen
source: helpcenter
---

Q: What is Integrate The Joy Loyalty Widget To Hydrogen in Joy Loyalty?
Q: How do I set up Integrate The Joy Loyalty Widget To Hydrogen?
Q: How do I connect Integrate The Joy Loyalty Widget To Hydrogen with Joy Loyalty?
Q: Where can I find Integrate The Joy Loyalty Widget To Hydrogen settings?
A: ### Introduction to Joy Loyalty Widget Integration with Hydrogen

The Joy Loyalty Widget Integration is your bridge to creating a seamless, engaging loyalty experience in a Hydrogen-powered Shopify store. It's a comprehensive solution that transforms customer interactions into valuable, rewarding moments.

You can find a complete guide on our [npm package here.](https://npmjs.com/joyso-hydrogen-sdk)

### Why do you need to integrate

Building your Shopify store with Hydrogen and integrating Joy Loyalty is a game-changer. A loyalty program boosts customer retention, increases average order value, and strengthens brand loyalty. With Joy Loyalty, you can incentivize repeat purchases, stand out from competitors, and gain insights into shopper behavior—all while delivering a seamless experience.

### How to enable custom storefront development

Go to **Settings > Developers > Enable Custom Storefront development**

### How to set up your Hydrogen store

If you've already developed your Hydrogen store, you're all set! However, if you haven't started yet or are looking to test a Hydrogen store with Joy Loyalty, don't worry. You can easily set up a quick-start Hydrogen store by following this guide: [Getting Started with Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started).

If you are not on Shopify Plus plan but still want to test this out with development store first. You can update your `.env` file with Storefront API key from your Custom App

### Installation

### Implementation

#### 1. Load Joy Loyalty Data

In your `app/root.jsx` or `app/layout.jsx` loader:

#### 2. Initialize Joy Loyalty in Root Layout

In your `app/root.jsx` or `app/layout.jsx`:

#### 3. Add CSP whitelist

Update your entry.server.jsx to include the CSP whitelist for Joy Loyalty:

After this, you should be able to see the Joy Loyalty widget in your storefront. Besides, the quickstart template of Hydrogen has `box-sizing: content-box` so the floating button may look a bit weird. You can add this CSS to `app. css` to fix it. Otherwise, there should be no CSS issues.

### 3. Point Calculator

**GraphQL Query and Loader**

First, update your product page loader and query:

#### **Component Implementation**

In your product page (e.g., `app/routes/products.$handle.jsx`):

### Test the widget

After these are implemented, you will see the widget display on your custom storefront according to your settings. However, you can compare the widgets on the custom storefront and the Online Store channel to make sure both are working properly. With the widget, you can earn points, redeem points, and use coupons seamlessly on your store.

### Wrap up


(See the full help center article for more details.)