circle-info

This feature is available for **Advanced and above plans**

### [hashtag](#user-content-overview) Overview

Submit Receipt is an earning program that allows customers to upload photos of their purchase receipts. Store staff review the submissions and approve or reject them. Approved receipts reward customers with points or discounts.

**Use case:** Merchants with physical stores or POS systems who want to reward in-store purchases through the loyalty program.

---

### [hashtag](#user-content-how-to-set-up) How to set up

#### [hashtag](#user-content-step-1-create-the-program) Step 1: Create the program

1. Go to **Reward programs → Earning programs → Add new**
2. Select **Submit receipt**
3. Configure:

   - **Program name** and **Description**
   - **Start/End date** (optional)
   - **Reward type:** Points, Amount discount, or Percentage discount
   - **Differ by VIP tier** (optional)

#### [hashtag](#user-content-step-2-set-submission-limit-anti-cheat) Step 2: Set submission limit (Anti-cheat)

Prevent abuse by limiting how often customers can submit receipts.

- Toggle **On** to enable limit
- Set the time frame (e.g., 10 submissions per 1 day)

#### [hashtag](#user-content-step-3-save-and-activate) Step 3: Save and activate

Click **Save** to create the program. Make sure the program status is **Active**.

---

### [hashtag](#user-content-customer-experience) Customer experience

#### [hashtag](#user-content-submitting-a-receipt) Submitting a receipt

Customers can upload receipts from:

- **Widget** → Way to earn → Submit receipt program
- **Loyalty page** → Block "Way to earn" → Submit receipt program

They can upload multiple images (JPG, PNG, JPEG, max 5MB each) in one submission.

#### [hashtag](#user-content-after-submission) After submission

- Customer sees a success message
- Receipt status is **Pending** until staff reviews
- Once approved → reward is granted, logged in activity history
- If rejected → no reward (optional: send notification via Shopify Flow/Klaviyo)

---

### [hashtag](#user-content-admin-review-process) Admin review process

#### [hashtag](#user-content-view-submitted-receipts) View submitted receipts

Go to **Activities → Submitted receipts** to see all submissions.

Table columns:

- Receipt ID
- Customer email
- Submitted time
- Status (Pending / Approved / Rejected)
- Actions

#### [hashtag](#user-content-use-ai-suggestion) Use AI Suggestion

Click **Ask AI** to analyze the receipt image. AI will extract:

- Customer info (name, phone, email if visible)
- Store info (name, address)
- Order info (items, amounts)
- Recommendation: Approve or Reject with confidence %

#### [hashtag](#user-content-approve-or-reject) Approve or Reject

- **Approve:** Customer receives reward, activity is logged
- **Reject:** No reward, optional notification to customer

---

### [hashtag](#user-content-notifications-shopify-flow--klaviyo) Notifications (Shopify Flow & Klaviyo)

You can set up automated emails to notify customers about their receipt submission status.

**Available triggers:**

- **Customer submit a receipt** – Send confirmation when receipt is uploaded
- **Moderator approved a receipt** – Notify customer their receipt was approved and reward granted
- **Moderator reject a receipt** – Notify customer their receipt was rejected

**Where to set up:**

- **Klaviyo:**

1. In Joy admin, go to **Integrations → Klaviyo → Select triggers** → Check the receipt triggers → **Confirm**

1. Then in Klaviyo, go to **Flows → Create flow** → Select the Joy event trigger you want

- ~~**Shopify Flow:**~~ ~~Go to Shopify Admin → Settings → Flow → Create workflow → Select Joy trigger~~ (Coming soon)

---

### [hashtag](#user-content-faq) FAQ

**Can customers submit multiple receipts at once?** Yes. Each submission can include multiple images, max to 5, but it creates one request for review.

**What file types are accepted?** JPG, PNG, and JPEG. Maximum 5MB per image.

**Is the AI analysis automatic?** No. Staff must click "Ask AI" to trigger the analysis. Final approval is always manual.

**What happens if a customer exceeds the submission limit?** They will see an error message and cannot submit until the limit resets.

**Can I change an approved receipt to rejected?** Yes. You can change the status, and the reward (coupon) will be revoked automatically.

[PreviousCustom programchevron-left](/reward-programs/earning-programs/custom-program)[NextSubmit Formchevron-right](/reward-programs/earning-programs/submit-form)

Last updated 19 days ago

Was this helpful?