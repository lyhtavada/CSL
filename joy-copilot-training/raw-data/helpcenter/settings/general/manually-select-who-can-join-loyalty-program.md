### [hashtag](#overview) Overview

Allow only selected customers to join your loyalty program.
When enabled, the system will ignore the default “auto join on login” logic — meaning customers **must be manually added or approved** before they can become members.

Typical use case:

> The merchant wants customers to first accept a **terms of service form**.
> Once accepted, a **Shopify Flow** triggers the action **Join Loyalty Program**, and the customer is added to the program.

### [hashtag](#how-to-set-up) How to set up

> ⚙️ Location: **Settings-> General → Customer Eligibility → Manually assigned customers only**
> 🧩 Automatic eligibility logic is disabled once this option is enabled.

When this option is enabled:

- The app **ignores the default logic** that treats every existing account as a loyalty member (including legacy ones).
- Customers **will not earn points or access loyalty features** unless they are manually added.
- POS and guest orders (email/phone only) will not auto-sync as members either.

#### [hashtag](#ways-to-make-a-customer-join-the-program) Ways to make a customer join the program

Customers can be added through multiple methods:

- **Join button** in Customer Detail (Joy Admin)
- **Shopify Flow action** → Action name: Join loyalty program
- **API integration**
- **Add tag method** → add tag `Joy: Join Loyalty` to customer in Shopify
- **Customer import** → update customer type to *Member* in CSV import

---

### [hashtag](#customer-experience) Customer experience

- **Before joining:**

  - Customer will **not see** any loyalty-related content (Widget, Points, Rewards, VIP, etc.).
  - Loyalty Page can still be accessed, but it appears empty (no data).
  - No point earning, redeeming, or blocks visibility across Account, Checkout, or Thank You pages.
- **After joining (via admin/Flow/API/import):**

  - Customer immediately gains access to all loyalty features and existing data.
  - Widget, Loyalty Page, and related blocks appear normally.

---

### [hashtag](#example-joy-loyalty-x-powerful-form-builder) Example: Joy Loyalty x Powerful form builder

You can combine Joy Loyalty with Powerful form builder to collect customer consent before joining the loyalty program.

**Video Guide:**

📝 **Note:**
When setting up this Flow, make sure to configure the proper **form** **conditions** as you wish e.g. Required login, auto create Customers, mapping fields such as Email, enable Flow trigger and place the consent form in the right section of your store to ensure correct member assignment.

**About the Flow**, you can download this file:

file-download

2KB

[Join loyalty program.flow](https://1367962225-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpAxc1paAgix94BNLrez8%2Fuploads%2Fgit-blob-f6e63ada8a3eab9faaf5c5c17560ee46c2ba3860%2FJoin%20loyalty%20program.flow?alt=media)

downloadDownload[arrow-up-right-from-squareOpen](https://1367962225-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpAxc1paAgix94BNLrez8%2Fuploads%2Fgit-blob-f6e63ada8a3eab9faaf5c5c17560ee46c2ba3860%2FJoin%20loyalty%20program.flow?alt=media)

And import to Shopify flow:

---

### [hashtag](#faq) FAQ

**1. What happens to existing customers when enabling this setting?**
→ All customers will be treated as *guest* until explicitly added back to the program.

**2. Can I still use Shopify Flow to automate member assignment?**
→ Yes, use the **Joy action: Join Loyalty Program** to add approved customers automatically.

**3. Can I manually add someone back?**
→ Yes. Go to **Customer Detail → Actions → Join program** or use **Import → Update type**.

**4. Do POS customers automatically join the program?**
→ No. POS customers (who leave only email/phone) won’t auto-sync as members if this option is enabled.

**5. Will this affect point earning or rewards visibility?**
→ Yes. Customers outside the program won’t earn or redeem points and will see empty loyalty content.

[PreviousExcluded B2B customers from loyalty programchevron-left](/settings/general/excluded-b2b-customers-from-loyalty-program)[NextCustomer behavior settingschevron-right](/settings/general/customer-behavior-settings)

Last updated 19 days ago

Was this helpful?