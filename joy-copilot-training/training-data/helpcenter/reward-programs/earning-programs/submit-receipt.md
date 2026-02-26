---
category: Reward Programs
subcategory: Earning Programs
topic: Submit Receipt
source: helpcenter
---

Q: What is Submit Receipt in Joy Loyalty?
Q: How do I set up Submit Receipt?
Q: How do customers earn rewards with Submit Receipt?
A: This feature is available for **Advanced and above plans**

### Overview

Submit Receipt is an earning program that allows customers to upload photos of their purchase receipts. Store staff review the submissions and approve or reject them. Approved receipts reward customers with points or discounts.

**Use case:** Merchants with physical stores or POS systems who want to reward in-store purchases through the loyalty program.

---

### How to set up

#### Step 1: Create the program

1. Go to **Reward programs → Earning programs → Add new**
2. Select **Submit receipt**
3. Configure:

   - **Program name** and **Description**
   - **Start/End date** (optional)
   - **Reward type:** Points, Amount discount, or Percentage discount
   - **Differ by VIP tier** (optional)

#### Step 2: Set submission limit (Anti-cheat)

Prevent abuse by limiting how often customers can submit receipts.

- Toggle **On** to enable limit
- Set the time frame (e.g., 10 submissions per 1 day)

#### Step 3: Save and activate

Click **Save** to create the program. Make sure the program status is **Active**.

---

### Customer experience

#### Submitting a receipt

Customers can upload receipts from:

- **Widget** → Way to earn → Submit receipt program
- **Loyalty page** → Block "Way to earn" → Submit receipt program

They can upload multiple images (JPG, PNG, JPEG, max 5MB each) in one submission.

#### After submission

- Customer sees a success message
- Receipt status is **Pending** until staff reviews
- Once approved → reward is granted, logged in activity history
- If rejected → no reward (optional: send notification via Shopify Flow/Klaviyo)

---

### Admin review process

#### View submitted receipts

Go to **Activities → Submitted receipts** to see all submissions.

Table columns:

- Receipt ID
- Customer email
- Submitted time
- Status (Pending / Approved / Rejected)
- Actions

#### Use AI Suggestion

Click **Ask AI** to analyze the receipt image. AI will extract:

- Customer info (name, phone, email if visible)
- Store info (name, address)
- Order info (items, amounts)
- Recommendation: Approve or Reject with confidence %

#### Approve or Reject

- **Approve:** Customer receives reward, activity is logged
- **Reject:** No reward, optional notification to customer

---

### Notifications (Shopify Flow & Klaviyo)

You can set up automated emails to notify customers about their receipt submission status.

**Available triggers:**

- **Customer submit a receipt** – Send confirmation when receipt is uploaded
- **Moderator approved a receipt** – Notify customer their receipt was approved and reward granted
- **Moderator reject a receipt** – Notify customer their receipt was rejected

**Where to set up:**

- **Klaviyo:**


(See the full help center article for more details.)