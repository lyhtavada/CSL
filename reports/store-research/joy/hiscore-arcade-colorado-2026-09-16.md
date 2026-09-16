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

## Call script (SPIN-style)

**Opening (1-2 min)**
> "Thanks for taking the time — before we jump in, I did a bit of homework on Hi-Score Arcade. Looks like you've got a great niche going — the arcade plus the manga/figures/model-kit shop. Mind if I ask a few questions first so I can make sure whatever we talk about today is actually useful for you, not just a generic pitch?"

**Situation (confirm what we found, don't assume)**
- "You're running the online shop on Square right now, is that right?"
- "About how much of your business is the online retail side vs. in-person arcade/foot traffic?"
- Q1 (migration): *Are you currently planning to migrate from Square Online to Shopify? What's driving that, and what's the timeline?*
- Q6 (history): *Have you run any loyalty or rewards program before — on Square, punch cards in-store, anything?*

**Problem (surface pain, let them say it, don't lead too hard)**
- "With ~400 SKUs of figures, model kits, and manga — categories people tend to collect and come back for — how are you currently keeping past customers coming back for the next drop?"
- "Anything about Square's ecosystem that's pushing you to look elsewhere, especially around apps like loyalty/rewards?"
- If they mention no current program: "So right now a repeat collector buying their 10th figure gets treated the same as a first-time visitor?"

**Implication (make the cost of doing nothing concrete)**
- "If a chunk of revenue is coming from a small group of repeat collectors, what happens to LTV if there's no reason for them to choose you over another shop with the same stock?"
- "When you do migrate, if loyalty isn't part of the stack from day one, is that something you'd have to circle back and retrofit later — with all your historical purchase data not carried over?"

**Need-payoff (let them articulate the win before you pitch)**
- Q5 (goal): *What's the main outcome you're hoping a loyalty program would drive — more repeat purchases, higher order value, competing with other collectible shops, something else?*
- "If customers earned points every time they bought a figure or model kit, and hit a VIP tier for early access to new drops — would that change how often they come back?"

**Position Joy (only after they've named the need — tie back to their own words)**
- Points-per-purchase framed as "earn toward your next figure"
- VIP tiers for top collectors — early access / exclusive perks
- Referral — "your customers already talk to each other in collector communities, referral rewards tend to do well there"
- **Be upfront on the gap:** "One honest caveat — Joy runs on Shopify transactions, so out of the box it rewards purchases, not arcade play itself. If you want points tied to game credits too, we'd need to scope that against how those go through Shopify POS — I don't want to overpromise that today."

**Close / next steps**
- Q7 (plan): *Do you already have a rough plan — budget, which Shopify/Joy tier, or a timeline in mind?*
- If migration isn't confirmed/near-term: "Since Joy only works once you're on Shopify, the useful next step today is nailing down your migration timeline — I can follow up right when you're ready to set up loyalty as part of that move."
- If migration is imminent: propose a follow-up config session once their Shopify store is live, using their real catalog (Gundam/Pokémon kits, figures, manga) as the worked example.

## Key takeaway for Liz

Since the store isn't on Shopify, Joy Loyalty can't be configured live on their site. This call should function as a discovery/needs conversation + migration-plan validation, not a live-config demo on their real store.
