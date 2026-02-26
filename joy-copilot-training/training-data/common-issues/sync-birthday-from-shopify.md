---
category: Integrations
problem: Can birthday data from Shopify be synced to Joy?
source: notion
---

Q: Can I sync customer birthday data from Shopify to Joy automatically?
Q: I already collect birthdays in Shopify metafields. How do I get that data into Joy?
Q: Is there a way to import birthday information from Shopify customer metafields into Joy?
Q: How do I connect Shopify birthday metafields with Joy Loyalty so birthdays sync over?
A: Yes! If your store already collects customer birthday data as a Shopify Metafield, you can sync it to Joy automatically. Here's how to set it up:

**Steps to enable birthday sync from Shopify:**

1. Go to **Joy app** > **Settings**
2. Find and enable the option **"Sync Shopify metafield to Joy data"**
3. Enter the **metafield name** that your store uses for birthday data
   - For example: `custom.birthday` (this is the most common format, but yours may be different depending on how it was set up in Shopify)
4. Click **Save**

Once enabled, Joy will automatically read the birthday data from the specified Shopify metafield and sync it to the customer's Joy profile.

**Tips:**
- Make sure the metafield name you enter matches exactly what is set up in your Shopify admin (including the namespace prefix like `custom.`)
- If you're not sure what your birthday metafield name is, you can check it in Shopify Admin > Settings > Custom data > Customers
- The sync happens automatically — you don't need to manually import or export any data
