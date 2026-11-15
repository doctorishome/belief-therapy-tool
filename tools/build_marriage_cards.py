"""Build the separate Marriage set; leaves the 120 Spiritual/Religious cards untouched."""
import json,sys,re,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import build_cards as b
from add_songs import add_songs
b.PEARLS_TOPICS=json.loads((ROOT/'tools/pearls-topics.json').read_text());b.GODLY_COUNSEL.update(json.loads((ROOT/'tools/godly-counsel-chapters.json').read_text()))
b.LIST_PAGE='https://doctorishome.github.io/belief-therapy-tool/belief-cards/interpersonal/marriage/'
BIBLE=b.load_bible();CAT=json.loads((ROOT/'tools/music-catalog.json').read_text());OUT=ROOT/'belief-cards/interpersonal/marriage';OUT.mkdir(parents=True,exist_ok=True)
DATA=[]
for p in sorted((ROOT/'tools/marriage').glob('*.json')):
 d=json.loads(p.read_text());d['songs']=[[CAT[k][0],CAT[k][1],CAT[k][2],CAT[k][4]] for k in d['songs']]
 _,page,_=b.render(d,BIBLE,(ROOT/'tools/card-style.css').read_text());page=add_songs(page,d)
 page=page.replace('Spiritual/Religious False Belief #','Interpersonal False Belief · Marriage #').replace('All Spiritual/Religious False Beliefs','All Marriage Cards')
 page=page.replace('Tap a song to play it right here.','Tap a song to play it right here. Three contemporary songs and one classic hymn or older favorite.')
 page=page.replace('<h2>My Truth Card</h2>','<h2>My Truth Card</h2>')
 page=page.replace('Rewrite my verse with my name in it and read it aloud each morning.','Write a personal reminder based on my verse and read it aloud. Keep this application separate from the Bible quotation.')
 page=page.replace('For example, James 1:19 becomes:', 'A personal reminder based on James 1:19:')
 note='<p class="bnote">Selected Scripture references draw on <em>Pearls</em>, “Marriage” (pp. 240–241) and “Marriage Guidance” (pp. 242–244), with other passages selected for this belief. Quotations use the BSB.</p>'
 page=page.replace('<h2>Related Pearls topics</h2>',note+'\n<h2>Related Pearls topics</h2>')
 safe='<p class="why">Choose exercises you can do safely. If there is coercion, violence, or fear of retaliation, seek private professional support before trying joint exercises.</p>'
 page=page.replace('<h2>My action step this week</h2>', '<h2>My action step this week</h2>')
 page=page.replace('<p class="why">Do one thing that tests the lie in real life.</p>', '<p class="why">Do one thing that tests the lie in real life.</p>'+safe)
 base=f'Marriage-{d["num"]:03d}-{d["file"]}';d['base']=base
 page=page.replace('<div class="printbar">','<div class="printbar"><p><a href="'+base+'.pdf" target="_blank" rel="noopener">Download Card and Homework (PDF)</a> · <a href="'+base+'-Homework.pdf" target="_blank" rel="noopener">Download Homework Only (PDF)</a></p>')
 for k in ['marriage','marriage-guidance']:assert '?topic='+k in page
 assert page.count('class="song"')==4
 (OUT/(base+'.html')).write_text(page);DATA.append(d)
items=''.join(f'<li><a href="{d["base"]}.html">Card {d["num"]}. {html.escape(d["belief"])}</a><br/><a href="{d["base"]}.pdf">Card and Homework PDF</a> · <a href="{d["base"]}-Homework.pdf">Homework PDF</a></li>' for d in DATA)
(OUT/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Marriage — False Beliefs and Homework</title><style>body{background:#EEEAE3;color:#1F3A5F;font:18px Georgia;line-height:1.7;margin:0}main{max-width:850px;margin:30px auto;padding:35px;background:#FFFDF8;border:2px solid #B08A4B}h1{color:#1F3A5F}a{color:#1F3A5F;text-decoration-color:#B08A4B}li{margin-bottom:22px}</style><main><h1>Marriage</h1><p>Identify a belief, consider Scripture and evidence, and choose practical homework. Each card includes BSB scriptures, related Pearls topics, four lyric videos, and printable exercises.</p><ol style="list-style:none;padding:0">'+items+'</ol><p><a href="Marriage-All-Five-Cards-and-Homework.pdf">Download all five cards and homework</a></p></main></html>')
print('Built five HTML cards and Marriage index.')
