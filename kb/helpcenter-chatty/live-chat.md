# Live Chat

## Setup
1. Enable Chatbox: Chatbox > General > Turn on
2. Enable Live chat block in Blocks section
3. Configure Pre-Chat Form: set required info (email mandatory; name, phone optional), allow anonymous chatting
4. Save and test on storefront

## Inbox
Central hub for all conversations across channels (live chat, email, Messenger, Instagram, WhatsApp).

**Filtering**: By status (Open, Resolved, Starred, Blocked, Unread), channel, or assignee (Your inbox, Unassigned, specific members).

**Actions**: Resolve, star, delete conversations. Assign to teammates. Add internal notes.

**Customer info visible**: Contact details, order history, tags, browsing activity, real-time cart.

## Customers in Inbox
Three types:
- **Guest (lead)**: Visitor who hasn't purchased. Shows email + customer icon.
- **Customer**: Has completed a purchase. Shows initials + full name.
- **Anonymous**: Used "Chat as anonymous". Random generated name.

Guests don't auto-convert to customers (prevents duplicates, incomplete records). Can manually convert by entering contact info in Inbox.

**Blocking**: Block user from conversation details. Blocked users can still send messages but won't get responses or notifications.

**Deleting**: Done in Contacts section. Deleting a contact deletes ALL their conversations.

## Conversation Details Panel
Shows during live chat: shopping cart, profile, browsing history, customer type.

Tools: custom attributes (e.g. "Priority: High"), related conversations, real-time behavior tracking, notes, checklists.

CSAT ratings display after conversations conclude.

## Real-time Translation (Pro+)
- Auto-detects customer language, shows in conversation and profile
- Auto-translates incoming messages to your default language
- **Live Translate**: Write in your language, preview translation before sending. Click Refresh after edits.

## Channels

### Email
- One email per store via forwarding
- Default sender: noreply@chattyemail.com (customizable with domain verification)
- Supports Gmail, Outlook, Zoho, Hostinger, Amazon SES, and more
- Outlook orgs may block forwarding (error 550 5.7.520). IT admin must allow it.
- Alias emails: verify primary first, then add aliases
- "Continue as email": customers switch from chat to email
- Conversation history sent when ticket marked solved
- Up to 5 CC email addresses on all outgoing messages

### Facebook Messenger & Instagram
- Connect via Facebook account, link fanpages
- Only one Facebook account at a time
- Can add multiple Pages from same account
- Messages show with platform icon in inbox
- Only Instagram business accounts connected to a Facebook Page
- Disconnecting preserves conversations but stops updates

### WhatsApp
- Multiple accounts supported
- Requires: Business Facebook page + WhatsApp Business account linked to it + admin access to both
- WhatsApp Templates required to initiate conversations (Marketing, Utility types; Authentication not supported)
- Personal WhatsApp accounts cannot be integrated
- "Pending" status = Meta approval processing
- Disconnecting preserves conversation history

## Proactive Chat
Targeted messages to visitors at strategic moments in shopping journey.

6 templates: Welcome visitors, Newsletter subscription, Product recommendations, Cart booster, Abandoned cart, Collection boost.

Targeting: specific pages, visitor type (new/returning), device type, timing (page load, scroll %, time delay).

Priority system when multiple campaigns could fire simultaneously.

## Contacts
Manage all customer contacts. View chat history, activity, orders, profile, tags, notes.

Export contacts as CSV (current page or all). Large exports sent via email.

Warning: Deleting a contact deletes ALL their conversations.

## Team
Invite members to shared inbox. Plan limits: Free = 1 admin, Basic = +2, Pro = +4.

**Assignment**: Manual (via Assignee field) or automatic rotation.
**Notes**: Private internal notes with @mention + push/email notifications.
**Team members can**: Respond across all channels, resolve, assign, access profiles, toggle online/offline status, switch between stores.

## Quick Replies
Pre-saved response templates. Access via icon or `/` command during chat.

Create with: shortcut name, category, response text. Can create/edit from within chat.

## Other Features

### Resolve Conversations
Manual: click Resolve button. Automatic: Settings > Automation (configurable inactivity period: 2-4h for busy stores, 24h for special support). Customer gets notice, can reopen by replying.

### Transcript
Email copy of complete chat history with timestamps. Enable in Settings > Channels > Email > Preferences. Both customers and team members can request.

### Satisfaction Survey
Post-conversation feedback: star ratings (1-5) or emoji scale. Configure trigger: "Conversation resolved" or keywords like "thank you". Customizable intro question and thank-you message.
