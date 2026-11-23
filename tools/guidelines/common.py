# Shared page builder for the specialty guidelines pages (Trauma, Abuse, ...).
# Takes the head, styles and menu from counselors/guidelines.html so every page matches.
import re

EXTRA = """<style>
table.bt{width:100%;border-collapse:collapse;margin:12px 0;background:#fff;font-size:.97rem}
table.bt th{background:var(--navy);color:#fff;text-align:left;padding:9px 12px}
table.bt td{border:1px solid var(--line);padding:9px 12px;vertical-align:top}
table.bt td:first-child{font-weight:bold;color:#7a1f1f}
table.bt a{color:var(--navy);font-size:.9rem}
.crit{background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px 18px;margin:10px 0}
.crit ol,.crit ul{margin:4px 0 4px 4px}
.also{background:#eef1f6;border-radius:8px;padding:10px 16px;margin:16px 0;font-size:.97rem}
.also a{color:var(--navy);font-weight:bold}
.hot{background:#fff;border:2px solid #7a1f1f;border-radius:10px;padding:12px 20px;margin:18px 0}
.hot h3{margin:0 0 6px;color:#7a1f1f}.hot ul{margin:4px 0;padding-left:20px}.hot li{margin:4px 0}
@media(max-width:560px){table.bt{font-size:.9rem}table.bt td,table.bt th{padding:7px 8px}}
</style>"""

def head(title, desc):
    src = open('counselors/guidelines.html').read()
    h = src[:src.index('<div class="hero"')]
    h = re.sub(r'<title>.*?</title>', f'<title>{title} | Belief Counseling</title>', h, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', h, count=1)
    assert 'class="l on" href="../counselors/guidelines.html">Guidelines' in h
    return h.replace('</head>', EXTRA + '</head>', 1)

def say(t): return f'<p class="say">“{t}”</p>'
def scrip(text, ref): return f'<p class="scrip">“{text}” <b>({ref}, BSB)</b></p>'

def belief_table(rows):
    return ('<table class="bt"><tr><th>False belief</th><th>A question to examine it</th></tr>'
            + ''.join(f'<tr><td>“{b}”<br><a href="../belief-cards/{c}">Open the belief card →</a></td><td>{q}</td></tr>' for b, q, c in rows)
            + '</table>')

def section(i, g):
    gid, title, glance, steps, why, practice, sayings, sc, extra = g
    h = f'<div class="g" id="{gid}"><h2><span class="n">{i}</span>{title}</h2>'
    h += ''.join(f'<span class="step">{s}</span>' for s in steps)
    h += f'<p class="why">{why}</p><h3>In practice</h3><ul>' + ''.join(f'<li>{p}</li>' for p in practice) + '</ul>'
    h += extra
    if sayings:
        h += '<h3>Try saying</h3>' + ''.join(say(s) for s in sayings)
    if sc:
        h += scrip(*sc)
    return h + '<p class="toplink"><a href="#top">Back to top ↑</a></p></div>'

def page(out, title, subtitle, desc, intro, note, core_big, core_p, G, AP, check_title, CHECK, students, related, motto, motto_ref, refs, top_extra=''):
    glance = '<ol class="glance">' + ''.join(f'<li><a href="#{g[0]}">{g[1]}</a><span>{g[2]}</span></li>' for g in G) + '</ol>'
    ap = '<table class="ap"><tr><th>Avoid</th><th class="p">Try instead</th></tr>' + ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in AP) + '</table>'
    body = f"""<div class="hero" id="top"><div class="eyebrow">Belief Counseling · Clinical Practice Guidelines</div><h1>{title}</h1><p>{subtitle}</p><p style="font-size:.95rem;margin-top:10px">Dr. Brian Campbell</p></div>
<div class="gwrap">
<div class="back"><a href="guidelines.html">&larr; All Guidelines</a><button class="printbtn" onclick="window.print()">Print these guidelines</button></div>
<p>{intro}</p>
<p class="scope"><strong>Please note:</strong> {note}</p>
{top_extra}
<div class="core"><div class="k">The central principle</div><div class="big">{core_big}</div><p>{core_p}</p></div>
<h2>The Guidelines at a Glance</h2>
<p class="small">Click any guideline to jump to it. The tags (Identify, Challenge, Replace) show where each one matters most in the Belief Counseling process.</p>
{glance}
{''.join(section(i + 1, g) for i, g in enumerate(G))}
<h2 id="phrases">Common Missteps: What to Say Instead</h2>
{ap}
<div class="check" id="check"><h3 style="margin-top:0">{check_title}</h3>
<ul>{''.join(f'<li>{c}</li>' for c in CHECK)}</ul></div>
<div class="stud"><h3 style="margin-top:0">For Students</h3><p style="margin:4px 0">{students}</p></div>
<div class="also">Related: {related}</div>
<p class="motto">{motto}</p>
<p style="text-align:center;margin:0 0 20px;color:var(--mut)">{motto_ref} (BSB)</p>
<h2 id="reading">References and Further Reading</h2>
<ul class="refs">{''.join(f'<li>{r}</li>' for r in refs)}</ul>
<p class="small">Scripture quotations are from the Berean Standard Bible.</p>
<p class="small">© 2026 Brian Campbell, Ph.D. All rights reserved.</p>
</div>
<div class="foot">Educational training for counselors. Never enter real client names or details. · © Brian Campbell, Ph.D. · <a href="https://www.beliefcounselor.com/help" target="_top">Help &amp; Support</a></div>
</body></html>"""
    open(out, 'w').write(head(title + ' Guidelines', desc) + body)
    print('ok', out)

def doi(d): return f'<a href="https://doi.org/{d}" target="_blank" rel="noopener">https://doi.org/{d}</a>'
def link(u, t=None): return f'<a href="{u}" target="_blank" rel="noopener">{t or u}</a>'
