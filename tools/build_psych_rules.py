"""Build Psych-026..030 (Rule Breaking) from tools/psych-rules/*.json using Psych-012 as the page skeleton."""
import json,re,glob,html,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TPL=(ROOT/'belief-cards/psychological/Psych-012-I-Dont-Need-Anyone-I-Am-Better-Off-Alone.html').read_text()
CAT=json.loads((ROOT/'tools/music-catalog.json').read_text())
GC=json.loads((ROOT/'tools/godly-counsel-chapters.json').read_text())
BIBLE=sys.path.insert(0,str(ROOT/'tools'))
AUD={'Anxiety':('https://music.wixstatic.com/mp3/dbdded_f67d414544534727acf6973d58189443.mp3','about 18 minutes'),
     'Depression':('https://music.wixstatic.com/mp3/dbdded_149606a27908493da01ac9492fb18ab1.mp3','about 20 minutes')}
PB='https://doctorishome.wixstudio.com/website-6/scriptures?topic='
GCB='https://doctorishome.github.io/belief-therapy-tool/belief-cards/godly-counsel/'
head=TPL[:TPL.index('<div class="card belief">')]
endmark='<div class="foot">✦ ✦ ✦</div></div></div>'
tail=TPL[TPL.rindex(endmark)+len(endmark):]
e=html.escape
def q(s): return s
def song(k):
    vid,title,art,_,blurb=CAT[k]
    return ('<div class="songwrap"><div class="song"><div class="video-area"><a class="video-poster" href="https://www.youtube.com/watch?v=%s" data-video="%s" aria-label="Play %s inside this card"><img loading="lazy" src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="%s video thumbnail"><span class="video-play">▶ Play lyric video</span></a></div><div class="txt"><strong>%s</strong><small>%s</small><p>%s</p></div></div><a class="ytlink" target="_blank" rel="noopener" href="https://www.youtube.com/watch?v=%s">Watch on YouTube (optional)</a></div>'%(vid,vid,e(title),vid,e(title),e(title),e(art),e(blurb),vid))
def ul(items): return '<ul>'+''.join('<li>%s</li>'%i for i in items)+'</ul>'
def build(d):
    n=d['num'];b=d['belief']
    t=re.sub(r'<title>.*?</title>','<title>Belief Card #%d: %s</title>'%(n,e(d['belief_plain'])),head,count=1)
    # reference-less verse lines: [(text, ref)]
    also=''.join('<p>“%s” <span class="ref">(%s)</span></p>'%(x[0],x[1]) for x in d['also'])
    pearls=''.join('<li><a target="_blank" rel="noopener" href="%s%s">%s</a></li>'%(PB,s,l) for s,l in d['pearls'])
    gcs=''
    for c in d['gc']:
        title=GC[str(c)][0];slug=re.sub(r'[^A-Za-z0-9]+','-',title).strip('-')
        gcs+='<li><a target="_blank" rel="noopener" href="%sGC-%02d-%s.pdf">%s</a></li>'%(GCB,c,slug,e(title))
    au,dur=AUD[d['listen']]
    errs=''.join('<li><strong>%s:</strong> %s</li>'%tuple(x) for x in d['errors'])
    opts6=d['questions'][:6]
    scr=''.join('<li><b>%s</b><span class="scrip">“%s”</span></li>'%(r,tx) for tx,r in [(d['key'][0],d['key'][1])]+[(x[0],x[1]) for x in d['also']])
    body=('<div class="card belief"><div class="tag">Psychological/Cognitive False Belief #%d · Honesty and Respect · %s</div><h1>%s</h1><div class="orn">✦ ✦ ✦</div>'%(n,e(d['tag']),b)
    +'<p class="intro">%s</p>'%d['intro']
    +'<h2>Where it often comes from</h2><p>%s</p><h2>How the belief can keep itself going</h2><p>%s</p><h2>What Scripture teaches</h2><p>%s</p>'%(d['origins'],d['keeps'],d['teaches'])
    +'<div class="key">“%s” <span class="ref">(%s)</span></div><h2>Also see</h2><div class="also">%s</div>'%(d['key'][0],d['key'][1],also)
    +'<h2>Common self-statements</h2>'+ul(d['self'])+'<h2>Common logical errors</h2><ul>'+errs+'</ul><h2>Challenging questions</h2>'+ul(d['questions'])
    +'<h2>Truth summary</h2><p class="truth">%s</p><h2>A short prayer</h2><p class="prayer">%s</p>'%(d['truth'],d['prayer'])
    +'<h2>Related Pearls topics</h2><p>Open these topics in the Pearls Scripture Search:</p><ul class="pearls">%s</ul><p><strong>Godly Counsel Lessons</strong> — read or print:</p><ul class="pearls">%s</ul>'%(pearls,gcs)
    +'<h2>Listen: Overcoming %s</h2><div class="audio"><p><a target="_blank" rel="noopener" href="%s"><strong>Overcoming %s</strong></a> · Dr. Brian Campbell · %s</p><audio controls preload="none" src="%s">Your browser cannot play this audio.</audio></div>'%(d['listen'],au,d['listen'],dur,au)
    +'<h2>Songs that speak truth to this belief</h2><p>Click a picture to play inside this card. Each selection is an official lyric video with words on screen.</p><div class="songs">%s</div><p class="songnote">YouTube may show ads.</p>'%''.join(song(k) for k in d['songs'])
    +'<h2>Clinical background</h2><p>%s</p><p><a href="https://beckinstitute.org/wp-content/uploads/2021/06/PBQ-SF-Full-Documents.pdf">Beck Institute: Personality Belief Questionnaire materials</a> · <a href="https://www.guilford.com/books/Cognitive-Therapy-of-Personality-Disorders/Beck-Davis-Freeman/9781462525812">Beck, Davis, &amp; Freeman, Cognitive Therapy of Personality Disorders</a></p>'%d['clinical']
    +'<p class="morning">%s</p><div class="foot">✦ ✦ ✦</div></div>'%d['morning'])
    hw=('<div class="card"><div class="tag">Homework · Replace and Rehearse</div><h1>My Plan for Replacing<br>%s</h1><div class="orn">✦ ✦ ✦</div><p class="intro">Check one choice in each section or write your own. Choose a question and a truth that feel meaningful to you.</p><div class="fill">Name: ____________________ Date started: ____________________</div>'%b
    +'<div class="step"><span class="num">1</span><div><h2>How strongly do I believe the lie?</h2><p><em>Rate it from 0%% to 100%%.</em></p></div></div><div class="rate"><strong>%s</strong> &nbsp; I believe this ______ %%.</div>'%b
    +'<div class="step"><span class="num">2</span><div><h2>My best question</h2><p><em>Select a question to ask when you catch yourself thinking, %s</em></p></div></div>'%d['catch']
    +'<ul class="opts">%s</ul><div class="fill">My own question:</div>'%''.join('<li>%s</li>'%x for x in opts6)
    +'<div class="step"><span class="num">3</span><div><h2>My replacement truth</h2><p><em>Select a balanced statement to practice.</em></p></div></div><ul class="opts">%s</ul><div class="fill">In my own words:</div>'%''.join('<li>%s</li>'%x for x in d['hw_truths'])
    +'<div class="step"><span class="num">4</span><div><h2>My Scripture</h2><p><em>Choose one passage to remember; these are the same passages shown on the card.</em></p></div></div><ul class="opts">%s</ul><div class="fill">The verse I will practice:</div><div class="foot">✦ ✦ ✦</div></div>'%scr)
    hw2=('<div class="card"><div class="tag">Homework · Practicing the Truth</div><h1>Practicing the Truth</h1><div class="orn">✦ ✦ ✦</div><div class="step"><span class="num">5</span><div><h2>Rehearse the truth daily</h2><p><em>Read your chosen Scripture, listen, and practice a balanced thought.</em></p></div></div>'
    +'<p>Read <a href="%s%s">Pearls: %s</a>. Listen to <a href="%s">Overcoming %s</a>. Say your replacement truth aloud once in the morning and once in the evening.</p><div class="fill">Today I noticed this change:</div>'%(PB,d['pearls'][0][0],d['pearls'][0][1],au,d['listen'])
    +'<div class="step"><span class="num">6</span><div><h2>Try a small behavioral experiment</h2><p><em>Choose a safe, low-risk test; do not ignore real warning signs.</em></p></div></div><ul class="opts">%s</ul>'%''.join('<li>%s</li>'%x for x in d['experiments'])
    +'<p><strong>My prediction:</strong></p><div class="fill"></div><p><strong>What actually happened:</strong></p><div class="fill"></div><p><strong>What I learned:</strong></p><div class="fill"></div>'
    +'<div class="step"><span class="num">7</span><div><h2>Track what changes</h2><p><em>Practice for seven days. Mark what you tried and rate belief strength.</em></p></div></div><table><thead><tr><th>Day</th><th>What I practiced</th><th>Belief %</th><th>What I learned</th></tr></thead><tbody>'+''.join('<tr><td>%d</td><td></td><td></td><td></td></tr>'%i for i in range(1,8))+'</tbody></table>'
    +'<h2>Song reflection</h2><p>%s</p><div class="fill">Song:</div><div class="fill">A truth I want to remember:</div>'%d['reflect']
    +'<h2>My Truth Card</h2><div class="cutcard"><strong>OLD BELIEF:</strong><p><s>%s</s></p><strong>NEW TRUTH:</strong><p>%s</p><strong>MY SCRIPTURE:</strong><p>%s</p></div>'%(d['belief_plain'],d['newtruth'],d['key'][1])
    +'<h2>A short prayer</h2><p class="prayer">%s</p><p class="songnote">Scripture quotations: Berean Standard Bible (BSB), public domain. Educational material only; not a diagnosis or substitute for professional care.</p><div class="foot">✦ ✦ ✦</div></div></div>'%d['prayer2'])
    return t+body+hw+hw2+tail
for f in sorted(glob.glob(str(ROOT/'tools/psych-rules/*.json'))):
    d=json.load(open(f));out=ROOT/('belief-cards/psychological/Psych-%03d-%s.html'%(d['num'],d['file']))
    out.write_text(build(d));print(out.name)
