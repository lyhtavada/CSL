---
category: Membership
problem: Customer reached a new VIP tier but did not receive the entry reward
source: notion
---

Q: A customer just reached a new VIP tier but didn't get the entry reward. Why not?
Q: VIP entry reward is not being given to customers when they level up. What's wrong?
Q: Customer was promoted to a higher tier but never received the welcome reward. How do I fix this?
Q: Entry reward not working when customers reach a new membership tier. What should I check?
Q: Why didn't my customer get the entry reward after reaching the Gold VIP tier?
A: Here's how to troubleshoot when a customer doesn't receive their VIP tier entry reward:

1. **Verify that entry rewards are configured.** Go to Joy app > Membership > VIP Tiers and check that the relevant tier has an entry reward set up. Make sure the reward type, value, and conditions are all correct.

2. **Check when the entry reward was created vs. when the customer reached the tier.** This is a very common cause! Entry rewards are **not retroactive**. If the entry reward was created **after** a customer already reached that tier, the customer will **not** receive it automatically.

   - For example, if a customer reached Gold tier on January 1, but you added the Gold entry reward on January 15, that customer won't get the reward.
   - Only customers who reach the tier **after** the entry reward is set up will receive it.

3. **If the entry reward was created before the customer reached the tier** and the configuration is correct, but the customer still didn't receive it, this may be a technical issue.

4. **Workaround:** As a temporary solution, the merchant can manually adjust the customer's points or create a manual discount code to compensate.

Escalate khi: Entry reward was created before the customer reached the tier, configuration is correct, but the reward was still not delivered. Escalate to dev with customer email/ID, VIP tier, and the date the entry reward was created.
