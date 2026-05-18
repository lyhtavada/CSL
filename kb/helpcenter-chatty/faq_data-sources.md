# AI Data Sources

<!-- CHUNK: data-sources-overview -->
```yaml
chunk_id: "data-sources__overview"
doc_id: "chatty-data-sources"
title: "What are AI data sources and what can I add"
category: "data-sources"
tags: ["data sources", "training data", "what to add", "AI training", "data types"]
applies_when: "Merchant asks about data sources for AI training or what information they can add"
```

## AI Data Sources Overview

**Does Chatty automatically sync my shipping policy, About us, or other store pages?** Yes — Chatty auto-syncs these Shopify store pages with no manual re-sync needed: Shipping policy, Return policy, Privacy policy, Terms of service, FAQ, Contact us, and About us. If a merchant updates one of these pages, the AI picks up the change automatically. No action required.

Data sources are the information you provide to train your AI assistant. The AI uses this data to give accurate, personalized responses about your products, services, and policies.

**Store data (auto-synced):**
- Products: descriptions, variants, pricing, availability, inventory status, metafields
- Discounts: all active and inactive discounts from Shopify
- Markets: market settings including currency and exchange rates
- FAQs: your existing FAQs in Chatty

**Custom data sources (manually added):**
- Questions (Q&A pairs)
- URLs (website links — content is scraped and indexed)
- Files (.JSON, .TXT, .PDF, .CSV — max 2MB for AI training data; images and PDFs with tables not yet supported)

**Auto-synced Shopify pages:** Shipping policy, Return policy, Privacy policy, Terms of service, FAQ, Contact us, About us. If not synced, go to **Data Sources** → **Sync store pages** or re-activate AI.

Product information updates daily at **12:00 AM PST**.

---

<!-- CHUNK: data-sources-add-manage -->
```yaml
chunk_id: "data-sources__add-manage"
doc_id: "chatty-data-sources"
title: "How to add and manage AI data sources"
category: "data-sources"
tags: ["add data source", "manage data", "sync products", "Q&A", "upload file", "add URL"]
applies_when: "Merchant wants to add data sources or manage their existing AI training data"
```

## Adding & Managing Data Sources

Go to **AI Assistant** → **Data Sources**.

**Sync store data:** Turn on auto-sync for products, discounts, markets, and FAQs.

**Add custom data:**
- **Questions** — add Q&A pairs (edit, change status Active/Inactive, delete, export to CSV)
- **URLs** — add website links; click **Resync** if content has changed; preview content in plain text
- **Files** — upload .JSON, .TXT, .PDF, or .CSV (max 2MB); edit or change status Active/Inactive

After adding data, go to **Test** to verify AI responds correctly. You can test AI even before activating it.

**Bulk management:** Click any data type to see the full list. Select multiple items for bulk actions: set as active, set as inactive, or delete.

---

<!-- CHUNK: data-sources-smart-recommendations -->
```yaml
chunk_id: "data-sources__smart-recommendations"
doc_id: "chatty-data-sources"
title: "Set up smart product recommendations for AI"
category: "data-sources"
tags: ["smart recommendations", "bestseller", "new arrival", "product recommendations", "AI recommendations"]
applies_when: "Merchant wants to set up smart product recommendations for the AI assistant"
```

## Smart Recommendations Setup

Tell AI which products to recommend in specific situations:

1. Click **Smart Recommendations** in Data Sources
2. Select a collection to manage
3. Set up product list and keywords
4. Click **Add product** to add items, **Delete** to remove
5. Click **Save** and activate the recommendation

**Categories:**
- **Bestseller** — AI suggests when customers ask "What's popular?"
- **New arrival** — AI suggests when customers ask "What's new?"
- **Sales promotion** — AI suggests when customers ask about discounts or deals
- **Special occasions** — AI suggests when customers ask about gifts or special events

**Smart syncing (auto):** By default, Chatty selects the top 20 products based on sales from the last 30 days and updates daily. Max 20 products per collection.

---

<!-- CHUNK: data-sources-manage-products -->
```yaml
chunk_id: "data-sources__manage-products"
doc_id: "chatty-data-sources"
title: "Enable or disable specific products from AI training"
category: "data-sources"
tags: ["enable products", "disable products", "product status", "product FAQ", "manage products"]
applies_when: "Merchant wants to enable or disable specific products from AI training data"
```

## Managing Individual Products

After syncing products:
1. Go to **Data Sources** → **Products** tab
2. Set each product's status to **Enabled** or **Disabled**

Only published, in-stock products work with Chatty. Product subscriptions are not supported.

**Add product-specific FAQs:**
1. Click **Products** tab
2. Click **Add FAQs** or **Manage FAQs** on a specific product
