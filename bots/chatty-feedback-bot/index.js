require('dotenv').config();
const { WebClient } = require('@slack/web-api');

const client = new WebClient(process.env.SLACK_BOT_TOKEN);

// ─── Config (đọc từ config.json mỗi lần poll — không cần restart khi sửa) ───

function loadConfig() {
  delete require.cache[require.resolve('./config.json')];
  return require('./config.json');
}

const FEEDBACK_CHANNEL = process.env.FEEDBACK_CHANNEL_ID || 'C08TSD3EET0';

const CRISP_API_KEY    = process.env.CRISP_API_KEY;
const CRISP_API_SECRET = process.env.CRISP_API_SECRET;
const CRISP_WEBSITE_ID = process.env.CRISP_WEBSITE_RETENTION;
const CRISP_AUTH = Buffer.from(`${CRISP_API_KEY}:${CRISP_API_SECRET}`).toString('base64');

// ts đã xử lý xong (đã reply link chat Crisp hoặc CS đã reply tay)
const processed = new Set();

// Bot user ID — lấy từ auth.test lúc start
let BOT_USER_ID = null;

// ─── Crisp: tìm chat của KH theo email ─────────────────────────────────────

async function findCrispSessionByEmail(email) {
  const url = `https://api.crisp.chat/v1/website/${CRISP_WEBSITE_ID}/conversations/1?search_type=text&search_query=${encodeURIComponent(email)}&search_operator=and`;
  const res = await fetch(url, {
    headers: {
      Authorization: `Basic ${CRISP_AUTH}`,
      'X-Crisp-Tier': 'plugin',
    },
  });
  if (!res.ok) {
    throw new Error(`Crisp API ${res.status}: ${await res.text()}`);
  }
  const body = await res.json();
  const conversations = body.data || [];
  if (conversations.length === 0) return null;
  // Kết quả mới nhất trước (Crisp trả về sort theo updated_at desc)
  return conversations[0].session_id;
}

function crispChatLink(sessionId) {
  return `https://app.crisp.chat/website/${CRISP_WEBSITE_ID}/inbox/${sessionId}/`;
}

// ─── Helper: lấy Shop Email từ feedback message ────────────────────────────

function extractShopEmail(msg) {
  const blockText = (msg.blocks || []).map(b => JSON.stringify(b)).join(' ');
  const m = blockText.match(/Shop Email:\*\\n?\s*<mailto:([^|>]+)/) || (msg.text || '').match(/Shop Email:\*\s*([^\s*]+@[^\s*]+)/);
  return m ? m[1] : null;
}

// ─── Poll loop ────────────────────────────────────────────────────────────────

async function poll() {
  const config = loadConfig();

  try {
    // Look back 720 phút (12h) để cover cả overnight khi tắt máy
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

      // Fetch thread để biết bot mình đã reply chưa
      const threadRes = await client.conversations.replies({
        channel: FEEDBACK_CHANNEL,
        ts:      msg.ts,
      });
      const replies = (threadRes.messages || []).slice(1); // bỏ parent message
      const alreadyReplied = replies.some(r => r.bot_id && r.user === BOT_USER_ID);
      if (alreadyReplied) {
        processed.add(msg.ts);
        continue;
      }

      const email = extractShopEmail(msg);
      let replyText;

      if (!email) {
        replyText = `⚠️ Không tìm thấy Shop Email trong feedback này.`;
      } else {
        try {
          const sessionId = await findCrispSessionByEmail(email);
          if (sessionId) {
            replyText = `🔗 Chat Crisp của KH (${email}): ${crispChatLink(sessionId)}`;
          } else {
            replyText = `⚠️ Không tìm thấy chat Crisp nào của KH (${email}) — cần tạo chat mới để fu.`;
          }
        } catch (err) {
          console.error(`[${new Date().toISOString()}] Crisp lookup error for ${msg.ts}:`, err.message);
          replyText = `⚠️ Lỗi tra chat Crisp cho KH (${email}) — ${err.message}.`;
        }
      }

      await client.chat.postMessage({
        channel:   FEEDBACK_CHANNEL,
        thread_ts: msg.ts,
        text:      replyText,
      });
      processed.add(msg.ts);
      console.log(`[${new Date().toISOString()}] Replied Crisp link for ${msg.ts} (email=${email || 'none'})`);
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
