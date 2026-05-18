# Access & Login Issues

<!-- CHUNK: access-login-account-not-activated -->
```yaml
chunk_id: "case__access-login-account-not-activated"
doc_id: "cs-case-access-login-issues"
title: "Merchant sees 'Account not activated' when logging into Chatty"
category: "troubleshooting"
subcategory: "access-login"
tags: ["login", "account not activated", "app.meetchatty.com", "access", "activation"]
applies_when: "Merchant gets 'Account not activated' error when trying to log in to app.meetchatty.com"
priority: "high"
```

## Symptom

Merchant sees "Account not activated" error on app.meetchatty.com.

## Common Causes

1. Merchant has never opened Chatty from Shopify Admin after installing — no internal account was created.
2. App was uninstalled and reinstalled but the old account wasn't reactivated.
3. Merchant is trying to log in directly via external link instead of through Shopify Admin.
4. Browser has cached old data.

## Resolution — by role

**Admin (store owner):**
1. Open Chatty from **Shopify Admin → Apps → Chatty**.
2. Go to **Settings → Team** — an activation banner will appear there, click it to activate and create a password using their Shopify email.
3. After activation, they can log in at app.meetchatty.com normally.
4. If issue persists → clear browser cache and try again.

**Team member:**
1. Team members cannot self-activate — they need an invitation from the store admin.
2. Ask the merchant to go to **Settings → Team** and send an invite to the team member's email.
3. Team member accepts the email invite and creates their credentials.
4. After that, they can log in directly at app.meetchatty.com.

---

<!-- CHUNK: access-login-incorrect-password -->
```yaml
chunk_id: "case__access-login-incorrect-password"
doc_id: "cs-case-access-login-issues"
title: "Merchant or team member gets 'Incorrect email or password' on Chatty web app"
category: "troubleshooting"
subcategory: "access-login"
tags: ["login", "incorrect password", "wrong password", "sign in", "web app", "team member"]
applies_when: "Merchant or agent can't log in to app.meetchatty.com due to wrong email/password"
priority: "high"
```

## Symptom

"Incorrect email or password" error on app.meetchatty.com.

## Resolution

Ask the merchant which sign-up method they used:

**If they used "Create account" (custom password):**
- Log in with email + the password created during sign-up.
- If forgotten → click "Forgot password" to reset.

**If they used "Sign up with Google":**
- Click "Sign in with Google" and use the same Gmail account they signed up with.

Ask the merchant/agent which method they used first, then guide accordingly.

---

<!-- CHUNK: access-login-dev-store-blocked -->
```yaml
chunk_id: "case__access-login-dev-store-blocked"
doc_id: "cs-case-access-login-issues"
title: "Development store is blocked or shows 'Not Found' in Chatty"
category: "troubleshooting"
subcategory: "access-login"
tags: ["dev store", "blocked", "not found", "blacklisted domain", "competitor"]
applies_when: "A development store or user from a blacklisted domain cannot access Chatty"
priority: "medium"
```

## Symptom

App shows "Not Found" or blocks access on a development store.

## Cause

Chatty automatically blocks access from development stores with emails from blacklisted domains (competitors and known testing accounts).

**Blacklisted domains:** @tidio.com, @intercom.com, @firegroup.io, @flowio.app, @beae.com, @fireapps.vn, @channelwill.cn, @bsscommerce.com, @amasty.com, @secomus.com, @appsfinal.com, @omegatheme.com, @loox.io, @samita.io.

## Resolution

If the merchant's email belongs to a blacklisted domain, CS does not need to continue support — resolve the conversation.

---

<!-- CHUNK: access-login-china-white-screen -->
```yaml
chunk_id: "case__access-login-china-white-screen"
doc_id: "cs-case-access-login-issues"
title: "Does Chatty work in China? Google Cloud blocked by Great Firewall — VPN required"
category: "troubleshooting"
subcategory: "access-login"
tags: ["china", "white screen", "blank screen", "Great Firewall", "VPN", "Google Cloud", "access blocked", "work in China", "China store", "regional availability"]
applies_when: "Merchant asks if Chatty works in China, or a merchant located in China sees a white/blank screen when opening Chatty"
priority: "medium"
```

## Chatty in China

Chatty may have limited functionality or not work at all in China because it is hosted on Google Cloud, which is commonly blocked by China's Great Firewall. Merchants in China should use a VPN to access the Chatty admin.

## Symptom

Merchant from China sees a blank white screen with console errors when opening Chatty.

## Cause

Chatty is hosted on Google Cloud, which is commonly blocked by China's Great Firewall.

## Resolution

1. Confirm the merchant is located in China.
2. If not using a VPN → guide them to use a reputable VPN that works in China.
3. If already using a VPN → suggest trying a different VPN or network.
4. Send the standalone link `https://app.meetchatty.com` and instruct them to try with VPN enabled.
5. If other apps work fine, explain Chatty's Google Cloud hosting limitation.
6. Escalate to dev only if VPN + standalone link still doesn't work.

---

<!-- CHUNK: access-login-multiple-stores -->
```yaml
chunk_id: "case__access-login-multiple-stores"
doc_id: "cs-case-access-login-issues"
title: "Managing multiple Shopify stores with one Chatty account"
category: "troubleshooting"
subcategory: "access-login"
tags: ["multiple stores", "multi-store", "switch store", "one account", "team member"]
applies_when: "Merchant asks how to manage or access Chatty across multiple Shopify stores"
priority: "low"
```

## How It Works

Each Shopify store requires its own Chatty installation. The merchant accesses each store's Chatty separately through their Shopify Admin.

For team members who work across multiple stores: they can be invited as team members on each store's Chatty installation and switch between them.

---

## Related
- faq_access-login-issues (login troubleshooting)
- faq_web-app (web app access and features)
