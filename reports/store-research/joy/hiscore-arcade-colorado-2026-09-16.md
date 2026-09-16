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

## How Joy Loyalty could help this store

Mapped from their business model (collector/repeat-purchase catalog + physical arcade repeat-visit traffic) — validate against their actual goals in Q5-7 above before pitching hard on any of these:

- **Points on purchase → repeat buys.** Collectibles (figures, model kits, manga) are a category where customers return for the next drop/release. Points-per-dollar + "earn toward your next figure" framing fits naturally — this is Joy's core mechanic.
- **VIP tiers → reward the collectors who spend the most.** A small segment of repeat collector customers likely drives disproportionate revenue (common in this category) — tiering unlocks early access to new drops, exclusive discounts, or free shipping thresholds for top spenders.
- **Referral program → collector communities refer each other.** Anime/collectible buyers cluster in fan communities (Discord, local meetups) — referral rewards tend to perform well here since word-of-mouth is already the norm in this niche.
- **Bridging arcade visits + retail spend — Joy's real gap to flag honestly.** Joy is built for Shopify online/POS transactions; it has no native way to award points for arcade machine play (not a Shopify transaction) unless arcade credit purchases or a location's POS run through Shopify POS. If they want points tied to game-play itself, that needs to be scoped explicitly — don't imply Joy can do this out of the box until confirmed via Shopify POS integration feasibility.
- **Migration timing.** None of the above is usable until they're actually on Shopify — so the near-term value of this call is aligning on their migration plan/timeline (Q1) and locking Joy in as part of the post-migration stack, not a live demo today.

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
