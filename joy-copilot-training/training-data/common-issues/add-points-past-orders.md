---
category: Reward programs
problem: Merchant wants to add points for orders placed before installing the app
source: notion
---

Q: I just installed Joy and I want to give loyalty points to customers who placed orders before I had the app. Is that possible?
Q: Can I retroactively award points for past orders that were placed before I set up the loyalty program?
Q: My existing customers made purchases before I installed Joy. How do I add points for their previous orders?
Q: I want to reward my loyal customers for orders they placed before I started using Joy Loyalty. What are my options?
Q: Is there a way to sync points for historical orders so my existing customers don't start with zero points?

A: By default, Joy only calculates points for orders placed after the app is installed. However, there are a couple of ways to award points for past orders:

**Option 1: Give a fixed point amount to existing customers**
This is the simplest approach and works well as a welcome gesture:
1. Prepare a CSV file with your existing customers and the point amounts you'd like to give each one.
2. Use the **Points Adjustment** feature in Joy to bulk-import the CSV and credit points to those customers.
3. Consider sending a newsletter or email to let your customers know they've received loyalty points and introduce them to your new rewards program.

**Option 2: Automatically calculate points for past orders**
If you want points to be calculated based on actual past order values:
1. In your Joy admin, go to **Dev_zone > Dev tool > Update points for past orders**.
2. Enter the date range for the orders you want to include. Make sure the start date aligns correctly with your order history.
3. The system will calculate and award points based on those historical orders.
4. For awarding points on **all past orders** (all-time), you can also use the **"Sync point for past order"** option found in **Settings**.

**Important tips:**
- Before running a bulk update, double-check your earning rules to make sure points are calculated the way you want.
- We recommend testing with a small date range first to verify everything looks correct before processing all historical orders.

Escalate khi: The Dev tool returns errors or points are not calculated correctly after running the sync.
