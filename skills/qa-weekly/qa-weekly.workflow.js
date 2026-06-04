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
    chats_reviewed: { type: 'integer' },
    chat_labels: {
      type: 'object',
      description: 'count of chats per label',
      properties: {
        clean: { type: 'integer' },
        minor: { type: 'integer' },
        major: { type: 'integer' },
        critical: { type: 'integer' },
      },
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
2. TRANSCRIPTS: ${cs.transcriptPath} — this week's sampled chats for CS "${cs.name}".
${cs.prevReportPath ? `3. LAST WEEK'S REPORT: ${cs.prevReportPath} — for the vs_last_week comparison.` : ''}

CRITICAL RULES:
- A single chat may contain messages from SEVERAL CS (shift handoffs). Score ONLY messages labeled "CS (${cs.name})". Do NOT blame or credit "${cs.name}" for other CS's messages.
- Every improvement MUST quote the actual chat line as evidence. If you can't quote it, don't report it.
- Skip anything not observable from chat (workshift, Trello cards, review system, ratings). Those are for monthly QA, not weekly.
- Be fair and developmental. This report is DM'd to the CS — accurate, specific, encouraging.

SCORING (per rubric §3):
- Label each chat: Clean(100) / Minor(80, only Low/Moderate) / Major(60, has High) / Critical(30, has Critical/Urgent).
- Weekly score = mean of per-chat scores, rounded.
- Map to label: 90-100 Xuất sắc, 80-89 Tốt, 70-79 Đạt, <70 Cần coaching.

POSITIVE CODES (rubric §2B): P1 empathy, P2 proactive, P3 clear-stepwise, P4 concise-on-flow, P5 reads-context.
Find 2-4 genuine strengths with chat number refs (e.g. "chat #3").

SEVERE FLAGS: if you find KN8 (rude), QT11 (ignored customer), or KT1 (wrong info), list them in severe_flags.

${cs.prevReportPath
    ? 'Compare to last week: score delta, repeated error codes, fixed error codes.'
    : 'There is no previous report — set vs_last_week to "Tuần đầu, chưa có dữ liệu so sánh."'}

CS metadata: app=${cs.app}, chats sampled=${cs.sampled} of ${cs.total} total this week.

Return the structured result. cs must be exactly "${cs.name}".`
}

phase('Grade')

const csList = (args && args.cs) || []
if (!csList.length) {
  log('No CS to grade — empty args.cs')
  return { week: args?.week, results: [] }
}

log(`Grading ${csList.length} CS for week ${args.week} (parallel, 1 subagent each)`)

const results = await parallel(
  csList.map((cs) => () =>
    agent(gradePrompt(cs, args.rubricPath), {
      label: `qa:${cs.name}`,
      phase: 'Grade',
      schema: RESULT_SCHEMA,
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
  week: args.week,
  prevWeek: args.prevWeek,
  count: graded.length,
  severe,
  results: graded,
}
