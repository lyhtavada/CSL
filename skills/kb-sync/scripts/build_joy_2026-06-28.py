#!/usr/bin/env python3
"""
build_joy_2026-06-28.py — KB-patch payloads for Joy Loyalty (joy-loyalty-agent).
REVIEW-GATE run: build payloads JSON only. Do NOT push / kb_api / reindex.

Pattern: start from CACHED live file (/tmp/kb-sync/joy/<flattened>), assert each
anchor/occurrence BEFORE replacing, emit FULL new file content per changed file.
"""
import json
import os

APP = "joy"
AGENT = "joy-loyalty-agent"
DATE = "2026-06-28"
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(
    f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")


def rd(flat_name):
    return open(os.path.join(SRC, flat_name)).read()


results = {}  # real path -> new full content

# =====================================================================
# OUTDATED 1 — Q10 decimal VIP multiplier → vip-tiers.md
# =====================================================================
f = rd("kb__reference__vip-tiers.md")
old_vip = ("A VIP tier can carry a **points-earning multiplier** as a perk, so higher tiers earn points faster "
           "(for example Bronze 1pt/$1, Silver 1.5×, Gold 2×). Configure it as a tier privilege; the storefront "
           "shows the earning rate for the customer's current logged-in tier.")
assert f.count(old_vip) == 1, f"vip old paragraph count = {f.count(old_vip)}"
new_vip = ("A VIP tier can carry a **points-earning multiplier** as a perk, so higher tiers earn points faster "
           "(for example Bronze 1pt/$1, Silver 2×, Gold 3×). Configure it as a tier privilege; the storefront "
           "shows the earning rate for the customer's current logged-in tier. "
           "The **Bonus Points** perk accepts **whole multipliers only** (2×, 3×, 4×) — fractional rates such as "
           "1.25× or 1.5× are not available in this field. When a merchant needs a fractional per-tier rate, bridge "
           "it with **Shopify Flow** (segment members by tier tag → award a calculated point amount per order). "
           "Decimal multipliers are logged as product feedback.")
f = f.replace(old_vip, new_vip, 1)
results["kb/reference/vip-tiers.md"] = f

# =====================================================================
# OUTDATED 2 — Q38 ReCharge auto-detected (no API-key connection) → integrations-subscription.md
# =====================================================================
g = rd("kb__reference__integrations-subscription.md")

old_list = "- **Recharge** (full integration with discount sync)"
assert g.count(old_list) == 1, f"recharge list item count = {g.count(old_list)}"
new_list = "- **Recharge** (auto-detected from Shopify subscription orders — discount-code sync + subscription rewards)"
g = g.replace(old_list, new_list, 1)

old_connect = "Connect at **Joy Admin → Integrations → Recharge**."
assert g.count(old_connect) == 1, f"recharge connect line count = {g.count(old_connect)}"
new_connect = (
    "ReCharge is now **auto-detected from Shopify subscription orders** — there is nothing to \"connect\" on the "
    "Joy side. The old API-key connection (Joy Admin → Integrations → Recharge) was deprecated.\n\n"
    "Deprecating that old API connection briefly disrupted the discount-code sync; it has since been restored and "
    "patched. If a Joy discount code is created on Shopify but does not appear on ReCharge, collect the **code + the "
    "order** so the team can verify the sync.")
g = g.replace(old_connect, new_connect, 1)
results["kb/reference/integrations-subscription.md"] = g

# =====================================================================
# GAP — Q8 points awarded late (webhook delay) → settings-order.md
# insert AFTER the awaiting/display-points area (before the next "---")
# =====================================================================
s = rd("kb__reference__settings-order.md")
anchor_s = ("Note: this is display-only — actual award still happens at fulfillment. For **true holding period** "
            "with anti-fraud, use **Pending Points** (kb_points-advanced).")
assert anchor_s in s, "settings-order awaiting-points anchor missing"
gap_s = ("""

## Points may post later than expected (Shopify webhook delay)

Points fire from a **Shopify webhook** sent when the order reaches the configured status (Paid or Fulfilled). That webhook can be delayed on **Shopify's side** — sometimes **40–90 minutes** — so points may post later than the merchant expects. This is most painful for **in-store POS**, where the customer wants to redeem immediately at the counter.

For repeated delays, collect the **order number + order time + when points actually posted** and escalate. The real-time-points-at-POS case is logged as product feedback.""")
s = s.replace(anchor_s, anchor_s + gap_s, 1)
results["kb/reference/settings-order.md"] = s

# =====================================================================
# GAP — Q20 monthly accounting export → customers.md (near Export paragraph)
# =====================================================================
c = rd("kb__reference__customers.md")
anchor_c = ("**Export.** The default export may not include the **VIP tier column** — the team can enable tier in "
            "the export on request. A tier-only file can be re-imported to bulk-update tiers without touching "
            "points. A full programmatic API export is **Ultimate**.")
assert anchor_c in c, "customers Export paragraph anchor missing"
gap_c = ("""

**Accounting export (Customer Name + Order ID + Points Earned).** There is no self-serve dashboard export that combines Customer Name + Order ID + Points Earned in a single file, but the **team can generate it on request** for a given period — each line maps customer → order ID → points earned, suitable for monthly expense/accounting reporting. The native **Activities** log is the self-serve interim view in the meantime.""")
c = c.replace(anchor_c, anchor_c + gap_c, 1)
results["kb/reference/customers.md"] = c

# =====================================================================
# PARTIAL — Q6 guest "order recorded" + pre-order full-points → case/points-earning.md
# add to the first case's Common Causes / Resolution area; insert before its Escalation
# =====================================================================
p = rd("kb__case__points-earning.md")
anchor_p = ("- **Step 5:** If settings and order data match expected behavior but points still missing, escalate to "
            "team to investigate and append `<escalate_human>` to the reply.")
assert anchor_p in p, "points-earning Step 5 anchor missing"
partial_p = ("""
- **Step 6:** Check the activity log wording. If it shows **"order recorded"** (instead of **"placed order"**), the buyer was a **guest** at that moment and is not yet eligible — they earn those points once they **create or log into an account with the same email**.
- **Step 7:** For **partial / deposit (pre-order)** orders, Joy awards the **full** points **once**, when the order becomes **Paid** — it does not split points across the deposit and the balance installments.""")
p = p.replace(anchor_p, anchor_p + partial_p, 1)
results["kb/case/points-earning.md"] = p

# =====================================================================
# PARTIAL — Q12 + Q25 → reference/points-advanced.md (ONE entry, two additions)
# Q12: Limit customer earning + max points per order (near Pending points)
# Q25: store-credit mechanics (store-credit section near "Store credit shown across the storefront")
# =====================================================================
a = rd("kb__reference__points-advanced.md")

# --- Q25: store-credit mechanics ---
anchor_a_sc = "- **In the Unified widget**, customize it on the **Balance card**: choose the design style, show or hide the store credit value, etc."
assert anchor_a_sc in a, "points-advanced store-credit balance-card anchor missing"
q25 = ("""

## Store credit mechanics

- **Calculated on the order subtotal** — shipping and tax are excluded. To also exclude gift cards from the earning base, add an **Advanced condition** on the rule.
- **Rate is simplified by default** — Joy reduces the displayed rate to its simplest form (e.g. 2 credits per $100 shows as 1 per $50). The **"don't simplify"** checkbox changes the **display only**, not the actual earning rate.
- **Rounding** — with the **Nearest** rounding option, a small order can round down to **$0**. To issue exact fractional amounts, enable **decimal store credit**.
- **Per-VIP-tier store-credit rates** are supported (set a different rate on each tier).
- **"Failed to adjust store credit"** error — re-grant access (re-run the Grant Access / Confirm step above).""")
a = a.replace(anchor_a_sc, anchor_a_sc + q25, 1)

# --- Q12: limit points earned per period ---
anchor_a_pp = ("Enable at **Joy Admin → Settings → Additional Features → Pending Points → Turn on**, then set the "
               "waiting period (e.g., 8 days). Pending points don't redeem and don't count toward tier status "
               "until they convert.")
assert anchor_a_pp in a, "points-advanced Pending points anchor missing"
q12 = ("""

## Limiting how many points a customer can earn

A hard cap on a customer's **total point balance** is not supported. To cap **how much they can earn**, use:
- **Limit customer earning** (Advanced) at **Settings → Additional features** — caps the maximum points a customer can earn within a chosen **timeframe**.
- **Maximum points per order** on the **Place order** program — caps the points awarded on any single order.""")
a = a.replace(anchor_a_pp, anchor_a_pp + q12, 1)
results["kb/reference/points-advanced.md"] = a

# =====================================================================
# PARTIAL — Q14 redeem-in-line 3rd-party cart + redeem entire balance → reference/cart-drawer.md
# =====================================================================
d = rd("kb__reference__cart-drawer.md")
anchor_d = "- For Shopify Plus stores, pair with checkout-page Quick Redeem for full coverage"
assert anchor_d in d, "cart-drawer notes anchor missing"
q14 = ("""
- **Redeem in line** binds to Shopify's **native cart drawer** selectors, so it won't auto-work with **third-party slide-cart apps** (e.g. qikify) or some page builders (e.g. PageFly). For those themes, support can add the **matching CSS selector** for the theme's cart button so the redeem control attaches correctly.
- To let customers **redeem their full balance at once**, set the redeem program to **Dynamic discount** and clear (or raise) the **Maximum points per redemption** field — that field only appears in **Dynamic** mode.""")
d = d.replace(anchor_d, anchor_d + q14, 1)
results["kb/reference/cart-drawer.md"] = d

# =====================================================================
# PARTIAL — Q39 Customer Hub / C:Hub blank loyalty panel → reference/integrations-other.md
# C:Hub is a chat/inbox-style integration → add after the Chatty/Gorgias block (before first "---")
# =====================================================================
o = rd("kb__reference__integrations-other.md")
anchor_o = "Both available on **all plans**. Connect at **Joy Admin → Integrations → [Chatty or Gorgias]**."
assert anchor_o in o, "integrations-other Chatty/Gorgias anchor missing"
q39 = ("""

## Customer Hub (C:Hub) — blank loyalty panel

The Joy × **Customer Hub (C:Hub)** integration surfaces the loyalty profile inside C:Hub. The loyalty panel can show up **blank** when the dynamic button is clicked. To fix, collect **store access** and escalate to tech to repair the binding (log the case where it stays unresolved).""")
o = o.replace(anchor_o, anchor_o + q39, 1)
results["kb/reference/integrations-other.md"] = o

# =====================================================================
# PARTIAL — Q41 no native repeat-purchase-rate-by-tier report → reference/analytics.md
# soften the existing "Retention by tier" native-report line + add caveat
# =====================================================================
an = rd("kb__reference__analytics.md")
old_ret = "- **Retention by tier** — repeat-purchase rate Bronze vs Silver vs Gold"
assert an.count(old_ret) == 1, f"analytics retention-by-tier line count = {an.count(old_ret)}"
new_ret = "- **Retention by tier** — there is **no native repeat-purchase-rate-by-VIP-tier report** today (logged as feedback); use the workaround below"
an = an.replace(old_ret, new_ret, 1)

anchor_an = ("- For ShopifyQL: ready-made templates ship in the Joy docs — no need to write queries from scratch")
assert anchor_an in an, "analytics ShopifyQL requirements anchor missing"
q41 = ("""

## Repeat-purchase rate by tier (not native yet)

There is **no native report** for repeat-purchase rate broken down by VIP tier — it is logged as product feedback. Workaround: use the **"Returning customers – Joy active redeemers"** metric in **Shopify Analytics**, combined with **auto-tagging active redeemers** (**Settings → Additional features**). Note that **Member-Analytics** figures may be **temporarily unstable** during the current analytics revamp.""")
an = an.replace(anchor_an, anchor_an + q41, 1)
results["kb/reference/analytics.md"] = an

# =====================================================================
# write payloads
# =====================================================================
ops = [{"agent": AGENT, "path": p, "content": content}
       for p, content in results.items()]
json.dump(ops, open(OUT, "w"), ensure_ascii=False, indent=None)
print(f"wrote {len(ops)} payloads -> {OUT}")
total = 0
for op in ops:
    b = len(op["content"].encode("utf-8"))
    total += b
    print(f"  {op['path']}: {b} bytes")
print(f"total content bytes: {total}")
print(f"file size: {os.path.getsize(OUT)} bytes")
