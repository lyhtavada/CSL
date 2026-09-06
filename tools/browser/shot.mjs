#!/usr/bin/env node
/**
 * shot.mjs — chụp màn hình qua Chrome mà Liz ĐANG đăng nhập, rồi upload lên
 * capture.avada.io (cùng backend Flameshot của Avada) và in ra link.
 *
 * Betty không cần user/pass: nó attach vào Chrome qua CDP, dùng luôn session
 * sẵn có. Liz phải mở Chrome ở chế độ debug trước (xem README.md).
 *
 * Dùng:
 *   node shot.mjs --list                        # liệt kê tab đang mở
 *   node shot.mjs --tab 2 --out kb.png          # chụp tab số 2
 *   node shot.mjs --url https://... --out x.png # mở url mới rồi chụp
 *   node shot.mjs --tab 2 --full                # chụp full page (cuộn hết)
 *   node shot.mjs --tab 2 --clip 0,0,1200,800   # chụp 1 vùng
 *   thêm --no-upload nếu chỉ muốn file local
 */
import { chromium } from 'playwright-core';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import fs from 'node:fs';

const args = process.argv.slice(2);
const has = f => args.includes(f);
const val = (f, d) => { const i = args.indexOf(f); return i >= 0 ? args[i + 1] : d; };

const CDP = val('--cdp', 'http://127.0.0.1:9222');
const OUTDIR = val('--outdir', '/tmp/betty-shots');
fs.mkdirSync(OUTDIR, { recursive: true });

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
let browser, launched = false;
try {
  if (has('--launch')) {
    // Chrome mới, profile trống — chỉ dùng cho trang public (vd help.chatty.net).
    // Không có session đăng nhập của Liz.
    browser = await chromium.launch({ executablePath: CHROME, headless: !has('--headed') });
    launched = true;
  } else {
    browser = await chromium.connectOverCDP(CDP);
  }
} catch (e) {
  console.error(`Không connect được Chrome tại ${CDP}.
Liz mở Chrome ở chế độ debug trước:
  1) Thoát hẳn Chrome (Cmd+Q)
  2) Chạy: open -a "Google Chrome" --args --remote-debugging-port=9222
  3) Đăng nhập Shopify / mở app Chatty như bình thường`);
  process.exit(1);
}

const ctx = launched ? await browser.newContext({ viewport: { width: 1440, height: 900 } })
                     : browser.contexts()[0];
const pages = ctx.pages();

if (!launched && (has('--list') || (!has('--tab') && !has('--url')))) {
  console.log('Tab đang mở:');
  for (const [i, p] of pages.entries()) {
    let t = ''; try { t = await p.title(); } catch {}
    console.log(`  [${i}] ${t}\n      ${p.url()}`);
  }
  if (!has('--list')) console.error('\nThiếu --tab <n> hoặc --url <link>.');
  await browser.close(); process.exit(0);
}

let page;
if (has('--url')) {
  page = await ctx.newPage();
  await page.goto(val('--url'), { waitUntil: 'networkidle', timeout: 60000 });
} else {
  page = pages[Number(val('--tab'))];
  if (!page) { console.error('Không có tab số đó — chạy --list để xem.'); process.exit(1); }
  await page.bringToFront();
}

// Trang lazy-load (help center, docs) chỉ tải ảnh khi cuộn tới -> full-page
// chụp thẳng sẽ dính placeholder mờ. Cuộn hết 1 lượt rồi về đầu trước khi chụp.
if (has('--full')) {
  await page.evaluate(async () => {
    const step = window.innerHeight * 0.8;
    for (let y = 0; y < document.body.scrollHeight; y += step) {
      window.scrollTo(0, y);
      await new Promise(r => setTimeout(r, 250));
    }
    window.scrollTo(0, 0);
    await new Promise(r => setTimeout(r, 400));
  });
}

const wait = Number(val('--wait', 1500));
if (wait) await page.waitForTimeout(wait);

const name = val('--out', `shot-${Date.now()}.png`);
const file = path.isAbsolute(name) ? name : path.join(OUTDIR, name);

const opts = { path: file, fullPage: has('--full') };
if (has('--clip')) {
  const [x, y, width, height] = val('--clip').split(',').map(Number);
  opts.clip = { x, y, width, height }; opts.fullPage = false;
}
await page.screenshot(opts);
console.log(`file: ${file}`);

if (!has('--no-upload')) {
  const out = execFileSync('python3', [path.join(import.meta.dirname, 'upload.py'), file], { encoding: 'utf8' });
  process.stdout.write(out);
}
await browser.close();
