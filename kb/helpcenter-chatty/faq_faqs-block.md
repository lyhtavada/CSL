# FAQs Block

<!-- CHUNK: faqs-block-overview -->
```yaml
chunk_id: "faq__faqs-block-overview"
doc_id: "chatty-faqs-block"
title: "What a FAQs block is and how to set one up on specific pages"
category: "faq"
subcategory: "build-faqs"
tags: ["faq block", "faqs block", "product page faq", "page-specific faq", "add faq to page", "faq section", "theme editor faq"]
applies_when: "When a merchant asks how to show FAQs on a specific page or how to create a FAQs block"
priority: "medium"
```

## FAQs Block Overview

A FAQs block lets you display a specific set of FAQs on any page of your store — for example, showing product-specific questions only on the relevant product page.

You can create multiple FAQs blocks with different questions for different products, collections, or pages.

## How to Set Up a FAQs Block

1. Go to **FAQs** → **FAQs block**
2. Set **General** information:
   - **Block name**: Internal name to identify this block (visible to admin only)
   - **Heading & Subheading**: Text shown in the block
3. Click **Browse** and select the FAQ questions to show
   - Turn on "Don't categorize FAQs" to show all questions in a flat list without category headers
4. Set display condition — choose where to show the block:
   - All pages
   - Specific product pages
   - All product pages of a collection
5. Customize appearance:
   - Heading size and alignment
   - Card corner radius
   - Colors
6. Click **Save**
7. Copy the **Block ID**
8. Go to your **Theme editor**:
   - Navigate to the page where you want to add the block
   - Click **Add section** → Search for **Chatty FAQs block** → Add it
   - Paste the Block ID in the settings
9. Click **Save** in the theme editor

You can also add the block using code: Go to **FAQs block code** → **Copy** → Add the HTML to your website's code.

---

<!-- CHUNK: faqs-block-manage -->
```yaml
chunk_id: "faq__faqs-block-manage"
doc_id: "chatty-faqs-block"
title: "How many FAQs blocks can be created and how to reuse FAQs across blocks"
category: "faq"
subcategory: "build-faqs"
tags: ["faq block limit", "multiple faq blocks", "reuse faq", "faq block management", "block id"]
applies_when: "When a merchant asks how many FAQs blocks they can create or whether the same FAQ can appear in multiple blocks"
priority: "low"
```

## Managing FAQs Blocks

In the FAQs block tab, you can:
- View all blocks with details (Block ID, name, number of FAQs, display conditions, status)
- Edit or delete blocks
- Create as many blocks as needed — **there's no limit**

There is no limit on the number of FAQs blocks you can create. Create separate blocks for each product or collection as needed.

To reuse the same FAQ in multiple blocks, include it when selecting questions for each block you create. The same FAQ question can appear in multiple blocks by using the same Block ID.
