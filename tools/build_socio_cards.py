"""Build the Socioeconomic · Scarcity and Security set (5 cards); leaves other sets untouched."""
import json,sys,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import build_cards as b
from add_songs import add_songs
b.PEARLS_TOPICS=json.loads((ROOT/'tools/pearls-topics.json').read_text());b.GODLY_COUNSEL.update(json.loads((ROOT/'tools/godly-counsel-chapters.json').read_text()))
SET=sys.argv[1] if len(sys.argv)>1 else 'socioeconomic'
SUB=sys.argv[2] if len(sys.argv)>2 else 'scarcity-security'
TITLE=sys.argv[3] if len(sys.argv)>3 else 'Scarcity and Security'
SLUG=SUB.title().replace('-','-')
b.LIST_PAGE='https://doctorishome.github.io/belief-therapy-tool/belief-cards/socioeconomic/%s/'%SUB
BIBLE=b.load_bible();CAT=json.loads((ROOT/'tools/music-catalog.json').read_text());OUT=ROOT/('belief-cards/socioeconomic/'+SUB);OUT.mkdir(parents=True,exist_ok=True)
DATA=[]
for p in sorted((ROOT/('tools/'+SET)).glob('*.json')):
 d=json.loads(p.read_text());d['songs']=[[CAT[k][0],CAT[k][1],CAT[k][2],CAT[k][4]] for k in d['songs']]
 _,page,_=b.render(d,BIBLE,(ROOT/'tools/card-style.css').read_text());page=add_songs(page,d)
 page=page.replace('Spiritual/Religious False Belief #','Socioeconomic False Belief #').replace('All Spiritual/Religious False Beliefs','All '+TITLE+' Cards')
 page=page.replace('Tap a song to play it right here.','Tap a song to play it right here. Three contemporary songs and one classic hymn or older favorite.')
 page=page.replace('Rewrite my verse with my name in it and read it aloud each morning.','Write a personal reminder based on my verse and read it aloud. Keep this application separate from the Bible quotation.')
 page=page.replace('For example, James 1:19 becomes:','A personal reminder based on '+d['name_example'][0]+':')
 safe='<p class="why">This card is educational and is not financial or legal advice. Choose steps you can do safely. If you are without food, housing, or safety, contact your church, a trusted advisor, or local assistance services.</p>'
 page=page.replace('<p class="why">Do one thing that tests the lie in real life.</p>','<p class="why">Do one thing that tests the lie in real life.</p>'+safe)
 base=f'Socio-{d["num"]:03d}-{d["file"]}';d['base']=base
 page=page.replace('<div class="printbar">','<div class="printbar"><p><a href="'+base+'.pdf" target="_blank" rel="noopener">Download Card and Homework (PDF)</a> · <a href="'+base+'-Homework.pdf" target="_blank" rel="noopener">Download Homework Only (PDF)</a></p>')
 for k in d['pearls'][:2]:assert '?topic='+k in page,k
 assert page.count('class="song"')==4
 (OUT/(base+'.html')).write_text(page);DATA.append(d)
items=''.join(f'<li><a href="{d["base"]}.html">Card {d["num"]}. {html.escape(d["belief"])}</a><br/><a href="{d["base"]}.pdf">Card and Homework PDF</a> · <a href="{d["base"]}-Homework.pdf">Homework PDF</a></li>' for d in DATA)
(OUT/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+TITLE+' — False Beliefs and Homework</title><style>body{background:#EEEAE3;color:#1F3A5F;font:18px Georgia;line-height:1.7;margin:0}main{max-width:850px;margin:30px auto;padding:35px;background:#FFFDF8;border:2px solid #B08A4B}h1{color:#1F3A5F}a{color:#1F3A5F;text-decoration-color:#B08A4B}li{margin-bottom:22px}</style><main><h1>'+TITLE+'</h1><p>Identify a belief, consider Scripture and evidence, and choose practical homework. Each card includes BSB scriptures, related Pearls topics, four lyric videos, and printable exercises.</p><ol style="list-style:none;padding:0">'+items+'</ol><p><a href="'+TITLE.replace(' and ','-').replace(' ','-')+'-All-Five-Cards-and-Homework.pdf">Download all five cards and homework</a></p></main></html>')
print('Built five HTML cards and index.')
