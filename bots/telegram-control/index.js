require('dotenv').config({ path: require('path').resolve(__dirname, '../../.env') });
const TelegramBot = require('node-telegram-bot-api');
const { spawn } = require('child_process');

// ─── Config ─────────────────────────────────────────────────────────────────
const TOKEN    = process.env.TELEGRAM_BOT_TOKEN;
const OWNER_ID = Number(process.env.TELEGRAM_OWNER_ID);
const REPO_DIR = require('path').resolve(__dirname, '../..');   // /Users/avada/CSL
const ALLOWED_TOOLS = 'Read,Bash,Edit,Write,Grep,Glob';
const TIMEOUT_MS = 10 * 60 * 1000;   // 10 phút / lệnh

if (!TOKEN || !OWNER_ID) {
  console.error('❌ Thiếu TELEGRAM_BOT_TOKEN hoặc TELEGRAM_OWNER_ID trong .env');
  process.exit(1);
}

const bot = new TelegramBot(TOKEN, { polling: true });

// Mỗi chat 1 session Claude để giữ ngữ cảnh (--resume)
let sessionId = null;
let busy = false;

// ─── Helper: gửi tin dài (Telegram giới hạn 4096 ký tự) ─────────────────────
async function sendLong(chatId, text) {
  const MAX = 4000;
  if (!text) text = '(không có output)';
  for (let i = 0; i < text.length; i += MAX) {
    await bot.sendMessage(chatId, text.slice(i, i + MAX));
  }
}

// ─── Chạy claude headless ────────────────────────────────────────────────────
function runClaude(prompt) {
  return new Promise((resolve) => {
    const args = ['-p', prompt, '--output-format', 'json', '--allowedTools', ALLOWED_TOOLS];
    if (sessionId) args.push('--resume', sessionId);

    const child = spawn('claude', args, { cwd: REPO_DIR });
    let stdout = '', stderr = '';

    const timer = setTimeout(() => {
      child.kill('SIGTERM');
      resolve({ ok: false, text: '⏱️ Quá thời gian (10 phút), đã hủy.' });
    }, TIMEOUT_MS);

    child.stdout.on('data', d => stdout += d);
    child.stderr.on('data', d => stderr += d);

    child.on('close', (code) => {
      clearTimeout(timer);
      try {
        const res = JSON.parse(stdout);
        if (res.session_id) sessionId = res.session_id;   // giữ phiên cho lần sau
        resolve({ ok: true, text: res.result || '(trống)' });
      } catch (e) {
        resolve({ ok: false, text: `❌ Lỗi (exit ${code}):\n${stderr || stdout || e.message}`.slice(0, 3500) });
      }
    });
  });
}

// ─── Guard: chỉ owner ────────────────────────────────────────────────────────
function isOwner(msg) {
  if (msg.from?.id === OWNER_ID) return true;
  bot.sendMessage(msg.chat.id, '⛔ Bot này riêng tư.');
  console.warn(`[${new Date().toISOString()}] Từ chối user lạ: ${msg.from?.id} (@${msg.from?.username})`);
  return false;
}

// ─── Commands ────────────────────────────────────────────────────────────────
bot.onText(/^\/start$/, (msg) => {
  if (!isOwner(msg)) return;
  bot.sendMessage(msg.chat.id,
    '👋 Betty đây. Nhắn gì mình chạy Claude Code trên máy Liz luôn.\n\n' +
    '/new — bắt đầu phiên mới (quên ngữ cảnh cũ)\n' +
    '/status — xem trạng thái');
});

bot.onText(/^\/new$/, (msg) => {
  if (!isOwner(msg)) return;
  sessionId = null;
  bot.sendMessage(msg.chat.id, '🆕 Đã bắt đầu phiên mới.');
});

bot.onText(/^\/status$/, (msg) => {
  if (!isOwner(msg)) return;
  bot.sendMessage(msg.chat.id, `📊 ${busy ? 'Đang chạy lệnh...' : 'Rảnh'}\nSession: ${sessionId ? sessionId.slice(0,8) : 'chưa có'}\nThư mục: ${REPO_DIR}`);
});

// ─── Tin nhắn thường = prompt cho Claude ─────────────────────────────────────
bot.on('message', async (msg) => {
  if (msg.text?.startsWith('/')) return;   // command đã xử lý ở trên
  if (!isOwner(msg)) return;
  if (!msg.text) return;

  if (busy) {
    bot.sendMessage(msg.chat.id, '⏳ Đang chạy lệnh trước, đợi xong nhé (hoặc /status).');
    return;
  }

  busy = true;
  bot.sendChatAction(msg.chat.id, 'typing');
  const ping = setInterval(() => bot.sendChatAction(msg.chat.id, 'typing'), 5000);

  const { text } = await runClaude(msg.text);
  clearInterval(ping);
  busy = false;

  await sendLong(msg.chat.id, text);
});

bot.on('polling_error', (e) => console.error(`[polling_error] ${e.message}`));

console.log(`✅ Telegram control bot chạy. Owner=${OWNER_ID}, repo=${REPO_DIR}`);
