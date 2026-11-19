"""Make a web page for each DSM-5-TR teaching review, in the Counselors' Room style.

Source: the .docx in each topic folder (the same file that made the PDF), converted with pandoc.
Writes counselors/reviews/<file>.html next to <file>.pdf. The page has the room menu, a Back button,
and a link to the PDF. Run after build_review.py:  python3 tools/reviews/build_review_html.py [topic ...]
"""
import re, sys, glob, pathlib, subprocess, importlib.util, html
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'counselors' / 'reviews'
helpp = (ROOT / 'counselors' / 'help.html').read_text()
NAV = re.search(r'<!--nav-->.*?<!--/nav-->', helpp, re.S).group(0)
NAV = NAV.replace('href="../', 'href="../../')  # pages live one folder deeper
NAV = NAV.replace('<a class="l" href="../../members/assessment.html">', '<a class="l on" href="../../members/assessment.html">')
NAVCSS = re.search(r'<style>(.*?)</style>', helpp, re.S).group(1)
NAVCSS = '\n'.join(l for l in re.findall(r'[^{}]+\{[^{}]*\}|@media[^{]*\{(?:[^{}]*\{[^{}]*\})*\s*\}', NAVCSS)
                   if l.strip().startswith(('.nav', '.brand', ':root', '@media')))
NAVJS = re.search(r'<!--navjs-->.*?<!--/navjs-->', helpp, re.S)
NAVJS = NAVJS.group(0) if NAVJS else ''

CSS = """
:root{--navy:#12284c;--navy2:#1d3a6b;--gold:#c9a227;--cream:#faf6ec;--ink:#1f2a3a;--mut:#5b6678;--line:#e3dcc6}
*{box-sizing:border-box}
body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--ink);background:var(--cream);line-height:1.65}
a{color:var(--navy2)}
.hero{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;padding:46px 22px 40px;text-align:center}
.hero .eyebrow{color:var(--gold);letter-spacing:2px;text-transform:uppercase;font-size:.78rem;margin-bottom:10px}
.hero h1{font-size:clamp(1.7rem,4.2vw,2.6rem);margin:0 0 10px;line-height:1.2}
.hero p{max-width:760px;margin:4px auto 0;color:#dfe6f2;font-size:1rem}
.hero .by{font-size:1.05rem;color:#fff;margin-top:12px}
.hero .ai{font-size:.85rem;font-style:italic;color:#c8d1e0}
.tools{max-width:960px;margin:0 auto;padding:22px 20px 0;display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.btn{display:inline-block;background:var(--gold);color:var(--navy);font-weight:bold;text-decoration:none;padding:9px 20px;border-radius:24px;border:0;font:inherit;font-weight:bold;cursor:pointer}
.btn.ghost{background:#fff;border:1px solid var(--navy);color:var(--navy)}
.paper{max-width:960px;margin:16px auto 0;background:#fff;border:1px solid var(--line);border-top:4px solid var(--gold);border-radius:8px;padding:10px 34px 30px;box-shadow:0 2px 8px rgba(18,40,76,.06)}
.paper h1{color:var(--navy);font-size:1.45rem;margin:30px 0 10px;border-bottom:2px solid var(--gold);padding-bottom:6px}
.paper h2{color:var(--navy);font-size:1.15rem;margin:22px 0 6px}
.paper p{margin:8px 0}
.paper li{margin:4px 0}.paper li p{margin:0}
.paper strong{color:var(--navy)}
.paper table{border-collapse:collapse;width:100%;margin:12px 0;font-size:.9rem;display:block;overflow-x:auto}
.paper th{background:var(--navy);color:#fff;text-align:left;padding:8px 10px;border:1px solid var(--navy)}
.paper th strong,.paper th a{color:#fff}
.paper td{padding:7px 10px;border:1px solid var(--line);vertical-align:top}
.paper tr:nth-child(even) td{background:#f7f3e8}
.paper td p,.paper th p{margin:0}
.paper .refs p{font-size:.88rem;padding-left:2em;text-indent:-2em;margin:6px 0;word-break:break-word}
.paper .final{font-size:.85rem;color:var(--mut);font-style:italic;margin-top:18px}
.foot{margin:34px 0 0;padding:20px;text-align:center;color:#c8d1e0;background:var(--navy);font-size:.85rem}.foot a{color:var(--gold)}
@media(max-width:620px){.paper{padding:6px 16px 22px;border-radius:0}}
@media print{.nav,.tools,.foot{display:none}.hero{background:none;color:var(--navy);padding:10px}.hero p,.hero .by,.hero .ai{color:var(--ink)}.paper{border:0;box-shadow:none}}
"""

BACK = """<script>(function(){var b=document.getElementById('back');b.addEventListener('click',function(e){
try{var r=document.referrer;if(r&&new URL(r).host===location.host&&history.length>1){e.preventDefault();history.back();}}catch(x){}});
try{if(window.top!==window&&document.referrer&&new URL(document.referrer).host===location.host){document.body.firstElementChild.scrollIntoView({block:'start'});}}catch(e){}})();</script>"""


def load(folder):
    spec = importlib.util.spec_from_file_location('c', folder / 'content.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def build(folder):
    C = load(folder)
    docx = folder / f'{C.FILE}.docx'
    body = subprocess.run(['pandoc', str(docx), '-t', 'html', '--wrap=none'], capture_output=True, text=True, check=True).stdout
    # drop the byline paragraphs (shown in the page header instead)
    for pat in [r'<p><em>Clinical Companion Knowledge Library[^<]*</em></p>\s*', r'<p><strong>Brian Campbell, Ph\.D\.</strong></p>\s*',
                r'<p><em>Prepared with AI research[^<]*</em></p>\s*']:
        body = re.sub(pat, '', body, count=1)
    body = re.sub(r'<a href="(https?://[^"]+)"', r'<a target="_blank" rel="noopener" href="\1"', body)
    # references block
    i = body.find('id="references"')
    if i > 0:
        j = body.find('</h1>', i) + 5
        body = body[:j] + '<div class="refs">' + body[j:] + '</div>'
        body = re.sub(r'(<p><em>Prepared for Clinical Companion.*?</p>)</div>$', r'</div><p class="final">\1</p>', body.strip(), flags=re.S)
    title = re.sub(r'(\s*\(DSM-5-TR\))?:\s*Teaching Overview\s*$', '', C.TITLE)
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · DSM-5-TR Teaching Review</title>
<style>{NAVCSS}
{CSS}</style></head><body>{NAV}
<div class="hero"><div class="eyebrow">DSM-5-TR Teaching Review</div><h1>{html.escape(title)}</h1>
<p>Clinical Companion Knowledge Library: for counselors and counseling students</p>
<p class="by">Brian Campbell, Ph.D.</p>
<p class="ai">Prepared with AI research and drafting assistance; content directed, reviewed, and approved by the author. © 2026 Brian Campbell, Ph.D. All rights reserved.</p></div>
<div class="tools"><a class="btn" id="back" href="../../members/assessment.html#rvlist">&#8592; Back</a><a class="btn ghost" href="{C.FILE}.pdf" target="_blank" rel="noopener">Download or print the PDF</a></div>
<div class="paper">
{body}
</div>
<div class="tools" style="padding-bottom:6px"><a class="btn" href="../../members/assessment.html#rvlist" onclick="try{{if(document.referrer&&new URL(document.referrer).host===location.host&&history.length>1){{history.back();return false;}}}}catch(e){{}}">&#8592; Back</a></div>
<div class="foot">Teaching overview for counselors. Not a substitute for the DSM-5-TR or clinical judgment. · © Brian Campbell, Ph.D. · <a href="https://www.beliefcounselor.com/help" target="_top">Help &amp; Support</a></div>
{BACK}{NAVJS}</body></html>
"""
    (OUT / f'{C.FILE}.html').write_text(page)
    return C.FILE, title


if __name__ == '__main__':
    names = sys.argv[1:] or sorted(p.parent.name for p in (ROOT / 'tools' / 'reviews').glob('*/content.py'))
    for n in names:
        print(*build(ROOT / 'tools' / 'reviews' / n))
