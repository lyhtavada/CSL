# Joy Loyalty — Program Setup Sheet (template for each merchant)

**Used with:** [Joy Onboarding Flow — Phase 1](./joy-onboarding-flow.md).

**Master Google Sheet:** https://docs.google.com/spreadsheets/d/1Dnvg96dqgXmckuj4lVpQ3GM4_Fs4yB-h-xClSWvhdME/edit — CS **Make a copy** → 1 bản/merchant → merchant fills in the Value column → paste copy link into the "Detail program" field of the main onboarding ticket. This markdown is the source-of-truth for the sheet content; keep both in sync if the sheet changes.

**Tabs:** `Store Info & Setup` · `Earning` · `Redemption` · `VIP Membership` · `Referral` · `Milestones & Quest`

- **Merchant fills** = the value this store chooses.
- **Suggested / Preset** = sample value (based on AOV + industry) for merchants who aren't sure. CS can use the in-app AI agent to read AOV/industry and generate suggestions.
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
| Item | Value | Suggested / Preset | Notes |
|------|-------|--------------------|-------|
| Program name | | "[Brand] Club" / "[Brand] Rewards" | |
| Point currency name | | "[Brand] Points" (e.g. Koko Points) | branded currency = feels owned |
| Point value | | 1 pt = $0.01 | ~5% rebate rate |
| Base earn rate | | 1 pt / $1 spent | tier multipliers added in VIP tab |
| Point expiry | | 12 months inactivity | win-back email before expiry |
| Coupon expiry | | 45 days from issue | gives customers time to use |
| BFCM / event policy | | pause earning during event? | toggle in Joy admin, notify customers first |

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

| Rule | Action (Joy) | Points Earned | Suggested / Preset | Status |
|------|-------------|---------------|--------------------|--------|
| Purchase Reward | Place Order | | 1 pt / $1 | |
| Welcome Bonus | Sign-Up | | 200 pts | |
| Newsletter Sign-Up | Newsletter Sign-Up | | 50 pts | |
| Birthday Gift | Birthday Reward | | 200–300 pts | |
| Product Review | Write Review | | 50 pts | |
| Photo/Video Review | Write Review (media) | | 150 pts | |
| Google Review | Google Reviews | | 150 pts (limit 1/customer) | |
| Follow Instagram | Social Activity | | 30 pts | |
| Follow TikTok | Social Activity | | 30 pts | |
| Social Share | Custom (Shopify Flow) | | 100 pts | |

---

## TAB 3 — Redemption (how customers redeem points)

| Reward | Type | Cost (Points) | Suggested / Preset | Status |
|--------|------|---------------|--------------------|--------|
| Fixed discount | Amount off | | 100 pts = $5 off | |
| Fixed discount | Amount off | | 500 pts = $30 off | |
| Percentage discount | % off | | 500 pts = 10% off | |
| Free shipping | Free ship | | 300 pts | |
| Free product | Product | | (store dependent) | |

| General Rule | Value | Suggested |
|--------------|-------|-----------|
| Min points to redeem | | 100 pts |
| Point expiration | | 12 months inactivity |

---

## TAB 4 — VIP Membership (if tiers used)

> Skip if the program is simple. Example (Maison Koko): Sipper → Steeper → Master.

| Tier Config | Value | Suggested |
|-------------|-------|-----------|
| **Tier calculated by** | | Amount spent OR points earned — pick one |
| Evaluation window | | over 12 months |
| **Point earn multiplied by tier?** | | Yes — higher tiers earn faster (e.g. 1x / 1.5x / 2x) |
| Re-evaluation cycle | | 12 months |

| Tier | Condition to Reach | Earn Multiplier | Perk | Suggested / Preset |
|------|--------------------|-----------------|------|--------------------|
| Tier 1 (e.g. Silver / Sipper) | | | | 1x — base earn |
| Tier 2 (e.g. Gold / Steeper) | | | | 1.5x — +earn, birthday gift |
| Tier 3 (e.g. Platinum / Master) | | | | 2x — early access, free shipping |

| Member vs Guest | Value | Suggested |
|-----------------|-------|-----------|
| Guest sees | | program + ways to earn; login required to earn/redeem |
| Member sees | | current points, history, tier, rewards |

---

## TAB 5 — Referral

| Item | Value | Suggested / Preset |
|------|-------|--------------------|
| Referrer gets | | +200 pts after friend's first order |
| Referred friend gets | | $10 off first order |
| Condition | | min order $X |
| **Referral points multiplied by tier?** | | Yes / No — higher tiers get bigger referral reward? |
| Referral banner (widget) | | on-brand image |

---

## TAB 6 — Milestones & Quest (if used)

> A chain of actions / milestones customers complete for extra rewards. Skip if not used.

| Milestone / Quest | Condition | Reward | Suggested / Preset |
|-------------------|-----------|--------|--------------------|
| Complete profile | | | +50 pts |
| First purchase | | | +100 pts |
| Reach X orders | | | bonus pts / unlock tier |
| Seasonal quest | | | (campaign dependent) |

---

## Go-live check

> Checklist go-live đầy đủ (earning/redeeming/VIP/guest-member/migration/widget/test loop/switch live) sống ở **ticket chính**, không lặp lại ở đây — xem [`joy-onboarding-flow.md` §6.1](./joy-onboarding-flow.md#6-ticket-structure--1-ticket-onboarding-chính--kh). Sheet này chỉ để KH điền **rule** (earning/redeeming/VIP/referral/milestone) trước khi CS chuyển qua bước setup + tick vào ticket.

*(Liz to adjust preset point values per real AOV/industry of the Advanced merchant later.)*
