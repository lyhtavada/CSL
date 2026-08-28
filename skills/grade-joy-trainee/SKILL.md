---
name: grade-joy-trainee
description: >
  Grade a Joy Loyalty CS trainee's test/learning-log pages on Notion —
  fetch every answered question, verify against product source-of-truth,
  flag wrong/contradictory/half-done answers, report a verdict per
  question in chat, then (only after Liz approves) append the review
  as inline callout blocks on the Notion page itself. Use when Liz shares
  one or more Notion URLs for a trainee's weekly test/learning card and
  asks to grade it.
---

# /grade-joy-trainee — chấm test Joy trainee trên Notion

Chấm bài trainee (vd Alice) làm trên Notion — test kiến thức Joy Loyalty
theo tuần/module. Input là 1 hoặc nhiều Notion URL Liz gửi trực tiếp; skill
không tự đi tìm bài.

## Input

- **Notion URL(s)** — Liz dán trực tiếp. Có thể là:
  - 1 page câu hỏi tự luận (numbered question + đoạn văn trả lời) — vd
    "Week 2 Overview", "Week 2 ICP"
  - 1 page ôm 1 `child_database` (mỗi row = 1 ngày/topic, mỗi row có bảng
    Q&A riêng) — vd "Week 2: Joy Loyalty App Learning"
- **Tên trainee** (để title report/callout cho rõ ai chấm ai)

Không tự suy luận trainee là ai hay chấm mục nào nếu Liz không nói rõ —
hỏi lại nếu chỉ đưa 1 URL mà không rõ đây là bài của ai / tuần nào.

## Flow

### 1. Fetch (mechanical)

```
python3 skills/grade-joy-trainee/scripts/notion_fetch.py <url1> [<url2> ...]
```

Tự động:
- Parse page id từ URL (đúng cả URL có `?v=<view-id>` phía sau — không lấy
  nhầm view id)
- Đệ quy dump toàn bộ block, **kèm block ID inline** trên mỗi dòng (để bước
  4 lấy đúng anchor)
- Nếu page có `child_database` ở top level, tự expand mỗi row thành 1 file
  riêng (không cần Liz gửi từng URL con)
- `table_row` được đọc đúng từ `cells` (không phải `rich_text`) — bug đã
  gặp 1 lần lúc làm tay, giờ script tự xử lý

Output: các file `.txt` trong `/tmp/grade-joy-trainee/`, mỗi dòng có dạng
`<block_id> | [type] text` (bảng thì `[row] cột1 || cột2`). Đọc (Read tool)
từng file được in ra ở manifest.

### 2. Xác định phần nào cần chấm (judgment)

Trong mỗi file, phân biệt:
- **Bảng/câu hỏi cần chấm** — thường có heading "Câu hỏi (điền câu trả lời
  vào bảng...)" ngay phía trên
- **Bảng/checklist thực hành** — có cột kiểu "Hoàn thành"/"Link screenshot"
  — đây là log công việc đã làm, KHÔNG phải câu hỏi kiến thức, **không
  chấm như Q&A** (nhưng vẫn có thể đọc để hiểu context nếu cần)

Chỉ chấm ô/đoạn đã có nội dung. Ô trống → verdict `unanswered`, không suy
diễn, không tự trừ điểm ngầm — chỉ note "Chưa trả lời".

### 3. Verify nội dung (judgment — đây là phần quan trọng nhất)

Thứ tự nguồn đối chiếu, ưu tiên từ trên xuống:

1. **Tài liệu đính kèm/được trỏ tới ngay trong task đó** — dòng "Đọc: ..."
   ở đầu mỗi page thường link tới 1 Notion Module cụ thể (vd "Module 1",
   "Untitled... phần VIP tiers"), hoặc file/page đính kèm khác. Đây là tài
   liệu task **yêu cầu đọc trực tiếp** nên ưu tiên cao nhất khi có — mở
   link đó ra đọc (qua Notion API, `notion_api_access.md`) trước khi chấm
   câu liên quan, đừng chỉ dựa suy luận chung chung.
2. **KB live `cs2.avada.net`** — qua `skills/kb-sync/scripts/kb_api.py`
   hoặc `fetch_kb.py joy <path>`, agent id `joy-loyalty-agent`. Cùng nguồn
   bot Joyce dùng — ưu tiên khi câu hỏi thuộc dạng support/troubleshoot.
3. **help.joy.so** — help center chính thức, mạnh về setup/troubleshoot
   chi tiết.
4. **joy.so** (trang marketing) — dùng cho câu hỏi kiểu "merchant nhìn
   thấy gì trên web": pricing/plan hiển thị public, value proposition,
   so sánh đối thủ, feature description ở mức merchant-facing.
5. **GitLab `starlink-team/joy`** (`docs/features/`, xem
   `gitlab_avada_repos.md`) — source code, dùng khi cần verify chi tiết kỹ
   thuật mà KB/help center chưa cập nhật.

Khi chấm, chủ động tìm 2 loại lỗi giá trị cao:
- **Mâu thuẫn giữa các câu trả lời trong cùng bài** — vd trainee trả lời
  đúng ở câu này nhưng câu ngay sau lại áp dụng sai chính khái niệm đó.
  Loại lỗi này dễ lọt khi đọc lướt từng câu riêng lẻ, nhưng nguy hiểm nhất
  vì cho thấy chưa nắm chắc, không phải chỉ gõ nhầm.
- **Tự nhận chưa hiểu nhưng câu trả lời vẫn "đúng"** — trainee đôi khi tự
  note kiểu "phần này em chưa hiểu lắm" ngay trên/dưới 1 câu trả lời đã
  chép đúng nguyên văn tài liệu. Verdict nội dung vẫn `ok`, nhưng thêm ghi
  chú riêng để Liz hỏi lại trực tiếp, đừng coi là đã nắm chắc chỉ vì câu
  chữ đúng.

Tách rõ 2 mức độ, đừng gộp chung:
- **Lỗi nội dung** (`warn`/sai kiến thức, cần verify số liệu) — mức độ
  nghiêm trọng, ảnh hưởng tư vấn merchant thật.
- **Lỗi trình bày** (gõ nhầm, sót copy-paste, trả lời cụt/thiếu ý) — mức
  độ nhẹ, chỉ cần nhắc dọn lại.

### 4. Report trong chat TRƯỚC (bắt buộc, không skip)

Trình bày theo từng page/topic, dạng bảng: câu hỏi | verdict (✅/⚠️/❌) +
lý do ngắn gọn. Cuối cùng có phần tổng kết: mục nào mạnh, mục nào còn
thiếu nhiều nhất — để Liz nhìn được bức tranh tổng, không chỉ điểm từng
câu.

**Dừng ở đây và chờ Liz xác nhận** trước khi đụng vào Notion — giống flow
`kb-sync` (Liz duyệt trước khi ghi ngược). Không tự động append callout
ngay sau khi chấm xong.

### 5. Append review vào Notion (chỉ sau khi Liz confirm)

Dựng file JSON review từ chính các block ID đã thấy ở bước 1 (không đoán
ID, phải lấy đúng từ file dump), theo format:

```json
[
  {
    "page_id": "<page chứa block anchor>",
    "anchor_id": "<block id để chèn callout NGAY SAU>",
    "text": "nội dung nhận xét",
    "verdict": "ok" | "warn" | "unanswered" | "note"
  }
]
```

`verdict` tự map icon + màu nền (không cần tự chọn emoji/màu):
- `ok` → ✅ nền xanh dương — đúng
- `warn` → ⚠️ nền vàng — có lỗi/cần sửa/cần verify
- `unanswered` → ❌ nền đỏ — chưa trả lời (dùng khi CẢ bảng trống)
- `note` → 📝 nền xám — ghi chú chung, không phải chấm điểm 1 câu cụ thể

**Quy tắc chọn anchor** (giới hạn kỹ thuật của Notion — table chỉ chứa
được `table_row`, không chèn block khác vào giữa bảng được):
- Mục dạng **bảng Q&A** (đa số các page Learning theo ngày): anchor = chính
  block `table`. Gộp nhận xét cho **tất cả câu trong bảng đó** vào 1
  callout duy nhất ngay sau bảng — không chèn xen kẽ được từng dòng.
- Mục dạng **câu hỏi + đoạn văn tự do** (Overview, ICP): anchor = block
  cuối cùng của đoạn trả lời đó (thường là 1 paragraph rỗng ngay trước
  `numbered_list_item` kế tiếp, hoặc block nội dung cuối nếu không có
  đoạn rỗng) — chèn được sát ngay sau từng câu.

Chạy:
```
python3 skills/grade-joy-trainee/scripts/notion_append_review.py review.json
```

In OK/FAIL từng item. Không sửa/xoá nội dung gốc của trainee — chỉ thêm
callout mới.

## Lưu ý

- Chỉ áp dụng cho Joy hiện tại (theo yêu cầu Liz). Có thể adapt sang Chatty
  sau nếu cần — đổi agent id `kb_api.py` và bỏ nguồn `joy.so`/`help.joy.so`
  sang `chatty.net`/help center Chatty.
- Không tự ý xoá callout cũ nếu chấm lại lần 2 — hỏi Liz muốn giữ lịch sử
  review cũ hay archive trước khi thêm review mới.
