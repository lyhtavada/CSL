# KB-sync diff — Joy Loyalty (week Jun 22–28, 2026)

> Mined-FAQ source: `reports/weekly-faqs/joy/joy_2026-06-22_2026-06-28.md` (43 FAQs, 171 sessions)
> Live KB compared: `joy-loyalty-agent` on cs2.avada.net (65 files, cached to `/tmp/kb-sync/joy/`)
> Run mode: **DIFF-ONLY / review-gate** — no push, no reindex.
> Payloads: `reports/analysis/kb-sync-joy-2026-06-28-payloads.json`

## Verdict counts
- **OUTDATED:** 2 (Q10 decimal VIP multiplier, Q38 ReCharge API-key)
- **GAP:** 2 (Q8 webhook delay, Q20 monthly accounting export)
- **PARTIAL:** 6 (Q6 guest "order recorded", Q12 limit-earning, Q14 redeem-in-line/redeem-all, Q25 store-credit mechanics, Q39 C:Hub blank panel, Q41 repeat-rate-by-tier)
- COVERED (no action): Q1–Q5, Q7, Q9, Q11, Q13, Q15–Q19, Q21–Q24, Q26–Q37, Q40, Q42, Q43

> Note Q7 (sign-up trigger change, freq ~6) is already correctly reflected in `kb/case/points-earning.md`, `kb/case/customers.md`, `kb/reference/earning-programs.md` — no KB file still claims welcome points auto-fire on account creation, so COVERED, not OUTDATED.

## OUTDATED
- **Q10 (freq ~5) — VIP multiplier** in `kb/reference/vip-tiers.md`. Stale: "Silver 1.5×". Correct: the Bonus-Points perk takes WHOLE multipliers only (2×, 3×), not decimals like 1.25×/1.5×; fractional rates bridge via Shopify Flow; logged as feedback.
- **Q38 (freq ~1) — ReCharge** in `kb/reference/integrations-subscription.md`. Stale: "Connect at Joy Admin → Integrations → Recharge". Correct: ReCharge is now auto-detected from Shopify subscription orders (old API-key connection deprecated); discount-sync was briefly disrupted, since restored.

## GAP
- **Q8 (freq ~3) — points awarded late (Shopify webhook 40–90 min, POS pain)** → `kb/reference/settings-order.md`. Collect order # + order time + when points posted → escalate; logged for the POS real-time case.
- **Q20 (freq ~2) — monthly accounting export (Customer Name + Order ID + Points Earned)** → `kb/reference/customers.md`. No self-serve combined export; team generates on request; Activities log = interim self-serve.

## PARTIAL
- **Q6 (freq ~16, top theme)** add "order recorded" = guest signal + pre-order full-points-on-Paid. (`kb/case/points-earning.md`)
- **Q14 (freq ~7)** redeem-in-line binds to native cart drawer only (3rd-party slide-cart/PageFly need a CSS selector); redeem entire balance via Dynamic discount + Maximum-points field. (`kb/reference/cart-drawer.md`)
- **Q25 (freq ~3)** store-credit mechanics: subtotal basis, rate simplification, rounding-to-$0 / decimal credit, per-tier rates, "re-grant access" on failure. (`kb/reference/points-advanced.md`)
- **Q41 (freq ~3)** no native repeat-purchase-rate-by-tier report; workaround + analytics-revamp instability caveat. (`kb/reference/analytics.md`)
- **Q12 (freq ~2)** name "Limit customer earning" (Advanced) + max-points-per-order. (`kb/reference/points-advanced.md`)
- **Q39 (freq ~2)** Customer Hub / C:Hub blank loyalty panel → escalate to tech (no C:Hub content existed in KB). (`kb/reference/integrations-other.md`)

## Priority (by mined frequency)
1. Q6 — guest "order recorded" (~16) — PARTIAL
2. Q14 — redeem-in-line / redeem-all (~7) — PARTIAL
3. Q10 — decimal VIP multiplier (~5) — OUTDATED
4. Q8 — webhook delay (~3) — GAP
5. Q25 — store-credit mechanics (~3) — PARTIAL
6. Q41 — repeat-rate-by-tier (~3) — PARTIAL
7. Q12 — limit-earning controls (~2) — PARTIAL
8. Q20 — monthly accounting export (~2) — GAP
9. Q39 — C:Hub blank panel (~2) — PARTIAL
10. Q38 — ReCharge API-key (~1) — OUTDATED
