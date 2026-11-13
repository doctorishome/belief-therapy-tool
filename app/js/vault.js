/**
 * Encrypted case store.
 * The records are encrypted with AES-GCM under a random data key. That data key is itself
 * stored encrypted twice: once under a key derived (PBKDF2; WebCrypto has no Argon2) from the
 * counselor's passphrase, and once under a key derived from a recovery key the counselor prints
 * and keeps. Either one opens the records, so a forgotten passphrase can be reset with the
 * recovery key and nothing is lost. Neither is stored anywhere.
 * Ciphertext lives in IndexedDB on this browser only. The data key stays in memory until lock.
 *
 * Envelope version 3 (this design):
 *   { format, version: 3, cipher, kdf: {alg, hash, iterations},
 *     keys: { passphrase: {salt, iv, data}, recovery: {salt, iv, data} },   // the wrapped data key
 *     iv, data }                                                            // the records
 * Version 2 (before Nov 12, 2026) encrypted the records directly under the passphrase key. A version 2
 * vault is upgraded the first time it is unlocked, and version 2 backups can still be restored.
 */
import { sampleCases } from "./samples.js";

export const KDF_ITERATIONS = 600_000;
const AAD = new TextEncoder().encode("clinical-companion-web-v1");
const DB = "clinical-companion";
const STORE = "vault";
const session = { key: null, raw: null, wraps: null, data: null, pendingCode: null };
const CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";   // 32 symbols, no 0/O or 1/I

function bytesToB64(bytes) {
  let s = "";
  const u = new Uint8Array(bytes);
  for (let i = 0; i < u.length; i++) s += String.fromCharCode(u[i]);
  return btoa(s);
}
function b64ToBytes(b64) {
  const s = atob(b64);
  const u = new Uint8Array(s.length);
  for (let i = 0; i < s.length; i++) u[i] = s.charCodeAt(i);
  return u;
}

async function deriveKey(password, salt, iterations = KDF_ITERATIONS) {
  const base = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(String(password).normalize("NFKC")),
    "PBKDF2",
    false,
    ["deriveKey"]
  );
  return crypto.subtle.deriveKey(
    { name: "PBKDF2", salt, iterations, hash: "SHA-256" },
    base,
    { name: "AES-GCM", length: 256 },
    false,
    ["encrypt", "decrypt"]
  );
}

async function encryptWithKey(key, obj) {
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const plain = new TextEncoder().encode(JSON.stringify(obj));
  const ct = await crypto.subtle.encrypt({ name: "AES-GCM", iv, additionalData: AAD }, key, plain);
  return { iv: bytesToB64(iv), data: bytesToB64(ct) };
}

async function decryptWithKey(key, box) {
  try {
    const plain = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv: b64ToBytes(box.iv), additionalData: AAD },
      key,
      b64ToBytes(box.data)
    );
    return JSON.parse(new TextDecoder().decode(plain));
  } catch {
    const err = new Error("That passphrase did not open these records.");
    err.code = "WRONG_PASSWORD";
    throw err;
  }
}

function envelopeFrom(salt, box) {
  return {
    format: "clinical-companion-vault",
    version: 2,
    kdf: { alg: "PBKDF2", hash: "SHA-256", iterations: KDF_ITERATIONS, salt: bytesToB64(salt) },
    cipher: "AES-GCM",
    ...box,
  };
}

export async function sealObject(password, obj) {
  const salt = crypto.getRandomValues(new Uint8Array(16));
  const key = await deriveKey(password, salt);
  const box = await encryptWithKey(key, obj);
  return { envelope: envelopeFrom(salt, box), key, salt };
}

export async function openEnvelope(password, envelope) {
  if (!envelope || envelope.format !== "clinical-companion-vault") {
    const err = new Error("That file is not a Clinical Companion backup.");
    err.code = "BAD_FILE";
    throw err;
  }
  const salt = b64ToBytes(envelope.kdf.salt);
  const key = await deriveKey(password, salt, envelope.kdf.iterations || KDF_ITERATIONS);
  const obj = await decryptWithKey(key, envelope);
  return { obj, key, salt };
}

export async function sealWithKey(key, salt, obj) {
  return envelopeFrom(salt, await encryptWithKey(key, obj));
}

/** A new recovery key: 25 characters (125 bits), shown as five groups of five. */
export function generateRecoveryCode() {
  const bytes = crypto.getRandomValues(new Uint8Array(25));
  let out = "";
  for (let i = 0; i < 25; i++) {
    out += CODE_ALPHABET[bytes[i] & 31];
    if (i % 5 === 4 && i < 24) out += "-";
  }
  return out;
}
/** Typed recovery keys: ignore case, spaces and dashes. */
export function normalizeRecoveryCode(code) {
  return String(code || "").toUpperCase().replace(/[^A-Z0-9]/g, "");
}

async function importDataKey(raw) {
  return crypto.subtle.importKey("raw", raw, { name: "AES-GCM" }, false, ["encrypt", "decrypt"]);
}
async function wrapDataKey(secret, raw) {
  const salt = crypto.getRandomValues(new Uint8Array(16));
  const box = await encryptWithKey(await deriveKey(secret, salt), { k: bytesToB64(raw) });
  return { salt: bytesToB64(salt), ...box };
}
async function unwrapDataKey(secret, wrap, iterations) {
  const key = await deriveKey(secret, b64ToBytes(wrap.salt), iterations || KDF_ITERATIONS);
  return b64ToBytes((await decryptWithKey(key, wrap)).k);   // throws WRONG_PASSWORD
}
function isV3(env) { return !!env && env.version === 3 && !!env.keys && !!env.keys.passphrase; }

/** Build a version 3 envelope. */
export async function sealV3(raw, wraps, obj) {
  const box = await encryptWithKey(await importDataKey(raw), obj);
  return {
    format: "clinical-companion-vault",
    version: 3,
    kdf: { alg: "PBKDF2", hash: "SHA-256", iterations: KDF_ITERATIONS },
    cipher: "AES-GCM",
    keys: wraps,
    ...box,
  };
}
/** Open a version 3 envelope with the passphrase ("passphrase") or the recovery key ("recovery"). */
export async function openV3(secret, env, which = "passphrase") {
  const wrap = env.keys[which];
  if (!wrap) {
    const e = new Error("These records have no recovery key.");
    e.code = "NO_RECOVERY";
    throw e;
  }
  const raw = await unwrapDataKey(which === "recovery" ? normalizeRecoveryCode(secret) : secret, wrap, env.kdf && env.kdf.iterations);
  const obj = await decryptWithKey(await importDataKey(raw), env);
  return { obj, raw };
}
/** New data key + both wraps for a passphrase. Returns the recovery key so it can be shown once. */
async function freshKeys(password) {
  const raw = crypto.getRandomValues(new Uint8Array(32));
  const code = generateRecoveryCode();
  const wraps = {
    passphrase: await wrapDataKey(password, raw),
    recovery: await wrapDataKey(normalizeRecoveryCode(code), raw),
  };
  return { raw, wraps, code };
}
async function startSession(raw, wraps, data) {
  session.raw = raw;
  session.wraps = wraps;
  session.key = await importDataKey(raw);
  session.data = data;
}

function idb() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB, 1);
    req.onupgradeneeded = () => {
      if (!req.result.objectStoreNames.contains(STORE)) req.result.createObjectStore(STORE);
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}
function idbGet(key) {
  return idb().then((db) => new Promise((resolve, reject) => {
    const r = db.transaction(STORE, "readonly").objectStore(STORE).get(key);
    r.onsuccess = () => resolve(r.result);
    r.onerror = () => reject(r.error);
  }));
}
function idbSet(key, value) {
  return idb().then((db) => new Promise((resolve, reject) => {
    const tx = db.transaction(STORE, "readwrite");
    tx.objectStore(STORE).put(value, key);
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  }));
}

export function isUnlocked() { return !!session.key; }
export async function vaultExists() { return !!(await idbGet("envelope")); }
export function getData() {
  if (!session.key) {
    const e = new Error("Records are locked.");
    e.code = "LOCKED";
    throw e;
  }
  return session.data;
}
async function persist() {
  const env = await sealV3(session.raw, session.wraps, session.data);
  await idbSet("envelope", env);
  return env;
}

/** True when the records in this browser can be opened with a recovery key. */
export async function hasRecoveryKey() {
  const env = await idbGet("envelope");
  return isV3(env) && !!env.keys.recovery;
}
/** The recovery key just created, if the counselor has not been shown it yet. Returns it once. */
export function takeNewRecoveryCode() {
  const code = session.pendingCode;
  session.pendingCode = null;
  return code;
}

export async function createVault(password) {
  if (await vaultExists()) throw new Error("A vault already exists in this browser.");
  const data = { cases: sampleCases(), libraryDocs: [], createdAt: new Date().toISOString() };
  const k = await freshKeys(password);
  await startSession(k.raw, k.wraps, data);
  await persist();
  session.pendingCode = k.code;
  return data;
}

export async function unlockVault(password) {
  const env = await idbGet("envelope");
  if (!env) {
    const e = new Error("No records in this browser yet.");
    e.code = "NO_VAULT";
    throw e;
  }
  let obj, raw, wraps, code = null;
  if (isV3(env)) {
    ({ obj, raw } = await openV3(password, env));
    wraps = env.keys;
  } else {
    // Older records (version 2): open them the old way, then upgrade so they gain a recovery key.
    ({ obj } = await openEnvelope(password, env));
    ({ raw, wraps, code } = await freshKeys(password));
  }
  if (!Array.isArray(obj.cases)) obj.cases = [];
  if (!Array.isArray(obj.libraryDocs)) obj.libraryDocs = [];
  await startSession(raw, wraps, obj);
  if (code) {
    await persist();
    session.pendingCode = code;
  }
  return session.data;
}

/**
 * Forgotten passphrase: open the records with the recovery key and set a new passphrase.
 * Nothing is lost. The old recovery key stops working and a new one is issued (takeNewRecoveryCode).
 */
export async function recoverVault(recoveryCode, newPassword) {
  const env = await idbGet("envelope");
  if (!isV3(env) || !env.keys.recovery) {
    const e = new Error("These records were created before recovery keys existed, so they have none.");
    e.code = "NO_RECOVERY";
    throw e;
  }
  let opened;
  try { opened = await openV3(recoveryCode, env, "recovery"); }
  catch (ex) {
    if (ex.code === "WRONG_PASSWORD") { ex.code = "WRONG_CODE"; ex.message = "That recovery key did not open these records."; }
    throw ex;
  }
  const code = generateRecoveryCode();
  const wraps = {
    passphrase: await wrapDataKey(newPassword, opened.raw),
    recovery: await wrapDataKey(normalizeRecoveryCode(code), opened.raw),
  };
  if (!Array.isArray(opened.obj.cases)) opened.obj.cases = [];
  if (!Array.isArray(opened.obj.libraryDocs)) opened.obj.libraryDocs = [];
  await startSession(opened.raw, wraps, opened.obj);
  await persist();
  session.pendingCode = code;
  return session.data;
}

/** Replace the recovery key (records must be unlocked). The old one stops working. Returns the new key. */
export async function renewRecoveryCode() {
  getData();
  const code = generateRecoveryCode();
  session.wraps = { ...session.wraps, recovery: await wrapDataKey(normalizeRecoveryCode(code), session.raw) };
  await persist();
  return code;
}

/** Forgotten passphrase: erase the encrypted records in this browser so a new passphrase can be created. Cannot be undone. */
export async function eraseVault() {
  lockVault();
  const db = await idb();
  await new Promise((resolve, reject) => {
    const tx = db.transaction(STORE, "readwrite");
    tx.objectStore(STORE).delete("envelope");
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

export function lockVault() {
  session.key = null;
  session.raw = null;
  session.wraps = null;
  session.data = null;
  session.pendingCode = null;
}

export async function saveCase(c) {
  const data = getData();
  const now = new Date().toISOString();
  const clean = { ...c };
  if (!clean.id) {
    clean.id = crypto.randomUUID();
    clean.createdAt = now;
  }
  clean.updatedAt = now;
  const i = data.cases.findIndex((x) => x.id === clean.id);
  if (i >= 0) data.cases[i] = clean;
  else data.cases.push(clean);
  await persist();
  return clean;
}

export async function deleteCase(id) {
  const data = getData();
  data.cases = data.cases.filter((x) => x.id !== id);
  await persist();
}

export async function saveLibraryDocs(docs) {
  getData().libraryDocs = docs;
  await persist();
}

export async function changePassword(oldPw, newPw) {
  getData();
  await openV3(oldPw, await idbGet("envelope"));   // throws WRONG_PASSWORD if the current passphrase is wrong
  session.wraps = { ...session.wraps, passphrase: await wrapDataKey(newPw, session.raw) };
  await persist();                                  // the recovery key keeps working
}

export async function exportEnvelope() {
  getData();
  return persist();
}

export async function restoreEnvelope(fileText, password) {
  getData();
  let env;
  try { env = JSON.parse(fileText); } catch {
    const e = new Error("That file could not be read.");
    e.code = "BAD_FILE";
    throw e;
  }
  if (!env || env.format !== "clinical-companion-vault") {
    const e = new Error("That file is not a Clinical Companion backup.");
    e.code = "BAD_FILE";
    throw e;
  }
  let opened;
  if (isV3(env)) {
    // A newer backup opens with the passphrase or the recovery key in use when it was made.
    try { opened = await openV3(password, env); }
    catch (ex) {
      if (ex.code !== "WRONG_PASSWORD" || !env.keys.recovery) throw ex;
      opened = await openV3(password, env, "recovery");
    }
  } else {
    opened = await openEnvelope(password, env);
  }
  if (!opened.obj || !Array.isArray(opened.obj.cases)) {
    const e = new Error("That backup contains no cases.");
    e.code = "BAD_FILE";
    throw e;
  }
  session.data = {
    cases: opened.obj.cases,
    libraryDocs: Array.isArray(opened.obj.libraryDocs) ? opened.obj.libraryDocs : [],
    createdAt: opened.obj.createdAt || session.data.createdAt,
  };
  await persist();
  return { cases: session.data.cases.length, libraryDocs: session.data.libraryDocs.length };
}
