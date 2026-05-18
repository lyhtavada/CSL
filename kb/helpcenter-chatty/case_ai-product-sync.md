# AI Product Sync Issues

<!-- CHUNK: ai-product-sync-stuck -->
```yaml
chunk_id: "ai-product-sync__stuck"
doc_id: "chatty-ai-product-sync"
title: "AI product sync stuck or not making progress"
category: "ai-product-sync"
tags: ["sync stuck", "product sync", "hanging", "not progressing", "sync frozen", "resync"]
applies_when: "AI product sync is stuck and not making progress"
```

## Product Sync Stuck

1. Go to **AI Assistant** → **Data Source** and check the timestamp of the most recent sync
2. If sync has been running too long with no progress → support agent goes to **DevZone** → **Testing** → click **Start Auto Resync** to reset and restart (warning: this restarts sync from scratch)
3. After resync, update the merchant. When products are fully displayed, notify them
4. Advise the merchant not to make changes (editing product tags, etc.) during resync to avoid data conflicts

---

<!-- CHUNK: ai-product-sync-missing-products -->
```yaml
chunk_id: "ai-product-sync__missing-products"
doc_id: "chatty-ai-product-sync"
title: "AI not syncing all products — product count mismatch"
category: "ai-product-sync"
tags: ["not syncing", "missing products", "product count", "product mismatch", "fewer products", "sync count"]
applies_when: "AI is not syncing all products from the store, or product count in AI doesn't match Shopify"
```

## AI Not Syncing All Products

Only **published, in-stock** products are synced to the AI. Products sync daily at **12:00 AM PST**.

Common causes:
- Products are in draft status or out of stock
- The merchant has hit their plan's product limit (Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000)
- Sync hasn't run yet after recent product changes

1. Check the merchant's plan and product count against the plan limit
2. Verify products are published and in stock in Shopify
3. Wait for the next daily sync or trigger a manual resync
4. If issue persists, escalate to the dev team

---

<!-- CHUNK: ai-product-sync-deleted-products -->
```yaml
chunk_id: "ai-product-sync__deleted-products"
doc_id: "chatty-ai-product-sync"
title: "Deleted products still showing in AI sync"
category: "ai-product-sync"
tags: ["deleted products", "removed products", "old products", "ghost products", "still showing"]
applies_when: "Merchant deleted products from Shopify but the AI still answers questions about them or they still appear in sync"
```

## Deleted Products Still Showing in AI

The sync may not immediately reflect product deletions.

1. Suggest the merchant turn off product synchronization entirely
2. When they add products back later, they can re-enable sync
3. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync

---

<!-- CHUNK: ai-product-sync-extend-limits -->
```yaml
chunk_id: "ai-product-sync__extend-limits"
doc_id: "chatty-ai-product-sync"
title: "Extend product, URL, or file limits for AI training"
category: "ai-product-sync"
tags: ["extend limit", "increase limit", "product limit", "URL limit", "file limit", "plan limit", "hit limit"]
applies_when: "Merchant has hit their AI training data limits and needs them extended"
```

## Extending AI Training Data Limits

1. Check the merchant's current plan and what data type they need more of (Products/URLs/Files)
2. Explain plan limits and recommend an appropriate upgrade
3. If the merchant is not ready to upgrade → escalate internally to PM + CSL
4. For small increases (100–200 products, 10–20 URLs/Files) → CS can proactively extend in **DevZone** without requiring an upgrade
5. For stores with > 10,000 products → offer a demo call with the sales lead — requires manual backend configuration
6. Never promise beyond your authority — always say "I'll check internally" before confirming extensions

---

## Related
- case_ai-product-limit (merchant hit product/URL/file training limit)
- case_ai-wrong-responses (AI recommending wrong or deleted products)
- faq_data-sources (what data types are supported)
