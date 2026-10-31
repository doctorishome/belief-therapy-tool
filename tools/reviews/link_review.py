"""Swap a 'Coming soon' row on counselors/reviews.html for an Open PDF link.
Run: python3 tools/reviews/link_review.py "<row title exactly as on the page>" <pdf-file-name>"""
import sys
title, f = sys.argv[1], sys.argv[2]
p = 'counselors/reviews.html'; s = open(p).read()
a = f'<span class="t">{title}</span><span class="soon">Coming soon</span>'
assert a in s, 'row not found'
s = s.replace(a, f'<span class="t">{title}</span><a class="open" href="https://doctorishome.github.io/belief-therapy-tool/counselors/reviews/{f}" target="_blank" rel="noopener">Open PDF</a>')
open(p, 'w').write(s); print('linked', title)
