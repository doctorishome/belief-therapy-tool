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
import { verifyMembershipToken } from "backend/cc-token";

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
const DEFAULT_MODEL = "grok-4.7";
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
    return ((list && list.orders) || []).find((order) => {
      if (!order || (order.status !== "ACTIVE" && order.statusNew !== "ACTIVE")) return false;
      if (!PLAN_NAME_INCLUDES) return true;
      return String(order.planName || "").toLowerCase().includes(PLAN_NAME_INCLUDES.toLowerCase());
    }) || null;
  } catch {
    return null;
  }
}

async function membershipOk(request) {
  if (await memberFromWixSession()) return { ok: true };
  const match = /^Bearer\s+(\S+)/i.exec(header(request, "authorization") || "");
  if (!match) return { ok: false, code: "MEMBER_REQUIRED", error: "Sign in on the Counselors page first." };
  let secret = "";
  try { secret = secretString(await elevatedGetSecretValue("CC_MEMBERSHIP_SECRET")); }
  catch { return { ok: false, code: "NOT_CONFIGURED", error: "The membership check is not set up yet." }; }
  if (!secret) return { ok: false, code: "NOT_CONFIGURED", error: "The membership check is not set up yet." };
  const payload = await verifyMembershipToken(match[1], secret);
  if (!payload) return { ok: false, code: "MEMBER_REQUIRED", error: "Sign in again on the Counselors page. This tab’s membership check has expired." };
  return { ok: true };
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

export function options_clinicalCompanion(request) {
  return response({ status: 204, headers: cors(request) });
}

export async function post_clinicalCompanion(request) {
  let body;
  try { body = await request.body.json(); }
  catch { return json(request, badRequest, { error: "The request could not be read.", code: "BAD_REQUEST" }); }

  const gate = await membershipOk(request);
  if (!gate.ok) return json(request, forbidden, { error: gate.error, code: gate.code });

  if (body.action === "health") return json(request, ok, { ok: true, membership: "active" });
  if (body.action !== "chat") return json(request, badRequest, { error: "Unknown action.", code: "BAD_REQUEST" });

  const problem = checkMessages(body.messages);
  if (problem) return json(request, badRequest, { error: problem, code: "BAD_REQUEST" });

  let apiKey = "";
  try { apiKey = secretString(await elevatedGetSecretValue("XAI_API_KEY")); }
  catch { return json(request, serverError, { error: "The AI key is not available.", code: "NOT_CONFIGURED" }); }
  if (!apiKey) return json(request, serverError, { error: "The AI key is not available.", code: "NOT_CONFIGURED" });

  const model = /^[A-Za-z0-9._:-]{1,64}$/.test(String(body.model || "")) ? String(body.model) : DEFAULT_MODEL;
  const effort = ["low", "medium", "high"].includes(body.reasoningEffort) ? body.reasoningEffort : "medium";
  let maxTokens = Number(body.maxTokens) || 4000;
  if (maxTokens < 256) maxTokens = 256;
  if (maxTokens > 8000) maxTokens = 8000;

  let upstream;
  try {
    upstream = await fetch(XAI_URL, {
      method: "post",
      headers: { "Content-Type": "application/json", Authorization: "Bearer " + apiKey },
      body: JSON.stringify({
        model,
        messages: body.messages.map((message) => ({ role: message.role, content: message.content })),
        max_completion_tokens: maxTokens,
        reasoning_effort: effort,
        stream: false,
      }),
    });
  } catch {
    return json(request, serverError, { error: "The AI service could not be reached.", code: "UPSTREAM" });
  }

  let payload = {};
  try { payload = await upstream.json(); } catch { payload = {}; }
  if (!upstream.ok) {
    const code = upstream.status === 401 ? "BAD_KEY" : upstream.status === 429 ? "RATE_LIMIT" : "UPSTREAM";
    return json(request, serverError, { error: "The AI service reported a problem.", code });
  }
  const choice = (payload.choices && payload.choices[0] && (payload.choices[0].message || payload.choices[0].delta)) || {};
  return json(request, ok, {
    content: typeof choice.content === "string" ? choice.content : "",
    thinking: typeof choice.reasoning_content === "string" ? choice.reasoning_content : "",
    model: payload.model || model,
  });
}
