/**
 * Builds the exact request, then either answers locally (mock) or POSTs it to the proxy.
 * The browser never contains an xAI API key.
 */
import { CONFIG } from "../config.js";
import { deidentifyCase, findLeaks } from "./deidentify.js";
import { buildMessages, buildPlanMessages } from "./prompt.js";
import { standingWords } from "./standing.js";
import { searchDocs, contextFromHits, bundledSearchDocs } from "./library.js";
import { mockReply } from "./mock.js";

export function isMock() {
  return CONFIG.mode !== "live" || !String(CONFIG.proxyUrl || "").trim();
}

export function proxyLabel() {
  if (isMock()) return "Mock mode on this browser (nothing is transmitted)";
  try { return new URL(CONFIG.proxyUrl).host; } catch { return CONFIG.proxyUrl; }
}

export function deidentify(caseRecord) {
  return deidentifyCase(caseRecord);
}

async function libraryContext(query, useLibrary, userDocs) {
  if (!useLibrary) return { text: "", sources: [] };
  const docs = [...(await bundledSearchDocs()), ...(userDocs || [])];
  return contextFromHits(searchDocs(docs, query, 4));
}

export async function prepareChat({ caseRecord, caseText, history, useLibrary, userDocs, question }) {
  const hist = (history || []).filter((m) => m && (m.role === "user" || m.role === "assistant"));
  const concerns = (/Presenting concerns:\n([\s\S]*?)(\n\n|$)/.exec(caseText) || [])[1] || "";
  const context = await libraryContext((question + "\n" + concerns).slice(0, 1500), useLibrary, userDocs);
  const messages = buildMessages(caseText, hist, context);
  const leaks = findLeaks([caseText, ...hist.map((m) => m.content), question || "", context.text || ""].join("\n"), caseRecord);
  return {
    kind: "chat",
    messages,
    leaks,
    sources: context.sources,
    preview: previewOf({ caseText, question, history: hist, context, leaks, kind: "chat" }),
  };
}

export async function preparePlan({ caseRecord, caseText, useLibrary, userDocs }) {
  const context = await libraryContext(caseText.slice(0, 1500), useLibrary, userDocs);
  const messages = buildPlanMessages(caseText, context.text);
  const leaks = findLeaks([caseText, context.text || ""].join("\n"), caseRecord);
  return {
    kind: "plan",
    messages,
    leaks,
    sources: context.sources,
    preview: previewOf({
      caseText,
      question: messages[messages.length - 1].content,
      history: [],
      context,
      leaks,
      kind: "plan",
    }),
  };
}

function previewOf({ caseText, question, history, context, leaks, kind }) {
  return {
    host: proxyLabel(),
    model: isMock() ? "mock-fictional" : CONFIG.model,
    mock: isMock(),
    kind,
    caseText,
    question: question || "",
    history: history || [],
    library: context.sources || [],
    libraryText: context.text || "",
    standingWords: standingWords(),
    leaks,
  };
}

export function rememberMembershipToken(token) {
  if (token) sessionStorage.setItem("cc-membership-token", token);
}

/** Plain sentence for a failed live call. Does not include keys or case text. */
export function friendlyAiError(err) {
  const code = err && err.code;
  if (code === "MEMBER_REQUIRED" || code === "NO_NETWORK") {
    return "Please open Clinical Companion from the Counselors' Room.";
  }
  return "Clinical Companion could not get an answer just now. Please try again.";
}

export async function complete(prepared) {
  if (isMock()) {
    await new Promise((r) => setTimeout(r, 350));
    const question = prepared.kind === "plan" ? "10-session plan" : prepared.preview.question || "";
    return mockReply({ kind: prepared.kind, question, sources: prepared.sources });
  }
  const headers = { "Content-Type": "application/json" };
  const token = sessionStorage.getItem("cc-membership-token") || "";
  if (token) headers.Authorization = "Bearer " + token;
  let res;
  try {
    res = await fetch(String(CONFIG.proxyUrl).trim(), {
      method: "POST",
      headers,
      body: JSON.stringify({
        action: "chat",
        model: CONFIG.model,
        maxTokens: CONFIG.maxTokens,
        reasoningEffort: CONFIG.reasoningEffort,
        messages: prepared.messages,
      }),
    });
  } catch {
    const e = new Error("Please open Clinical Companion from the Counselors' Room.");
    e.code = "NO_NETWORK";
    throw e;
  }
  let body = {};
  try { body = await res.json(); } catch { body = {}; }
  if (!res.ok) {
    const code = body.code || (res.status === 401 || res.status === 403 ? "MEMBER_REQUIRED" : "PROXY");
    const e = new Error(friendlyAiError({ code }));
    e.code = code;
    throw e;
  }
  return { content: body.content || "", thinking: body.thinking || "", model: body.model || CONFIG.model, mock: false };
}
