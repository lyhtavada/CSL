# Hi-Score Arcade — hiscorearcadecolorado.com

**Date:** 2026-09-16
**App:** Joy Loyalty
**Status:** Prospect — NOT on Shopify yet. Not a `/store-research` run (no Avada merchant/deal data exists); this is a pure web-discovery brief for demo-call prep.

## Business model

Hybrid business: physical arcade (Southern Colorado, 100+ games on freeplay) **+** online retail of anime/collectible goods (manga, anime figures, Gundam/Pokémon model kits, plush, merch).

Meta description: *"Southern Colorado's premier arcade with over 100 games on freeplay, also your source for manga, and anime figures!"*

## E-commerce — confirmed real, not a placeholder site

- ~408 live products in sitemap, across 6 categories: Gundam model kits / Pokémon model kits / merch / figures / plush / manga
- Has a `/return-policy` page and real checkout (`cdn3.editmysite.com/app/checkout`) — actually selling and shipping, not just a catalog
- Separate `/game-list` page listing arcade cabinets (physical side)

## Platform — Square Online (Weebly), NOT Shopify

- `<meta generator="Square Online">`, asset domain `editmysite.com`
- No Shopify footprint found: `/products.json` → 404, no Shopify script/CDN references anywhere in the HTML
- → Joy Loyalty cannot be installed yet; this is a pre-Shopify prospect

## Shopify-migration hypothesis — unconfirmed

No direct evidence found (no Shopify beta/coming-soon site, no public announcement). Platform config exposes feature flags `membership_registration` / `ecom.splash.loyalty` = true, but these are generic Square Online platform capability flags, not evidence of an active loyalty program — no real loyalty/rewards/membership page found on the site. Treat "about to migrate to Shopify" as a hypothesis to validate on the call, not a fact.

## Discovery questions for the call

1. Are you currently planning to migrate from Square Online to Shopify? What's the timeline, and what's driving the move (app ecosystem limits, checkout, managing retail + arcade inventory together)?
2. Do you currently run any loyalty/membership/punch-card program — for merch purchases, arcade play, or both (even offline)?
3. Would loyalty apply only to the online retail side, or should it also connect to in-store arcade play/spend (POS)? That's the biggest difference from a typical pure-online Joy prospect.
4. Your catalog (figures, model kits, manga) is a classic repeat-purchase/collector category — great fit for a points + tier mechanic. Worth using as a live example when demoing.
5. What's the main goal you're hoping a loyalty program achieves (repeat purchases, higher AOV, tying arcade visits to retail spend, competing with other collectible shops, something else)?
6. Have you run a loyalty/rewards program before — on Square, in-store punch cards, or anywhere else? What worked, what didn't?
7. Do you have a plan in mind already — budget range, which Shopify/Joy plan tier, or a rough go-live timeline?

## Key takeaway for Liz

Since the store isn't on Shopify, Joy Loyalty can't be configured live on their site. This call should function as a discovery/needs conversation + migration-plan validation, not a live-config demo on their real store.
