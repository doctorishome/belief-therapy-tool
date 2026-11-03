/**
 * Short-lived membership token shared by the HTTP function and the web method.
 * This is not the xAI key. The key lives only in Wix Secrets.
 *
 * Paste this file into the site Backend folder as cc-token.js.
 */

const TOKEN_MS = 8 * 60 * 60 * 1000;

function bytesToB64Url(bytes) {
  let s = "";
  const u = new Uint8Array(bytes);
  for (let i = 0; i < u.length; i++) s += String.fromCharCode(u[i]);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}
function b64UrlToBytes(s) {
  const pad = s.length % 4 === 0 ? "" : "=".repeat(4 - (s.length % 4));
  const raw = atob(s.replace(/-/g, "+").replace(/_/g, "/") + pad);
  const u = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) u[i] = raw.charCodeAt(i);
  return u;
}
async function hmacKey(secret, usages) {
  return crypto.subtle.importKey("raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, usages);
}

export async function signMembershipToken(memberId, secret, extras = {}) {
  const payload = JSON.stringify({
    memberId: String(memberId),
    exp: Date.now() + TOKEN_MS,
    staff: !!extras.staff,
  });
  const key = await hmacKey(secret, ["sign"]);
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(payload));
  return bytesToB64Url(new TextEncoder().encode(payload)) + "." + bytesToB64Url(sig);
}

export async function verifyMembershipToken(token, secret) {
  const parts = String(token || "").split(".");
  if (parts.length !== 2) return null;
  let payloadText;
  try { payloadText = new TextDecoder().decode(b64UrlToBytes(parts[0])); } catch { return null; }
  const key = await hmacKey(secret, ["verify"]);
  let ok = false;
  try { ok = await crypto.subtle.verify("HMAC", key, b64UrlToBytes(parts[1]), new TextEncoder().encode(payloadText)); }
  catch { return null; }
  if (!ok) return null;
  let payload;
  try { payload = JSON.parse(payloadText); } catch { return null; }
  if (!payload || !payload.memberId || typeof payload.exp !== "number" || payload.exp < Date.now()) return null;
  return payload;
}
