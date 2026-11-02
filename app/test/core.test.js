import assert from "node:assert/strict";
import test from "node:test";
import { deidentifyCase, findLeaks } from "../js/deidentify.js";
import { sampleCases } from "../js/samples.js";
import { sealObject, openEnvelope } from "../js/vault.js";
import { prepareChat } from "../js/ai.js";
import { standingText } from "../js/standing.js";
import { mockReply } from "../js/mock.js";

test("sample case is de-identified before preview", () => {
  const c = sampleCases()[0];
  const { text, counts } = deidentifyCase(c);
  assert.match(text, /\[CLIENT\]/);
  assert.equal(text.includes("Jordan"), false);
  assert.equal(text.includes("Testcase"), false);
  assert.equal(text.includes("555"), false);
  assert.equal(text.includes("example.com"), false);
  assert.equal(text.includes("Example Street"), false);
  assert.ok(counts["client name"] > 0);
  assert.equal(findLeaks(text, c).length, 0);
});

test("vault ciphertext does not contain the client name", async () => {
  const secret = "sample-passphrase";
  const payload = { cases: [{ name: "Alex Example", phone: "(555) 010-9999", email: "alex.example@example.com", notes: [] }] };
  const sealed = await sealObject(secret, payload);
  const raw = JSON.stringify(sealed.envelope);
  assert.equal(raw.includes("Alex Example"), false);
  assert.equal(raw.includes("alex.example@example.com"), false);
  assert.equal(sealed.envelope.cipher, "AES-GCM");
  assert.equal(sealed.envelope.kdf.alg, "PBKDF2");
  const opened = await openEnvelope(secret, sealed.envelope);
  assert.equal(opened.obj.cases[0].name, "Alex Example");
  await assert.rejects(() => openEnvelope("wrong-passphrase", sealed.envelope), (err) => err.code === "WRONG_PASSWORD");
});

test("send preview shows the case text and hides standing instructions", async () => {
  const c = sampleCases()[1];
  const deid = deidentifyCase(c);
  const prepared = await prepareChat({
    caseRecord: c,
    caseText: deid.text,
    history: [{ role: "user", content: "What diagnostic considerations apply?" }],
    useLibrary: false,
    userDocs: [],
    question: "What diagnostic considerations apply?",
  });
  const previewJson = JSON.stringify(prepared.preview);
  assert.equal(previewJson.includes("Sam Fictional"), false);
  assert.equal(previewJson.includes(standingText().slice(0, 40)), false);
  assert.match(prepared.messages[0].content, /STANDING INSTRUCTIONS/);
  assert.match(prepared.preview.caseText, /\[CLIENT\]/);
  assert.ok(prepared.preview.standingWords > 10);
});

test("mock diagnosis and treatment plan are fictional drafts", () => {
  for (const question of ["Diagnostic considerations", "Draft treatment plan"]) {
    const reply = mockReply({ kind: "chat", question, sources: [] });
    assert.match(reply.content, /consider|Treatment plan/i);
    assert.match(reply.content, /\[CLIENT\]/);
    assert.match(reply.content, /Fictional-cases practice only/);
    assert.equal(/HIPAA (approved|certified)/i.test(reply.content), false);
  }
});
