"""Builds the GitHub-hosted belief-list pages that the Wix False Beliefs pages display.
Edit tools/lists/<page>.json (add a belief, add a card link), run this, then push; no Wix editing needed.
A belief is [text] or [text, "Card-file.html"]; a card link makes it a clickable 'Open belief card' link."""
import json,sys,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CSS=('body{margin:16px;color:#2b2b2b;font:18px/1.7 Georgia,serif}h2{color:#a8864f;font-size:24px;border-bottom:1px solid #d9c7a3}aside{padding:16px;border-left:3px solid #a8864f;background:#fbf6ec;font:14px/1.6 Arial;color:#5b6472}.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:start}details{border:1px solid #eadcc4;border-radius:12px;background:#f6eee2;overflow:hidden}summary{padding:22px;cursor:pointer;color:#1e3556;font:bold 18px/1.4 Georgia;min-height:65px}summary small{display:block;font:12px Arial;color:#5b6472;margin-top:8px}ol{background:#fdfaf4;margin:0;padding:15px 25px 20px 42px;font-size:16px}li{padding:8px 0}input{box-sizing:border-box;width:100%;padding:16px;background:#fdfaf4;border:1px solid #eadcc4;border-radius:8px;font:17px Georgia;margin:12px 0 20px}label{font:17px Arial;color:#1e3556}footer{font:13px/1.6 Arial;color:#5b6472;margin-top:25px}@media(max-width:600px){.grid{grid-template-columns:1fr}}a.cardlink{color:#1e3556;text-decoration:underline;text-decoration-color:#a8864f;text-underline-offset:3px}a.cardlink:hover{color:#a8864f}.cardtag{font:12px Arial;color:#a8864f;white-space:nowrap}')
def build(name):
    d=json.loads((ROOT/'tools/lists'/(name+'.json')).read_text(encoding='utf-8'))
    e=html.escape
    def li(b):
        if len(b)>1: return '<li><a class="cardlink" href="%s%s" target="_blank" rel="noopener">“%s”</a> <small class="cardtag">Open belief card</small></li>'%(d['card_base'],b[1],e(b[0],quote=False))
        return '<li>“%s”</li>'%e(b[0],quote=False)
    boxes=''.join('<details><summary>%s<small>%d beliefs</small></summary><ol>%s</ol></details>'%(e(g['name'],quote=False),len(g['beliefs']),''.join(li(b) for b in g['beliefs'])) for g in d['groups'])
    page=('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head><body><p>%s</p><aside>%s</aside><p><label for="search">%s</label><input id="search" type="search" placeholder="%s"></p><h2>%s</h2><p style="font:15px Arial;color:#5b6472">%s</p><div class="grid">%s</div><footer>%s</footer><script>document.querySelector("input").oninput=function(){let q=this.value.toLowerCase().trim();document.querySelectorAll("details").forEach(d=>{d.hidden=!d.textContent.toLowerCase().includes(q);d.open=!!q&&!d.hidden})}</script></body></html>'
      %(e(d['heading'],quote=False),CSS,d['intro'],d['aside'],d['search_label'],e(d['placeholder']),d['heading'],d['hint'],boxes,d['footer']))
    out=ROOT/'belief-lists'/(name+'.html');out.write_text(page,encoding='utf-8');print(out.name,len(page))
for n in (sys.argv[1:] or [p.stem for p in (ROOT/'tools/lists').glob('*.json')]): build(n)
