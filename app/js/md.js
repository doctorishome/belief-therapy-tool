/** Tiny Markdown to HTML. Escapes HTML first. */

export function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function inline(s) {
  s = esc(s);
  s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/(^|[^*])\*([^*\s][^*]*)\*/g, "$1<em>$2</em>");
  return s;
}

export function render(md) {
  const lines = String(md || "").replace(/\r/g, "").split("\n");
  const out = [];
  let list = null;
  let para = [];
  const flushPara = () => {
    if (para.length) { out.push("<p>" + para.map(inline).join("<br>") + "</p>"); para = []; }
  };
  const closeList = () => { if (list) { out.push("</" + list + ">"); list = null; } };
  for (const line of lines) {
    let m;
    if (!line.trim()) { flushPara(); closeList(); continue; }
    if ((m = /^\s*(#{1,6})\s+(.*)$/.exec(line))) {
      flushPara(); closeList();
      const n = Math.min(4, m[1].length + 1);
      out.push(`<h${n}>${inline(m[2])}</h${n}>`);
      continue;
    }
    if (/^\s*(-{3,}|\*{3,})\s*$/.test(line)) { flushPara(); closeList(); out.push("<hr>"); continue; }
    if ((m = /^\s*[-*•]\s+(.*)$/.exec(line))) {
      flushPara();
      if (list !== "ul") { closeList(); out.push("<ul>"); list = "ul"; }
      out.push("<li>" + inline(m[1]) + "</li>");
      continue;
    }
    if ((m = /^\s*\d+[.)]\s+(.*)$/.exec(line))) {
      flushPara();
      if (list !== "ol") { closeList(); out.push("<ol>"); list = "ol"; }
      out.push("<li>" + inline(m[1]) + "</li>");
      continue;
    }
    closeList();
    para.push(line);
  }
  flushPara();
  closeList();
  return out.join("\n");
}

export function toPlain(md) {
  return String(md || "")
    .replace(/\r/g, "")
    .replace(/^\s*#{1,6}\s+/gm, "")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/^\s*[*•]\s+/gm, "- ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}
