# KB Diff — Joy (mined FAQ 2026-07-13→19 vs live KB)

78 mined FAQs reviewed. ~57 COVERED (several "assumed" via targeted spot-check, per agent note), 1 OUTDATED, 8 GAP, 7 PARTIAL.

## OUTDATED
1. `kb/case/notifications.md` — DMARC guidance said "recommend setting policy to none" for Simple Custom Sender; contradicts `kb/reference/settings-email.md` and mined answer, which says never weaken DMARC — use Custom Sending Domain instead. Fixed.

## GAP (8)
1. `kb/case/points-redeeming.md` — reward larger than cart zeroes total, breaks 3rd-party checkout apps → added min-cart-value fix
2. `kb/reference/integrations-subscription.md` — Free Gift rewards fail on subscription-portal renewals (Loop/Recharge) — Function can't resolve contract cart
3. `kb/case/review-points.md` — verified-buyer-only review points toggle undocumented
4. `kb/reference/referral.md` — Grant Markets Access button does nothing for limited-permission accounts
5. `kb/reference/settings-general.md` — GDPR/DPA documentation (joy.so links, no signature needed)
6. `kb/reference/translations.md` — Translate & Adapt app overriding Joy's own translations (6 sessions/week, recurring)
7. `kb/reference/translations.md` — admin UI language list (6 languages) missing, separate from 38 storefront languages
8. `kb/reference/widget.md` — custom Shopify customer metafield can't be shown in widget; workaround via Submit form/Fill survey
- Also noted in translations.md: currency-symbol-as-words bug (now fixed)
- **Skipped:** Q77 (stale domain in account links) — 1 session, no clear KB anchor, low priority per diff agent; not patched.

## PARTIAL (7)
1. `kb/reference/customers.md` — opt-in "Join Program" mid-launch gotcha (Guests silently stop earning, no retroactive rewards)
2. `kb/reference/vip-tiers.md` — tier program **start date** as root cause of "tiers/points look wrong" (most common, missed entirely before)
3. `kb/reference/translations.md` — (see GAP, same file)
4. `kb/reference/points-advanced.md` — store credit NOT available for Sign up / social / Instagram programs
5. `kb/reference/earning-programs.md` — multiple Place-order rules require Rule Engine (Advanced/Ultimate); Essential workaround
6. `kb/reference/widget.md` — Unified→Classic switch discards design; mobile shows as popup; Instant popup follow-up nuances
7. `kb/reference/referral.md` — pixel "Disconnected" reassurance (points unaffected) + re-authorize fix

12 files patched. Payloads: `reports/analysis/kb-sync-joy-2026-07-19-payloads.json`
