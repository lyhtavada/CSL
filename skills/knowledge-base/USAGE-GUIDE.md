# Hướng Dẫn Sử Dụng — KnowledgeBase Skill

Hướng dẫn chi tiết cách sử dụng skill KnowledgeBase để quản lý ghi chú trong Obsidian vault.

---

## Mục Lục

1. [Cài Đặt](#1-cài-đặt)
2. [Workflow: Save — Lưu Ghi Chú](#2-workflow-save--lưu-ghi-chú)
3. [Workflow: Search — Tìm Kiếm](#3-workflow-search--tìm-kiếm)
4. [Workflow: Daily Journal — Nhật Ký](#4-workflow-daily-journal--nhật-ký)
5. [Workflow: Daily Note — Ghi Chú Hàng Ngày](#5-workflow-daily-note--ghi-chú-hàng-ngày)
6. [Workflow: Watch Later — Xem Sau](#6-workflow-watch-later--xem-sau)
7. [Workflow: Lint — Kiểm Tra Sức Khỏe Vault](#7-workflow-lint--kiểm-tra-sức-khỏe-vault)
8. [Workflow: Synthesize — Tổng Hợp Khái Niệm](#8-workflow-synthesize--tổng-hợp-khái-niệm)
9. [Cấu Trúc Thư Mục](#9-cấu-trúc-thư-mục)
10. [Mẹo Sử Dụng](#10-mẹo-sử-dụng)

> **Xem thêm:** [WORKFLOW.md](./WORKFLOW.md) để hiểu toàn bộ pipeline từ input → aggregation → audit → synthesis → retrieval.

---

## 1. Cài Đặt

### Bước 1: Cấu hình vault path

Mở file `CONFIG.example.md` và thay thế `{{YOUR_VAULT_PATH}}` bằng đường dẫn thực tế đến Obsidian vault của bạn:

```yaml
VAULT_PATH: "/duong/dan/den/vault/cua/ban"
```

### Bước 2: Tạo cấu trúc thư mục

Tạo các thư mục sau trong vault (nếu chưa có):

```
Vault/
├── 1. Inbox/
├── 2. Notes/
│   ├── Reference/
│   ├── Learning/
│   ├── Ideas/
│   └── Conversations/
├── 3. Projects/
├── 4. Journal/
├── 5. Resources/
│   ├── Clippings/
│   └── Templates/
└── 7. Daily Notes/
```

### Bước 3: Đặt skill files

Copy thư mục `KnowledgeBase/` vào thư mục skills của Claude Code.

### Bước 4: Kiểm tra

Nói với Claude: **"save a test note about setup complete"** — nếu file được tạo trong vault, bạn đã cài đặt thành công.

---

## 2. Workflow: Save — Lưu Ghi Chú

### Cách dùng

Nói bất kỳ câu nào có ý "lưu" hoặc "ghi chú":

| Câu lệnh | Loại ghi chú | Thư mục |
|-----------|-------------|---------|
| "Save this note about..." | Reference | `2. Notes/Reference/` |
| "Save this learning..." | Learning | `2. Notes/Learning/` |
| "Save this idea..." | Idea | `2. Notes/Ideas/` |
| "Clip this article..." | Resource | `5. Resources/Clippings/` |
| "Save this..." (không rõ loại) | Inbox | `1. Inbox/` |

### Ví dụ

```
"Save this learning — Khi dùng Docker multi-stage build,
luôn copy package.json trước rồi mới run npm install
để tận dụng cache layer."
```

**Kết quả:**
- File: `{{VAULT_PATH}}/2. Notes/Learning/2026-03-12-docker-multi-stage-build-cache.md`
- Tags: `docker`, `devops`, `optimization`
- Tự động tìm ghi chú liên quan trong vault và tạo wikilinks

### Định dạng file

Mỗi ghi chú được lưu với YAML frontmatter:

```markdown
---
title: "Docker Multi-stage Build Cache"
date: 2026-03-12
type: learning
tags:
  - docker
  - devops
  - optimization
source: "conversation"
connections:
  related: ["[[2026-03-01-docker-best-practices]]"]
  status: connected
---

# Docker Multi-stage Build Cache

Khi dùng Docker multi-stage build, luôn copy package.json
trước rồi mới run npm install để tận dụng cache layer.

## Connections

**Related:** [[2026-03-01-docker-best-practices]]
```

---

## 3. Workflow: Search — Tìm Kiếm

### Các chế độ tìm kiếm

| Chế độ | Câu lệnh | Ví dụ |
|--------|----------|-------|
| **Từ khóa** | "search vault for..." | "search vault for docker" |
| **Tag** | "find notes tagged..." | "find notes tagged with devops" |
| **Tên file** | "find note named..." | "find note named docker" |
| **Ngày** | "find notes from..." | "find notes from 2026-03-10" |
| **Loại** | "find all learnings" | "find all learning notes" |

### Ví dụ

```
"Tìm trong vault về rate limiting"
```

**Kết quả:**

```
### Search Results for "rate limiting"

3 notes found:

1. **API Rate Limiting Best Practices** (2026-03-05)
   Type: reference | Tags: api, security, performance
   > When implementing rate limiting, use a sliding window...
   Path: {{VAULT_PATH}}/2. Notes/Reference/2026-03-05-api-rate-limiting.md

2. ...
```

---

## 4. Workflow: Daily Journal — Nhật Ký

### Cách dùng

Nói **"journal entry"** theo sau bởi nội dung:

```
"Journal entry — Hôm nay deploy xong feature authentication mới.
Team feedback tích cực. Cần follow up vấn đề performance
ở dashboard page."
```

### Đặc điểm

- **Một file mỗi ngày:** `{{VAULT_PATH}}/4. Journal/2026-03-12.md`
- **Nhiều entry trong ngày:** Mỗi entry có timestamp riêng
- **Giữ nguyên giọng viết:** AI không chỉnh sửa nội dung của bạn

### Định dạng

```markdown
---
title: "Journal — March 12, 2026"
date: 2026-03-12
type: journal
tags:
  - journal
  - daily
---

# Journal — March 12, 2026

## 14:30

Hôm nay deploy xong feature authentication mới...

## 17:45

Follow up meeting với team về performance...
```

### Weekly Review — Đánh giá tuần

Nói **"weekly review"** để tạo file đánh giá tuần từ template.

---

## 5. Workflow: Daily Note — Ghi Chú Hàng Ngày

### Cách dùng

Daily Note được **tự động cập nhật** mỗi khi bạn lưu bất kỳ ghi chú nào. Bạn cũng có thể xem trực tiếp:

```
"What did I save today?"
"Show today's daily note"
```

### Đặc điểm

- **Tự động:** Mỗi lần Save hoặc Journal, daily note được cập nhật
- **Tổng hợp:** Hiển thị tất cả ghi chú, journal, resources trong ngày
- **Backfill:** Nói "backfill daily notes" để tạo daily notes cho ghi chú cũ

### Định dạng

```markdown
# March 12, 2026

## Journal

- [[2026-03-12]] — Journal entry

## Notes

- [[2026-03-12-docker-multi-stage-build-cache]] — Docker Multi-stage Build Cache
- [[2026-03-12-api-design-patterns]] — API Design Patterns

## Resources

- [[2026-03-12-scaling-postgres-tips]] — Scaling Postgres Tips
```

---

## 6. Workflow: Watch Later — Xem Sau

### Thêm vào hàng đợi

```
"Watch later: https://example.com/video-about-ai"
"Read later: https://example.com/article-about-rust"
```

### Xem hàng đợi

```
"Show my queue"
"What's in my queue?"
```

### Xử lý item trong hàng đợi

```
"Process the first article from my queue"
```

→ Tự động fetch nội dung, lưu vào vault, và chuyển từ Queue sang Processed.

### Các loại content

| Loại | Ví dụ |
|------|-------|
| `article` | Blog post, tin tức, essay |
| `video` | YouTube, Vimeo |
| `podcast` | Audio content |
| `thread` | Twitter/X thread, Reddit |
| `paper` | Academic paper, PDF |
| `tool` | GitHub repo, app, product |

---

## 7. Workflow: Lint — Kiểm Tra Sức Khỏe Vault

### Cách dùng

Khi vault đã có nhiều ghi chú (vài trăm trở lên), dùng Lint để audit vault và phát hiện các vấn đề:

```
"Lint my vault"
"Vault health check"
"KB audit"
"Kiểm tra sức khỏe vault"
```

### 5 Kiểm tra (4 cái đầu chạy song song, cái thứ 5 ghi dữ liệu)

| # | Kiểm tra | Tác dụng |
|---|----------|----------|
| 1 | **Orphan reconnection** | Tìm orphan notes (không có link) mà giờ có thể kết nối với ghi chú mới hơn — gợi ý wikilinks |
| 2 | **Stale content** | Ghi chú cũ hơn 90 ngày gắn với Telos goals đang active — có thể đã lỗi thời |
| 3 | **Missing cross-refs** | Cluster 3+ ghi chú share 3+ tags nhưng chưa link với nhau |
| 4 | **Telos coverage** | Bảng xếp hạng goals/projects theo số lượng ghi chú — phát hiện goal thiếu nội dung |
| 5 | **Topical index rebuild** | Rebuild section `## By Topic` trong Sources Index bằng cách cluster tags |

### Đặc điểm

- **Nhanh:** Hoàn thành dưới 30 giây, tối đa 15 grep/glob calls
- **Read-only (trừ check 5):** 4 kiểm tra đầu chỉ đọc vault — chạy thoải mái
- **Chỉ báo cáo, không tự sửa:** Kiểm tra 1–4 chỉ gợi ý, không tự động edit ghi chú

### Kết quả

Báo cáo có cấu trúc `# Vault Health Report — YYYY-MM-DD` với summary tổng quát và chi tiết từng check. Ví dụ:

```markdown
## Summary
- **Total notes scanned:** 247
- **Orphans found:** 12 (5 reconnection candidates)
- **Stale notes:** 3 (older than 90 days, linked to active goals)
- **Missing cross-refs:** 2 clusters
- **Telos coverage:** G6 has only 2 notes (thin)
```

### Mẹo

Chạy Lint mỗi tuần một lần để giữ vault "khỏe mạnh" — tránh để orphan notes tích tụ và phát hiện sớm khi một Telos goal bị thiếu nội dung.

---

## 8. Workflow: Synthesize — Tổng Hợp Khái Niệm

### Cách dùng

Synthesize tạo ra concept page — một trang tổng hợp kiến thức về một chủ đề từ nhiều ghi chú có liên quan.

```
"Synthesize notes on agentic architecture"
"What do I know about product strategy?"
"Concept page for typescript patterns"
"Tổng hợp ghi chú về rate limiting"
```

### Quy trình

1. **Freshness check:** Nếu concept page về chủ đề này đã tồn tại và không có source notes mới, skill sẽ hỏi trước khi regenerate
2. **Tìm kiếm song song:** Grep tags + Glob filenames + Grep nội dung → merge kết quả, loại duplicate
3. **Yêu cầu tối thiểu:** Cần ít nhất 3 ghi chú source (tối đa 15 ghi chú mới nhất)
4. **Đọc đầy đủ:** Skill đọc **toàn bộ** nội dung từng source note — không tóm tắt hời hợt
5. **Viết concept page:** Lưu vào `{{VAULT_PATH}}/2. Notes/Synthesis/YYYY-MM-DD-{topic}-synthesis.md`

### Định dạng concept page

```markdown
---
title: "{Topic} — Synthesis"
date: 2026-04-06
type: synthesis
tags:
  - synthesis
  - {topic-tags}
sources: 8
---

# {Topic}

{Tổng quan 2-3 câu: chủ đề này là gì, tại sao quan trọng}

## Key Patterns
{Patterns lặp lại qua nhiều ghi chú — không phải danh sách tóm tắt, mà là phân tích}

## Core Ideas
{Ý tưởng quan trọng nhất, tổ chức logic, trích dẫn bằng [[wikilinks]]}

## Contradictions & Tensions
{Các claims mâu thuẫn giữa ghi chú, hoặc "No contradictions detected"}

## Open Questions
{Câu hỏi các ghi chú đặt ra nhưng chưa trả lời — gaps để Save thêm sau}

## Sources
- [[2026-03-06-note-1]] — {mô tả 1 dòng}
- [[2026-02-18-note-2]] — {mô tả 1 dòng}
```

### Mẹo

- **Synthesize là "payoff" của cả hệ thống:** Save → aggregate → lint → **synthesize**. Dành thời gian mỗi tuần để synthesize 1–2 chủ đề đã "chín" (có đủ source notes)
- **Đọc Open Questions:** Đây là gợi ý rất tốt để biết lần tới cần Save thêm nội dung gì
- **Không bị duplicate:** Freshness check tự động phát hiện concept page đã có

---

## 9. Cấu Trúc Thư Mục

```
{{VAULT_PATH}}/
├── 1. Inbox/              ← Quick captures, watch-later queue
│   └── watch-later.md     ← File quản lý hàng đợi
├── 2. Notes/
│   ├── Reference/         ← Ghi chú tham khảo
│   ├── Learning/          ← Bài học, TIL
│   ├── Ideas/             ← Ý tưởng, brainstorm
│   ├── Conversations/     ← Tóm tắt cuộc họp
│   └── Synthesis/         ← Concept pages (auto từ Synthesize)
├── 3. Projects/           ← Ghi chú theo dự án
├── 4. Journal/            ← Nhật ký hàng ngày
├── 5. Resources/
│   ├── Clippings/         ← Bài viết đã clip
│   └── Templates/         ← Templates (weekly review, etc.)
└── 7. Daily Notes/        ← Tổng hợp hàng ngày (tự động)
```

---

## 10. Mẹo Sử Dụng

### Ghi chú nhanh
Nếu không chắc loại ghi chú, cứ nói **"save this"** — nó sẽ được lưu vào Inbox. Bạn có thể sắp xếp lại sau trong Obsidian.

### Tận dụng tags
Skill tự động tạo 2-5 tags cho mỗi ghi chú. Dùng Search workflow để tìm theo tag khi cần.

### Vault connections
Mỗi ghi chú mới sẽ tự động tìm và link đến ghi chú liên quan đã có trong vault bằng `[[wikilinks]]`. Điều này giúp xây dựng knowledge graph tự nhiên.

### Kết hợp với Obsidian Graph View
Sau khi tích lũy đủ ghi chú, mở Graph View trong Obsidian để thấy mối liên hệ giữa các ghi chú — rất hữu ích cho việc khám phá ý tưởng mới.

### URL luôn được lưu
Nếu trong cuộc hội thoại có đề cập URL nào, skill sẽ tự động lưu vào phần References của ghi chú. Không bao giờ mất link.

### Watch Later workflow
Đừng đọc tất cả ngay — queue lại và xử lý vào cuối tuần. Skill sẽ tự động link bài đã xử lý với ghi chú đã lưu.
