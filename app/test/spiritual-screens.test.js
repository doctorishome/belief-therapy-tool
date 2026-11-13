import assert from "node:assert/strict";
import test from "node:test";
import { deidentifyCase } from "../js/deidentify.js";
import { sealObject } from "../js/vault.js";
import {
  INSTRUMENTS, RSS5_ID, RCOPE_ID, flatItems,
  scoreRss5, scoreBriefRcope, resultCopy, missingPieces, plainSummary,
} from "../js/spiritual-screens.js";

const RSS_ITEMS = [
  "Felt as though God had abandoned me",
  "Felt rejected or misunderstood by religious/spiritual people",
  "Worried that my actions were morally or spiritually wrong",
  "Felt troubled by doubts or questions about spirituality/religion",
  "Questioned whether life really matters",
];

const RCOPE_ITEMS = [
  "Looked for a stronger connection with God.",
  "Sought God\u2019s love and care.",
  "Sought help from God in letting go of my anger.",
  "Tried to put my plans into action together with God.",
  "Tried to see how God might be trying to strengthen me in this situation.",
  "Asked forgiveness for my sins.",
  "Focused on religion to stop worrying about my problems.",
  "Wondered whether God had abandoned me.",
  "Felt punished by God for my lack of devotion.",
  "Wondered what I did for God to punish me.",
  "Questioned God\u2019s love for me.",
  "Wondered whether my church had abandoned me.",
  "Decided the devil made this happen.",
  "Questioned the power of God.",
];

test("RSS-5 items and anchors match the 2025 article", () => {
  const inst = INSTRUMENTS[RSS5_ID];
  assert.deepEqual(flatItems(inst).map((item) => item.text), RSS_ITEMS);
  assert.deepEqual(inst.anchors.map((a) => [a.value, a.label]), [
    [1, "Not at all"],
    [2, "A little bit"],
    [3, "Somewhat"],
    [4, "Quite a bit"],
    [5, "A great deal"],
  ]);
  assert.match(inst.credit, /creativecommons\.org\/licenses\/by\/4\.0/);
  assert.match(inst.credit, /10\.1007\/s10862-024-10182-9/);
  assert.match(inst.credit, /Exline and colleagues \(2014\)/);
  assert.match(inst.intro, /Positive Energy Providence/);
});

test("RSS-5 total is the sum of five items, with no cutoff", () => {
  assert.equal(scoreRss5([1, 1, 1, 1, 1]).total, 5);
  assert.equal(scoreRss5([5, 5, 5, 5, 5]).total, 25);
  const mixed = scoreRss5([1, 2, 3, 4, 5]);
  assert.equal(mixed.total, 15);
  assert.deepEqual(mixed.explore.map((item) => item.domain), ["Moral", "Doubt", "Ultimate meaning"]);
  assert.equal(scoreRss5([1, 2, 3, 4]), null);
  assert.equal(scoreRss5([0, 1, 1, 1, 1]), null);
  const copy = resultCopy(RSS5_ID, [4, 1, 1, 1, 5], "");
  assert.match(copy.lines.join(" "), /No clinical cutoff/);
  assert.match(copy.lines.join(" "), /not a diagnosis/i);
  assert.equal(copy.scores.total, 12);
  assert.equal(copy.explore[0].domain, "Divine");
  assert.equal("combined" in copy.scores, false);
});

test("Brief RCOPE items match Table 2 and the subscales stay separate", () => {
  const inst = INSTRUMENTS[RCOPE_ID];
  assert.deepEqual(flatItems(inst).map((item) => item.text), RCOPE_ITEMS);
  assert.equal(flatItems(inst).length, 14);
  assert.deepEqual(inst.anchors.map((a) => a.value), [0, 1, 2, 3]);
  assert.match(inst.credit, /creativecommons\.org\/licenses\/by\/3\.0/);
  assert.match(inst.credit, /10\.3390\/rel2010051/);
  const scores = scoreBriefRcope([3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 1]);
  assert.equal(scores.positive, 21);
  assert.equal(scores.negative, 1);
  assert.equal("total" in scores, false);
  assert.equal(scoreBriefRcope([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]).positive, 0);
  assert.equal(scoreBriefRcope([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]).negative, 21);
  assert.equal(scoreBriefRcope([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), null);
  assert.equal(scoreBriefRcope([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]), null);
  const copy = resultCopy(RCOPE_ID, [1, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0], "loss of a job");
  assert.equal(copy.scores.positive, 3);
  assert.equal(copy.scores.negative, 3);
  const text = copy.lines.join(" ");
  assert.match(text, /not added into one total/i);
  assert.match(text, /does not give a clinical cutoff/i);
  assert.match(text, /loss of a job/);
  assert.deepEqual(missingPieces(RCOPE_ID, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "  "), [
    "Name the stressor this screen is about.",
  ]);
});

test("saved screens stay in the local record text and the stressor is de-identified", () => {
  const answers = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2];
  const c = {
    name: "Jordan Testcase",
    dob: "1980-04-02",
    presentingConcerns: "",
    assessments: [
      {
        instrument: RSS5_ID,
        completedAt: "2026-11-01T15:00:00.000Z",
        answers: [5, 1, 1, 1, 1],
      },
      {
        instrument: RCOPE_ID,
        completedAt: "2026-11-02T15:00:00.000Z",
        stressor: "argument with Jordan Testcase",
        answers,
      },
    ],
  };
  const { text } = deidentifyCase(c, { now: new Date("2026-11-13T12:00:00Z") });
  assert.equal(text.includes("Jordan"), false);
  assert.match(text, /RSS-5/);
  assert.match(text, /No clinical cutoff/);
  assert.match(text, /Total 9/);
  assert.match(text, /Positive religious coping 7/);
  assert.match(text, /Negative religious coping 2/);
  assert.match(text, /\[CLIENT\]/);
  const summary = plainSummary(c.assessments[1]);
  assert.match(summary, /argument with Jordan Testcase/);
});

test("a saved screen is inside the encrypted vault, not in the ciphertext", async () => {
  const payload = {
    cases: [{
      name: "Alex Example",
      assessments: [{
        instrument: RCOPE_ID,
        stressor: "Alex Example lost the house on Example Street",
        answers: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      }],
    }],
  };
  const sealed = await sealObject("sample-passphrase", payload);
  const raw = JSON.stringify(sealed.envelope);
  assert.equal(raw.includes("Alex Example"), false);
  assert.equal(raw.includes("Example Street"), false);
  assert.equal(raw.includes("lost the house"), false);
});
