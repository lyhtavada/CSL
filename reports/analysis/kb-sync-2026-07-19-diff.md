# KB Sync diff — week Jul 13–19, 2026 (REVIEW GATE, nothing pushed)

Run: 2026-07-20 · diff-only. Payloads built, **not** pushed, **not** reindexed.

| App | Mined FAQs | KB files | OUTDATED | GAP | PARTIAL | COVERED | Files patched |
|---|---|---|---|---|---|---|---|
| Chatty | 75 | 70 | 11 | 14 | 29 | 21 | 21 |
| Joy | 78 | 66 | 10 | 12 | 33 | 23 | 19 |

Payloads:
- `reports/analysis/kb-sync-chatty-2026-07-19-payloads.json` (21 files)
- `reports/analysis/kb-sync-joy-2026-07-19-payloads.json` (19 files)

Push after review:
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py ~/CSL/reports/analysis/kb-sync-chatty-2026-07-19-payloads.json
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py ~/CSL/reports/analysis/kb-sync-joy-2026-07-19-payloads.json
```

---

## Chatty

### OUTDATED — plan limits, verified against chatty.net/pricing (2026-07-20)

The KB contradicted **itself** on plan limits, so the live pricing page was used
as the tiebreaker. The mined data was right in every case.

| Fact | KB said | Correct | Files fixed |
|---|---|---|---|
| Basic products for AI training | 1,500 | **500** | 5 files, 8 lines |
| Plus URLs & files | Unlimited | **700** | 2 files |
| Basic chat history | Unlimited | **12 months** | knowledge-base.md |
| Plus price | $199.99 | **$199** | knowledge-base.md |

The extension baseline table in `kb/case/ai-product-limit.md` was realigned too,
otherwise CS would extend a Free merchant to a limit that no longer exists.

### OUTDATED — other

- `kb/faq/inbox.md` — web app domain `app.meetchatty.com` → `app.chatty.net`
  (exactly 1 occurrence cache-wide; 7 other files already use the correct one).
- `kb/faq/ai-compliance.md` — "Default retention is 90 days, you can adjust this
  in your settings" → per-plan retention (90d Free / 12mo Basic / unlimited
  Pro+Plus), and dropped the non-existent setting.
- `kb/faq/inbox.md` — anonymous visitor nicknames were documented as "feature
  request under review, no workaround". Two workarounds exist today (remove
  `{{customer_name}}` from the AI welcome message; fixed "Anonymous-xxx" label
  on request).

### Highest-value additions

- **Welcome message, three places** (~10 sessions) → `kb/faq/chatbox-settings.md`.
  Translations copy overrides both the AI and chatbox greeting. Root cause of
  most "my edit didn't save" reports.
- **AI still gives the old answer after a FAQ edit** (~6) →
  `kb/case/ai-wrong-responses.md`. Conversation starters carry their own
  answers — the cause behind most "AI still says 3–5 days" complaints this week.
- **Web push is per browser AND per device** (~20) → `kb/case/notification-issues.md`.
- **Analytics metric definitions** (~6) → `kb/faq/analytics.md`. "Handled
  Conversations" only counts replies within 24h; 0 conversations = Live chat
  block off.
- **Mobile inbox crashes** (~5) → `kb/faq/mobile-app.md`, with the device-info
  collection list.
- Also: FAQs-vs-Custom-knowledge-vs-Instructions-vs-Scenarios table, Meta 24-hour
  reply window, "FAQs page URL already taken", AI conversation counting
  surprises, custom-URL path-only rule (2 files), shopper-in-support-inbox rule
  in `persona/facts.md`.

### ⚠️ NOT patched — needs your call

1. **Annual billing discount.** chatty.net/pricing says **"Save 18%"**; the KB
   says 15% and "~15–17%" in two places. But the KB's own annual prices
   ($16.99 / $58.99 / $169.99 vs $19.99 / $68.99 / $199) compute to **~15%**.
   Either the percentage or the annual prices are stale — changing just the
   number would leave the page self-contradictory. Needs the real annual price
   list.
2. **"Categories can't be deleted."** Mined Q39 says so; `kb/faq/add-category.md`
   documents a delete icon. One of them is wrong — needs a product check.
3. **Spam protection.** Mined Q70 claims "no automated bot detection today", but
   `kb/faq/general-settings.md` documents a working **Smart spam protection**
   toggle. Here the *mined answer* looks wrong, so the KB was left alone.
4. **Q24 handover.** KB says *Inbox → Assign to AI*; mined says *Reset
   conversation*. Both may work — worth standardising so CS gives one answer.
5. **Integrations list** disagrees three ways (`general-settings.md` has Gorgias
   and Shopify Flow, `knowledge-base.md` has Air Reviews, mined has neither
   Gorgias nor Flow). Can't resolve from the cache.

Note: the "5,000 products needs manual backend config" line is **not** a
contradiction of the 8,000 Pro limit — it's a separate operational threshold.
Left as-is.

---

## Joy

### OUTDATED

- **Decimal per-tier multipliers** (`kb/reference/vip-tiers.md`) — KB told agents
  to bridge 1.5× with **Shopify Flow** and that decimals were "logged as product
  feedback". Now supported via **Rule Engine** (Advanced+). This week's reversal;
  agents corrected the AI on it twice. Exactly 1 occurrence — no scattered copies.
- **Sign-up backfill** (`kb/reference/earning-programs.md`, `kb/case/points-earning.md`)
  — both files said "escalate, do not promise a self-serve toggle". It is now
  self-serve at **Settings → Pre-launch → Sync Sign Up**. ~9 sessions/week, and
  the KB was actively telling agents to escalate something merchants can do
  themselves.
- **Cart drawer redemption** (`kb/reference/pricing.md`) — table said Advanced+;
  `kb/reference/cart-drawer.md` already said Essential+. Pricing table was the
  wrong copy.
- **Analytics plan gate** (`kb/reference/analytics.md`) — line 21 said "All
  plans" while line 42 of the *same file* and `pricing.md` both said Essential+.
  The bot could tell a Starter merchant Analytics was included.
- **Trial length** (`kb/case/billing.md`) — flat "14 days" → 14 (Essential/
  Advanced) / 30 (Ultimate).
- **Classic widget** (`kb/case/widget.md`) — offered as a neutral fallback with
  no warning. It's deprecated, and switching back **discards the Unified design**.
- **Klaviyo** — `coupon_name` now exists (KB said it didn't); and both
  `integrations-email.md` and `case/integrations.md` said `person|lookup` was the
  *only* supported format immediately before/after sections that use
  `event|lookup`. That absolutism is what produces the `n/a` symptom merchants
  report.
- **Referral popup** (`kb/reference/onsite-content.md`) — said it is "NOT in the
  Popups tab". The toggle *is* there; only the design lives under Widget →
  Referrals.

### Highest-value additions

- **Redeemed code does not auto-apply at checkout** (~11 sessions, top redemption
  topic) → `kb/reference/redeeming-programs.md`.
- **Launcher position + widget not showing** (~22 and ~9 — the two largest Joy
  topics) → `kb/case/widget.md`, incl. the jump-after-tap rendering bug, the
  "check the button is actually ours" step, and the inaccurate "App embed 0
  Active" badge.
- **"Complete birthday info" reward** (~8) → `kb/reference/birthday.md`. Absent
  entirely; distinct from the Birthday reward. Plus the self-serve **Trigger
  birthday reward** button (KB said escalate).
- **VIP program start date resets everyone's tier** (~7) → `kb/case/vip-tiers.md`.
- **Order placed but no points** (~13) → contradictory rule conditions
  (Online store AND POS) + expired end date.
- **Fixed reward > cart total breaks third-party apps** (~7) → fix is a minimum
  cart value.
- Also: opt-in enrollment mechanics, date-range activity export, pixel
  "Disconnected" reassurance, Grant-access permission failure, suppressing
  notifications during bulk updates.

### ⚠️ NOT patched — needs your call

1. **POS plan row.** `kb/reference/pricing.md` says `Shopify POS | ❌ | ❌ | ✅ | ✅`
   (Essential ❌), but `kb/reference/pos.md`, the mined answer and pricing.md's own
   plan-id table all indicate Essential supports **earn-only POS display**, with
   redemption at Advanced+. Commercially sensitive; the clean fix is probably
   splitting the row into "POS (earn display)" vs "POS redemption".
2. `kb/reference/customers.md` line 88 has a **duplicated sentence** — cosmetic,
   left alone.
