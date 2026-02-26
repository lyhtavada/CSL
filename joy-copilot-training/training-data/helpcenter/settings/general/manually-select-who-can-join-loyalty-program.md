---
category: Settings
subcategory: General
topic: Manually Select Who Can Join Loyalty Program
source: helpcenter
---

Q: What is Manually Select Who Can Join Loyalty Program in Joy Loyalty?
Q: How do I set up Manually Select Who Can Join Loyalty Program?
Q: Where can I find Manually Select Who Can Join Loyalty Program settings?
A: ### Overview

Allow only selected customers to join your loyalty program.
When enabled, the system will ignore the default “auto join on login” logic — meaning customers **must be manually added or approved** before they can become members.

Typical use case:

> The merchant wants customers to first accept a **terms of service form**.
> Once accepted, a **Shopify Flow** triggers the action **Join Loyalty Program**, and the customer is added to the program.

### How to set up

> ⚙️ Location: **Settings-> General → Customer Eligibility → Manually assigned customers only**
> 🧩 Automatic eligibility logic is disabled once this option is enabled.

When this option is enabled:

- The app **ignores the default logic** that treats every existing account as a loyalty member (including legacy ones).
- Customers **will not earn points or access loyalty features** unless they are manually added.
- POS and guest orders (email/phone only) will not auto-sync as members either.

#### Ways to make a customer join the program

Customers can be added through multiple methods:

- **Join button** in Customer Detail (Joy Admin)
- **Shopify Flow action** → Action name: Join loyalty program
- **API integration**
- **Add tag method** → add tag `Joy: Join Loyalty` to customer in Shopify
- **Customer import** → update customer type to *Member* in CSV import

---

### Customer experience

- **Before joining:**

  - Customer will **not see** any loyalty-related content (Widget, Points, Rewards, VIP, etc.).
  - Loyalty Page can still be accessed, but it appears empty (no data).
  - No point earning, redeeming, or blocks visibility across Account, Checkout, or Thank You pages.
- **After joining (via admin/Flow/API/import):**

  - Customer immediately gains access to all loyalty features and existing data.
  - Widget, Loyalty Page, and related blocks appear normally.

---

### Example: Joy Loyalty x Powerful form builder

You can combine Joy Loyalty with Powerful form builder to collect customer consent before joining the loyalty program.

**Video Guide:**

📝 **Note:**
When setting up this Flow, make sure to configure the proper **form** **conditions** as you wish e.g. Required login, auto create Customers, mapping fields such as Email, enable Flow trigger and place the consent form in the right section of your store to ensure correct member assignment.

**About the Flow**, you can download this file:

file-download

2KB

[Join loyalty program.flow](https://1367962225-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpAxc1paAgix94BNLrez8%2Fuploads%2Fgit-blob-f6e63ada8a3eab9faaf5c5c17560ee46c2ba3860%2FJoin%20loyalty%20program.flow?alt=media)


(See the full help center article for more details.)