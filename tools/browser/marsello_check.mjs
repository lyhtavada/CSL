import { chromium } from 'playwright-core';

const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto('https://blauerboardshop.com', { waitUntil: 'networkidle', timeout: 60000 });
await page.waitForTimeout(2000);

// close popup if any
try { await page.click('text=Rewards', { timeout: 10000 }); } catch(e) { console.log('open widget click failed', e.message); }
await page.waitForTimeout(2000);

// find iframe
const frames = page.frames();
console.log('frames:', frames.map(f => f.url()));

let widgetFrame = null;
for (const f of frames) {
  if (/marsello|smile|loyaltylion|widget/i.test(f.url())) { widgetFrame = f; break; }
}
if (!widgetFrame) {
  console.log('no widget iframe found, trying largest non-main frame');
  widgetFrame = frames.find(f => f !== page.mainFrame());
}

if (widgetFrame) {
  try {
    await widgetFrame.click('text=Redeem', { timeout: 10000 });
    await page.waitForTimeout(1500);
  } catch(e) { console.log('click redeem in frame failed:', e.message); }

  const bodyText = await widgetFrame.evaluate(() => document.body.innerText);
  console.log('=== WIDGET TEXT AFTER REDEEM CLICK ===');
  console.log(bodyText);
}

await page.screenshot({ path: '/tmp/bb-redeem-full.png' });
await browser.close();
