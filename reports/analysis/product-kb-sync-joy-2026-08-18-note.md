
# Product KB Sync — Joy Loyalty — 2026-08-18 (DIFF-ONLY, review-gate)

Sources: Slack #product-release (Joy, since 2026-08-10) + GitLab diff since commit `dba2c7d` (498 commits, reconstructed local diff).
No push/reindex performed. Payloads for Liz's review: `reports/analysis/product-kb-sync-joy-2026-08-18-payloads.json` (9 entries).

## Classification table

| # | Item | Source | Classification | Target KB file | Reason |
|---|------|--------|----------------|-----------------|--------|
| A1 | MCP connection — manage loyalty via Claude/ChatGPT | Slack + B6 (OauthConsent) + B9 (ConnectedApps/read-only key) | **GAP** | `kb/reference/ai-mcp-connection.md` (new) | No KB coverage of MCP/external-AI connection at all; existing `joy-ai.md` only covers Joy's own in-app assistant + Sidekick. |
| A2 | GoodAPI — redeem points for tree planting / ocean plastic | Slack | **GAP** | `kb/reference/goodapi-environmental-rewards.md` (new) | Zero mention of GoodAPI anywhere in cached KB (grep returned no hits). |
| A3 | Milestone insights — customer card + analytics tab | Slack + B1 (analytics doc) + B2 (customer card doc) + B15 (AnalyticsV2 metric labels) | **PARTIAL** | `kb/reference/milestone.md` | `milestone.md` exists and covers setup/types, but has zero mention of analytics or the customer-detail progress card — a real merchant-facing gap in an otherwise-covered topic. |
| A4 | Wallet pass — cross-app notifications (Swym, Joy Subscription) | Slack | **OUTDATED** | `kb/reference/wallet-pass.md` | Current KB text implies notifications are Joy-only ("Sends real-time notifications ... for: points earned, reward applied, tier upgrade, etc."). Now factually incomplete/misleading. |
| A5 | Deleted/archived product warning banner for rewards | Slack + B2/B7 (RewardConfigWarningBanner copy) | **PARTIAL** | `kb/reference/redeeming-programs.md` | Redeeming-programs.md already covers reward products/variants in depth but has no mention of this protection — merchants will ask "why did my customer get charged points for a broken reward" without it. |
| B3 | Milestone step custom names | GitLab only (pure GAP, no Slack note) | **PARTIAL** (folded into milestone.md) | `kb/reference/milestone.md` | Same file/topic as A3; adding as a second section keeps milestone.md self-contained rather than splitting a closely related detail into a new file. |
| B4 | Store-credit copy standardization ("$X store credit" not "N credits") | GitLab only (pure GAP) | **PARTIAL** | `kb/reference/points-advanced.md` | Copy-only change, but worth documenting so bot answers use correct terminology and don't get flagged as outdated when merchants reference old screenshots. |
| B5 | Store-credit currency-scoped balance + activity-feed display fix | GitLab only (pure GAP) | **PARTIAL** | `kb/reference/points-advanced.md` | Functional detail with real support impact ("why can't my customer use their store credit at checkout") not previously documented at all. |
| B6 | OAuth consent screen copy for MCP | GitLab (enrich A1) | folded into A1 | — | Per task instructions, enrich not duplicate. |
| B7 | RewardConfigWarningBanner copy | GitLab (enrich A5) | folded into A5 | — | Per task instructions, enrich not duplicate. |
| B8 | AI Translation Assistant (natural-language widget text editor) | GitLab only (pure GAP) | **PARTIAL** | `kb/reference/translations.md` | translations.md already covers "editing widget text" — this AI assistant is a new route to the same job, high-value addition to an existing, frequently-referenced file. |
| B9 (Recharge part) | Recharge `write_batches` scope error on bulk reward-code sync | GitLab only (pure GAP) | **PARTIAL** | `kb/reference/integrations-subscription.md` | Specific, actionable error message + fix not previously documented; distinct from the ConnectedApps/MCP content in B9 (which was folded into A1). |
| B10 | MilestoneV2.json "Choice of {rewards}" wording | GitLab | **SKIPPED (too minor)** | — | Per task instructions — minor UI wording addition, folded one line into the milestone.md custom-step-names section rather than a dedicated callout. |
| B12 | "Keep intact rate" checkbox (store credit) | GitLab only (pure GAP) | **PARTIAL** | `kb/reference/points-advanced.md` | Existing KB's "don't simplify" wording was ambiguous/inconsistent with this description — clarified in the same section. |
| B13 | `?open_joy` query param for email-redirect deep links | GitLab only (pure GAP) | **PARTIAL** | `kb/reference/settings-developers.md` | Concrete support fix for "deep link isn't opening from our email campaign" tickets. |
| B14 | CustomerDetails pending-rewards status filter/badges + "Credits" → "Store credit" rename | GitLab | **SKIPPED (too minor / folded)** | `kb/reference/points-advanced.md` (rename only) | The rename is already captured by the B4 copy-standardization note; the filter/badge UI itself is a minor admin-UX polish, not something merchants typically ask CS about. |
| B16 | Storefront widget copy: points-expiration display, V4 store-credit earn template, reward-unavailable messages | GitLab | **COVERED enough / SKIPPED** | — | These are storefront copy additions supporting features already documented elsewhere (point expiration in points-advanced.md, store credit in points-advanced.md, broken-reward messaging now added via A5 patch) — no standalone merchant question this would answer that isn't already covered by the other patches. |

## Counts

- **GAP (new files):** 2 — `ai-mcp-connection.md`, `goodapi-environmental-rewards.md`
- **OUTDATED (full replace):** 1 — `wallet-pass.md`
- **PARTIAL (edited in place):** 6 — `milestone.md`, `redeeming-programs.md`, `points-advanced.md`, `translations.md`, `settings-developers.md`, `integrations-subscription.md`
- **Total files patched:** 9
- **Skipped as too minor / already covered:** B10 (folded 1 line only), B14 (folded rename only, UI filter/badges skipped), B16 (skipped, underlying features already covered)

## Notes for Liz

- The 4 pure-GAP items with **no Slack release note at all** (found only via GitLab code diff) are the highest-value finds this run — see final chat summary for the call-out list.
- `milestone.md` and `points-advanced.md` and `redeeming-programs.md` got the heaviest edits (each folding in 2-3 signal items) — worth a careful read since they're full-file replacements of already-live, frequently-referenced KB pages.
- Plan tier for GoodAPI wasn't given precisely ("Plus-tier+ brands" per Slack) — flagged in the patch as "verify current plan gating in-app before promising availability," since Joy's plan names (Starter/Essential/Advanced/Ultimate) don't include a "Plus" tier — this may mean Shopify Plus merchants specifically, not a Joy plan tier. Worth Liz double-checking with product before this goes live.
