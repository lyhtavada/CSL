circle-info

This feature is available for **All** plans.

### [hashtag](#what-is-this-feature) What is this feature

Joy Loyalty allows you to collect a customer's date of birth directly in the registration form using a simple date picker. When customers create an account, the birthday is saved to Shopify and synced to Joy through Shopify’s customer creation webhook.

In addition to collecting the birthday during registration, Joy can also sync birthday information from the **Shopify Customer Metafield** section. This is helpful if your team manually updates birthdays, if you migrated data from another platform, or if you use third-party apps that enrich customer profiles.

### [hashtag](#where-the-birthday-is-stored) Where the birthday is stored

Birthday data collected from either source is stored in:

- **Shopify Customer Notes**, under the field name *Birthday* (or your configured name).
- **Shopify Customer Metafields**, if the metafield exists and contains a valid date.

Joy reads from both locations and keeps the birthday information synchronized.

### [hashtag](#requirements-before-using-this-feature) Requirements before using this feature

Before collecting birthdays through either method, ensure you have:

- A Joy Loyalty program set up. Birthday rewards are optional — you can collect birthdays even if you don’t enable birthday rewards.
- Access to your theme’s Liquid template files if you plan to add the birthday field to the registration form.
- The correct birthday field name configured in Joy (default: **"Birthday"**).
- Customer metafields enabled or available in your Shopify admin if you plan to sync birthdays from metafields.

### [hashtag](#why-you-should-collect-birthdays) Why you should collect birthdays

Birthdays are one of the most effective and expected reward moments. Approaching customers at the right time strengthens loyalty and drives repeat purchases. Gathering birthdays during registration—or syncing them from Shopify metafields—helps you maintain more complete profiles without depending on low-conversion surveys or follow-up emails.

### [hashtag](#two-ways-to-collect-birthday-data) Two ways to collect birthday data

#### [hashtag](#id-1.-collect-birthday-from-the-customer-registration-form) 1. Collect birthday from the customer registration form\

**Step 1 — Configure Joy to recognize the birthday field**

Open your Joy dashboard settings and locate the “Birthday field name in register form” setting.
Enter **Birthday** (or your preferred name) and save.
This tells Joy where to read the value from Shopify's customer notes.

**Step 2 — Add the birthday field to your registration form**

Go to your theme editor and open the registration template (usually `customers/register.liquid`).
Insert the following code where you want the birthday field to appear:

Save the template. Customers will now see a native date picker when registering, and Joy will automatically pick up this information.

#### [hashtag](#id-2.-sync-birthday-from-shopify-customer-metafields) 2. Sync birthday from Shopify customer metafields

If your store already stores birthdays in **Shopify Customer Metafields**, Joy can read this value and sync it to the loyalty platform. This helps in scenarios such as:

- Migrating customer data from another loyalty system.
- Using third-party apps (e.g., Klaviyo) that write data to Shopify customer profiles.
- Staff manually updating customer birthdays inside Shopify Admin.

How this works:

- In Joy, go to **Settings → General → Sync Shopify metafields to Joy customer data**.
- Map the appropriate metafield (e.g., `facts.birthdate`) to the Joy birthday field.
- When a customer is created or updated, Joy checks the metafield.
- If a valid date exists, Joy updates the customer’s birthday in the loyalty program.

This makes the metafield a seamless, automated alternative.

#### [hashtag](#example-video) Example video

You included a video showing how data flows from Klaviyo → Shopify metafield → Joy Loyalty. Keep it here as a practical reference.

### [hashtag](#supporting-existing-customers) Supporting existing customers

For customers created before adding the registration field, you can gather birthdays by:

- Editing Shopify customer metafields
- Asking customers through email
- Using profile completion flows
- Collecting data via customer service channels

Joy will sync all updates from either customer notes or metafields.

### [hashtag](#frequently-asked-questions) Frequently Asked Questions

**What happens if customers don't want to provide their birthday?**

The birthday field is optional by default. Customers can complete registration without entering a birth date, and the system will simply proceed without storing birthday information. This maintains registration conversion rates while maximizing data collection opportunities.

**Can the birthday field be customized to match our theme design?**

Yes, the field uses standard HTML input elements that inherit your theme's existing form styling. You can apply custom CSS classes or modify the styling to match your brand's visual design requirements.

**How does this work with privacy regulations like GDPR?**

Birthday collection follows the same privacy principles as other customer data in Shopify. Include birthday information in your privacy policy and ensure customers consent to data collection as part of your standard registration process.

**Will this affect our registration conversion rates?**

Studies show that single additional fields in registration forms have minimal impact on conversion rates when properly implemented. The optional nature of the field and its integration with existing form flow helps maintain registration performance.

**Can we use a different field name than "Birthday"?**

Yes, you can customize the field name in both the liquid code and Joy settings. Ensure both locations use the same identifier for proper data synchronization.

[PreviousExcluding customers from loyalty programchevron-left](/customers/excluding-customers-from-loyalty-program)[NextReward programschevron-right](/reward-programs)

Last updated 19 days ago

Was this helpful?