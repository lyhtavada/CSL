#!/usr/bin/env bun
/**
 * parse-transcripts.ts — deterministic friction-signal extractor for harness-retro.
 *
 * Reads ~/.claude/projects/-Users-avada-CSL/*.jsonl, strips noise, redacts secrets,
 * and writes a compact digest of friction signals to skills/harness-retro/.digest.json.
 *
 * Usage:
 *   bun parse-transcripts.ts --days 7 [--out path] [--summary]
 */

import { readdirSync, readFileSync, writeFileSync, statSync } from "fs";
import { homedir } from "os";
import { join } from "path";
import { createInterface } from "readline";
import { createReadStream } from "fs";

const PROJECT_DIR = join(homedir(), ".claude", "projects", "-Users-avada-CSL");
const DEFAULT_OUT = join(import.meta.dir, "..", ".digest.json");

const args = process.argv.slice(2);
function flag(name: string, def?: string) {
  const i = args.indexOf(`--${name}`);
  if (i === -1) return def;
  const v = args[i + 1];
  return v && !v.startsWith("--") ? v : "true";
}

const days = parseInt(flag("days", "7")!, 10);
const outPath = flag("out", DEFAULT_OUT)!;
const summary = args.includes("--summary");

const SECRET_RE = /(sk-[a-zA-Z0-9_-]{10,}|Bearer\s+[a-zA-Z0-9._-]{10,}|eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}|[A-Za-z0-9_-]{32,})/g;
function redact(s: string) {
  return s.replace(SECRET_RE, "[REDACTED]");
}

const CORRECTION_WORDS = ["no ", "no,", "not that", "wrong", "stop", "redo", "sai rồi", "không phải", "làm lại", "không đúng"];
const MISSING_CAP_WORDS = ["I don't have access", "no skill for", "not available in this session", "can't do that"];

type Signal = { type: string; detail?: string };
type SessionDigest = {
  file: string;
  turns: number;
  signals: Signal[];
};

function scanFile(path: string): SessionDigest {
  const raw = readFileSync(path, "utf-8");
  const lines = raw.split("\n").filter(Boolean);
  const signals: Signal[] = [];
  let turns = 0;
  const toolFailCounts: Record<string, number> = {};

  for (const line of lines) {
    let obj: any;
    try {
      obj = JSON.parse(line);
    } catch {
      continue;
    }
    if (obj.type === "user" || obj.type === "assistant") turns++;

    // tool errors
    if (obj.type === "tool_result" && obj.is_error) {
      const name = obj.tool_name || obj.name || "unknown_tool";
      toolFailCounts[name] = (toolFailCounts[name] || 0) + 1;
      signals.push({ type: "tool_error", detail: redact(String(obj.content || "").slice(0, 200)) });
    }

    // permission denials
    const textBlob = JSON.stringify(obj).toLowerCase();
    if (textBlob.includes("permission denied") || textBlob.includes("permission to use")) {
      signals.push({ type: "permission_denied" });
    }

    // user corrections
    if (obj.type === "user" && typeof obj.message?.content === "string") {
      const t = obj.message.content.toLowerCase();
      if (CORRECTION_WORDS.some((w) => t.startsWith(w) || t.includes(` ${w}`))) {
        signals.push({ type: "user_correction", detail: redact(obj.message.content.slice(0, 200)) });
      }
    }

    // missing capability
    if (obj.type === "assistant" && typeof obj.message?.content === "string") {
      const t = obj.message.content;
      if (MISSING_CAP_WORDS.some((w) => t.toLowerCase().includes(w.toLowerCase()))) {
        signals.push({ type: "missing_capability", detail: redact(t.slice(0, 200)) });
      }
    }

    // context compact
    if (textBlob.includes("/compact") || textBlob.includes("context_compact")) {
      signals.push({ type: "context_compact" });
    }
  }

  for (const [name, count] of Object.entries(toolFailCounts)) {
    if (count >= 3) signals.push({ type: "retry_loop", detail: `${name} failed ${count}x` });
  }
  if (turns >= 120) signals.push({ type: "high_churn_session", detail: `${turns} turns` });

  return { file: path, turns, signals };
}

function main() {
  let files: string[] = [];
  try {
    files = readdirSync(PROJECT_DIR)
      .filter((f) => f.endsWith(".jsonl"))
      .map((f) => join(PROJECT_DIR, f));
  } catch {
    console.error(`No transcript dir found at ${PROJECT_DIR}`);
    process.exit(1);
  }

  const cutoff = Date.now() - days * 24 * 60 * 60 * 1000;
  files = files.filter((f) => {
    try {
      return statSync(f).mtimeMs >= cutoff;
    } catch {
      return false;
    }
  });

  const sessions = files.map(scanFile);
  const signalTally: Record<string, number> = {};
  for (const s of sessions) {
    for (const sig of s.signals) {
      signalTally[sig.type] = (signalTally[sig.type] || 0) + 1;
    }
  }

  const digest = {
    generatedAt: new Date().toISOString(),
    windowDays: days,
    sessionCount: sessions.length,
    sessionsWithFriction: sessions.filter((s) => s.signals.length > 0).length,
    signalTally,
    sessions: sessions.filter((s) => s.signals.length > 0),
  };

  writeFileSync(outPath, JSON.stringify(digest, null, 2));

  if (summary) {
    console.log(`Sessions scanned: ${sessions.length} (last ${days}d)`);
    console.log(`Sessions with friction: ${digest.sessionsWithFriction}`);
    console.log("Signal tally:", signalTally);
  }
  console.log(`Digest written to ${outPath}`);
}

main();
