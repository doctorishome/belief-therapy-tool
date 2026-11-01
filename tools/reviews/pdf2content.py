"""Recover content.py (text, bold/italic, headings, lists, raw references) from a review PDF
whose Word source was lost. Usage: python3 pdf2content.py in.pdf out_content.py file_base"""
import sys, re, pdfplumber
src, out, base = sys.argv[1:4]
pdf = pdfplumber.open(src)

def style(fn):
    return ('b' if 'Bold' in fn else '') + ('i' if 'Italic' in fn else '')

lines = []
for pno, pg in enumerate(pdf.pages):
    words = pg.extract_words(extra_attrs=['fontname', 'size', 'non_stroking_color'], keep_blank_chars=False, use_text_flow=True)
    # group words into lines by 'top'
    cur = []
    for w in words:
        if cur and abs(w['top'] - cur[-1]['top']) > 2:
            lines.append((pno, cur)); cur = []
        cur.append(w)
    if cur: lines.append((pno, cur))

def line_text(ws):
    parts, prev = [], None
    for w in ws:
        t = w['text']
        if t in ('', '•', '', '◦', '▪'): continue
        st = style(w['fontname'])
        sp = '' if prev is None else ('' if w['x0'] - prev['x1'] < 0.8 else ' ')
        parts.append((sp, t, st)); prev = w
    return parts

LM = min(round(ws[0]['x0']) for _, ws in lines)
items, cur = [], None   # item: dict(kind, parts, x, bottom, page)
title = []
mode = 'body'; raw_refs = []; sources = []; final = []
for idx, (pno, ws) in enumerate(lines):
    first = ws[0]; size = round(first['size']); x0 = round(first['x0']); top = first['top']
    txt = ' '.join(w['text'] for w in ws).strip()
    col = first['non_stroking_color'] or (0,)
    if re.fullmatch(r'\d+', txt) and top > 700: continue          # page number
    if size >= 20: title.append(txt); continue
    if idx < 4 and 'Clinical Companion Knowledge Library' in txt: continue
    is_head = size >= 12 and 'Bold' in first['fontname'] and isinstance(col, tuple) and len(col) == 3 and col[2] > 0.4
    if is_head:
        cur = None
        if txt == 'Sources note': mode = 'src'; continue
        if txt == 'References': mode = 'refs'; continue
        items.append({'kind': 'H' if size >= 14 else 'H2', 'parts': [(a, b, '') for a, b, _ in line_text(ws)], 'x': x0, 'bottom': first['bottom'], 'page': pno}); continue
    if mode == 'src':
        sources.append(txt); continue
    if mode == 'refs':
        if txt.startswith('Prepared for') or final:
            final.append(txt); continue
        if x0 <= LM + 2 or not raw_refs: raw_refs.append(line_text(ws))
        else:
            lp = line_text(ws)
            prev = raw_refs[-1][-1][1] if raw_refs[-1] else ''
            if lp: lp[0] = ('' if prev.endswith('-') else ' ', lp[0][1], lp[0][2])
            raw_refs[-1] += lp
        continue
    has_bullet = ws[0]['text'] in ('', '•', '', '▪')
    num = re.match(r'^(\d+)\.$', ws[0]['text'])
    gap = (top - cur['bottom']) if (cur and cur['page'] == pno) else 99
    if has_bullet:
        lvl = 'B' if x0 < LM + 8 else 'B2'
        cur = {'kind': lvl, 'parts': line_text(ws), 'x': round(ws[1]['x0']) if len(ws) > 1 else x0, 'bottom': first['bottom'], 'page': pno}
        items.append(cur); continue
    if num and len(ws) > 1 and ws[1]['x0'] - ws[0]['x1'] > 6:
        cur = {'kind': 'NI', 'num': num.group(1), 'parts': line_text(ws[1:]), 'x': round(ws[1]['x0']), 'bottom': first['bottom'], 'page': pno}
        items.append(cur); continue
    cont = cur is not None and (gap < 5.5 or (cur['page'] != pno and x0 >= cur['x'] - 2 and cur['kind'] != 'P' and x0 > LM + 2)) and abs(x0 - cur['x']) < 4
    if cur is not None and cur['page'] != pno and cur['kind'] == 'P' and x0 <= LM + 2 and idx > 0:
        # paragraph continuing across a page: previous page's last line did not end a sentence
        last = ''.join(t for _, t, _ in cur['parts'])
        cont = not re.search(r'[.:!?)"”]$', last)
    if cont:
        prev_last = cur['parts'][-1][1] if cur['parts'] else ''
        lp = line_text(ws)
        if lp:
            joiner = '' if prev_last.endswith('-') and not prev_last.endswith(' -') else ' '
            lp[0] = (joiner, lp[0][1], lp[0][2])
        cur['parts'] += lp; cur['bottom'] = first['bottom']; cur['page'] = pno
    else:
        cur = {'kind': 'P', 'parts': line_text(ws), 'x': x0, 'bottom': first['bottom'], 'page': pno}
        items.append(cur)

def render(parts):
    # merge runs of same style and wrap with markdown markers
    s, buf, bst = '', '', None
    def flush():
        nonlocal s, buf
        if not buf: return
        core = buf.strip(); lead = buf[:len(buf) - len(buf.lstrip())]; trail = buf[len(buf.rstrip()):]
        if bst == 'b' or bst == 'bi': s += lead + '**' + core + '**' + trail
        elif bst == 'i': s += lead + '*' + core + '*' + trail
        else: s += buf
        buf = ''
    for sp, t, st in parts:
        if st != bst:
            if sp and buf: buf += ''
            flush(); bst = st; buf = sp + t
        else:
            buf += sp + t
    flush()
    return re.sub(r'\s+', ' ', s).strip()

with open(out, 'w') as o:
    o.write(f'TITLE = {" ".join(title)!r}\nFILE = {base!r}\nSOURCES_NOTE = {" ".join(sources)!r}\nFINAL_NOTE = {" ".join(final)!r}\nBODY = [\n')
    for it in items:
        t = render(it['parts'])
        if it['kind'] == 'NI': t = it['num'] + '|' + t
        o.write(f'({it["kind"]!r}, {t!r}),\n')
    o.write(']\nRAW_REFS = [\n')
    for r in raw_refs:
        t = render(r)
        m = re.search(r'https://doi\.org/(\S+)$', t)
        doi = m.group(1) if m else None
        if m: t = t[:m.start()].rstrip()
        o.write(f'    ({t!r}, {doi!r}),\n')
    o.write(']\n')
print(len(items), 'items,', len(raw_refs), 'refs')
