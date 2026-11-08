// E3: headless render of the same official sites. No stealth, no UA spoofing, no retries on a block.
import { createRequire } from "node:module";
import fs from "node:fs";
const require = createRequire("C:/Users/prasa/Documents/Github/JobHub/_prototypes/02_persona-job-review-v3/package.json");
const { chromium } = require("playwright");
const RUN = new URL("..", import.meta.url).pathname.replace(/^\//, "");
const sites = JSON.parse(fs.readFileSync(RUN + "outputs/e2_plain_fetch.json", "utf8")).filter(s => s.url);
const out = [];
const browser = await chromium.launch({ headless: true });
for (const s of sites) {
  const rec = { id: s.id, url: s.url, plain_status: s.status, plain_chars: s.visible_chars ?? null };
  const t0 = Date.now();
  try {
    const ctx = await browser.newContext(); const page = await ctx.newPage();
    const resp = await page.goto(s.url, { waitUntil: "domcontentloaded", timeout: 30000 });
    await page.waitForLoadState("networkidle", { timeout: 8000 }).catch(() => {});
    const text = await page.evaluate(() => document.body.innerText);
    rec.http = resp?.status(); rec.rendered_chars = text.length; rec.title = (await page.title()).slice(0, 100);
    rec.status = rec.http >= 400 ? `http_${rec.http}` : (text.length >= 500 ? "ok" : "thin");
    fs.writeFileSync(RUN + `outputs/pages/${s.id}_rendered.txt`, text.slice(0, 60000));
    await ctx.close();
  } catch (e) { rec.status = "render_failed:" + String(e.message).split("\n")[0].slice(0, 80); }
  rec.seconds = +((Date.now() - t0) / 1000).toFixed(1); out.push(rec); console.log(rec.id, rec.status, rec.plain_chars, "->", rec.rendered_chars, rec.seconds + "s");
}
await browser.close();
fs.writeFileSync(RUN + "outputs/e3_playwright_render.json", JSON.stringify(out, null, 1));
