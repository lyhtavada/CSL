/**
 * Agent Daily Report — Chatty, Joy, Wishlist
 * Queries BigQuery openclaw_livechat_analytics.events for yesterday's data
 * and posts a digest to Slack.
 *
 * Run: node agent-daily-report.js
 * Cron: 0 8 * * * (every day 8am Vietnam time)
 */

const { BigQuery } = require("@google-cloud/bigquery");
const path = require("path");
const fs = require("fs");

// ── Config ──────────────────────────────────────────────────────────────────

const BQ_PROJECT = "avada-crm";
const BQ_DATASET = "openclaw_livechat_analytics";
const BQ_TABLE   = "events";

const SA_KEY_PATH   = path.join(__dirname, "sa.json");
const SLACK_TOKEN   = process.env.SLACK_BOT_TOKEN   || "";
// Post to G2 Retention channel (Chatty + Joy + Wishlist are all G2)
const SLACK_CHANNEL = process.env.SLACK_REPORT_CHANNEL || "C0AHN7DH3PD";

const AGENTS = [
  { id: "chatty-agent",       label: "Chatty",   emoji: "⚡" },
  { id: "joy-loyalty-agent",  label: "Joy",      emoji: "⭐" },
  { id: "wishlist-agent",     label: "Wishlist", emoji: "❤️" },
];

// ── BigQuery ─────────────────────────────────────────────────────────────────

const credentials = JSON.parse(fs.readFileSync(SA_KEY_PATH, "utf-8"));
const bq = new BigQuery({ projectId: BQ_PROJECT, credentials });

async function queryYesterday() {
  const agentList = AGENTS.map(a => `'${a.id}'`).join(", ");

  const sql = `
    WITH base AS (
      SELECT
        agent_id,
        session_id,
        type,
        duration_ms,
        tier,
        escalation_reason,
        ts
      FROM \`${BQ_PROJECT}.${BQ_DATASET}.${BQ_TABLE}\`
      WHERE DATE(ts) = DATE_SUB(CURRENT_DATE('Asia/Ho_Chi_Minh'), INTERVAL 1 DAY)
        AND agent_id IN (${agentList})
    ),

    -- one row per session per agent
    sessions AS (
      SELECT
        agent_id,
        session_id,
        COUNTIF(type = 'reply') AS reply_count,
        MAX(CASE WHEN type = 'escalation' THEN 1 ELSE 0 END) AS escalated,
        ANY_VALUE(tier) AS tier,
        MAX(duration_ms) AS max_duration_ms
      FROM base
      GROUP BY agent_id, session_id
    ),

    -- escalation reasons (top 3 per agent)
    esc_reasons AS (
      SELECT agent_id, escalation_reason, COUNT(*) AS cnt
      FROM base
      WHERE type = 'escalation' AND escalation_reason IS NOT NULL
      GROUP BY agent_id, escalation_reason
    ),

    agg AS (
      SELECT
        agent_id,
        COUNT(DISTINCT session_id)                          AS total_conv,
        COUNTIF(escalated = 0)                              AS resolved,
        COUNTIF(escalated = 1)                              AS escalated,
        COUNTIF(tier = 'fast')                              AS tier_fast,
        COUNTIF(tier = 'full')                              AS tier_full,
        ROUND(AVG(max_duration_ms) / 1000, 1)               AS avg_resp_s
      FROM sessions
      GROUP BY agent_id
    )

    SELECT
      a.agent_id,
      a.total_conv,
      a.resolved,
      a.escalated,
      a.tier_fast,
      a.tier_full,
      a.avg_resp_s,
      ARRAY_AGG(
        STRUCT(r.escalation_reason AS reason, r.cnt)
        ORDER BY r.cnt DESC LIMIT 3
      ) AS top_esc_reasons
    FROM agg a
    LEFT JOIN esc_reasons r USING (agent_id)
    GROUP BY 1,2,3,4,5,6,7
    ORDER BY a.total_conv DESC
  `;

  const [rows] = await bq.query({ query: sql, location: "US" });
  return rows;
}

// ── Format Slack message ──────────────────────────────────────────────────────

function buildSlackMessage(rows) {
  // Build lookup map
  const byAgent = {};
  for (const row of rows) byAgent[row.agent_id] = row;

  const yesterday = new Date();
  yesterday.setDate(yesterday.getDate() - 1);
  const dateStr = yesterday.toISOString().slice(0, 10);

  const lines = [
    `📊 *Agent Daily Report — ${dateStr}*`,
    "",
  ];

  for (const { id, label, emoji } of AGENTS) {
    const d = byAgent[id];
    if (!d || d.total_conv === 0) {
      lines.push(`${emoji} *${label}* — no conversations yesterday`);
      lines.push("");
      continue;
    }

    const resolvedPct = d.total_conv > 0
      ? Math.round((d.resolved / d.total_conv) * 100)
      : 0;
    const resolvedIcon = resolvedPct >= 80 ? "✅" : resolvedPct >= 60 ? "⚠️" : "❌";
    const totalFast = (d.tier_fast || 0) + (d.tier_full || 0);
    const fastPct = totalFast > 0 ? Math.round((d.tier_fast / totalFast) * 100) : 0;

    lines.push(`${emoji} *${label}*`);
    lines.push(`  • Conversations: *${d.total_conv}*`);
    lines.push(`  • ${resolvedIcon} Resolved: *${resolvedPct}%* (${d.resolved}/${d.total_conv})`);
    lines.push(`  • 🚨 Escalated: *${d.escalated}*`);
    lines.push(`  • ⚡ Avg response: *${d.avg_resp_s}s*`);
    lines.push(`  • 🤖 Tier split: ${fastPct}% FAQ (Haiku) / ${100 - fastPct}% Complex (Sonnet)`);

    if (d.top_esc_reasons?.length > 0) {
      const reasons = d.top_esc_reasons
        .filter(r => r.reason)
        .map(r => `${r.reason} (${r.cnt}x)`)
        .join(", ");
      if (reasons) lines.push(`  • 📌 Top escalation: ${reasons}`);
    }

    lines.push("");
  }

  // Overall summary
  const totals = rows.reduce(
    (acc, r) => {
      acc.conv += r.total_conv || 0;
      acc.escalated += r.escalated || 0;
      return acc;
    },
    { conv: 0, escalated: 0 }
  );

  if (totals.conv > 0) {
    lines.push(`_Total: ${totals.conv} conversations, ${totals.escalated} escalated_`);
  }

  return lines.join("\n");
}

// ── Slack post ────────────────────────────────────────────────────────────────

async function postToSlack(text) {
  if (!SLACK_TOKEN) {
    console.log("No SLACK_BOT_TOKEN — printing to stdout:\n");
    console.log(text);
    return;
  }

  const res = await fetch("https://slack.com/api/chat.postMessage", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${SLACK_TOKEN}`,
    },
    body: JSON.stringify({
      channel: SLACK_CHANNEL,
      text,
      mrkdwn: true,
    }),
  });

  const data = await res.json();
  if (!data.ok) {
    throw new Error(`Slack error: ${data.error}`);
  }
  console.log(`✅ Posted to Slack channel ${SLACK_CHANNEL}`);
}

// ── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🔍 Querying BigQuery...");
  const rows = await queryYesterday();
  console.log(`   Got ${rows.length} agent rows`);

  const message = buildSlackMessage(rows);
  console.log("\n--- Preview ---");
  console.log(message);
  console.log("---------------\n");

  await postToSlack(message);
}

main().catch(err => {
  console.error("❌ Error:", err.message);
  process.exit(1);
});
