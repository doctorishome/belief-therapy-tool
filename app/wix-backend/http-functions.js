/**
 * Clinical Companion AI proxy for Wix Velo.
 *
 * Paste this file into the site Backend section. If http-functions.js already
 * exists, copy options_clinicalCompanion and post_clinicalCompanion into it.
 * Also paste cc-token.js into Backend.
 *
 * The xAI key is read from Wix Secrets (name: XAI_API_KEY). It is never returned
 * to the browser. Request text is not written to a collection.
 *
 * URL after you publish:
 *   https://www.beliefcounselor.com/_functions/clinicalCompanion
 * Put that single URL in app/config.js (proxyUrl) and set mode to "live".
 * Any other server that accepts the same JSON can be used instead.
 */
import { ok, badRequest, forbidden, serverError, response } from "wix-http-functions";
import { fetch } from "wix-fetch";
import { secrets } from "wix-secrets-backend.v2";
import { elevate } from "wix-auth";
import { orders } from "wix-pricing-plans.v2";
import wixData from "wix-data";
import { verifyMembershipToken } from "backend/cc-token";
import {
  MEMBER_MONTHLY_AI_BUDGET_USD,
  MAX_ANSWER_OUTPUT_TOKENS,
  CLASSIFIER_MODEL,
  CLASSIFIER_MAX_TOKENS,
  MAIN_MODEL,
  OFF_TOPIC_DECLINE,
  BUDGET_MESSAGE,
  heuristicScope,
  parseClassifier,
  latestUserText,
  costUsd,
  estimateUsd,
  usageSummary,
  isBudgetExempt,
  monthKey,
} from "backend/ai-budget";

const elevatedGetSecretValue = elevate(secrets.getSecretValue);

/** Browser origins allowed to call this function. Add a custom domain here if you use one. */
const ALLOWED_ORIGINS = [
  "https://doctorishome.github.io",
  "http://localhost:8080",
  "http://127.0.0.1:8080",
];

/**
 * Leave blank to allow any active Pricing Plan, including the free week.
 * Set to part of a plan name (for example "Clinical") to require that plan.
 */
const PLAN_NAME_INCLUDES = "";

const XAI_URL = "https://api.x.ai/v1/chat/completions";
const DEFAULT_MODEL = MAIN_MODEL;
const USAGE_COLLECTION = "ClinicalCompanionUsage";
const MAX_CHARS = 120000;

function header(request, name) {
  const headers = (request && request.headers) || {};
  const want = name.toLowerCase();
  for (const key of Object.keys(headers)) {
    if (String(key).toLowerCase() === want) return headers[key];
  }
  return "";
}

function cors(request) {
  const origin = header(request, "origin");
  return {
    "Access-Control-Allow-Origin": ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0],
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Max-Age": "86400",
    "Content-Type": "application/json",
  };
}

function json(request, statusFn, body) {
  return statusFn({ headers: cors(request), body });
}

function secretString(value) {
  if (typeof value === "string") return value.trim();
  if (value && typeof value.value === "string") return value.value.trim();
  return "";
}

async function memberFromWixSession() {
  try {
    const list = await orders.memberListOrders();
    const order = ((list && list.orders) || []).find((/** @type {any} */ order) => {
      if (!order || (order.status !== "ACTIVE" && order.statusNew !== "ACTIVE")) return false;
      if (!PLAN_NAME_INCLUDES) return true;
      return String(order.planName || "").toLowerCase().includes(String(PLAN_NAME_INCLUDES).toLowerCase());
    }) || null;
    if (!order) return null;
    const memberId = order.buyer && order.buyer.memberId ? String(order.buyer.memberId) : "";
    return { memberId, staff: false };
  } catch {
    return null;
  }
}

async function membershipOk(request) {
  const session = await memberFromWixSession();
  if (session) return { ok: true, memberId: session.memberId, staff: false };
  const match = /^Bearer\s+(\S+)/i.exec(header(request, "authorization") || "");
  if (!match) return { ok: false, code: "MEMBER_REQUIRED", error: "Please open Clinical Companion from the Counselors' Room." };
  let secret = "";
  try { secret = secretString(await elevatedGetSecretValue("CC_MEMBERSHIP_SECRET")); }
  catch { return { ok: false, code: "NOT_CONFIGURED", error: "The membership check is not set up yet." }; }
  if (!secret) return { ok: false, code: "NOT_CONFIGURED", error: "The membership check is not set up yet." };
  const payload = await verifyMembershipToken(match[1], secret);
  if (!payload) return { ok: false, code: "MEMBER_REQUIRED", error: "Please open Clinical Companion from the Counselors' Room." };
  return { ok: true, memberId: String(payload.memberId || ""), staff: !!payload.staff };
}

function checkMessages(messages) {
  if (!Array.isArray(messages) || !messages.length || messages.length > 40) return "The request was not in the expected shape.";
  let chars = 0;
  for (const message of messages) {
    if (!message || !["system", "user", "assistant"].includes(message.role) || typeof message.content !== "string") {
      return "The request was not in the expected shape.";
    }
    chars += message.content.length;
  }
  if (chars > MAX_CHARS) return "That request is too long.";
  return "";
}

function usageFromXai(usage) {
  const details = (usage && usage.prompt_tokens_details) || {};
  return {
    prompt_tokens: Number(usage && usage.prompt_tokens) || 0,
    completion_tokens: Number(usage && usage.completion_tokens) || 0,
    cached_tokens: Number(details.cached_tokens) || 0,
  };
}

async function readMonth(memberId, month) {
  const found = await wixData.query(USAGE_COLLECTION)
    .eq("memberId", memberId)
    .eq("month", month)
    .limit(1)
    .find({ suppressAuth: true });
  return (found.items && found.items[0]) || null;
}

async function addCost(memberId, month, model, usage) {
  const added = costUsd(model, usage);
  const row = await readMonth(memberId, month);
  const next = {
    memberId,
    month,
    inputTokens: Number(row && row.inputTokens) || 0,
    outputTokens: Number(row && row.outputTokens) || 0,
    cachedTokens: Number(row && row.cachedTokens) || 0,
    costUsd: Number(row && row.costUsd) || 0,
  };
  next.inputTokens += usage.prompt_tokens;
  next.outputTokens += usage.completion_tokens;
  next.cachedTokens += usage.cached_tokens;
  next.costUsd = Math.round((next.costUsd + added) * 1000000) / 1000000;
  if (row && row._id) next._id = row._id;
  if (next._id) await wixData.update(USAGE_COLLECTION, next, { suppressAuth: true });
  else await wixData.insert(USAGE_COLLECTION, next, { suppressAuth: true });
  return next.costUsd;
}

async function callXai(apiKey, payload) {
  const upstream = await fetch(XAI_URL, {
    method: "post",
    headers: { "Content-Type": "application/json", Authorization: "Bearer " + apiKey },
    body: JSON.stringify(payload),
  });
  let data = {};
  try { data = await upstream.json(); } catch (e) { data = {}; }
  return { ok: !!upstream.ok, status: upstream.status, data };
}

async function classifyQuestion(apiKey, question) {
  const heuristic = heuristicScope(question);
  if (heuristic !== "UNSURE") return { scope: heuristic, usage: null };
  try {
    const result = await callXai(apiKey, {
      model: CLASSIFIER_MODEL,
      messages: [
        { role: "system", content: "Reply with exactly one word: CLINICAL or OFF_TOPIC. CLINICAL means counseling, mental-health assessment, diagnosis support, treatment, documentation, ethics, risk, or faith inside counseling. If unsure, reply CLINICAL." },
        { role: "user", content: String(question || "").slice(0, 600) },
      ],
      max_completion_tokens: CLASSIFIER_MAX_TOKENS,
      temperature: 0,
    });
    if (!result.ok) return { scope: "CLINICAL", usage: null };
    const choice = (result.data.choices && result.data.choices[0] && result.data.choices[0].message) || {};
    return { scope: parseClassifier(choice.content), usage: usageFromXai(result.data.usage) };
  } catch (e) {
    return { scope: "CLINICAL", usage: null };
  }
}

export function options_clinicalCompanion(request) {
  return response({ status: 204, headers: cors(request) });
}

export async function post_clinicalCompanion(request) {
  let body;
  try { body = await request.body.json(); }
  catch { return json(request, badRequest, { error: "The request could not be read.", code: "BAD_REQUEST" }); }

  const gate = await membershipOk(request);
  if (!gate.ok) return json(request, forbidden, { error: gate.error, code: gate.code });

  const month = monthKey();
  const exempt = isBudgetExempt(gate.memberId, gate.staff);
  if (!exempt && !gate.memberId) {
    return json(request, serverError, { error: "Clinical Companion could not check this month's allowance, so nothing was sent.", code: "USAGE_UNAVAILABLE" });
  }
  let spent = 0;
  if (!exempt) {
    try {
      const row = await readMonth(gate.memberId || "unknown", month);
      spent = Number(row && row.costUsd) || 0;
    } catch (e) {
      return json(request, serverError, { error: "Clinical Companion could not check this month's allowance, so nothing was sent.", code: "USAGE_UNAVAILABLE" });
    }
  }
  const meter = usageSummary(spent);

  if (body.action === "health" || body.action === "usage") {
    return json(request, ok, { ok: true, membership: "active", usage: meter, exempt });
  }
  if (body.action !== "chat") return json(request, badRequest, { error: "Unknown action.", code: "BAD_REQUEST" });

  const problem = checkMessages(body.messages);
  if (problem) return json(request, badRequest, { error: problem, code: "BAD_REQUEST" });

  if (!exempt && spent >= MEMBER_MONTHLY_AI_BUDGET_USD) {
    return json(request, forbidden, { error: BUDGET_MESSAGE, code: "BUDGET", usage: meter });
  }

  let apiKey = "";
  try { apiKey = secretString(await elevatedGetSecretValue("XAI_API_KEY")); }
  catch { return json(request, serverError, { error: "The AI key is not available.", code: "NOT_CONFIGURED" }); }
  if (!apiKey) return json(request, serverError, { error: "The AI key is not available.", code: "NOT_CONFIGURED" });

  const question = latestUserText(body.messages);
  let classified;
  try { classified = await classifyQuestion(apiKey, question); }
  catch (e) { classified = { scope: "CLINICAL", usage: null }; }
  if (!exempt && classified.usage) {
    try { spent = await addCost(gate.memberId || "unknown", month, CLASSIFIER_MODEL, classified.usage); }
    catch (e) { return json(request, serverError, { error: "Clinical Companion could not record this month's usage, so nothing was sent.", code: "USAGE_UNAVAILABLE" }); }
  }
  if (classified.scope === "OFF_TOPIC") {
    return json(request, ok, { content: OFF_TOPIC_DECLINE, offTopic: true, model: CLASSIFIER_MODEL, usage: usageSummary(spent), exempt });
  }

  const model = DEFAULT_MODEL;
  const effort = ["low", "medium", "high"].includes(body.reasoningEffort) ? body.reasoningEffort : "medium";
  let maxTokens = Number(body.maxTokens) || MAX_ANSWER_OUTPUT_TOKENS;
  if (maxTokens < 256) maxTokens = 256;
  if (maxTokens > MAX_ANSWER_OUTPUT_TOKENS) maxTokens = MAX_ANSWER_OUTPUT_TOKENS;

  const messages = body.messages.map((message) => ({ role: message.role, content: message.content }));
  if (!exempt && spent + estimateUsd(messages, maxTokens, model) > MEMBER_MONTHLY_AI_BUDGET_USD) {
    return json(request, forbidden, { error: BUDGET_MESSAGE, code: "BUDGET", usage: usageSummary(spent) });
  }

  let result;
  try {
    result = await callXai(apiKey, {
      model,
      messages,
      max_completion_tokens: maxTokens,
      reasoning_effort: effort,
      stream: false,
    });
  } catch (e) {
    return json(request, serverError, { error: "The AI service could not be reached.", code: "UPSTREAM" });
  }
  if (!result.ok) {
    const code = result.status === 401 ? "BAD_KEY" : result.status === 429 ? "RATE_LIMIT" : "UPSTREAM";
    return json(request, serverError, { error: "The AI service reported a problem.", code, usage: usageSummary(spent) });
  }
  const choice = (result.data.choices && result.data.choices[0] && (result.data.choices[0].message || result.data.choices[0].delta)) || {};
  const mainUsage = usageFromXai(result.data.usage);
  if (!exempt) {
    try { spent = await addCost(gate.memberId || "unknown", month, model, mainUsage); }
    catch (e) { /* the answer is already produced; this one charge is missing if the write failed */ }
  }
  return json(request, ok, {
    content: typeof choice.content === "string" ? choice.content : "",
    thinking: typeof choice.reasoning_content === "string" ? choice.reasoning_content : "",
    model: result.data.model || model,
    usage: usageSummary(spent),
    exempt,
  });
}
