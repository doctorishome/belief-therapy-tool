import assert from "node:assert/strict";
import test from "node:test";
import { deidentifyCase, findLeaks } from "../js/deidentify.js";
import { sampleCases } from "../js/samples.js";
import { sealObject, openEnvelope } from "../js/vault.js";
import { prepareChat } from "../js/ai.js";
import { buildMessages } from "../js/prompt.js";
import { CONFIG } from "../config.js";
import { heuristicScope, parseClassifier, costUsd, typicalQuestionEstimate, OFF_TOPIC_DECLINE, MEMBER_MONTHLY_AI_BUDGET_USD, MAIN_MODEL } from "../wix-backend/ai-budget.js";
import { loadStanding } from "../js/standing.js";
import { readFile } from "node:fs/promises";
import { chunkText, searchDocs } from "../js/library.js";
import { mockReply } from "../js/mock.js";
import { friendlyAiError } from "../js/ai.js";
import { signMembershipToken, verifyMembershipToken } from "../wix-backend/cc-token.js";

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
  const standing = await loadStanding();
  const again = await prepareChat({
    caseRecord: c,
    caseText: deid.text,
    history: [{ role: "user", content: "What diagnostic considerations apply?" }],
    useLibrary: false,
    userDocs: [],
    question: "What diagnostic considerations apply?",
  });
  const previewJson = JSON.stringify(prepared.preview);
  assert.equal(previewJson.includes("Sam Fictional"), false);
  assert.equal(previewJson.includes("Prime Directives"), false);
  assert.equal(prepared.messages[0].role, "system");
  assert.equal(prepared.messages[0].content, standing);
  assert.equal(again.messages[0].content, prepared.messages[0].content);
  assert.match(prepared.messages[0].content, /AI assistant inside Clinical Companion/);
  assert.equal(/local AI/i.test(prepared.messages[0].content), false);
  assert.equal((prepared.messages[0].content.match(/13\. Clinical Use Only/g) || []).length, 1);
  assert.ok(prepared.messages[0].content.indexOf("13. Clinical Use Only") < prepared.messages[0].content.indexOf("Closing Note"));
  assert.match(prepared.messages[0].content, /I can only help with clinical and counseling-practice questions/);
  assert.match(prepared.messages[1].content, /DE-IDENTIFIED CASE/);
  assert.equal(prepared.messages[0].content.includes("REFERENCE MATERIAL"), false);
  assert.match(prepared.preview.caseText, /\[CLIENT\]/);
  assert.ok(prepared.preview.standingWords > 10);
  assert.equal(prepared.messages[0].content.includes("maxTokens"), false);
});

test("library passages come after the standing instructions", async () => {
  const standing = await loadStanding();
  const messages = await buildMessages("DE-IDENTIFIED CASE", [], { text: "LIBRARY PASSAGE XYZ", sources: [] });
  assert.equal(messages[0].role, "system");
  assert.equal(messages[0].content, standing);
  assert.equal(messages[0].content.includes("LIBRARY PASSAGE XYZ"), false);
  assert.match(messages[1].content, /LIBRARY PASSAGE XYZ/);
  assert.equal(CONFIG.maxTokens, 3000);
});

test("the APA measures guide is retrieved for a first-session question", async () => {
  const text = await readFile(new URL("../library/apa-adult-measures-guide.md", import.meta.url), "utf8");
  const title = "Free APA DSM-5-TR Assessment Measures for Adults — Guide and Links";
  const chunks = chunkText(title, text);
  const urls = text.match(/https:\/\/www\.psychiatry\.org\/\S+/g) || [];
  assert.ok(urls.length >= 30);
  const joined = chunks.map((c) => c.text).join("\n");
  for (const url of urls) assert.ok(joined.includes(url), "missing url " + url);
  const hits = searchDocs([{ title, text }], "which assessment measures should I give after the first session", 4);
  assert.ok(hits.some((h) => h.title === title));
  assert.match(hits.map((h) => h.text).join("\n"), /https:\/\/www\.psychiatry\.org\//);
});

test("off-topic questions are declined and clinical ones are kept", () => {
  assert.equal(heuristicScope("What's a good lasagna recipe for dinner?"), "OFF_TOPIC");
  assert.equal(heuristicScope("What DSM-5-TR considerations fit this low mood?"), "CLINICAL");
  assert.equal(heuristicScope("Hello there"), "UNSURE");
  assert.equal(heuristicScope("The client mentioned a lasagna recipe in session"), "CLINICAL");
  assert.equal(parseClassifier("maybe CLINICAL"), "CLINICAL");
  assert.equal(parseClassifier("OFF_TOPIC"), "OFF_TOPIC");
  assert.match(OFF_TOPIC_DECLINE, /clinical and counseling-practice/);
});

test("ten dollars covers a few hundred typical questions", () => {
  const estimate = typicalQuestionEstimate();
  assert.equal(MEMBER_MONTHLY_AI_BUDGET_USD, 10);
  assert.ok(estimate.totalUsd > 0.01 && estimate.totalUsd < 0.08);
  assert.ok(estimate.questionsPerBudget >= 150);
  const short = costUsd(MAIN_MODEL, { prompt_tokens: 100_000, completion_tokens: 0, cached_tokens: 0 });
  assert.equal(Math.round(short * 100), 20);
  const long = costUsd(MAIN_MODEL, { prompt_tokens: 1_000_000, completion_tokens: 0, cached_tokens: 0 });
  assert.equal(long, 4);
});

test("a missing membership or a dead proxy gets a plain sentence", () => {
  const room = "Please open Clinical Companion from the Counselors' Room.";
  assert.equal(friendlyAiError({ code: "MEMBER_REQUIRED" }), room);
  assert.equal(friendlyAiError({ code: "NO_NETWORK" }), room);
  assert.equal(/key|xai-/i.test(friendlyAiError({ code: "PROXY" })), false);
});

test("a staff membership token is signed and does not carry case text", async () => {
  const secret = "not-the-api-key";
  const token = await signMembershipToken("site-admin", secret, { staff: true });
  assert.equal(token.includes("Jordan"), false);
  const payload = await verifyMembershipToken(token, secret);
  assert.equal(payload.staff, true);
  assert.equal(await verifyMembershipToken(token, "wrong"), null);
});

test("mock diagnosis and treatment plan are fictional drafts", () => {
  for (const question of ["Diagnostic considerations", "Draft treatment plan"]) {
    const reply = mockReply({ kind: "chat", question, sources: [] });
    assert.match(reply.content, /consider|Treatment plan/i);
    assert.match(reply.content, /\[CLIENT\]/);
    assert.match(reply.content, /Practice mode — draft for the counselor's clinical judgment, not a diagnosis/);
    assert.equal(/HIPAA (approved|certified)/i.test(reply.content), false);
  }
});
