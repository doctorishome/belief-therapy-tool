#!/usr/bin/env python3
"""Build printable web-page worksheets from worksheets/worksheets.json.

Each worksheet becomes worksheets/<key>.html: same look as Life_Events_Beliefs_Screening.html
(logo, gold border, two columns, check boxes and note lines you can fill in on screen,
"Print this form" button, prints on two letter pages). Web pages open even where a
browser add-on blocks PDF files.

Usage:  python3 tools/build_worksheets.py
To change wording: edit worksheets/worksheets.json, run this, commit and push.
"""
import html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "worksheets" / "worksheets.json"
OUT = ROOT / "worksheets"
FIRST_PAGE_SECTIONS = 4

CSS = """
  :root{--ink:#2f4357;--gold:#b08a4b;--goldtext:#a8742e;--line:#c9b48a;--body:#2b2b2b}
  *{box-sizing:border-box}
  html,body{margin:0;background:#f4f1ea;color:var(--body);font-family:Georgia,"Times New Roman",serif}
  .bar{max-width:8.5in;margin:16px auto 0;display:flex;gap:10px;justify-content:center;flex-wrap:wrap;padding:0 16px}
  .bar button{font-family:inherit;font-size:16px;padding:10px 22px;border-radius:6px;cursor:pointer;border:1px solid var(--ink)}
  .bar .print{background:var(--ink);color:#fff}
  .bar .clear{background:#fff;color:var(--ink)}
  .tip{max-width:8.5in;margin:8px auto 0;text-align:center;font-size:14px;color:#6b6250;padding:0 16px}
  .page{max-width:8.5in;margin:16px auto 24px;background:#fff;border:1.5px solid var(--gold);padding:.45in .5in .5in;box-shadow:0 2px 10px rgba(0,0,0,.06)}
  .page + .page{margin-top:0}
  header{text-align:center}
  header img{width:78px;height:auto}
  h1{font-size:26px;color:var(--ink);margin:6px 0 2px}
  .sub{font-style:italic;color:var(--goldtext);font-size:14px;margin:0}
  .who{display:flex;gap:24px;margin:18px 0 6px;font-size:14px;font-weight:700}
  .who label{display:flex;align-items:flex-end;gap:6px}
  .who .name{flex:1}
  .who input{flex:1;border:0;border-bottom:1px solid #555;font:inherit;font-weight:400;padding:2px 4px;min-width:120px;background:transparent}
  .grid{display:grid;grid-template-columns:1fr 1fr;column-gap:28px;row-gap:26px;margin-top:16px}
  section h2{font-size:17px;color:var(--ink);margin:0 0 8px;padding-bottom:4px;border-bottom:1.5px solid var(--line)}
  .item{display:flex;align-items:flex-start;gap:6px;font-size:14px;line-height:1.35;margin:5px 0;cursor:pointer}
  .item input{margin:3px 0 0;width:15px;height:15px;flex:none;accent-color:var(--ink)}
  .note{font-style:italic;color:var(--goldtext);font-size:12.5px;margin:10px 0 4px}
  textarea{width:100%;min-height:80px;font:14px/26px Georgia,serif;border:0;resize:vertical;padding:0 2px;
    background:repeating-linear-gradient(to bottom,transparent 0,transparent 25px,#999 25px,#999 26px);}
  .closing{margin-top:26px;text-align:center;font-size:14px;line-height:1.5;color:#3d3a35}
  .verse{margin-top:12px;font-style:italic;color:var(--ink);font-size:15px}
  .ref{font-size:13px;color:var(--goldtext);margin-top:2px}
  .extra{margin-top:14px;font-size:13px;color:#3d3a35}
  footer{margin-top:20px;text-align:center;font-size:13px;color:#555;font-style:italic}
  .pgno{text-align:right;font-size:12px;color:#777;margin-bottom:10px}
  @media (max-width:640px){
    .page{padding:20px 16px;border-left:0;border-right:0}
    .grid{grid-template-columns:1fr}
    .who{flex-direction:column;gap:12px}
  }
  @media print{
    @page{size:letter;margin:.35in}
    html,body{background:#fff}
    .bar,.tip{display:none}
    .page{box-shadow:none;margin:0;width:100%;max-width:100%;padding:.3in .4in;border:1.5px solid var(--gold);page-break-after:always;break-after:page}
    .page:last-child{page-break-after:auto;break-after:auto}
    header img{width:58px}
    h1{font-size:22px}
    .who{margin:10px 0 4px}
    .grid{grid-template-columns:1fr 1fr;row-gap:14px;margin-top:8px}
    section h2{font-size:15px;margin-bottom:4px}
    .item{font-size:12.5px;margin:2px 0}
    .note{margin:6px 0 2px}
    textarea{resize:none;min-height:54px}
    section{break-inside:avoid}
    .closing{margin-top:16px;font-size:12.5px}
  }
"""

SCRIPT = """
<script>
  function clearForm(){
    if(!confirm('Clear all checked boxes and notes on this page?')) return;
    document.querySelectorAll('input[type=checkbox]').forEach(function(c){c.checked=false;});
    document.querySelectorAll('input[type=text],textarea').forEach(function(t){t.value='';});
  }
</script>"""

e = html.escape


def section_html(s):
    items = "\n".join(
        f'        <label class="item"><input type="checkbox">{e(i)}</label>' for i in s["items"])
    return (f'      <section>\n        <h2>{e(s["h"])}</h2>\n{items}\n'
            f'        <p class="note">{e(s["p"])}</p>\n'
            f'        <textarea aria-label="{e(s["h"])} notes"></textarea>\n      </section>')


def grids(sections):
    """Two sections per row; each row is its own grid so rows never split across printed pages."""
    rows = [sections[i:i + 2] for i in range(0, len(sections), 2)]
    return "\n".join('    <div class="grid">\n' + "\n".join(section_html(s) for s in r) + "\n    </div>"
                     for r in rows)


def build(key, w):
    first, rest = w["sections"][:FIRST_PAGE_SECTIONS], w["sections"][FIRST_PAGE_SECTIONS:]
    extra = "".join(f"<div>{e(x)}</div>" for x in w.get("extra", []))
    closing = (f'    <div class="closing">\n      <p>{e(w["note"])}</p>\n'
               f'      <div class="verse">{e(w["verse"])}</div>\n      <div class="ref">{e(w["ref"])}</div>\n'
               + (f'      <div class="extra">{extra}</div>\n' if extra else "") + "    </div>")
    footer = ("    <footer>Thank you — this helps your counselor understand the beliefs behind what you’re "
              "experiencing. Your answers are confidential within your counseling relationship.</footer>")
    page2 = (f'  <div class="page">\n    <div class="pgno">Page 2</div>\n{grids(rest)}\n{closing}\n{footer}\n  </div>'
             if rest else "")
    page1_tail = "" if rest else f"\n{closing}\n{footer}"
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(w["title"])} | Belief Counseling</title>
<style>{CSS}</style>
</head>
<body>
  <div class="bar">
    <button class="print" onclick="window.print()">Print this form</button>
    <button class="clear" onclick="clearForm()">Clear my answers</button>
  </div>
  <p class="tip">You can check boxes and type notes right on this page before printing, or print it blank and fill it in by hand.</p>

  <div class="page">
    <header>
      <img src="../belief-counseling-logo.png" alt="Belief Counseling">
      <h1>{e(w["title"])}</h1>
      <p class="sub">{e(w["intro"])}</p>
    </header>
    <div class="who">
      <label class="name">Name: <input type="text" aria-label="Name"></label>
      <label>Date: <input type="text" aria-label="Date"></label>
    </div>
{grids(first)}{page1_tail}
  </div>
{page2}
{SCRIPT}
</body>
</html>
"""
    (OUT / f"{key}.html").write_text(doc, encoding="utf-8")
    return OUT / f"{key}.html"


if __name__ == "__main__":
    data = json.loads(DATA.read_text(encoding="utf-8"))
    for k, w in data.items():
        print("built", build(k, w).relative_to(ROOT))
