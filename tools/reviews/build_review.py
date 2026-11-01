"""Build a DSM-5-TR teaching overview (Word + PDF) in the same style as the existing reviews.

Each topic folder holds:
  refs.py     REFS list (made by make_refs.py from verified Crossref/PubMed data)
  content.py  TITLE, FILE (pdf base name) and BODY, a list of (kind, text):
              H heading, P paragraph, B bullet, B2 sub-bullet, N numbered item, I italic note.
              In text, **bold** and *italic* work.
Run:  python3 tools/reviews/build_review.py tools/reviews/<topic>
Writes <FILE>.docx in the topic folder and <FILE>.pdf in counselors/reviews/.
"""
import re, sys, subprocess, shutil, pathlib, importlib.util
from docx import Document
from docx.shared import Pt, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH

folder = pathlib.Path(sys.argv[1]).resolve()
ROOT = pathlib.Path(__file__).resolve().parents[2]


def load(name):
    spec = importlib.util.spec_from_file_location(name, folder / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


REFS = load("refs").REFS
C = load("content")
VERIFIED = getattr(C, "VERIFIED", "Saturday, Oct 31, 2026")
SRC = getattr(C, "SOURCES", "Crossref and PubMed")

d = Document()
for s in d.sections:
    s.left_margin = s.right_margin = Inches(0.75); s.top_margin = s.bottom_margin = Inches(0.7)
st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
st.paragraph_format.space_after = Pt(4); st.paragraph_format.line_spacing = 1.05
for nm in ('Title', 'Heading 1', 'Heading 2'):
    s = d.styles[nm]; s.font.name = 'Calibri'
    rf = s.element.rPr.rFonts
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'): rf.set(qn(a), 'Calibri')
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
d.styles['Title'].font.size = Pt(24)
h1 = d.styles['Heading 1']; h1.font.size = Pt(13)
h1.paragraph_format.space_before = Pt(10); h1.paragraph_format.space_after = Pt(2)
for nm in ('List Bullet', 'List Bullet 2', 'List Number'):
    d.styles[nm].paragraph_format.space_after = Pt(2)


def runs(p, text, size=None, italic=False):
    for part in re.split(r'(\*\*.+?\*\*|\*[^*]+?\*)', text):
        if not part: continue
        if part.startswith('**'): r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith('*'): r = p.add_run(part[1:-1]); r.italic = True
        else: r = p.add_run(part)
        if italic: r.italic = True
        if size: r.font.size = Pt(size)
    return p


def link(p, url, text, size):
    h = OxmlElement('w:hyperlink')
    h.set(qn('r:id'), p.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True))
    r = OxmlElement('w:r'); pr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '1F4E79'); pr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); pr.append(u)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size * 2))); pr.append(sz)
    r.append(pr); t = OxmlElement('w:t'); t.text = text; r.append(t); h.append(r); p._p.append(h)


d.add_paragraph(C.TITLE, style='Title')
runs(d.add_paragraph(), 'Clinical Companion Knowledge Library: for counselors and counseling students', italic=True)
STY = {'P': None, 'B': 'List Bullet', 'B2': 'List Bullet 2', 'N': 'List Number'}
LINK_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')


def cell_text(p, text, size, bold=False, color=None):
    pos = 0
    for m in LINK_RE.finditer(text):
        if m.start() > pos:
            runs(p, text[pos:m.start()], size=size)
        link(p, m.group(2), m.group(1), size)
        pos = m.end()
    if pos < len(text):
        runs(p, text[pos:], size=size)
    if bold or color:
        for r in p.runs:
            if bold: r.bold = True
            if color: r.font.color.rgb = color


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hexcolor); tcPr.append(sh)


def add_table(spec):
    from docx.shared import RGBColor
    cols, rows, widths = spec['cols'], spec['rows'], spec['widths']
    t = d.add_table(rows=1 + len(rows), cols=len(cols)); t.style = 'Table Grid'; t.autofit = False
    SZ = spec.get('size', 8.5)
    for i, row in enumerate([cols] + rows):
        for j, val in enumerate(row):
            c = t.cell(i, j); c.width = Inches(widths[j])
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
            if i == 0:
                shade(c, '1F3864'); cell_text(p, val, SZ, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
            else:
                if i % 2 == 0: shade(c, 'EEF2F8')
                cell_text(p, val, SZ)
    # fixed column widths (LibreOffice needs the grid and table width)
    tblPr = t._tbl.tblPr
    tw = OxmlElement('w:tblW'); tw.set(qn('w:w'), str(int(sum(widths) * 1440))); tw.set(qn('w:type'), 'dxa')
    for old in tblPr.findall(qn('w:tblW')): tblPr.remove(old)
    tblPr.append(tw)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    for gc, wv in zip(t._tbl.tblGrid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(int(wv * 1440)))
    for row in t.rows:
        trPr = row._tr.get_or_add_trPr(); cs = OxmlElement('w:cantSplit'); cs.set(qn('w:val'), 'true'); trPr.append(cs)
    # repeat header row on each page
    trPr = t.rows[0]._tr.get_or_add_trPr(); h = OxmlElement('w:tblHeader'); h.set(qn('w:val'), 'true'); trPr.append(h)
    for note in spec.get('notes', []):
        p = d.add_paragraph(); p.paragraph_format.space_before = Pt(3); cell_text(p, note, 8.5)


for kind, text in C.BODY:
    if kind == 'H':
        d.add_heading(text, level=1)
    elif kind == 'H2':
        h = d.add_heading(text, level=2)
        for r in h.runs: r.font.name = 'Calibri'; r.font.size = Pt(11.5)
    elif kind == 'NI':
        num, body = text.split('|', 1)
        p = d.add_paragraph(); pf = p.paragraph_format
        pf.left_indent = Inches(0.6); pf.first_line_indent = Inches(-0.25); pf.space_after = Pt(1)
        runs(p, num + '.\t' + body)
        pf.tab_stops.add_tab_stop(Inches(0.6))
    elif kind == 'T':
        add_table(text)
    elif kind == 'I':
        runs(d.add_paragraph(), text, italic=True)
    else:
        runs(d.add_paragraph(style=STY[kind]), text)

n = len(REFS)
d.add_heading('Sources note', level=1)
if hasattr(C, 'SOURCES_NOTE'):
    runs(d.add_paragraph(), C.SOURCES_NOTE)
else:
  runs(d.add_paragraph(), f'All {n} references were checked against {SRC} ({VERIFIED.split(", ", 1)[1]}), and the figures quoted were checked against each study’s abstract. Each DOI is a live link to the publisher record.')
d.add_heading('References', level=1)
S = 8.5
for _, au, yr, ti, jo, vo, iss, pg, doi in REFS:
    p = d.add_paragraph(); pf = p.paragraph_format
    pf.left_indent = Inches(0.35); pf.first_line_indent = Inches(-0.35); pf.space_after = Pt(2); pf.line_spacing = 1.0
    r = p.add_run(f'{au} ({yr}). '); r.font.size = Pt(S)
    if jo is None:
        r = p.add_run(ti + '. '); r.italic = True; r.font.size = Pt(S)
    else:
        end = ti[-1] in '?!'
        r = p.add_run(ti + ('' if end else '.') + ' '); r.font.size = Pt(S)
        r = p.add_run(jo + (', ' + vo if vo else '')); r.italic = True; r.font.size = Pt(S)
        r = p.add_run((f'({iss})' if iss else '') + (f', {pg}' if pg else '') + '. '); r.font.size = Pt(S)
    link(p, 'https://doi.org/' + doi, 'https://doi.org/' + doi, S)
runs(d.add_paragraph(), getattr(C, 'FINAL_NOTE', f'Prepared for Clinical Companion (Brian Campbell). Teaching overview only. Clinically review before use. Not a substitute for the DSM-5-TR or clinical judgment. All {n} references and DOIs verified via {SRC} ({VERIFIED}). Effect sizes as reported in the cited sources.'), size=8, italic=True)
for s in d.sections:
    fp = s.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run(); f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin'); r._r.append(f1)
    it = OxmlElement('w:instrText'); it.text = 'PAGE'; r._r.append(it)
    f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'end'); r._r.append(f2); r.font.size = Pt(9)

docx = folder / f'{C.FILE}.docx'
d.save(docx)
out = ROOT / 'counselors' / 'reviews'
subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', str(folder), str(docx)],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
shutil.move(str(folder / f'{C.FILE}.pdf'), out / f'{C.FILE}.pdf')
pages = subprocess.run(['pdfinfo', str(out / f'{C.FILE}.pdf')], capture_output=True, text=True).stdout
print([l for l in pages.splitlines() if l.startswith('Pages')][0], '->', out / f'{C.FILE}.pdf')
