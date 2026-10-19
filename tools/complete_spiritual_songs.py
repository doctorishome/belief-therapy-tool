"""Apply the reviewed 3 contemporary + 1 classic music plan without rebuilding teaching text."""
import json,re,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CAT=json.loads((ROOT/'tools/music-catalog.json').read_text())
# Each line covers five cards in numeric order. Last entry in each group is the classic.
PLAN='''
east wins clean assurance;even glorious held faithful;father name grace lovesme;stays alone jesus friend;who yousay again amazing
jesus messiah inchrist glory;grace wins chains assurance;onegod messiah jesus great;knows worn soul friend;east clean cross amazing
power greater conquer victory;knows soul held faithful;grace cross wins assurance;speak want onegod eyes;body broken love glory
battle fear onegod great;conquer greater power victory;breaker cross chains amazing;heaven hope forever lives;jesus fear father friend
soul knows worn friend;held alone even faithful;worn truth stays tender;who grace allnew lovesme;love truth speak eyes
east clean wins amazing;truth grace inchrist assurance;name who father lovesme;knows power greater victory;jesus cross chains glory
speak onegod truth eyes;voice speak want faithful;truth worthy onegod great;speak messiah voice glory;cross speak jesus amazing
east grace chains amazing;cross wins clean assurance;forgive truth love eyes;younger name broken tender;forgive worn knows friend
chains grace cross amazing;inchrist hope name assurance;east wins stays lovesme;jesus forever heaven lives;messiah onegod broken glory
even held soul faithful;broken grace love glory;want speak onegod eyes;knows worn stays friend;heaven glorious hope great
worn knows even friend;who name grace assurance;truth alone father lovesme;father stays jesus faithful;love amen again glory
worthy even voice assurance;alone stays held faithful;speak worn jesus friend;inchrist hope glorious eyes;fear battle conquer victory
grace cross hope amazing;heaven who father lovesme;heaven allnew amen glory;hope forever glorious faithful;east clean name assurance
cross chains grace amazing;inchrist wins hope assurance;east jesus clean tender;father held glorious faithful;love who again lovesme
allnew respower forever lives;heaven hope allnew glory;respower glorious held faithful;power forever onegod victory;hope heaven jesus assurance
soul worn held friend;knows glorious heaven faithful;hope forever fear lives;cross grace father assurance;even alone stays lovesme
jesus father even friend;speak broken grace tender;stays want held faithful;worn knows truth eyes;cross wins clean amazing
speak grace love lovesme;speak onegod voice eyes;worthy worn jesus friend;speak hope want faithful;speak body truth glory
voice speak onegod eyes;jesus who broken assurance;stays inchrist father faithful;truth worn knows friend;body love want glory
truth fear battle eyes;broken allnew glorious tender;grace love again glory;held father stays faithful;who yousay name assurance
glorious want held faithful;want love again glory;voice speak jesus eyes;held glorious inchrist assurance;conquer even hope victory
east cross grace amazing;worn knows soul friend;glorious held even faithful;soul truth worn tender;alone stays jesus lovesme
chains wins grace amazing;who father again lovesme;love want body glory;held jesus worn friend;broken clean cross tender
fear hope conquer victory;speak want glorious eyes;inchrist grace name assurance;body love again glory;knows even held faithful
'''
ROWS=[r.strip() for r in PLAN.split(';') if r.strip()]
# Newlines delimit topics as well as semicolons.
ROWS=[r.split() for line in PLAN.strip().splitlines() for r in line.split(';')]
assert len(ROWS)==120

def block(keys):
 out=['<h2>Songs that speak truth to this belief</h2>','<p class="songnote2">Tap a song to play it right here. Three contemporary selections and one classic hymn or older favorite.</p>','<div class="songs">']
 for k in keys:
  v,t,a,era,why=CAT[k];e=html.escape;label='Contemporary' if era=='contemporary' else 'Classic hymn / older favorite'
  out.append(f'<a class="song" data-era="{era}" href="https://www.youtube.com/watch?v={v}" target="_blank" rel="noopener"><span class="thumb" style="background-image:url(\'https://i.ytimg.com/vi/{v}/hqdefault.jpg\')"></span><span class="txt"><span class="st">{e(t)}</span><span class="sa">{e(a)} · {label}</span><span class="sw">{e(why)}</span></span></a>')
 out+=['</div>','<p class="songnote">Songs play here through YouTube and may start with a short ad. If one will not play, use its “Watch on YouTube” link.</p>','']
 return '\n'.join(out)

JOURNAL='''<h2>My song journal</h2>
<p class="why">After each day's song, write what it told you that challenges the lie.</p>
<table class="track songj"><tr><th>Day</th><th>Song I listened to</th><th>What it told me that challenges the lie</th></tr>
'''+''.join(f'<tr><td>{d}</td><td></td><td></td></tr>\n' for d in 'Mon Tue Wed Thu Fri Sat Sun'.split())+'</table>\n\n'

def main():
 for n,keys in enumerate(ROWS,1):
  assert len(keys)==len(set(keys))==4
  assert [CAT[k][3] for k in keys]==['contemporary']*3+['classic']
  matches=list((ROOT/'belief-cards').glob(f'Belief-{n:03d}-*.html'));assert len(matches)==1
  path=matches[0];s=path.read_text()
  old=s
  if '<h2>Songs that speak truth to this belief</h2>' in s:
   s,count=re.subn(r'<h2>Songs that speak truth to this belief</h2>.*?(?=<p class="morning">)',block(keys)+'\n',s,flags=re.S);assert count==1
  else:
   assert s.count('<p class="morning">')==1
   s=s.replace('<p class="morning">',block(keys)+'\n<p class="morning">')
  if '<h2>My song journal</h2>' not in s:
   assert s.count('Everyone does the first three.')==1
   s=s.replace('Everyone does the first three.','Everyone does the first four.')
   assert s.count('<li><strong>Set reminders</strong>')==1
   s=s.replace('<li><strong>Set reminders</strong>','<li><strong>Listen to one song each day</strong> from “Songs that speak truth to this belief” on my card, and fill in my song journal (below).</li>\n<li><strong>Set reminders</strong>')
   assert s.count('<h2>My Truth Card</h2>')==1
   s=s.replace('<h2>My Truth Card</h2>',JOURNAL+'<h2>My Truth Card</h2>')
  assert s.count('class="song"')==4 and s.count('data-era="contemporary"')==3 and s.count('data-era="classic"')==1
  assert s.count('<h2>My song journal</h2>')==1
  # Teaching and scripture before the audio/music area must remain byte-for-byte identical.
  assert old.split('<div class="audio">')[0]==s.split('<div class="audio">')[0]
  path.write_text(s)
  p=ROOT/f'tools/cards/{n:03d}.json'
  if p.exists():
   d=json.loads(p.read_text());d['songs']=[[CAT[k][0],CAT[k][1],CAT[k][2],CAT[k][4]] for k in keys];p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'tools/spiritual-song-plan.json').write_text(json.dumps({str(n):keys for n,keys in enumerate(ROWS,1)},indent=2)+'\n')
 print('Updated 120 cards, 480 selections, and matching source data.')
if __name__=='__main__':main()
