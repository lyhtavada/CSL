circle-info

**Who can use this feature?**

- This feature is available for all users

### [hashtag](#why-add-data-sources) Why add data sources

We've trained AI on your own data. By adding your own data sources, you can train AI assistant about your specific products, services, and business policies.

This helps the AI give more accurate and personalized responses to your customers.

[Train AIchevron-right](/ai/train-ai)

### [hashtag](#type-of-data-sources) Type of data sources

There are two main types of data sources:

- **Store data**: Information already available in your Shopify store that can be automatically synced
- **Custom data source**: Additional information you manually add to enhance AI knowledge

- Products: product descriptions, variants, pricing, and availability
- Discounts: discounts created in Shopify
- Markets: Market settings, including currency and exchange rates
- FAQs: Your existing FAQs section in Chatt

- Questions
- URLs
- Files

chevron-rightWhat product information is synced to Chatty?[hashtag](#what-product-information-is-synced-to-chatty)

Available product information that is synced to Chatty:

- Specific product details (name, descriptions, images, vendor, type)
- Product variants (colors, sizes, styles)
- Price ranges and comparisons
- Product features and specifications
- Collection
- Product inventory
- Product metafields

Your product information will be updated daily at 12:00 AM PST.

chevron-rightWhat types of product metafields are supported?[hashtag](#what-types-of-product-metafields-are-supported)

We support all metafields in this list [Shopify documentation on metafield typesarrow-up-right](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/metafield-types), **except:**

- Reference type:

  - collection\_reference
  - customer\_reference
  - file\_reference
  - metaobject\_reference
  - mixed\_reference
  - page\_reference
  - product\_reference
  - product\_taxonomy\_value\_reference
  - variant\_reference
- Other:

  - Link
  - URL

chevron-rightSome main Shopify pages will be auto-synced when you activate AI. What are they?[hashtag](#some-main-shopify-pages-will-be-auto-synced-when-you-activate-ai.-what-are-they)

- Shipping policy
- Return polity
- Privacy policy
- Terms of service
- FAQ
- Contact us
- About us

If your Shopify pages are not auto-synced to data sources, go to Data sources *→* Click Sync store pages or re-activate AI.

[What goes in each data sourcechevron-right](/ai/data-sources/what-goes-in-each-data-source)

### [hashtag](#how-to-add-data-sources) How to add data sources

1

Go to **AI assistant** tab

2

Sync store data

Turn on auto-sync store data: products, discounts, markets, and FAQs.

3

Add custom data sources

- **Question**: You can add a single question or multiple questions at once.
- **URL**: Add URL/website links
- **File**: Add files (.JSON, .TXT, .PDF, .CSV) to data source. Maximum file size is 2MB per files. Images and PDFs with tables are not yet supported.

Learn more about [what goes in each data source](/ai/data-sources/what-goes-in-each-data-source)

4

After building your data source, you can go to [Test](/ai/test-and-optimize-ai) to test your AI assistant.

circle-info

If you haven't activated AI, you **can still test AI assistant** with data source you added.

5

You can edit or delete it from data source.

### [hashtag](#how-to-manage-data-sources) How to manage data sources

#### [hashtag](#id-0.-bulk-management) 0. Bulk management

In "Data sources", click on any data type to go to data source list.

You can select multiple data sources and take bulk actions: set as active, set as inactive, or delete.

#### [hashtag](#id-1.-faqs) 1. FAQs

You will manage FAQs in your FAQs list. All FAQs from your list will be added to data source.

Click FAQs → You'll be redirected to **Manage FAQs** page

[⁉️FAQschevron-right](/faqs)

#### [hashtag](#id-2.-products) 2. Products

After syncing all products, you can manage which products are used to train AI.

1. Click **Products** tab
2. Go to Product list
3. Change status of each product `Enabled/Disabled` to show/hide it in the training data.

circle-info

Currently, Chatty only works with published products that are in stock. Product subscriptions are not supported at this time.

**FAQs for products**

You can also add specific FAQs for each product. This helps AI answer

1. Click Products tab
2. Go to Product list
3. Click **Add FAQs** or **Manage FAQs**

#### [hashtag](#id-3.-discounts) 3. Discounts

All discounts available in your Shopify store are synced to AI training data. (both active & inactive)

If you don't see you discounts, click Sync now to update the latest discount from your store.

#### [hashtag](#id-3.-smart-recommendations) 3. Smart recommendations

You can manage which products AI recommends as best sellers and new arrivals.

Chatty provides two pre-built collections that AI uses for recommendations:

1. **Bestseller:** Products AI suggests when customers ask, "What's popular?" or "What do others buy?"
2. **New arrival**: Products AI suggests when customers ask, "What's new?" or "Any new items?"
3. **Sales promotion:** Products AI suggests when customers ask about "discounts", "deals", or "what's on sale?"
4. **Special occasions:** Products AI suggests when customers ask about "gifts", "birthday presents", or mention special events

**What is smart syncing (auto)?**

By default, Chatty automatically does the following for Best sellers and New arrivals:

- Select top 20 products based on sales from the last 30 days
- Update the list daily

circle-info

You can combine auto-selection with your manual choices by:

- Activate smart sync
- Add/remove manually products from the list

This means: Your recommendation will be updated daily with new products while remaining your manual choices. (maximum 20 products/collection)

**How to set up smart recommendations:**

1. Click **Smart recommendations**
2. Select a collection to manage
3. Set up product list and keywords (custom recommendations)
4. Click **Add product** to add products
5. Click **Delete** to remove products from list
6. Click **Save** and activate the recommendation

#### [hashtag](#id-4.-questions) 4. Questions

You can delete, edit details, or change the status `Active/Inactive` of each question.

- Click **Products** tab
- Go to Data source list
- Edit question details

You can export all questions (or active questions) in a CSV file.

#### [hashtag](#id-5.-url) 5. URL

You can edit or change the status `Active/Inactive` of each URL.

If there's any content change in the URL, you can click Resync to update to the latest version.

When you click the link, you can preview the page in plain text mode.

#### [hashtag](#id-6.-files) 6. Files

You can edit or change the status `Active/Inactive` of each file.

[PreviousHow Chatty trains AIchevron-left](/ai/overview/how-chatty-trains-ai)[NextWhat goes in each data sourcechevron-right](/ai/data-sources/what-goes-in-each-data-source)

Last updated 3 months ago

Was this helpful?