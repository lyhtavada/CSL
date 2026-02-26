---
category: Reward programs
problem: Understanding birthday reward settings and why customers don't receive rewards
source: notion
---

Q: How do I set up birthday rewards in Joy, and why aren't my customers receiving them?
Q: My customer entered their birthday but didn't get the birthday reward. What happened?
Q: How does the birthday reward timing work in Joy?
Q: Why didn't a customer receive their birthday points even though they entered their birthday?
Q: Can you explain the birthday reward trigger settings and timing requirements?

A: Birthday rewards in Joy depend on **two key settings** that work together. Understanding both is important to figure out why a customer might not have received their reward.

### Setting 1: "Birthday allowed after" (DevZone)
This setting controls how many days **after entering their birthday** a customer becomes eligible for the birthday reward. The default is **30 days**. This prevents abuse (e.g., someone entering a fake birthday just to get an immediate reward).

### Setting 2: "When to reward" (Reward Program settings)
This controls **when** the birthday reward is actually sent:
- **Exact birthday date** -- reward is sent on the customer's actual birthday
- **Calendar month of birthday** -- reward is sent at the beginning of the birthday month
- **Around birthday** -- reward must be triggered manually by the merchant

### How These Two Settings Combine
Both conditions must be met for the reward to trigger. Here's an example:

- If the reward is set to **automatic** + **exact birthday date** + sent **7 days before** the birthday
- And "Birthday allowed after" is set to **30 days**
- Then the customer must enter their birthday at least **30 + 7 = 37 days** before their birthday

If a customer entered their birthday too close to the reward trigger date, they won't receive it this year. They'll be eligible next year.

### Quick Checklist
1. Check the "Birthday allowed after" value in DevZone.
2. Check the "When to reward" setting in the birthday reward program.
3. Calculate whether the customer entered their birthday early enough to qualify.
4. Verify the customer actually entered a valid birthday in their profile.
