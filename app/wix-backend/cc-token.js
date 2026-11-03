/**
 * Short-lived membership token shared by the HTTP function and the web method.
 * This is not the xAI key. The key lives only in Wix Secrets.
 *
 * Paste this file into the site Backend folder as cc-token.js.
 */
import { createHmac, timingSafeEqual } from "crypto";
import { Buffer } from "buffer";

const TOKEN_MS = 8 * 60 * 60 * 1000;

function b64url(buf) {
  return Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}
function fromB64url(s) {
  const pad = s.length % 4 === 0 ? "" : "=".repeat(4 - (s.length % 4));
  return Buffer.from(s.replace(/-/g, "+").replace(/_/g, "/") + pad, "base64");
}
function hmac(secret, text) {
  return createHmac("sha256", String(secret)).update(text, "utf8").digest();
}

export async function signMembershipToken(memberId, secret, extras = {}) {
  const payload = JSON.stringify({
    memberId: String(memberId),
    exp: Date.now() + TOKEN_MS,
    staff: !!extras.staff,
  });
  return b64url(Buffer.from(payload, "utf8")) + "." + b64url(hmac(secret, payload));
}

export async function verifyMembershipToken(token, secret) {
  const parts = String(token || "").split(".");
  if (parts.length !== 2) return null;
  let payloadText;
  try { payloadText = fromB64url(parts[0]).toString("utf8"); } catch (e) { return null; }
  const expected = hmac(secret, payloadText);
  let given;
  try { given = fromB64url(parts[1]); } catch (e) { return null; }
  if (given.length !== expected.length || !timingSafeEqual(given, expected)) return null;
  let payload;
  try { payload = JSON.parse(payloadText); } catch (e) { return null; }
  if (!payload || !payload.memberId || typeof payload.exp !== "number" || payload.exp < Date.now()) return null;
  return payload;
}
