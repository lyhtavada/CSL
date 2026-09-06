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
 *   node shot.mjs --tab 2 --clip 0,0,1200,800   # chụp 1 vùng theo toạ độ
 *   thêm --no-upload nếu chỉ muốn file local
 *
 * Tương tác trước khi chụp — lặp --do bao nhiêu lần cũng được, chạy đúng thứ tự:
 *   --do 'click:text=Settings'      bấm (selector CSS, hoặc text=/role= của Playwright)
 *   --do 'fill:#email=abc@x.com'    gõ vào ô input
 *   --do 'press:Enter'              bấm phím (hoặc 'press:#q=Enter' cho 1 ô cụ thể)
 *   --do 'select:#plan=pro'         chọn dropdown
 *   --do 'hover:.menu'              rê chuột (mở submenu)
 *   --do 'scrollto:h2#pricing'      cuộn tới
 *   --do 'waitfor:.modal'           chờ tới khi element hiện ra
 *   --do 'wait:2000'                chờ 2 giây
 *   --do 'goto:https://...'         điều hướng sang trang khác
 *
 * Chụp gọn / che dữ liệu:
 *   --element '.pricing-table'      chỉ chụp 1 element, không chụp cả trang
 *   --hide '.crisp-client'          ẩn hẳn element (widget chat, banner cookie)
 *   --mask '.customer-name'         bôi hộp che (dữ liệu merchant) — lặp được
 *   --viewport 1440x900             đổi kích thước cửa sổ
 */
import { chromium } from 'playwright-core';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import fs from 'node:fs';

const args = process.argv.slice(2);
const has = f => args.includes(f);
const val = (f, d) => { const i = args.indexOf(f); return i >= 0 ? args[i + 1] : d; };
// lấy TẤT CẢ giá trị của 1 flag lặp lại, giữ nguyên thứ tự dòng lệnh
const vals = f => args.reduce((a, x, i) => (x === f && args[i + 1] ? [...a, args[i + 1]] : a), []);

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

const [vw, vh] = val('--viewport', '1440x900').split('x').map(Number);
const ctx = launched ? await browser.newContext({ viewport: { width: vw, height: vh } })
                     : browser.contexts()[0];
const pages = ctx.pages();

// Khi ATTACH vào Chrome của Liz: tuyệt đối không browser.close() — nó đóng luôn
// mọi tab Liz đang mở. Chỉ dọn đúng tab do script này tạo ra rồi ngắt kết nối.
let ownPage = null;
async function finish(code) {
  try {
    if (launched) await browser.close();
    // Attach: chỉ đóng tab do chính script mở ra. Không đụng browser —
    // process.exit() bên dưới tự ngắt kết nối CDP, Chrome của Liz nguyên vẹn.
    else if (ownPage) await ownPage.close().catch(() => {});
  } catch {}
  process.exit(code);
}

if (!launched && (has('--list') || (!has('--tab') && !has('--url')))) {
  console.log('Tab đang mở:');
  for (const [i, p] of pages.entries()) {
    let t = ''; try { t = await p.title(); } catch {}
    console.log(`  [${i}] ${t}\n      ${p.url()}`);
  }
  if (!has('--list')) console.error('\nThiếu --tab <n> hoặc --url <link>.');
  await finish(0);
}

let page;
if (has('--url')) {
  page = await ctx.newPage();
  if (!launched) ownPage = page;
  await page.goto(val('--url'), { waitUntil: 'networkidle', timeout: 60000 });
} else {
  page = pages[Number(val('--tab'))];
  if (!page) { console.error('Không có tab số đó — chạy --list để xem.'); await finish(1); }
  await page.bringToFront();
  if (has('--viewport')) await page.setViewportSize({ width: vw, height: vh });
}

// ── các bước tương tác, chạy tuần tự theo đúng thứ tự --do trên dòng lệnh ──
const STEP_TIMEOUT = Number(val('--step-timeout', 15000));
for (const step of vals('--do')) {
  const i = step.indexOf(':');
  if (i < 0) { console.error(`--do sai cú pháp (thiếu dấu ':'): ${step}`); process.exit(1); }
  const op = step.slice(0, i).trim().toLowerCase();
  const rest = step.slice(i + 1);
  // với fill/select/press-vào-ô: tách 'selector=giá trị' ở dấu '=' CUỐI cùng,
  // để selector chứa '=' (vd [data-id=x]) vẫn dùng được
  const eq = rest.lastIndexOf('=');
  const sel = eq >= 0 ? rest.slice(0, eq) : rest;
  const arg = eq >= 0 ? rest.slice(eq + 1) : null;
  const o = { timeout: STEP_TIMEOUT };
  try {
    switch (op) {
      case 'click':    await page.click(rest, o); break;
      case 'hover':    await page.hover(rest, o); break;
      case 'fill':     await page.fill(sel, arg ?? '', o); break;
      case 'select':   await page.selectOption(sel, arg ?? '', o); break;
      case 'press':    arg !== null ? await page.press(sel, arg, o)
                                    : await page.keyboard.press(rest); break;
      case 'scrollto': await page.locator(rest).scrollIntoViewIfNeeded(o); break;
      case 'waitfor':  await page.waitForSelector(rest, o); break;
      case 'wait':     await page.waitForTimeout(Number(rest)); break;
      case 'goto':     await page.goto(rest, { waitUntil: 'networkidle', timeout: 60000 }); break;
      default: console.error(`--do không hiểu lệnh '${op}'. Xem đầu file shot.mjs.`); process.exit(1);
    }
  } catch (e) {
    console.error(`--do '${step}' thất bại: ${e.message.split('\n')[0]}`);
    await finish(1);
  }
  console.error(`  ✓ ${step}`);
}

// ẩn hẳn element không muốn có trong ảnh (widget chat, banner cookie)
for (const sel of vals('--hide')) {
  await page.evaluate(s => document.querySelectorAll(s).forEach(el => el.style.setProperty('display', 'none', 'important')), sel);
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
const masks = vals('--mask');
if (masks.length) opts.mask = masks.map(s => page.locator(s));
if (has('--clip')) {
  const [x, y, width, height] = val('--clip').split(',').map(Number);
  opts.clip = { x, y, width, height }; opts.fullPage = false;
}

if (has('--element')) {
  const el = page.locator(val('--element')).first();
  await el.scrollIntoViewIfNeeded({ timeout: STEP_TIMEOUT });
  delete opts.fullPage; delete opts.clip;
  await el.screenshot(opts);
} else {
  await page.screenshot(opts);
}
console.log(`file: ${file}`);

if (!has('--no-upload')) {
  const out = execFileSync('python3', [path.join(import.meta.dirname, 'upload.py'), file], { encoding: 'utf8' });
  process.stdout.write(out);
}
await finish(0);
