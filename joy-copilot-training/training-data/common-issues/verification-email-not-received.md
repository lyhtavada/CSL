---
category: Notifications
problem: Verification email not received when adding Custom Email Sender
source: notion
---

Q: I added a custom email sender in Joy but I never received the verification email. What should I do?
Q: The verification email for my custom sender isn't arriving. How do I fix this?
Q: I'm trying to verify my custom sender email in Joy but the verification email never comes through.
Q: Why am I not getting the verification email after adding my custom email sender in Joy?
Q: I've been waiting for the Joy custom sender verification email but it hasn't arrived. Help!

A: If you're not receiving the verification email after adding a custom email sender in Joy, here are the steps to troubleshoot:

### Step 1: Verify the Email Address is Valid
Make sure the email address you entered is correct and actually exists. You can use a free tool like [ZeroBounce](https://www.zerobounce.net/) to validate the email address.

### Step 2: Check All Folders
The verification email might have landed somewhere unexpected. Check these folders:
- **Spam / Junk** folder
- **Promotions** tab (Gmail)
- **Updates** tab (Gmail)
- **Other / Focused** inbox (Outlook)

### Step 3: Resend the Verification Email
In your Joy admin, go to the custom sender settings and click **"Resend verification email"**. Sometimes the first email can be delayed or lost.

### Step 4: Check Your DMARC Policy
Your domain's DMARC policy might be blocking the verification email. Use [MXToolbox DMARC Lookup](https://mxtoolbox.com/dmarc.aspx) to check.

If your DMARC record shows `p=reject`, this is likely blocking the verification email from being delivered.

### Step 5: Resolve DMARC Blocking
If your DMARC policy is set to `p=reject`, you have these options:
- **Use a Custom Sending Domain or Custom SMTP** (available on higher-tier plans) -- this is the most reliable solution.
- **Try a different email address** -- use an email on a domain without strict DMARC (e.g., a Gmail address for testing).

If none of these steps work, please share your email address and domain, and we'll look into it further!

Escalate khi: If the email address is valid, DMARC is not blocking, resend has been attempted multiple times, and the verification email still doesn't arrive -- escalate to dev team to investigate potential system issues.
