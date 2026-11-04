/**
 * Clinical-only check and monthly cost math. No Wix imports, so tests can run it.
 * Prices are USD per 1,000,000 tokens from https://docs.x.ai/developers/models
 * (read Nov 3, 2026). A prompt at or above longAt tokens is billed entirely at the long rate.
 */

export const MEMBER_MONTHLY_AI_BUDGET_USD = 10;
export const MAX_ANSWER_OUTPUT_TOKENS = 3000;
/** Cheapest general non-reasoning model on that price list. grok-build-0.1 is cheaper but is a code model. */
export const CLASSIFIER_MODEL = "grok-4.20-0309-non-reasoning";
export const CLASSIFIER_MAX_TOKENS = 16;
export const MAIN_MODEL = "grok-4.7";

/** Wix member ids with no monthly cap. Site-owner tokens (staff: true) are also uncapped. */
export const ADMIN_UNLIMITED_MEMBER_IDS = [];

export const OFF_TOPIC_DECLINE = "I can only help with clinical and counseling-practice questions.";
export const BUDGET_MESSAGE = "This month's Clinical Companion allowance has been used. It resets on the 1st.";

export const XAI_PRICES_PER_MILLION = {
  "grok-4.7": { input: 2, cached: 0.5, output: 6, longInput: 4, longCached: 1, longOutput: 12, longAt: 200000 },
  "grok-4.6": { input: 2, cached: 0.5, output: 6, longInput: 4, longCached: 1, longOutput: 12, longAt: 200000 },
  "grok-4.5": { input: 2, cached: 0.3, output: 6, longInput: 4, longCached: 0.6, longOutput: 12, longAt: 200000 },
  "grok-4.3": { input: 1.25, cached: 0.2, output: 2.5, longInput: 2.5, longCached: 0.4, longOutput: 5, longAt: 200000 },
  "grok-4.20-0309-reasoning": { input: 1.25, cached: 0.2, output: 2.5, longInput: 2.5, longCached: 0.4, longOutput: 5, longAt: 200000 },
  "grok-4.20-0309-non-reasoning": { input: 1.25, cached: 0.2, output: 2.5, longInput: 2.5, longCached: 0.4, longOutput: 5, longAt: 200000 },
  "grok-build-0.1": { input: 1, cached: 0.2, output: 2, longInput: 2, longCached: 0.4, longOutput: 4, longAt: 200000 },
};

const CLINICAL_WORDS = /\b(client|patient|diagnos\w*|dsm|icd|treatment|session|therap\w*|counsel\w*|phq|gad-?7|whodas|belief|scripture|suicid\w*|trauma|anxi\w*|depress\w*|symptom\w*|intake|ethic\w*|risk|cpt|cbt|homework|intervention\w*|assessment|measure\w*|insurance|progress note|case|grief|ocd|bipolar|safety)\b/i;
const OFF_TOPIC_WORDS = /\b(recipe|lasagna|cook(?:ing)?|bake|stock price|bitcoin|crypto|nft|nfl|nba|mlb|world cup|super bowl|weather forecast|write (?:me )?a poem|tell me a joke|celebrity|movie review|vacation itinerary|book a flight|best restaurant|python code|javascript tutorial|who won the game)\b/i;

export function heuristicScope(text) {
  const q = String(text || "");
  if (!q.trim()) return "CLINICAL";
  const clinical = CLINICAL_WORDS.test(q);
  const off = OFF_TOPIC_WORDS.test(q);
  if (off && !clinical) return "OFF_TOPIC";
  if (clinical) return "CLINICAL";
  return "UNSURE";
}

export function parseClassifier(text) {
  const t = String(text || "").toUpperCase();
  if (/\bOFF[_\s-]*TOPIC\b/.test(t) && !/\bCLINICAL\b/.test(t)) return "OFF_TOPIC";
  return "CLINICAL";
}

export function latestUserText(messages) {
  const list = Array.isArray(messages) ? messages : [];
  for (let i = list.length - 1; i >= 0; i--) {
    if (list[i] && list[i].role === "user") return String(list[i].content || "").slice(0, 600);
  }
  return "";
}

export function priceRow(model) {
  return XAI_PRICES_PER_MILLION[model] || XAI_PRICES_PER_MILLION[MAIN_MODEL];
}

/** usage: { prompt_tokens, completion_tokens, cached_tokens } */
export function costUsd(model, usage) {
  const row = priceRow(model);
  const prompt = Math.max(0, Number(usage && usage.prompt_tokens) || 0);
  const cached = Math.min(prompt, Math.max(0, Number(usage && usage.cached_tokens) || 0));
  const completion = Math.max(0, Number(usage && usage.completion_tokens) || 0);
  const long = prompt >= row.longAt;
  const inRate = long ? row.longInput : row.input;
  const cacheRate = long ? row.longCached : row.cached;
  const outRate = long ? row.longOutput : row.output;
  const fresh = prompt - cached;
  return (fresh * inRate + cached * cacheRate + completion * outRate) / 1e6;
}

export function estimateUsd(messages, maxTokens, model) {
  const chars = (messages || []).reduce((n, m) => n + String((m && m.content) || "").length, 0);
  return costUsd(model, { prompt_tokens: Math.ceil(chars / 4), completion_tokens: maxTokens, cached_tokens: 0 });
}

export function usageSummary(spentUsd, budgetUsd = MEMBER_MONTHLY_AI_BUDGET_USD) {
  const spent = Math.max(0, Number(spentUsd) || 0);
  const budget = Number(budgetUsd) || MEMBER_MONTHLY_AI_BUDGET_USD;
  const percent = budget <= 0 ? 100 : Math.min(100, Math.round((spent / budget) * 100));
  return { spentUsd: Math.round(spent * 10000) / 10000, budgetUsd: budget, percent };
}

export function typicalQuestionEstimate() {
  const main = costUsd(MAIN_MODEL, { prompt_tokens: 6000, completion_tokens: 1200, cached_tokens: 0 });
  const classify = costUsd(CLASSIFIER_MODEL, { prompt_tokens: 250, completion_tokens: 8, cached_tokens: 0 });
  const total = main + classify;
  return {
    inputTokens: 6000,
    outputTokens: 1200,
    mainUsd: main,
    classifyUsd: classify,
    totalUsd: total,
    questionsPerBudget: Math.floor(MEMBER_MONTHLY_AI_BUDGET_USD / total),
  };
}

export function isBudgetExempt(memberId, staff) {
  if (staff) return true;
  return ADMIN_UNLIMITED_MEMBER_IDS.includes(String(memberId || ""));
}

export function monthKey(date = new Date()) {
  try {
    const parts = new Intl.DateTimeFormat("en-CA", { timeZone: "America/New_York", year: "numeric", month: "2-digit" }).format(date);
    return String(parts).slice(0, 7);
  } catch {
    return date.toISOString().slice(0, 7);
  }
}
