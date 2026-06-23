#!/usr/bin/env python3
"""Build kb-sync payloads for Chatty (Ivy) — window 2026-06-15 → 2026-06-21.
6 items: 2 OUTDATED (Q4, Q17), 1 GAP (Q26), 3 PARTIAL (Q2, Q12, Q21, Q24)."""
import json, os

APP, AGENT, DATE = "chatty", "chatty-agent", "2026-06-15"
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")

def rd(flat): return open(os.path.join(SRC, flat)).read()
results = {}

# ---- Q4 OUTDATED: Plus scenario limit ----
f = rd("kb__case__ai-scenario-limit.md")
assert f.count("| Plus | — |") == 1
f = f.replace("| Plus | — |", "| Plus | Unlimited |")
results["kb/case/ai-scenario-limit.md"] = f

# ---- Q17 OUTDATED: custom/3rd-party metafields not supported ----
f = rd("kb__faq__ai-training-setup.md")
old_mf = """## AI and Shopify Metafields

Yes — metafields are synced if they are published and readable via the Shopify API. Go to **AI agent** → **Training data** → **Manage** → **Products** to verify metafield data is available after syncing.

**Limitation:** Metaobject references (metafields that reference other metaobjects) are not yet fully supported — this feature is in development. Log all requests for this in the tracking sheet."""
assert old_mf in f, "Q17 metafields anchor not found"
new_mf = """## AI and Shopify Metafields

Only **standard / supported** metafield types are synced to the AI. You can see and toggle which metafields are synced at **AI agent** → **Training data** → **Manage** → **Products** → **Manage metafields**.

**Not supported:** Non-standard / third-party **custom metafields** (for example, metafields created via a separate metafields app) are **not currently synced** — only the supported metafield types sync. Metaobject references (metafields that reference other metaobjects) are also not yet fully supported.

**Workaround:** Add that data into **Custom knowledge** as a Q&A so the AI can still use it. If supporting a specific metafield type matters to the store, log a **feature request** with the merchant's use case so the product team can prioritize it."""
f = f.replace(old_mf, new_mf, 1)

# ---- Q2 PARTIAL: "X of X learned but list empty" + deactivated/filter checks ----
anchor_sync = """If the store exceeds the plan limit, Chatty trains on the most recently updated products first. For stores with more than 5,000 products, contact support — this requires manual backend configuration."""
assert anchor_sync in f, "Q2 product sync anchor not found"
q2_add = anchor_sync + """

### "It won't upload all my products" / products missing from the list

If products are missing in **AI agent** → **Training data** → **Manage** → **Products**, check in this order:
1. **Deactivated products** — products toggled off in the list won't train; toggle them **Active**.
2. **A search or filter is hiding them** — clear any active search/filter.
3. **Header says "X of X products learned" but the list shows "No items found"** — clear the filter and switch to the **All** tab. If the list is still empty, escalate as a **display bug** (collect store URL + a screenshot)."""
f = f.replace(anchor_sync, q2_add, 1)
results["kb/faq/ai-training-setup.md"] = f

# ---- Q26 GAP: FAQ page blank / "wiped" after upgrade ----
f = rd("kb__faq__faqs-page.md")
anchor_fp = """The FAQs page is a dedicated page on your Shopify store where customers can browse and find answers without contacting support."""
assert anchor_fp in f, "Q26 faqs-page anchor not found"
q26_add = anchor_fp + """

### Why the FAQ page looks blank / "wiped" after upgrading

Upgrading your plan does **not** delete your FAQ content. Two things create this impression:
1. **The Shopify page editor shows the FAQ page as blank by design** — the content is rendered by the Chatty app, not stored in the Shopify page. Check the live storefront URL (`/pages/avada-faqs`) instead of the page editor.
2. **On a new install, Chatty seeds a small sample/default FAQ** as a starting point, which can be mistaken for your real FAQs being replaced.

Your own questions live in **FAQs** → **Manage FAQs** — edit or add them there. The Chatty FAQ page is optional; if you already have your own FAQ page, keep it and feed its URL into **AI agent** → **Training data** → **Custom knowledge** instead."""
f = f.replace(anchor_fp, q26_add, 1)
results["kb/faq/faqs-page.md"] = f

# ---- Q21 PARTIAL: hide carrier / own tracking page (Track123) vs 17TRACK ----
f = rd("kb__faq__order-tracking.md")
anchor_tm = """- **17TRACK** — Best for stores wanting to keep customers on-site. Embeds the 17TRACK tracking page directly on your store."""
assert anchor_tm in f, "Q21 tracking-methods anchor not found"
q21_add = anchor_tm + """

### Hiding the carrier / using your own tracking page

If the tracking result shows the **wrong or a foreign (e.g. Chinese) carrier** and the merchant wants customers redirected to **their own tracking page** (e.g. a Track123 page) instead of seeing the raw carrier, use **Custom tracking** and set their own tracking URL.

Hiding a specific carrier name **inside the AI's tracking reply**, or forcing a third-party page in place of the built-in tracking flow, is **not** self-serve — it needs a custom scenario / backend tweak. Collect the desired tracking URL and an example order, then escalate to TS."""
f = f.replace(anchor_tm, q21_add, 1)
results["kb/faq/order-tracking.md"] = f

# ---- Q12 PARTIAL: team offline while logged in + browser notif to be alerted ----
f = rd("kb__faq__chatbox-settings.md")
anchor_am = """Away mode allows individual team members to appear offline to customers without logging out. When enabled:
- The storefront shows that staff member as unavailable
- If **all** staff have Away mode on, customers see the store as offline
- Resets automatically when the member logs out and back in

Activate it via the toggle at the top of the Chatty app interface."""
assert anchor_am in f, "Q12 away-mode anchor not found"
q12_add = anchor_am + """

**Team shows "offline" even though a member is logged in:** this is almost always **Away mode** on that member — turn it off so they show online to customers. Two related points merchants ask about:
- **Online/offline status only works when the Live chat block is on** in Chatbox settings, and working hours are set in **Settings** → **General** → **Chat availability**.
- **To be alerted to a new live chat, the agent must allow browser notifications from Chatty** in their browser (see notification troubleshooting if alerts don't arrive). Agents log in at **app.chatty.net** — no Shopify admin needed; they accept the invite email and set a password first."""
f = f.replace(anchor_am, q12_add, 1)
results["kb/faq/chatbox-settings.md"] = f

# ---- Q24 PARTIAL: WhatsApp Pending — Business Admin role + OAuth perms ----
f = rd("kb__case__whatsapp-messenger-issues.md")
anchor_wa = """3. Ensure **Two-factor authentication (2FA)** is enabled for the phone number in WhatsApp Business settings"""
assert anchor_wa in f, "Q24 whatsapp-pending anchor not found"
q24_add = anchor_wa + """
4. Confirm the connecting user has the **Business Admin** role in Meta Business Manager (not Employee)
5. Confirm all permissions were granted to **"AVADA group company limited"** during OAuth, with no popup / cookie blockers active"""
f = f.replace(anchor_wa, q24_add, 1)
results["kb/case/whatsapp-messenger-issues.md"] = f

# ---- write payloads ----
ops = [{"agent": AGENT, "path": p, "content": c} for p, c in results.items()]
json.dump(ops, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"wrote {len(ops)} payloads -> {OUT}")
for o in ops:
    print(f"  {o['path']}: {len(o['content'])} bytes")
