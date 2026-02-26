# Chatty — Knowledge Base

## Product Overview

Chatty is a Shopify app that helps merchants communicate with store visitors via live chat, automate customer support with an AI chatbot (powered by ChatGPT), and build self-serve FAQ help centers. Chatty is designed as an AI-first chat platform specifically for eCommerce stores, turning customer conversations into sales opportunities.

Built for Shopify badge. Available on Shopify App Store. 4.9 stars with 1,700+ reviews.

## Plans

| Feature | Free | Basic ($19.99/mo) | Pro ($68.99/mo) | Plus ($199.99/mo) |
|---------|------|--------------------|------------------|---------------------|
| AI conversations | 50 lifetime | 50/month | 300/month | 700/month |
| Additional conversations | N/A | $0.40 each | $0.40 each | $0.40 each |
| Products for AI training | 100 | 500 | 8,000 | 20,000 |
| Team members | 1 | 5 | 10 | Unlimited |
| Auto-translation languages | 1 | 2 | 9 | Unlimited |
| Chat history | 90 days | Unlimited | Unlimited | Unlimited |
| Email channel | 1 | 1 | 1 | 1 |
| Smart product recommendations | No | No | Yes | Yes |
| CSAT survey | No | No | Yes | Yes |
| Cart booster | No | No | Yes | Yes |
| Dedicated AI consultant | No | No | No | Yes |

Annual billing: ~15% savings. 7-day free trial for paid plans. 30-day money-back guarantee.

## Core Features

### Live Chat
Real-time messaging between merchants and store visitors. Key capabilities:
- **Inbox**: Unified inbox to manage all conversations. Includes customer details panel, conversation details, chat zone with rich text editor.
- **Channels**: Email, Facebook Messenger, Instagram, WhatsApp — all synced into one inbox.
- **Contacts**: Customer management with tags, notes, and conversation history.
- **Team**: Invite team members, assign roles, manage conversation assignments.
- **Quick Replies**: Pre-saved response templates for faster replies.
- **Proactive Chat**: Behavior-triggered messages to engage visitors (e.g., time on page, specific page visit).
- **Real-time Translation**: Auto-translate messages between merchant and customer languages.

### AI Assistant
AI-powered chatbot that handles customer questions 24/7, trained on the merchant's store data:
- **AI Conversations**: Automatic responses to customer questions. AI shows as assignee in conversation details. Team can join AI conversations at any time.
- **Chat Summary**: When conversation transfers to human, AI summarizes the full conversation with language detection, issue highlights, and response suggestions.
- **Data Sources**:
  - *Store data* (auto-synced): Products (name, description, variants, pricing, inventory, metafields), discounts, markets, FAQs, policies (shipping, return, privacy, terms).
  - *Custom data* (manual): Individual questions, URLs/websites, files (.JSON, .TXT, .PDF, .CSV — max 2MB).
  - Products sync daily at 12:00 AM PST. Only published, in-stock products are trained.
- **AI Skills**:
  - *Shopping skills*: Smart recommendations (bestsellers, new arrivals, sales, special occasions — auto top 20 by sales, updated daily), size guide (upload images, per-product assignment), inventory status.
  - *Customer support skills*: Transfer to human, refund/return form, order tracking in chat.
- **AI Settings**: Bot name, avatar, welcome message, custom instructions (tone, response style, specific scenarios), AI availability (based on team online hours), AI channels.
- **Test & Optimize**: Test zone to preview AI responses before going live. Review unresolved questions to improve training.

### Chatbox
The chat widget displayed on the merchant's storefront:
- **General**: Turn on/off chatbox, enable chat focus mode, set header (logo, heading, description), configure blocks (Contact us, Order tracking, FAQs, Categories).
- **Appearance**: Brand colors (preset or custom), chatbox button (launcher icon, size, alignment), chatbox style (navigation mode, mobile ratio).
- **Advanced**: Deep links (open specific chatbox sections via URL), display rules (devices, pages), continue-as-email, custom CSS.
- **Contact Button**: Add contact methods — supports 11 methods: WhatsApp, Messenger, Phone, Email, Instagram, Telegram, Skype, Line, Zalo, TikTok, SMS.
- **Embedded Chatbox**: Embed chatbox directly in page content instead of floating widget.

### FAQ Builder
Build a self-serve knowledge hub:
- **Categories**: Organize questions into categories with icons and descriptions.
- **Questions**: Add questions with rich text answers, assign to categories.
- **FAQs Page**: Dedicated FAQ page on the storefront with customizable theme.
- **FAQs Block**: Show selected FAQs inside the chatbox.
- **FAQs Analytics**: Track views, clicks, and search queries.
- **Export**: Export questions as CSV file.
- **Translation**: Translate FAQs into multiple languages.

### Order Tracking
Customers can track orders directly in the chatbox. Supports Shopify order tracking and third-party tracking integrations.

### Mobile & Web App
- **Mobile App**: Manage conversations on the go (iOS/Android). Receive push notifications for new messages.
- **Web App**: Browser-based admin dashboard at app.chatty.net.

### Integrations
- **Klaviyo**: Sync customer data (contacts, tags, conversation counts, timestamps) to Klaviyo for targeted email/SMS campaigns. Requires Klaviyo API key with Read/Write access for Lists and Profiles.
- **Zendesk**: Connect Zendesk for unified helpdesk management.
- **Joy Loyalty**: Show loyalty data (points, tier) in customer conversations.
- **Air Reviews**: Connect product reviews for AI training context.
- **Powerful Contact Form**: Integrate contact form submissions.
- **Website**: Connect external website for AI data training.

### Notifications
Configure notification preferences for new messages, assignments, and other events.

### Analytics
Track conversation metrics, AI performance, response times, and customer satisfaction.

### Online Hours
Set business hours to control online/offline status. Affects chatbox display and AI availability settings.

### Translation
Translate app interface and FAQs into multiple languages. Number of languages depends on plan.

### General Settings
App-wide configuration: branding, defaults, display preferences.

## Channel Details

### Email Channel
- Connect one email to Chatty via email forwarding.
- Default sender: noreply@chattyemail.com (customizable with domain verification).
- "Continue as email" feature lets customers switch from live chat to email.
- Conversation history sent to customer when ticket is marked solved.

### Facebook Messenger & Instagram
- Connect via Facebook account — link fanpages to sync messages.
- Messages appear in Chatty inbox with platform icon indicators.
- Disconnecting doesn't remove existing conversations.

### WhatsApp
- Connect multiple WhatsApp accounts.
- Requires: Business Facebook page, WhatsApp Business account linked to that page, admin access to both.

## Key Terminology

| Term | Meaning |
|------|---------|
| AI conversation | A customer chat handled by AI assistant |
| Transfer | When AI hands off conversation to a human agent |
| Data source | Information used to train the AI (products, FAQs, custom data) |
| AI skill | Specialized capability for AI (recommendations, size guide, etc.) |
| Chatbox | The chat widget displayed on the storefront |
| Deep link | URL that opens a specific chatbox section directly |
| Proactive chat | Automated messages triggered by visitor behavior |
| Quick reply | Pre-saved response template for faster messaging |
| Contact button | Floating button with multiple contact method options |
| CSAT | Customer Satisfaction survey (Pro+ plans) |
| Smart recommendations | AI-powered product suggestions based on collections |

## Common Issues

- **Chatbox not showing on store**: Check if chatbox is turned on (Chatbox > General > Turn on), app embed is enabled in Shopify theme editor, and display rules (devices/pages) aren't excluding the page.
- **AI not responding**: Verify AI assistant is turned on, live chat block is enabled in chatbox, data sources are synced, and AI has been trained on sufficient data.
- **Email channel not connecting (Outlook)**: Organization's Outlook settings may block automatic email forwarding. Contact IT admin to allow email forwarding.
- **Online status not showing**: Contact Us block must be enabled. Go to Chatbox > General > Blocks > turn on "Contact us".
- **WhatsApp not connecting**: Ensure you have a Business Facebook page, WhatsApp Business account linked to it, and admin access to both accounts.
- **Translation not showing on store**: Website must support the language first. In Shopify Admin > Settings > Languages, add and publish the language before enabling it in Chatty.
- **AI recommending wrong products**: Check Smart Recommendations collections in AI Skills. Disable smart sync if auto-selected products aren't relevant. Manually curate product lists.
- **FAQ page not showing after uninstall/reinstall**: After uninstalling, Chatty's code may remain disabled. Check Shopify Admin > Online Store > Pages for orphaned FAQ pages.
- **Order tracking not working**: Ensure Order Tracking block is enabled in chatbox. Verify Shopify order tracking info is properly set up.
- **Products not appearing in AI training**: Only published, in-stock products are trained. Products sync daily at 12:00 AM PST. Check product count against plan limit.

## Privacy & Compliance

- **AI Compliance**: Chatty's AI follows data privacy standards. Customer conversation data is used only for AI training within the merchant's store scope.
- **Cookie Policy**: Chatty uses cookies for session management and chatbox functionality.
- **Data Access**: App accesses customer data (names, emails, addresses, browsing behavior), store owner info, product catalogs, orders, and discounts to function.
