---
name: icp-score
description: Use this skill when Liz or a CS agent wants to score how strong an ICP fit a Chatty merchant is — "chấm điểm ICP KH này", "check KH này có phải ICP không", "score this merchant", given a shop_domain or an email/store name to search first. Data-driven (BigQuery + StoreLeads), NOT the old chat-qualification SOP.
version: 1.0.0
---

# ICP Score Skill (Chatty)

On-demand data-driven ICP scoring for one Chatty merchant. Spec: `playbooks/chatty-icp-scoring-spec.md` — read it once for the full scoring rationale; this file is the operational checklist.

**This replaces the old 4-tier tags** (`icp-solo`/`icp-growing`/`icp-scaling`/`icp-midmarket` from `kb/cs-process/chatty/handle-icp-qualification.md`) with a score 0-100 → `ICP-High` / `ICP-Medium` / `ICP-Low` / `ICP-Unknown` + confidence %. Do not mix the two tag systems in output.

## Input

- `shop_domain` (e.g. `example.myshopify.com`) — if Liz only gives an email or store name, use `mcp__avada-analytic__merchant_search_by_identity` or `mcp__avada-analytic__merchant_search` first to resolve it.

## Steps

1. **Pull merchant data:**
   - `mcp__avada-analytic__merchant_profile(shop_domain, app_id="avadaFaq")` → primary source (`dash_merchant_360` fields: `current_mrr`, `mrr`, `is_paying_now`, `days_since_install`, `trial_flag`, `chatty_conversations_30d`, `usage_segment`, `ticket_count`, `dfy_ticket_count`)
   - `mcp__avada-analytic__shop_profile(shop_domain, app_id="avadaFaq")` → use `primary_plan` (normalized plan, e.g. `plus`/`advanced`/`grow`/`basic` — do NOT use the raw `shopify_plan` field, it mixes legacy codes like `professional`/`unlimited` with new ones) and `storeleads_profile.{estimated_visits, employee_count}` for store scale. `storeleads_profile` can be `null` if StoreLeads has no match — that counts against confidence, don't guess a value.
   - If `merchant_profile` returns nothing for this shop_domain, stop and report "no data — cannot score" rather than guessing.

2. **Compute score (0-100)** using the weighted formula in `playbooks/chatty-icp-scoring-spec.md` §2:

   | Tiêu chí | Weight |
   |---|---|
   | Shopify plan tier (`primary_plan`) | 25% |
   | Chatty MRR / investment (`current_mrr`) | 20% |
   | Store scale (`storeleads_profile.estimated_visits` + `employee_count`) | 20% |
   | Chatty engagement (`chatty_conversations_30d`, `usage_segment`) | 15% |
   | Support relationship (`ticket_count`, `dfy_ticket_count`) | 10% |
   | Business maturity (`days_since_install`, `trial_flag`) | 10% |

3. **Compute confidence %** = share of the above fields that actually had real data (not null/missing). If confidence < 60%, segment is forced to `ICP-Unknown` regardless of score.

4. **Segment:**
   - Confidence < 60% → `ICP-Unknown`
   - Score ≥ 80 → `ICP-High`
   - Score 50–79 → `ICP-Medium`
   - Score < 50 → `ICP-Low`

## Output Format

Always show the score breakdown, not just the tag — this is the whole point vs. a plain tag:

```
[shop_domain]
ICP Score: 87/100 → ICP-High (confidence: 92%)

- Shopify plan: Plus (100)
- Chatty MRR: $118/mo (100)
- Store scale: [từ StoreLeads hoặc fallback, ghi rõ nguồn]
- Engagement: high_usage, 34 conversations/30d (100)
- Support: 1 DFY ticket (100)
- Maturity: 210 days, not trial (100)

Gợi ý: [routing action theo segment, §3 trong spec — vd "ICP-High → ưu tiên SLA, cân nhắc offer discovery call"]
```

If Liz asks to **tag it** ("gắn tag luôn", "ghi vào CRM"): use `mcp__avada-analytic__shop_work_comment_create` to log the score+segment+reasoning as an internal CRM Work comment (this is the only write path — comments can't be edited later, only appended). Confirm with Liz before writing if she didn't explicitly ask to save it.

## Limits (say this out loud, don't just silently skip)

- This is Phase 1 (on-demand, manual). It does **not** auto-run when a chat opens — that requires dev work in the bridge repo (see spec §4), not yet implemented.
- Score is a signal, not a verdict — a merchant with real needs shouldn't be deprioritized just because of a low score; this compresses what the old chat-qualification SOP still does when data is thin.
