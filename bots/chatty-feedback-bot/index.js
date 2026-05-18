require('dotenv').config();
const { WebClient } = require('@slack/web-api');

const client = new WebClient(process.env.SLACK_BOT_TOKEN);

// ─── Config (đọc từ config.json mỗi lần poll — không cần restart khi sửa) ───

function loadConfig() {
  delete require.cache[require.resolve('./config.json')];
  return require('./config.json');
}

const FEEDBACK_CHANNEL  = process.env.FEEDBACK_CHANNEL_ID  || 'C08TSD3EET0';
const WORKSHIFT_CHANNEL = process.env.WORKSHIFT_CHANNEL_ID || 'C034NAWKMFA';

// Ca trực (VN time UTC+7)
const SHIFTS = [
  { ca: 1, sh:  0, sm: 0, eh:  4, em: 10 },
  { ca: 2, sh:  4, sm: 0, eh:  8, em: 10 },
  { ca: 3, sh:  8, sm: 0, eh: 12, em: 10 },
  { ca: 4, sh: 12, sm: 0, eh: 16, em: 10 },
  { ca: 5, sh: 16, sm: 0, eh: 20, em: 10 },
  { ca: 6, sh: 20, sm: 0, eh:  0, em: 10 },
];

// ts đã xử lý xong (đã tag + remind hoặc CS đã reply)
const processed = new Set();

// Bot user ID — lấy từ auth.test lúc start
let BOT_USER_ID = null;

// ─── Timezone helpers ─────────────────────────────────────────────────────────

const VN_OFFSET_MS = 7 * 60 * 60 * 1000;

function getVNMinutes() {
  const totalUTCMinutes = new Date().getUTCHours() * 60 + new Date().getUTCMinutes();
  return (totalUTCMinutes + 7 * 60) % (24 * 60);
}

function getActiveShifts() {
  const mins = getVNMinutes();
  return SHIFTS.filter(({ ca, sh, sm, eh, em }) => {
    const start = sh * 60 + sm;
    const end   = eh * 60 + em;
    if (ca === 6) return mins >= start || mins < end;
    return mins >= start && mins < end;
  });
}

function getShiftStartUnix(shift) {
  const now   = new Date();
  const vnNow = new Date(now.getTime() + VN_OFFSET_MS);
  const vnStart = new Date(vnNow);
  vnStart.setUTCHours(shift.sh, shift.sm, 0, 0);
  if (shift.ca === 6 && getVNMinutes() < shift.em) {
    vnStart.setUTCDate(vnStart.getUTCDate() - 1);
  }
  // Trừ 15 phút để catch check-in sớm trước đầu ca
  return Math.floor((vnStart.getTime() - VN_OFFSET_MS) / 1000) - 15 * 60;
}

// ─── Workshift reader ─────────────────────────────────────────────────────────

async function getOnDutyIds(shiftStartUnix, chattyCS) {
  const checkedIn  = new Set();
  const checkedOut = new Set();

  let cursor;
  do {
    const res = await client.conversations.history({
      channel: WORKSHIFT_CHANNEL,
      oldest:  String(shiftStartUnix),
      limit:   200,
      cursor,
    });
    for (const msg of res.messages || []) {
      const text = msg.text || '';
      const inMatch  = text.match(/^(\S+)\s+\*?check\s+in\*?\b/i);
      const outMatch = text.match(/^(\S+)\s+\*?check\s+out\*?\b/i);
      if (inMatch)  checkedIn.add(inMatch[1].toLowerCase());
      if (outMatch) checkedOut.add(outMatch[1].toLowerCase());
    }
    cursor = res.response_metadata?.next_cursor;
  } while (cursor);

  // Lowercase lookup map để match case-insensitive (Hienpt → HienPT)
  const lowerMap = {};
  for (const [k, v] of Object.entries(chattyCS)) lowerMap[k.toLowerCase()] = v;

  const normalize = u => u.replace(/\.[a-z]+$/i, '');
  return [...checkedIn]
    .filter(u => !checkedOut.has(u))
    .map(u => lowerMap[normalize(u)])
    .filter(Boolean);
}

// ─── Helper: lấy on-duty IDs cho tất cả ca đang active ──────────────────────

async function getOnDutyForActiveShifts(activeShifts, chattyCS) {
  const ids = new Set();
  for (const shift of activeShifts) {
    const shiftIds = await getOnDutyIds(getShiftStartUnix(shift), chattyCS);
    shiftIds.forEach(id => ids.add(id));
  }
  return ids;
}

// ─── Poll loop ────────────────────────────────────────────────────────────────

async function poll() {
  const config = loadConfig();

  try {
    const activeShifts = getActiveShifts();
    if (activeShifts.length === 0) return;

    // Look back 720 phút (12h) để cover cả overnight khi tắt máy
    const reminderDelay = (config.reminderDelayMinutes || 60) * 60;
    const lookbackSec = String(Math.floor(Date.now() / 1000) - 720 * 60);
    const res = await client.conversations.history({
      channel: FEEDBACK_CHANNEL,
      oldest:  lookbackSec,
      limit:   50,
    });

    for (const msg of (res.messages || [])) {
      if (msg.thread_ts && msg.thread_ts !== msg.ts) continue; // skip thread replies
      if (processed.has(msg.ts)) continue;

      // Skip "Customer Data Request" messages (GDPR/data requests — no CS action needed)
      const msgText = msg.text || '';
      const blockText = (msg.blocks || []).map(b => JSON.stringify(b)).join(' ');
      const attachText = (msg.attachments || []).map(a => JSON.stringify(a)).join(' ');
      if (/customer data request/i.test(msgText + blockText + attachText)) {
        processed.add(msg.ts);
        continue;
      }

      // Fetch thread để biết chính xác bot mình đã reply chưa
      const threadRes = await client.conversations.replies({
        channel: FEEDBACK_CHANNEL,
        ts:      msg.ts,
      });
      const replies = (threadRes.messages || []).slice(1); // bỏ parent message

      const myBotReplies = replies.filter(r => r.bot_id && r.user === BOT_USER_ID);
      const hasHumanReply = replies.some(r => !r.bot_id);

      if (hasHumanReply) {
        // CS đã reply, xong
        processed.add(msg.ts);
        continue;
      }

      if (myBotReplies.length === 0) {
        // ── Chưa tag lần nào — tag CS lần đầu ──
        let onDutyIds = await getOnDutyForActiveShifts(activeShifts, config.chattyCS);
        if (onDutyIds.size === 0 && config.fallbackUserId) {
          console.log(`[${new Date().toISOString()}] No Chatty CS on duty, falling back to Liz for ${msg.ts}`);
          onDutyIds = new Set([config.fallbackUserId]);
        }
        if (onDutyIds.size === 0) {
          console.log(`[${new Date().toISOString()}] No Chatty CS on duty, skipping ${msg.ts}`);
          continue;
        }
        const mentions = [...onDutyIds].map(id => `<@${id}>`).join(' ');
        await client.chat.postMessage({
          channel:   FEEDBACK_CHANNEL,
          thread_ts: msg.ts,
          text:      `${mentions} ${config.message}`,
        });
        console.log(`[${new Date().toISOString()}] Tagged ${onDutyIds.size} CS agent(s) for ${msg.ts}`);

      } else if (myBotReplies.length === 1) {
        // ── Bot đã tag 1 lần — check thời gian để remind ──
        const tagAge = Date.now() / 1000 - parseFloat(myBotReplies[0].ts);
        if (tagAge < reminderDelay) continue; // chưa đủ lâu

        let onDutyIds = await getOnDutyForActiveShifts(activeShifts, config.chattyCS);
        if (onDutyIds.size === 0 && config.fallbackUserId) {
          console.log(`[${new Date().toISOString()}] No Chatty CS on duty for reminder, falling back to Liz for ${msg.ts}`);
          onDutyIds = new Set([config.fallbackUserId]);
        }
        if (onDutyIds.size === 0) {
          console.log(`[${new Date().toISOString()}] No Chatty CS on duty for reminder, skipping ${msg.ts}`);
          processed.add(msg.ts);
          continue;
        }
        const mentions = [...onDutyIds].map(id => `<@${id}>`).join(' ');
        await client.chat.postMessage({
          channel:   FEEDBACK_CHANNEL,
          thread_ts: msg.ts,
          text:      `${mentions} ${config.reminderMessage}`,
        });
        processed.add(msg.ts);
        console.log(`[${new Date().toISOString()}] Reminded ${onDutyIds.size} CS agent(s) for ${msg.ts}`);

      } else {
        // Bot đã remind rồi (>= 2 bot replies), xong
        processed.add(msg.ts);
      }
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
  const pollIntervalMs = config.pollIntervalMinutes * 60 * 1000;

  console.log(`✅ Chatty Feedback Bot started (bot=${BOT_USER_ID}, polling every ${config.pollIntervalMinutes}min)`);
  poll();
  setInterval(poll, pollIntervalMs);
}

start();
