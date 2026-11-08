import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const port = Number(process.env.PORT || 8767);
const maxChars = 120_000;

function json(res, status, body) {
  res.writeHead(status, { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' });
  res.end(JSON.stringify(body));
}

function classify({ title, text, url }) {
  const lower = `${title}\n${text}`.toLowerCase();
  if (/captcha|verify you are human|security check|access denied/.test(lower)) return 'capture_unavailable';
  if (text.length < 2_000 && /sign in|log in|join linkedin|create an account/.test(lower)) return 'capture_unavailable';
  if (!text || text.length < 180) return 'partial';
  if (!/job|role|responsibilit|requirement|salary|apply|employment|experience/.test(lower)) return 'partial';
  return url ? 'captured' : 'partial';
}

async function readRequest(req) {
  let body = '';
  for await (const chunk of req) {
    body += chunk;
    if (body.length > 20_000) throw new Error('request too large');
  }
  return JSON.parse(body || '{}');
}

async function capture(url) {
  let playwright;
  try {
    playwright = await import('playwright');
  } catch {
    return { status: 'capture_unavailable', url, text: '', message: 'Playwright is not installed. Paste the job description instead.' };
  }
  let browser;
  try {
    browser = await playwright.chromium.launch({ headless: true });
    const context = await browser.newContext({ javaScriptEnabled: true });
    const page = await context.newPage();
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20_000 });
    await page.waitForTimeout(1_000);
    const result = await page.evaluate(() => ({
      title: document.title || '',
      text: document.body?.innerText || '',
      jsonLd: [...document.querySelectorAll('script[type="application/ld+json"]')].map(node => node.textContent || '').slice(0, 5)
    }));
    const text = result.text.slice(0, maxChars);
    return { status: classify({ ...result, text, url }), url, title: result.title, text, jsonLd: result.jsonLd };
  } catch (error) {
    return { status: 'capture_unavailable', url, text: '', message: `The page could not be read: ${error.message}` };
  } finally {
    await browser?.close();
  }
}

async function serveFile(req, res) {
  const requestPath = decodeURIComponent(new URL(req.url, `http://${req.headers.host}`).pathname);
  const relative = requestPath === '/' ? 'index.html' : requestPath.replace(/^\/+/, '');
  const target = path.resolve(root, relative);
  if (!target.startsWith(root)) return json(res, 400, { error: 'invalid path' });
  try {
    const data = await fs.readFile(target);
    const type = target.endsWith('.html') ? 'text/html' : target.endsWith('.json') ? 'application/json' : target.endsWith('.txt') ? 'text/plain' : 'application/octet-stream';
    res.writeHead(200, { 'content-type': `${type}; charset=utf-8` }); res.end(data);
  } catch { json(res, 404, { error: 'not found' }); }
}

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === 'POST' && req.url === '/api/capture') {
      const { url } = await readRequest(req);
      if (typeof url !== 'string' || !/^https?:\/\//i.test(url)) return json(res, 400, { status: 'capture_unavailable', message: 'A public http(s) URL is required.' });
      return json(res, 200, await capture(url));
    }
    if (req.method === 'GET') return serveFile(req, res);
    return json(res, 405, { error: 'method not allowed' });
  } catch (error) { return json(res, 500, { error: error.message }); }
});

server.listen(port, '127.0.0.1', () => console.log(`JobHub V3 running at http://127.0.0.1:${port}/`));
