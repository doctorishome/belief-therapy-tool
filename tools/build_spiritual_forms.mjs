// Builds printable RSS-5 and Brief RCOPE forms for the Counselors' Room Process page.
// Item text comes from app/js/spiritual-screens.js (copied verbatim from the open-access articles).
// Run: node tools/build_spiritual_forms.mjs
import { writeFileSync } from "node:fs";
import { INSTRUMENTS } from "../app/js/spiritual-screens.js";

const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const linkify = (s) => esc(s).replace(/(https?:\/\/[^\s,)]+?)(\.?)(?=[\s,)]|$)/g, '<a href="$1">$1</a>$2');

const CSS = `:root{--navy:#12284c;--gold:#c9a227;--cream:#faf6ec;--ink:#1f2a3a;--mut:#5b6678;--line:#e3dcc6}
*{box-sizing:border-box}body{margin:0;background:var(--cream);font-family:Georgia,'Times New Roman',serif;color:var(--ink);font-size:17px;line-height:1.5}
.page{max-width:860px;margin:24px auto;background:#fff;border:1px solid var(--line);border-top:6px solid var(--navy);border-radius:8px;padding:30px 36px}
.brand{font:bold .78rem Arial,Helvetica,sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--gold)}
h1{color:var(--navy);margin:4px 0 2px;font-size:1.7rem}.sub{color:var(--mut);margin:0 0 16px}
.bar{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 18px}.bar button{background:var(--gold);color:var(--navy);border:0;border-radius:30px;padding:9px 22px;font:bold 1rem Georgia,serif;cursor:pointer}
.info{display:grid;grid-template-columns:1fr 1fr;gap:10px 24px;margin:0 0 18px}.info div{border-bottom:1px solid #999;padding-top:16px;font-size:.92rem;color:var(--mut)}
.box{background:var(--cream);border-left:4px solid var(--gold);padding:12px 16px;border-radius:0 6px 6px 0;margin:0 0 16px}
h2{color:var(--navy);font-size:1.15rem;margin:20px 0 4px}.note{color:var(--mut);font-size:.92rem;margin:0 0 8px}
table{width:100%;border-collapse:collapse;margin:0 0 6px}th,td{border-bottom:1px solid var(--line);padding:9px 6px;vertical-align:middle}
th{font:bold .74rem Arial,Helvetica,sans-serif;color:var(--navy);text-align:center;background:#f3efe3}th.q{text-align:left}
td.n{width:30px;color:var(--mut)}td.c{text-align:center;width:74px}.dot{display:inline-flex;align-items:center;justify-content:center;line-height:1;width:30px;height:30px;border:1.5px solid var(--navy);border-radius:50%;font:bold .9rem Arial,sans-serif;color:var(--navy)}
.stress{border:1px solid var(--line);border-radius:6px;padding:10px 14px;margin:0 0 14px}.stress .ln{border-bottom:1px solid #999;height:28px}
.score{border:1px solid var(--navy);border-radius:6px;padding:12px 16px;margin:18px 0}.score h3{margin:0 0 6px;color:var(--navy);font-size:1rem}
.score .row{display:flex;gap:18px;flex-wrap:wrap}.score .row span{border-bottom:1px solid #999;min-width:90px;display:inline-block}
.credit{font-size:.78rem;color:var(--mut);margin-top:18px;border-top:1px solid var(--line);padding-top:10px}.credit a{color:var(--mut)}
@media print{body{background:#fff;font-size:12pt}.page{border:0;margin:0;padding:0;max-width:none}.bar{display:none}tr{page-break-inside:avoid}}
@media (max-width:600px){.page{padding:18px 14px;margin:0}.info{grid-template-columns:1fr}td.c{width:auto}.dot{width:26px;height:26px}}`;

function form(inst, file, extra) {
  const head = inst.anchors.map((a) => `<th>${a.value}<br>${esc(a.label)}</th>`).join("");
  let n = 0;
  const groups = inst.groups.map((g) => `<h2>${esc(g.heading)}</h2><p class="note">${esc(g.note)}</p>
<table><thead><tr><th class="q" colspan="2">${esc(extra.lead)}</th>${head}</tr></thead><tbody>
${g.items.map((it) => `<tr><td class="n">${++n}.</td><td>${esc(it.text)}</td>${inst.anchors.map((a) => `<td class="c"><span class="dot">${a.value}</span></td>`).join("")}</tr>`).join("\n")}
</tbody></table>`).join("\n");
  const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(inst.title)} | Belief Counseling</title><style>${CSS}</style></head><body><div class="page">
<div class="brand">Belief Counseling · Spiritual Assessment (optional)</div>
<h1>${esc(inst.title)}</h1><p class="sub">${esc(inst.blurb)}</p>
<div class="bar"><button onclick="window.print()">Print this form</button></div>
<div class="info"><div>Client name or code</div><div>Date</div><div>Counselor</div><div>Session</div></div>
${extra.before}
<div class="box"><b>Instructions.</b> ${extra.useIntro?esc(inst.intro)+" ":""}${esc(extra.howTo)}</div>
${groups}
<div class="score"><h3>Scoring (counselor)</h3><p class="note" style="margin:0 0 8px">${esc(inst.scaleNote)}</p><div class="row">${extra.score}</div></div>
<p class="note"><b>For counselors.</b> ${esc(extra.counselor)}</p>
<div class="credit">${linkify(inst.credit.replace(/ The article’s sentence for the moral item[^.]*\.[^.]*\./, ""))}<br>Form layout © Brian Campbell, Ph.D., Belief Counseling. May be printed for use with clients. Source citation must stay on the form.</div>
</div></body></html>`;
  writeFileSync(new URL(`../counselors/forms/${file}`, import.meta.url), html);
}

form(INSTRUMENTS.rss5, "Belief-Counseling-RSS-5.html", {
  before: "", useIntro: true, lead: "In the past few months, I have…",
  howTo: "Thinking about the past few months, circle the number that shows how much you have had each experience.",
  score: "<span>Total (5–25): &nbsp;</span>",
  counselor: "There is no clinical cutoff. Use the total as a measure of how much the client is struggling spiritually, and talk through any item rated 4 or 5. Each item points to a possible false belief to mine at the Spiritual/Religious level (for example, “God has abandoned me”).",
});

form(INSTRUMENTS.brcope, "Belief-Counseling-Brief-RCOPE.html", {
  useIntro: false, lead: "In dealing with this event, I…",
  before: `<div class="stress"><b>The stressor.</b> Write the one difficult life event these questions are about:<div class="ln"></div><div class="ln"></div></div>`,
  howTo: "Think about the event you wrote above. For each statement, circle the number that shows how much you used that way of coping with this event.",
  score: "<span>Positive coping, items 1–7 (0–21): &nbsp;</span><span>Negative coping, items 8–14 (0–21): &nbsp;</span>",
  counselor: "Keep the two scores separate; do not add them together. A higher negative score (for example, feeling punished or abandoned by God) often points to false beliefs about God worth exploring in the Challenge and Replace steps.",
});
console.log("built");
