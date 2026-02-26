---
category: Reward programs
problem: Program not working correctly and merchant doesn't remember what changed
source: notion
---

Q: My loyalty program stopped working correctly but I don't remember what I changed. How can I check?
Q: Is there a way to see the change history of a program in Joy?
Q: How do I use Program History in Dev Zone to troubleshoot my program?
Q: I need to find out who changed my earning program settings and when. Where can I see that?
Q: Something broke in my rewards program after a recent change. How do I find out what was modified?
A: You can use the **Program History** feature in Dev Zone to see every change that was made to a program. This is a great way to troubleshoot when something isn't working as expected!

Here's how to check your program's change history:

**Step 1 - Get the Program ID:**
- You can find the Program ID in the **URL** when you're viewing the program in Joy admin (it's the number at the end of the URL).
- Alternatively, you can find it in the browser's **Network tab** (for advanced users).

**Step 2 - Open Program History:**
1. Go to **Dev Zone** in your Joy admin.
2. Search for or navigate to **"Program History"**.

**Step 3 - Search for your program:**
1. Enter the **Program ID** in the search field.
2. Click **Search**.

**Step 4 - Review the changes:**
- Results are shown with the **newest changes first**.
- Each entry shows:
  - **Timestamp** - when the change was made
  - **Operation** - what type of change (CREATE, UPDATE, etc.)
  - **Fields changed** - which settings were modified
- You can **filter by a specific field** if you're looking for a particular setting change.
- Click the **eye icon** on any entry to see a side-by-side comparison of the **old vs. new values** for that change.

**Supported programs:**
Program History works with all programs that have a Program ID, including:
- Earning programs
- Redeeming programs
- Perks
- Exclusive deals
- Milestones
- And more!

Escalate khi: Program History does not show the expected changes, or the merchant needs help interpreting the changes and reverting to a previous configuration.
