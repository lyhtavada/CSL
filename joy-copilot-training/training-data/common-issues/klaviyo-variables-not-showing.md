---
category: Integrations
problem: Klaviyo variables not generating points or VIP data when previewing email content
source: notion
---

Q: I'm using Klaviyo with Joy, but the loyalty variables (like points balance and VIP tier) are not showing up when I preview my emails. What's wrong?
Q: Klaviyo is not pulling in my customers' point balances or VIP status into email templates. How do I fix this?
Q: The Joy Loyalty variables in my Klaviyo email preview are blank or showing errors. How can I troubleshoot this?
Q: I integrated Joy with Klaviyo but the personalization variables for loyalty points and VIP tier aren't populating. What should I check?
Q: My Klaviyo emails are supposed to show customer point balances from Joy, but the data isn't appearing. Can you help?

A: When Klaviyo variables for Joy Loyalty data (points, VIP tier, etc.) are not displaying correctly, it's usually related to data sync, API configuration, or profile-level issues. Let's troubleshoot step by step:

**Step 1: Identify the affected profile**
Find a specific customer/profile where the issue is occurring. Note their email address so we can trace the data.

**Step 2: Check customer info in Joy**
Go to **Joy > Customers** and search for that customer. Verify that their points balance and VIP tier data are correct within the Joy app itself.

**Step 3: Verify the Klaviyo integration status**
In your Joy admin, go to **Integration > Klaviyo** and make sure the integration shows as **connected** and active. If it shows as disconnected or has a warning, the data may not be syncing properly.

**Step 4: Check the Klaviyo profile**
Open the customer's profile in Klaviyo and look for the custom properties related to Joy (such as points balance, VIP tier, etc.). Take a screenshot of the profile properties for reference.

**Step 5: Re-generate the API key if needed**
If the integration appears incomplete or was set up a while ago:
1. In Klaviyo, generate a **new private API key** with the appropriate permissions.
2. Go back to **Joy > Integration > Klaviyo** and re-enter the new API key.
3. Save and allow time for the data to re-sync.

**Step 6: Test again**
After re-integrating, send a test email or preview a Klaviyo flow to see if the Joy variables now populate correctly. Note that it may take a few minutes for data to fully sync.

If the issue persists after completing all the steps above, please share screenshots of both the Joy customer profile and the Klaviyo profile so we can escalate to our development team for further investigation.

Escalate khi: Variables still not populating after re-generating the API key and re-integrating. Dev team investigation required.
