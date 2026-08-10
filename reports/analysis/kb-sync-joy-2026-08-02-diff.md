# KB Diff — Joy (mined FAQ 2026-07-27 → 2026-08-02) — DIFF-ONLY, not pushed

Source: `reports/weekly-faqs/joy/joy_2026-07-27_2026-08-02.md` (43 FAQs) vs live KB cached from `cs2.avada.net` (`joy-loyalty-agent`, 66 files).

## Summary

| Verdict | Count |
|---|---|
| COVERED | 24 |
| GAP | 8 |
| PARTIAL | 5 |
| OUTDATED | 1 |

## OUTDATED

1. **Referral cookie expiry** — KB said cookie expiry (>7 days) flatly kills the referrer's reward; mined FAQ (Q27) shows the reward still fires if the referee's order email matches the referral claim email, even past 7 days. Fixed in `kb/reference/referral.md` + `kb/case/referral.md`.

## GAP (8) → patched in payload

1. Point Calculator tax-inclusive estimate vs tax-exclusive actual points + `{{earning_point_raw}}` placeholder syntax → `kb/reference/product-page.md`
2. No auto-expire for used one-time discount codes → `kb/reference/redeeming-programs.md`
3. Cart Drawer redeem-block revocation known limitation → `kb/reference/cart-drawer.md`
4. Exclusive tier + zero members = nothing to sync to Klaviyo → `kb/reference/vip-tiers.md`
5. Widget can't display on Shopify New Customer Account "Profile" page → `kb/reference/widget.md` + `kb/case/widget.md`
6. Customers can't edit own birthday after first entry → `kb/reference/birthday.md`
7. Fixed notification variables (e.g. `{{birthday_rewards}}`) not editable; `{{birthday_reward}}` singular workaround → `kb/reference/notifications.md`
8. Discount class change (Order→Product) technique to fix combination conflicts → `kb/reference/points-advanced.md`

## PARTIAL (5) → patched in payload

1. Stacking caveats — whole-subtotal calc + blank "Applies to" label → `kb/reference/points-advanced.md`
2. VIP tier edits inactive until re-Launch + "grant entry reward" checkbox gotcha → `kb/reference/vip-tiers.md`
3. Store credit — exactly 3 reward sources + no partial redemption explanation → `kb/reference/points-advanced.md`
4. Widget-not-showing checklist missing Profile-page caveat → `kb/case/widget.md`
5. Pixel "Connect" bug — missing referral-toggle refresh fix + "no App Blocks needed" note → `kb/case/integrations.md`

## Top 5 by mined-FAQ frequency

1. Q6/Q7 (order didn't earn points / Member vs sign-up bonus, 14+8 sessions) — already COVERED, no action.
2. Q9 Point Calculator tax gap (3 sessions, new recurring confusion) — GAP, low effort/high clarity.
3. Q29/Q31 widget overlap & not-showing (10 sessions each) — mostly COVERED; patch the Profile-page edge case.
4. Q17 discount combination Order→Product technique (4 sessions) — GAP/PARTIAL, codifies a technique agents already use ad hoc.
5. Q37/Q39 Shopify Pixel Connect bug (3 sessions, expected to rise before Aug 2026 Customer Events migration) — PARTIAL, add now before volume increases.

## Payload
`reports/analysis/kb-sync-joy-2026-08-02-payloads.json` — 12 files, full new content, gitignored.

## Push command (after Liz approves)
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py reports/analysis/kb-sync-joy-2026-08-02-payloads.json
```
