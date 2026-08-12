"""
config.py — per-app source config for product-kb-sync.

Each app has different repo layouts (confirmed by manual GitLab survey,
2026-08-12 — see memory `gitlab_avada_repos.md`). Nothing here is uniform
across apps on purpose: don't try to generalize the paths, just look them up.

B1 = curated feature docs (prose, closest to patch-ready, but engineering-voiced
     — needs synthesis before it can go into a merchant-facing KB file).
B2 = raw label/nav files (cleanest diff signal for exact copy/nav changes, but
     zero narrative — code diff of a JSON/JS file, not a description of why).
"""

APPS = {
    "chatty": {
        "kb_app": "chatty",  # kb_api.py APP_AGENTS key
        "gitlab_project": "avada%2Favada-helpcenter-faqs",
        "branch": "master",
        "b1_paths": [
            "chatty-knowledge/entities/features",  # 18 files, engineering-voiced feature docs
        ],
        "b2_paths": [
            "packages/assets/src/i18n/messages.json",       # master i18n catalog (code-extracted, not curated)
            "packages/assets/src/i18n/catalogs",              # per-namespace catalogs
            "packages/assets/src/layouts/FullLayout/AppFullLayout.js",  # nav is INLINE here, not a config file
        ],
        "notes": "Nav has no dedicated file — diff on AppFullLayout.js will include unrelated layout code, review by hand.",
    },
    "joy": {
        "kb_app": "joy",
        "gitlab_project": "avada%2Fstarlink-team%2Fjoy",
        "branch": "master",
        "b1_paths": [
            "docs/features",    # ~55 files, per-feature/PR docs
            "docs/ai-agent",    # Joy AI agent architecture/behavior docs
        ],
        "b2_paths": [
            "packages/assets/src/locale/input",                              # admin label source, 215 files
            "packages/assets/src/pages/Translations/Parts/translationsWidgetV4.js",  # storefront widget copy
            "packages/assets/src/pages/Translations/Parts/translationsWidgetV2.js",
            "packages/assets/src/helpers/getAppNavigation.js",                # primary nav, clean
            "packages/assets/src/config/appMenu.js",                         # secondary nav/tabs, noisier (mixes logic)
        ],
        "notes": "getAppNavigation.js is clean; appMenu.js diffs need a noise-filter pass before treating as a real nav change.",
    },
    "wishlist": {
        "kb_app": "wishlist",
        "gitlab_project": "avada%2Fstarlink-team%2Fwishlist",
        "branch": "master",
        "b1_paths": [],  # no curated feature-docs folder exists — docs/features/ here is eng planning junk, not usable
        "b2_paths": [
            "packages/assets/src/locale/translations",  # 7 locale files, clean
            "packages/assets/src/const/navigation.js",  # single nav layer, clean
        ],
        "notes": "No B1 source. Agent (Wendy) is enabled:false / pre-launch as of 2026-07-22 — low priority app for this skill.",
    },
}

# Shared Slack signal source for ALL apps (confirmed by Liz 2026-08-12).
RELEASE_CHANNEL_ID = "C07RNAY9ZC6"
