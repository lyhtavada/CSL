# Chatty FAQ — March 2026
*Generated from Crisp transcripts (March 2026) + Chatty KB*

---

## AI Assistant — Training & Data Sources

| No | Question | Answer |
|----|----------|--------|
| 1 | How does Chatty train its AI and what data does it use? | The AI learns from multiple sources that you provide: (1) **Products** — auto-synced daily at 12 AM PST (published, in-stock items only); (2) **FAQs** — your help-center Q&As; (3) **Policies** — shipping, returns, etc.; (4) **Custom Knowledge** — individual Q&As, URLs you submit, or uploaded files (.JSON, .TXT, .PDF, .CSV, max 2 MB each). The more specific and accurate your data, the better the AI performs. See: https://help.chatty.net/ai/data-sources |
| 2 | How do I add a URL or file to the AI's knowledge base? | Go to **AI Assistant > Data Sources > Custom Knowledge** and either paste a URL (the AI will crawl the page) or upload a file. Note: a single URL/page is limited to 25,000 characters. If a page exceeds this limit, consider exporting the content as a file and uploading it instead. |
| 3 | Why is the AI giving outdated information (e.g., old shipping rates, old prices)? | The AI caches data from the sources it learned. To fix: (1) Go to **AI Assistant > Data Sources > Custom Knowledge**; (2) Find the relevant URL or Q&A; (3) Click **Re-sync** to force an update. Also review all URLs in Custom Knowledge for any that haven't been re-synced recently. After re-syncing, test the AI to confirm it now returns the correct information. |
| 4 | The AI is referencing products from a different website or giving wrong product links. | This usually means the AI matched a query to incorrect backend data (e.g., a collection lookup). Contact support with the specific conversation ID so the team can add an instruction hook to guide the AI's response logic. As a preventive step, ensure product descriptions are detailed and unambiguous. |
| 5 | Can I add product-specific FAQs, or do I need to add a FAQ for every product? | You only need product-specific FAQs for products with special information not covered in the product description. If a product's description already contains all the details you want the AI to answer, no additional FAQ is needed. |
| 6 | Does adding product FAQs help with "View Similar" recommendations? | No — product FAQs do not influence the "View Similar" product recommendation feature. Recommendations are handled through the Smart Recommendations settings, not FAQ data. |
| 7 | The AI is not syncing enough products — my plan limit is too low. | Each plan has a product sync limit (Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000). If you have hit the limit, contact support — they can extend you up to the next plan's limit as a temporary accommodation. For permanent higher limits, upgrading your plan is the solution. If you have more than 5,000 products, contact support directly as this requires a manual backend configuration. |
| 8 | How do I sync a specific product manually? | Go to **AI Assistant > Data Sources > Products**, search for the product by name, and enable/sync it manually. After syncing, refresh your browser to see the updated data. |
| 9 | The AI is not syncing all my products — some show as inactive or unavailable. | The AI only learns from products marked as **Published** in Shopify with in-stock inventory. Draft or inactive products are excluded. You can manually set individual products as Active or Inactive in the Product Knowledge list. If inactive products are still appearing, contact support to have them removed from the AI's training data. |
| 10 | How do I prevent the AI from recommending products from a different store's catalog (e.g., AVADA collections)? | Contact support with the specific conversation ID. This is typically caused by the AI matching against backend collection data incorrectly. The team will add an instruction hook to prevent this behavior. |
| 11 | Can the AI answer questions based on our website content automatically? | No — the AI does not automatically read your website. You must submit specific page URLs to the **Custom Knowledge** section so it can learn the content of those pages. Submitting just the domain (e.g., yourstore.com) only trains on the homepage content. |
| 12 | What AI model does Chatty use? | Chatty uses its own AI assistant layer built on top of large language model technology. The specific underlying model is not publicly disclosed, but the AI is optimized for e-commerce support scenarios. |

---

## AI Assistant — Behavior & Instructions

| No | Question | Answer |
|----|----------|--------|
| 13 | How do I set a custom name, avatar, and tone for my AI? | Go to **AI Assistant > Settings**. Here you can set the bot name, upload an avatar, write a welcome message, and configure the AI's personality and behavior in the **Instructions** field. Use the "Create with AI" option to auto-generate a structured instruction based on your store type. |
| 14 | The AI is answering in the wrong language (e.g., responding in Chinese/Japanese when the customer wrote in another language). | The AI is designed to respond in the customer's language. If it's getting confused — especially for very short messages or ambiguous text — contact support with the conversation ID. The team can add an explicit instruction: "Always reply in the same language the customer is using." |
| 15 | How do I stop the AI from providing incorrect information (e.g., wrong contact email, wrong price)? | (1) Review **AI Assistant > Data Sources** — check that all sources have accurate, up-to-date content; (2) Go to the AI conversation in your Inbox, click **Review Sources** on the AI's response to see which source it pulled from, then correct that source; (3) Add a Custom Q&A or Scenario Instruction to explicitly override incorrect behavior. |
| 16 | Can I configure scenarios for specific customer situations (e.g., order cancellation, returns, product abbreviations)? | Yes — go to **AI Assistant > Instructions > Assistant Skills > Add Custom Scenario**. Scenarios let you define specific situations and how the AI should respond. Examples: handling product abbreviations, guiding customers to your TCGPlayer store for singles, redirecting after-sales requests. |
| 17 | The AI is repeating information from a previous auto-reply FAQ when answering a follow-up question. | This is a known bug. Contact support with the specific conversation ID — the dev team can investigate and fix the response logic so the AI does not repeat content already shown in the auto-reply. |
| 18 | Can I use a Custom Scenario to handle a situation where the AI should not add a product to the cart? | Scenario Instructions can set behavioral guidelines, but some default AI actions (like the Add-to-Cart button appearing when recommending products) are system-level behaviors. If you need to suppress ATC functionality specifically, contact support — the team can apply a custom instruction or CSS/code solution. |
| 19 | How do I make the AI always provide our contact phone number when customers ask about contacting support? | Two approaches: (1) Add the phone number to your **General AI Instructions** so the AI references it broadly; (2) Create a **Custom Scenario** (AI Assistant > Instructions > Assistant Skills > Add Scenario) that triggers whenever a customer asks about contacting the team, and have it provide the email and phone number. |
| 20 | Can Chatty AI check whether a customer has an account or loyalty points? | No — Chatty AI cannot access customer account data (login status, loyalty points balance, etc.). As a workaround, create a Custom Scenario that directs customers to your login/registration page when they ask about rewards or account-specific questions. |
| 21 | How do I restore AI Instructions if they were accidentally deleted? | Contact support immediately. The team may be able to recover a previous version from backend logs. Going forward, keep a copy of your Instructions text saved externally (e.g., in a Google Doc). |
| 22 | Can I increase the character limit for Custom Scenario instructions? | Currently the character limit for individual scenario fields cannot be increased. However, the team can help you optimize and shorten the scenario text to fit within the limit. Contact support for assistance. |

---

## AI Assistant — Transfer to Human & Notifications

| No | Question | Answer |
|----|----------|--------|
| 23 | How does a customer request to speak to a human agent? | Customers simply ask the AI something like "Can I talk to a real person?" or "Connect me to a human." The AI will then trigger the human handover based on your settings in **AI Assistant > Instructions > Assistant Skills > Human Handover**. There is no dedicated button for this — it's handled conversationally. |
| 24 | Can I set up the AI to transfer conversations to a human after a fixed time without a response? | This is not currently a built-in feature. A feature request for "Auto-assign AI conversations to a human team after a fixed time" has been noted by the product team for consideration on the roadmap. |
| 25 | The AI is transferring conversations to human agents randomly, even when customers haven't asked. | This is typically caused by a conflict in your FAQ or scenario settings — an FAQ that "intercepts" conversations before the handover logic resolves correctly. Solutions: (1) Move relevant FAQ content to the "Outside Working Hours" section; (2) Add a supplementary scenario question to clarify the flow. Contact support with conversation IDs and the team will diagnose and fix it. |
| 26 | The AI is not transferring to a human agent even when the customer explicitly asks. | Check your **Pre-transfer message** in Human Handover settings — if it references an email option, the AI may interpret the customer's "yes" as agreement to contact via email rather than a live transfer. Revise the pre-transfer message to guide the AI toward the intended action. Contact support for help adjusting the wording. |
| 27 | Can I configure the AI to send contact details via email instead of doing a live transfer? | Yes — go to **AI Assistant > Instructions > Assistant Skills > Human Handover** and configure the handover to send the conversation details to your support email instead of assigning to a live agent. Contact support if you need help configuring this. |
| 28 | How do I receive a notification when a customer wants to speak to a human? | Go to **Settings > Notifications** and enable email notifications. Also ensure the team member who handles escalations has the **"There is a conversation assigned to me"** email notification enabled in their personal Notification settings. If using automatic assignment to a specific agent, that agent must have notifications enabled. |

---

## AI Assistant — Analytics & Metrics

| No | Question | Answer |
|----|----------|--------|
| 29 | What do the three AI metrics mean — AI engagement rate, AI resolution rate, and answer rate? | **AI Engagement Rate**: percentage of total conversations where the AI participated (including those later transferred to human). **AI Resolution Rate**: percentage of AI-handled conversations fully resolved by AI without any human involvement. **Answer Rate**: percentage of customer questions where the AI had enough knowledge to provide an answer (reflects knowledge base coverage). In short: Engagement = did AI join? Resolution = did AI solve it alone? Answer rate = did AI have the knowledge? |
| 30 | The AI resolution rate seems to include conversations where a human agent also intervened. | This is a known analytics calculation issue. If your numbers don't add up (e.g., AI resolved + human participated > total conversations), contact support with your date range and the team will investigate the counting logic. |
| 31 | How is the "Total Sales" figure in Analytics calculated? | Analytics tracks orders placed by customers after they interacted via chat — these are "assisted" sales. If a customer chats and then completes a Shopify checkout, the order amount is included. Payments made outside Shopify or through non-tracked channels may not be counted. |
| 32 | Is there a report for average resolution time per agent? | Not yet as a built-in report. The product team has accepted a feature request to add **resolution time** and **handle time** to the Agent Report section. You will be notified once this is released. |
| 33 | Agent conversations are showing zero resolved conversations in Analytics even though they replied to many chats. | This is usually an assignment setting issue. Check **Settings > Automation** — if set to "Conversations stay with assigned member (or stay unassigned)," conversations handled by a specific agent won't be counted unless they were explicitly assigned. Change to **"Conversations will be assigned to whoever replies"** so conversations are attributed correctly. Note: this setting change does not retroactively update past Analytics data. |

---

## AI Assistant — Limits & Extensions

| No | Question | Answer |
|----|----------|--------|
| 34 | What are the AI conversation limits per plan? | Free: 50 lifetime. Basic: 50/month. Pro: 300/month. Plus: 700/month. Extra conversations beyond the monthly limit are charged at $0.40 each. You can set a spending cap in your subscription settings. |
| 35 | My AI conversation limit has been reached — what do I do? | Once the limit is reached, the AI will stop responding. Options: (1) Upgrade to the next plan for a higher monthly limit; (2) Purchase additional conversations at $0.40 each; (3) Contact support to request a temporary extension (requires PM approval). |
| 36 | Can support extend my product, URL/file, or custom answer limits? | Yes — CS agents can extend these limits up to the next plan's level as a one-time accommodation. For example, a Basic store can be extended to Pro limits (8,000 products, 500 URLs). Contact support and specify what you need. |
| 37 | What is the limit for AI Scenarios and can it be extended? | Free/Basic: 5 scenarios. Pro: 15 scenarios. Plus: no limit. Extensions beyond plan limits require PM approval. Contact support and explain your use cases — the more specific you are, the faster the request can be processed. |
| 38 | I have more than 10,000 products — can I still use AI product recommendations? | Yes, but it requires a manual backend configuration beyond the standard 5,000-product limit. Contact support and provide your total product count and monthly order volume. For stores with 10,000+ products and 100+ orders/month, a demo call with the product team is recommended. |

---

## Widget & Chatbox

| No | Question | Answer |
|----|----------|--------|
| 39 | The chat widget is not showing on my website. | Common causes: (1) App embed is not enabled in Shopify — go to **Online Store > Themes > Customize > App Embeds** and enable Chatty; (2) Display rules are set to show on specific pages only — check **Chatbox > Advanced > Display Settings**; (3) Chatbox is toggled off — check **Chatbox > General** and enable it. After making changes, hard-reload the page (Ctrl+Shift+R). |
| 40 | How do I show the widget only on specific pages, or hide it on certain pages? | Go to **Chatbox > Advanced > Display Settings**. You can choose to show on specific pages or hide on specific pages. When adding a URL, use only the path portion (e.g., `/pages/contact`), not the full URL. |
| 41 | How do I adjust the position of the chat widget (move it higher, lower, left, right)? | Go to **Chatbox > Appearance > Alignment** to switch between left and right. For fine-tuned pixel adjustments (e.g., move 20px from bottom), go to **Chatbox > Advanced > Custom CSS** and add custom CSS positioning code. Contact support if you need help writing the CSS. |
| 42 | Can I resize the chat bubble icon? | Yes — go to **Chatbox > Appearance** to adjust the icon size and style. For a percentage-based resize (e.g., reduce to 60% of original), a custom CSS code can be added via **Chatbox > Advanced > Custom CSS**. Contact support to help apply this. |
| 43 | The chat widget is overlapping other elements on my page (e.g., cart drawer, sticky bars). | This is a z-index issue. Contact support — the team can add a custom CSS snippet to adjust the widget's z-index so it does not interfere with other elements. Provide a screenshot or recording showing the overlap. |
| 44 | Can I embed the chat widget directly into a page section (not floating)? | Yes — use the **Embedded Chatbox** feature. Go to **Chatbox > Embedded** to get the embed code. Note: embedding a fully functional AI chat widget into a Hero Banner or homepage section is in development. For now, the embedded option works within page content sections. |
| 45 | How do I remove or change the starter questions / conversation starters shown in the chat? | Go to **Chatbox > Chat Page > Conversation Starter** and edit or remove them. These are separate from the AI's FAQ data — they are preset buttons shown in the chatbox UI. |
| 46 | Can I disable the "View Similar" button that appears in AI product recommendations? | Currently there is no on/off toggle for this button in settings. Contact support — the team can hide it using custom CSS via **Chatbox > Advanced > Custom CSS**. |
| 47 | The chat widget button shows the wrong shape or icon on mobile. | This is usually caused by custom CSS in the app settings that conflicts on mobile. Contact support with a screenshot — the team will review and correct the CSS. |
| 48 | What is "Away Mode"? | Away mode allows individual team members to appear offline to customers without logging out of the app. When enabled: the storefront shows that staff member as unavailable; if all staff have Away mode on, customers see the store as offline. It resets automatically when the member logs out and back in. Activate it via the toggle at the top of the Chatty app interface. Useful for lunch breaks, meetings, or when unavailable to take new chats. |

---

## Live Chat & Inbox

| No | Question | Answer |
|----|----------|--------|
| 49 | How do I invite team members to Chatty? | Go to **Settings > Team > Invite Member**. Team member limits per plan: Free: 1, Basic: 5, Pro: 10, Plus: unlimited. The invited member will receive an email to activate their account — make sure they click the activation link before trying to respond to chats. |
| 50 | Can a deactivated team member still access my Chatty account? | No — once a member is deactivated or removed from the team, they lose access to the Chatty inbox. The only exception is the Admin account, which cannot be deactivated. |
| 51 | How do I manually reassign a conversation from a human agent back to the AI? | In the Inbox, open the conversation and look for the assign/reassign option — select the AI assistant as the assignee. Note: the customer must send a new message after reassignment for the AI to start handling the conversation again. |
| 52 | How do I reply to a conversation as myself (not as admin) so my name shows in the chat? | Each team member should log in with their own Chatty account. If replies are showing as "Admin," check **Settings > Automation** — the assignment rule may be keeping conversations assigned to the admin instead of routing to whoever replies. Change the setting to "Assign to whoever replies" to resolve this. |
| 53 | Can I manage chats from multiple Shopify stores in one Chatty account? | No — each Shopify store has its own separate Chatty app instance. You would need to log into each store's Chatty separately. There is no multi-store unified inbox at this time. |
| 54 | Is there a way to mark all messages as read at once? | A "Mark all as read" feature is not available yet. This has been submitted as a feature request to the product team. |
| 55 | How do I export conversation history? | Chatty does not currently support self-serve conversation export with date range filters from the app UI. Contact support and provide the date range — the team can export the data as a CSV/JSON file and send it to your email. For large exports, allow 2–3 business days. |
| 56 | Can I save chat history via API? | The Chatty Public API does not currently support saving chat history via API endpoint. However, if you integrate with **Zendesk**, all Chatty conversations are automatically saved as Zendesk tickets when marked as resolved. The support team can also manually export transcripts. |
| 57 | What does the AI star icon on a conversation in the Inbox mean? | The star icon indicates that the conversation is currently being handled by the AI assistant. |

---

## Email Channel

| No | Question | Answer |
|----|----------|--------|
| 58 | How do I set up email forwarding in Chatty? | Go to **Settings > Channels > Email** and follow the step-by-step instructions. For most providers, choose your email provider from the list, or select "Others" for GoDaddy, Zoho, or custom setups. The verification link is sent to Chatty's side (not your inbox) — click the "Get Verification Link" button inside the app to confirm. See: https://help.chatty.net/live-chat/channels/email |
| 59 | I'm not receiving the email verification link when setting up my email channel. | The verification email is not sent to your inbox — it goes to Chatty's system. To verify, go back to the Email channel setup in the app and click **"Get Verification Link"** or **"Resend email"** — then click the confirmation link inside the app interface (Step 3 of the setup). |
| 60 | Email forwarding from Hotmail/Outlook is not working. | Organizational Outlook/Hotmail accounts often block auto-forwarding rules by default. Your IT admin will need to allow external email forwarding in the Exchange/M365 settings. This is a Microsoft policy restriction, not a Chatty issue. |
| 61 | Can I receive messages from multiple email addresses in Chatty? | Currently, Chatty supports one email per store via forwarding. Contact support if you have specific needs around multiple email addresses or alias setups. |
| 62 | When the AI replies to an email conversation, does the customer receive the response? | Yes — replies sent through Chatty (by AI or human agents) are delivered to the customer's email. The default sender address is noreply@chattyemail.com unless you have configured a custom sender domain. |
| 63 | How can I use Klaviyo to send outreach emails and have Chatty handle the replies? | Set up your Klaviyo campaign with a **Reply-To** address that is connected to a Chatty email channel. When leads reply to the email, their response will appear in Chatty's inbox as a new conversation, where AI or your team can take over. |

---

## WhatsApp & Social Channels

| No | Question | Answer |
|----|----------|--------|
| 64 | What do I need to connect WhatsApp to Chatty? | You need: (1) A Facebook Business page; (2) A WhatsApp Business account linked to that Facebook page; (3) Admin access to both; (4) Two-Factor Authentication (2FA) enabled in WhatsApp Business settings; (5) Your WhatsApp Business phone number approved by Meta. See the full guide: https://help.chatty.net/live-chat/channels/whatsapp |
| 65 | My WhatsApp number has been showing "Pending" status for several days. | The most common cause is that Two-Factor Authentication (2FA) has not been enabled on the WhatsApp Business account. This must be done by someone with Business Admin role: go to **WhatsApp Manager > Phone Numbers > Settings (gear icon) > Two-step verification > Enable**. Also confirm your Facebook Business account is verified and approved by Meta. |
| 66 | My WhatsApp number is already connected to another app (e.g., Bitespeed). Can I switch to Chatty? | Meta policy allows a WhatsApp Business API number to be managed by only one Business Solution Provider (BSP) at a time. To switch to Chatty, you must either migrate the number (disconnect from the current BSP and reconnect via Meta Business Manager) or create a new WhatsApp Business Account and associate the same phone number with it. Contact support for guidance on the migration process. |
| 67 | Can I use Chatty AI to answer WhatsApp messages without showing the widget on my website? | Yes — once WhatsApp is connected, go to **AI Assistant > Settings** and enable the AI for the WhatsApp channel. The AI will respond to WhatsApp messages using the same training data and settings as the website chatbox. Access WhatsApp conversations via the Inbox > WhatsApp tab. |
| 68 | Can I initiate (send first) WhatsApp messages to customers from Chatty? | No — Chatty currently only supports responding within existing WhatsApp conversations. You cannot initiate new outbound WhatsApp messages from Chatty to contacts who haven't messaged you first. |
| 69 | Instagram story replies are showing an error in Chatty's Inbox. | Chatty currently supports Instagram text and image messages only. Unsupported message types include: story replies, reel shares, voice messages/audio, stickers, post shares, and vanish mode messages. The team is working on expanding support for these formats. |
| 70 | Messages I send directly in Instagram/Facebook Messenger are not showing in Chatty Inbox. | Replies made directly in the Meta platform (not via Chatty) may not sync back to the Chatty inbox. This is a known limitation — a feature request has been filed to improve sync coverage for replies made outside of Chatty. |
| 71 | The AI is not responding to Instagram messages. | Go to **AI Assistant > Settings** and check if the AI is enabled for the Instagram channel — there is a per-channel toggle. Enable it and the AI will start responding automatically. Previously unhandled messages will continue to be assigned to agents by default until the toggle is on. |

---

## FAQ Builder

| No | Question | Answer |
|----|----------|--------|
| 72 | How do I add the FAQ block to a page (e.g., a blog post or collection page)? | After creating your FAQs in the app, go to your Shopify theme editor > select the page template > click "Add block" > find the Chatty FAQ block. For collection pages, if you want unique FAQs per collection, you need to create separate Collection templates for each collection and assign the corresponding FAQ block ID to each template. See: https://help.meetchatty.com/build-faqs/faqs-block |
| 73 | The FAQ page is not showing after reinstalling the app. | Check **Shopify Admin > Online Store > Pages** for orphaned FAQ pages from the previous installation. Re-enable the correct page or re-assign the Chatty FAQ template. Also check that the FAQ block is properly embedded in your theme. |
| 74 | An FAQ page URL I submitted to AI training is failing to sync. | The most common cause is that the page exceeds the 25,000 character limit. As a workaround: export the FAQ content as a file (CSV, TXT, or PDF) and upload it to **Custom Knowledge** instead. This is not a plan limitation — it's a system engineering constraint. |
| 75 | How do I assign different FAQ blocks to different collection pages without them appearing on all collections? | Create separate Collection page templates in Shopify (one per collection), then assign each template to its specific collection and add only the relevant FAQ block ID to each template. Using one shared Default Collection template means all collections share the same blocks. |
| 76 | Can I translate my FAQ content? | Yes — go to **Settings > Translations** to manage FAQ text in different languages. If a FAQ was updated and the translation shows "Outdated," edit and re-save the FAQ in the app to force the translation to refresh. |

---

## Notifications & Mobile App

| No | Question | Answer |
|----|----------|--------|
| 77 | How do I set up notifications for new incoming conversations? | Go to **Settings > Notifications** and enable web push and/or email notifications. Use the "Send test" button to verify notifications are working. For mobile, install the Chatty web app (see Q78) and enable push notifications after installation. |
| 78 | How do I install Chatty on my phone (iOS or Android)? | Chatty uses a mobile web app (PWA), not a native App Store app. To install: (1) In the Chatty app, go to **Inbox > Download Chatty App** and scan the QR code; (2) On iPhone: tap the Share icon > "Add to Home Screen." On Android: tap the browser menu > "Add to Home Screen"; (3) Open the installed app from your home screen; (4) Go to the 3-dot menu > Settings > Notifications > Allow. Make sure Silent mode and Do Not Disturb are off. |
| 79 | I'm not receiving push notifications on my iPhone for new chats. | Steps to fix: (1) Confirm the Chatty web app is opened from your Home Screen (not browser); (2) In the app, go to Settings > Notifications and tap "Allow" if not already done; (3) Go to iPhone Settings > Notifications and verify Chatty is listed with Banners, Sounds, and Badges enabled; (4) Check that Silent mode / Do Not Disturb is not blocking notifications; (5) If still not working, remove the web app from Home Screen, re-add it, and repeat the steps to trigger a fresh notification prompt. |
| 80 | I'm not receiving email notifications when a conversation is transferred to a human. | Check: (1) **Settings > Notifications** — email notifications must be enabled; (2) If conversations are auto-assigned to a specific team member, that member must enable "There is a conversation assigned to me" in their own notification settings; (3) Check spam/junk folder; (4) Ensure you have not previously unsubscribed from Chatty notification emails. |
| 81 | How do I access Chatty from the mobile web app when I'm away from my computer? | In the Chatty app dashboard, go to **Inbox** and click the "Open Web App" or "Download Chatty App" button. You can also access app.chatty.net directly from your mobile browser. |

---

## Billing & Plans

| No | Question | Answer |
|----|----------|--------|
| 82 | What plans does Chatty offer and what are the prices? | Free (no charge), Basic ($19.99/month), Pro ($68.99/month), Plus ($199.99/month). Annual billing saves approximately 15%. A 7-day free trial is available on paid plans, and a 30-day money-back guarantee applies. See plan comparison: https://help.chatty.net/product-roadmap/pricing#compare-plans |
| 83 | Are there extra charges beyond the monthly plan fee? | Yes — extra AI conversations beyond your monthly limit are charged at $0.40 each. You can set a spending cap in your subscription settings to control this. Human agent responses have no per-conversation charge. |
| 84 | I was charged but I thought I was on the Free plan / I started a trial and forgot to cancel. | Chatty does not automatically upgrade plans. However, if you signed up for a paid trial (e.g., 7-day Basic trial) and did not downgrade before the trial ended, Shopify charged you when the new cycle began. To stop future charges, go to **Settings > Subscription** and select the Free plan. For a refund, contact support with a screenshot of the Shopify charge (showing app name, billing cycle, and amount) — the team will review and process a refund if applicable. |
| 85 | How do I cancel my subscription / downgrade to Free? | Go to **Settings > Subscription > Plan > Select Free Plan** and confirm. Do this before your next billing cycle to avoid charges. Downgrading does not delete your data or settings. |
| 86 | I have a discount code — how do I apply it? | Go to **Settings > Subscription** and enter the code in the Discount Code field before upgrading. If the code shows as invalid, make sure you are on the correct plan (some codes are plan-specific). Contact support if the code still doesn't work. |
| 87 | I was previously on a legacy pricing plan and my price changed without notice. | Contact support with a screenshot of your Shopify billing history. If you had an active discount or legacy pricing that should have been honored, the team can escalate to the billing team to review and restore your previous pricing. Refunds for the price difference can be requested if applicable. |
| 88 | Where can I see my Shopify app credits for Chatty? | Go to **Shopify Admin > Settings > Billing > App credits**. Credits appear here and can offset future app usage charges. |
| 89 | I received an unexpected extra usage charge. What happened? | Extra charges appear when AI conversations exceed your monthly plan limit. If you believe the charge was incorrect (e.g., a system miscalculation), contact support with a screenshot of the Shopify billing section — the team will investigate and process a refund if the charge was an error. |

---

## Account & Settings

| No | Question | Answer |
|----|----------|--------|
| 90 | How do I set up online/offline hours for live chat? | Go to **Settings > General > Chat Availability** and configure your business hours. When outside set hours, the widget will display your store as offline. To have the AI take over when agents are offline, go to **AI Assistant > Settings > AI Availability** and select "Only when agents are offline." |
| 91 | If I'm logged into Chatty outside business hours but don't want to appear online, what do I do? | Use **Away Mode** — toggle it on at the top of the Chatty app. This makes you appear offline to customers even while logged in. It resets when you log out and back in. If all agents have Away mode on, customers see the store as fully offline. |
| 92 | How do I change the AI's welcome message? | Go to **AI Assistant > Settings** (not Chatbox settings). The welcome message for AI-handled conversations is set here. Changes in Chatbox settings only affect the non-AI chatbox appearance. |
| 93 | How do I require customers to provide their name and/or email before chatting? | Go to **Chatbox > Chat Page > Pre-chat Form**. Enable the pre-chat form and configure which fields to require. To allow completely anonymous chat (no form), select "Chat as anonymous." You can also customize to require email only (no name) or name only. |
| 94 | How do I set up the Proactive Chat (auto-triggered welcome message)? | Go to **Proactive Chat settings** in the app. You can configure triggers based on time on page, specific page URLs, or other visitor behaviors. The delay timing for the welcome message popup is also configured here. |
| 95 | Does Chatty have real-time translation for conversations between agents and customers? | Yes — **Real-time Translation** is available on Pro and Plus plans. It allows automatic translation between the agent's language and the customer's language within the Inbox. Go to **Settings > Translation** to configure languages. |
| 96 | What languages does the auto-translation support? | Free: 1 language, Basic: 2, Pro: 9, Plus: unlimited. Languages must be added in Shopify Admin > Settings > Languages first before they appear in Chatty's translation settings. |
| 97 | Can I connect all channels (Gmail, Facebook, Instagram, WhatsApp) and manage everything in one inbox? | Yes — go to **Settings > Channels** and connect each channel. Once connected, messages from all channels appear in the unified Chatty inbox. A single team member can manage all channels from one place. |
| 98 | How do I set up a contact form so customer submissions come to my email? | Go to **AI Assistant > Instructions > Assistant Skills > After-sale Support** (or equivalent contact form settings) and add your support email address. When customers submit the form, the details will be forwarded to that email. |
| 99 | Can I access Chatty from the Shopify admin or only from app.chatty.net? | Both. You can access Chatty from the Shopify Apps section or directly at https://app.chatty.net. The web app offers a more complete experience and is recommended for full inbox management. |
| 100 | How do I change the date format displayed in my billing date (e.g., "04/12/2026")? | Chatty uses MM/DD/YYYY format. "Renews on 04/12/2026" means April 12, 2026 — not December 4. |

---

## Integrations & API

| No | Question | Answer |
|----|----------|--------|
| 101 | Does Chatty have a public API? | Yes — the Chatty Public API provides access to your store's customer data (contacts, chat history timestamps, order counts, total spend). It's primarily for custom integrations: syncing contacts to a CRM, pulling data into spreadsheets, or building internal dashboards. Detailed endpoint documentation (beyond API key generation) is not yet publicly available. See: https://help.chatty.net/integrations/chatty-public-api |
| 102 | Does Chatty integrate with Zendesk? | Yes — when a conversation is resolved in Chatty, a ticket is automatically created in Zendesk with the full transcript and customer details. Note: sync happens on resolution, not in real-time. Customers who want Zendesk as long-term chat history storage should resolve conversations in Chatty to trigger the sync. |
| 103 | Does Chatty integrate with HubSpot? | A direct native HubSpot integration is not available yet. You can use the Chatty Public API with a custom setup or tools like Zapier to sync data to HubSpot. The product team has noted this as a potential future integration. |
| 104 | Does Chatty integrate with Klaviyo? | Yes — the Klaviyo integration lets you sync Chatty contacts, tags, and conversation data to Klaviyo for targeted email/SMS campaigns. This is a one-way data sync (Chatty → Klaviyo). See: app Settings > Integrations > Klaviyo. |
| 105 | Does Chatty support adding a size guide for AI training? | Yes — the size guide AI Skill is available on Pro plan and above. Go to **AI Assistant > Train AI > AI Skills > Size Guide** to configure it. For Free/Basic plans, you can try uploading a size guide as a file (Excel/CSV) to Custom Knowledge, though this is less reliable for complex sizing logic than the dedicated feature. See: https://help.chatty.net/ai/train-ai/ai-skills/size-guide |
| 106 | Can I connect Chatty to my existing WhatsApp support system via API? | The Chatty Public API provides data access but does not offer a full WhatsApp messaging API integration out of the box. For deep custom integrations, development work on your side would be needed. Contact support to discuss your use case in detail. |

---

## Getting Started & General

| No | Question | Answer |
|----|----------|--------|
| 107 | How do I get started with Chatty? | (1) Install Chatty from the Shopify App Store; (2) Enable the app embed in your Shopify theme (**Online Store > Themes > App Embeds**); (3) Enable Live Chat in **Chatbox > General > Live Chat**; (4) Activate your admin account in **Settings > Team**; (5) Enable the AI Assistant and add data sources; (6) Set up notifications. You can also use the in-app Setup Guide to walk through each step. |
| 108 | Is Chatty just for live chat or does it also have an AI bot? | Chatty combines both — a **live chat** system for real-time agent responses and an **AI Assistant** that can handle conversations 24/7 automatically. The AI and human agents share the same inbox. You can configure the AI to handle all conversations, or only when agents are offline. |
| 109 | Can I book a demo call to get a walkthrough of Chatty's features? | Yes — if you are a high-potential merchant, considering a paid plan upgrade, or need AI training guidance, you can book a call at: https://cal.com/drake-q-fonihl/chatty-consultant. If you just need help with setup or troubleshooting, the live chat support team is available 24/7 and can assist directly. |
| 110 | Does Chatty work on headless Shopify sites? | Yes, Chatty can be installed on headless stores. Some features (like audio notification sounds flagged by accessibility tools like WAVE) may behave differently. The audio element is used for customer notification sounds and is a standard, harmless functional element — WAVE flags it for accessibility review, not as an error. |
| 111 | The app is not loading / showing a 404 error. | Try: (1) Hard reload the page (Ctrl+Shift+R / Cmd+Shift+R); (2) Clear browser cache and cookies; (3) Try a different browser; (4) Try incognito mode. If the issue persists across browsers, contact support — it may be a temporary backend issue. |
| 112 | Is there a way to ask my website visitors a question through the chat (outbound proactive message)? | Yes — use the **Proactive Chat** feature to trigger automated messages to visitors based on behavior (time on page, specific pages). This is configured in the Proactive Chat settings section of the app. Note: Proactive Chat is for outbound automated messages, not for manually initiating individual conversations from the Inbox. |
