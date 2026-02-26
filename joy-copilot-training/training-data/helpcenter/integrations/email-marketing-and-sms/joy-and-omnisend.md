---
category: Integrations
subcategory: Email Marketing And SMS
topic: Joy And Omnisend
source: helpcenter
---

Q: What is Joy And Omnisend in Joy Loyalty?
Q: How do I set up Joy And Omnisend?
Q: How do I connect Joy And Omnisend with Joy Loyalty?
Q: Why is Joy And Omnisend not working?
A: **Who can connect Joy with Omnisend?**

- This feature is available for **All** plans.

### What is this feature

The Omnisend integration for Joy Loyalty allows you to synchronize your loyalty program data with your email marketing platform, enabling more targeted and effective communications. This integration has been enhanced with real-time event triggers that automatically send detailed loyalty event data to Omnisend when specific loyalty activities occur.

The integration works on two levels:

1. **Basic data synchronization**: Customer loyalty information, like points balance, tier status, and referral links, is made available in Omnisend for segmentation and personalization.
2. **Enhanced event triggers**: Real-time loyalty events are transmitted to Omnisend, allowing you to create automated email workflows based on specific loyalty activities.

### Why do you need to integrate Omnisend with Joy Loyalty Program?

Omnisend is a powerful email and SMS marketing automation tool designed for eCommerce businesses, including those on Shopify. When integrated with Joy Loyalty, this partnership empowers merchants to enhance their marketing strategies by leveraging loyalty program data to drive engagement and increase customer retention.

This collaboration helps you:

- **Streamline marketing**: Use real-time loyalty data to inform and automate email and SMS campaigns
- **Personalize customer engagement**: Enhance communications by tailoring messages based on loyalty insights
- **Improve customer retention**: Keep customers coming back by consistently highlighting rewards and program benefits
- **Save time**: Simplify marketing efforts with automated workflows triggered by loyalty activities
- **Create targeted campaigns**: Segment customers based on their loyalty tier or points balance for exclusive offers
- **Drive program engagement**: Automatically remind customers about expiring points or available rewards

With event triggers, your email marketing transitions from periodic campaigns to an ongoing conversation that responds directly to customer interactions with your loyalty program.

### **Understanding the Rule**

The integration between Joy Loyalty and Omnisend allows seamless data synchronization, enabling merchants to include loyalty program details in their marketing efforts. Here's how it works:

1. **Data Flow**:

   - Omnisend pulls essential loyalty program data from Joy Loyalty, such as points balance, membership status, VIP tiers, referral links, and birthdays.
   - This information becomes accessible for segmentation and personalization in Omnisend.
2. **Use Cases**:

   - Create automated workflows to reward loyal customers or re-engage inactive ones.

(See the full help center article for more details.)

---

Q: Which loyalty events can trigger Omnisend automations?
A: Joy Loyalty sends many events to trigger automations including point earnings, redemptions, tier changes, upcoming tier resets, birthdays, point expirations, and referral activities. The full list can be viewed and configured in your Joy Loyalty integration settings.

Q: Do I need to set up the triggers in both Joy Loyalty and Omnisend?
A: Yes. You need to enable the triggers you want in the Joy Loyalty integration settings, then create corresponding automation workflows in Omnisend that use these triggers as starting points.

Q: How do I access loyalty data in Omnisend email templates?
A: You can use variables such as `{{ event.pointsBalance }}`, `{{ event.tierName }}`, and others depending on the trigger event. These variables are available in the Omnisend email editor.

Q: How quickly are loyalty events sent to Omnisend?
A: Events are transmitted to Omnisend in real-time as they occur in your loyalty program, allowing for immediate email communications.

Q: How do I troubleshoot if an expected email isn't being triggered?
A: First verify the trigger is enabled in Joy Loyalty, then check that the corresponding workflow is active in Omnisend. Also confirm the test customer has a valid email address and hasn't unsubscribed from marketing emails.
