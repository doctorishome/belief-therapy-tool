import { CONFIG } from "../config.js";
import { esc, render as renderMd, toPlain } from "./md.js";
import { findLeaks } from "./deidentify.js";
import * as vault from "./vault.js";
import { sampleCases } from "./samples.js";
import { deidentify, prepareChat, preparePlan, complete, isMock, rememberMembershipToken } from "./ai.js";
import { formatPlanRecord } from "./prompt.js";
import { loadCatalog, loadBundledDoc } from "./library.js";
import {
  INSTRUMENTS, RSS5_ID, RCOPE_ID, instrumentById, flatItems, anchorLabel,
  scoreInstrument, missingPieces, resultCopy,
} from "./spiritual-screens.js";

const $ = (s) => document.querySelector(s);
const FIELDS = ["name", "preferredName", "dob", "phone", "email", "clientId", "address", "presentingConcerns", "history", "workingDiagnoses", "confirmedDiagnoses", "treatmentPlan", "sessionPlan"];
const QUICK = {
  "Diagnostic considerations": "Based on the case, what diagnostic considerations (DSM-5-TR) should I think about? For each, list criteria that appear met, criteria unmet or unknown, and what I should ask or assess next.",
  "Differential diagnosis": "Walk me through a differential diagnosis for this case. Include rule-outs (medical, substance or medication, other mental disorders), what distinguishes each, and how certain each consideration is.",
  "Draft treatment plan": "Draft a treatment plan for this case: problem statements, long-term goals, SMART short-term objectives, and evidence-based interventions. Mark anything that depends on information I still need to confirm.",
  "Format for insurance": "Format the current treatment plan in language suitable for insurance documentation: the counselor's working diagnosis with ICD-10-CM code, medical necessity, functional impairment, measurable objectives, interventions, frequency and duration, and discharge criteria.",
  "Session report": "Draft a session report from this de-identified record: what the record supports, a clinical impression for my review, interventions and response, risk, and a Scripture note only if the record shows the client wants faith included.",
};

const state = {
  view: "",
  cases: [],
  currentId: null,
  editing: null,
  editNotes: [],
  editDirty: false,
  session: null,
  prefs: loadPrefs(),
  returnView: "home",
  screen: null,
  screenDirty: false,
};

function loadPrefs() {
  const defaults = { autoLockMin: 15, speech: false, useLibrary: true };
  try { return { ...defaults, ...JSON.parse(localStorage.getItem("cc-prefs") || "{}") }; }
  catch { return defaults; }
}
function savePrefs(p) {
  state.prefs = { ...state.prefs, ...p };
  localStorage.setItem("cc-prefs", JSON.stringify(state.prefs));
}

function show(name) {
  const prev = state.view;
  document.querySelectorAll(".view").forEach((v) => { v.hidden = true; });
  const el = $("#view-" + name);
  if (el) el.hidden = false;
  $("#topbar").hidden = name === "setup" || name === "unlock";
  state.view = name;
  if ((name === "settings" || name === "privacy") && prev && prev !== "settings" && prev !== "privacy") {
    state.returnView = prev;
  }
}

let toastTimer = null;
function toast(msg) {
  $("#toast-msg").textContent = msg;
  $("#toast").hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { $("#toast").hidden = true; }, 4200);
}

function modal({ title, html, okLabel = "OK", cancelLabel = "Cancel", danger = false }) {
  return new Promise((resolve) => {
    $("#modal-title").textContent = title;
    $("#modal-body").innerHTML = html;
    $("#modal-ok").textContent = okLabel;
    $("#modal-ok").className = "btn " + (danger ? "danger" : "primary");
    $("#modal").classList.toggle("danger", danger);
    const cancel = $("#modal-cancel");
    cancel.hidden = cancelLabel == null;
    cancel.textContent = cancelLabel || "Cancel";
    $("#modal-backdrop").hidden = false;
    const finish = (val) => {
      $("#modal-backdrop").hidden = true;
      $("#modal-ok").onclick = null;
      cancel.onclick = null;
      document.removeEventListener("keydown", onKey);
      resolve(val);
    };
    const onKey = (e) => { if (e.key === "Escape") finish(false); };
    document.addEventListener("keydown", onKey);
    $("#modal-ok").onclick = () => finish(true);
    cancel.onclick = () => finish(false);
    $("#modal-ok").focus();
  });
}

function confirmBox(title, text, okLabel, danger) {
  return modal({ title, html: `<p>${esc(text)}</p>`, okLabel, cancelLabel: "Cancel", danger });
}

function goCounselors() { location.href = CONFIG.counselorsReturnUrl; }
function goBack() {
  const dest = state.returnView;
  if (dest === "case" && state.currentId) openCase(state.currentId);
  else if (dest === "library") renderLibrary().catch((e) => toast(e.message));
  else if (dest === "forms") renderForms();
  else if (dest === "screen" && state.currentId) openCase(state.currentId);
  else showHome();
}

function ageLine(dob) {
  const m = /^(\d{4})-(\d{1,2})-(\d{1,2})/.exec(String(dob || ""));
  if (!m) return "";
  const b = new Date(+m[1], +m[2] - 1, +m[3]);
  let age = new Date().getFullYear() - b.getFullYear();
  const md = new Date().getMonth() - b.getMonth();
  if (md < 0 || (md === 0 && new Date().getDate() < b.getDate())) age--;
  if (age < 0 || age > 130) return "";
  return String(age);
}
function caseById(id) { return state.cases.find((c) => c.id === id); }

function showHome() {
  endSession(true);
  renderHome();
  show("home");
}

function renderHome() {
  const q = ($("#search").value || "").trim().toLowerCase();
  const list = state.cases
    .filter((c) => !q || (c.name + " " + (c.presentingConcerns || "")).toLowerCase().includes(q))
    .slice()
    .sort((a, b) => String(b.updatedAt || "").localeCompare(String(a.updatedAt || "")));
  $("#home-mode").textContent = isMock()
    ? "Mock mode: canned answers stay in this browser. Nothing is sent to an AI service."
    : "Live mode: each request is previewed, then sent only to the configured proxy.";
  const box = $("#case-list");
  if (!list.length) {
    box.innerHTML = `<div class="empty">${state.cases.length ? "No cases match that search." : "No cases yet."}</div>`;
    return;
  }
  box.innerHTML = list.map((c) => `
    <button class="case-card" type="button" data-id="${esc(c.id)}">
      <h3>${esc(c.name || "Untitled")}${c.sample ? ' <span class="badge sample">Fictional</span>' : ""}</h3>
      <div class="concerns">${esc(c.presentingConcerns || "No presenting concerns yet.")}</div>
      <div class="meta">${c.updatedAt ? "Updated " + esc(c.updatedAt.slice(0, 10)) : ""}${(c.assessments || []).length ? " · spiritual screen on file" : ""}</div>
    </button>`).join("");
  box.querySelectorAll(".case-card").forEach((b) => { b.onclick = () => openCase(b.dataset.id); });
}

function blankCase() {
  const c = { notes: [] };
  for (const f of FIELDS) c[f] = "";
  return c;
}

function openEdit(id) {
  const existing = id ? caseById(id) : null;
  state.editing = existing ? JSON.parse(JSON.stringify(existing)) : blankCase();
  state.editNotes = JSON.parse(JSON.stringify(state.editing.notes || []));
  state.editDirty = false;
  $("#edit-title").textContent = existing ? "Edit case" : "New case";
  const form = $("#case-form");
  for (const f of FIELDS) if (form.elements[f]) form.elements[f].value = state.editing[f] || "";
  renderNotesEditor();
  show("edit");
}

function addBlankNote() {
  state.editNotes.push({ id: crypto.randomUUID(), date: new Date().toISOString().slice(0, 10), text: "" });
  state.editDirty = true;
  renderNotesEditor();
  const areas = document.querySelectorAll("#notes-editor textarea");
  const last = areas[areas.length - 1];
  if (last) last.focus();
}

function addSessionNoteFromCase() {
  if (!state.currentId) return;
  openEdit(state.currentId);
  addBlankNote();
  requestAnimationFrame(() => {
    const fs = document.getElementById("notes-fieldset");
    if (fs) fs.scrollIntoView({ block: "start" });
  });
}

function renderNotesEditor() {
  const box = $("#notes-editor");
  box.innerHTML = state.editNotes.map((n, i) => `
    <div class="note-edit" data-i="${i}">
      <div class="row">
        <input type="date" value="${esc(n.date || "")}" data-date>
        <button type="button" class="btn danger-ghost" data-del>Remove</button>
        ${state.prefs.speech ? '<button type="button" class="btn sm" data-mic>Dictate</button>' : ""}
      </div>
      <textarea rows="3" data-text>${esc(n.text || "")}</textarea>
    </div>`).join("") || `<p class="hint">No session notes yet.</p>`;
  box.querySelectorAll(".note-edit").forEach((el) => {
    const i = +el.dataset.i;
    el.querySelector("[data-date]").oninput = (e) => { state.editNotes[i].date = e.target.value; state.editDirty = true; };
    el.querySelector("[data-text]").oninput = (e) => { state.editNotes[i].text = e.target.value; state.editDirty = true; };
    el.querySelector("[data-del]").onclick = () => { state.editNotes.splice(i, 1); state.editDirty = true; renderNotesEditor(); };
    const mic = el.querySelector("[data-mic]");
    if (mic) mic.onclick = () => dictateInto(el.querySelector("[data-text]"), (val) => { state.editNotes[i].text = val; state.editDirty = true; });
  });
}

function readEditForm() {
  const form = $("#case-form");
  const c = { ...state.editing, notes: state.editNotes.filter((n) => (n.text || "").trim() || n.date) };
  for (const f of FIELDS) if (form.elements[f]) c[f] = form.elements[f].value.trim();
  return c;
}

async function saveEdit() {
  const c = readEditForm();
  if (!c.name) { toast("A name is required, even for a fictional case."); return; }
  const saved = await vault.saveCase(c);
  const i = state.cases.findIndex((x) => x.id === saved.id);
  if (i >= 0) state.cases[i] = saved; else state.cases.push(saved);
  state.editDirty = false;
  toast("Saved in this browser, encrypted.");
  openCase(saved.id);
}

async function cancelEdit() {
  if (state.editDirty && !(await confirmBox("Discard changes?", "You have unsaved changes to this case.", "Discard", true))) return;
  if (state.editing && state.editing.id) openCase(state.editing.id);
  else showHome();
}

function sec(label, val) {
  return `<div class="rec-section"><h4>${esc(label)}</h4><div class="val ${val ? "" : "empty-val"}">${val ? esc(val) : "Not recorded"}</div></div>`;
}
function hasDxOrPlan(c) {
  return !!(String(c.workingDiagnoses || "").trim() || String(c.confirmedDiagnoses || "").trim() || String(c.treatmentPlan || "").trim());
}

function screenWhen(iso) {
  const day = String(iso || "").slice(0, 10);
  return day || "Undated";
}

function renderScreenSection(c) {
  const list = (Array.isArray(c.assessments) ? c.assessments : [])
    .slice()
    .sort((a, b) => String(b.completedAt || "").localeCompare(String(a.completedAt || "")));
  const saved = list.map((a) => {
    const inst = instrumentById(a.instrument);
    const copy = resultCopy(a.instrument, a.answers, a.stressor);
    if (!inst || !copy) return "";
    const headline = a.instrument === RSS5_ID
      ? `Total ${copy.scores.total} of 5–25`
      : `Positive ${copy.scores.positive} of 0–21 · Negative ${copy.scores.negative} of 0–21`;
    const detail = copy.lines.map((line) => `<div>${esc(line)}</div>`).join("");
    const flags = (copy.explore || []).map((item) => `<div>${esc(item.domain)}: ${item.value} ${esc(item.label)} — ${esc(item.text)}</div>`).join("");
    return `<div class="saved-screen">
      <div class="date">${esc(inst.short)} · ${esc(screenWhen(a.completedAt))}</div>
      <div><b>${esc(headline)}</b></div>
      ${detail}
      ${flags}
      <div class="row" style="margin-top:.4rem">
        <button type="button" class="btn sm" data-open-screen="${esc(a.id)}">Review</button>
        <button type="button" class="btn sm danger-ghost" data-del-screen="${esc(a.id)}">Remove from record</button>
      </div>
    </div>`;
  }).join("");
  return `<div class="rec-section" id="spiritual-screens">
    <h4>Spiritual assessment</h4>
    <p class="hint">Optional intake screens for adult clients. Completed here with the client. Answers stay in this encrypted record and are not uploaded.</p>
    ${saved || `<div class="val empty-val">No spiritual screen saved on this record yet.</div>`}
    <div class="row wrap-row" style="margin-top:.6rem">
      <button type="button" class="btn sm primary" id="new-rss5">Complete RSS-5</button>
      <button type="button" class="btn sm primary" id="new-rcope">Complete Brief RCOPE</button>
    </div>
  </div>`;
}

function bindScreenSection(c) {
  const start = (id) => openScreen(c.id, id, null);
  const rss = $("#new-rss5");
  const rcope = $("#new-rcope");
  if (rss) rss.onclick = () => start(RSS5_ID);
  if (rcope) rcope.onclick = () => start(RCOPE_ID);
  document.querySelectorAll("[data-open-screen]").forEach((b) => {
    b.onclick = () => openScreen(c.id, null, b.dataset.openScreen);
  });
  document.querySelectorAll("[data-del-screen]").forEach((b) => {
    b.onclick = () => removeScreen(c.id, b.dataset.delScreen);
  });
}

function renderRecord(c) {
  const age = ageLine(c.dob);
  const notes = (c.notes || []).slice().sort((a, b) => String(a.date).localeCompare(String(b.date)));
  const noteCount = notes.length;
  $("#record-tools").innerHTML = `
    <button type="button" class="btn sm" id="jump-screens">Spiritual screens</button>
    <button type="button" class="btn sm" id="jump-notes">Session notes${noteCount ? " (" + noteCount + ")" : ""}</button>
    <button type="button" class="btn sm primary" id="add-note-case">+ Add session note</button>`;
  $("#jump-screens").onclick = () => {
    const el = document.getElementById("spiritual-screens");
    if (el) el.scrollIntoView({ block: "start" });
  };
  $("#jump-notes").onclick = () => {
    const el = document.getElementById("session-notes");
    if (el) el.scrollIntoView({ block: "start" });
  };
  $("#add-note-case").onclick = () => addSessionNoteFromCase();
  $("#record-body").innerHTML = `
    <div class="rec-section"><h4>Client</h4>
      <dl class="id-grid">
        <dt>Name</dt><dd>${esc(c.name)}</dd>
        ${c.preferredName ? `<dt>Preferred</dt><dd>${esc(c.preferredName)}</dd>` : ""}
        ${c.dob ? `<dt>Birth date</dt><dd>${esc(c.dob)}${age ? " (age " + esc(age) + ")" : ""}</dd>` : ""}
        ${c.phone ? `<dt>Phone</dt><dd>${esc(c.phone)}</dd>` : ""}
        ${c.email ? `<dt>Email</dt><dd>${esc(c.email)}</dd>` : ""}
        ${c.clientId ? `<dt>Client ID</dt><dd>${esc(c.clientId)}</dd>` : ""}
        ${c.address ? `<dt>Address</dt><dd>${esc(c.address)}</dd>` : ""}
      </dl>
    </div>
    ${sec("Presenting concerns", c.presentingConcerns)}
    ${sec("History", c.history)}
    ${renderScreenSection(c)}
    ${sec("Working diagnoses", c.workingDiagnoses)}
    ${sec("Confirmed diagnoses", c.confirmedDiagnoses)}
    ${sec("Treatment plan", c.treatmentPlan)}
    <div class="rec-section">
      <h4>10-session plan</h4>
      <div class="val ${c.sessionPlan ? "" : "empty-val"}">${c.sessionPlan ? esc(c.sessionPlan) : "Not written yet."}</div>
      ${hasDxOrPlan(c)
        ? `<p class="hint">Draft a 10-session CBT plan from the de-identified record. You preview the exact text, then choose Send or Cancel.</p>
           <button class="btn ai-primary" type="button" id="plan-ten">Plan 10 sessions</button>`
        : `<p class="hint">Add a working diagnosis or a treatment plan first, then this button appears.</p>`}
    </div>
    <div class="rec-section" id="session-notes"><h4>Session notes</h4>
      ${notes.length ? notes.map((n) => `<div class="rec-note"><div class="date">${esc(n.date || "Undated")}</div><div class="val">${esc(n.text || "")}</div></div>`).join("") : `<div class="val empty-val">No session notes yet.</div>`}
    </div>`;
  const planBtn = $("#plan-ten");
  if (planBtn) planBtn.onclick = () => planTen(c.id);
  bindScreenSection(c);
}

function openCase(id) {
  const c = caseById(id);
  if (!c) return showHome();
  if (state.session && state.session.caseId !== id) endSession(true);
  state.currentId = id;
  $("#case-title").textContent = c.name || "Case";
  $("#case-sample-badge").hidden = !c.sample;
  renderRecord(c);
  renderAI();
  show("case");
}

function openScreen(caseId, instrumentId, adminId) {
  const c = caseById(caseId);
  if (!c) return showHome();
  let admin = null;
  if (adminId) {
    admin = (c.assessments || []).find((a) => a.id === adminId);
    if (!admin) { toast("That screen is no longer on this record."); return; }
    instrumentId = admin.instrument;
  }
  const inst = instrumentById(instrumentId);
  if (!inst) return;
  state.currentId = caseId;
  state.screen = {
    caseId,
    instrument: inst.id,
    adminId: admin ? admin.id : null,
    answers: admin ? admin.answers.slice() : flatItems(inst).map(() => null),
    stressor: admin ? (admin.stressor || "") : "",
  };
  state.screenDirty = false;
  renderScreen();
  show("screen");
}

function renderScreen() {
  const s = state.screen;
  const inst = s && instrumentById(s.instrument);
  if (!inst) return;
  const c = caseById(s.caseId);
  $("#screen-title").textContent = inst.short;
  const items = flatItems(inst);
  let n = 0;
  const groups = inst.groups.map((g) => {
    const cards = g.items.map((item) => {
      const i = n++;
      const opts = inst.anchors.map((a) => {
        const on = s.answers[i] === a.value ? " on" : "";
        return `<label class="${on.trim()}"><input type="radio" name="item-${i}" value="${a.value}" ${s.answers[i] === a.value ? "checked" : ""}><small>${a.value}</small>${esc(a.label)}</label>`;
      }).join("");
      const domain = item.domain ? `<div class="domain-tag">${esc(item.domain)}</div>` : "";
      return `<div class="item-card">${domain}<p><b>${i + 1}.</b> ${esc(item.text)}</p><div class="scale-opts">${opts}</div></div>`;
    }).join("");
    return `<div class="screen-card"><h3>${esc(g.heading)}</h3><p class="hint">${esc(g.note)}</p>${cards}</div>`;
  }).join("");
  const copy = resultCopy(inst.id, s.answers, s.stressor);
  const missing = missingPieces(inst.id, s.answers, s.stressor);
  const scoreHtml = copy ? scorePanel(inst, copy) : `<div class="score-panel"><h3>Score</h3><p>${esc(missing[0] || "Answer every item to see the official score.")}</p><p>Nothing is written into the record until you press Save.</p></div>`;
  const stressor = inst.needsStressor ? `<label>Critical life event (the stressor this screen is about)
      <input id="screen-stressor" type="text" maxlength="500" value="${esc(s.stressor)}" autocomplete="off" placeholder="Name the event before the items">
    </label>` : "";
  $("#screen-body").innerHTML = `
    <div class="screen-banner">
      <div class="domain-tag" style="color:var(--gold-ink)">Clinical Companion · adult clients</div>
      <h3>${esc(inst.title)}</h3>
      <p>${esc(inst.intro)}</p>
      <p class="adult-note">For an adult client, completed with the counselor. Answers stay in this encrypted record on this computer. They are not uploaded.</p>
    </div>
    <div class="screen-card">
      <p>${esc(inst.scaleNote)}</p>
      ${stressor}
      ${c ? `<p class="hint">Record: ${esc(c.name || "Untitled")}</p>` : ""}
    </div>
    ${groups}
    ${scoreHtml}
    <p class="error" id="screen-error"></p>
    <div class="row wrap-row">
      <button type="button" class="btn primary" id="screen-save">Save into this record</button>
      <button type="button" class="btn" id="screen-cancel">Cancel</button>
    </div>
    <p class="credit-line">${linkifyCredit(inst.credit)}</p>`;
  $("#screen-body").querySelectorAll(".scale-opts input").forEach((input) => {
    input.onchange = () => {
      const i = Number(input.name.replace("item-", ""));
      s.answers[i] = Number(input.value);
      state.screenDirty = true;
      const y = window.scrollY;
      renderScreen();
      window.scrollTo(0, y);
    };
  });
  const stressorInput = $("#screen-stressor");
  if (stressorInput) {
    stressorInput.oninput = () => { s.stressor = stressorInput.value; state.screenDirty = true; updateLiveScore(); };
  }
  $("#screen-save").onclick = () => saveScreen().catch((e) => toast(e.message));
  $("#screen-cancel").onclick = () => leaveScreen();
}

function linkifyCredit(text) {
  return esc(text).replace(/https?:\/\/[^\s)]+/g, (url) => `<a href="${url}" target="_blank" rel="noopener">${url}</a>`);
}

function scorePanel(inst, copy) {
  let nums = "";
  if (inst.id === RSS5_ID) {
    nums = `<div class="score-num"><b>${copy.scores.total}</b><span>Total, range 5–25</span></div>`;
  } else {
    nums = `<div class="score-num"><b>${copy.scores.positive}</b><span>Positive religious coping, 0–21</span></div>
      <div class="score-num"><b>${copy.scores.negative}</b><span>Negative religious coping, 0–21</span></div>`;
  }
  const explore = (copy.explore || []).map((item) => `<li><b>${esc(item.domain)}</b> · ${item.value} ${esc(item.label)}: ${esc(item.text)}</li>`).join("");
  return `<div class="score-panel" aria-live="polite"><h3>Counselor’s result</h3><div class="score-nums">${nums}</div>
    ${copy.lines.map((line) => `<p>${esc(line)}</p>`).join("")}
    ${explore ? `<ul class="explore-list">${explore}</ul>` : ""}
  </div>`;
}

function updateLiveScore() {
  const s = state.screen;
  const inst = instrumentById(s.instrument);
  const panel = document.querySelector("#screen-body .score-panel");
  if (!panel || !inst) return;
  const copy = resultCopy(inst.id, s.answers, s.stressor);
  const missing = missingPieces(inst.id, s.answers, s.stressor);
  panel.outerHTML = copy
    ? scorePanel(inst, copy)
    : `<div class="score-panel" aria-live="polite"><h3>Score</h3><p>${esc(missing[0] || "Answer every item to see the official score.")}</p><p>Nothing is written into the record until you press Save.</p></div>`;
}

async function saveScreen() {
  const s = state.screen;
  const c = caseById(s.caseId);
  const inst = instrumentById(s.instrument);
  if (!c || !inst) return;
  const missing = missingPieces(inst.id, s.answers, s.stressor);
  if (missing.length) {
    $("#screen-error").textContent = missing[0];
    return;
  }
  const scores = scoreInstrument(inst.id, s.answers);
  const copy = JSON.parse(JSON.stringify(c));
  copy.assessments = Array.isArray(copy.assessments) ? copy.assessments : [];
  const record = {
    id: s.adminId || crypto.randomUUID(),
    instrument: inst.id,
    completedAt: new Date().toISOString(),
    answers: s.answers.slice(),
    stressor: inst.needsStressor ? s.stressor.trim() : "",
    scores,
  };
  const i = copy.assessments.findIndex((a) => a.id === record.id);
  if (i >= 0) copy.assessments[i] = record;
  else copy.assessments.push(record);
  const saved = await vault.saveCase(copy);
  state.cases[state.cases.findIndex((x) => x.id === saved.id)] = saved;
  state.screenDirty = false;
  toast(inst.short + " saved in this encrypted record.");
  openCase(saved.id);
  requestAnimationFrame(() => {
    const el = document.getElementById("spiritual-screens");
    if (el) el.scrollIntoView({ block: "start" });
  });
}

async function removeScreen(caseId, adminId) {
  if (!(await confirmBox("Remove this screen?", "The answers will be deleted from this record on this computer.", "Remove", true))) return;
  const c = caseById(caseId);
  if (!c) return;
  const copy = JSON.parse(JSON.stringify(c));
  copy.assessments = (copy.assessments || []).filter((a) => a.id !== adminId);
  const saved = await vault.saveCase(copy);
  state.cases[state.cases.findIndex((x) => x.id === saved.id)] = saved;
  renderRecord(saved);
  toast("Removed from this record.");
}

async function leaveScreen() {
  if (!(await leaveScreenIfNeeded())) return;
  if (state.currentId) openCase(state.currentId);
  else showHome();
}

async function leaveScreenIfNeeded() {
  if (state.view !== "screen") return true;
  if (state.screenDirty && !(await confirmBox("Leave this screen?", "Answers you have not saved will stay off the record.", "Leave without saving", true))) return false;
  state.screenDirty = false;
  state.screen = null;
  return true;
}

function endSession(silent) {
  state.session = null;
  if (!silent) renderAI();
}

function renderAI() {
  const body = $("#ai-body");
  const s = state.session;
  if (!s || s.caseId !== state.currentId) {
    body.innerHTML = `
      <div class="ai-intro">
        <h3>Think a case through</h3>
        <p class="remote-note">Names, dates, phone numbers, emails, addresses, and ID numbers are removed before you are asked to send anything. You see the exact text and choose Send or Cancel.</p>
        <p class="small">${isMock() ? "Mock mode is on. The answer is a canned fictional draft. Nothing leaves this browser." : "Live mode sends only the approved text to the proxy in config.js. This browser does not have the API key."}</p>
        <p class="small">The chat is temporary. Only what you add to the record is saved.</p>
        <button class="btn ai-primary" type="button" id="ai-start">Start AI session</button>
      </div>`;
    $("#ai-start").onclick = startSession;
    return;
  }
  if (s.stage === "preview") return renderDeidPreview();
  renderChat();
}

function startSession() {
  const c = caseById(state.currentId);
  const built = deidentify(c);
  state.session = { caseId: c.id, stage: "preview", draft: built.text, counts: built.counts, deidText: null, messages: [], busy: false };
  renderAI();
}

function renderDeidPreview() {
  const s = state.session;
  const chips = Object.entries(s.counts).map(([k, n]) => `<span class="chip">${esc(String(k).replace("removed field: ", "removed "))}${n > 1 ? " ×" + n : ""}</span>`).join("");
  $("#ai-body").innerHTML = `
    <div class="preview-wrap">
      <h3>Review the de-identified case</h3>
      <p class="small">This is the case text later requests will include. Edit anything that could still identify a person. Nothing is sent on this step.</p>
      <div class="chips">${chips || '<span class="chip">no identifiers found</span>'}</div>
      <textarea id="deid-text" spellcheck="false"></textarea>
      <div class="preview-actions">
        <button class="btn" type="button" id="deid-cancel">Cancel</button>
        <div class="spacer"></div>
        <button class="btn ai-primary" type="button" id="deid-approve">Approve and open the chat</button>
      </div>
    </div>`;
  $("#deid-text").value = s.draft;
  $("#deid-text").oninput = (e) => { s.draft = e.target.value; };
  $("#deid-cancel").onclick = () => { endSession(true); renderAI(); };
  $("#deid-approve").onclick = approveDeid;
}

async function approveDeid() {
  const s = state.session;
  const text = $("#deid-text").value;
  const leaks = findLeaks(text, caseById(s.caseId));
  if (leaks.length) {
    const ok = await modal({
      title: "Possible identifying details",
      okLabel: "Use this text anyway",
      cancelLabel: "Go back and edit",
      danger: true,
      html: `<p>These items still look identifying:</p><div class="leak-warn">${leaks.map((l) => "• " + esc(l)).join("<br>")}</div>`,
    });
    if (!ok) return;
  }
  s.deidText = text;
  s.stage = "chat";
  renderAI();
}

function renderChat() {
  const s = state.session;
  $("#ai-body").innerHTML = `
    <div class="ai-toolbar">
      <span class="model">${esc(isMock() ? "Mock · fictional draft" : "Live proxy")}</span>
      <div class="spacer"></div>
      <button class="btn ai sm" type="button" id="chat-view">View shared text</button>
      <button class="btn danger-ghost sm" type="button" id="chat-end">End session</button>
    </div>
    <div class="chat" id="chat"></div>
    <div class="quick">${Object.keys(QUICK).map((k) => `<button class="btn ai sm quick-btn" type="button">${esc(k)}</button>`).join("")}</div>
    <div class="composer">
      <textarea id="chat-input" rows="2" placeholder="Ask a question… Enter to preview and send. Shift+Enter for a new line."></textarea>
      ${state.prefs.speech ? '<button class="btn" type="button" id="chat-mic">Dictate</button>' : ""}
      <button class="btn ai-primary" type="button" id="chat-send">Send</button>
    </div>`;
  $("#ai-body").querySelectorAll(".quick-btn").forEach((b) => { b.onclick = () => sendQuestion(QUICK[b.textContent]); });
  $("#chat-send").onclick = () => sendQuestion($("#chat-input").value);
  $("#chat-input").onkeydown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendQuestion($("#chat-input").value); }
  };
  if ($("#chat-mic")) $("#chat-mic").onclick = () => dictateInto($("#chat-input"));
  $("#chat-end").onclick = async () => {
    if (await confirmBox("End AI session?", "The chat and the de-identified text will be cleared. Anything you did not add to the record will be gone.", "End session")) {
      endSession(true); renderAI(); toast("AI session cleared.");
    }
  };
  $("#chat-view").onclick = () => modal({
    title: "Text shared with the AI",
    html: `<div class="add-preview">${esc(s.deidText)}</div>`,
    okLabel: "Close",
    cancelLabel: null,
  });
  renderMessages();
}

function renderMessages() {
  const s = state.session;
  const chat = $("#chat");
  if (!chat || !s) return;
  if (!s.messages.length) {
    chat.innerHTML = `<p class="small">The approved de-identified case is loaded. Ask a question, or use a prompt below. Each question shows a preview before it is sent.</p>`;
    return;
  }
  chat.innerHTML = s.messages.map((m, i) => {
    if (m.role === "user") return `<div class="msg user">${esc(m.content)}</div>`;
    if (m.role === "error") return `<div class="msg error-msg">${esc(m.content)}</div>`;
    if (m.streaming) return `<div class="msg assistant"><div class="ai-tag">AI draft — not part of the record</div><p>Working…</p></div>`;
    return `<div class="msg assistant"><div class="ai-tag">AI draft — not part of the record</div><div class="content">${renderMd(m.content)}</div>
      <div class="actions"><button class="btn sm" type="button" data-copy="${i}">Copy</button><button class="btn ai sm" type="button" data-add="${i}">Add to record…</button></div></div>`;
  }).join("");
  chat.querySelectorAll("[data-copy]").forEach((b) => {
    b.onclick = () => navigator.clipboard.writeText(s.messages[+b.dataset.copy].content).then(() => toast("Copied"));
  });
  chat.querySelectorAll("[data-add]").forEach((b) => { b.onclick = () => addToRecord(+b.dataset.add); });
  chat.scrollTop = chat.scrollHeight;
}

function userDocs() {
  return (vault.getData().libraryDocs || []).map((d) => ({ title: d.title, text: d.text }));
}

async function sendQuestion(text) {
  const s = state.session;
  text = String(text || "").trim();
  if (!s || s.busy || !text) return;
  s.busy = true;
  let prepared;
  try {
    prepared = await prepareChat({
      caseRecord: caseById(s.caseId),
      caseText: s.deidText,
      history: s.messages.filter((m) => m.role === "user" || m.role === "assistant").concat([{ role: "user", content: text }]),
      useLibrary: state.prefs.useLibrary !== false,
      userDocs: userDocs(),
      question: text,
    });
  } catch (err) {
    s.busy = false;
    toast(err.message);
    return;
  }
  const ok = await showSendPreview(prepared.preview);
  if (!ok) { s.busy = false; return; }
  s.messages.push({ role: "user", content: text });
  const reply = { role: "assistant", content: "", streaming: true };
  s.messages.push(reply);
  if ($("#chat-input")) $("#chat-input").value = "";
  renderMessages();
  try {
    const result = await complete(prepared);
    reply.content = result.content || "(No answer.)";
    reply.streaming = false;
  } catch (err) {
    s.messages.pop();
    s.messages.pop();
    s.messages.push({ role: "error", content: err.message });
  } finally {
    s.busy = false;
    renderMessages();
  }
}

function showSendPreview(preview) {
  const leaks = preview.leaks || [];
  const hist = preview.history || [];
  const earlier = hist.length > 1 ? hist.slice(0, -1) : [];
  const question = preview.kind === "plan" ? "" : (preview.question || "");
  return modal({
    title: "What will be sent",
    okLabel: leaks.length ? "Send anyway" : "Send",
    cancelLabel: "Cancel",
    danger: leaks.length > 0,
    html: `
      <p class="remote-note">${preview.mock
        ? "Mock mode. If you press Send, a canned draft is written in this browser. This text is not transmitted."
        : "If you press Send, this text goes to <b>" + esc(preview.host) + "</b>. The API key stays on that server."}</p>
      <p class="small">Model <b>${esc(preview.model)}</b>. Standing instructions (${preview.standingWords} words) and the clinical instructions are included. They contain no client information and are not shown here.</p>
      ${leaks.length ? `<div class="leak-warn"><b>Possible identifying details:</b> ${leaks.map((l) => "<code>" + esc(l) + "</code>").join(", ")}. Cancel unless they are fictional.</div>` : ""}
      ${question ? `<p><b>Your question</b></p><div class="add-preview">${esc(question)}</div>` : `<p><b>Request</b></p><div class="add-preview">${esc(preview.question || "")}</div>`}
      <p><b>De-identified case</b> (${(preview.caseText || "").length.toLocaleString()} characters)</p>
      <div class="add-preview">${esc(preview.caseText || "")}</div>
      ${earlier.length ? `<p><b>Earlier messages</b></p><div class="add-preview">${earlier.map((m) => esc((m.role === "user" ? "Counselor: " : "AI: ") + m.content)).join("\n\n")}</div>` : ""}
      ${(preview.library || []).length ? `<p><b>Library passages</b> (${preview.library.length})</p><div class="add-preview">${esc(preview.libraryText || "")}</div>` : ""}
    `,
  });
}

async function addToRecord(i) {
  const m = state.session.messages[i];
  if (!m || m.role !== "assistant") return;
  const sections = [["note", "New session note (today)"], ["workingDiagnoses", "Working diagnoses"], ["confirmedDiagnoses", "Confirmed diagnoses"], ["treatmentPlan", "Treatment plan"], ["sessionPlan", "10-session plan"]];
  $("#modal-title").textContent = "Add to the permanent record";
  $("#modal-body").innerHTML = `<p class="small">Edit the draft. Placeholders such as [CLIENT] stay until you change them.</p>
    <div id="add-secs">${sections.map(([k, v], n) => `<label class="check"><input type="radio" name="sec" value="${k}" ${n === 1 ? "checked" : ""}> ${esc(v)}</label>`).join("")}</div>
    <textarea id="add-text" rows="8"></textarea>`;
  $("#add-text").value = toPlain(m.content);
  $("#modal-ok").textContent = "Save into the case";
  $("#modal-ok").className = "btn primary";
  $("#modal-cancel").hidden = false;
  $("#modal-cancel").textContent = "Cancel";
  $("#modal").classList.remove("danger");
  $("#modal-backdrop").hidden = false;
  const choice = await new Promise((resolve) => {
    const finish = (val) => {
      const text = val ? $("#add-text").value.trim() : "";
      const picked = document.querySelector('#add-secs input[name="sec"]:checked');
      $("#modal-backdrop").hidden = true;
      $("#modal-ok").onclick = null;
      $("#modal-cancel").onclick = null;
      resolve(val ? { text, section: picked ? picked.value : "workingDiagnoses" } : null);
    };
    $("#modal-ok").onclick = () => finish(true);
    $("#modal-cancel").onclick = () => finish(false);
  });
  if (!choice || !choice.text) return;
  await commitAdd(choice.section, choice.text);
}

async function commitAdd(section, text) {
  const c = JSON.parse(JSON.stringify(caseById(state.session.caseId)));
  const stamp = new Date().toISOString().slice(0, 10);
  const block = text + "\n(AI-assisted draft, reviewed by counselor, " + stamp + ")";
  if (section === "note") {
    c.notes = c.notes || [];
    c.notes.push({ id: crypto.randomUUID(), date: stamp, text: block });
  } else if (section === "sessionPlan") c.sessionPlan = block;
  else c[section] = (c[section] ? c[section].replace(/\s+$/, "") + "\n\n" : "") + block;
  const saved = await vault.saveCase(c);
  state.cases[state.cases.findIndex((x) => x.id === saved.id)] = saved;
  renderRecord(saved);
  toast("Saved into the encrypted case.");
}

async function planTen(caseId) {
  const c = caseById(caseId);
  if (!hasDxOrPlan(c)) return;
  if (!state.session || state.session.caseId !== caseId || !state.session.deidText) {
    const built = deidentify(c);
    state.session = { caseId, stage: "preview", draft: built.text, counts: built.counts, deidText: null, messages: [], busy: false };
    renderAI();
    toast("Approve the de-identified case first. Then use Plan 10 sessions again.");
    return;
  }
  const prepared = await preparePlan({
    caseRecord: c,
    caseText: state.session.deidText,
    useLibrary: state.prefs.useLibrary !== false,
    userDocs: userDocs(),
  });
  if (!(await showSendPreview(prepared.preview))) return;
  try {
    const result = await complete(prepared);
    const record = formatPlanRecord(result.content, { generatedAt: new Date().toISOString(), model: result.model });
    const keep = await modal({
      title: "Save this 10-session plan?",
      okLabel: "Save into the case",
      cancelLabel: "Don't save",
      html: `<p class="small">This draft is not in the record until you save it.</p><div class="add-preview">${esc(record)}</div>`,
    });
    if (!keep) {
      state.session.messages.push({ role: "user", content: "Plan 10 sessions" }, { role: "assistant", content: result.content });
      renderChat();
      return;
    }
    const copy = JSON.parse(JSON.stringify(c));
    copy.sessionPlan = record;
    const saved = await vault.saveCase(copy);
    state.cases[state.cases.findIndex((x) => x.id === saved.id)] = saved;
    renderRecord(saved);
    toast("10-session plan saved in this encrypted case.");
  } catch (err) { toast(err.message); }
}

let recog = null;
function dictateInto(textarea, onValue) {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) { toast("This browser does not offer speech-to-text."); return; }
  if (recog) { try { recog.stop(); } catch { /* already stopped */ } recog = null; return; }
  recog = new SR();
  recog.lang = "en-US";
  recog.interimResults = false;
  recog.onresult = (ev) => {
    const said = ev.results[ev.results.length - 1][0].transcript;
    textarea.value = (textarea.value ? textarea.value.replace(/\s*$/, " ") : "") + said;
    if (onValue) onValue(textarea.value);
  };
  recog.onerror = () => toast("Dictation stopped.");
  recog.onend = () => { recog = null; };
  recog.start();
  toast("Listening… press Dictate again to stop.");
}

async function renderLibrary() {
  show("library");
  const q = ($("#lib-search").value || "").trim().toLowerCase();
  const cat = await loadCatalog();
  const user = vault.isUnlocked() ? vault.getData().libraryDocs || [] : [];
  const items = (cat.items || []).filter((it) => !q || (it.label + " " + (it.subcategory || "")).toLowerCase().includes(q));
  const groups = new Map();
  for (const it of items) {
    const key = it.category || "Library";
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(it);
  }
  let html = "";
  const userFiltered = user.filter((d) => !q || d.title.toLowerCase().includes(q));
  if (userFiltered.length) {
    html += `<div class="lib-block card"><h3>Your notes (encrypted)</h3>${userFiltered.map((d) => `
      <div class="lib-item"><button class="btn ghost" type="button" data-user="${esc(d.id)}">${esc(d.title)}</button>
      <button class="btn danger-ghost sm" type="button" data-user-del="${esc(d.id)}">Remove</button></div>`).join("")}</div>`;
  }
  for (const [catName, list] of groups) {
    html += `<div class="lib-block card"><h3>${esc(catName)}</h3>${list.map((it) => `
      <div class="lib-item"><div><strong>${esc(it.label)}</strong><div class="hint">${esc(it.subcategory || "")}</div></div>
      <span>${it.file ? `<button class="btn sm" type="button" data-read="${esc(it.bundledId)}">Read</button>` : ""}
      ${it.href ? `<a class="btn sm" href="${esc(it.href)}" target="_blank" rel="noopener">PDF</a>` : ""}</span></div>`).join("")}</div>`;
  }
  $("#lib-tree").innerHTML = html || `<div class="empty">Nothing in the library matches.</div>`;
  $("#lib-tree").querySelectorAll("[data-read]").forEach((b) => {
    b.onclick = async () => {
      const item = (cat.items || []).find((x) => x.bundledId === b.dataset.read);
      const text = await loadBundledDoc(item);
      const reader = $("#lib-reader");
      reader.hidden = false;
      reader.innerHTML = `<h3>${esc(item.label)}</h3><div class="content">${renderMd(text)}</div>`;
      reader.scrollIntoView({ behavior: "smooth", block: "start" });
    };
  });
  $("#lib-tree").querySelectorAll("[data-user]").forEach((b) => {
    b.onclick = () => {
      const doc = user.find((d) => d.id === b.dataset.user);
      const reader = $("#lib-reader");
      reader.hidden = false;
      reader.innerHTML = `<h3>${esc(doc.title)}</h3><div class="content">${renderMd(doc.text)}</div>`;
    };
  });
  $("#lib-tree").querySelectorAll("[data-user-del]").forEach((b) => {
    b.onclick = async () => {
      const docs = (vault.getData().libraryDocs || []).filter((d) => d.id !== b.dataset.userDel);
      await vault.saveLibraryDocs(docs);
      toast("Removed from this browser.");
      renderLibrary();
    };
  });
}

function renderForms() {
  const local = [
    [RSS5_ID, "RSS-5: Spiritual struggles", INSTRUMENTS[RSS5_ID].blurb + " Complete it inside a client record."],
    [RCOPE_ID, "Brief RCOPE: Religious coping", INSTRUMENTS[RCOPE_ID].blurb + " Complete it inside a client record."],
  ];
  const forms = [
    ["Flow of Care chart", "The 14 steps of care, from the first phone call to belief cards. Printable PDF.", "../counselors/forms/Clinical-Companion-Flow-of-Care.pdf"],
    ["New Client Forms (Step 2)", "The link the intake person sends after the phone call: About You and the Brief History, completed online before the first visit. Practice sample: fictional clients only.", "../counselors/new-client-forms.html"],
    ["Forms to Complete card (Step 9)", "At the end of a session, check off the follow-up forms (PHQ-9, GAD-7, and more), then send the client one link or print the card. RSS-5 and Brief RCOPE are completed in the client record, not on that public card. Practice sample: fictional clients only.", "../counselors/followup-forms.html"],
    ["New Client Packet", "Fill practice details in the browser and download a packet. Review it with an attorney in your state.", "../counselors/practice-forms.html"],
    ["Confidentiality agreement", "Blank fillable PDF.", "../counselors/forms/Confidentiality-Agreement-fillable.pdf"],
    ["Pastoral confidentiality agreement", "Blank fillable PDF.", "../counselors/forms/Pastoral-Confidentiality-Agreement-fillable.pdf"],
    ["Questioning false beliefs", "Blank Belief Counseling worksheet.", "../counselors/forms/Belief-Counseling-Questioning-False-Beliefs.pdf"],
    ["Cognitive errors checklist", "Blank Belief Counseling worksheet.", "../counselors/forms/Belief-Counseling-Cognitive-Errors-Checklist.pdf"],
    ["Christian experiences and beliefs", "Blank Belief Counseling checklist. Counselor-guided, separate from the scored screens.", "../counselors/forms/Belief-Counseling-Christian-Experiences-and-Beliefs-Checklist.pdf"],
  ];
  const localHtml = local.map(([id, title, blurb]) => `
    <div class="card form-card"><h3>${esc(title)}</h3><p>${esc(blurb)}</p>
    <button type="button" class="btn primary" data-local-screen="${esc(id)}">Open in the client record</button></div>`).join("");
  $("#form-list").innerHTML = localHtml + forms.map(([title, blurb, href]) => `
    <div class="card form-card"><h3>${esc(title)}</h3><p>${esc(blurb)}</p>
    <a class="btn" href="${esc(href)}" target="_blank" rel="noopener">Open</a></div>`).join("");
  $("#form-list").querySelectorAll("[data-local-screen]").forEach((b) => {
    b.onclick = () => {
      if (!state.currentId || !caseById(state.currentId)) {
        toast("Open a client record first. The screen is saved there, on this computer.");
        showHome();
        return;
      }
      openScreen(state.currentId, b.dataset.localScreen, null);
    };
  });
  show("forms");
}

function renderPrivacy() {
  $("#privacy-body").innerHTML = `
    <div class="pv warn"><b>Not yet for real client data</b><p>Use fictional cases only. A Business Associate Agreement is not signed, and zero data retention is not confirmed. Do not type real names or identifiers.</p>
    <p>The wording to use later, after a signed BAA and zero data retention, is “HIPAA-compliant processing under a signed BAA.” That is not true of this app today.</p></div>
    <div class="pv"><b>Records stay in this browser</b><p>Cases are encrypted with AES-GCM. The key is derived from your passphrase with PBKDF2 (600,000 rounds) and is kept in memory only while the app is unlocked. The website and Wix do not receive case text.</p></div>
    <div class="pv"><b>What an AI request contains</b><p>You see the exact de-identified text, your question, and any library passages, then press Send or Cancel. Standing instructions are added by the program and are not shown or editable. In mock mode nothing is transmitted. In live mode the text goes only to the proxy address in config.js, which holds the API key.</p></div>
    <div class="pv"><b>Backups</b><p>Export writes an encrypted file. Import replaces the cases in this browser. The file does not help if you forget the passphrase.</p></div>`;
  show("privacy");
}

function renderSettings() {
  $("#settings-mode").innerHTML = isMock()
    ? `<b>Mock mode.</b> Canned answers. Proxy address: <code>${esc(CONFIG.proxyUrl || "(not set)")}</code>`
    : `<b>Live mode.</b> Proxy: <code>${esc(CONFIG.proxyUrl)}</code>`;
  $("#set-library").checked = state.prefs.useLibrary !== false;
  $("#set-speech").checked = !!state.prefs.speech;
  $("#set-autolock").value = String(state.prefs.autoLockMin ?? 15);
  show("settings");
}

async function exportBackup() {
  const env = await vault.exportEnvelope();
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([JSON.stringify(env)], { type: "application/json" }));
  a.download = "clinical-companion-backup-" + new Date().toISOString().slice(0, 10) + ".json";
  a.click();
  URL.revokeObjectURL(a.href);
  $("#backup-msg").textContent = "Encrypted backup downloaded.";
}

function bind() {
  $("#nav-home").onclick = async () => { if (await leaveScreenIfNeeded()) showHome(); };
  $("#nav-library").onclick = async () => { if (await leaveScreenIfNeeded()) renderLibrary().catch((e) => toast(e.message)); };
  $("#nav-forms").onclick = async () => { if (await leaveScreenIfNeeded()) renderForms(); };
  $("#nav-back").onclick = goCounselors;
  $("#nav-privacy").onclick = async () => { if (await leaveScreenIfNeeded()) renderPrivacy(); };
  $("#nav-settings").onclick = async () => { if (await leaveScreenIfNeeded()) renderSettings(); };
  $("#nav-lock").onclick = async () => {
    if (!(await leaveScreenIfNeeded())) return;
    endSession(true); vault.lockVault(); $("#unlock-pw").value = ""; show("unlock");
  };
  $("#screen-back").onclick = () => leaveScreen();
  $("#setup-back").onclick = goCounselors;
  $("#unlock-back").onclick = goCounselors;
  $("#settings-back").onclick = goBack;
  $("#privacy-back").onclick = goBack;
  $("#new-case").onclick = () => openEdit(null);
  $("#search").oninput = renderHome;
  $("#edit-back").onclick = cancelEdit;
  $("#edit-cancel").onclick = cancelEdit;
  $("#edit-save").onclick = () => saveEdit().catch((e) => toast(e.message));
  $("#add-note").onclick = () => addBlankNote();
  $("#case-form").oninput = () => { state.editDirty = true; };
  $("#case-back").onclick = showHome;
  $("#case-edit").onclick = () => state.currentId && openEdit(state.currentId);
  $("#case-delete").onclick = async () => {
    const c = caseById(state.currentId);
    if (!c) return;
    if (!(await confirmBox("Delete this case?", "“" + c.name + "” will be removed from this browser.", "Delete", true))) return;
    await vault.deleteCase(c.id);
    state.cases = state.cases.filter((x) => x.id !== c.id);
    endSession(true);
    showHome();
    toast("Case deleted from this browser.");
  };
  $("#setup-form").onsubmit = async (e) => {
    e.preventDefault();
    const a = $("#setup-pw").value, b = $("#setup-pw2").value;
    if (a.length < 8) { $("#setup-error").textContent = "Use 8 or more characters."; return; }
    if (a !== b) { $("#setup-error").textContent = "The two passphrases do not match."; return; }
    $("#setup-submit").disabled = true;
    $("#setup-submit").textContent = "Encrypting…";
    try {
      const data = await vault.createVault(a);
      state.cases = data.cases;
      $("#setup-pw").value = "";
      $("#setup-pw2").value = "";
      showHome();
      toast("Encrypted records created in this browser. Three fictional cases are included.");
    } catch (ex) { $("#setup-error").textContent = ex.message; }
    finally { $("#setup-submit").disabled = false; $("#setup-submit").textContent = "Create encrypted records"; }
  };
  $("#unlock-form").onsubmit = async (e) => {
    e.preventDefault();
    const btn = $("#unlock-submit");
    btn.disabled = true; btn.textContent = "Unlocking…";
    $("#unlock-error").textContent = "";
    try {
      const data = await vault.unlockVault($("#unlock-pw").value);
      $("#unlock-pw").value = "";
      state.cases = data.cases;
      showHome();
    } catch (ex) {
      $("#unlock-error").textContent = ex.code === "WRONG_PASSWORD" ? "That passphrase did not open these records." : ex.message;
    } finally { btn.disabled = false; btn.textContent = "Unlock"; }
  };
  $("#set-save").onclick = () => {
    savePrefs({ useLibrary: $("#set-library").checked, speech: $("#set-speech").checked, autoLockMin: Number($("#set-autolock").value) });
    $("#set-msg").textContent = "Saved on this browser.";
    armIdle();
  };
  $("#pw-form").onsubmit = async (e) => {
    e.preventDefault();
    const n = $("#pw-new").value;
    if (n.length < 8) { $("#pw-error").textContent = "Use 8 or more characters."; return; }
    if (n !== $("#pw-new2").value) { $("#pw-error").textContent = "The new passphrases do not match."; return; }
    try {
      await vault.changePassword($("#pw-old").value, n);
      $("#pw-form").reset();
      $("#pw-error").textContent = "";
      toast("Passphrase changed. Records were re-encrypted.");
    } catch (ex) {
      $("#pw-error").textContent = ex.code === "WRONG_PASSWORD" ? "The current passphrase is not right." : ex.message;
    }
  };
  $("#backup-export").onclick = () => exportBackup().catch((err) => toast(err.message));
  $("#backup-restore").onclick = () => $("#restore-file").click();
  $("#restore-file").onchange = async () => {
    const file = $("#restore-file").files[0];
    $("#restore-file").value = "";
    if (!file) return;
    try {
      const result = await vault.restoreEnvelope(await file.text(), $("#restore-pw").value);
      state.cases = vault.getData().cases;
      $("#restore-pw").value = "";
      $("#restore-msg").textContent = "";
      toast("Restored " + result.cases + " cases into this browser.");
      showHome();
    } catch (ex) {
      $("#restore-msg").textContent = ex.code === "WRONG_PASSWORD" ? "That passphrase did not open the backup." : ex.message;
    }
  };
  $("#add-samples").onclick = async () => {
    let n = 0;
    for (const sample of sampleCases()) {
      if (state.cases.some((c) => c.id === sample.id)) continue;
      state.cases.push(await vault.saveCase(sample));
      n++;
    }
    $("#samples-msg").textContent = n ? "Added " + n + " fictional cases." : "Those sample cases are already here.";
  };
  $("#lib-search").oninput = () => renderLibrary().catch(() => {});
  $("#lib-add").onclick = () => $("#lib-file").click();
  $("#lib-file").onchange = async () => {
    const file = $("#lib-file").files[0];
    $("#lib-file").value = "";
    if (!file) return;
    const docs = vault.getData().libraryDocs || [];
    docs.push({ id: crypto.randomUUID(), title: file.name, text: await file.text(), addedAt: new Date().toISOString() });
    await vault.saveLibraryDocs(docs);
    toast("Added to your encrypted library.");
    renderLibrary();
  };
  ["pointerdown", "keydown"].forEach((ev) => document.addEventListener(ev, armIdle, { passive: true }));
}

let idleTimer = null;
function armIdle() {
  clearTimeout(idleTimer);
  const min = Number(state.prefs.autoLockMin ?? 15);
  if (!min || !vault.isUnlocked()) return;
  idleTimer = setTimeout(() => {
    if (!vault.isUnlocked()) return;
    endSession(true);
    vault.lockVault();
    show("unlock");
    toast("Locked after idle time.");
  }, min * 60 * 1000);
}

function takeMembershipToken() {
  const params = new URLSearchParams(location.hash.replace(/^#/, ""));
  const token = params.get("cct");
  if (token) {
    rememberMembershipToken(token);
    history.replaceState(null, "", location.pathname + location.search);
  }
  window.addEventListener("message", (ev) => {
    if (!CONFIG.membershipTokenOrigins.includes(ev.origin)) return;
    const data = ev.data || {};
    if (data.type === "cc-membership" && typeof data.token === "string" && data.token) {
      rememberMembershipToken(data.token);
      toast("Membership check received for this tab.");
    }
  });
}

async function boot() {
  takeMembershipToken();
  bind();
  try {
    if (await vault.vaultExists()) show("unlock");
    else show("setup");
  } catch (err) {
    show("setup");
    $("#setup-error").textContent = "This browser could not open private storage. Try a normal window (not private mode). " + err.message;
  }
}

boot();
