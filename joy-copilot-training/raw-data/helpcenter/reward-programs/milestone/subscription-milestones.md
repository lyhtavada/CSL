circle-info

This feature is available for **Advanced** and **Ultimate** plans.

### [hashtag](#overview) Overview

**Subscription milestones** track **consecutive successful billing cycles** across a customer's subscription contracts and trigger rewards when they hit specific renewal targets.

#### [hashtag](#when-to-use-this) When to use this

- You sell subscription products and want to **reduce churn**
- You want to reward long-term subscribers for their commitment
- You want to incentivize customers to keep their subscription active rather than canceling

### [hashtag](#how-to-set-up) How to set up

When you open the Subscription milestone config page, you'll see a setup guide with 4 steps:

#### [hashtag](#step-1-ensure-shopify-flow-is-connected) Step 1: Ensure Shopify Flow is connected

Go to **Settings → Integrations** and make sure **Shopify Flow** is connected to Joy.

#### [hashtag](#step-2-import-the-flow-template-required) Step 2: Import the Flow template (Required)

The subscription milestone needs a **Shopify Flow workflow** to track billing cycle data. Here's how to do it:

**Manual import**

1. Download the Flow template file: Joy Loyalty – Subscription Order Data Sync.flow below:

file-download

3KB

[Joy Loyalty - Subscription Order Data Sync.flow](https://1367962225-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpAxc1paAgix94BNLrez8%2Fuploads%2FDP3e9ubXOB8GKbmaLnDC%2FJoy%20Loyalty%20-%20Subscription%20Order%20Data%20Sync.flow?alt=media&token=2abf64fb-4a26-4bdc-8838-d3a63202f33b)

downloadDownload[arrow-up-right-from-squareOpen](https://1367962225-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FpAxc1paAgix94BNLrez8%2Fuploads%2FDP3e9ubXOB8GKbmaLnDC%2FJoy%20Loyalty%20-%20Subscription%20Order%20Data%20Sync.flow?alt=media&token=2abf64fb-4a26-4bdc-8838-d3a63202f33b)

1. In your Shopify admin, go to **Apps → Shopify Flow**
2. Click **Import** (top-right corner)

1. Select the downloaded `.flow` file

1. Review the workflow and click **Turn on**

> **Why is this needed?** Shopify doesn't send subscription renewal data to apps by default. This Flow template listens for subscription billing events and sends the data to Joy, so we can count billing cycles for your milestones.

#### [hashtag](#step-3-set-up-your-milestone-rules) Step 3: Set up your milestone rules

1. **Rule name:** Give your milestone a descriptive name (e.g., "6-Month Subscriber Reward")
2. **Start date / End date:** Set the active period (end date is optional)
3. **Milestone condition:** Set the number of **successful billing cycles** required

   - Example: Set to `6` to reward customers after their 6th consecutive renewal
4. **Rewards:** Choose one or more rewards (**Bonus points**, **Gift**, or **Discount**)

#### [hashtag](#step-4-activate-the-program) Step 4: Activate the program

Click **Save** to apply your changes, then click **Turn on** to start tracking.

### [hashtag](#how-it-works) How it works

- The milestone counts **consecutive successful billing cycles** for each subscription contract
- If a customer has multiple subscriptions, only **one** needs to reach the milestone to trigger the reward
- Each customer receives the reward **once per milestone** — not per subscription contract

### [hashtag](#important-notes) Important notes

- **Paused subscriptions** do not reset progress. When resumed, the cycle count continues from where it left off
- **Cancelled or expired subscriptions** will reset the cycle count for that contract
- **Upgrade/downgrade** of a subscription plan does not reset progress (as long as the subscription isn't cancelled)
- **Prepaid subscriptions** (one-time payment covering multiple cycles) are not supported and will not count toward this milestone

### [hashtag](#faq) FAQ

**Does each subscription contract count separately?** No. The milestone is per customer, not per contract. If a customer has 2 active subscriptions and both reach the milestone threshold, the reward is only given once — on the first contract that qualifies.

**What happens if a customer cancels and resubscribes?** The cycle count resets. They start from 0 on the new subscription contract.

**Do I need a specific subscription app?** No specific app is required. The milestone works via **Shopify Flow**, which tracks billing events from any subscription app integrated with Shopify.

**Is this available on all plans?** Subscription milestones are available on **Advanced** and **Enterprise** plans.

[PreviousMilestonechevron-left](/reward-programs/milestone)[NextAdvanced settingschevron-right](/reward-programs/advanced-settings)

Last updated 12 days ago

Was this helpful?