By default, in most of the Shopify themes, customers are redirected to the customer account page right after the login. This creates quite a disruptive experience for the customers during the shopping journey. In this guide, we will help you change this behavior and bring customers back to the right page where they logged in beforehand.

### [hashtag](#video) Video

See this video if you want to see it in action:

### [hashtag](#dive-into-the-theme-code) Dive into the theme code

Most of the Shopify themes have a `headers.liquid` file, in this file you search for this block of code. And notice the `routes.account_login_url` , this is the variable that is responsible for redirecting the customer post-login. You can change this behavior by updating the [other variables herearrow-up-right](https://shopify.dev/docs/api/liquid/objects/routes).

### [hashtag](#update-the-code) Update the code

All you need to do is change the `routes.account_login_url` to `routes.storefront_login_url` , which means it would take customers back to the page before the customer attempted the login.

### [hashtag](#result) Result

As you can see in the result, the customer is redirected back to the cart page with ease and no longer needs to exit the account page, go to checkout anymore. Voila!

[PreviousDoes manual point adjusting affect VIP tier status?chevron-left](/faqs/does-manual-point-adjusting-affect-vip-tier-status)[NextPrivacy Policychevron-right](/policies/privacy-policy)

Last updated 19 days ago

Was this helpful?