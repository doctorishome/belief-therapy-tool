"""Turn a review .docx made by build_review.py back into content.py (used when content.py was lost)."""
import sys, pathlib
from docx import Document
src, out, file_base = sys.argv[1], sys.argv[2], sys.argv[3]
d = Document(src)
MAP = {'Normal': 'P', 'List Bullet': 'B', 'List Bullet 2': 'B2', 'List Number': 'N', 'Heading 1': 'H', 'Heading 2': 'H2'}
def text(p):
    s = ''
    for r in p.runs:
        t = r.text
        if not t: continue
        if r.bold and t.strip(): s += '**' + t + '**'
        elif r.italic and t.strip() and not all(x.italic for x in p.runs): s += '*' + t + '*'
        else: s += t
    return s.replace('****', '')
paras = d.paragraphs
title = paras[0].text
body, sources, final, mode = [], None, None, 'body'
for p in paras[2:]:
    st = p.style.name
    if st == 'Heading 1' and p.text.strip() == 'Sources note': mode = 'src'; continue
    if st == 'Heading 1' and p.text.strip() == 'References': mode = 'refs'; continue
    if mode == 'src':
        sources = p.text; mode = 'skip'; continue
    if mode in ('refs', 'skip'):
        if p.text.startswith('Prepared for'): final = p.text
        continue
    if not p.text.strip(): continue
    kind = MAP[st]
    t = text(p)
    if kind == 'P' and all(r.italic for r in p.runs if r.text.strip()): kind, t = 'I', p.text
    body.append((kind, t))
with open(out, 'w') as o:
    o.write(f'TITLE = {title!r}\nFILE = {file_base!r}\nSOURCES_NOTE = {sources!r}\nFINAL_NOTE = {final!r}\nBODY = [\n')
    for k, t in body: o.write(f'({k!r}, {t!r}),\n')
    o.write(']\n')
print(len(body), 'items')
