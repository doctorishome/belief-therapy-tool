import { plainSummary } from "./spiritual-screens.js";

// De-identification of a case record. Same rules as Clinical Companion 1.2.0-beta.
// (1) drop direct-identifier fields; (2) replace literal identifiers in free text;
// (3) regex-scrub remaining phones, emails, dates, SSN-like numbers, long IDs,
// street addresses, ZIP codes, URLs, and titled names.

const MONTHS = "Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?";
const NAME_STOP = new Set(["de", "la", "le", "van", "von", "der", "da", "del", "di", "du", "st", "jr", "sr", "ii", "iii", "iv", "mr", "mrs", "ms", "dr", "the", "and"]);

function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
function literalRe(term) {
  const body = escapeRe(term.trim()).replace(/\s+/g, "\\s+");
  return new RegExp("(?<![\\p{L}\\p{N}])" + body + "(?![\\p{L}\\p{N}])", "giu");
}
function splitList(s) {
  return String(s || "").split(/[\n,;]+/).map((x) => x.trim()).filter(Boolean);
}
function nameTokens(full) {
  return String(full || "").replace(/[()"]/g, " ").split(/[\s]+/)
    .map((t) => t.replace(/^[^\p{L}]+|[^\p{L}'-]+$/gu, ""))
    .filter((t) => t.length >= 2 && !NAME_STOP.has(t.toLowerCase()));
}
function pad(n) { return String(n).padStart(2, "0"); }
function dobVariants(dob) {
  const m = /^(\d{4})-(\d{1,2})-(\d{1,2})/.exec(String(dob || ""));
  if (!m) return dob ? [String(dob)] : [];
  const [, y, mo, d] = m;
  const M = +mo, D = +d;
  const names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const mn = names[M - 1] || "";
  const v = [`${y}-${pad(M)}-${pad(D)}`, `${pad(M)}/${pad(D)}/${y}`, `${M}/${D}/${y}`, `${pad(M)}-${pad(D)}-${y}`, `${M}-${D}-${y}`,
    `${pad(D)}/${pad(M)}/${y}`, `${D}/${M}/${y}`, `${pad(M)}/${pad(D)}/${y.slice(2)}`, `${M}/${D}/${y.slice(2)}`, `${pad(M)}.${pad(D)}.${y}`];
  if (mn) v.push(`${mn} ${D}, ${y}`, `${mn} ${D} ${y}`, `${D} ${mn} ${y}`, `${mn.slice(0, 3)} ${D}, ${y}`, `${D} ${mn.slice(0, 3)} ${y}`);
  return v;
}
export function ageFrom(dob, now = new Date()) {
  const m = /^(\d{4})-(\d{1,2})-(\d{1,2})/.exec(String(dob || ""));
  if (!m) return null;
  const b = new Date(+m[1], +m[2] - 1, +m[3]);
  let age = now.getFullYear() - b.getFullYear();
  const md = now.getMonth() - b.getMonth();
  if (md < 0 || (md === 0 && now.getDate() < b.getDate())) age--;
  if (age < 0 || age > 130) return null;
  return age >= 90 ? "90 or older" : String(age);
}
export function relativeDate(dateStr, now = new Date()) {
  const m = /^(\d{4})-(\d{1,2})-(\d{1,2})/.exec(String(dateStr || ""));
  if (!m) return "[DATE]";
  const d = new Date(+m[1], +m[2] - 1, +m[3]);
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const days = Math.round((today - d) / 86400000);
  if (days === 0) return "today";
  if (days < 0) { const f = -days; return f < 14 ? `in ${f} day${f === 1 ? "" : "s"}` : `in about ${Math.round(f / 7)} weeks`; }
  if (days === 1) return "1 day ago";
  if (days < 14) return `${days} days ago`;
  if (days < 60) return `${Math.round(days / 7)} weeks ago`;
  if (days < 730) return `about ${Math.round(days / 30.44)} months ago`;
  return `about ${Math.round(days / 365.25)} years ago`;
}

export function literalIdentifiers(c) {
  const out = [];
  const add = (term, tag, type) => {
    term = String(term || "").trim().replace(/[.,;:!?]+$/, "");
    if (term.length >= 2) out.push({ term, tag, type });
  };
  add(c.name, "[CLIENT]", "client name");
  nameTokens(c.name).forEach((t) => add(t, "[CLIENT]", "client name"));
  splitList(c.preferredName).forEach((n) => { add(n, "[CLIENT]", "client name"); nameTokens(n).forEach((t) => add(t, "[CLIENT]", "client name")); });
  add(c.email, "[EMAIL]", "email");
  add(c.phone, "[PHONE]", "phone");
  add(c.clientId, "[ID]", "ID number");
  add(c.insuranceNumber, "[ID]", "insurance number");
  const ins = c.insurance || {};
  for (const nm of [ins.insuredName, ins.otherInsuredName]) {
    add(nm, "[NAME]", "insured name");
    nameTokens(nm).forEach((t) => add(t, "[NAME]", "insured name"));
  }
  for (const [v, type] of [[ins.groupNumber, "group number"], [ins.priorAuth, "authorization number"], [ins.otherPolicy, "policy number"]]) {
    if (String(v || "").trim().length >= 4) add(v, "[ID]", type);
  }
  add(ins.insuredPhone, "[PHONE]", "phone");
  if (ins.insuredAddress) {
    add(ins.insuredAddress, "[ADDRESS]", "address");
    splitList(ins.insuredAddress).forEach((part) => { if (part.length >= 4 && !/^[A-Z]{2}\s*\d{0,5}$/.test(part)) add(part, "[ADDRESS]", "address"); });
  }
  dobVariants(ins.insuredDob).forEach((v) => add(v, "[DOB]", "date of birth"));
  if (c.address) {
    add(c.address, "[ADDRESS]", "address");
    splitList(c.address).forEach((part) => { if (part.length >= 4 && !/^[A-Z]{2}\s*\d{0,5}$/.test(part)) add(part, "[ADDRESS]", "address"); });
  }
  dobVariants(c.dob).forEach((v) => add(v, "[DOB]", "date of birth"));
  const seen = new Set();
  return out.filter((x) => { const k = x.term.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; })
    .sort((a, b) => b.term.length - a.term.length);
}

const PATTERNS = [
  { type: "email", tag: "[EMAIL]", re: /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi },
  { type: "url", tag: "[URL]", re: /\bhttps?:\/\/[^\s)]+|\bwww\.[^\s)]+/gi },
  { type: "SSN-like number", tag: "[SSN]", re: /\b\d{3}[-\s]\d{2}[-\s]\d{4}\b/g },
  { type: "phone", tag: "[PHONE]", re: /(?:\+?1[\s.-]?)?(?:\(\d{3}\)\s?|\b\d{3}[\s.-])\d{3}[\s.-]\d{4}\b|\b\d{10}\b/g },
  { type: "date", tag: "[DATE]", re: /\b\d{4}-\d{1,2}-\d{1,2}\b/g },
  { type: "date", tag: "[DATE]", re: /\b\d{1,2}[\/.-]\d{1,2}[\/.-](?:\d{4}|\d{2})\b/g },
  { type: "date", tag: "[DATE]", re: new RegExp("\\b(?:" + MONTHS + ")\\.?\\s+\\d{1,2}(?:st|nd|rd|th)?,?\\s+\\d{4}\\b", "g") },
  { type: "date", tag: "[DATE]", re: new RegExp("\\b\\d{1,2}(?:st|nd|rd|th)?\\s+(?:of\\s+)?(?:" + MONTHS + ")\\.?,?\\s+\\d{4}\\b", "g") },
  { type: "date", tag: "[DATE]", re: new RegExp("\\b(?:" + MONTHS + ")\\.?\\s+\\d{1,2}(?:st|nd|rd|th)?\\b", "g") },
  { type: "date", tag: "[DATE]", re: new RegExp("\\b\\d{1,2}(?:st|nd|rd|th)?\\s+(?:of\\s+)?(?:" + MONTHS + ")\\b", "g") },
  { type: "street address", tag: "[ADDRESS]", re: /\b\d{1,6}\s+(?:[A-Z][\w'-]*\s+){1,4}(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Way|Place|Pl|Terrace|Ter|Circle|Cir|Highway|Hwy|Parkway|Pkwy)\b\.?(?:,?\s*(?:Apt|Apartment|Unit|Suite|Ste|#)\.?\s*[\w-]+)?/g },
  { type: "apartment/unit", tag: "[ADDRESS]", re: /\b(?:Apt|Apartment|Unit|Suite|Ste)\.?\s*#?\s*\d+[A-Z]?\b/g },
  { type: "titled name", tag: "$1 [NAME]", re: /\b((?:Mr|Mrs|Ms|Miss|Mx|Dr)\.?)\s+[A-Z][a-z'-]+(?:\s+[A-Z][a-z'-]+)?/g },
  { type: "ID number", tag: "[ID]", re: /\b(?=[A-Za-z0-9-]*\d)[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\b/g, filter: (m) => (m.match(/\d/g) || []).length >= 6 },
  { type: "ZIP code", tag: "[ZIP]", re: /\b\d{5}(?:-\d{4})?\b/g },
];

export function scrubText(text, literals, counts) {
  let s = String(text || "");
  const bump = (t, n = 1) => { counts[t] = (counts[t] || 0) + n; };
  for (const L of literals) {
    s = s.replace(literalRe(L.term), () => { bump(L.type); return L.tag; });
    if (L.type === "phone") {
      const digits = L.term.replace(/\D/g, "");
      if (digits.length >= 7) {
        const flex = digits.split("").join("[\\s().-]*");
        s = s.replace(new RegExp("(?<!\\d)" + flex + "(?!\\d)", "g"), () => { bump("phone"); return "[PHONE]"; });
      }
    }
  }
  for (const P of PATTERNS) {
    s = s.replace(P.re, (m, g1) => {
      if (P.filter && !P.filter(m)) return m;
      bump(P.type);
      return P.tag.replace("$1", g1 || "");
    });
  }
  return s;
}

export function deidentifyCase(c, opts = {}) {
  const now = opts.now || new Date();
  const literals = literalIdentifiers(c);
  const counts = {};
  const S = (t) => scrubText(t, literals, counts).trim();
  const lines = ["DE-IDENTIFIED CASE SUMMARY", "Client: [CLIENT]"];
  const age = ageFrom(c.dob, now);
  if (age) lines.push("Age: " + age);
  if (c.dob) counts["date of birth"] = (counts["date of birth"] || 0) + 1;
  const FL = { phone: "phone field", email: "email field", address: "address field", clientId: "client ID field", insuranceNumber: "insurance # field" };
  for (const f of Object.keys(FL)) if (c[f]) counts["removed field: " + FL[f]] = 1;
  const section = (label, v) => { const t = S(v); if (t) { lines.push(""); lines.push(label + ":"); lines.push(t); } };
  section("Presenting concerns", c.presentingConcerns);
  section("Relevant history", c.history);
  section("Counselor's working diagnoses", c.workingDiagnoses);
  section("Confirmed diagnoses", c.confirmedDiagnoses);
  section("Current treatment plan", c.treatmentPlan);
  const screens = (Array.isArray(c.assessments) ? c.assessments : [])
    .map((a) => ({ when: String(a.completedAt || "").slice(0, 10), text: plainSummary(a) }))
    .filter((a) => a.text);
  if (screens.length) {
    lines.push("");
    lines.push("Spiritual assessment screens (saved in this local record):");
    screens
      .slice()
      .sort((a, b) => a.when.localeCompare(b.when))
      .forEach((a) => lines.push(`- Screen ${relativeDate(a.when, now)}: ${S(a.text)}`));
  }
  const notes = (c.notes || []).filter((n) => (n.text || "").trim()).slice().sort((a, b) => String(a.date).localeCompare(String(b.date)));
  if (notes.length) {
    lines.push("");
    lines.push("Session notes (oldest first):");
    notes.forEach((n) => lines.push(`- Session ${relativeDate(n.date, now)}: ${S(n.text)}`));
  }
  if (c.sessionPlan && String(c.sessionPlan).trim()) section("10-session plan", c.sessionPlan);
  return { text: lines.join("\n"), counts };
}

export function findLeaks(text, c) {
  const leaks = new Set();
  for (const L of literalIdentifiers(c)) if (literalRe(L.term).test(text)) leaks.add(L.term);
  for (const P of PATTERNS) {
    if (P.type === "titled name") continue;
    const re = new RegExp(P.re.source, P.re.flags);
    let m;
    while ((m = re.exec(text))) { if (!P.filter || P.filter(m[0])) leaks.add(m[0]); }
  }
  return [...leaks];
}
