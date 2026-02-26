circle-info

This feature is available for **Advanced and above plans**

The **Custom Program** allows you to create flexible earning programs with triggers beyond the default options.
You can reward customers for **any activity you define** — whether it happens on your storefront, through a custom event, or inside Shopify Flow.

Each trigger action gives you more freedom to build unique, personalized experiences and automate loyalty rewards based on your own business logic.

---

### [hashtag](#id-1.-visit-a-page) **1. Visit a page**

#### [hashtag](#overview) 🧩 Overview

This trigger allows you to reward customers when they visit a specific page on your storefront.
You can use it to create engaging earning activities, such as visiting your new collection, blog, or campaign landing page.
This is a great way to encourage traffic to important pages on your site.

---

#### [hashtag](#how-to-set-up) ⚙️ How to set up

1. Go to **Reward programs → Custom Program → Trigger action → Visit a page**
2. Enter:

   - **Program name**
   - **Page URL** (exact page or contains specific keywords)
   - **Reward points**
   - **Start / End date** (optional)
3. Enable **Fraud prevention** if you want to limit repeated actions from the same customer.
4. Click **Save** to create the program.
5. Turn on the program when ready.

---

#### [hashtag](#customer-experience) 🧍 Customer experience

Once active, the program appears in your loyalty widget and loyalty page.
When a customer visits the configured URL, Joy automatically records the action and adds reward points.

---

#### [hashtag](#faq) ❓FAQ

**Q: Can I track visits for multiple pages?**
A: Yes. You can create multiple custom programs, separate each program for each URL.

**Q: Do I need to add any code?**
A: No. Joy automatically tracks page visits once the program is active.

---

### [hashtag](#id-2.-custom-trigger) **2. Custom trigger**

#### [hashtag](#overview-1) 🧩 Overview

The **Custom trigger** option lets you define your own event on your website — such as button clicks, form submissions, or any custom interaction — and reward customers when it happens.
This gives merchants maximum flexibility to connect Joy with any activity on their storefront or POS system.

---

#### [hashtag](#how-to-set-up-1) ⚙️ How to set up

1. Go to **Reward programs → Custom Program → Trigger action → Custom trigger**
2. Create a new program by entering:

   - **Program name**
   - **Reward points**
   - **Start / End date** (optional)
   - Click **Save**
     → Joy automatically generates an **action\_key**.
3. In the integration guide shown in-app:

   - **Step 1: Copy the JS snippet provided.**
   - **Step 2: Add the code generated to your website** where you want to trigger the reward action. This is normally placed inside event handlers (button clicks, form submissions, etc.)

     Example usage:

     • After a survey form is submitted

     • When a video finishes playing

     • When a specific button is clicked

     • After completing a quiz
   - **Step 3: Activate the program**

     Test your custom trigger yourself to update the connection status. Once successfully connected, you can turn on the program. You can also skip this step by selecting 'Skip' (status will become connected).

> You can skip the connection test and turn it on directly — just make sure the integration code is correctly placed as intend.

---

#### [hashtag](#customer-experience-1) 🧍 Customer experience

Once the program is active:

- When the custom trigger fires (for example, a button click or form submit), Joy receives the event and rewards the customer automatically.
- For POS stores, the staff can tap **Complete** in the Loyalty POS app to reward customers.

---

#### [hashtag](#faq-1) ❓FAQ

**Q: What if I skip the connection step?**
A: That’s fine — just ensure the trigger code is added correctly. Once the trigger runs, Joy will recognize it automatically.

**Q: Is coding required?**
A: A basic understanding of HTML/JS is recommended to install the trigger code properly.

---

### [hashtag](#id-3.-shopify-flow-trigger) **3. Shopify Flow trigger**

#### [hashtag](#overview-2) 🧩 Overview

This trigger allows you to connect Joy Loyalty directly with **Shopify Flow**, so you can reward customers based on any Flow automation — for example, when a customer makes a purchase, submits a form, or meets certain conditions.

This makes your loyalty program more flexible and powerful, integrating seamlessly into your existing Shopify automation workflows.

---

#### [hashtag](#how-to-set-up-2) ⚙️ How to set up

1. Go to **Reward programs → Custom Program → Trigger action → Shopify Flow trigger**
2. Create a new program:

   - Enter program name, reward points
   - Click **Save**
     → Joy generates a unique **action\_key** and sets the program as `draft`.
3. Open **Shopify Flow** and create a new flow with your desired use case
4. Add an **action** → **Run a custom program** in your use case flow

   - Fill in:

     - `action_key`: copied from Joy
     - `email`: customer email variable from Flow trigger, you can add by click add variable and search for email
   - Save the flow
   - Run a test by trigger the flow and the Run a custom program action
5. Go back to Joy

   - Once Joy detects a call from Shopify Flow with that `action_key`, the status changes to **Connected**. (Joy will automatically check for conection status)
6. Click **Turn on** to activate the program.

---

#### [hashtag](#customer-experience-2) 🧍 Customer experience

Once the program is turned on:
Whenever the connected Flow runs and the action is triggered, Joy will automatically reward customers with the points defined in your custom program.

---

#### [hashtag](#faq-2) ❓FAQ

**Q: What if my Flow doesn’t show up in Joy?**
A: Make sure the Flow has been triggered at least once and that the `action_key` matches exactly.

**Q: Is Shopify Flow required to use Joy?**
A: No. Shopify Flow is optional — you can still use the “Visit a page” or “Custom trigger” options instead.

[PreviousStreak bonus challengechevron-left](/reward-programs/earning-programs/streak-bonus-challenge)[NextSubmit Receiptchevron-right](/reward-programs/earning-programs/submit-receipt)

Last updated 19 days ago

Was this helpful?