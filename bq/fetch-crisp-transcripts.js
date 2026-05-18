require('dotenv').config({ path: '/Users/avada/CSL/.env' });
const https = require('https');
const fs = require('fs');
const path = require('path');

const KEY = process.env.CRISP_API_KEY;
const SECRET = process.env.CRISP_API_SECRET;
const WEBSITE_ID = process.env.CRISP_WEBSITE_RETENTION;
const AUTH = 'Basic ' + Buffer.from(KEY + ':' + SECRET).toString('base64');

const DAYS = parseInt(process.argv[2] || '7');
const APP = process.argv[3] || 'chatty'; // chatty | joy | all
const SINCE_MS = Date.now() - DAYS * 24 * 60 * 60 * 1000;

const CHATTY_SEGS = new Set(['app_chatty', 'app_faqs']);
const JOY_SEGS   = new Set(['app_joy']);

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function get(path_) {
  return new Promise((resolve, reject) => {
    https.get({
      hostname: 'api.crisp.chat', path: path_,
      headers: { Authorization: AUTH, 'X-Crisp-Tier': 'plugin' }
    }, res => {
      let d = ''; res.on('data', c => d += c);
      res.on('end', () => { try { resolve(JSON.parse(d)); } catch(e) { reject(e); } });
    }).on('error', reject);
  });
}

function matchesApp(segments = []) {
  if (APP === 'all') return true;
  if (APP === 'chatty') return segments.some(s => CHATTY_SEGS.has(s));
  if (APP === 'joy')    return segments.some(s => JOY_SEGS.has(s));
  return false;
}

async function fetchMessages(sessionId) {
  const r = await get(`/v1/website/${WEBSITE_ID}/conversation/${sessionId}/messages`);
  return (r.data || []).map(m => ({
    from: m.from,        // user | operator
    type: m.type,
    content: m.content,
    ts: m.stamped ? new Date(m.stamped).toISOString() : null,
    operator: m.user?.nickname || null,
  })).filter(m => m.type === 'text' && m.content);
}

async function run() {
  console.log(`\n🔍 Fetching Crisp transcripts | app=${APP} | last ${DAYS} days\n`);
  const outFile = path.join(__dirname, `crisp-transcripts-${APP}-${DAYS}d.jsonl`);
  const stream = fs.createWriteStream(outFile);

  let page = 1, total = 0, fetched = 0, done = false;

  while (!done) {
    const r = await get(`/v1/website/${WEBSITE_ID}/conversations/${page}`);
    const convos = r.data || [];
    if (!convos.length) break;

    for (const c of convos) {
      // Stop if conversation is older than our window
      if (c.updated_at < SINCE_MS) { done = true; break; }

      const segs = c.meta?.segments || [];
      if (!matchesApp(segs)) continue;

      total++;
      process.stdout.write(`\r  [${page}p] matched: ${total}, fetched: ${fetched}`);

      await sleep(150); // rate limit buffer
      const messages = await fetchMessages(c.session_id);
      if (!messages.length) continue;

      stream.write(JSON.stringify({
        session_id: c.session_id,
        created_at: new Date(c.created_at).toISOString(),
        updated_at: new Date(c.updated_at).toISOString(),
        segments: segs,
        shopDomain: c.meta?.email || null,
        shopName: c.meta?.nickname || null,
        state: c.state,
        messages,
      }) + '\n');

      fetched++;
    }

    page++;
    await sleep(200);
  }

  stream.end();
  console.log(`\n\n✅ Done! ${fetched} conversations saved → ${outFile}`);
}

run().catch(e => console.error('ERR', e.message));
