---
name: share-note
description: Use when Liz wants to share a file/doc as a link, asks "share note", "gửi link file này", "upload note", or needs to hand a report/draft to someone outside this repo via URL. Uploads a file to notes.avada.net and returns a share link.
version: 1.0.0
---

# /share-note — upload a file, get a share URL

Uploads a `.md` or `.html` file to notes.avada.net (Avada's internal note-sharing
service) and returns the public share link. No login needed to view; files
persist permanently and can't be edited (re-upload makes a new URL).

## Flow

1. Confirm the file path with Liz if not given.
2. Run:
```bash
cd ~/CSL && python3 skills/share-note/scripts/upload.py path/to/file.md
```
3. Report back the printed URL.

- `.md` frontmatter (YAML between `---`) is stripped automatically before upload.
- Pass `--ext html` for HTML files (auto-detected from `.html` extension too).
- Auth via `NOTES_API_KEY` in `~/CSL/.env`.

## Update / delete an existing note

```bash
python3 skills/share-note/scripts/upload.py path/to/file.md --update <url-or-id>   # overwrite in place, same URL
python3 skills/share-note/scripts/upload.py --delete <url-or-id>                    # remove
```

There is no public API doc for these (`/api-ref`, `/docs` both 404 on notes.avada.net) — verified
2026-09-10 by probing the real endpoint directly:
- Update = `PUT /api/upload/{id}?ext=md|html`, requires `X-Notes-Git-Email`, `X-Notes-Hostname`,
  `X-Notes-Client`, `X-Notes-Client-Type` headers (`X-Notes-Client-Type` must be exactly `"cli"` —
  the server 400s on any other value). The script sets these automatically.
- Delete = `DELETE /api/upload/{id}`, only needs `Authorization`.

## Constraints

- 5MB file size limit
- 60 uploads/minute per token
- Only the token owner (by email tied to the token) can update/delete a note
