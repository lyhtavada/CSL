---
category: Customers
problem: One customer has two separate accounts in the app (one for online, one for POS/offline)
source: notion
---

Q: One of my customers has two different accounts in the Joy app -- one from online orders and one from POS. Why did this happen and how can I merge them?
Q: A customer placed orders both online and in-store, but Joy shows them as two separate people with different point balances. Can you help?
Q: I noticed duplicate customer profiles in my loyalty program. The same person has two accounts with different points. How do I fix this?
Q: My customer has two loyalty accounts -- one was created from their online purchases and another from in-store POS purchases. How can I combine them into one?
Q: Why does Joy treat my online customer and POS customer as two different people when it's actually the same person?

A: This happens because of how Shopify handles customer records. When a customer shops online and in-store (via POS), Shopify may create two separate customer IDs if the information doesn't match exactly -- for example, if the email used online is different from the phone number used at the POS. Since Joy syncs directly with Shopify's customer data, it recognizes these as two different customers.

Here's what you can do:

1. **Verify it's the same person** -- Confirm that both accounts truly belong to the same customer by cross-checking their name, email, and phone number across both profiles.
2. **Understand the root cause** -- Shopify generates separate customer IDs when the identifying information (email or phone) doesn't match between online and POS transactions. This is a Shopify-level behavior, not a Joy-specific issue.
3. **Request a merge** -- If you'd like to combine both accounts into one, let us know. Our development team can merge the two customer profiles so that their points and history are consolidated under a single account.
4. **After merging** -- Once the accounts are merged on the Shopify side, Joy will automatically sync the updated customer data. The customer will then see their combined point balance and reward history in one place.

To prevent this in the future, encourage customers to use the same email address both online and in-store.

Escalate khi: Merchant requests account merging (requires dev team intervention).
