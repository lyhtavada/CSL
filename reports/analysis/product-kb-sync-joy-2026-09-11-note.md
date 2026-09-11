# /product-kb-sync — Joy — 2026-09-11

## Sources reviewed
- **Slack** (release channel, shared): 2 Joy posts (28/08, 03/09) — SMS/phone-bonus, milestone claim badge, referral widget counts, Widget V4 on-brand/Customer Accounts mode/coupon QR/style presets.
- **GitLab B1** `docs/features` (53 commits) + `docs/ai-agent` (1 commit) since baseline `89782c5f` (2026-08-21).
- **GitLab B2**: `locale/input` (215 files, not enumerated individually — covered implicitly via the B1 feature docs that reference the same labels), `translationsWidgetV4.js`/`V2.js`, `getAppNavigation.js` (0 commits), `appMenu.js` (1 commit — admin nav entry for referral V3 editor, internal-only, skipped).

## Outcome: 3 patches drafted (1 OUTDATED, 2 GAP)

| # | Verdict | File | Reason |
|---|---|---|---|
| 1 | **OUTDATED** | `kb/reference/settings-developers.md` | KB said "REST API v2 and Webhook API are exclusively available on Ultimate ($499/mo)". Product reversed this policy (fd0ceb07, d0547db6, b48eb9a8): now a paid-plan entitlement — Free/Starter denied with 402 (not 403), Pro gets 30 req/10s + 200/day, Advanced 60 req/10s + 2,000/day, Ultimate unlimited. MCP shares the same per-shop quota (also no longer Ultimate-only). Numbers were retuned twice during the window (final commit b48eb9a8, 2026-09-10) — used the final numbers. |
| 2 | **GAP** | `kb/reference/checkout.md` | "Points earned in order confirmation email" checkout block (Joy Point Calculator writes order attributes a merchant can render via Liquid in Shopify's order confirmation email) had **zero** KB coverage before this patch. Recently extended (571cba0a, 2026-09-10) to also write balance + custom point label attributes, not just the earned-points estimate. Shopify Plus requirement carried over from the existing checkout.md framing. |
| 3 | **GAP** | `kb/reference/referral.md` | Slack (28/08) mentioned Widget V4 referral block now shows Invited/Completed/Pending counts + an activity list to the referrer, self-serve. Not previously documented; added as a short new section, cross-referenced to the existing "Referral export — Status detail column" states already in the file. |

## Discarded / not patched (with reason)
- **Member Exclusive Deal duplicate** (099415d5 + 3 related commits) — doc itself is flagged `Status: proposed — NOT product-approved`, came from a single merchant ticket routed to product, no sign-off. Not shipped; skipped.
- **Coupon QR code, on-brand design scan, Neo-Brutalism style preset (beta), open-widget-from-theme-account-button, Customer Accounts widget mode** — all already fully and correctly documented in `kb/reference/widget.md` (a prior sync evidently already covered the 03/09 Slack post + the 2026-09-03 GitLab commit `39dd5c0f`/`5a982113`). Verified COVERED, no changes needed.
- **Milestone `reward ready to claim` event + claimable badge** (Slack 28/08) — already documented in `kb/reference/milestone.md` under "Claim reminder — event + claimable badge (Widget V4 only)". COVERED.
- **SMS subscribe + phone-number bonus** (Slack 28/08, GitLab `79bbc1fe` + related) — already documented in `kb/reference/earning-programs.md` under "Subscribe SMS marketing (+ phone number bonus)", matching the later revision that folded the phone badge into the card's Details block. COVERED.
- **Referral claim popup V3** (8e77fa00 + cb8fdd1e + 3ef443d6) — a real shipped UI/UX change (two-step claim→reveal flow, retires the old referrer-side invite popup on V3 shops) but the existing `kb/case/referral.md` "Disabling the Referral Pop-up" scenario is generic ("guide customers to disable... or toggle the widget element") and not clearly contradicted by V3 — didn't have enough confidence in what merchant-visible UI text actually changed to safely patch as OUTDATED without over-claiming. **Flagging for a follow-up pass, not patched this run.**
- **REST API paid-entitlement docs churn** (eb0094d9, 6aa7c0e5, bfe4bfe2, e9001eee, d79f761c, 05da7c58, cb8fdd1e-adjacent) — pure internal docs/rationale commits explaining the same policy change patched in #1 above; not separate signals.
- **Widget-v4 on-brand auto-scan bug-fix cluster** (~20 commits, 2026-08-24→27) — all `fix:` commits hardening a feature already documented in `kb/reference/widget.md`; no new merchant-facing behavior beyond what's already there.
- **Store-credit routing refactor, export-pipeline refactor, Shopify API-version bump fix (docs/ai-agent)** — internal engineering only, no merchant-facing surface.

## Not pushed
Per review-gate mode: payloads written, not pushed/reindexed. State (`state/last_sync.json`) not advanced — Betty will handle that separately after Liz reviews.

Payloads: `reports/analysis/product-kb-sync-joy-2026-09-11-payloads.json`
