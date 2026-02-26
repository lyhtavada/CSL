---
category: Reward Programs
subcategory: Milestone
topic: Subscription Milestones
source: helpcenter
---

Q: What is Subscription Milestones in Joy Loyalty?
Q: How do I set up Subscription Milestones?
Q: How do customers earn rewards with Subscription Milestones?
A: This feature is available for **Advanced** and **Ultimate** plans.

### Overview

**Subscription milestones** track **consecutive successful billing cycles** across a customer's subscription contracts and trigger rewards when they hit specific renewal targets.

#### When to use this

- You sell subscription products and want to **reduce churn**
- You want to reward long-term subscribers for their commitment
- You want to incentivize customers to keep their subscription active rather than canceling

### How to set up

When you open the Subscription milestone config page, you'll see a setup guide with 4 steps:

#### Step 1: Ensure Shopify Flow is connected

Go to **Settings → Integrations** and make sure **Shopify Flow** is connected to Joy.

#### Step 2: Import the Flow template (Required)

The subscription milestone needs a **Shopify Flow workflow** to track billing cycle data. Here's how to do it:

**Manual import**

1. Download the Flow template file: Joy Loyalty – Subscription Order Data Sync.flow below:

file-download

3KB

[Joy Loyalty - Subscription Order Data Sync.flow](https://1367962225-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpAxc1paAgix94BNLrez8%2Fuploads%2FDP3e9ubXOB8GKbmaLnDC%2FJoy%20Loyalty%20-%20Subscription%20Order%20Data%20Sync.flow?alt=media&token=2abf64fb-4a26-4bdc-8838-d3a63202f33b)

downloadDownload[-from-squareOpen](https://1367962225-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpAxc1paAgix94BNLrez8%2Fuploads%2FDP3e9ubXOB8GKbmaLnDC%2FJoy%20Loyalty%20-%20Subscription%20Order%20Data%20Sync.flow?alt=media&token=2abf64fb-4a26-4bdc-8838-d3a63202f33b)

1. In your Shopify admin, go to **Apps → Shopify Flow**
2. Click **Import** (top-right corner)

1. Select the downloaded `.flow` file

1. Review the workflow and click **Turn on**

> **Why is this needed?** Shopify doesn't send subscription renewal data to apps by default. This Flow template listens for subscription billing events and sends the data to Joy, so we can count billing cycles for your milestones.

#### Step 3: Set up your milestone rules

1. **Rule name:** Give your milestone a descriptive name (e.g., "6-Month Subscriber Reward")
2. **Start date / End date:** Set the active period (end date is optional)
3. **Milestone condition:** Set the number of **successful billing cycles** required

   - Example: Set to `6` to reward customers after their 6th consecutive renewal
4. **Rewards:** Choose one or more rewards (**Bonus points**, **Gift**, or **Discount**)

#### Step 4: Activate the program

Click **Save** to apply your changes, then click **Turn on** to start tracking.

### How it works

- The milestone counts **consecutive successful billing cycles** for each subscription contract

(See the full help center article for more details.)