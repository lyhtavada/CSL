circle-info

- **Editing English content** is available in the **Free plan**.
- **Changing the default language** and **editing content in the default language** require the **Professional plan**.
- **Using the Detect Language feature** is available only in the **Advanced and Enterprise plans**.

### [hashtag](#understanding-the-rule) Understanding the Rule

Joy's translation feature operates through two main tabs:

1. **Default Language**: This is the language in which the widget will be displayed if no other language is detected.
2. **Detected Language**: This language is identified based on the user's information. There are two methods for detecting the language:

   - **Customer's IP**: Detects the language based on the customer's geographical location.
   - **Browser's Language**: Detects the language set in the customer's browser settings.
   - **Shopify language selector**: Auto-translate pages corresponding to the language selected on a multi-language store

circle-check

Find [detailed instructions](/translations#translate-with-shopify-language-selector) for the advanced translation option - Shopify language selector

With Joy Loyalty's Translations, you can change the language of the widget to suit your customers' preferences. The supported languages include:

circle-info

**Note:** After translating your loyalty program to your new language, you can still customize the content title in a more specialized manner to suit your objectives

The **default language** refers to the language in which the widget is displayed.

- In the **Free plan**, the default language is always **English**, and you can make basic content edits.
- Starting from the **Professional plan**, merchants can change the default language and modify all content in that language.

To change the default language:

1

Go to **Translations**

2

**Select the language** you want to set as the default in the widget

### [hashtag](#how-to-set-up-the-detected-language) How to set up the **detected language**

The Detected Language feature allows the widget to display content in the user's preferred language. This preference is determined based on:

- The user's IP address
- The language settings of the user's browser

#### [hashtag](#translate-with-shopify-language-selector) **Translate with Shopify language selector**

This option allows a seamless translation option that aligns with the customer's selected language on multi-language stores.

Merchants can combine the [Shopify language selectorarrow-up-right](https://help.shopify.com/en/manual/international/localization-and-translation) with the Joy translation settings for a comprehensive on-site translation.

#### [hashtag](#set-up-detected-language) Set Up Detected Language:

1

Go to **Translations**

2

Choose how to detect your customer's language

3

Add **Detected Languages** and edit the list by selecting the languages you want to support

#### [hashtag](#important-notes) Important notes

- You must have **at least one language** in the **Detected Language** list for this feature to work.
- When a customer's language matches a language in the **Detected Language** list, the widget will display in that language.
- If the customer's language is **not** in the **Detected Language** list, the widget will default to the **default language**.

- The **Detect Language** feature is only available when customers are **logged into** your loyalty program.
- If a customer is **not logged in**, the widget will display the **default language**.

### [hashtag](#how-to-edit-widgets-content) How to edit widget's content

1

Go to Translations, choose widget design

2

**Select the content** you want to translate

3

Manually change the translation of labels

Navigate to the **tabs** you want to modify.

Adjust the **translation** as needed.

Click the **Save** button to apply your changes.

#### [hashtag](#important-note) Important note

When translating content, you must **maintain the variable format** to ensure correct values are displayed.

Only translate the content, but **keep variables in English** using the format **{{variable\_name}}**.

- Example: To display the **page number**, always use **{{page\_number}}**, regardless of the language.

**Correct Example:**

✅ **Korean:** `페이지 {{page_number}}`

**Incorrect Example:**

❌ `페이지 {{페이지_넘버}}` (This will not work correctly.)

[PreviousShopify Flow: Zigpoll and Joy Loyaltychevron-left](/integrations/integrate-with-shopify-flow/shopify-flow-zigpoll-and-joy-loyalty)[NextNotificationschevron-right](/notifications)

Last updated 19 days ago

Was this helpful?