circle-info

**Who can connect Joy with Klaviyo?**

This feature is available for **All** **plans.**

### [hashtag](#what-is-this-feature) Overview

The [Klaviyoarrow-up-right](https://www.klaviyo.com/) integration for Joy Loyalty allows you to synchronize your loyalty program data with your email marketing platform, enabling more targeted and effective communications. This integration has been enhanced with real-time event triggers that automatically send detailed loyalty event data to Klaviyo when specific loyalty activities occur.

The integration works on two levels:

1. **Basic data synchronization** [Joy and Klaviyo](/integrations/email-marketing-and-sms/joy-and-klaviyo#how-to-segment-customers-in-klaviyo): Customer loyalty information, like points balance, tier status, and referral links, is made available in Klaviyo for segmentation and personalization.
2. **Enhanced event triggers** [How to create event-based automations in Klaviyo](/integrations/email-marketing-and-sms/joy-and-klaviyo#how-to-create-event-based-automations-in-klaviyo): Real-time loyalty events are transmitted to Klaviyo, allowing you to create automated email workflows based on specific loyalty activities.

### [hashtag](#why-do-you-need-to-integrate-omnisend-with-joy-loyalty-program) Benefits when integrate Klaviyo with Joy?

Klaviyo is a powerful email and SMS marketing automation tool designed for eCommerce businesses, including those on Shopify. When integrated with Joy Loyalty, this partnership empowers merchants to enhance their marketing strategies by leveraging loyalty program data to drive engagement and increase customer retention.

This collaboration helps you:

- **Streamline marketing**: Use real-time loyalty data to inform and automate email and SMS campaigns
- **Personalize customer engagement**: Enhance communications by tailoring messages based on loyalty insights
- **Improve customer retention**: Keep customers coming back by consistently highlighting rewards and program benefits
- **Save time**: Simplify marketing efforts with automated workflows triggered by loyalty activities
- **Create targeted campaigns**: Segment customers based on their loyalty tier or points balance for exclusive offers
- **Drive program engagement**: Automatically remind customers about expiring points or available rewards

With event triggers, your email marketing transitions from periodic campaigns to an ongoing conversation that responds directly to customer interactions with your loyalty program.

### [hashtag](#understanding-the-rule) **Understanding the Rule**

The integration between Joy Loyalty and Klaviyo allows seamless data synchronization, enabling merchants to include loyalty program details in their marketing efforts. Here's how it works:

1. **Data Flow**:

   - Klaviyo pulls essential loyalty program data from Joy Loyalty, such as points balance, membership status, VIP tiers, referral links, and birthdays.
   - This information becomes accessible for segmentation and personalization in Klaviyo.
2. **Use Cases**:

   - Create automated workflows to reward loyal customers or re-engage inactive ones.
   - Segment customers based on their loyalty tier or point balance for exclusive offers.

By integrating these tools, merchants can craft highly targeted campaigns that resonate with their audience while fostering loyalty and driving sales.

### [hashtag](#how-to-integrate) **How to integrate**

The very first step to integrate Joy successfully with Klaviyo is to allow API connection between the 2 apps. Follow the simple guide below to see how:

1

**Connect Joy to Klaviyo API**

- In **Step 1: Connect to Klaviyo API**, click on the `Connect`button
- Review carefully the **data** that **Klaviyo** will have access to
- Click `Allow`to finish connecting

2

**Sync Joy customer data to Klaviyo**

- In **Step 2: Sync data**, click on the `Connect`button to allow customer data sync from Joy to Klaviyo
- Check in Klaviyo's end to see customer's profile is now filled with loyalty data, including:

  - `Joy Loyalty Points`
  - `Joy member status`
  - `Joy Referral URL`
  - `Joy Vip tier`
  - `Shopify Tags`

circle-exclamation

This process may take a long time if you have over 100,000 customers in Joy Loyalty, primarily due to the [Klaviyo API's throttlingarrow-up-right](https://developers.klaviyo.com/en/v1-2/docs/rate-limits-and-error-handling).

3

**Set up automation triggers**

- Click on `Select triggers` to set up automation triggers
- Tick on events that you need, and `Confirm` to start sending triggers to Klaviyo

#### [hashtag](#how-to-segment-customers-in-klaviyo-bonus) How to segment customers in Klaviyo (Bonus)

Segmenting customers with loyalty criteria means classifying customers based on loyalty conditions. For example, you can categorize customers by tier, such as segmenting Gold tier customers to send emails exclusively to this group.

1

**Head to List & segments**

- In the Klaviyo platform, open the `Audience` > `List & segments`
- Click on `Create new segment`

2

**Customize segment conditions**

- Add a name for the segment
- Add a condition, using the `Properties about someone` condition type
- Select Joy's properties, including: Joy member status, Joy Referral URL, Joy Vip tier
- Enter value *(e.g. Joy Vip tier equals to "Gold")*

3

**Save the segment**

- Click `Create segment` to save and use for email campaigns *(e.g. monthly newsletter)*

### [hashtag](#how-to-create-event-based-automations-in-klaviyo) How to create event-based automations in Klaviyo

The **essence of creating automated workflows:** Create workflows that include loyalty program information in your email content. For example, you can send emails notifying customers about their points balance, sharing referral links, or tier details directly within the email.

Building workflows with loyalty program details is simple—just use variables and integrate them into your email content appropriately. For instance, the example below demonstrates creating a workflow:

1

**Log in to Klaviyo**

Log in to your Klaviyo account

2

**Create workflow**

Navigate to **Flows** > **Create Flow** to start creating your event-based flow

3

**Select trigger event**

- Start with `Select a trigger` menu, click on the `Your metrics` option
- Choose the `API` option as the Joy Loyalty event folders. You'll see all the Joy Loyalty events you've enabled
- Select the specific events (refer to [Joy and Klaviyo](/integrations/email-marketing-and-sms/joy-and-klaviyo#available-trigger-events) for detailed information) you want to use as a trigger for the workflow and click `Add`

4

**Customize emails**

Design your email workflow using Klaviyo editor

Utilize event data in your email content to personalize messages

Set the workflow to active when ready

### [hashtag](#example-automation-workflows) Example automation workflows

Here are powerful automation workflows you can create with the Joy Loyalty triggers:

chevron-rightPoints redemption reminder[hashtag](#points-redemption-reminder)

**Trigger**: Joy: Points Eligible Reward
**Purpose**: Alert customers when they have enough points for rewards
**Content**: Show available rewards and provide a clear redemption path
**Benefit**: Increases redemption rates and program engagement

chevron-rightTier advancement celebration[hashtag](#tier-advancement-celebration)

**Trigger**: Joy: Tier Achieved
**Purpose**: Congratulate customers on reaching a new tier
**Content**: Highlight new tier benefits and exclusive offers
**Benefit**: Reinforces the value of loyalty program progression

chevron-rightTier retention reminder[hashtag](#tier-retention-reminder)

**Trigger**: Joy: 4 Weeks Pre Tier Reset
**Purpose**: Notify customers who are at risk of losing their current tier
**Content**: Show current status, requirements to maintain tier, and benefits of keeping status
**Benefit**: Motivates additional purchases to maintain tier status

chevron-rightPoint expiration warning series[hashtag](#point-expiration-warning-series)

**Triggers**: Joy: 30 Days Pre Point Expiration → Joy: 7 Days Pre Point Expiration → Joy: 3 Days Pre Point Expiration
**Purpose**: Create a sequence of increasingly urgent reminders about expiring points
**Content**: Show expiring points amount and suggest redemption options
**Benefit**: Reduces point wastage and drives redemption activity

chevron-rightBirthday campaign sequence[hashtag](#birthday-campaign-sequence)

**Triggers**: Joy: 7 Days Pre Birthday → Joy: Birthday
**Purpose**: Build anticipation for birthday rewards and then deliver them
**Content**: Teaser message followed by birthday reward details
**Benefit**: Creates a memorable loyalty moment and strengthens emotional connection

chevron-rightReferral thank you[hashtag](#referral-thank-you)

**Trigger**: Joy: Point Referrers
**Purpose**: Thank customers who have successfully referred friends
**Content**: Show points earned and encourage additional referrals
**Benefit**: Reinforces referral behavior and acknowledges customer advocacy

### [hashtag](#trigger-events) Trigger events

The following events can be used to trigger automations in Klaviyo:

#### [hashtag](#birthday-events) Birthday Events

Event Name

Description

Joy: 7 Days Pre Birthday

Triggered 7 days before a customer's birthday

Joy: Birthday

Triggered on a customer's birthday

#### [hashtag](#point-events) Point Events

Event Name

Description

Joy: Points Eligible Reward

Triggered when customer has enough points to redeem a reward

Joy: Redeem Points

Triggered when customer redeems points

Joy: POS Point Redemption

Triggered when customer redeems points at POS

Joy: Earn Point

Triggered when customer earns points

Joy: Upon Point Expiration

Triggered when customer points expire

Joy: 30 Days Pre Point Expiration

Triggered 30 days before customer points expire

Joy: 7 Days Pre Point Expiration

Triggered 7 days before customer points expire

Joy: 3 Days Pre Point Expiration

Triggered 3 days before customer points expire

#### [hashtag](#referral-events) Referral Events

Event Name

Description

Joy: Coupon Referrers

Triggered when referrer receives a coupon reward

Joy: Point Referrers

Triggered when referrer receives points reward

Joy: Referral Friend

Triggered when a referred friend makes their first purchase

#### [hashtag](#tier-events) Tier Events

Event Name

Description

Joy: 4 Weeks Pre Tier Demotion

Triggered 4 weeks before customer tier demotion

Joy: 2 Weeks Pre Tier Demotion

Triggered 2 weeks before customer tier demotion

Joy: 1 Day Pre Tier Demotion

Triggered 1 day before customer tier demotion

Joy: Tier Downgrade

Triggered when customer tier is downgraded

Joy: 4 Weeks Pre Tier Reset

Triggered 4 weeks before customer tier reset

Joy: 2 Weeks Pre Tier Reset

Triggered 2 weeks before customer tier reset

Joy: 1 Day Pre Tier Reset

Triggered 1 day before customer tier reset

Joy: Tier Reset

Triggered when customer tier is reset

Joy: Tier Achieved

Triggered when customer achieves a new tier

#### [hashtag](#milestone-events) Milestone Events

Event Name

Description

Joy: Milestone Achieved

Triggered when a customer reaches a milestone

#### [hashtag](#member-anniversary-events) Member anniversary Events

Event Name

Description

Joy: Member Anniversary

Triggered on the anniversary of the customer's membership date

Joy: 7 Days Pre Member Anniversary

Triggered 7 days before the anniversary of the customer's membership date

#### [hashtag](#submit-receipt-events) Submit receipt Events

Event Name

Description

Joy: Approved submit receipt

Triggered when submitted receipt is approved

Joy: Reject submit receipt

Triggered when submitted receipt is rejected

### [hashtag](#event-properties) Event properties

Use the following `event|lookup` variables inside Klaviyo’s Flow Builder. These let you display dynamic data from each Joy Loyalty event.

#### [hashtag](#points-event-properties-earn-redeem-pos-redemption) Points Event Properties (Earn, Redeem, POS Redemption)

Property

Klaviyo Syntax

Example

Program name

`{{ event|lookup:'Program name'|default:'' }}`

Earn point program

Discount code

`{{ event|lookup:'Discount code'|default:'' }}`

SAVE10

Earned points

`{{ event|lookup:'Earned points'|default:'' }}`

10 points

Created at

`{{ event|lookup:'Created at'|default:'' }}`

2025-01-30T13:17:41Z

Redeemed points

`{{ event|lookup:'Redeemed points'|default:'' }}`

50 points

Point expired

`{{ event|lookup:'Points expire'|default:'' }}`

10 points

Expired at

`{{ event|lookup:'Expired at'|default:'' }}`

2025-12-31

#### [hashtag](#tier-event-properties-achieved-downgrade-reset) Tier Event Properties (Achieved, Downgrade, Reset)

Property

Klaviyo Syntax

Example

New tier name

`{{ event|lookup:'New tier name'|default:'' }}`

Gold

Old tier name

`{{ event|lookup:'Old tier name'|default:'' }}`

Silver

Current tier name

`{{ event|lookup:'Current tier name'|default:'' }}`

Platinum

Amount to next tier

`{{ event|lookup:'Amount to next tier'|default:'' }}`

100

Is Highest Tier

`{{ event.isHighestTier|default:'' }}`

False

Level up rule

`{{ event.typeCalculator|default:'' }}`

Point earned, Money spent, Number of orders

#### [hashtag](#birthday-events-1) Birthday Events

Property

Klaviyo Syntax

Example

Birthday

`{{ event|lookup:'Birthday'|default:'' }}`

07/12

Reward type

`{{ event.rewardType|default:'' }}`

Point, Coupon, Multiple Rewards

Reward value

`{{ event.reward|default:'' }}`

100, JOY-ABCDEF

#### [hashtag](#referral-event-properties-coupon-referrers-point-referrers-referral-friend) Referral Event Properties (Coupon Referrers, Point Referrers, Referral Friend)

Property

Klaviyo Syntax

Example

Earned points (referrer only)

`{{ event|lookup:'Earned points'|default:'' }}`

10 points

Reward type

{{ event.rewardType|default:'' }}

Point, Coupon, Store redit

Reward value

{{ event.reward|default:'' }}

100, JOY-ABCDEF, 10.5

#### [hashtag](#milestone-event-properties) Milestone Event Properties

Property

Klaviyo Syntax

Example

Milestone name

{{ event|lookup:'Milestone name'|default:'' }}

Number of order #1

Milestone rewards

{{ event.Reward|default:'' }}

10 points

#### [hashtag](#member-anniversary-event-properties) Member anniversary Event Properties

Property

Klaviyo Syntax

Example

Reward

{{ event.Reward|default:'' }}

10 points

circle-info

Notes

- All events include common customer properties like email, name, points, and ID.
- Some fields, such as **Program name** and **Discount code,** may appear in multiple event types.
- Test events may contain different values than live data.
- Date formats:

  - Timestamps use ISO 8601 (`YYYY-MM-DDTHH:mm:ssZ`)
  - Standard dates use `YYYY-MM-DD`
  - Birthdays use `MM/DD`

### [hashtag](#faq) FAQ

**Q: Which loyalty events can trigger Klaviyo automations?**
A: Joy Loyalty sends many events to trigger automations including point earnings, redemptions, tier changes, upcoming tier resets, birthdays, point expirations, and referral activities. The full list can be viewed and configured in your Joy Loyalty integration settings.

**Q: Do I need to set up the triggers in both Joy Loyalty and Klaviyo?**
A: Yes. You need to enable the triggers you want in the Joy Loyalty integration settings, then create corresponding automation workflows in Klaviyo that use these triggers as starting points.

**Q: How do I access loyalty data in Klaviyo email templates?**
A: You can use variables such as `{{ event|lookup:'Customer points'|default:0 }}`, and others, depending on the trigger event. These variables are available in the Klaviyo email editor.

**Q: How quickly are loyalty events sent to Klaviyo?**
A: Events are transmitted to Klaviyo in real-time as they occur in your loyalty program, allowing for immediate email communications.

**Q: How do I troubleshoot if an expected email isn't being triggered?**
A: First verify the trigger is enabled in Joy Loyalty, then check that the corresponding workflow is active in Klaviyo. Also confirm the test customer has a valid email address and hasn't unsubscribed from marketing emails.

### [hashtag](#wrap-up) Wrap up

And that's it! Your integration between Joy Loyalty and Klaviyo is now all set and ready to save your marketing efforts. If you run into any issues or have questions along the way, don't hesitate to reach out to our 24/7 live chat support. We're always here and happy to assist you!

[PreviousEmail Marketing & SMSchevron-left](/integrations/email-marketing-and-sms)[NextJoy and Sendlanechevron-right](/integrations/email-marketing-and-sms/joy-and-sendlane)

Last updated 7 hours ago

Was this helpful?