# Joy Loyalty — Program Setup Sheet (template for each merchant)

**Used with:** [Joy Onboarding Flow — Phase 1](./joy-onboarding-flow.md).

**Master Google Sheet:** https://docs.google.com/spreadsheets/d/1Dnvg96dqgXmckuj4lVpQ3GM4_Fs4yB-h-xClSWvhdME/edit — CS **Make a copy** → 1 bản/merchant → merchant fills in the Value column → paste copy link into the "Detail program" field of the main onboarding ticket. This markdown is the source-of-truth for the sheet content; keep both in sync if the sheet changes.

**Tabs:** `Store Info & Setup` · `Earning` · `Redemption` · `VIP Membership` · `Referral` · `Milestones & Quest`

- **Merchant fills** = the value this store chooses.
- Not sure what value to pick? Leave it blank, or CS can use the in-app AI agent to read AOV/industry and generate suggestions.
- **Status:** Existing / New / Upgraded / Skip — mark once set up in Joy admin.

---

## TAB 1 — Store Info & Setup

### Store Info
| Item | Value | Notes |
|------|-------|-------|
| Store / domain | | |
| Plan | Advanced | |
| Industry | | |
| AOV (avg order value) | | |
| **Target launch date** | | |
| Used a loyalty app before? | | app name / no |
| Migrating? | | yes → old app / no |

### Program Config
| Item | Value | Notes |
|------|-------|-------|
| Program name | | |
| Point currency name | | branded currency = feels owned |
| Point value | | ~5% rebate rate |
| Base earn rate | | tier multipliers added in VIP tab |
| Point expiry | | win-back email before expiry |
| Coupon expiry | | gives customers time to use |
| BFCM / event policy (pause earning during event?) | | toggle in Joy admin, notify customers first |

### Migration / Import (migrating only)
| Item | Value | Notes |
|------|-------|-------|
| Old app | | |
| Data exported yet? | | point balance / member list / tier |
| File format | | CSV? |
| **How far does point balance migrate** | | ⚠️ confirm early, complex → forward TS |
| Number of members | | |

---

## TAB 2 — Earning (how customers earn points)

| Rule | Action (Joy) | Points Earned | Status |
|------|-------------|---------------|--------|
| Purchase Reward | Place Order | | |
| Welcome Bonus | Sign-Up | | |
| Newsletter Sign-Up | Newsletter Sign-Up | | |
| Birthday Gift | Birthday Reward | | |
| Product Review | Write Review | | |
| Photo/Video Review | Write Review (media) | | |
| Google Review | Google Reviews | | |
| Follow Instagram | Social Activity | | |
| Follow TikTok | Social Activity | | |
| Social Share | Custom (Shopify Flow) | | |

---

## TAB 3 — Redemption (how customers redeem points)

| Reward | Type | Cost (Points) | Status |
|--------|------|---------------|--------|
| Fixed discount | Amount off | | |
| Fixed discount | Amount off | | |
| Percentage discount | % off | | |
| Free shipping | Free ship | | |
| Free product | Product | | |

| General Rule | Value |
|--------------|-------|
| Min points to redeem | |
| Point expiration | |

---

## TAB 4 — VIP Membership (if tiers used)

> Skip if the program is simple. Example (Maison Koko): Sipper → Steeper → Master.

| Tier Config | Value |
|-------------|-------|
| **Tier calculated by** (amount spent OR points earned — pick one) | |
| Evaluation window | |
| **Point earn multiplied by tier?** | |
| Re-evaluation cycle | |

| Tier | Condition to Reach | Earn Multiplier | Perk |
|------|--------------------|-----------------|------|
| Tier 1 (e.g. Silver / Sipper) | | | |
| Tier 2 (e.g. Gold / Steeper) | | | |
| Tier 3 (e.g. Platinum / Master) | | | |

| Member vs Guest | Value |
|-----------------|-------|
| Guest sees | |
| Member sees | |

---

## TAB 5 — Referral

| Item | Value |
|------|-------|
| Referrer gets | |
| Referred friend gets | |
| Condition | |
| **Referral points multiplied by tier?** | |
| Referral banner (widget) | |

---

## TAB 6 — Milestones & Quest (if used)

> A chain of actions / milestones customers complete for extra rewards. Skip if not used.

| Milestone / Quest | Condition | Reward |
|-------------------|-----------|--------|
| Complete profile | | |
| First purchase | | |
| Reach X orders | | |
| Seasonal quest | | |

---

## Go-live check

> Checklist go-live đầy đủ (earning/redeeming/VIP/guest-member/migration/widget/test loop/switch live) sống ở **ticket chính**, không lặp lại ở đây — xem [`joy-onboarding-flow.md` §6.1](./joy-onboarding-flow.md#6-ticket-structure--1-ticket-onboarding-chính--kh). Sheet này chỉ để KH điền **rule** (earning/redeeming/VIP/referral/milestone) trước khi CS chuyển qua bước setup + tick vào ticket.
