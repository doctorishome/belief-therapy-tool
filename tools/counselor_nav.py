"""Rewrite the top menu on every Counselors' Room page (counselors/*.html).

The menu has drop-down groups. To add a page, add it to GROUPS below and run:
    python3 tools/counselor_nav.py
Safe to run again: it replaces the menu, its styles and its script each time.

Pages marked <!--standalone--> (a member embed with no menu) are left unchanged.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent / "counselors"

# (label, [(page label, file)]) ; a group with one page is a plain link
GROUPS = [
    ("Welcome", [("Welcome", "welcome.html")]),
    ("Learn", [("The Process", "process.html"),
               ("Theory Topics", "theory.html"),
               ("Professional Tips", "tips.html")]),
    ("Practice", [("Case Studies", "cases.html"),
                  ("The Course", "course.html")]),
    ("Resources", [("Clinical Library", "library.html"),
                   ("Articles", "articles.html"),
                   ("DSM-5-TR Reviews", "reviews.html")]),
]
OUTSIDE = [
    ("False Belief Finder ↗", "https://doctorishome.wixstudio.com/website-6/false-belief-finder"),
    ("Public Site ↗", "https://doctorishome.wixstudio.com/website-6"),
]

CSS = """/*nav*/
.nav .dd{position:relative}
.nav .dd>button{background:none;border:0;border-bottom:2px solid transparent;color:#e9edf5;font:inherit;font-size:.92rem;padding:5px 2px;cursor:pointer}
.nav .dd>button::after{content:" \\25BE";color:var(--gold);font-size:.8em}
.nav .dd>button:hover,.nav .dd.on>button{color:#fff;border-color:var(--gold)}
.nav .menu{display:none;position:absolute;left:-10px;top:100%;min-width:210px;background:#fff;border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:0 0 8px 8px;box-shadow:0 10px 24px rgba(18,40,76,.22);padding:6px 0;z-index:30}
.nav .menu a{display:block;padding:10px 18px;color:var(--navy);text-decoration:none;font-size:.97rem;white-space:nowrap}
.nav .menu a:hover{background:var(--cream)}
.nav .menu a.on{background:var(--cream);font-weight:bold;border-left:3px solid var(--gold);padding-left:15px}
.nav .dd.open .menu{display:block}
@media(hover:hover){.nav .dd:hover .menu{display:block}}
@media(max-width:560px){.nav .dd{position:static}.nav .menu{left:12px;right:12px;min-width:0}.nav .dd>button{font-size:.88rem}}
/*/nav*/"""

JS = """<!--navjs--><script>
document.querySelectorAll('.nav .dd>button').forEach(function(b){
  b.addEventListener('click',function(e){
    e.stopPropagation();var d=b.parentNode,o=!d.classList.contains('open');
    document.querySelectorAll('.nav .dd').forEach(function(x){x.classList.remove('open');x.firstChild.setAttribute('aria-expanded','false');});
    if(o){d.classList.add('open');b.setAttribute('aria-expanded','true');}
  });
});
document.addEventListener('click',function(){document.querySelectorAll('.nav .dd.open').forEach(function(x){x.classList.remove('open');});});
</script><!--/navjs-->"""


def nav(current):
    out = ['<!--nav--><div class="nav"><div class="brand">Belief Counseling<small>For Counselors</small></div>']
    for label, pages in GROUPS:
        if len(pages) == 1:
            t, f = pages[0]
            out.append(f'<a class="l{" on" if f == current else ""}" href="{f}">{t}</a>')
            continue
        here = any(f == current for _, f in pages)
        items = "".join(f'<a{" class=\"on\"" if f == current else ""} href="{f}">{t}</a>' for t, f in pages)
        out.append(f'<div class="dd{" on" if here else ""}"><button type="button" aria-haspopup="true" aria-expanded="false">{label}</button><div class="menu">{items}</div></div>')
    for t, u in OUTSIDE:
        out.append(f'<a class="pub" target="_blank" rel="noopener" href="{u}">{t}</a>')
    out.append('</div><!--/nav-->')
    return "".join(out)


for p in sorted(ROOT.glob("*.html")):
    h = p.read_text(encoding="utf-8")
    if "<!--standalone-->" in h:
        print("menu skipped (standalone):", p.name)
        continue
    if "<!--nav-->" in h:
        h = re.sub(r"<!--nav-->.*?<!--/nav-->", lambda m: nav(p.name), h, flags=re.S)
    else:
        h, n = re.subn(r'<div class="nav">.*?</a></div>', lambda m: nav(p.name), h, count=1, flags=re.S)
        assert n == 1, p
    h = re.sub(r"/\*nav\*/.*?/\*/nav\*/\n?", "", h, flags=re.S)
    h = h.replace("</style>", CSS + "\n</style>", 1)
    h = re.sub(r"<!--navjs-->.*?<!--/navjs-->", "", h, flags=re.S)
    h = h.replace("</body>", JS + "</body>", 1)
    p.write_text(h, encoding="utf-8")
    print("menu updated:", p.name)
