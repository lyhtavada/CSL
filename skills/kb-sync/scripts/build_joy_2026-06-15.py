#!/usr/bin/env python3
"""Build kb-sync payloads for Joy (Joyce) — window 2026-06-15 → 2026-06-21.
Scope: Legacy-Pro note in pricing + full GAP/PARTIAL (Q18 skipped per Liz).
"Pro" is the LEGACY plan (customers who installed before 2023), NOT a rename of
Advanced — so no Pro->Advanced edits. Insert new ## sections at unique anchors,
match KB voice, no negative examples."""
import json, os

APP, AGENT, DATE = "joy", "joy-loyalty-agent", "2026-06-15"
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")

def rd(flat): return open(os.path.join(SRC, flat)).read()
def patch(flat, anchor, new, where="before"):
    """Insert `new` before/after `anchor` (must be unique). Returns new content."""
    f = rd(flat)
    assert f.count(anchor) == 1, f"anchor not unique/found in {flat}: {anchor!r} ({f.count(anchor)}x)"
    return f.replace(anchor, (new + anchor) if where == "before" else (anchor + new), 1)

results = {}

# ============ pricing.md — Legacy Pro note (grandfathered) ============
anchor = "**Existing subscribers (subscribed before Feb 9, 2026)** keep their previous rate **permanently** — grandfathered pricing."
note = """**Legacy "Pro" plan:** "Pro" is a **legacy plan** held by merchants who installed Joy before 2023. It is no longer offered to new merchants, but legacy Pro subscribers keep it. When a feature is listed as available on "Pro, Advanced, Ultimate," that includes these grandfathered Pro merchants — it is not a renamed Advanced plan.

"""
results["kb/reference/pricing.md"] = patch("kb__reference__pricing.md", anchor, note, "before")

# ============ Q30 GAP — Unified widget overlaps mobile checkout ============
# append new case at EOF (## Related/- kb_widget repeats 5x, not unique)
sec = """

## Unified widget float button overlaps the mobile checkout button

**Symptoms:** On mobile, the Joy floating button overlaps the store's checkout / add-to-cart button, or the merchant reports the **Unified** widget loading slowly on mobile. Some merchants temporarily switch back to the **Classic** widget because of this.

**Resolution Steps:**
- **Step 1:** Reposition the launcher — **Settings → Launcher → Alignment** and adjust position/offset so it clears the checkout button.
- **Step 2:** Use page-hide rules to hide the widget on cart/checkout pages where it conflicts.
- **Step 3:** If the merchant prefers, they can switch back to **Classic** while the issue is logged.
- **Step 4:** For pixel-precise placement, collect a screenshot + device + page URL and escalate to the team to apply targeted CSS via collaborator access. Append `<escalate_human>` to the reply.
"""
fw = rd("kb__case__widget.md")
assert "## Unified widget float button" not in fw
results["kb/case/widget.md"] = fw.rstrip() + "\n" + sec

# ============ Q36 GAP — storefront console error / Missing Key ============
# append at EOF (Step-4 line is duplicated, not unique)
sec = """
## Storefront console error / redirect / "Missing Key" / analytics issue

**Symptoms:** Merchant reports a JavaScript console error on the storefront (e.g. on Add to cart), an unexpected redirect, a Google Analytics tracking issue, a "Missing Key" message, the app pixel showing as disconnected, or sections rendering only their titles.

**Resolution Steps:**
- **Step 1:** Collect the store URL, the exact page/action, and a screenshot of the console error.
- **Step 2:** Note these are usually theme/snippet/Liquid or configuration issues — some are merchant-side theme errors, not Joy itself.
- **Step 3:** If the app pixel is involved, check **Settings → Customer Events** to confirm Joy is enabled.
- **Step 4:** Request temporary collaborator / theme access if investigation is needed, escalate to the team, and ask the merchant to revoke access afterward. Append `<escalate_human>` to the reply.
"""
fe = rd("kb__case__errors.md")
assert "## Storefront console error" not in fe
results["kb/case/errors.md"] = fe.rstrip() + "\n" + sec

# ============ Q39 GAP — customer used/generated unofficial Joy codes (fraud) ============
anchor = """## Related
- kb_integrations-shopify-flow
- kb_redeeming-programs
- Reference: https://help.joy.so/integrations/integrate-with-shopify-flow/shopify-flow-store-credit"""
sec = """## Customer used or generated Joy discount codes that were not officially issued

**Symptoms:** A customer redeemed or generated Joy discount codes that were never officially issued, or appears to have found a loophole to create valid codes.

**Resolution Steps:**
- **Step 1:** Treat this as a security issue. Collect the customer email and the specific order / discount codes involved.
- **Step 2:** Escalate to the team so they can investigate and close the loophole at the source. Append `<escalate_human>` to the reply.
- **Step 3:** For prevention going forward, the merchant can rely on one-time-use codes (default), per-customer redemption limits, minimum-order requirements, and **Pending Points** (Advanced, Ultimate) to hold points through the return window.

"""
results["kb/case/points-redeeming.md"] = patch("kb__case__points-redeeming.md", anchor, sec, "before")

# ============ Q8 GAP — per-tier points-earning rate ============
anchor = "Discount code prefix must follow `ABCD-` format."
sec = """## Per-tier points-earning rate

A VIP tier can carry a **points-earning multiplier** as a perk, so higher tiers earn points faster (for example Bronze 1pt/$1, Silver 1.5×, Gold 2×). Configure it as a tier privilege; the storefront shows the earning rate for the customer's current logged-in tier.

The alternative mechanism is a **segment-targeted earning rule** in the Rule engine (Customer segment → Bonus for VIP tier or tagged customers) when you want finer targeting.

> If the earning value shown in the popup does not match the tier setting, collect the customer email + tier + a screenshot and escalate — a display mismatch has been logged to tech before.

"""
results["kb/reference/vip-tiers.md"] = patch("kb__reference__vip-tiers.md", anchor, sec, "before")

# ============ Q21 PARTIAL — redeeming can demote points-based tiers ============
# add to same vip-tiers.md, in the Tier calculation rules block. Re-read patched content.
f = results["kb/reference/vip-tiers.md"]
anchor21 = "| **Number of orders** | Reward repeat purchase frequency |"
assert f.count(anchor21) == 1
add21 = anchor21 + """

> Redeeming/spending points lowers the active points balance and can **demote** a customer on **Points earned** tiers. To keep redemption from demoting customers, use **Amount spent** (cumulative spend is not reduced by redemptions) or assign protected customers to an **Exclusive tier**."""
results["kb/reference/vip-tiers.md"] = f.replace(anchor21, add21, 1)

# ============ Q16 + Q17 PARTIAL — import "non-existent customers", 0-point import, export tier col ============
anchor = "**Adjusting points does NOT change tier status** — tiers update only through VIP rules or manual tier change in customer profile."
sec = anchor + """

**Import matches on email already in Shopify.** The "Non-existent customers" error means an email in the CSV does not yet exist as a Shopify customer — customers must exist in Shopify first, and the email must match exactly (no typos or extra spaces). Re-importing the same file **updates existing customers (matched by email), it does not create duplicates**, so there is no need to delete the current list first.

**Orders imported at 0 points / retro backfill.** If past orders imported without points, the team can delete and re-add points with the correct rule — confirm the date range and which customers already had manual points first, to avoid double-crediting.

**Export.** The default export may not include the **VIP tier column** — the team can enable tier in the export on request. A tier-only file can be re-imported to bulk-update tiers without touching points. A full programmatic API export is **Ultimate**."""
results["kb/reference/customers.md"] = patch("kb__reference__customers.md", anchor, sec, "after")

# ============ Q5 PARTIAL — signup/welcome bonus not awarded ============
# append a case to points-earning.md before its final ## Related (line ~118 area).
anchor = """## Related"""  # NOT unique — points-earning has many. Use last block's unique text instead.
# Use the Case B escalation tail as anchor:
f = rd("kb__case__points-earning.md")
anchor5 = "## Resolution Steps - Case B: First Order = App logic via Shopify Flow"
assert f.count(anchor5) == 1
sec5 = """## Signup / welcome bonus points not awarded

**Symptoms:** A customer signed up but the signup/welcome bonus points were not added.

**Common Causes:**
- The customer did not complete the exact signup action tied to the bonus.
- The customer is not logged into a customer account with that email.
- The program was in **Sandbox**, not live, when they signed up.

**Resolution Steps:**
- **Step 1:** Confirm the signup program is live (not Sandbox) and the customer logged in with the bonus email.
- **Step 2:** If everything checks out, add the points manually via **Customers → adjust points**.
- **Step 3:** For repeated misses, escalate with the affected customer emails.

"""
results["kb/case/points-earning.md"] = f.replace(anchor5, sec5 + anchor5, 1)

# ============ Q22 PARTIAL — referral test mode + same-browser false negative ============
anchor = """## Anti-cheat"""
sec = """## Common false negatives when testing

- **"Running in test mode" message** means the referral program is in **Sandbox / preview** — go live for real rewards to be issued.
- **Same PC / same browser:** on a device where the merchant is logged into their own store, the referral page may show only the code without prompting for a friend's email. Test in incognito, another account, or a phone to see the real behaviour.

"""
results["kb/reference/referral.md"] = patch("kb__reference__referral.md", anchor, sec, "before")

# ============ Q29 PARTIAL — pause without canceling (Sandbox) ============
anchor = "## Refund Eligibility"
sec = """## Pause instead of cancel

If a merchant wants to pause rather than cancel, two options: downgrade to **Free** (config + points are retained), or **pause earning** by putting programs in **Sandbox** and turning notifications off. Both keep their data intact.

"""
results["kb/reference/billing-refund.md"] = patch("kb__reference__billing-refund.md", anchor, sec, "before")

# ============ Q9 PARTIAL — subscription renewals need Flow bridge ============
anchor = "## Related"  # not unique across file? integrations-subscription has one ## Related at 56
f = rd("kb__reference__integrations-subscription.md")
assert f.count("## Related") == 1
sec9 = """## Subscription renewals from non-native apps need the Flow bridge

Shopify does not natively pass subscription **renewal** data to apps. For subscription apps that are not natively integrated (e.g. Seal, BOLD, Subi), connect **Shopify Flow** (Settings → Integrations) and import the **"Joy Loyalty - Subscription Order Data Sync.flow"** template — then renewals earn points like one-time orders. See kb_milestone and kb_integrations-shopify-flow.

"""
results["kb/reference/integrations-subscription.md"] = f.replace("## Related", sec9 + "## Related", 1)

# ============ Q4 PARTIAL — points tracked on all plans ============
anchor = "**Legacy \"Pro\" plan:**"  # we just added this; insert before it in pricing
f = results["kb/reference/pricing.md"]
assert anchor in f
add4 = """**All plans track points.** Every plan (including Free/Starter and Essential) tracks point earning, holding, and redemption — the plan changes the order quota and which advanced features are available, not whether points work.

"""
results["kb/reference/pricing.md"] = f.replace(anchor, add4 + anchor, 1)

# ============ Q7 PARTIAL — earn only on full-price, exclude sale items ============
anchor = '## Conditions ("Check if")'
sec = anchor + """

**Recipe — earn only on full-price items (exclude sale items):** keep sale items in a dedicated collection (e.g. "SALE"), set the Place-order rule's product condition to **exclude** that collection, and mirror the same restriction on the redeeming program's **Applicable categories** so redemption doesn't stack on discounted items.
"""
results["kb/reference/earning-programs.md"] = patch("kb__reference__earning-programs.md", anchor, sec.replace(anchor, "", 1), "after")

# ============ Q10 PARTIAL — trust-based earning (visit/social/Google) not awarded ============
# add to earning-programs fraud-prevention area; use unique "## Fraud prevention"
f = results["kb/reference/earning-programs.md"]
anchor10 = "## Fraud prevention"
assert f.count(anchor10) == 1
sec10 = """## Trust-based earning not awarded (visit / social / Google review)

For Visit website, social, Instagram, and Google review programs, the customer must be **logged in** when performing the action. **Google review** points sit in a **pending/approval queue** the merchant must approve before they are granted. **Instagram** needs an IG Business/Creator account connected and the customer's IG username linked.

"""
results["kb/reference/earning-programs.md"] = f.replace(anchor10, sec10 + anchor10, 1)

# ============ Q14 PARTIAL — reorder redemption options ============
anchor = "## Important block notes"
sec = anchor + """

**Reordering Ways to redeem:** the order of redeeming programs is controlled in the **Reward programs** menu — drag to reorder them (e.g. lowest → highest points). If the merchant tells us the desired order, the team can reorder them on request.
"""
results["kb/reference/loyalty-page.md"] = patch("kb__reference__loyalty-page.md", anchor, sec.replace(anchor, "", 1), "after")

# ============ Q15 PARTIAL — large files + high-volume Sales hand-off ============
anchor = "## Import vs Migrate"
sec = """## Large files & high-volume stores

- Files **larger than 10 MB** can't go through chat — ask the merchant for a Google Drive / Dropbox link instead.
- For high-volume stores (10k+ orders) considering Ultimate, route to **Sales** for a custom quota / discount.

"""
results["kb/reference/migration.md"] = patch("kb__reference__migration.md", anchor, sec, "before")

# ============ Q20 PARTIAL — tier perk on POS / reward given twice ============
f = rd("kb__case__vip-tiers.md")
anchor20 = """## Resolution Steps
- """  # not unique. Use the perk-missing Symptoms block's first ## Related as anchor.
anchor20 = """## Related"""
# vip-tiers case has multiple ## Related; append a new case before the LAST one.
parts = f.rsplit("## Related", 1)
assert len(parts) == 2
sec20 = """## Tier perk not applying on POS, or a tier reward granted twice

**POS:** if a per-tier discount/perk applies on web but not on **Shopify POS**, run a live test logged in as a tier member through cart → checkout on both web and POS, then escalate with the exact flow, customer email, and tier.

**Reward granted twice:** if a customer received the same tier reward twice (and possibly used both), collect the customer email + order and escalate so the team can check whether others were affected and remediate. (This is distinct from the intended re-grant after a downgrade/re-upgrade.)

## Related"""
results["kb/case/vip-tiers.md"] = parts[0] + sec20 + parts[1]

# ============ Q25 PARTIAL — POS customer accessing same account online (no password) ============
anchor = "## Customer Accounts (new)"
sec = anchor + """

A customer added in-store (**POS**) reaches the same loyalty account online by logging in with the **same email** — with New Customer Accounts they use the email / one-time-code flow (no password to set). In-store and online activity tie to the same email and the same points balance.
"""
results["kb/case/customers.md"] = patch("kb__case__customers.md", anchor, sec.replace(anchor, "", 1), "after")

# ============ Q26 PARTIAL — birthday choose-gift + POS can't capture ============
anchor = "## Method 1 — Registration form"
sec = """## Limitations & options

- **Choose the gift:** when several birthday gift options are configured, a setting lets the customer pick one from the set.
- **POS can't capture birthdays:** Shopify POS does not capture a birthday at signup — customers add it in their Joy profile online (or via the registration form / metafields below).

"""
results["kb/reference/birthday.md"] = patch("kb__reference__birthday.md", anchor, sec, "before")

# ============ Q33 PARTIAL — VIP tier desc not translating + Classic->Unified carryover ============
anchor = "## Checkout limitation"
sec = """## Known limitations

- Translations entered on the **Classic** widget carry over when switching to **Unified** — no re-entry needed.
- Some strings, specifically **VIP tier descriptions inside Customer Accounts**, can show untranslated and may need manual entry; log a gap if a surface won't translate.

"""
results["kb/reference/translations.md"] = patch("kb__reference__translations.md", anchor, sec, "before")

# ============ Q34 PARTIAL — Flow coupon on combined conditions + delayed start ============
anchor = "## Common fields (every trigger)"
sec = """## Auto-issuing a coupon on order/spend conditions with a delayed start

A Flow can fire per-event to issue an exclusive coupon when conditions are met (e.g. 5 orders AND $200 spent). Note: a coupon's **validity window** controls when it can be *used*, not which orders *qualify* — qualifying by a date range is a separate Flow condition. Combining "X orders AND $Y spent AND only orders after a date" usually needs tuned Flow logic or tech-assisted setup; where Joy can't express the logic, log it as product feedback and offer the closest workaround (manually issue to a qualifying list).

"""
results["kb/reference/integrations-shopify-flow.md"] = patch("kb__reference__integrations-shopify-flow.md", anchor, sec, "before")

# ============ Q37 PARTIAL — customers got emails they didn't sign up for / GDPR ============
anchor = "## Internal Note"
sec = """## Customers received emails they never signed up for (incl. privacy/GDPR complaint)

**Resolution Steps:**
- **Step 1 (immediate):** turn the **global notification toggle off** to stop all Joy emails at once, then re-enable only the enrolled-member events you want.
- **Step 2:** check for a Sandbox-leak / notification-config cause (cross-ref Sandbox mode and the global notification controls).
- **Step 3 (privacy/GDPR):** escalate to the team immediately, confirm what was sent and to whom, and address the customer's data-handling concern. Treat as high-priority, not a routine deliverability ticket. Append `<escalate_human>` to the reply.

"""
results["kb/case/notifications.md"] = patch("kb__case__notifications.md", anchor, sec, "before")

# ---- write payloads ----
ops = [{"agent": AGENT, "path": p, "content": c} for p, c in results.items()]
json.dump(ops, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"wrote {len(ops)} payloads -> {OUT}")
for o in ops:
    print(f"  {o['path']}: {len(o['content'])} bytes")
