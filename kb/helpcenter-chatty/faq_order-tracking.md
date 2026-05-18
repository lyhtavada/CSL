# Order Tracking

<!-- CHUNK: order-tracking-setup -->
```yaml
chunk_id: "faq__order-tracking-setup"
doc_id: "chatty-order-tracking"
title: "How to enable and configure order tracking in the Chatty chatbox"
category: "faq"
subcategory: "chatbox"
tags: ["order tracking", "track order", "order status", "enable order tracking", "17TRACK", "custom tracking", "default tracking"]
applies_when: "When a merchant asks how to set up order tracking in Chatty or which tracking method to use"
priority: "high"
```

## Order Tracking Overview

Order tracking is a self-service feature that lets customers check their order status directly through your chatbox — without emailing you or calling support.

Customers can track using either an order number or a tracking number.

## How to Enable Order Tracking

1. Go to **Chatbox** → **General** tab → Turn on **Order tracking** in the Blocks section
2. Go to **Settings** → **Integrations** → In Order tracking, click **Manage**
3. Select your preferred tracking method
4. Click **Save**

## Tracking Methods

- **Default tracking** — Best for stores using major carriers (DHL, FedEx, UPS). Redirects customers to the carrier's official tracking page.
- **Custom tracking** — Best for stores using local or private shipping carriers. Redirects customers to a custom tracking URL.
- **17TRACK** — Best for stores wanting to keep customers on-site. Embeds the 17TRACK tracking page directly on your store.

---

<!-- CHUNK: order-tracking-customer-experience -->
```yaml
chunk_id: "faq__order-tracking-customer-experience"
doc_id: "chatty-order-tracking"
title: "How customers track orders and what information is shown"
category: "faq"
subcategory: "chatbox"
tags: ["track order customer", "order tracking widget", "order status display", "tracking information", "AI order tracking", "order number lookup"]
applies_when: "When a merchant asks how customers use the order tracking feature or what information is displayed"
priority: "medium"
```

## How Customers Track Orders

**On your website:**
1. Click to open the chatbox → Click **Order tracking**
2. Enter an order number + email or phone, OR enter a tracking number
3. Click **Track**

**In AI conversation:**
Customers can ask the AI for order tracking. The AI will request tracking information and provide status directly in chat.

## What Customers See

**General order information:**
- Order number
- Order status (Confirmed, On its way, Delivered for physical orders; Confirmed, Completed for digital orders)
- Confirmation date
- Total items and amount

**Tracking information:**
- Product images and quantities
- Shipment status and update date
- Shipping carrier, tracking number, fulfillment date

---

<!-- CHUNK: order-tracking-issues -->
```yaml
chunk_id: "faq__order-tracking-issues"
doc_id: "chatty-order-tracking"
title: "Why order tracking may not show correct or updated information"
category: "faq"
subcategory: "chatbox"
tags: ["order tracking not updating", "wrong order status", "carrier not supported", "tracking issue", "order status incorrect"]
applies_when: "When a merchant reports that order tracking is not showing correct or updated information"
priority: "medium"
```

## Why Order Tracking May Not Be Updating

For Shopify-supported carriers (like DHL, FedEx, UPS), full tracking details update automatically in real time.

For unsupported carriers, only basic status updates appear: Confirmed, On its way, Delivered.

To check if your carrier is supported by Shopify, look it up in the Shopify carrier documentation. If not supported, consider switching to the **Custom tracking** method to link directly to your carrier's tracking page.
