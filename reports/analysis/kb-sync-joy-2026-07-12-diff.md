# KB-sync diff — Joy (Joyce) · window Jul 06–12 2026

Mined FAQ: `reports/weekly-faqs/joy/joy_2026-07-06_2026-07-12.md` (67 FAQs, 176 sessions)
Live KB: agent `joy-loyalty-agent` on cs2.avada.net (cached `/tmp/kb-sync/joy/`)
**Review-gate run — nothing pushed, nothing reindexed.**

## Tally
- COVERED: 48 · **OUTDATED: 0** · **GAP: 7** · **PARTIAL: 12** (19 actionable)
- Payloads (13 files): `reports/analysis/kb-sync-joy-2026-07-12-payloads.json`
- KB is factually current — every price/plan-gate/format/limit already matches. All items are **additive** sub-points under existing anchors; no existing text rewritten.

## GAP (net-new)
- **Q5** Recharge webhook change `subscription_contract → subscription_contract_checkout_one` → `kb/case/points-earning.md`  *(highest-freq, ~8 sessions)*
- **Q10** gender/age not collected (birthday only) → `kb/reference/birthday.md`
- **Q18** free-gift code invalid on Loop/Recharge recurring → `kb/reference/redeeming-programs.md`
- **Q23** milestone counting: order-count = lifetime, spend/points = post start-date → `kb/reference/milestone.md`
- **Q35** POS tile name fixed ("Joy Loyalty") → `kb/reference/pos.md`
- **Q36** no per-POS-location awarding → `kb/reference/pos.md`
- **Q45** silent retroactive import (turn off notifications first) → `kb/reference/migration.md`
- **Q64** "JOY-XXXX" discount tag not configurable → `kb/reference/customers.md`

## PARTIAL (missing sub-point)
- **Q46** "App embed 0 Active/Inactive" dashboard glitch → `kb/case/widget.md` *(~5 sessions)*
- **Q13** Claim → adjust points partial redemption → `kb/reference/redeeming-programs.md`
- **Q16** free-gift must be published/active, hide via template not draft; NCA code-only → `kb/reference/redeeming-programs.md`
- **Q19** balance can go negative after refund of redeemed order → `kb/reference/points-advanced.md`
- **Q22** quarterly VIP reset unsupported → Milestone workaround → `kb/reference/vip-tiers.md`
- **Q25** Shopify fixed-amount discount applies per item; no accumulated-points perk → `kb/reference/vip-tiers.md`
- **Q28** custom-domain referral link → `kb/reference/referral.md`
- **Q38** Spoks/Seguno have no native sync → `kb/reference/integrations-email.md`
- **Q39** two "Follow on Instagram" accounts = one global action → `kb/reference/earning-programs.md`
- **Q44** revoke-vs-remove coupon distinction at relaunch → `kb/reference/customers.md`
- **Q63** excluded/"Left program" customers on account page → `kb/reference/customers.md`

## After review
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py reports/analysis/kb-sync-joy-2026-07-12-payloads.json
```
