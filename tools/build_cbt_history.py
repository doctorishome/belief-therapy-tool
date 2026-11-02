"""Builds counselors/theory/From-CBT-to-Christian-CBT.docx (and .pdf) from the article XML
exported from the Claude Doc. Usage: python3 build_cbt_history.py <article.xml>"""
import sys, os, re, subprocess, xml.etree.ElementTree as ET
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'counselors', 'theory')
NAVY, GOLD, MUTED = RGBColor(0x12, 0x28, 0x4C), RGBColor(0xC9, 0xA2, 0x27), RGBColor(0x5B, 0x66, 0x78)

tree = ET.fromstring(open(sys.argv[1]).read())
d = Document()
sec = d.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for a in ('left_margin', 'right_margin'): setattr(sec, a, Inches(1))
sec.top_margin = sec.bottom_margin = Inches(0.9)
st = d.styles['Normal']; st.font.name = 'Georgia'; st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Georgia')
st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.15
for lvl, size in ((1, 20), (2, 14)):
    h = d.styles[f'Heading {lvl}']; h.font.name = 'Georgia'; h.font.size = Pt(size); h.font.bold = True
    h.font.color.rgb = NAVY; h.element.rPr.rFonts.set(qn('w:asciiTheme'), 'Georgia') if False else None
    rf = h.element.rPr.rFonts
    for k in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'): rf.set(qn(k), 'Georgia')
    for k in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(k)) is not None: del rf.attrib[qn(k)]
    h.paragraph_format.space_before = Pt(14 if lvl == 2 else 0); h.paragraph_format.space_after = Pt(4)


def border_bottom(p, color='C9A227', sz=12):
    pPr = p._p.get_or_add_pPr(); b = OxmlElement('w:pBdr'); e = OxmlElement('w:bottom')
    for k, v in (('val', 'single'), ('sz', str(sz)), ('space', '4'), ('color', color)): e.set(qn('w:' + k), v)
    b.append(e); pPr.append(b)


def link(p, url, text, size=None):
    rid = p.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
    r = OxmlElement('w:r'); pr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '1F4E9A'); pr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); pr.append(u)
    if size:
        s = OxmlElement('w:sz'); s.set(qn('w:val'), str(int(size * 2))); pr.append(s)
    r.append(pr); t = OxmlElement('w:t'); t.text = text; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); p._p.append(h)


def fill(p, node, size=None):
    for t in node.findall('text'):
        ln = t.find('link')
        if ln is not None:
            link(p, ln.get('href'), ln.text, size); continue
        b, i = t.find('bold'), t.find('italic')
        txt = (b if b is not None else i if i is not None else t)
        r = p.add_run(''.join(txt.itertext()))
        r.bold = b is not None; r.italic = i is not None
        if size: r.font.size = Pt(size)


# Header block: logo, title, byline
logo = os.path.join(ROOT, 'belief-counseling-logo.png')
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run().add_picture(logo, width=Inches(0.75))
kids = list(tree)
title = ''.join(kids[0].itertext())
p = d.add_paragraph(style='Heading 1'); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.add_run(title)
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
r = p.add_run('Brian Campbell, Ph.D.'); r.bold = True; r.font.color.rgb = NAVY
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Prepared with AI research and drafting assistance; content directed, reviewed, and approved by the author. '
              '© 2026 Brian Campbell, Ph.D. All rights reserved.')
r.italic = True; r.font.size = Pt(8.5); r.font.color.rgb = MUTED
border_bottom(p)

in_refs = False
for n in kids[2:]:  # skip title and date/mention line
    if n.tag == 'paragraph':
        if n.get('heading'):
            txt = ''.join(n.itertext()); in_refs = txt == 'References'
            d.add_paragraph(txt, style='Heading 2'); continue
        if in_refs and n.find('text/link') is None and 'checked against' in ''.join(n.itertext()):
            p = d.add_paragraph(); fill(p, n, 9); p.runs[0].italic = True; continue
        p = d.add_paragraph()
        if in_refs:
            pf = p.paragraph_format; pf.left_indent = Inches(0.35); pf.first_line_indent = Inches(-0.35)
            pf.space_after = Pt(3); pf.line_spacing = 1.0
            fill(p, n, 9.5)
        else:
            fill(p, n)
    elif n.tag == 'list':
        style = 'List Number' if n.get('kind') == 'ordered' else 'List Bullet'
        for li in n.findall('listItem'):
            p = d.add_paragraph(style=style); p.paragraph_format.space_after = Pt(4)
            fill(p, li.find('paragraph'))

# Footer
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run('© 2026 Brian Campbell, Ph.D. All rights reserved. · Page '); r.font.size = Pt(8); r.font.color.rgb = MUTED
r = fp.add_run(); r.font.size = Pt(8); r.font.color.rgb = MUTED
for tag, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
    if tag:
        f = OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'), tag); r._r.append(f)
    else:
        it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = txt; r._r.append(it)

d.core_properties.author = 'Brian Campbell, Ph.D.'; d.core_properties.title = title
os.makedirs(OUT, exist_ok=True)
docx_path = os.path.join(OUT, 'From-CBT-to-Christian-CBT.docx')
d.save(docx_path)
subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', OUT, docx_path], check=True, capture_output=True)
print(docx_path)
