circle-info

This feature is available for: **Professional, Advanced, and Enterprise plans**

### [hashtag](#what-is-zigpoll-integration-via-shopify-flow) What is [Zigpollarrow-up-right](https://www.zigpoll.com/) Integration via Shopify Flow

Zigpoll Integration via Shopify Flow allows you to automatically reward customers with loyalty points when they complete surveys created with Zigpoll. This integration uses Shopify Flow's automation capabilities to trigger point awards based on survey completion events, creating a seamless connection between your feedback collection and loyalty program.

The integration works by setting up a Flow automation that listens for Zigpoll survey completion events and automatically awards points to customers through Joy Loyalty's API, encouraging more customers to participate in your surveys and providing valuable feedback.

### [hashtag](#why-you-should-use-this-integration) Why you should use this integration

Customer feedback is invaluable for business growth, but getting customers to complete surveys can be challenging. By integrating Zigpoll with your loyalty program through Shopify Flow, you create a win-win situation where customers are incentivized to provide feedback in exchange for loyalty points.

This integration helps increase survey response rates significantly, as customers see immediate value in participating. The automated nature of the integration means you don't need to manually track survey completions or award points, saving time while ensuring consistent reward distribution. Additionally, the points earned from surveys can drive customers back to your store to redeem their rewards, creating a positive feedback loop that benefits both customer satisfaction and business growth.

### [hashtag](#setting-up-a-fill-out-a-survey-program-in-joy) Setting up a "Fill out a survey" program in Joy

1

**Get access to "Fill out a survey"**

Choose **Reward programs** -> **Earning programs** -> Click **Add rule** -> Choose **Fill out a survey**

2

**Set up "Fill out a survey"**

**a. Program Information**

- **Program Name**: Choose a clear and attractive name
- **Description**: Provide context
- **Survey Link**: Insert the survey URL

Survey apps embed links on store pages, like checkout. To maximize responses, retrieve survey links directly. Here’s how (using Zigpoll as an example):

**b. Program Rule**

Click on **Create Shopify flow** and follow our guide to create a flow connecting survey completion to reward distribution

Ensure the flow syncs loyalty points automatically to prevent manual errors

circle-check

**Pro Tip**: Test the flow to ensure smooth functionality, then press **Publish to store front**

### [hashtag](#setting-up-zigpoll-integration-via-shopify-flow) Setting up Zigpoll Integration via Shopify Flow

1

**Access Shopify Flow**

- From your Shopify admin, go to **Apps**
- Click on **Shopify Flow**
- Click **Create workflow** to start building your automation

2

**Set up the trigger (Zigpoll survey completion)**

- In the Flow builder, click **Add trigger**
- Search for and select **Zigpoll** from the available triggers
- Choose **Survey completed** as the trigger event
- Configure trigger settings:

  - Select specific surveys to track (or all surveys)
  - Set any conditions for survey completion (optional)
- Click **Save** to confirm the trigger

3

**Add conditions (optional)**

You can add conditions to filter when points are awarded:

1. Click **Add condition** below the trigger
2. Available conditions might include:

   - Customer email exists (to award points only to registered customers)
   - Survey type or category
   - Response quality metrics (if available)
   - Customer segment or tags
3. Configure your desired conditions and click **Save**

4

**Set up the action (Award Joy Loyalty points)**

- Click **Add action** after your trigger (and conditions if added)
- Search for and select **Joy Loyalty** from available actions
- Choose **Award points** as the action type
- Configure the point award settings:

  - **Customer**: Map to the survey respondent's email or customer ID
  - **Points amount**: Set how many points to award (e.g., 50 points)
  - **Activity name**: Create a descriptive name (e.g., "Survey Completion")
  - **Reference**: Add survey name or ID for tracking (optional)
- Click **Save** to confirm the action

### [hashtag](#advanced-configuration-options) Advanced configuration options

#### [hashtag](#multiple-point-values-for-different-surveys) Multiple point values for different surveys

Create separate workflows for different survey types:

1. **Product feedback surveys**: Higher points (e.g., 100 points)
2. **Quick polls**: Lower points (e.g., 25 points)
3. **Detailed reviews**: Premium points (e.g., 200 points)

#### [hashtag](#limiting-rewards-per-customer) Limiting rewards per customer

Add conditions to prevent point farming:

1. Use customer tags to track survey participation
2. Add conditions to limit rewards to once per survey
3. Set up time-based restrictions (e.g., one survey reward per week)

#### [hashtag](#dynamic-point-calculations) Dynamic point calculations

Use Flow's variables to award points based on:

1. Survey completion percentage
2. Response quality or length
3. Customer tier status from Joy Loyalty

### [hashtag](#best-practices) Best practices

#### [hashtag](#survey-design-considerations) Survey design considerations

- **Keep surveys focused**: Shorter surveys with appropriate point rewards work better
- **Set clear expectations**: Tell customers upfront how many points they'll earn
- **Vary reward amounts**: Match point values to survey complexity and importance

#### [hashtag](#communication-strategy) Communication strategy

- **Announce the integration**: Let customers know they can earn points for surveys
- **Include point values**: Show point rewards in survey invitations
- **Thank customers**: Send follow-up communications acknowledging their participation

#### [hashtag](#technical-maintenance) Technical maintenance

- **Regular testing**: Periodically test the Flow to ensure it's working correctly
- **Monitor errors**: Check Flow logs for any failed point awards
- **Update conditions**: Adjust workflows as your survey strategy evolves

### [hashtag](#faqs) FAQs

#### [hashtag](#can-i-reward-points-for-partially-completed-surveys) Can I reward points for partially completed surveys?

This depends on Zigpoll's available triggers. Most integrations reward points only for fully completed surveys, but check Zigpoll's Flow trigger options for partial completion events.

#### [hashtag](#will-customers-see-immediate-point-updates) Will customers see immediate point updates?

Points are typically awarded within a few minutes of survey completion. Customers will see the points in their Joy Loyalty account and receive notifications if enabled.

#### [hashtag](#can-i-customize-the-point-activity-name-that-appears-in-customer-accounts) Can I customize the point activity name that appears in customer accounts?

Yes, when setting up the Joy Loyalty action in Flow, you can customize the activity name that will appear in the customer's point history.

#### [hashtag](#what-happens-if-a-customer-completes-the-same-survey-multiple-times) What happens if a customer completes the same survey multiple times?

By default, they would receive points each time unless you add conditions to prevent this. Most merchants use customer tags or Flow conditions to limit rewards to one per survey.

#### [hashtag](#can-i-integrate-this-with-other-survey-apps-besides-zigpoll) Can I integrate this with other survey apps besides Zigpoll?

Yes, Shopify Flow supports many apps with survey capabilities. The setup process is similar - look for the survey app's triggers in Flow and connect them to Joy Loyalty's point award action.

[PreviousShopify Flow: Store creditchevron-left](/integrations/integrate-with-shopify-flow/shopify-flow-store-credit)[NextTranslationschevron-right](/translations)

Last updated 19 days ago

Was this helpful?