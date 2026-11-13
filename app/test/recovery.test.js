import assert from "node:assert/strict";
import test from "node:test";
import { sealV3, openV3, sealObject, generateRecoveryCode, normalizeRecoveryCode } from "../js/vault.js";

// Build the two wraps the same way the vault does, through the public pieces.
async function makeVault(passphrase, obj) {
  // sealV3 needs wraps; create them by round-tripping a tiny helper vault via the module's own wrap format.
  const raw = crypto.getRandomValues(new Uint8Array(32));
  const code = generateRecoveryCode();
  const wrap = async (secret) => {
    const { envelope } = await sealObject(secret, { k: Buffer.from(raw).toString("base64") });
    return { salt: envelope.kdf.salt, iv: envelope.iv, data: envelope.data };
  };
  const wraps = { passphrase: await wrap(passphrase), recovery: await wrap(normalizeRecoveryCode(code)) };
  return { env: await sealV3(raw, wraps, obj), code };
}

test("recovery key looks right and is forgiving about how it is typed", () => {
  const code = generateRecoveryCode();
  assert.match(code, /^([A-HJ-NP-Z2-9]{5}-){4}[A-HJ-NP-Z2-9]{5}$/);
  assert.equal(normalizeRecoveryCode(" " + code.toLowerCase().replace(/-/g, " ") + " "), code.replace(/-/g, ""));
  assert.notEqual(generateRecoveryCode(), code);
});

test("records open with the passphrase or with the recovery key, and with nothing else", async () => {
  const data = { cases: [{ name: "Alex Example", notes: [] }] };
  const { env, code } = await makeVault("correct horse battery", data);
  assert.deepEqual((await openV3("correct horse battery", env)).obj, data);
  assert.deepEqual((await openV3(code, env, "recovery")).obj, data);
  assert.deepEqual((await openV3(code.toLowerCase().replace(/-/g, " "), env, "recovery")).obj, data);
  await assert.rejects(openV3("wrong passphrase", env), { code: "WRONG_PASSWORD" });
  await assert.rejects(openV3(generateRecoveryCode(), env, "recovery"), { code: "WRONG_PASSWORD" });
  await assert.rejects(openV3(code, env, "passphrase"), { code: "WRONG_PASSWORD" });
});

test("the stored envelope holds no readable client name, passphrase or recovery key", async () => {
  const { env, code } = await makeVault("correct horse battery", { cases: [{ name: "Alex Example" }] });
  const text = JSON.stringify(env);
  assert.equal(text.includes("Alex"), false);
  assert.equal(text.includes("correct horse"), false);
  assert.equal(text.includes(code), false);
  assert.equal(text.includes(normalizeRecoveryCode(code)), false);
  assert.equal(env.version, 3);
});
