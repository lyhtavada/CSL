import { chromium } from 'playwright-core';

const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto('https://blauerboardshop.com', { waitUntil: 'networkidle', timeout: 60000 });
await page.waitForTimeout(2000);
try { await page.click('text=Rewards', { timeout: 10000 }); } catch(e) {}
await page.waitForTimeout(2000);

const frames = page.frames();
let widgetFrame = frames.find(f => /marsello/i.test(f.url()));

for (const tab of ['Earn', 'Redeem', 'Home']) {
  try {
    await widgetFrame.click(`text=${tab}`, { timeout: 8000 });
    await page.waitForTimeout(1200);
    const bodyText = await widgetFrame.evaluate(() => document.body.innerText);
    console.log(`=== TAB: ${tab} ===`);
    console.log(bodyText);
    console.log('');
  } catch(e) { console.log(`tab ${tab} failed:`, e.message); }
}

await browser.close();
