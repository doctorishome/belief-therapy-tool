/** Knowledge Library: public teaching notes, plus the counselor's own notes (encrypted in the vault). */

const STOP = new Set("the and for with that this from are was were have has been not but you your about into what when where which while would could should their they them than then just also only more most some any can will may might does did its".split(" "));

export function tokens(s) {
  return (String(s || "").toLowerCase().match(/[a-z][a-z'-]{2,}/g) || []).filter((t) => !STOP.has(t));
}

function windows(text, size) {
  const paras = String(text || "").split(/\n\s*\n/).map((p) => p.trim()).filter(Boolean);
  const out = [];
  let buf = "";
  for (const p of paras) {
    if (buf && (buf.length + p.length) > size) { out.push(buf); buf = p; }
    else buf = buf ? buf + "\n\n" + p : p;
  }
  if (buf) out.push(buf);
  return out.length ? out : [String(text || "").slice(0, size)];
}

export function chunkText(title, text) {
  const raw = String(text || "").trim();
  if (raw.length < 40) return [];
  const headed = raw.split(/\n(?=#{1,3} )/);
  const parts = headed.length > 1 ? headed : windows(raw, 1100);
  return parts.map((part) => {
    const body = part.trim();
    const heading = (/^#{1,3}\s+(.+)/.exec(body) || [])[1] || title;
    const slice = body.length > 1400 ? body.slice(0, 1400).replace(/\s+\S*$/, "") + " …" : body;
    return { title, loc: heading.replace(/\s+/g, " ").slice(0, 120), text: slice };
  }).filter((c) => c.text.length >= 40);
}

export function searchDocs(docs, query, k = 4) {
  const q = [...new Set(tokens(query))];
  if (!q.length) return [];
  const hits = [];
  for (const doc of docs) {
    if (!doc || !doc.text) continue;
    for (const ch of chunkText(doc.title || "Note", doc.text)) {
      const hay = (ch.loc + "\n" + ch.text).toLowerCase();
      let score = 0;
      for (const t of q) if (hay.includes(t)) score++;
      if (score >= (q.length === 1 ? 1 : 2)) hits.push({ ...ch, score });
    }
  }
  hits.sort((a, b) => b.score - a.score);
  const seen = new Set();
  const out = [];
  for (const h of hits) {
    const key = h.title + "|" + h.text.slice(0, 80);
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(h);
    if (out.length >= k) break;
  }
  return out;
}

export function contextFromHits(hits) {
  if (!hits.length) return { text: "", sources: [] };
  const sources = hits.map((h, i) => ({
    n: "S" + (i + 1),
    title: h.title,
    loc: h.loc || "",
    excerpt: h.text.slice(0, 280),
  }));
  const text = hits.map((h, i) => `[S${i + 1}] ${h.title}${h.loc ? " — " + h.loc : ""}\n${h.text}`).join("\n\n");
  return { text, sources };
}

let catalogPromise = null;
const textCache = new Map();

export function loadCatalog() {
  if (!catalogPromise) {
    catalogPromise = fetch("library/catalog.json").then((r) => {
      if (!r.ok) throw new Error("Knowledge Library catalog could not be loaded.");
      return r.json();
    });
  }
  return catalogPromise;
}

export async function loadBundledDoc(item) {
  if (!item.file) return "";
  if (textCache.has(item.file)) return textCache.get(item.file);
  const res = await fetch("library/" + item.file);
  if (!res.ok) throw new Error("Could not read " + item.label);
  const text = await res.text();
  textCache.set(item.file, text);
  return text;
}

export async function bundledSearchDocs() {
  const cat = await loadCatalog();
  const docs = [];
  for (const item of cat.items || []) {
    if (!item.file) continue;
    try {
      docs.push({ title: item.label, text: await loadBundledDoc(item), id: item.bundledId });
    } catch { /* skip a missing file */ }
  }
  return docs;
}
