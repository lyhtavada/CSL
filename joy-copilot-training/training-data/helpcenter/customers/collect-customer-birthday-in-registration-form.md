---
category: Customers
topic: Collect Customer Birthday In Registration Form
source: helpcenter
---

Q: What is Collect Customer Birthday In Registration Form in Joy Loyalty?
Q: How does Collect Customer Birthday In Registration Form work?
A: This feature is available for **All** plans.

### What is this feature

Joy Loyalty allows you to collect a customer's date of birth directly in the registration form using a simple date picker. When customers create an account, the birthday is saved to Shopify and synced to Joy through Shopify’s customer creation webhook.

In addition to collecting the birthday during registration, Joy can also sync birthday information from the **Shopify Customer Metafield** section. This is helpful if your team manually updates birthdays, if you migrated data from another platform, or if you use third-party apps that enrich customer profiles.

### Where the birthday is stored

Birthday data collected from either source is stored in:

- **Shopify Customer Notes**, under the field name *Birthday* (or your configured name).
- **Shopify Customer Metafields**, if the metafield exists and contains a valid date.

Joy reads from both locations and keeps the birthday information synchronized.

### Requirements before using this feature

Before collecting birthdays through either method, ensure you have:

- A Joy Loyalty program set up. Birthday rewards are optional — you can collect birthdays even if you don’t enable birthday rewards.
- Access to your theme’s Liquid template files if you plan to add the birthday field to the registration form.
- The correct birthday field name configured in Joy (default: **"Birthday"**).
- Customer metafields enabled or available in your Shopify admin if you plan to sync birthdays from metafields.

### Why you should collect birthdays

Birthdays are one of the most effective and expected reward moments. Approaching customers at the right time strengthens loyalty and drives repeat purchases. Gathering birthdays during registration—or syncing them from Shopify metafields—helps you maintain more complete profiles without depending on low-conversion surveys or follow-up emails.

### Two ways to collect birthday data

#### 1. Collect birthday from the customer registration form\

**Step 1 — Configure Joy to recognize the birthday field**

Open your Joy dashboard settings and locate the “Birthday field name in register form” setting.
Enter **Birthday** (or your preferred name) and save.
This tells Joy where to read the value from Shopify's customer notes.

**Step 2 — Add the birthday field to your registration form**

Go to your theme editor and open the registration template (usually `customers/register.liquid`).
Insert the following code where you want the birthday field to appear:

Save the template. Customers will now see a native date picker when registering, and Joy will automatically pick up this information.

#### 2. Sync birthday from Shopify customer metafields


(See the full help center article for more details.)