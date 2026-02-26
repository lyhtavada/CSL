---
category: Reward Programs
subcategory: Earning Programs
topic: Custom Program
source: helpcenter
---

Q: What is Custom Program in Joy Loyalty?
Q: How do I set up Custom Program?
Q: How do customers earn rewards with Custom Program?
A: This feature is available for **Advanced and above plans**

The **Custom Program** allows you to create flexible earning programs with triggers beyond the default options.
You can reward customers for **any activity you define** — whether it happens on your storefront, through a custom event, or inside Shopify Flow.

Each trigger action gives you more freedom to build unique, personalized experiences and automate loyalty rewards based on your own business logic.

---

### **1. Visit a page**

#### 🧩 Overview

This trigger allows you to reward customers when they visit a specific page on your storefront.
You can use it to create engaging earning activities, such as visiting your new collection, blog, or campaign landing page.
This is a great way to encourage traffic to important pages on your site.

---

#### ⚙️ How to set up

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

#### 🧍 Customer experience

Once active, the program appears in your loyalty widget and loyalty page.
When a customer visits the configured URL, Joy automatically records the action and adds reward points.

---

#### ❓FAQ

**Q: Can I track visits for multiple pages?**
A: Yes. You can create multiple custom programs, separate each program for each URL.

**Q: Do I need to add any code?**
A: No. Joy automatically tracks page visits once the program is active.

---

### **2. Custom trigger**

#### 🧩 Overview

The **Custom trigger** option lets you define your own event on your website — such as button clicks, form submissions, or any custom interaction — and reward customers when it happens.
This gives merchants maximum flexibility to connect Joy with any activity on their storefront or POS system.

---

#### ⚙️ How to set up

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


(See the full help center article for more details.)

---

Q: Can I track visits for multiple pages?
A: Yes. You can create multiple custom programs, separate each program for each URL.

Q: Do I need to add any code?
A: No. Joy automatically tracks page visits once the program is active.

---

Q: What if I skip the connection step?
A: That’s fine — just ensure the trigger code is added correctly. Once the trigger runs, Joy will recognize it automatically.

Q: Is coding required?
A: A basic understanding of HTML/JS is recommended to install the trigger code properly.

---

Q: What if my Flow doesn’t show up in Joy?
A: Make sure the Flow has been triggered at least once and that the `action_key` matches exactly.

Q: Is Shopify Flow required to use Joy?
A: No. Shopify Flow is optional — you can still use the “Visit a page” or “Custom trigger” options instead.

[PreviousStreak bonus challenge](/reward-programs/earning-programs/streak-bonus-challenge)[NextSubmit Receipt](/reward-programs/earning-programs/submit-receipt)

Last updated 19 days ago

Was this helpful?
