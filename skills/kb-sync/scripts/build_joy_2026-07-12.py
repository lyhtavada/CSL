#!/usr/bin/env python3
"""build_joy_2026-07-12.py — payloads for the Jul 06-12 2026 kb-sync run (Joy).
Review-gate: writes payloads JSON only. No push, no reindex.
0 OUTDATED — all items are additive sub-points under existing anchors.
"""
import json, os

APP, AGENT, DATE = "joy", "joy-loyalty-agent", "2026-07-12"
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")


def rd(flat):
    return open(os.path.join(SRC, flat)).read()


def _find(lines, anchor):
    idx = [i for i, l in enumerate(lines) if l.strip() == anchor]
    assert len(idx) == 1, f"anchor {anchor!r}: found {len(idx)}x (need 1)"
    return idx[0]


def before(content, anchor, block):
    lines = content.split("\n")
    i = _find(lines, anchor)
    return "\n".join(lines[:i] + block.strip("\n").split("\n") + [""] + lines[i:])


def after(content, anchor, block):
    lines = content.split("\n")
    i = _find(lines, anchor)
    return "\n".join(lines[:i + 1] + [""] + block.strip("\n").split("\n") + lines[i + 1:])


results = {}

# Q10 GAP — gender/age at signup
results["kb/reference/birthday.md"] = after(rd("kb__reference__birthday.md"), "## Limitations & options",
"""- **Only birthday is collected — not gender or age:** Joy's registration form supports **birthday only** (via the register form or Shopify Customer Metafields). Neither Joy nor native Shopify captures gender or age at the moment of sign-up. To collect those, use a third-party custom-registration-fields app that syncs to Shopify customer profiles. If the goal is rewards, birthday is the built-in field and can drive automatic birthday rewards.""")

# Q13, Q16, Q18 — redeeming-programs.md
red = rd("kb__reference__redeeming-programs.md")
red = after(red, "## Redeem value modes",
"""> **Customer-side partial redemption:** after the customer clicks **Claim** on a redeem option, they can adjust **how many points to redeem** — no merchant-side change needed (e.g. redeem 200 pts for £2 instead of the base 100 pts for £1). To cap this, set **Maximum points per redemption** (Dynamic Discount mode only — fixed-discount mode has no per-redemption cap). Min-cart-value and dynamic-discount options require **Essential+**.""")
red = after(red, "## Selection modes",
"""> **Gift product must be published & active** on the Online Store channel to be redeemable — but it does **not** need to be visible. Hide it with a product template that has the "Add to Cart" button removed (do **not** keep it in draft, or redemption fails). Redemption generates a discount code, so inventory decreases normally per order — monitor stock.
>
> **Where auto-add works:** on the Unified widget / storefront the free gift **auto-adds to cart** when redeemed. Inside the Shopify **New Customer Accounts / Loyalty Hub** it only generates a **copyable code** — Shopify does not allow auto-add-to-cart or auto-apply there.""")
red = before(red, "## Discount types",
"""## Free gift on recurring subscription orders (Loop / Recharge)

Joy's **Free Gift** redemption supports **one-time orders only**. A generated free-gift code becomes invalid after its first use and isn't designed for recurring subscription contracts — applied to a Loop/Recharge recurring order it returns **"Invalid code."** Percentage/amount discount codes behave differently (they can sync to subscription orders). Auto-applying a free gift to the next subscription delivery has no native workaround today; log it as a feature request.""")
results["kb/reference/redeeming-programs.md"] = red

# Q23 GAP — milestone counting basis
results["kb/reference/milestone.md"] = before(rd("kb__reference__milestone.md"), "## Milestone types",
"""## What each milestone type counts (start date vs lifetime)

The counting basis differs by milestone type:

- **Amount spent** and **Earned points** milestones only count orders placed **on/after the program start date** — every customer starts fresh at launch.
- **Number of orders** milestones count the customer's **lifetime** Shopify order total. A customer with several past orders can therefore trigger the 2/3/4/6-order milestones **all at once** right after launch. There is no native option to restrict order-count milestones to post-launch orders (logged as a feature request).

**Recalculation note:** on large stores milestone recalculation can take several hours to 12+ hours. The "retroactive" checkbox only looks back to the **start date you set**, not all-time.""")

# Q35, Q36 — pos.md
pos = rd("kb__reference__pos.md")
pos = before(pos, "## Two versions",
"""## POS tile name is fixed

The POS tile title (**"Joy Loyalty"**) is the default and applies globally across the store — it **cannot** be renamed to a custom brand name. Add the tile via **help.joy.so/pos/add-joy-to-shopify-pos**. Note that at POS, points are awarded automatically once an order completes (no need to tap the tile); tapping the tile is only for previewing a balance, redeeming a reward, or completing a Custom Trigger.""")
pos = after(pos, "## Earning",
"""> **Per-location awarding not supported:** Joy does not currently track or award points based on purchases across specific POS locations, so there is no native way to award e.g. "100 points if the customer buys in all 3 stores" (logged as a feature request). A standard Place-order program works across all channels (POS + online) but cannot distinguish individual store locations.""")
results["kb/reference/pos.md"] = pos

# Q45 GAP — silent retroactive import
results["kb/reference/migration.md"] = before(rd("kb__reference__migration.md"), "## Large files & high-volume stores",
"""## Silent retroactive import (don't spam customers)

A retroactive sync **can fire emails** if the relevant notifications are on. Before importing, turn **OFF** the **"Points earned"** and **"VIP tier"** notifications, then re-enable them after.

- Points for past orders use the earning rules configured **at sync time** and apply each customer's **current tier multiplier**. To use the base rate for everyone, temporarily set all members to one tier / disable per-tier rates, then restore.
- Tier **entry rewards** are only granted for the tier a customer is assigned to (not every tier passed through) and can be kept off during import.
- **Requirements:** both the Rewards Program and the Place Order rule must be enabled, and the Place Order **start date must cover the historical orders**.
- The import **can't be tested on a single customer** and **can't be reversed** from the merchant's end — the team runs it for the store.""")

# Q44, Q63, Q64 — customers.md
cust = rd("kb__reference__customers.md")
cust = before(cust, "## Import customer data (CSV)",
"""## Bulk reset at relaunch (reset points / remove coupons / re-award by old tier)

The team handles these bulk actions. When removing existing coupons, clarify **revoke vs remove** first: **Revoke** deactivates the coupon **and refunds** the points back to the customer; **Remove** deactivates the coupon **without** refunding points. The team can also reset all balances to 0 and re-award fixed points by old VIP tier (a one-time bonus). VIP program can be turned off anytime by the merchant at **Membership → VIP tier program → Deactivate**. Large coupon-deactivation batches may need dev processing (hours). All bulk point/coupon changes appear in the customer's activity history and on the widget.""")
cust = after(cust, "## Setup",
"""> **Excluded / "Left program" customers on the account page:** excluding hides the widget for those customers but does **not** auto-zero existing points (adjust to 0 manually if needed). A known issue: excluded/"Left program" customers could still see Redeem/VIP **blocks on the account page** (Profile-page blocks didn't respect the status the way the widget did). This was flagged and fixed for Profile-page blocks — verify on the store. Note Exclude segments requires **Advanced+**.""")
cust = before(cust, "## Add customer inline (Shopify Admin Intents)",
"""## The "JOY-XXXX" discount tag on customer profiles

The `JOY-XXXX` tag is added automatically to track which customer used which coupon and to prevent code reuse. It is **not configurable from app settings** — there is no self-serve toggle to disable or shorten it (logged as a feature request; a hide / "show more" / shortened format is being explored). Joy does not otherwise auto-tag customers with discount tags, so if other unexpected tags appear, check Shopify Flow or another app.""")
results["kb/reference/customers.md"] = cust

# Q5 PARTIAL — Recharge webhook change (case file)
results["kb/case/points-earning.md"] = before(rd("kb__case__points-earning.md"), "## Signup / welcome bonus points not awarded",
"""## Subscription (Recharge) orders stopped earning after a Shopify webhook change

Shopify changed the subscription webhook property (`subscription_contract` -> `subscription_contract_checkout_one`). If subscription/Recharge orders stopped earning points, set the Place-order rule's purchase-location condition to **All channels** so subscription orders earn again. Past missed orders can be credited manually. Always collect email + order number and confirm member-vs-guest before escalating.""")

# Q19 PARTIAL — negative balance
results["kb/reference/points-advanced.md"] = after(rd("kb__reference__points-advanced.md"), "## Refund points (All plans)",
"""- **Balance can go negative.** If earned points were already redeemed and the order is later refunded with auto-revoke on, the deduction can push the balance **below zero**. Joy allows **system-created** negative balances (the customer earns their way back). You **cannot** manually set a balance below zero from admin — manual adjust is a goodwill/correction tool, not a penalty. For corrections set the balance to zero or a positive value; for genuine negative-balance scenarios escalate for a case-by-case workaround.""")

# Q22, Q25 — vip-tiers.md
vip = rd("kb__reference__vip-tiers.md")
vip = after(vip, "## Tier Assessment (rolling-window re-evaluation)",
"""> **Quarterly reset is not natively supported.** Reset/assessment cycle options do not include a quarterly reset (logged as feature research). For a "gift-with-purchase every quarter" goal, use a **Milestone program** (tracks cumulative spend toward a threshold, e.g. AUD $300; the qualifying order is tagged via Shopify Flow so the warehouse packs the gift — never added to cart, never a discount code) plus a cart-progress nudge ("$40 to go") on the account page.""")
vip = after(vip, "## Privilege types",
"""> **Perk-on-accumulated-points is not supported** — perks apply as ongoing benefits (free shipping, % discount, fixed amount) while the customer holds the tier, not on hitting a point threshold.
>
> **Shopify fixed-amount behavior:** a **fixed-amount** automatic discount restricted to specific products applies **per eligible item**, not once per order (e.g. $10 off x 7 items = $70). This is Shopify's native discount engine, not a Joy bug. For a true order-level cap, use a % discount or free shipping perk.""")
results["kb/reference/vip-tiers.md"] = vip

# Q28 PARTIAL — custom-domain referral link
results["kb/reference/referral.md"] = after(rd("kb__reference__referral.md"), "## Referral redirection URL",
"""> **Custom-domain referral links:** referral links can use your **custom domain** instead of the myshopify URL — each customer gets a unique link like `yourdomain.com?referralCode=xxxx`. The team switches this on request. Popup edit/disable lives under On-site content -> Widget -> Referrals. Auto-show frequency = times it auto-appears per visit (max 10); Display frequency = wait time before it reappears after being closed (30 min-30 days).""")

# Q38 PARTIAL — unsupported marketing apps
results["kb/reference/integrations-email.md"] = after(rd("kb__reference__integrations-email.md"), "## Supported",
"""> **Apps not on this list have no native sync.** Being a Shopify app on both sides does not guarantee integration. Examples with **no native Joy sync** today: **Spoks**, **Seguno**. New integration requests are logged as feature requests with no committed timeline — do not promise a date.""")

# Q39 PARTIAL — two IG accounts
results["kb/reference/earning-programs.md"] = after(rd("kb__reference__earning-programs.md"), "## Instagram programs (Advanced, Ultimate)",
"""> **You cannot run two separate "Follow on Instagram" rewards for two IG accounts.** The backend treats **"Instagram Follow" as one global action** — once a customer completes the first follow, a second follow program won't award. Workaround: a **Custom Program / Submit Form**. Also verify the follow link points to *your* IG profile (Reward programs -> Follow on Instagram) — it defaults to a placeholder.""")

# Q46 PARTIAL — App embed 0 Active glitch (case file — append new case block at end)
wid = rd("kb__case__widget.md").rstrip("\n")
wid += """

## Dashboard shows "App embed 0 Active" / "Inactive" though the widget is enabled

**Symptoms:** the Joy dashboard shows the embed as 0 Active / Inactive even though the widget displays fine on the storefront.

**Resolution Steps:**
- **Step 1:** Confirm the embed is on — **Online Store -> Themes -> Customize -> App embeds -> "Joy Loyalty - Widget" -> Save**, then hard-refresh the Joy dashboard (Cmd/Ctrl+Shift+R).
- **Step 2:** If it still shows 0 Active / Inactive despite displaying on the storefront, this is a **known dashboard display glitch** — the store works normally. Self-serve retry: toggle the embed off -> Save -> on -> Save -> reload the app.
- **Step 3:** If it persists, escalate; the team's dev fix corrects the status. (The App **Pixel** under Checkout -> Tracking is separate — it only relates to the Referral program and auto-connects when Referral is on.)
"""
results["kb/case/widget.md"] = wid + "\n"

ops = [{"agent": AGENT, "path": p, "content": c} for p, c in results.items()]
json.dump(ops, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"wrote {len(ops)} payloads -> {OUT}")
for o in ops:
    print(f"  {o['path']}: {len(o['content'])} bytes")
