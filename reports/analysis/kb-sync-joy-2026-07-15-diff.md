# KB patch diff — Joy tickets July review (G1,G5,G6,P2,P4,P5,P7,P8)

```diff
--- a/kb/case/vip-tiers.md
+++ b/kb/case/vip-tiers.md
@@ -92,5 +92,66 @@
 
 **Reward granted twice:** if a customer received the same tier reward twice (and possibly used both), collect the customer email + order and escalate so the team can check whether others were affected and remediate. (This is distinct from the intended re-grant after a downgrade/re-upgrade.)
 
+---
+
+## All customers suddenly dropped to the lowest tier (Bronze/Basic)
+
+**Symptoms**
+- Many/all customers were reset to the lowest tier at once, often right after the merchant changed tier thresholds, changed the calculation rule, re-launched VIP Tier, or imported a spend file.
+
+**What's happening (not data loss)**
+- Changing a threshold, changing the calculation metric, or re-launching VIP Tier makes Joy **re-run tier assessment for every customer against the new rule**. If the new threshold is higher than a customer's current value (e.g. Silver raised to $25k), most customers fall to the lowest tier. This is a re-assessment, not lost history.
+
+**Resolution Steps**
+- **Step 1:** Ask the merchant whether they just changed a threshold, changed the calculation rule (Points earned / Amount spent / Number of orders), re-launched tiers, or ran a tier import — and when.
+- **Step 2:** Confirm the metric in use. If it's **Amount spent** and customer spend has not fully synced from Shopify, tiers can be calculated on incomplete data.
+- **Step 3:** Check whether a **tier import file** was run in parallel (an import can overwrite tiers).
+- **Step 4:** If a threshold/rule change explains it, explain the re-assessment behavior. If the threshold did **not** change but tiers still reset en masse, or the merchant needs existing customers restored to their old tiers, escalate with: store URL, when it happened, old vs new thresholds, and a screenshot of the tier settings. Append `<escalate_human>`.
+
 ## Related
 - kb_vip-tiers
+- kb_points-advanced
+
+---
+
+## VIP tier points did not change after I reset / adjusted the point balance
+
+**Symptoms**
+- Merchant reset or adjusted customers' **point balance** (via CSV or manual adjust) but **VIP tier points** still reflect the old values, or tier points were added on top of the old balance.
+
+**Answer**
+- **VIP tier points** and **point balance** are two **separate** metrics. Adjusting or resetting the point balance does **not** automatically recalculate tier points — tier points keep their accumulated value unless recalculated separately. There is no self-serve toggle to re-sync tier points to a new balance.
+
+**Resolution Steps**
+- **Step 1:** Confirm the order of operations (e.g. reset points first, then enabled VIP Tier).
+- **Step 2:** Take one example customer (email): current point balance vs current tier points vs the expected value from the file.
+- **Step 3:** Escalate for the team to recalculate/re-import lifetime tier points from the source file, with: the original points file, the list of affected customers, and the reset timestamp. Append `<escalate_human>`.
+
+## Related
+- kb_vip-tiers
+- kb_points-earning
+
+---
+
+## Tier perk / privilege discount not auto-applying in cart for some customers
+
+**Symptoms**
+- A tier perk (auto discount, free product) applies for some customers in a tier but not others, or a Free-product perk can't be claimed / generates no code.
+
+**Common Causes**
+- Customer is not logged in to the correct account, or not actually in that tier.
+- Perk eligibility conditions are too narrow (minimum spend, product/collection eligibility, excluded items).
+- The cart already has another discount that isn't allowed to combine.
+- Free-product perk: the selected product is out of stock / no longer eligible, so no code is generated.
+- Privilege perks require **Advanced+**.
+
+**Resolution Steps**
+- **Step 1:** Confirm the customer is logged in to the right account and is genuinely in the tier.
+- **Step 2:** Check the perk's eligibility/display conditions and that the cart product is eligible with no conflicting discount (check Discount Combinations).
+- **Step 3:** For a Free-product perk, confirm the product is still eligible and in stock.
+- **Step 4:** Test live: log in as a tier member, add the product, go to cart → checkout; compare a customer where it works vs one where it doesn't.
+- **Step 5:** If setup is correct but the perk still applies to some customers and not others in the same tier (or a Free-product perk generates no code), escalate with two customer emails (works + doesn't-work), the tier, the product URL, and a screenshot of the perk setup. Append `<escalate_human>`.
+
+## Related
+- kb_vip-tiers
+- kb_redeeming-programs

--- a/kb/case/integrations.md
+++ b/kb/case/integrations.md
@@ -56,3 +56,26 @@
 - kb_integrations-email
 - kb_vip-tiers
 
+---
+
+## Joy app pixel shows "Disconnected" in Shopify Customer Events
+
+**Symptoms**
+- Under **Shopify → Settings → Customer Events** (or **Checkout Settings → Tracking and analytics → App pixels**), the Joy Loyalty pixel shows **Disconnected**.
+- Clicking **Connect** only redirects to the Joy dashboard and the pixel stays Disconnected.
+
+**Common Causes**
+- Joy's Web Pixel needs re-authorization (Shopify is asking for a newly-scoped grant).
+- There is no clear manual "connect" action in the current Shopify UI, so most cases need the team to recreate the pixel on the backend.
+
+**Resolution Steps**
+- **Step 1:** Confirm the exact location: **Shopify Checkout Settings → Tracking and analytics → App pixels** (or Customer Events) with Joy = Disconnected.
+- **Step 2:** Ask the merchant to **re-authorize the Joy app** (re-open the app / re-accept permissions) so Shopify grants the new scope, then re-check the status.
+- **Step 3:** If re-authorizing doesn't surface a connect option or the pixel is still Disconnected, escalate for the team to recreate the pixel, with: store URL, a screenshot of Customer Events, and a short video of the Connect button behavior if available. Append `<escalate_human>`.
+
+> Note: expect this to rise in volume around the Shopify checkout/customer-events migration deadline (Aug 2026) — treat repeated reports as the same known issue.
+
+## Related
+- kb_integrations-shopify-flow
+- kb_settings-developers
+

--- a/kb/reference/redeeming-programs.md
+++ b/kb/reference/redeeming-programs.md
@@ -92,6 +92,13 @@
 
 Unused coupons can be revoked and converted back to points by merchant on customer request — **Joy Admin → Customers → [name] → Revoke coupon**.
 
+### Deactivate a coupon WITHOUT refunding points
+
+**Revoke** always converts the unused coupon **back into points** — that is by design, and there is no toggle to "revoke without refund" and no bulk-deactivate in Joy.
+
+- To **disable a code but keep the points spent**, deactivate the code **directly in Shopify → Discounts** (do **not** use Joy's Revoke). Note: after deactivating in Shopify, the coupon's status inside Joy may not auto-update to Expired — if the merchant needs the app status synced, escalate.
+- To **deactivate many/all coupons at once without refunding** (e.g. before re-launching a new redeem program), there is no self-serve UI — escalate with the store URL and the list/criteria of coupons to disable. Append `<escalate_human>`.
+
 ---
 
 Both require **Shopify Plus + Checkout Extensibility** and **Ultimate** plan (Advanced via sales contact).

--- a/kb/reference/cart-drawer.md
+++ b/kb/reference/cart-drawer.md
@@ -32,6 +32,14 @@
 - **Redeem in line** binds to Shopify's **native cart drawer** selectors, so it won't auto-work with **third-party slide-cart apps** (e.g. qikify) or some page builders (e.g. PageFly). For those themes, support can add the **matching CSS selector** for the theme's cart button so the redeem control attaches correctly.
 - To let customers **redeem their full balance at once**, set the redeem program to **Dynamic discount** and clear (or raise) the **Maximum points per redemption** field — that field only appears in **Dynamic** mode.
 
+## Common request: "add the redeem block to my cart drawer"
+
+This is a frequent how-to. Handle it in this order:
+
+1. **Native Shopify cart drawer** → guide the Setup steps above (On-site content → Product page → Redeem in Cart Drawer → Edit in Theme Editor → enable **Joy: Redeem in line** → Save).
+2. **Third-party slide-cart / page builder** (e.g. **swatches-popup-cart**, **qikify**, **PageFly**) → the embed binds to native cart-drawer selectors and will **not** auto-attach. Ask which cart app the store uses, request **theme access + app permission** (`ref_collaborator-access-flow`), then escalate for the team to add the **matching CSS selector** for that theme's cart button. Append `<escalate_human>`.
+3. Same root cause covers "**entry/redeem coupon errors in the cart but applies fine at checkout**": reassure the merchant the coupon is still valid and **applies at checkout** — only the cart-drawer display needs the selector fix. Escalate as in step 2.
+
 ## Related
 - kb_redeeming-programs (configure redeem programs)
 - kb_widget (loyalty widget — alternative redemption path)

--- a/kb/reference/integrations-email.md
+++ b/kb/reference/integrations-email.md
@@ -95,6 +95,21 @@
 - **Sendlane** — API Token (from Sendlane → Account → API → Sendlane API V2). Pick a list to sync. Same fields as Drip
 - **PushOwl** — OAuth. Push-notification triggers for: 7 days before birthday, Birthday, Point expiration (7 + 3 days prior), Eligible for reward, Point activity (earned/redeemed)
 
+## Troubleshooting: Klaviyo events/variables
+
+**Joy events/metrics not showing in Klaviyo (need to re-add triggers)**
+- Confirm **Integrations → Klaviyo** is Connected. The available Joy metrics are `Joy: Earn Point`, `Joy: Redeem Points`, `Joy: Tier Achieved`, `Joy: Points Eligible Reward`, `Joy: Birthday`, `Joy: 7 Days Pre Point Expiration`.
+- If the metrics don't appear, **disconnect and reconnect** Klaviyo (generates a fresh API key) to re-stream events, then re-check.
+- Still missing after reconnect → escalate with store URL + screenshot of Klaviyo metrics. Append `<escalate_human>`.
+
+**Variable shows `n/a` or the wrong value in a Klaviyo email**
+- Almost always the wrong **lookup type**. Data sitting on the **profile** uses `person|lookup` (e.g. `{{ person|lookup:'Joy Loyalty Points'|default:'' }}`). Data carried by the **triggering event** (bonus points on an Earn/Tier flow) uses `event|lookup` (e.g. `{{ event|lookup:'Customer points'|default:'0' }}`). Using `person|lookup` for event data returns `n/a`.
+- Confirm the customer actually has the data in Joy and that the Klaviyo profile shows Joy properties. If syntax and data are correct but the value is still wrong, escalate with store URL + email preview + Klaviyo profile + Joy customer screenshots. Append `<escalate_human>`.
+
+**Known limitations (log as feature requests, don't promise a fix)**
+- The coupon-reminder event carries the **coupon code** but **not the coupon name**.
+- There is **no dedicated "Reward Expiring" Klaviyo event** — Joy syncs `coupon_expiry_date` as a profile property only.
+
 ## Related
 - kb_integrations-shopify-flow (Joy + Klaviyo via Flow workflow)
 - kb_settings-email (Joy default email vs marketing tool)

--- a/kb/case/points-earning.md
+++ b/kb/case/points-earning.md
@@ -131,7 +131,23 @@
 ## Escalation
 - Confirm logic and impact with merchant before triggering. Adjust legacy customer points on request.
 
+---
+
+## Order earned points at the old rate after the merchant changed the earning rate
+
+**Symptoms**
+- Merchant raised the earning rate (e.g. 1pt/$1 → 5pts/$1) but an order fulfilled today still earned at the old rate, or points that were pending at ×5 converted at ×1.
+
+**Answer**
+- Points are **locked at the rate in effect when the earn event was recorded** (when the order was placed / the earn record was created), **not** at the moment of fulfillment. An order **placed before** the rate change keeps the old rate even if it fulfills after — this is expected.
+
+**Resolution Steps**
+- **Step 1:** Confirm the new rate is **saved** and the program is **Live** (not Sandbox).
+- **Step 2:** Confirm the new rate only applies to orders **placed after** the change — orders placed before are expected to keep the old rate.
+- **Step 3:** If an order **placed after** the rate change still earns the old rate, escalate with the order number, customer email, the time the rate was changed, and a screenshot of the activity. Append `<escalate_human>`.
+
 ## Related
 - kb_earning-programs
 - kb_integrations-shopify-flow
 - kb_rule-engine
+- kb_points-advanced

--- a/kb/reference/points-advanced.md
+++ b/kb/reference/points-advanced.md
@@ -81,6 +81,16 @@
 
 Example for Full expiration set to 365: customer earns Jan 1 → expires Dec 31 unless they engage; new purchase June 1 extends all to next May 31.
 
+### Troubleshooting: points expired sooner than expected
+- Confirm which expiration type is on (Full inactivity / Fixed date / FIFO).
+- For **Full expiration**, the clock runs on the **last activity (earn OR spend)**, not the last order date, and it resets for the **whole** balance on any activity. A common cause of "expired too early" is that the setting was **turned on or changed earlier** and the merchant forgot, or the inactivity clock is measured from an **older earn**, not the most recent order.
+- Check the customer's activity log for the `expired` event date and compare it to the last activity. If the expiry date doesn't match any of the three logics above, escalate so the team can check the setting's history — append `<escalate_human>`.
+
+### Adjusting a customer's points has a floor of 0
+- You **cannot** push a balance **negative** — the minimum adjustment is **0**. If a merchant over-credited and needs to remove more than the customer currently has, they can only remove down to the current balance.
+- Adjusting a balance to **0** clears the available points for **that customer only** — it is not a shop-wide reset. Resetting points for **all** customers requires a CSV import / team tooling.
+- Adjusting the point balance does **not** re-sync **VIP tier points** (separate metric) — see kb_vip-tiers.
+
 ---
 
 ## Refund points (All plans)
```
