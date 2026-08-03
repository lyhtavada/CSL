# KB Sync Diff — Joy Loyalty (Joyce)

**Mined-FAQ source:** `reports/weekly-faqs/joy/joy_2026-07-20_2026-07-26.md` (190 Crisp sessions, Jul 20–26 2026)
**KB snapshot:** `/tmp/kb-sync/joy/` (66 files, agent `joy-loyalty-agent`)
**Gate:** review-only — no push, no reindex performed. Payloads saved to `kb-sync-joy-2026-07-26-payloads.json`, awaiting Liz's approval.

## Summary table

| Q# | Topic | KB file | Verdict |
|---|---|---|---|
| Q1 | Setup from scratch | reference/getting-started.md | COVERED |
| Q2 | Free team setup/styling | reference/getting-started.md | PARTIAL |
| Q3 | Starter vs paid plans | reference/pricing.md | COVERED |
| Q4 | Testing with Sandbox mode | reference/rule-engine.md, reference/points-advanced.md | COVERED |
| Q5 | Migrate/import from another app | reference/migration.md | COVERED |
| Q6 | No points on order | case/points-earning.md | COVERED |
| Q7 | Sign-up bonus not awarded | case/points-earning.md | COVERED |
| Q8 | Per-product/collection rates, exclude sale items | reference/earning-programs.md | PARTIAL |
| Q9 | Customer Opt-in / Join Program | case/points-earning.md, reference/earning-programs.md | PARTIAL |
| Q10 | Social/Instagram/review points | case/review-points.md, reference/earning-programs.md | COVERED |
| Q11 | Birthday reward not received | case/birthday-reward.md | COVERED |
| Q12 | Manual points → VIP tier | reference/points-advanced.md | COVERED |
| Q13 | How redemption works | reference/redeeming-programs.md | COVERED |
| Q14 | Code not combining at checkout | case/points-redeeming.md, reference/points-advanced.md | COVERED |
| Q15 | Edit/deactivate coupon w/o refund | reference/redeeming-programs.md | COVERED |
| Q16 | Redeem doesn't scale with quantity | reference/redeeming-programs.md | COVERED |
| Q17 | Product missing from redeem picker / variant cap | reference/redeeming-programs.md | COVERED |
| Q18 | Imported coupon can't be revoked | reference/migration.md | COVERED |
| Q19 | Tier entry reward not given | case/vip-tiers.md | COVERED |
| Q20 | Tiers/points look wrong after edit | case/vip-tiers.md | COVERED |
| Q21 | Exclusive tier annual renewal | reference/vip-tiers.md | COVERED |
| Q22 | Per-tier earning rates & setup order | reference/vip-tiers.md | PARTIAL |
| Q23 | Referral not visible in widget | reference/referral.md | PARTIAL |
| Q24 | When referrer gets rewarded | reference/referral.md | COVERED |
| Q25 | "Failed to adjust store credit" | reference/points-advanced.md | COVERED |
| Q26 | Referral analytics / export status fields | reference/referral.md | GAP |
| Q27 | Launcher overlap / positioning | case/widget.md | COVERED |
| Q28 | Classic vs Unified widget | reference/widget.md | COVERED |
| Q29 | Cart drawer "0 points" for guests | reference/cart-drawer.md | GAP |
| Q30 | Translation not working | reference/translations.md, case/onsite-content.md | COVERED |
| Q31 | Metafield sync | reference/settings-general.md | COVERED |
| Q32 | Omnisend sync | reference/integrations-email.md | COVERED |
| Q33 | POS tile error / sync | case/pos.md, reference/pos.md | PARTIAL |
| Q34 | Marketplace orders in usage quota | case/billing.md | COVERED |

**23 COVERED · 0 OUTDATED · 2 GAP · 6 PARTIAL (7 file patches, since Q23+Q26 both land in reference/referral.md)**

The KB is in very good shape this week — several items that were flagged "🆕 new" in the mined-FAQ digest (Q12 manual points→tier, Q16 redeem doesn't scale, Q17 variant cap, Q18 imported coupons, Q21 Exclusive tier renewal, Q30 translation limits, Q32 Omnisend) turned out to already be word-for-word present in the live KB — likely patched in a prior kb-sync run this cycle. Only the items below need action.

---

## GAP — no existing KB content

### Q29 — Cart drawer shows "0 points, Redeem" to logged-out guests
**File:** `kb/reference/cart-drawer.md`
**Missing:** No mention anywhere in the cart-drawer reference of guest-visitor behavior. Mined chats this week surfaced a genuinely new fix: a theme cart-drawer block setting to hide the redeem-inline block for unauthenticated visitors (showing a login prompt instead).
**Patch:** Added a new "Cart drawer showing '0 points, Redeem' to logged-out guests" section after the intro, before the "Common request" section.

### Q26 — Referral analytics & export status fields
**File:** `kb/reference/referral.md`
**Missing:** KB has no mention of the **Referral Management** screen (per-customer referral counts), nor of export status-field semantics (Pending/Awaiting fulfilment vs Completed), nor the known "Completed At timestamp shown while status is Pending" export display bug that one mined case confirmed as a real bug (not a support misunderstanding).
**Patch:** Added a "Referral performance & export status fields" section after "Reward revocation on refund."

---

## PARTIAL — KB covers the core but misses a sub-point

### Q2 — Free team setup/styling (~10 sessions, recurring)
**File:** `kb/reference/getting-started.md`
**Gap:** The only "free setup" content in the KB lives in `reference/widget.md`, scoped narrowly to the Classic→Unified migration flow. Mined chats show merchants ask for free setup/styling independent of any migration — a general capability, not migration-specific.
**Patch:** Added a "Free setup / styling service" section before the file's closing `## Related` block, generalizing the offer and cross-linking to `kb_collaborator-access`.

### Q8 — Multiple Place-order rules require Rule Engine (~3 sessions)
**File:** `kb/reference/earning-programs.md`
**Gap:** KB's "Recipe — earn only on full-price items" explains *how* to set a product-condition exclusion, but never states that running **more than one Place-order rule** (e.g. different rates per collection) requires **Rule Engine (Advanced/Ultimate)** — on Essential, a shop has only one rule, so a temporary rate change means editing and reverting the single rule.
**Patch:** Appended a clarifying paragraph to the "Conditions" section, cross-linking `kb_rule-engine`.

### Q9 — Customer Opt-in (Join Program) nuances (~4 sessions)
**File:** `kb/case/points-earning.md`
**Gap:** `reference/earning-programs.md` briefly lists opt-in as an earning blocker, but no case file walks through the most common real-world trigger — opt-in turned on **after launch**, catching already-active Guests off guard — nor clarifies that (a) previously awarded points don't auto-disappear, and (b) entry rewards for tier/loyalty programs are not retroactive for pre-join customers.
**Patch:** Added a new "Customer Opt-in (Join Program) and how it changes earning" section at the end of `case/points-earning.md`.

### Q22 — VIP tier setup sequencing (~3 sessions)
**File:** `kb/reference/vip-tiers.md`
**Stale/missing:** KB fully covers *how* to set per-tier earning rates (Bonus Points perk vs Rule Engine) but never states the **required setup order** when multiple programs are configured together: launch VIP Tiers first → per-tier earning rates → redeem programs → milestones last. Several mined chats hit "tier rate field greyed out" because they configured things out of order.
**Patch:** Added a "Setup order when configuring several programs together" section right after the per-tier earning-rate guidance.

### Q23 — Referral not visible in widget (~4 sessions)
**File:** `kb/reference/referral.md`
**Gap:** `case/referral.md` covers the *escalation* path for a hidden referral pop-up, but the reference file never explains that referral sharing lives inside the widget by default (not a floating element), never mentions the `#joy-referral-program` deeplink, and never calls out that there are **two separate toggles** that must both be on: On-site content → Widget → Referrals, and Reward programs → Referrals.
**Patch:** Added a "Referral isn't a separate floating element by default" section after "Sharing channels."

### Q33 — Don't run both POS extension versions at once (~3 sessions)
**File:** `kb/reference/pos.md`
**Gap:** KB documents the Legacy vs New POS extension distinction but never warns that running both simultaneously on the same device can conflict (session-token/loading errors) — this was a real recurring troubleshooting step in mined chats before deeper investigation.
**Patch:** Appended a short warning paragraph to the "Two versions" section.

---

## Priority list (ranked by mined frequency, high first)

1. **Q2 — Free setup/styling** (~10 sessions/wk, recurring) → `reference/getting-started.md`
2. **Q9 — Opt-in turned on after launch** (~4 sessions) → `case/points-earning.md`
3. **Q23 — Referral visibility / two toggles / deeplink** (~4 sessions) → `reference/referral.md`
4. **Q8 — Multi-rule Place-order needs Rule Engine** (~3 sessions) → `reference/earning-programs.md`
5. **Q22 — VIP tier setup order** (~3 sessions) → `reference/vip-tiers.md`
6. **Q33 — Don't run both POS extension versions** (~3 sessions) → `reference/pos.md`
7. **Q26 — Referral analytics/export status + Completed-At export bug** (~2 sessions, new) → `reference/referral.md`
8. **Q29 — Cart drawer 0-points for guests** (~1 session, new) → `reference/cart-drawer.md`

## Files that will change on push (7 total)
- `kb/reference/getting-started.md`
- `kb/reference/cart-drawer.md`
- `kb/reference/referral.md` (covers both Q23 and Q26)
- `kb/reference/pos.md`
- `kb/reference/vip-tiers.md`
- `kb/case/points-earning.md`
- `kb/reference/earning-programs.md`

**Awaiting Liz's approval before running `push_kb.py` + reindex.**
