import fs from "node:fs/promises";
import process from "node:process";
import dotenv from "dotenv";
import { chromium } from "playwright";
import OpenAI from "openai";

dotenv.config({ path: new URL("../../../.env", import.meta.url) });

const args = process.argv.slice(2);
const valueAfter = (flag) => {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : null;
};
const hasFlag = (flag) => args.includes(flag);
const url = valueAfter("--url");
const textFile = valueAfter("--text-file");
const outputFile = valueAfter("--out") || "capture.json";

if (!url && !textFile) {
  console.error("Usage: node capture-and-extract.mjs --url <url> [--out capture.json] [--extract]");
  console.error("   or: node capture-and-extract.mjs --text-file posting.txt [--out report.json] [--extract]");
  process.exit(1);
}

async function captureUrl(targetUrl) {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    const response = await page.goto(targetUrl, { waitUntil: "domcontentloaded", timeout: 30000 });
    await page.waitForTimeout(1500);
    const pageData = await page.evaluate(() => {
      const jsonLd = [...document.querySelectorAll('script[type="application/ld+json"]')]
        .map((node) => { try { return JSON.parse(node.textContent); } catch { return null; } })
        .filter(Boolean);
      return {
        title: document.title || null,
        visible_text: document.body?.innerText || "",
        json_ld: jsonLd,
        canonical: document.querySelector('link[rel="canonical"]')?.href || null
      };
    });
    const blocked = !pageData.visible_text.trim() || /captcha|verify you are human|access denied/i.test(pageData.visible_text);
    return {
      input_type: "url",
      url: targetUrl,
      http_status: response?.status() ?? null,
      captured_at: new Date().toISOString(),
      capture_status: blocked ? "blocked" : "captured",
      title: pageData.title,
      canonical: pageData.canonical,
      visible_text: pageData.visible_text,
      json_ld: pageData.json_ld
    };
  } finally {
    await browser.close();
  }
}

async function captureText(file) {
  const text = await fs.readFile(file, "utf8");
  return {
    input_type: "pasted_text",
    url: null,
    captured_at: new Date().toISOString(),
    capture_status: text.trim() ? "captured" : "partial",
    title: null,
    canonical: null,
    visible_text: text,
    json_ld: []
  };
}

async function extractReport(capture) {
  if (!process.env.GROQ_API_KEY && !process.env.OPENAI_API_KEY) {
    return { status: "not_run", reason: "No OpenAI-compatible API key configured." };
  }
  const client = new OpenAI({
    apiKey: process.env.GROQ_API_KEY || process.env.OPENAI_API_KEY,
    baseURL: process.env.GROQ_API_KEY ? (process.env.GROQ_BASE_URL || "https://api.groq.com/openai/v1") : undefined
  });
  const model = process.env.GROQ_MODEL || process.env.OPENAI_MODEL;
  if (!model) return { status: "not_run", reason: "Set GROQ_MODEL or OPENAI_MODEL before running extraction." };

  const response = await client.chat.completions.create({
    model,
    temperature: 0,
    response_format: { type: "json_object" },
    messages: [
      {
        role: "system",
        content: "Extract a concise JobHub V2 report. Use only the captured posting. Do not invent duties, qualifications, salary rules, employer identity, fit or legitimacy. Treat missing information as missing. Describe red flags as things to check, never as a scam verdict. Return JSON matching report.schema.json."
      },
      {
        role: "user",
        content: JSON.stringify({ source: capture, user_skills: "Not provided" })
      }
    ]
  });
  return { status: "extracted", model, report: JSON.parse(response.choices[0].message.content) };
}

const capture = url ? await captureUrl(url) : await captureText(textFile);
const result = { capture, extraction: hasFlag("--extract") ? await extractReport(capture) : { status: "not_requested" } };
await fs.writeFile(outputFile, JSON.stringify(result, null, 2), "utf8");
console.log(JSON.stringify({ output: outputFile, capture_status: capture.capture_status, extraction_status: result.extraction.status }, null, 2));
