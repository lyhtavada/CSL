# Configuration — KnowledgeBase Skill

All configurable values for the Obsidian KnowledgeBase skill. Replace placeholders with your actual paths before use.

> **No hardcoded paths. No credentials.** Every path is a variable.

## Required Configuration

```yaml
# Your Obsidian vault root directory
VAULT_PATH: "{{YOUR_VAULT_PATH}}"
# Examples:
#   macOS:   /Users/yourname/Documents/MyVault
#   Windows: C:/Users/yourname/Documents/MyVault
#   Linux:   /home/yourname/Documents/MyVault
#   Cloud:   /Users/yourname/Library/CloudStorage/OneDrive-Personal/MyVault
```

## Directory Structure

These are relative to `VAULT_PATH`. Customize to match your vault layout.

```yaml
# Where quick captures and unsorted items go
INBOX_DIR: "1. Inbox"

# Notes organized by type
NOTES_REFERENCE_DIR: "2. Notes/Reference"
NOTES_LEARNING_DIR: "2. Notes/Learning"
NOTES_IDEAS_DIR: "2. Notes/Ideas"
NOTES_CONVERSATIONS_DIR: "2. Notes/Conversations"

# Project-specific notes
PROJECTS_DIR: "3. Projects"

# Journal entries
JOURNAL_DIR: "4. Journal"

# External content
RESOURCES_CLIPPINGS_DIR: "5. Resources/Clippings"

# Templates
TEMPLATES_DIR: "5. Resources/Templates"

# Auto-generated daily notes
DAILY_NOTES_DIR: "7. Daily Notes"
```

## Watch Later Queue

```yaml
# Queue file location (relative to VAULT_PATH)
QUEUE_FILE: "1. Inbox/watch-later.md"
```

## Sources Index

```yaml
# Chronological index of all consumed content (relative to VAULT_PATH)
SOURCES_INDEX: "2. Notes/Reference/sources-index.md"
```

## File Naming

```yaml
# Date format for filenames
DATE_FORMAT: "YYYY-MM-DD"

# Filename pattern: {date}-{slug}.md
# slug: lowercase, hyphens for spaces, max 60 characters
# Example: 2026-03-12-typescript-generics-cheatsheet.md
```

## Optional: Telos Integration

If your team uses the Telos goal-tracking system, map notes to goals/projects/problems:

```yaml
# Enable Telos integration (set to false to skip)
TELOS_ENABLED: false

# Paths to Telos files (relative to your PAI user directory)
# TELOS_PROBLEMS: "{{YOUR_PAI_PATH}}/USER/TELOS/PROBLEMS.md"
# TELOS_GOALS: "{{YOUR_PAI_PATH}}/USER/TELOS/GOALS.md"
# TELOS_PROJECTS: "{{YOUR_PAI_PATH}}/USER/TELOS/PROJECTS.md"
```

## Optional: Weekly Review Template

```yaml
# Path to weekly review template (relative to VAULT_PATH)
WEEKLY_REVIEW_TEMPLATE: "5. Resources/Templates/weekly-review.md"
```

## Setup Checklist

- [ ] Set `VAULT_PATH` to your Obsidian vault root
- [ ] Verify directory structure matches your vault (or create the directories)
- [ ] Copy skill files to your Claude Code skills directory
- [ ] (Optional) Enable Telos integration if your team uses it
- [ ] (Optional) Create a weekly review template
- [ ] Test with: "save a test note about configuration"
