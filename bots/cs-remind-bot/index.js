require('dotenv').config();
const { WebClient } = require('@slack/web-api');

const client = new WebClient(process.env.SLACK_BOT_TOKEN);

// ─── Config (đọc từ config.json mỗi lần poll — không cần restart khi sửa) ───

function loadConfig() {
  delete require.cache[require.resolve('./config.json')];
  return require('./config.json');
}

const ANNOUNCE_CHANNEL = process.env.ANNOUNCE_CHANNEL_ID;
const LEADER_USER_ID   = process.env.LEADER_USER_ID;  // Slack ID của Liz

// Bot user ID — lấy từ auth.test lúc start
let BOT_USER_ID = null;

// ─── Reactions helper ─────────────────────────────────────────────────────────

async function getReactedUserIds(channel, messageTs) {
  try {
    const res = await client.reactions.get({ channel, timestamp: messageTs, full: true });
    const userIds = new Set();
    for (const reaction of (res.message?.reactions || [])) {
      for (const uid of (reaction.users || [])) userIds.add(uid);
    }
    return userIds;
  } catch (err) {
    console.error(`[${new Date().toISOString()}] reactions.get error for ${messageTs}:`, err.message);
    return new Set();
  }
}

// ─── Poll loop ────────────────────────────────────────────────────────────────

async function poll() {
  const config = loadConfig();
  const delayMs  = (config.delayHours  || 24) * 3600 * 1000;
  const bufferMs = (config.bufferHours ||  2) * 3600 * 1000;
  const oldestSec = String(Math.floor((Date.now() - delayMs - bufferMs) / 1000));

  try {
    const res = await client.conversations.history({
      channel: ANNOUNCE_CHANNEL,
      oldest:  oldestSec,
      limit:   50,
    });

    for (const msg of (res.messages || [])) {
      // Skip thread replies
      if (msg.thread_ts && msg.thread_ts !== msg.ts) continue;

      // Chỉ track messages của Liz (nếu LEADER_USER_ID được set)
      if (LEADER_USER_ID && msg.user !== LEADER_USER_ID) continue;

      // Chỉ xử lý messages có @channel
      if (!msg.text?.includes('<!channel>')) continue;

      // Phải đủ 24h tuổi
      const ageMs = Date.now() - parseFloat(msg.ts) * 1000;
      if (ageMs < delayMs) continue;

      // Fetch thread replies
      const threadRes = await client.conversations.replies({
        channel: ANNOUNCE_CHANNEL,
        ts:      msg.ts,
      });
      const replies = (threadRes.messages || []).slice(1);

      // Nếu bot đã reply trong thread → đã xử lý, skip
      if (replies.some(r => r.user === BOT_USER_ID)) continue;

      // CS đã reply trong thread (trừ Liz và bot)
      const repliedIds = new Set(
        replies
          .filter(r => r.user !== BOT_USER_ID && r.user !== LEADER_USER_ID)
          .map(r => r.user)
      );

      // Lấy danh sách user đã react
      const reactedIds = await getReactedUserIds(ANNOUNCE_CHANNEL, msg.ts);

      // Acknowledged = đã react HOẶC đã reply
      const acknowledgedIds = new Set([...reactedIds, ...repliedIds]);

      // Tìm CS chưa react và chưa reply
      const g2CS = config.g2CS || {};
      const unreadMentions = Object.entries(g2CS)
        .filter(([, id]) => id && id !== 'TODO' && !acknowledgedIds.has(id))
        .map(([, id]) => `<@${id}>`);

      if (unreadMentions.length === 0) {
        console.log(`[${new Date().toISOString()}] All CS acknowledged ${msg.ts}, no action`);
        continue;
      }

      // Tag CS chưa acknowledge vào thread
      await client.chat.postMessage({
        channel:   ANNOUNCE_CHANNEL,
        thread_ts: msg.ts,
        text:      `${unreadMentions.join(' ')} ${config.message}`,
      });
      console.log(`[${new Date().toISOString()}] Tagged ${unreadMentions.length} CS who haven't reacted/replied to ${msg.ts}`);
    }
  } catch (err) {
    console.error(`[${new Date().toISOString()}] Poll error:`, err.message);
  }
}

// ─── Start ────────────────────────────────────────────────────────────────────

async function start() {
  const auth = await client.auth.test();
  BOT_USER_ID = auth.user_id;

  const config = loadConfig();
  const intervalMs = (config.pollIntervalMinutes || 30) * 60 * 1000;

  console.log(`✅ CS Remind Bot started (bot=${BOT_USER_ID}, polling every ${config.pollIntervalMinutes}min)`);
  poll();
  setInterval(poll, intervalMs);
}

start();
