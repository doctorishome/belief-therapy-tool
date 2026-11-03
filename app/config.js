/**
 * Clinical Companion (browser) — the one place to change site addresses.
 *
 * The xAI API key does not belong in this file. Live answers go to proxyUrl,
 * and that server holds the key.
 */
export const CONFIG = {
  appName: "Clinical Companion",
  version: "1.2.0-web",

  /**
   * "Back to Counselors" opens this address.
   * counselors/welcome.html in this repo is the Counselors Welcome page.
   * The public site sends counselors to the Counselors' Room, which embeds
   * counselors/welcome.html. If that page address changes, edit only this value.
   */
  counselorsReturnUrl: "https://www.beliefcounselor.com/blank-11",

  /**
   * AI proxy. The xAI key stays on that server. Another proxy can be used by
   * changing this one address. Fictional-cases-only stays on either way.
   */
  proxyUrl: "https://www.beliefcounselor.com/_functions/clinicalCompanion",

  /** "live" calls proxyUrl. "mock" uses canned answers and does not call the proxy. */
  mode: "live",

  /**
   * Keep true until a Business Associate Agreement is signed AND zero data retention
   * is confirmed. The app then stays in fictional-cases-only mode.
   * Counselors cannot turn this off in the screen.
   */
  fictionalOnly: true,

  /** Suggested model name. The proxy may use its own. */
  model: "grok-4.7",
  maxTokens: 4000,
  reasoningEffort: "medium",

  /** Pages allowed to hand the app a short-lived membership token (not an API key). */
  membershipTokenOrigins: ["https://www.beliefcounselor.com", "https://beliefcounselor.com"],
};
