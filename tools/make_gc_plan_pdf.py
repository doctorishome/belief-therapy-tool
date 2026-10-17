"""Makes the printable review list of suggested Godly Counsel Lessons for all 120 cards.
Usage: python3 tools/make_gc_plan_pdf.py <output.pdf>   (reads tools/godly-counsel-plan.json)"""
import json, glob, re, os, sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
T = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(T, 'gc_fonts')
pdfmetrics.registerFont(TTFont('Corm', F + '/Cormorant-SemiBold.ttf'))
pdfmetrics.registerFont(TTFont('Serif', F + '/SourceSerif4-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SerifI', F + '/SourceSerif4-Italic.ttf'))
NAVY, GOLD, LINE, SOFT = HexColor('#1F3A5F'), HexColor('#B08A4B'), HexColor('#E4D9C6'), HexColor('#F7F2E8')
plan = json.load(open(os.path.join(T, 'godly-counsel-plan.json')))
ch = json.load(open(os.path.join(T, 'godly-counsel-chapters.json'), encoding='utf-8'))
beliefs, groups = {}, {}
for f in glob.glob(os.path.join(T, 'cards', '*.json')):
    d = json.load(open(f, encoding='utf-8')); beliefs[d['num']] = d['belief']; groups[d['num']] = d['group']
for line in open(os.path.join(T, '..', 'PROGRESS.md'), encoding='utf-8'):
    m = re.match(r'\| ([1-5]) \| (.+?) \|', line)
    if m: beliefs[int(m.group(1))] = m.group(2); groups[int(m.group(1))] = 'God'
t = ParagraphStyle('t', fontName='Corm', fontSize=24, textColor=NAVY, leading=28)
sub = ParagraphStyle('s', fontName='Serif', fontSize=9.5, leading=13.5, textColor=HexColor('#2D2A26'))
cell = ParagraphStyle('c', fontName='Serif', fontSize=9, leading=11.5)
cellI = ParagraphStyle('ci', parent=cell, fontName='SerifI', textColor=NAVY)
gh = ParagraphStyle('g', fontName='Corm', fontSize=14, textColor=NAVY, leading=17)
story = [Paragraph('Godly Counsel Lessons for the 120 Belief Cards', t), Spacer(1, 4),
         Paragraph('Suggested lessons to list under &ldquo;Related Pearls topics&rdquo; on each Spiritual/Religious Belief Card. '
                   'The best fit is listed first. Cross out any you don&rsquo;t want and write in any you would add. Card 43 is already done.', sub),
         Spacer(1, 10)]
rows, styles, cur = [], [], None
for n in range(1, 121):
    if groups[n] != cur:
        cur = groups[n]; rows.append([Paragraph(cur, gh), '', '', '']); r = len(rows) - 1
        styles += [('SPAN', (0, r), (-1, r)), ('LINEBELOW', (0, r), (-1, r), 0.8, GOLD), ('TOPPADDING', (0, r), (-1, r), 10)]
    les = '<br/>'.join(ch[str(x)][0] for x in plan[str(n)])
    rows.append([Paragraph(str(n), cell), Paragraph(beliefs[n], cell), Paragraph(les, cellI),
                 Paragraph('&#9744; OK' if n != 43 else 'Done', cell)])
    if n % 2 == 0: styles.append(('BACKGROUND', (0, len(rows) - 1), (-1, len(rows) - 1), SOFT))
tb = Table(rows, colWidths=[24, 262, 150, 44])
tb.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('TOPPADDING', (0, 0), (-1, -1), 4),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('LINEBELOW', (0, 0), (-1, -1), 0.3, LINE)] + styles))
story.append(tb)
def foot(c, d):
    c.saveState(); c.setFont('SerifI', 8); c.setFillColor(NAVY)
    c.drawString(66, 36, 'Godly Counsel Lessons for the Belief Cards · proposal for review')
    c.drawRightString(546, 36, 'Page %d' % d.page); c.restoreState()
SimpleDocTemplate(sys.argv[1], pagesize=letter, leftMargin=66, rightMargin=66, topMargin=54, bottomMargin=58,
                  title='Godly Counsel Lessons for the Belief Cards', author='Dr. Brian Campbell').build(story, onFirstPage=foot, onLaterPages=foot)
print('saved', sys.argv[1])
