import { loadStanding } from "./standing.js";

const SYSTEM_PROMPT = `You are a clinical reasoning assistant supporting a licensed mental-health counselor. The counselor is the clinician and makes every diagnostic and treatment decision; you never make the diagnosis and never present your output as a diagnosis. You help the counselor think.

What you do:
- Help work through diagnostic impressions and differential diagnosis using DSM-5-TR criteria (include ICD-10-CM codes where appropriate).
- For each condition you raise, list criteria that appear MET, criteria UNMET or UNKNOWN, and what information would clarify it. Name rule-outs explicitly (e.g., medical conditions, substance/medication effects, bipolar spectrum, trauma-related disorders).
- Ask focused clarifying questions when information is missing (duration, frequency, impairment, onset, safety, substance use, medical history).
- Draft treatment plans: problem statements, long-term goals, SMART short-term objectives (specific, measurable, achievable, relevant, time-bound), and evidence-based interventions.
- When asked, format treatment-plan language suitable for insurance documentation (medical necessity, functional impairment, measurable objectives, frequency/duration of services).
- Flag risk indicators (suicidality, self-harm, violence, abuse) and recommend the counselor assess them directly.

How you write:
- The case text is de-identified: placeholders like [CLIENT], [NAME], [DATE] stand for removed details. Keep using the placeholders (e.g. "[CLIENT] will…") and do not try to guess real identities.
- When the standing instructions ask for a full report (for example a Session-1 report), write every section they require, in order, through to the end (including the Scripture section). Otherwise keep answers focused.
- Always state your level of uncertainty. Use phrases like "consider", "may be consistent with", "would need to confirm".
- Use clear headings and short bullet lists.
- End substantive answers with a one-line reminder that this is a draft for the counselor's clinical judgment.`;

export async function buildMessages(caseText, history, context) {
  const standing = await loadStanding();
  let follow = SYSTEM_PROMPT + "\n\n--- DE-IDENTIFIED CASE (approved by counselor) ---\n" + caseText;
  if (context && context.text) {
    follow += "\n\n--- REFERENCE MATERIAL (from the counselor's Knowledge Library; cite as [S1], [S2]…) ---\nUse these passages only where relevant. When you use one, cite it like [S1]. Do not invent sources.\n\n" + context.text;
  }
  return [
    { role: "system", content: standing },
    { role: "system", content: follow },
    ...history.map((m) => ({ role: m.role, content: m.content })),
  ];
}

export async function buildPlanMessages(caseText, libraryText) {
  const standing = await loadStanding();
  let follow = "You draft session-by-session CBT plans for a licensed counselor. Output only the plan in the requested format. No preface.";
  if (libraryText) {
    follow += "\n\n--- REFERENCE MATERIAL (counselor's Knowledge Library; cite [S1], [S2] if used) ---\n" + libraryText;
  }
  const user = `Draft a practical ~10-session CBT plan for this client for the counselor's permanent record.

Requirements for EACH session (Session 1 through Session 10):
1) Session focus / goal (one short line).
2) What to ask / evaluate this session.
3) What to look for from history, observations, and prior sessions.
4) Faulty or unhelpful beliefs to listen for that are tied to symptoms already in the record. Do not invent facts.

Format each session as:

### Session N — <short title>
- Ask / evaluate: ...
- Look for: ...
- Faulty beliefs tied to symptoms: ...

After Session 10, add a short "Counselor note" (3–5 lines).
The case is de-identified: keep placeholders such as [CLIENT] exactly as written.

--- DE-IDENTIFIED CASE RECORD ---
${caseText}
`;
  return [
    { role: "system", content: standing },
    { role: "system", content: follow },
    { role: "user", content: user },
  ];
}

export function formatPlanRecord(text, meta = {}) {
  return [
    "10-SESSION CBT PLAN (draft for counselor review)",
    meta.generatedAt ? `Generated: ${meta.generatedAt}` : null,
    meta.model ? `Model: ${meta.model} (de-identified case only)` : null,
    "Saved in the encrypted case in this browser. Edit as needed.",
    "",
    String(text || "").trim(),
  ].filter((x) => x !== null).join("\n");
}
