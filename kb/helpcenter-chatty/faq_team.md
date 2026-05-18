# Team Management

<!-- CHUNK: team-invite-members -->
```yaml
chunk_id: "team__invite-members"
doc_id: "chatty-team"
title: "Invite team members to Chatty"
category: "team"
tags: ["invite", "team member", "add staff", "team", "seats", "how many members"]
applies_when: "Merchant wants to invite team members or asks how many team members they can have"
```

## Inviting Team Members

Team member limits by plan:
- **Free**: 1 seat (admin only)
- **Basic**: 2 additional members (3 total)
- **Pro**: 4 additional members (5 total)
- **Plus**: Unlimited members

**How to invite:**
1. Go to **Settings** → **Manage** in Teams
2. Click **Invite member**
3. Enter the member's name and email (email cannot be changed later)
4. Click **Invite** — invitation email is sent
5. Ask the member to check their email and click **Create account**

---

<!-- CHUNK: team-assign-conversations -->
```yaml
chunk_id: "team__assign-conversations"
doc_id: "chatty-team"
title: "Assign conversations to team members"
category: "team"
tags: ["assign", "conversation assignment", "auto assign", "round robin", "manual assign"]
applies_when: "Merchant wants to assign conversations to team members manually or automatically"
```

## Assigning Conversations

**Manually:**
1. Go to **Inbox** → select a conversation
2. In conversation details, go to **Assignee** → click **Assign** → select a team member

**Automatically (round-robin):**
Go to **Settings** → **Automation** → **Assignment** → **Automatic**

Chatty rotates new conversations to available team members in sequence. These auto-assignment settings also apply to conversations transferred from the AI assistant.

---

<!-- CHUNK: team-internal-notes -->
```yaml
chunk_id: "team__internal-notes"
doc_id: "chatty-team"
title: "Leave internal notes and mention teammates in conversations"
category: "team"
tags: ["internal notes", "notes", "mention", "@mention", "team notes", "private comment"]
applies_when: "Merchant wants to leave internal notes or mention teammates in a conversation"
```

## Internal Notes & Mentions

Internal notes are private comments visible only to your team — customers cannot see them. Use internal notes to leave instructions, flag issues, or coordinate with teammates inside a conversation.

**Leave a note:**
1. In a conversation, click the **Notes** tab
2. Type your note
3. To mention a teammate, type `@` followed by their name
4. Click **Send**

When you mention someone with `@`, they receive a push notification and email notification.

---

<!-- CHUNK: team-deactivate-member -->
```yaml
chunk_id: "team__deactivate-member"
doc_id: "chatty-team"
title: "Deactivated team member access"
category: "team"
tags: ["deactivate", "remove member", "access", "revoke access", "deactivated"]
applies_when: "Merchant asks if a deactivated team member can still access Chatty"
```

## Deactivated Team Members

Once a member is deactivated or removed, they **lose access** to the Chatty inbox. The only exception is the Admin account, which cannot be deactivated.

---

<!-- CHUNK: team-notification-human-request -->
```yaml
chunk_id: "team__notification-human-request"
doc_id: "chatty-team"
title: "Get notified when a customer wants to speak to a human"
category: "team"
tags: ["notification", "human request", "talk to human", "escalation notification", "assigned notification"]
applies_when: "Merchant wants to receive notifications when a customer asks to speak to a human agent"
```

## Notifications for Human Escalation Requests

Go to **Settings** → **Notifications** and enable email notifications.

Also ensure the agent handling escalations has **"There is a conversation assigned to me"** enabled in their personal Notification settings.

If using automatic assignment to a specific agent, that agent must have notifications enabled.

---

<!-- CHUNK: team-invitation-email-not-received -->
```yaml
chunk_id: "team__invitation-not-received"
doc_id: "chatty-team"
title: "Team member invitation email not received"
category: "team"
tags: ["invitation email", "invite not received", "team invite", "email not arrived", "Gmail spam", "resend invite"]
applies_when: "A team member didn't receive the invitation email from Chatty"
```

## Invitation Email Not Received

1. Ask the invitee to check their **spam/junk folder** — especially Gmail Promotions tab
2. If using **Google Workspace** → check both the Promotions and Spam folders
3. **Resend the invitation** from **Settings → Team**
4. If invite consistently fails → try a different email address (e.g., a personal Gmail instead of corporate)

> Corporate email providers and Google Workspace are the most common causes. Spam folder is the first thing to check.

---

<!-- CHUNK: team-multiple-simultaneous -->
```yaml
chunk_id: "team__multiple-simultaneous"
doc_id: "chatty-team"
title: "Can multiple team members use Chatty at the same time"
category: "team"
tags: ["multiple agents", "simultaneous", "concurrent", "team members online", "team limits"]
applies_when: "Merchant asks if multiple team members can use Chatty at the same time"
```

## Multiple Team Members Using Chatty Simultaneously

Yes — multiple team members can be logged in and handling conversations at the same time.

**Team member limits by plan:**

| Plan | Members |
|------|---------|
| Free | 1 (admin only) |
| Basic | 5 total |
| Pro | 10 total |
| Plus | Unlimited |

Each member can have different roles and configure their own notification preferences. Invite members via **Settings → Team → Invite member**.
