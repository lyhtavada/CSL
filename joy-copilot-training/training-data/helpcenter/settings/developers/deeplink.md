---
category: Settings
subcategory: Developers
topic: Deeplink
source: helpcenter
---

Q: What is Deeplink in Joy Loyalty?
Q: How do I set up Deeplink?
Q: Where can I find Deeplink settings?
A: This feature is available for **All plans**.

### What is "Deeplink"?[**​**](https://help.avada.app/joy/how-to-set-up-VIP-Tier/#introduction)

Deeplink is a feature that simplifies access to the Joy widget directly from your store's website. By adding Deeplinks to your menu or footer, customers can quickly open the loyalty program interface, improving their interaction with your store.

Additionally, this Deeplink allows you to hide the floating button if not needed. The widget will be triggered by the link on the menu.

### Why do you need Deeplinks?

Deeplinks make it easy for customers to access your Joy widget directly from your website’s menu or footer, ensuring seamless interaction with your loyalty program. They also let you hide the floating button, keeping your store’s design clean while maintaining quick access for customers.

### **How to set up**

Deeplink is supported right out of the box, so there’s no need to manually set up the deeplink anchors. The available anchors include: `#joy-home`, `#joy-ways-to-earn`, `#joy-ways-to-redeem`, `#joy-referral-program`

1

**Find your deeplink settings**

Go to **Setting > General** and you can see the deeplink information

2

**Add the Deeplink to the Menu or Footer**

In the top bar navigation, select **Online Store** -> choose **Navigation.** Next, choose the Main Menu or Footer where you want to add the Deeplink

3

**Fill the information for the menu item**

Click on **Add menu item**, and fill in the name for the menu item. With the URL value, you can just paste the value copied straight from the Joy admin and then hit Enter.

In the example below, I chose the **Main menu** and added a **Rewards** item to it. I then pasted the parameter `#joy-home` into the link field. After saving all the settings, clicking "Rewards" in the menu will automatically display the Joy widget's home page.

The floating widget show on the click of the link on the top navigation

### How to trigger widget using top menu only

In **Widget Design** > **Advanced Settings**, simply toggle the **Hide Widget** option. This will hide the floating button, but the widget will still function and can be triggered via a deeplink or our [JS SDK](https://devdocs.joy.so/joy-javascript-api/widget-methods#open-widget).

### Wrap up

Integrating Deeplinks into your website’s menu or footer provides an alternative way for customers to access your loyalty program. By setting up Deeplinks, you give your customers an additional, convenient option to trigger the Joy widget whenever they need it.