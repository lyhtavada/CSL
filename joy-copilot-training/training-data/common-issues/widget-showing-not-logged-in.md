---
category: Onsite content
problem: Widget showing customer as not logged in despite being logged in
source: notion
---

Q: Why does the Joy widget show "not logged in" even though I'm already logged into my store account?
Q: My customer says they are logged in but the loyalty widget still asks them to log in. What's going on?
Q: The Joy loyalty widget doesn't recognize that a customer is signed in. How do I fix this?
Q: After logging in, the Joy widget still shows the guest view instead of the member view. Why?
Q: Customers complain they have to log in again on the Joy widget even though they're already signed in on my Shopify store.
A: This is a known issue caused by a Shopify bug with the new Customer Accounts system. When a customer logs in using Shopify's new Customer Accounts, the single sign-on (SSO) state sometimes doesn't sync properly when the customer navigates back to the storefront after logging in.

Here's what you can do right now:

**Quick workaround for customers:**
1. After logging in to your Shopify account, click the **"Join program"** button on the Joy widget. This will re-authenticate the session and the widget will recognize the customer correctly.

**Recommended store-level fix:**
2. Set up a **Shopify redirect** so that after login, customers are sent back to the **previous page** they were on (instead of the default account page). This helps the SSO state sync properly.

**Permanent fix:**
3. Our dev team is aware of this issue and is actively working on a permanent fix. We'll notify you once the update is released.

Escalate khi: The workaround and redirect setup do not resolve the issue, or the problem persists across multiple customers consistently.
