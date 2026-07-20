#!/usr/bin/env python3
"""
build_joy_2026-07-19.py — build KB patch payloads for joy-loyalty-agent from the
mined FAQ file joy_2026-07-13_2026-07-19.md.

Every operation asserts its anchor exists, so a moved heading fails loudly.
Output: reports/analysis/kb-sync-joy-2026-07-19-payloads.json
"""
import json
import os

AGENT = "joy-loyalty-agent"
CACHE = "/tmp/kb-sync/joy"
OUT = os.path.expanduser(
    "~/CSL/reports/analysis/kb-sync-joy-2026-07-19-payloads.json")

files = {}


def load(path):
    if path not in files:
        flat = path.replace("/", "__")
        with open(os.path.join(CACHE, flat), encoding="utf-8") as fh:
            files[path] = fh.read()
    return files[path]


def sub(path, old, new, count=None):
    text = load(path)
    n = text.count(old)
    assert n > 0, f"ANCHOR MISSING in {path}: {old[:80]!r}"
    if count is not None:
        assert n == count, f"{path}: expected {count} of {old[:50]!r}, found {n}"
    files[path] = text.replace(old, new)


def insert_before(path, heading, block):
    text = load(path)
    assert heading in text, f"ANCHOR MISSING in {path}: {heading!r}"
    files[path] = text.replace(heading, block.rstrip() + "\n\n" + heading, 1)


def append(path, block):
    files[path] = load(path).rstrip() + "\n\n" + block.rstrip() + "\n"


# ---------------------------------------------------------------------------
# OUTDATED
# ---------------------------------------------------------------------------

# 1. Decimal per-tier multipliers now go through Rule Engine, not Shopify Flow
sub("kb/reference/vip-tiers.md",
    "When a merchant needs a fractional per-tier rate, bridge it with "
    "**Shopify Flow** (segment members by tier tag → award a calculated point "
    "amount per order). Decimal multipliers are logged as product feedback.",
    "When a merchant needs a fractional per-tier rate such as **1.5×**, use "
    "the **Rule Engine**: upgrade the Earning program to Rule Engine (under "
    "**More actions** on the Earning programs page), then add a **Place order** "
    "rule with the decimal rate targeted at that tier. Rule Engine is available "
    "on **Advanced and Ultimate**. Shopify Flow is not needed for this.",
    count=1)

# 2. Sign-up backfill is self-serve now (2 files told agents to escalate)
sub("kb/reference/earning-programs.md",
    "If the merchant wants existing/older customers to earn it too, this "
    "requires an internal adjustment — **escalate to the team** "
    "(do not promise a self-serve setting).",
    "If the merchant wants existing/older customers to earn it too, they can "
    "run it themselves from **Settings → Pre-launch → Sync Sign Up**. Our team "
    "can also run it for them. Ask whether they want notifications suppressed "
    "so the backfill doesn't email every customer.",
    count=1)
sub("kb/case/points-earning.md",
    "or — if the merchant wants all existing customers to earn it — escalate "
    "to the team and append `<escalate_human>` (do not promise a self-serve "
    "toggle for this).",
    "or — if the merchant wants all existing customers to earn it — point them "
    "to **Settings → Pre-launch → Sync Sign Up**, which they can run "
    "themselves. Our team can run it instead if they prefer. Ask whether "
    "notifications should be suppressed so the backfill doesn't email everyone.",
    count=1)

# 3. Cart drawer redemption is Essential+, not Advanced+
#    (kb/reference/cart-drawer.md already says Essential — pricing table is the
#    only wrong copy)
sub("kb/reference/pricing.md",
    "| Cart drawer redemption | ❌ | ❌ | ✅ | ✅ |",
    "| Cart drawer redemption | ❌ | ✅ | ✅ | ✅ |", count=1)

# 4. Analytics plan gate — file contradicted itself (line 42 + pricing.md agree
#    on Essential+)
sub("kb/reference/analytics.md",
    "Available on **All plans**. Open at **Joy Admin → Analytics**.",
    "Available on **Essential and above**. Open at **Joy Admin → Analytics**.",
    count=1)

# 5. Referral popup toggle IS in the Popups tab; only the design lives elsewhere
sub("kb/reference/onsite-content.md",
    "- The **Referral popup** is NOT in the Popups tab — it lives under "
    "**Widget → Referrals** (see above).",
    "- To **turn the referral invite popup off**, go to **Joy Admin → On-site "
    "content → Popups** and toggle it off. Its **design** is configured "
    "separately under **On-site content → Widget → Referrals → Setup**.",
    count=1)

# 6. Trial length is 14 days Essential/Advanced, 30 days Ultimate
sub("kb/case/billing.md",
    "- Trial lasts 14 days; usage is recorded but not charged during trial.",
    "- Trial lasts **14 days** (Essential/Advanced) or **30 days** (Ultimate); "
    "usage is recorded but not charged during trial.", count=1)
sub("kb/case/billing.md",
    "- Therefore the usage period and Shopify billing cycle are offset by "
    "14 days.",
    "- Therefore the usage period and the Shopify billing cycle are offset by "
    "the length of that trial.", count=1)

# 7. Classic widget is deprecated and switching back discards the Unified design
sub("kb/case/widget.md",
    "- **Step 3:** If the merchant prefers, they can switch back to "
    "**Classic** while the issue is logged.",
    "- **Step 3:** Switching back to **Classic** is a last resort, not a "
    "neutral option — Classic is being **deprecated** and won't receive new "
    "features, and switching back **discards the current Unified design**. "
    "Say so before doing it.", count=1)

# 8. Klaviyo — coupon_name now exists; and person|lookup is not the only format
sub("kb/reference/integrations-email.md",
    "- The coupon-reminder event carries the **coupon code** but "
    "**not the coupon name**.",
    "- The coupon-reminder event carries both the **coupon code** and the "
    "coupon's display name via `{{ event.coupon_name }}`.", count=1)
sub("kb/reference/integrations-email.md",
    "These are the only variables Joy supports for Klaviyo; do not suggest any "
    "other variable format.",
    "Profile data uses `person|lookup`; data carried by the triggering event "
    "uses `event|lookup` (see the event-properties section below). Those two "
    "are the only supported formats — do not suggest any other.", count=1)
sub("kb/case/integrations.md",
    "These are the only supported variables; do not suggest any other format.",
    "Data carried by the **triggering event** instead uses `event|lookup` — "
    "e.g. `{{ event|lookup:'Customer points'|default:'0' }}`. Using "
    "`person|lookup` for event data returns `n/a`. Those two are the only "
    "supported formats — do not suggest any other.", count=1)

# ---------------------------------------------------------------------------
# GAP / PARTIAL
# ---------------------------------------------------------------------------

# Q18 (~11) — the single most-reported redemption behaviour
sub("kb/reference/redeeming-programs.md",
    "When customers redeem, Joy generates a unique one-time-use coupon code.",
    "When customers redeem, Joy generates a unique one-time-use coupon code.\n\n"
    "**The code does not apply itself at checkout.** The points are spent and "
    "the code is valid, but nothing happens until the customer clicks **Apply** "
    "or pastes the code. This is the most common \"my discount didn't work\" "
    "report. Unused codes are always retrievable from the widget's "
    "**My coupons** section. Clicking **Apply** with an **empty cart** holds "
    "the discount until items are added, and the page may need a refresh.",
    count=1)

# Q13 (~8) — "Complete birthday info" reward absent entirely
insert_before("kb/reference/birthday.md", "## Related", """
## "Complete birthday info" reward (distinct from the Birthday reward)

**Complete birthday info** is a **separate earning reward**. It grants points
the moment a customer submits their birthday through the loyalty widget for the
first time — immediately, unrelated to the actual birthday date.

Do not confuse it with the **Birthday reward**, which fires on/near the
customer's birthday each year.

A bug that awarded 0 points on this program has been patched. Accounts that
already logged the activity **cannot re-trigger it** — add the points manually
and test with a fresh account.
""")

# Q13 — self-serve trigger button exists
sub("kb/case/birthday-reward.md",
    "**Merchant wants to reward now anyway**: ask our team to manually trigger "
    "the birthday reward for this customer — provide the customer email and "
    "escalate with `<escalate_human>`",
    "**Merchant wants to reward now anyway**: there is a **Trigger birthday "
    "reward** button in the customer's profile in Joy admin that the merchant "
    "can use themselves. If that fails, provide the customer email and escalate "
    "with `<escalate_human>`", count=1)
sub("kb/case/birthday-reward.md",
    "- **Step 2:** Tell the merchant our team will manually trigger the "
    "birthday reward for this customer.",
    "- **Step 2:** Point the merchant at the **Trigger birthday reward** button "
    "in the customer's profile in Joy admin — they can fire it themselves. If "
    "it doesn't work, our team can trigger it manually.", count=1)

# Q6 (~13) — conflicting rule conditions
insert_before("kb/reference/earning-programs.md", "## Calculation notes", """
## Order placed but no points — two silent blockers

Beyond the documented program conditions, two configurations stop earning with
no error shown anywhere:

- **Contradictory conditions on one rule** — e.g. sales channel set to
  *equals Online store* **and** *equals POS* on the same rule. No order can
  satisfy both, so nothing ever qualifies. Check each rule's conditions as a
  set, not individually.
- **An expired program end date** — earning stops silently the moment the end
  date passes. Check the program's start/end dates against the store timezone.
""")

# Q21 (~7) — fixed reward larger than cart
insert_before("kb/case/points-redeeming.md", "## Related", """
## Discount larger than the cart total breaks some third-party apps

A **fixed-amount** reward larger than the cart total reduces the order to
**$0**. Shopify permits this, but some third-party fee, bundle or checkout apps
throw a validation error at $0 and leave the checkout button unresponsive.

**Fix:** set a **minimum cart value** on the redeem program so the discount can
never exceed the order total.
""")

# Q31 (~7) — VIP start date is the top cause of tier resets
insert_before("kb/case/vip-tiers.md", "## Related", """
## Everyone's tier changed after launching or editing the VIP program

The most common cause is the **VIP tier program's start date**. Tier points are
only calculated from orders placed **on or after** that date — setting it to
today zeroes everyone's tier qualification.

**Fix:** set the start date back to the intended date and re-launch. Joy
recalculates tier points and reassigns customers. **Launching does not affect
point balances** — only tier qualification.

For large customer bases recalculation can take **several hours**; the
per-customer activity log shows progress.
""")

# Q43 (~22, largest topic) + Q42 (~9) — widget position / not showing
append("kb/case/widget.md", """
## Widget not showing on the storefront

Work through these in order — in recent cases #2 and #3 were far more common
than #1:

1. **App embed** — Shopify Admin → Online Store → Themes → Customize →
   App embeds → **Joy Loyalty - Widget** on → Save.
2. **Hide widget button / hidden on all devices** — On-site content → Widget →
   Advanced → Display settings.
3. **Display after login** — hides the widget from logged-out visitors.
4. **Customer eligibility = "Manually assigned customers only"** — restricts it
   to a hand-picked list.

**The "App embed 0 Active" / "Inactive" badge inside Joy can be inaccurate.**
It is synced from the theme and is thrown off by theme conflicts. It does
**not** stop points earning — if the activity log shows earning, treat the
badge as cosmetic.

## Launcher position — two things to check before treating it as a CSS request

- **The launcher jumps position after being tapped** — this is a *rendering*
  bug, not a positioning request. Collect device + OS and escalate for a fix
  rather than routing it to Launcher settings.
- **Confirm the overlapping element is actually Joy's.** Check the storefront
  first — in several cases this week the conflicting floating button belonged
  to another app, which Joy cannot move.

For pixel-precise placement, collect: screenshot or mockup, page URL, device
(and mobile OS), and the collaborator code.
""")

# Q57 — pixel "Disconnected": answer the merchant's real question
sub("kb/case/integrations.md",
    '## Joy app pixel shows "Disconnected" in Shopify Customer Events',
    '## Joy app pixel shows "Disconnected" in Shopify Customer Events\n\n'
    "**Lead with the reassurance:** Joy does **not** depend on customer-event "
    "tracking to award points. Order, sign-up and customer data come directly "
    "from Shopify, so points, balances and tiers are unaffected by pixel "
    "status — all that's needed is the program enabled and the app embed "
    "active. The pixel **is** used for **referral attribution**, so it only "
    "matters if referrals aren't tracking.", count=1)

# Q74 — permission buttons silently fail for non-owner accounts
append("kb/case/errors.md", """
## A permission button ("Grant access", "Grant Markets Access") does nothing

The action must be performed by the **store owner or a staff member with full
admin permissions** — Shopify silently blocks the request from a
limited-permission staff account, so the button appears to do nothing.

Suggested reply: "Permission grants have to come from the store owner or a
full-admin staff account. Could you ask the store owner to log into the Joy app
and click the button again? It should go through right away."

**Grant Markets Access** gives Joy access to Shopify Markets configuration,
which unlocks region-specific referral rewards. Without it, referral rewards by
region are unavailable.

If it still fails from a full-permission account, collect a screen recording
plus the collaborator code and escalate.
""")

# Q55 — suppressing notifications during a team-run bulk update
append("kb/case/notifications.md", """
## Suppressing notifications during a bulk update

When our team runs a bulk tier reassignment, points import or retroactive sync,
notifications **can be disabled for the duration** — but the merchant must flag
it **when requesting the work**, not afterwards.

This is a common and reasonable request: it avoids sending thousands of
"you've reached a new tier" emails in one batch.

The merchant-side equivalent is the global toggle at
**Settings → Notifications**.
""")

# Q62 (~8) — date-range point activity export
append("kb/reference/shopify-admin.md", """
## Export point activity over a date range

**Customers → Activities → set date range → Export type = Earned → enter your
email → Start export.** The file is emailed, typically within 5–10 minutes.

This is separate from the customer/points/tiers export button, which is enabled
per-store by our team.
""")

# Q39 — opt-in enrollment mechanics (only one KB line existed)
append("kb/case/customers.md", """
## Opt-in enrollment ("Join Program")

Enabling opt-in changes who earns, and merchants are repeatedly caught out by
it:

- **Enabling opt-in after launch retroactively converts already-signed-up
  customers into Guests.** This is the most common complaint — they stop
  earning until they join.
- **Points awarded before opt-in was enabled are not removed automatically.**
  Clearing them, or setting a true program start date, is a manual team pass —
  we need the exact date and scope.
- **Entry rewards do not retroactively fire** for customers who joined before
  the tier program went live. Also a manual pass.
- Shopify sends no reliable sign-up webhook under new customer accounts, so
  membership **cannot** be auto-restricted to deliberate account creators.
  Opt-in is the closest available control.
""")

# ---------------------------------------------------------------------------
payloads = [{"agent": AGENT, "path": p, "content": c}
            for p, c in sorted(files.items())]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(payloads, fh, ensure_ascii=False, indent=2)
print(f"Wrote {len(payloads)} file payload(s) -> {OUT}")
for p in sorted(files):
    print(f"  - {p}")
