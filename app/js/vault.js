/**
 * Encrypted case store.
 * PBKDF2 (WebCrypto has no Argon2) derives a key. AES-GCM encrypts the records.
 * Ciphertext lives in IndexedDB on this browser only. The key stays in memory until lock.
 */
import { sampleCases } from "./samples.js";

export const KDF_ITERATIONS = 600_000;
const AAD = new TextEncoder().encode("clinical-companion-web-v1");
const DB = "clinical-companion";
const STORE = "vault";
const session = { key: null, salt: null, data: null };

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
  const env = await sealWithKey(session.key, session.salt, session.data);
  await idbSet("envelope", env);
  return env;
}

export async function createVault(password) {
  if (await vaultExists()) throw new Error("A vault already exists in this browser.");
  const data = { cases: sampleCases(), libraryDocs: [], createdAt: new Date().toISOString() };
  const sealed = await sealObject(password, data);
  await idbSet("envelope", sealed.envelope);
  session.key = sealed.key;
  session.salt = sealed.salt;
  session.data = data;
  return data;
}

export async function unlockVault(password) {
  const env = await idbGet("envelope");
  if (!env) {
    const e = new Error("No records in this browser yet.");
    e.code = "NO_VAULT";
    throw e;
  }
  const opened = await openEnvelope(password, env);
  if (!Array.isArray(opened.obj.cases)) opened.obj.cases = [];
  if (!Array.isArray(opened.obj.libraryDocs)) opened.obj.libraryDocs = [];
  session.key = opened.key;
  session.salt = opened.salt;
  session.data = opened.obj;
  return session.data;
}

export function lockVault() {
  session.key = null;
  session.salt = null;
  session.data = null;
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
  await openEnvelope(oldPw, await idbGet("envelope"));
  const sealed = await sealObject(newPw, session.data);
  await idbSet("envelope", sealed.envelope);
  session.key = sealed.key;
  session.salt = sealed.salt;
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
  const opened = await openEnvelope(password, env);
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
