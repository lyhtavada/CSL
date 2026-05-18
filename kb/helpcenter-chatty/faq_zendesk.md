# Zendesk Integration

<!-- CHUNK: zendesk-integration-overview -->
```yaml
chunk_id: "faq__zendesk-integration-overview"
doc_id: "chatty-zendesk"
title: "How Chatty integrates with Zendesk to save resolved conversations as tickets"
category: "faq"
subcategory: "integrations"
tags: ["zendesk", "zendesk integration", "support tickets", "conversation history", "zendesk sync", "resolved conversations", "ticket creation"]
applies_when: "When a merchant asks how to connect Zendesk to Chatty or how conversations are saved to Zendesk"
priority: "medium"
```

## Zendesk Integration Overview

The Zendesk integration automatically saves resolved Chatty conversations to Zendesk as support tickets. When you resolve a conversation in Chatty, a ticket is created in Zendesk with the full conversation transcript and customer details.

**Why integrate Zendesk:**
- Automatically save all resolved conversations as Zendesk tickets
- Keep complete conversation history in one central system
- Track support performance across all channels
- Access customer records without manual work

## How to Connect

1. Go to **Settings** → **Integrations** → Find Zendesk → Click **Manage**
2. Enter your **Zendesk subdomain** (the first part of your Zendesk URL — e.g., if your URL is `yourstore.zendesk.com`, the subdomain is `yourstore`)
3. Click **Connect** → You'll be redirected to Zendesk's OAuth page
4. Click **Allow** to authorize Chatty
5. You'll be redirected back to Chatty with connection status showing **Connected**

## How It Works

**Automatic ticket creation:** When you resolve a conversation in Chatty, a ticket is created in Zendesk containing:
- Customer profile (name, email, contact details)
- Full conversation transcript
- Timestamp of the conversation

**Reopened conversations:** If you reopen and re-resolve a conversation, Chatty creates a new ticket instead of updating the existing one, so each support interaction is tracked separately.

> Note: Sync happens on resolution, not in real-time. To use Zendesk as long-term chat history storage, resolve conversations in Chatty to trigger the sync.
