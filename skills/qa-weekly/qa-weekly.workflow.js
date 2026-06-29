export const meta = {
  name: 'qa-weekly',
  description: 'Grade each Team G2 CS\'s weekly chats against the QA weekly rubric, one subagent per CS in parallel',
  phases: [
    { title: 'Grade', detail: 'one grading subagent per CS' },
  ],
}

// args: {
//   week: "2026-W22",
//   prevWeek: "2026-W21",
//   rubricPath: "/Users/avada/CSL/playbooks/qa-weekly-rubric.md",
//   prevReportDir: "/Users/avada/CSL/reports/qa-weekly",
//   cs: [ { name, slack_id, app, total, sampled, transcriptPath, prevReportPath } ]
// }

const RESULT_SCHEMA = {
  type: 'object',
  required: ['cs', 'score', 'label', 'chats_reviewed', 'strengths', 'improvements'],
  properties: {
    cs: { type: 'string' },
    score: { type: 'integer', description: '0-100, mean of per-chat scores' },
    label: {
      type: 'string',
      enum: ['Xuất sắc', 'Tốt', 'Đạt', 'Cần coaching'],
    },
    chats_reviewed: {
      type: 'integer',
      description: 'chats actually scored (exclude ones with no messages from this CS)',
    },
    overall: {
      type: 'string',
      description: 'Nhận xét tổng quan 2-4 câu về CS tuần này: phong cách làm việc, điểm mạnh nổi bật nhất, và RÕ RÀNG hướng cần tập trung. Giọng THẲNG THẮN, không vòng vo — gọi tên vấn đề trực diện và nêu hệ quả để CS hiểu mình thiếu ở đâu, đừng lấp liếm bằng giọng quá nhẹ. Tiếng Việt. Gọi CS là "bạn" (trung lập) — KHÔNG gọi "em".',
    },
    axis_avg: {
      type: 'object',
      description: 'điểm trung bình từng trục trên toàn mẫu (để thấy CS yếu trục nào)',
      required: ['mindset', 'knowledge', 'skill'],
      properties: {
        mindset: { type: 'number', description: 'TB trục Mindset (0-34)' },
        knowledge: { type: 'number', description: 'TB trục Kiến thức (0-33)' },
        skill: { type: 'number', description: 'TB trục Kỹ năng xử lý (0-33)' },
      },
    },
    excluded: {
      type: 'integer',
      description: 'số chat loại khỏi mẫu (không có message của CS này)',
    },
    strengths: {
      type: 'array',
      description: '2-4 positive points (P1-P5) with chat number refs',
      items: {
        type: 'object',
        required: ['code', 'note', 'chat_refs'],
        properties: {
          code: { type: 'string', description: 'P1-P5' },
          note: { type: 'string' },
          chat_refs: { type: 'array', items: { type: 'string' } },
        },
      },
    },
    improvements: {
      type: 'array',
      description: 'improvement points, each with error code, quote, and an action tip',
      items: {
        type: 'object',
        required: ['code', 'severity', 'issue', 'evidence', 'action', 'chat_refs'],
        properties: {
          code: { type: 'string', description: 'QT/KT/KN code' },
          severity: { type: 'string', enum: ['Low', 'Moderate', 'High', 'Critical', 'Urgent'] },
          issue: { type: 'string' },
          evidence: { type: 'string', description: 'quote from the chat' },
          action: { type: 'string', description: 'concrete coaching tip' },
          chat_refs: { type: 'array', items: { type: 'string' } },
        },
      },
    },
    severe_flags: {
      type: 'array',
      description: 'KN8 / QT11 / KT1 occurrences needing Liz review before DM',
      items: { type: 'string' },
    },
    review_ask: {
      type: 'object',
      description: 'THEO DÕI xin review — KHÔNG tính vào score (rubric §4.1). Chỉ ghi nhận hành vi CS chủ động mời KH để lại review Shopify.',
      required: ['eligible', 'asked', 'note'],
      properties: {
        eligible: { type: 'integer', description: 'số chat "đáng lẽ nên xin": KH hài lòng/đã xử lý xong VÀ chat header ghi "Review: chưa có review". LOẠI chat header ghi "Review: ĐÃ CÓ review".' },
        asked: { type: 'integer', description: 'trong số eligible, bao nhiêu chat CS có chủ động xin review (phải quote được câu xin)' },
        well_timed: { type: 'integer', description: 'số lần xin đúng lúc (KH vừa hài lòng/cảm ơn)' },
        mistimed: { type: 'integer', description: 'số lần xin sai lúc (KH chưa xong/đang bực) → cần coaching nhẹ' },
        note: { type: 'string', description: '1-2 câu tiếng Việt ghi nhận: xin X/Y chat phù hợp, có bỏ lỡ chat vàng không, đúng/sai lúc. Giọng nhẹ (ghi nhận, KHÔNG phải lỗi). Không có chat eligible → "Tuần này không có chat phù hợp để xin review."' },
      },
    },
    vs_last_week: {
      type: 'string',
      description: 'comparison text vs previous week report, or "Tuần đầu, chưa có dữ liệu so sánh"',
    },
  },
}

function gradePrompt(cs, rubricPath) {
  return `You are a QA reviewer for the Avada CS team. Grade ONE CS agent's chats for the week.

Read these two files:
1. RUBRIC: ${rubricPath} — the weekly QA rubric (scoring, error codes, positive codes, DM format).
2. TRANSCRIPTS: ${cs.transcriptPath} — this week's sampled chats for CS "${cs.name}". The file is divided into blocks "CHAT #1", "CHAT #2", … up to "CHAT #N". FIRST count how many CHAT blocks the file has (grep/scan for "CHAT #") — that N is how many chats you MUST score. Read and label every one.
${cs.prevReportPath ? `3. LAST WEEK'S REPORT: ${cs.prevReportPath} — for the vs_last_week comparison.` : ''}

CRITICAL RULES:
- A single chat may contain messages from SEVERAL CS (shift handoffs). Score ONLY messages labeled "CS (${cs.name})". Do NOT blame or credit "${cs.name}" for other CS's messages.
- Every improvement MUST quote the actual chat line as evidence. If you can't quote it, don't report it.
- Skip anything not observable from chat (workshift, Trello cards, review system, ratings, TS/dev coordination, shift handoff, post-chat follow-up). Those are for monthly QA, not weekly — do NOT speculate about them or let them affect the score.
- The weekly score reflects ONLY chat quality with the customer. Never imply this is a full performance review (the DM no longer prints a long disclaimer — just don't over-claim scope in overall/vs_last_week).
- Be fair and developmental. This report is DM'd to the CS — accurate, specific, encouraging.

KNOWLEDGE CHECK (KT1/KT2) — verify against KB, but be efficient:
- Do NOT judge knowledge claims from your own memory.
- PRICING is the most common claim — it is embedded below, so for any price/plan/limit claim, check against THIS table directly. Do NOT open a KB file for pricing.

  JOY (orders/mo free quota): Starter $0 = 250 · Essential $29 = 500 · Advanced $129 = 2,000 · Ultimate $499 = 7,000. (Starter's figure is in transactions.) Free trial 14d Essential/Advanced, 30d Ultimate; Starter free forever; 30-day refund after upgrade.
  CHATTY (per month unless noted): Free $0 = 50 AI convo lifetime, 100 products, 1 member, 90d history · Basic $19.99 = 50 AI/mo, 500 products, 5 members, 12mo history · Pro $68.99 = 300 AI/mo, 8,000 products, 10 members, unlimited history · Plus $199 = 700 AI/mo, 20,000 products, unlimited members.

- For NON-pricing claims (specific feature behavior, refund/policy edge cases): only THEN consult the KB. The KB is the LIVE KB that Joyce/Ivy actually run, on cs2.avada.net — do NOT read the old claw-webhook repo. Index of available paths: /Users/avada/CSL/skills/qa-weekly/references/kb-index.md. To read a file, run: \`python3 /Users/avada/CSL/skills/qa-weekly/scripts/fetch_kb.py <chatty|joy> <kb/path.md>\` (e.g. \`... chatty kb/case/billing-refund.md\`). Read at most 1-2 files, only when a chat genuinely has a checkable non-price claim.
  - Claim CONTRADICTS the table/KB → KT1: quote the CS line + the correct value.
  - KB clearly has the answer but CS went in circles / said "can't be done" when it can → KT2.
- Most chats have NO claim worth verifying — don't force it. If two KB files disagree (e.g. team-member count), that's a KB bug → severe_flag for Liz, NOT the CS's fault.
- No claim / not sure → skip, do not speculate, do not open KB.

SCORING — THREE-AXIS model (per rubric §2-§3). Each chat is scored on 3 independent axes that sum to 0-100:
  • Trục 1 MINDSET (0-34): ownership (theo tới cùng, không đẩy việc/đóng lửng) + empathy (thấu cảm, trấn an đúng lúc) + proactive (chủ động vì lợi ích KH) + effort (nỗ lực làm KH hài lòng, kiên nhẫn với KH khó). ~34 xuất sắc, ~25 ổn, ~15 máy móc, ~5 vô cảm/đẩy việc.
  • Trục 2 KNOWLEDGE (0-33): tư vấn ĐÚNG, verified against the real agent KB (see KB rules above). ~33 mọi claim đúng KB; ~22 đúng nhưng thiếu/chưa chắc; ~10 KT2 (KB có sẵn mà lòng vòng); ~0 KT1 (sai giá/tính năng/chính sách). KB outdated → flag Liz, đừng vội trừ.
  • Trục 3 SKILL (0-33): rõ ràng, đúng flow, không lỗi giao tiếp. Trừ cho KN3/KN7 (khó hiểu/chung chung), QT9/KN2 (vòng vo/hỏi lại), KN5/KN6 (hiểu sai/kết luận sớm), QT18/22/25 (đóng lửng/bỏ sót/hẹn rồi im), KN1 (typo). ~33 mượt không lỗi; ~22 1 lỗi nhẹ; ~10 lỗi nặng; ~0 hỏng.

LANGUAGE — IMPORTANT: Crisp has built-in live translation, so a CS replying in the customer's language is NOT a skill worth praising. NEVER list "đa ngôn ngữ / handles multiple languages / replied in French/Chinese/etc" as a strength, and don't mention it in the overall note. The only language thing that matters: if the CUSTOMER writes in language A but the CS replies in a DIFFERENT language B (mismatch) — that forces the customer to read/translate themselves and is a real skill issue → note it as a KN3 improvement (and deduct on the Skill axis). Same-language reply = normal, no comment either way.

Chat score = mindset + knowledge + skill (0-100). The 3-axis model means: a CS who is technically correct but cold/robotic loses ~⅓ at Mindset; a caring + accurate CS with minor typos still scores high. This is intentional — reward serving the customer with heart AND accuracy, not just following process.

*** YOU MUST SCORE EVERY SINGLE CHAT. *** The file has N chats (CHAT #1 … CHAT #N). Go through ALL one by one — do NOT stop after a handful or only summarize "notable" ones. chats_reviewed MUST equal (N − excluded). A low number = you skipped chats = BUG.
- excluded = ONLY chats with zero "CS (${cs.name})" lines. Every chat with at least one MUST be scored.
- Weekly score = mean of per-chat (mindset+knowledge+skill), rounded.
- axis_avg = mean of each axis across scored chats (shows which axis the CS is weak on).
- Map overall label: 90-100 Xuất sắc, 80-89 Tốt, 70-79 Đạt, <70 Cần coaching.

Before returning: confirm you scored all N chats (chats_reviewed + excluded = N).

For strengths/improvements, tag each with which axis it belongs to (Mindset/Kiến thức/Kỹ năng) plus the relevant code. Find genuine strengths (not flattery) and concrete improvements with quotes + action tips.

SEVERE FLAGS: if you find KN8 (rude), QT11 (ignored customer), KT1 (wrong info), or a live-store mistake, list them in severe_flags.

REVIEW-ASK TRACKING (rubric §4.1) — fill 'review_ask'. This is OBSERVE-ONLY, it does NOT affect the score:
- Each chat header has a "Review:" field. "ĐÃ CÓ review" = KH đã để review rồi → CS không cần xin → EXCLUDE from eligible. "chưa có review" = candidate.
- eligible = chats with Review:"chưa có review" AND where the customer was satisfied / issue resolved (KH cảm ơn, khen, "thanks/perfect", vấn đề xong). NOT angry/unresolved/one-liner chats.
- asked = of those eligible, how many the CS actually invited a Shopify review in (must be quotable, e.g. "would you mind leaving us a review", "cho shop xin 5 sao"). well_timed vs mistimed as in the schema.
- note: gently record "đã xin X/Y chat phù hợp", whether golden chats were missed, timing. Light tone — this is recognition, never a deduction. No eligible chat → say so.
- Do NOT speculate: only count a chat as eligible when the transcript clearly shows satisfaction. When unsure, leave it out.

${cs.prevReportPath
    ? 'Compare to last week: score delta, repeated error codes, fixed error codes.'
    : 'There is no previous report — set vs_last_week to "Tuần đầu, chưa có dữ liệu so sánh."'}

CS metadata: app=${cs.app}, chats sampled=${cs.sampled} of ${cs.total} total this week.

Also write the 'overall' field: 2-4 câu tiếng Việt tóm tắt tuần của CS này — phong cách làm việc, điểm mạnh nổi bật nhất, và RÕ RÀNG hướng cần tập trung. Giọng THẲNG THẮN, gọi tên vấn đề trực diện + nêu hệ quả (làm khách hỏi lại / hiểu sai / kéo dài chat) để CS hiểu chính xác mình thiếu ở đâu — KHÔNG vòng vo, không hạ nhẹ mức độ. Khen có cơ sở, không xã giao. Gọi CS là "bạn" (trung lập), KHÔNG gọi "em".

Return the structured result. cs must be exactly "${cs.name}".`
}

phase('Grade')

// args may arrive as a STRING (JSON-encoded) instead of a parsed value —
// the runtime passes it verbatim. Parse it if so.
let A = args
if (typeof A === 'string') {
  try { A = JSON.parse(A) } catch (e) { A = null }
}

// A can be: {week, rubricPath, cs:[...]}  OR  a bare array of names
// OR {names:[...]}. Normalize so any shape works.
const RUBRIC = (A && A.rubricPath) ||
  '/Users/avada/CSL/playbooks/qa-weekly-rubric.md'
const WEEK = (A && A.week) || '2026-W22'

function csFromName(name) {
  return {
    name,
    app: '?',
    total: 0,
    sampled: 0,
    transcriptPath: `/tmp/qa_tx_${name}.txt`,
    prevReportPath: null,
  }
}

let csList = []
if (A && Array.isArray(A.cs) && A.cs.length) {
  csList = A.cs
} else if (Array.isArray(A) && A.length) {
  csList = A.map((x) => (typeof x === 'string' ? csFromName(x) : x))
} else if (A && Array.isArray(A.names) && A.names.length) {
  csList = A.names.map(csFromName)
}

if (!csList.length) {
  log('No CS to grade — args shape: ' + JSON.stringify(A).slice(0, 200))
  return { week: WEEK, results: [] }
}

log(`Grading ${csList.length} CS for week ${WEEK} (parallel, 1 subagent each)`)

const results = await parallel(
  csList.map((cs) => () =>
    agent(gradePrompt(cs, RUBRIC), {
      label: `qa:${cs.name}`,
      phase: 'Grade',
      schema: RESULT_SCHEMA,
      // Sonnet is plenty for rubric-based grading and uses far less quota than
      // Opus — 9 Opus graders over 30-chat transcripts hit the subscription
      // usage limit. Sonnet keeps the fan-out within budget.
      model: 'sonnet',
    })
  )
)

const graded = results.filter(Boolean)
log(`Done — ${graded.length}/${csList.length} CS graded`)

// Sort by score ascending so the ones needing coaching surface first
graded.sort((a, b) => (a.score ?? 0) - (b.score ?? 0))

const severe = graded.filter((g) => (g.severe_flags || []).length > 0)
                     .map((g) => ({ cs: g.cs, flags: g.severe_flags }))

return {
  week: WEEK,
  prevWeek: (A && A.prevWeek) || null,
  count: graded.length,
  severe,
  results: graded,
}
