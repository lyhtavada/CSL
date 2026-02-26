circle-info

This feature is available for **All** plans.

### [hashtag](#overview) Overview

Customer types are one of the foundations of how Joy Loyalty works. They determine who can earn points, who can redeem rewards, and who can actually see their loyalty status. Understanding how customers move between these types—and how Shopify’s account system affects them—helps you run a loyalty program that is consistent, fair, and aligned with your store setup.

### [hashtag](#why-customer-types-matter) Why customer types matter

Every customer interacts with your store differently. Some authenticate through Shopify’s modern SSO, some still use legacy customer accounts, and others simply check out as guests. Joy translates these behaviors into clear customer types so the loyalty experience always stays consistent.

- **Members** can earn points, redeem rewards, and see their full loyalty status inside the widget.
- **Guests** may earn points if allowed, but they cannot redeem or view their loyalty balance until they register.
- **Left-program customers** are fully excluded and do not see the loyalty widget at all.

This structure ensures your loyalty program behaves exactly as you intend, no matter how customers choose to shop.

### [hashtag](#the-three-customer-types-in-joy-loyalty) The three customer types in Joy Loyalty

#### [hashtag](#member) **Member**

A Member is a fully eligible customer who can earn points, redeem rewards, join VIP tiers, and see their loyalty status inside the widget. Members have access to the complete loyalty experience.

How someone becomes a Member depends on your Shopify account system, which Joy automatically detects.

You can also let all as guest, and choose to manually assign who can be accessible to the program.

#### [hashtag](#guest) **Guest**

A Guest is a customer who is not recognized as a Member. They may earn points if guest earning is enabled, but they cannot redeem rewards or view their loyalty data until they become Members. The widget only displays general program information to them.

#### [hashtag](#left-program) **Left program**

Customers in this type are completely excluded from the loyalty program. They cannot earn points, cannot redeem, and cannot view the loyalty widget at all. Stores often use this type for wholesale users, internal staff, test accounts, or any customers who should be excluded from rewards.

### [hashtag](#sso-vs-legacy-accounts-how-customers-become-members) SSO vs legacy accounts: how customers become Members

Joy follows Shopify’s authentication rules to determine the customer type.

#### [hashtag](#if-your-store-uses-shopifys-sso-new-customer-accounts) If your store uses Shopify’s SSO (New Customer Accounts)

With SSO, customers authenticate using Shopify’s identity system instead of creating a traditional store account. Once authenticated:

- Joy always treats them as a **Member**
- They do not need to register a store account
- Their loyalty status appears instantly
- They can earn and redeem seamlessly

**With SSO, customers are Members anytime Shopify identifies them.**

#### [hashtag](#if-your-store-uses-legacy-customer-accounts) If your store uses legacy customer accounts

Legacy accounts require customers to manually create a store account and log in.

Under this system:

- A customer becomes a **Member only after creating an account**
- If they are not logged in, they are treated as **Guest**
- Guests cannot redeem or see loyalty status
- Once logged in, they regain **Member** status

**With legacy accounts, customers are Members only when they register and log in.**

### [hashtag](#customer-behavior-comparison-sso-vs-legacy-accounts) Customer behavior comparison: SSO vs legacy accounts

Feature / Behavior

**SSO (New Customer Accounts)**

**Legacy Customer Accounts**

How customer becomes a Member

Automatically, whenever authenticated

Only after registering + logging in

Guest behavior

Appears as Guest only if fully unauthenticated

Very common; remains Guest until account created

Can earn points

Yes

Yes (or as Guest if enabled)

Can redeem points

Yes

Only when logged in

Can see loyalty widget

Yes, personalized

Yes, personalized only when logged in

Can see loyalty status

Always when authenticated

Only when logged in

Experience

Seamless, modern, recommended

Requires manual registration/login

### [hashtag](#manual-eligibility-mode-optional) Manual eligibility mode (optional)

Some merchants want full control over who becomes a Member. Joy supports this through the [**Manually assigned customers only**](/settings/general/manually-select-who-can-join-loyalty-program) mode.

When this mode is enabled:

- Joy stops auto-assigning Members and Guests
- Customers do not become Members automatically, even if they authenticate or register
- You manually assign who can join the program
- Only assigned Members can earn, redeem, and see loyalty status

This mode is ideal for B2B stores, invite-only loyalty programs, and stores with strict qualification rules.

circle-info

Please note that the Exclude from program in the demo flow below is just for demo purpose that you can join/exclude via Shopify Flow. Please update to your use case.

### [hashtag](#managing-customer-types-in-your-joy-dashboard) Managing customer types in your Joy dashboard

You can update a customer’s type at any time from the **Customers** section of your Joy dashboard.

Joy enforces logical transitions to keep data consistent:

- A **Guest** can become a **Member** or be moved to **Left program**
- A **Member** can be changed to **Left program**
- A **Left program** customer can be reinstated as a **Member**

Inside each customer profile, shortcuts such as **Join program** and **Exclude from program** make adjustments quick and simple.

circle-info

Notes

- A customer marked as **Guest** can only be changed to **Member** or **Left program**.
- A **Member** can only be changed to **Left program**.
- A **Left program** customer can only be changed to **Member**.

### [hashtag](#summary) Summary

Customer types define how each shopper experiences your loyalty program. Depending on whether your store uses Shopify SSO or legacy accounts, customers may automatically become Members or remain Guests until they register. Members receive the full benefits. Guests have limited access. Left-program customers are excluded entirely.

With manual eligibility mode, you gain even more control over who can join and participate in your loyalty system.

By understanding these types and how they work, you can deliver a loyalty experience that stays clear, predictable, and suited to the way your customers shop.

### [hashtag](#wrap-up) Wrap up

Segmenting customer types within Joy Loyalty ensures that each customer receives the appropriate engagement based on their level of interaction with your loyalty program. By organizing your customers into Members, Guests, and Left Program categories, you can better tailor your rewards and communication strategies to keep your loyalty program running smoothly.

[PreviousImport customer datachevron-left](/customers/import-customer-data)[NextGenerate customer QR codechevron-right](/customers/generate-customer-qr-code)

Last updated 19 days ago

Was this helpful?