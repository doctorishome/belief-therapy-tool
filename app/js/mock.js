/**
 * Canned answers so the whole screen can be tried with no server and no API key.
 * Every answer is a fictional draft and keeps [CLIENT] placeholders.
 */

const CLOSE = "\n\nPractice mode — draft for the counselor's clinical judgment, not a diagnosis.";

function sourcesLine(sources) {
  if (!sources || !sources.length) return "";
  return "\n\nLibrary passages that fit this question (practice search on this computer):\n" +
    sources.map((s) => `- [${s.n}] ${s.title}${s.loc ? " — " + s.loc : ""}`).join("\n");
}

const DIAGNOSTIC = `## Diagnostic considerations (draft)

These are considerations for you to weigh, not a diagnosis. Use only what the de-identified record actually says about [CLIENT].

### Depressive disorders — consider when low mood, lost interest, or poor sleep is described
- MET: only the symptoms, duration, and impairment written in the record.
- UNMET or UNKNOWN: appetite, energy, “most of the day, nearly every day,” and a current PHQ-9 unless the record already has them.
- Ask next: how long, how many days a week, effect on work or relationships, and a direct safety check.
- A moderate recurrent episode is often coded F33.1 when a prior episode is documented. Do not assign that code unless the history supports it.

### Anxiety disorders — consider when worry or body tension is described
- Broad, hard-to-control worry across several areas suggests generalized anxiety (F41.1).
- Sudden peaks with fear of dying or losing control suggest panic, which is a different question.
- Intrusive thoughts plus neutralizing rituals (confession, checking, avoidance) suggest OCD, including religious scrupulosity, rather than ordinary worry.
- Rule out a medical cause, substance or medication effects, and a bipolar spectrum history. Ask once, directly, about high-energy periods.

### Grief
If the record describes a death, keep ordinary grief in view. A depressive disorder is a consideration when symptoms, impairment, and time course go beyond what you judge to be grief for this person. Do not collapse the two.

### Safety
Re-ask about suicidal intent, self-harm, violence, and abuse. A note that says “denies SI” is not a substitute for your own check today.

### Beliefs
Listen for faulty beliefs the person has actually said (worthlessness with depression, catastrophic prediction with anxiety, “thinking it is as bad as doing it” with scrupulosity, “God is punishing me” with guilt). Do not invent a belief that is not in the record.`;

const DIFFERENTIAL = `## Differential (draft)

Rank only from the de-identified record. Certainty stays low until you have duration, impairment, a safety check, and a medical review.

- A depressive episode rises when low mood, lost interest, and sleep or concentration problems travel together.
- An anxiety disorder rises when worry or body tension is the main thread, especially if it is broader than one situation.
- OCD rises when there are intrusions plus rituals or avoidance. Scrupulosity is that pattern in religious or moral dress.
- Grief stays primary when the pain is about a death and functioning is mostly intact. Depression joins it only if you see a syndrome, not only sadness.
- Always leave room for a medical contributor, substance or medication effects, and bipolar spectrum until you have asked.

What would change the ranking: a repeated scale score, a clear time course, and one belief quoted in the client’s own words.`;

const TREATMENT = `## Treatment plan (draft)

### Problems
1. The symptoms named in the de-identified record (mood, anxiety, grief, or rituals — only those that are actually written).
2. Any faulty belief the record already quotes. If none is quoted, the first task is to listen for one, not to supply one.

### Long-term goals
- [CLIENT] can do the ordinary tasks of the week (sleep, work or study, one relationship) without the symptom running the day.
- [CLIENT] can state a truer sentence in place of the faulty belief, in their own words.

### Short-term objectives (about 12 weeks)
- A repeated scale (PHQ-9, GAD-7, or the measure you already use) moves in the direction you and [CLIENT] set.
- One behavioral step on most days (a walk, a meal, a service, or a chosen exposure).
- One written belief, the evidence for and against it, and a replacement sentence, by week 4 — only for a belief [CLIENT] has said.

### Interventions
- CBT matched to the leading consideration: behavioral activation for depression, worry skills for anxiety, ERP-informed work for rituals, grief support when a death is the story.
- A brief medical rule-out if none is documented.
- Safety check each session.
- Scripture only if [CLIENT] wants faith in the work. Do not assign a verse they have not welcomed.

Mark anything you still need to confirm. Do not invent medicines, family history, or trauma.`;

const INSURANCE = `## Insurance-style wording (draft)

Practice language for a fictional case. It is not a claim and not a bill.

- Working consideration: use only the counselor’s own wording and ICD-10-CM code from the record. This draft does not choose a final diagnosis.
- Medical necessity: symptoms, duration, and functional impairment as written (work, sleep, relationships, worship, or study).
- Objectives: measurable, time-bounded, and tied to those impairments.
- Interventions: CBT (and ERP when rituals are present), about weekly, often about 10 sessions, then review.
- Discharge: goals met, a step down when function is stable, or a referral if risk or a medical issue needs another setting.

Confirm every code and date against your own record before anyone else sees it.`;

const REPORT = `## Session report (draft)

**Fictional case. Placeholders only.**

### What the record supports
Summarize only the de-identified facts: presenting concerns, the history that is written, the latest note, and any scale score that is actually recorded. Do not add events.

### Impression for your review
State the leading consideration and one rule-out, with uncertainty. You decide.

### If you are writing this session up
- Interventions you actually used.
- [CLIENT]’s response, in the words of the note.
- Homework that was agreed.
- Risk: your own assessment today, not a sentence copied from an old note.

### Scripture
Only if [CLIENT] wants faith included. A passage often used when the mind is being renewed is Romans 12:2. Do not assign it unless it fits the person in the room.`;

const PLAN = `### Session 1 — Map symptoms and safety
- Ask / evaluate: mood, sleep, worry, rituals, grief, and a direct safety check.
- Look for: duration, impairment, and what the record already quotes.
- Faulty beliefs tied to symptoms: only a sentence [CLIENT] has said.

### Session 2 — One behavioral step
- Ask / evaluate: what stopped, and one small step to resume.
- Look for: avoidance versus low energy.
- Faulty beliefs tied to symptoms: “If I rest, I am failing,” only if [CLIENT] says something like it.

### Session 3 — The body of the symptom
- Ask / evaluate: sleep, appetite, chest tightness, or the urge to ritualize.
- Look for: a medical question that is still open.
- Faulty beliefs tied to symptoms: “If I feel it, it is true.”

### Session 4 — Name one belief
- Ask / evaluate: the exact sentence that shows up with the symptom.
- Look for: all-or-nothing or punishment wording already in the notes.
- Faulty beliefs tied to symptoms: quote [CLIENT]; do not invent.

### Session 5 — Evidence
- Ask / evaluate: facts that fit the belief and facts that do not.
- Look for: one past event that did not match the belief.
- Faulty beliefs tied to symptoms: one error, one thought, or one tragedy means “I am condemned.”

### Session 6 — A truer statement
- Ask / evaluate: a sentence [CLIENT] can actually say.
- Look for: whether faith language is welcome.
- Faulty beliefs tied to symptoms: “I must earn the right to be all right.”

### Session 7 — Worry, ritual, or grief skill
- Ask / evaluate: which loop has a next action, and which is a ritual or a wave of grief.
- Look for: reassurance seeking or repeated confession.
- Faulty beliefs tied to symptoms: “If I stop the ritual, something terrible is my fault.”

### Session 8 — A real-life experiment
- Ask / evaluate: one situation to approach differently, then debrief.
- Look for: avoidance of work, church, or people.
- Faulty beliefs tied to symptoms: “They will see that I do not belong.”

### Session 9 — Early warning signs
- Ask / evaluate: sleep, withdrawal, the old sentence.
- Look for: who already notices a change.
- Faulty beliefs tied to symptoms: “A dip means I am back at zero.”

### Session 10 — Review
- Ask / evaluate: scores, one belief that loosened, and whether more care is needed.
- Look for: unfinished medical questions or rising risk.
- Faulty beliefs tied to symptoms: “I should be finished forever.”

### Counselor note
- If safety changes, leave the outline and assess directly.
- If the leading picture changes (depression, anxiety, OCD, grief), change the skill, not just the title.
- Keep every belief tied to something [CLIENT] said.
- This outline is a draft for a fictional record.`;

export function mockReply({ kind, question, sources }) {
  const q = String(question || "").toLowerCase();
  let body;
  if (kind === "plan" || /10-session|plan 10 sessions/.test(q)) body = PLAN;
  else if (/insurance/.test(q)) body = INSURANCE;
  else if (/session report|progress note/.test(q)) body = REPORT;
  else if (/treatment plan/.test(q)) body = TREATMENT;
  else if (/differential/.test(q)) body = DIFFERENTIAL;
  else body = DIAGNOSTIC;
  return { content: body + sourcesLine(sources) + CLOSE, model: "mock-fictional", mock: true };
}
