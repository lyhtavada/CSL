# product-kb-sync — joy — 2026-09-08 (diff-only, review gate)

## Sources used

**Slack** (`C07RNAY9ZC6`, shared release channel, since ts 1787212665.307569 → latest 1788506031.307929):
- "Joy Loyalty - 28/08/2026" (ts 1787913553.978889) — Subscribe SMS marketing earning program + phone-number bonus, phone prefix auto-detect, Milestone "reward ready to claim" event + widget badge (Widget V4 only), Referral widget invite-count + activity list.
- "Joy Loyalty - 03/09/2026" (ts 1788428641.841989) — Widget v4 1-click On-brand, open-from-theme-account-button + Account mode, Default style more minimal for new installs, back button, Inspect (click-to-edit in preview), mobile swipe.
- 3x "Chatty release" posts in the same channel — not Joy, skipped.

**GitLab** (`avada/starlink-team/joy`, `89782c5f...` → `870fee76...`, 848 commits):
- `docs/features/coupon-qr-code.md` (NEW, shipped, Widget V4 opt-in)
- `docs/features/widget-v4-style-presets.md` (NEW, Neo-Brutalism beta style preset, merged 2026-08-23)
- `docs/features/brand-identity-store.md` (NEW — "Save to brand settings" button on scan panels + Settings→Brand record; explicitly groundwork for a future AI widget-editing tool, "no AI tool edits widget design today")
- `docs/features/referral-claim-popup-v3.md` (NEW — big claim-popup redesign for the *referred friend*, gated behind `useReferralV3`, **new installs + DevZone toggle only, no backfill** — distinct surface from the Slack referral-widget item, which is the *referrer's* invite-count/activity view)
- `docs/features/member-exclusive-deal-duplicate.md` (Status: proposed, NOT product-approved — not shipped)
- `docs/ai-agent/shopifyql-loyalty-fields.md`, `docs/features/loyalty-widget-demo.md` — internal-only (analytics field reference, sales demo tool), skipped
- `docs/features/activities-tier-tab.md`, `milestone-claimable-event-badge.md`, `programs/sms-subscribe-phone-bonus.md`, `referral-export-status-and-completed-at.md`, `widget-v4-on-brand-design-scan.md` — empty diffs (doc existed before this range, or cross-referenced from the Slack items above)
- B2 (`appMenu.js`, all `locale/input/*.json`, `translationsWidgetV4.js`, `translationsWidgetV2.js`) — every diff came back **empty**, nothing to filter

## Classification

| Item | Source | Verdict | Why |
|---|---|---|---|
| Subscribe SMS marketing + phone bonus | Slack 28/08 | **COVERED** | `kb/reference/earning-programs.md` already documents both rewards in full (matches Slack almost verbatim) |
| Phone prefix auto-detect | Slack 28/08 | **COVERED** | `kb/reference/widget.md` SMS/WhatsApp consent section already covers it |
| Milestone claim event + widget badge | Slack 28/08 | **PARTIAL → patched** | Feature covered in `kb/reference/milestone.md`, but the literal Klaviyo/Flow trigger name ("Joy: Milestone Reward Ready To Claim") was missing — added |
| Referral widget invite-count + activity list | Slack 28/08 | **COVERED** | `kb/reference/widget.md` Body-block table already describes it |
| Widget v4 1-click On-brand + account-button + Account mode | Slack 03/09 | **COVERED** | `kb/reference/widget.md` "On-brand design scan" + "Open the widget from the theme's account button" sections already match |
| Widget v4 Inspect / back button / mobile swipe / Default-more-minimal | Slack 03/09 | **GAP → patched** | Not documented anywhere in the KB — added new section |
| Coupon QR code | GitLab B1 | **COVERED** | `kb/reference/widget.md` "Coupon QR code (My Coupons)" section already matches |
| Widget v4 Style Presets (Neo-Brutalism) | GitLab B1 | **COVERED** | `kb/reference/widget.md` "Style preset — Neo-Brutalism" section already matches, including Beta badge + known gaps |
| Referral export Status detail / Completed At | GitLab B1 | **COVERED** | `kb/reference/referral.md` "Referral export — Status detail column" already matches |
| Brand identity store (Save to brand settings) | GitLab B1 | **SKIPPED** | Groundwork feature for a future AI widget-editing tool; thin merchant-visible surface, not in release notes, risk of confusing with the existing "Brand colors" (Settings → Colors) section — left for a future pass once it has real usage |
| Referral claim popup V3 | GitLab B1 | **SKIPPED** | Gated behind `useReferralV3`, new-installs-only + DevZone toggle, explicitly no backfill — not generally live, would mislead existing-shop CS answers if documented as current behavior |
| Member exclusive deal duplicate | GitLab B1 | **SKIPPED** | Status: proposed, not product-approved — not shipped |
| shopifyql field reference, loyalty-widget-demo | GitLab B1 | **SKIPPED** | Internal-only docs, not CS-relevant |

## Files that will change (pending Liz's approval)

- `kb/reference/milestone.md` — added literal Klaviyo/Flow trigger name to the "Claim reminder" section
- `kb/reference/widget.md` — new section "Widget V4 editor — Inspect mode, back button, mobile swipe (added 2026-09-03)"

Payloads: `/Users/avada/CSL/reports/analysis/product-kb-sync-joy-2026-09-08-payloads.json`

No push, no reindex, no state update performed — waiting on review.
