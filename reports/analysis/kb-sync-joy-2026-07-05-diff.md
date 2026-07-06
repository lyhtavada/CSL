# KB Sync Diff — Joy Loyalty (`joy-loyalty-agent`)

**Mined-FAQ source:** `reports/weekly-faqs/joy/joy_2026-06-29_2026-07-05.md` (Jun 29 – Jul 5, 2026; 55 FAQs)
**KB snapshot:** live cache from `cs2.avada.net`, 66 files (cached `/tmp/kb-sync/joy/`)
**Run type:** diff-only, review-gate (no push). Verdicts verified against actual cached file content.

## Result: 0 actionable changes — KB already current

**COVERED: 55 · OUTDATED: 0 · GAP: 0 · PARTIAL: 0 → payloads = `[]` (nothing to push)**

The first automated pass flagged 8 files as OUTDATED/PARTIAL, but on line-level verification against the live KB **every one of those facts already exists verbatim** — they landed in the prior-week sync (`build_joy_2026-06-28.py`). This week's mined FAQs are ~65% recurring, and the KB was brought current last week, so there is nothing new to add. The corrected verdicts:

| Item (mined Q#) | Fact | First-pass verdict | Verified verdict | Evidence in live KB |
| --- | --- | --- | --- | --- |
| Q34 / Q20 | VIP **Tier Assessment = Ultimate only**, NOT Advanced ("common mistake") | PARTIAL | **COVERED** | `kb/reference/pricing.md:62` (feature row) + `:96` ("Tier Assessment is **NOT** on Advanced… Ultimate only") |
| Q21 | Existing tier members can get the entry reward via **"Grant the entry reward for existing customers"** at relaunch | OUTDATED | **COVERED** | `kb/case/vip-tiers.md:50–52`; `kb/reference/vip-tiers.md:102–108` |
| Q50 | Birthday 30-day anti-fraud window **reducible to 7 days on request** | PARTIAL | **COVERED** | `kb/case/birthday-reward.md:96` |
| Q11 | Streak bonus runs on **server time (UTC+0)** — known bug | PARTIAL | **COVERED** | `kb/reference/earning-programs.md:184` |
| Q29 | **POS-created customers** may miss sign-up reward; Shopify Flow "Customer created" workaround | PARTIAL | **COVERED** | `kb/reference/earning-programs.md:79–83` |
| Q41 | **Opt-in enrollment** ("Join the Program") + Member-tag vs VIP-tier-tag | PARTIAL | **COVERED** | `kb/reference/customers.md:61–72` |
| — | **Store credit expiration now available** | PARTIAL | **COVERED** | `kb/reference/points-advanced.md:84–86` |
| Q18 | Free Gift = Shopify **Product discount**; no native gift cards; Store Credit alternative | PARTIAL | **COVERED** | `kb/reference/redeeming-programs.md:89–93` |

Additional new-this-week items spot-checked and confirmed covered: Q12 multi-currency earning rates (`kb/reference/earning-programs.md`), Q32 third-party cart-drawer redeem (`kb/reference/cart-drawer.md`), Q43 centralized points / expansion stores (`kb/reference/case-handling.md`), Q54 Thank-you page double-join (`kb/reference/thank-you-page.md`), Q7 promo 5x→1x "Lock earning conditions" (documented; the live incident is a bug/escalation, not a stale KB fact).

## Why no patch
Pushing byte-identical content would create empty commits + an unnecessary reindex and would misleadingly imply the KB changed. Joy is left untouched this week. Re-run next week against the fresh mined file.
