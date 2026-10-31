"""Build the Counselors' World pages (counselors/*.html). Shared nav + styling. Public shell/outline content only."""
import html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'counselors'; OUT.mkdir(exist_ok=True)
SITE='https://doctorishome.wixstudio.com/website-6'
PAGES=[('welcome','Welcome','blank-11'),('process','The Process','blank-12'),('tips','Professional Tips','blank-13'),
       ('theory','Theory Topics','blank-14'),('cases','Case Studies','blank-15'),('course','The Course','blank-16'),('library','Clinical Library','blank-17')]
CSS="""
:root{--navy:#12284c;--navy2:#1d3a6b;--gold:#c9a227;--cream:#faf6ec;--ink:#1f2a3a;--mut:#5b6678;--line:#e3dcc6}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--ink);background:var(--cream);line-height:1.6}
a{color:var(--navy2)}
.nav{position:sticky;top:0;z-index:5;background:var(--navy);border-bottom:3px solid var(--gold);padding:10px 18px;display:flex;flex-wrap:wrap;align-items:center;gap:6px 18px}
.brand{color:#fff;font-weight:bold;font-size:1.05rem;margin-right:auto;letter-spacing:.3px}.brand small{display:block;color:var(--gold);font-weight:normal;font-size:.72rem;letter-spacing:1.5px;text-transform:uppercase}
.nav a.l{color:#e9edf5;text-decoration:none;font-size:.92rem;padding:5px 2px;border-bottom:2px solid transparent}
.nav a.l:hover{border-color:var(--gold)}.nav a.on{color:#fff;border-color:var(--gold)}
.nav a.pub{color:var(--gold);font-size:.85rem;text-decoration:none;border:1px solid var(--gold);border-radius:20px;padding:3px 12px}
.hero{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;padding:54px 22px 46px;text-align:center}
.hero h1{font-size:clamp(1.8rem,4.5vw,2.9rem);margin:0 0 10px;line-height:1.2}.hero p{max-width:720px;margin:0 auto;font-size:1.12rem;color:#dfe6f2}
.hero .eyebrow{color:var(--gold);letter-spacing:2px;text-transform:uppercase;font-size:.78rem;margin-bottom:10px}
.wrap{max-width:1000px;margin:0 auto;padding:36px 20px 20px}
h2{color:var(--navy);font-size:1.55rem;margin:34px 0 8px;border-bottom:2px solid var(--gold);padding-bottom:6px}
h3{color:var(--navy);margin:0 0 4px;font-size:1.12rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:16px 0}
.card{background:#fff;border:1px solid var(--line);border-top:4px solid var(--gold);border-radius:8px;padding:16px 18px;box-shadow:0 2px 6px rgba(18,40,76,.06)}
.card p{margin:4px 0 0;color:var(--mut);font-size:.96rem}
.step{display:flex;gap:14px;background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px 18px;margin:12px 0}
.num{flex:0 0 42px;height:42px;border-radius:50%;background:var(--navy);color:var(--gold);font-weight:bold;display:flex;align-items:center;justify-content:center;font-size:1.2rem}
.step p{margin:3px 0 0;color:var(--mut)}.step strong{color:var(--navy)}
.cta{text-align:center;margin:36px 0 8px}
.btn{display:inline-block;background:var(--gold);color:var(--navy);font-weight:bold;text-decoration:none;padding:13px 30px;border-radius:30px;font-size:1.05rem;border:0}
.btn.soon{opacity:.85}.note{color:var(--mut);font-size:.9rem;text-align:center;margin-top:8px}
.scrip{background:#fff;border-left:4px solid var(--gold);padding:10px 16px;margin:10px 0;font-style:italic}.scrip b{font-style:normal;color:var(--navy)}
.tag{display:inline-block;font-size:.72rem;letter-spacing:1px;text-transform:uppercase;background:var(--navy);color:var(--gold);border-radius:12px;padding:2px 10px;margin-bottom:6px}
.tag.free{background:var(--gold);color:var(--navy)}
ul.clean{padding-left:20px}ul.clean li{margin:5px 0}
.foot{margin:40px 0 0;padding:20px;text-align:center;color:#c8d1e0;background:var(--navy);font-size:.85rem}.foot a{color:var(--gold)}
@media(max-width:560px){.nav{padding:8px 12px}.nav a.l{font-size:.85rem}.step{flex-direction:column}}
"""
NAV_CSS = """/*nav*/
.nav .dd{position:relative}
.nav .dd>button{background:none;border:0;border-bottom:2px solid transparent;color:#e9edf5;font:inherit;font-size:.92rem;padding:5px 2px;cursor:pointer}
.nav .dd>button::after{content:" \\25BE";color:var(--gold);font-size:.8em}
.nav .dd>button:hover,.nav .dd.on>button{color:#fff;border-color:var(--gold)}
.nav .menu{display:none;position:absolute;left:-10px;top:100%;min-width:210px;background:#fff;border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:0 0 8px 8px;box-shadow:0 10px 24px rgba(18,40,76,.22);padding:6px 0;z-index:30}
.nav .menu a{display:block;padding:10px 18px;color:var(--navy);text-decoration:none;font-size:.97rem;white-space:nowrap}
.nav .menu a:hover{background:var(--cream)}
.nav .menu a.on{background:var(--cream);font-weight:bold;border-left:3px solid var(--gold);padding-left:15px}
.nav .dd.open .menu{display:block}
@media(hover:hover){.nav .dd:hover .menu{display:block}}
@media(max-width:560px){.nav .dd{position:static}.nav .menu{left:12px;right:12px;min-width:0}.nav .dd>button{font-size:.88rem}}
/*/nav*/"""
NAV_JS = """<!--navjs--><script>
document.querySelectorAll('.nav .dd>button').forEach(function(b){
  b.addEventListener('click',function(e){
    e.stopPropagation();var d=b.parentNode,o=!d.classList.contains('open');
    document.querySelectorAll('.nav .dd').forEach(function(x){x.classList.remove('open');x.firstChild.setAttribute('aria-expanded','false');});
    if(o){d.classList.add('open');b.setAttribute('aria-expanded','true');}
  });
});
document.addEventListener('click',function(){document.querySelectorAll('.nav .dd.open').forEach(function(x){x.classList.remove('open');});});
</script><!--/navjs-->"""
def nav(active):
    # These pages sit in a Wix embed. Counselor links stay in the box. Public links open a new tab.
    # The free-week button messages the parent page; the embed sandbox blocks target="_top".
    current = active + '.html'
    groups = [
        ("Welcome", [("Welcome", "welcome.html")]),
        ("Learn", [("The Process", "process.html"),
                   ("Theory Topics", "theory.html"),
                   ("Professional Tips", "tips.html")]),
        ("Practice", [("Case Studies", "cases.html"),
                      ("The Course", "course.html")]),
        ("Resources", [("Clinical Library", "library.html"),
                       ("Articles", "articles.html")]),
    ]
    outside = [
        ("False Belief Finder \u2197", SITE + "/false-belief-finder"),
        ("Public Site \u2197", SITE),
    ]
    out = ['<!--nav--><div class="nav"><div class="brand">Belief Counseling<small>For Counselors</small></div>']
    for label, pages in groups:
        if len(pages) == 1:
            t, f = pages[0]
            out.append('<a class="l%s" href="%s">%s</a>' % (' on' if f == current else '', f, t))
            continue
        here = any(f == current for _, f in pages)
        items = ''.join('<a%s href="%s">%s</a>' % (' class="on"' if f == current else '', f, t) for t, f in pages)
        out.append('<div class="dd%s"><button type="button" aria-haspopup="true" aria-expanded="false">%s</button><div class="menu">%s</div></div>' % (' on' if here else '', label, items))
    for t, u in outside:
        out.append('<a class="pub" target="_blank" rel="noopener" href="%s">%s</a>' % (u, t))
    out.append('</div><!--/nav-->')
    return ''.join(out)
FOOT='<div class="foot">Educational training for counselors. Never enter real client names or details. · Scripture quotations: Berean Standard Bible (BSB), public domain. · © Brian Campbell, Ph.D.</div>'
def page(key,title,hero_sub,body,eyebrow='Belief Counseling for Counselors', extra_css='', with_nav=True):
    # with_nav=False is a standalone embed (no menu, no outside links, no script).
    # counselor_nav.py leaves files marked <!--standalone--> alone.
    nav_css = NAV_CSS if with_nav else ''
    top = nav(key) if with_nav else '<!--standalone-->'
    js = NAV_JS if with_nav else ''
    h='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s%s%s'%(html.escape(title),CSS,extra_css,nav_css)
    h+='\n</style></head><body>'
    h+=top+'<div class="hero"><div class="eyebrow">%s</div><h1>%s</h1><p>%s</p></div><div class="wrap">%s</div>%s%s</body></html>'%(eyebrow,title,hero_sub,body,FOOT,js)
    (OUT/('%s.html'%key)).write_text(h)
def cards(items, extra=''): return '<div class="grid">'+''.join('<div class="card"><h3>%s</h3><p>%s</p></div>'%i for i in items)+extra+'</div>'
JOIN='<div class="cta"><a class="btn soon" target="_blank" href="https://doctorishome.wixstudio.com/website-6/blank-11#clinical-companion" onclick="window.parent.postMessage({type:\'cc-start-free-week\'}, \'*\'); return false;">Start your free week</a><div class="note">One week free, then $29.25 a month.</div></div>'

# 1 Welcome
WELCOME_CSS = '''/*reviews*/
.grid>.card:last-child{grid-column:1 / -1}
.card .pdfs{margin:12px 0 0;display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.card .pdfs a{color:var(--navy2);font-weight:bold}
/*/reviews*/
'''
DSM_CARD = ('<div class="card"><h3>DSM-5-TR Reviews</h3>'
 '<p>Condensed teaching reviews of major DSM-5-TR disorders: key features, the most effective treatments with special attention to CBT, and research on Christian-integrated care, with full references.</p>'
 '<p class="pdfs"><a href="reviews/depression-teaching-overview.pdf" target="_blank" rel="noopener">Depression: A DSM-5-TR Teaching Overview (PDF)</a>'
 '<a href="reviews/anxiety-teaching-overview.pdf" target="_blank" rel="noopener">Anxiety Disorders: A DSM-5-TR Teaching Overview (PDF)</a></p></div>')
page('welcome','Welcome to the Counselors’ Room','Learn Christian cognitive-behavioral Belief Therapy from a psychologist with 35 years of clinical experience, and practice it on guided cases before you meet your next client.',
 '<h2>What you will find inside</h2>'+cards([
 ('Professional Tips','Short, practical teaching from Dr. Campbell’s years in practice, delivered weekly to your inbox and kept in a searchable archive.'),
 ('The Process','The three steps of Belief Counseling (Identify, Challenge, Replace), with the reason behind each one, from Assess through Reinforce.'),
 ('Theory Topics','A framework for understanding the great majority of psychological struggles: beliefs, personality, and the whole person.'),
 ('Case Studies','Practice on composite cases guided by an AI supervisor trained on Dr. Campbell’s method. Start with a free week; then $29.25 a month, cancel anytime.'),
 ('The Course','A step-by-step course in Christian Cognitive-Behavioral Therapy, with quizzes and a certificate of completion.'),
 ('Clinical Library','Counselor-only background, assessment tools, and references behind every false-belief card on the public site.')], DSM_CARD)+
 '<h2>How it works</h2>'
 '<div class="step"><div class="num">1</div><div><strong>Start with a free week; then $29.25 a month, cancel anytime.</strong><p>You get the tips, the library, and the theory topics right away.</p></div></div>'
 '<div class="step"><div class="num">2</div><div><strong>Try a practice case during your free week.</strong><p>Walk a composite client through Identify, Challenge, and Replace. Your supervisor pauses for your answer before showing the model approach.</p></div></div>'
 '<div class="step"><div class="num">3</div><div><strong>Keep growing.</strong><p>Add more cases in sets of five, work through the course, and earn your certificate of completion.</p></div></div>'
 '<h2>About Dr. Campbell</h2><p>Brian Campbell, Ph.D., has spent 35 years in private practice, teaching, and writing. Belief Therapy grew from that work: a Christian cognitive-behavioral approach that helps clients name the lies behind their pain and replace them with truth from God’s Word.</p>'
 '<div class="scrip">“Do not be conformed to this world, but be transformed by the renewing of your mind.” <b>Romans 12:2</b></div>'+JOIN,
 extra_css=WELCOME_CSS)
# 2 Process
FLOW_CSS = r'''/*flow*/
.flow{display:flex;align-items:stretch;margin:22px 0 10px}
.fb{flex:1 1 0;min-width:0;border-radius:10px;padding:14px 10px;text-align:center;background:#fff;border:1px solid var(--line);box-shadow:0 2px 6px rgba(18,40,76,.06)}
.fb h3{font-size:1.02rem;margin:0 0 6px}.fb p{margin:0;font-size:.86rem;line-height:1.4;color:var(--mut)}
.fb .n{display:inline-block;width:30px;height:30px;line-height:30px;border-radius:50%;background:var(--gold);color:var(--navy);font-weight:bold;margin-bottom:6px}
.fb.start{background:var(--cream);border-style:dashed}
.fb.mine{border:2px solid var(--navy)}
.fb.step3{background:var(--navy);border-color:var(--navy)}.fb.step3 h3{color:#fff}.fb.step3 p{color:#dfe6f2}
.fb.end{background:var(--gold);border-color:var(--gold)}.fb.end h3{color:var(--navy)}.fb.end p{color:var(--navy)}
.ar{flex:0 0 24px;display:flex;align-items:center;justify-content:center;color:var(--gold);font-size:1.5rem;font-weight:bold}
.ar::before{content:"\2192"}
.loop{margin:4px 0 6px;text-align:center;color:var(--navy);font-size:.95rem;border:1px dashed var(--gold);border-radius:8px;padding:8px 12px;background:#fff}
.stage{background:#fff;border:1px solid var(--line);border-left:5px solid var(--navy);border-radius:8px;padding:16px 20px;margin:14px 0}
.stage h3{font-size:1.2rem;margin:0 0 6px}.stage ul{margin:6px 0 8px;padding-left:22px}.stage li{margin:3px 0}
.stage .why{margin:0;color:var(--mut);font-style:italic}
.stage.pre{border-left-color:var(--gold)}
.btn2{display:inline-block;margin:8px;color:var(--navy);font-weight:bold;text-decoration:none;padding:12px 26px;border:2px solid var(--navy);border-radius:30px}
@media(max-width:820px){.flow{flex-direction:column}.ar{flex-basis:30px}.ar::before{content:"\2193"}.fb{padding:12px 14px}}
@media print{.nav,.cta,.foot{display:none}.hero{padding:18px;-webkit-print-color-adjust:exact;print-color-adjust:exact}body{background:#fff}.fb,.stage,.scrip{break-inside:avoid;-webkit-print-color-adjust:exact;print-color-adjust:exact}.flow{flex-direction:row}.ar::before{content:"\2192"}}
/*/flow*/
'''
PROCESS_BODY = '''<h2>The flow of Belief Counseling</h2><p>Every client moves through the same path. Belief Mining uncovers the beliefs; the three steps change them.</p>
<div class="flow" role="img" aria-label="Flow diagram: Presenting problem, then Belief Mining, then 1 Identify, 2 Challenge, 3 Replace, resulting in The truth sets you free">
<div class="fb start"><h3>Presenting Problem</h3><p>Why the client came: the distress, the symptoms, the story</p></div><div class="ar"></div>
<div class="fb mine"><h3>Belief Mining</h3><p>Dig through six levels to find what the client believes</p></div><div class="ar"></div>
<div class="fb step3"><div class="n">1</div><h3>Identify</h3><p>Name the false belief in the client’s own words</p></div><div class="ar"></div>
<div class="fb step3"><div class="n">2</div><h3>Challenge</h3><p>Question it, refute it, and test it</p></div><div class="ar"></div>
<div class="fb step3"><div class="n">3</div><h3>Replace</h3><p>Put biblical truth in its place and practice it</p></div><div class="ar"></div>
<div class="fb end"><h3>The Truth Sets You Free</h3><p>The result of the three steps (John 8:32)</p></div>
</div>
<p class="loop">&#8634; When another false belief comes to light, return to Belief Mining and Step 1, and work through the steps again.</p>
<h2>Each part of the flow</h2>
<div class="stage pre"><h3>Belief Mining</h3><p>Start with the presenting problem, then gather the whole story and look for the beliefs beneath it at six levels:</p><ul><li>Biological</li><li>Psychological/Cognitive</li><li>Interpersonal</li><li>Socioeconomic</li><li>Sociocultural</li><li>Spiritual/Religious</li></ul><p class="why">Why: You cannot find the right belief until you know the person.</p></div>
<div class="stage"><h3>1. Identify False Beliefs</h3><ul><li>Put the specific false belief into words, in the client’s own language.</li><li>Check it against the 22 Core False Beliefs and the Spiritual/Religious False Beliefs.</li><li>Choose the belief that, if changed, would bring the greatest relief.</li></ul><p class="why">Why: You cannot challenge a belief you haven’t named.</p></div>
<div class="stage"><h3>2. Challenge False Beliefs</h3><ul><li><strong>Questioning:</strong> ask general and Christian questions that let the client examine the belief for themselves.</li><li><strong>Refuting:</strong> weigh the belief against evidence, Scripture, logic, and the client’s own experience.</li><li><strong>Behavioral experiments:</strong> do something differently and see what actually happens.</li></ul><p class="why">Why: A belief held for years needs more than a gentle doubt.</p></div>
<div class="stage"><h3>3. Replace False Beliefs</h3><ul><li>Replace the lie with biblical truth, such as “I am imperfect, but deeply loved by God.”</li><li>Use the Scriptural Truths for the belief, and Pearls Scripture Search for more.</li><li>Practice the truth with homework: Scripture memory, reminder cards, songs, listening, and journaling.</li><li>Review progress, belief strength, and remaining triggers.</li></ul><p class="why">Why: Removing a lie leaves a gap; truth must take its place, and beliefs change through repetition.</p></div>
<div class="stage" style="border-left-color:var(--gold);background:var(--cream)"><h3>The Truth Sets You Free</h3><p style="margin:0">Freedom is not a fourth step. It is what happens when a lie is identified, challenged, and replaced with God’s truth.</p></div>
<h2>Key Scriptures</h2><div class="scrip">“Do not be conformed to this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what is the good, pleasing, and perfect will of God.” <b>Romans 12:2</b></div><div class="scrip">“We tear down arguments and every presumption set up against the knowledge of God; and we take captive every thought to make it obedient to Christ.” <b>2 Corinthians 10:5</b></div><div class="scrip">“Then you will know the truth, and the truth will set you free.” <b>John 8:32</b></div><div class="scrip">“I have hidden Your word in my heart that I might not sin against You.” <b>Psalm 119:11</b></div><div class="scrip">“All Scripture is God-breathed and is useful for instruction, for conviction, for correction, and for training in righteousness.” <b>2 Timothy 3:16</b></div><div class="cta"><a class="btn" href="cases.html">Practice the process on a case</a><a class="btn2" href="Belief-Counseling-Flow.pdf" target="_blank" rel="noopener">Download as PDF</a></div>'''
page('process','The Process','Three steps: Identify, Challenge, and Replace. The result: the truth sets you free.',PROCESS_BODY,extra_css=FLOW_CSS)
# 3 Tips
page('tips','Professional Tips','Practical teaching from 35 years of clinical experience, delivered to you and kept here for reference.',
 '<h2>How the Tips work</h2><p>New tips arrive by email on a regular schedule, and every tip is saved here in a searchable archive, organized by topic.</p>'
 '<h2>Topics you can expect</h2><ul class="clean"><li>Beliefs and how they shape feelings and behavior</li><li>Working with anxiety and depression</li><li>Parental messages and the beliefs children absorb</li><li>Core lies: worthlessness, abandonment, failure</li><li>Cognitive errors and how to name them</li><li>Using Scripture in counseling, wisely and well</li><li>Homework that clients actually do</li><li>Ethics, scope of practice, and knowing when to refer</li></ul>'
 '<div class="card"><span class="tag">Coming soon</span><h3>Your first tip</h3><p>The tip archive opens when membership begins.</p></div>')
# 4 Theory
page('theory','Theory Topics','A framework for understanding the great majority of psychological struggles.',
 '<h2>The big ideas</h2>'+cards([('Beliefs Shape Personality','Personality as a set of beliefs passed on, learned, and changed; biology plays a part too.'),
 ('Levels of Analysis','The whole person: biological, psychological, interpersonal, socioeconomic, sociocultural, and spiritual.'),
 ('Parental Patterns','How the messages children receive become the beliefs adults live by.'),
 ('Cognitive Errors','The thinking habits that hold false beliefs in place.'),
 ('Core Beliefs and Personality Patterns','How deep beliefs show up as enduring patterns of relating and coping.'),
 ('Integration of Faith and Psychology','Principles for combining Scripture and the science of counseling responsibly.')])+
 '<div class="card"><span class="tag">Coming soon</span><h3>Full articles</h3><p>Each topic will open as a full teaching article for members.</p></div>')
# 5 Cases
cats=['Depression and Hopelessness','Anxiety and Panic','Trauma and Abuse History','Marital and Relational Conflict','Grief and Loss','Addiction and Self-Destructive Patterns','Spiritual Crisis','Shame and Guilt','Personality Patterns','Serious Mental Illness (supporting medical care)']
page('cases','Case Studies','Practice Identify, Challenge, and Replace on composite cases, guided by an AI supervisor trained on Dr. Campbell’s method.',
 '<h2>How practice works</h2><div class="step"><div class="num">1</div><div><strong>You choose a case.</strong><p>Pick the type of case that matches your caseload. No random assignments.</p></div></div>'
 '<div class="step"><div class="num">2</div><div><strong>You work each step.</strong><p>The supervisor pauses and asks for your thinking before showing the model approach, and offers a help menu if you are stuck.</p></div></div>'
 '<div class="step"><div class="num">3</div><div><strong>You keep a clean summary.</strong><p>Each case ends with a summary of the model path and a short quiz you can review later.</p></div></div>'
 '<h2>Pricing</h2><div class="grid"><div class="card"><span class="tag free">Free</span><h3>Your first case</h3><p>Included with membership.</p></div><div class="card"><span class="tag">Sets of five</span><h3>More cases</h3><p>Add cases in sets of five whenever you are ready. Pricing to be announced.</p></div></div>'
 '<h2>Case categories</h2><ul class="clean">'+''.join('<li>%s</li>'%c for c in cats)+'</ul>'
 '<p><strong>Important:</strong> all cases are fictional composites. Never enter real client names or details.</p>')
# 6 Course
secs=['Welcome and How This Course Works','The Process: Identify, Challenge, Replace','Levels of Analysis: The Whole Person','Assess and Identify: Finding the Lies','Hypothesize and Question','Refute and Replace','Rehearse and Reinforce','Core Beliefs and Personality Patterns','Safety, Ethics, and Scope of Practice','Practice Cases and Final Review']
page('course','Christian Cognitive-Behavioral Therapy: The Course','A step-by-step course in Belief Therapy, with quizzes, practice cases, and a certificate of completion.',
 '<h2>Course outline</h2>'+''.join('<div class="step"><div class="num">%d</div><div><strong>%s</strong></div></div>'%(i+1,s) for i,s in enumerate(secs))+
 '<div class="card"><span class="tag">Coming soon</span><h3>Certificate of completion</h3><p>Finish the lessons and quizzes to receive a certificate of completion from Dr. Campbell.</p></div>')
# 7 Library
page('library','Clinical Library','Counselor-only background, tools, and references.',
 '<h2>Assessment tools</h2><ul class="clean"><li>Adult History Questionnaire</li><li>Christian Experiences and Beliefs Inventory</li><li>Parental Messages checklist</li><li>Life Events and Beliefs Screening</li><li>Anxious Thoughts and Beliefs checklist</li><li>Depressive Thoughts and Beliefs checklist</li><li>Discover the Lies worksheet</li><li>Questioning Your Beliefs worksheet</li></ul>'
 '<h2>Clinical background for the belief cards</h2><p>Each public false-belief card links to a counselor note on origins, cognitive errors, and treatment approach. Members will find them organized by category: Spiritual/Religious, Psychological/Cognitive, Interpersonal, Socioeconomic, Sociocultural, and Biological/Physical.</p>'
 '<h2>Recommended reading</h2><ul class="clean"><li>Beck, Davis, and Freeman, <em>Cognitive Therapy of Personality Disorders</em></li><li>Beck Institute Personality Belief Questionnaire materials</li></ul>'
 '<div class="card"><span class="tag">Coming soon</span><h3>Library opens with membership</h3><p>Documents will be added here in stages.</p></div>')
# 8 Clinical Companion (member embed: no menu, no script).
# The client-forms button opens practice-forms.html in a new tab so a Wix iframe does not block the download.
CC_CSS = '''/*cc*/
.card p{margin:0;color:var(--ink);font-size:1.02rem}
.pill{display:inline-block;margin-top:14px;padding:7px 16px;border-radius:20px;background:#ece7da;color:#6d7686;font-size:.85rem;font-weight:bold;letter-spacing:.4px;border:1px solid #ddd4c0;cursor:default;user-select:none}
ol.clean{list-style:none;margin:16px 0;padding:0;counter-reset:step}
ol.clean li{counter-increment:step;display:flex;gap:14px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px 18px;margin:12px 0}
ol.clean li::before{content:counter(step);flex:0 0 42px;height:42px;border-radius:50%;background:var(--navy);color:var(--gold);font-weight:bold;display:flex;align-items:center;justify-content:center;font-size:1.2rem}
.faq{margin:8px 0 4px}
.faq details{background:#fff;border:1px solid var(--line);border-top:4px solid var(--gold);border-radius:8px;margin:12px 0;box-shadow:0 2px 6px rgba(18,40,76,.06)}
.faq summary{color:var(--navy);font-weight:bold;font-size:1.05rem;padding:14px 46px 14px 18px;cursor:pointer;list-style:none;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::marker{content:""}
.faq summary::after{content:"+";position:absolute;right:16px;top:50%;transform:translateY(-50%);color:var(--gold);font-size:1.35rem;font-weight:bold;line-height:1}
.faq details[open] summary::after{content:"\u2212"}
.faq details p{margin:0;padding:0 18px 16px;color:var(--navy)}
.faq summary:hover{background:#fbf8f0}
.faq summary:focus{outline:2px solid var(--gold);outline-offset:-2px}
h2.forms-title{margin-top:22px}
.forms{display:flex;gap:18px;align-items:center;justify-content:space-between;margin:2px 0 4px}
.forms p{margin:0;flex:1 1 auto}
.forms .btn{flex:0 0 auto;white-space:nowrap;padding:11px 22px}
@media(max-width:640px){.forms{flex-direction:column;align-items:flex-start}.forms .btn{white-space:normal}}
@media(max-width:560px){ol.clean li{flex-direction:column;align-items:flex-start}}
/*/cc*/
'''
FAQS = [
 ("How does the free week work?", "Your first 7 days are free. If you don't cancel before the week ends, your membership continues at $29.25 a month."),
 ("How do I cancel?", "Sign in, open My Account, go to My Subscriptions, and choose Cancel. You can cancel anytime."),
 ("Will I get a refund if I cancel?", "Your access continues to the end of the month you've paid for. The remainder of the month isn't refunded. If you have special circumstances, contact us."),
 ("What happens to my access after I cancel?", "You keep full access until the end of your paid month. After that, the app and member resources are no longer available to you."),
 ("What does 'fair use' mean?", "Clinical Companion is meant for your own professional caseload. Sharing your account, or very heavy automated use, isn't permitted."),
 ("Who is Clinical Companion for?", "Professional counselors, psychologists, and students in training who want to integrate Christian belief counseling into their work."),
 ("What do I need to run it?", "A Windows computer and an internet connection."),
 ("Can I enter real client information?", "Use fictional or de-identified information unless your plan states otherwise."),
 ("How do I get help?", "Contact us through the Contact page and we'll get back to you."),
]
FAQ_HTML = '<h2>Frequently asked questions</h2><div class="faq">' + ''.join(
 '<details><summary>%s</summary><p>%s</p></details>' % pair for pair in FAQS) + '</div>'
page('clinical-companion','Clinical Companion',
 "Welcome to your Clinical Companion member area. Here you'll find the app download, a quick-start guide, help, and your account.",
 '<h2>Download the app</h2>'
 '<div class="card"><p>The Windows download will be available here when your membership begins.</p>'
 '<span class="pill">Coming soon</span></div>'
 '<h2>Quick start</h2><ol class="clean">'
 '<li>Install Clinical Companion and open it.</li>'
 '<li>Sign in with your website member login.</li>'
 '<li>Try a practice case before using it with clients.</li>'
 '<li>Write your session notes, then ask for an analysis.</li></ol>'
 '<h2 class="forms-title">Client Forms for Your Practice</h2>'
 '<div class="forms"><p>Enter your practice details once and download a New Client Packet and Confidentiality Agreement pre-filled with them. Review them with an attorney in your state.</p>'
 '<a class="btn" href="practice-forms.html" target="_blank" rel="noopener">Open client forms</a></div>'
 '<h2>Help</h2><p>Questions or problems? Contact us through the Contact page and we\'ll get back to you. For billing questions or special circumstances, contact us and we\'ll do our best to help.</p>'
 '<h2>Your account</h2><p>Manage your membership, payment method, or cancel anytime from My Account. Your access continues to the end of the month you\'ve paid for; the remainder of the month isn\'t refunded.</p>'
 + FAQ_HTML +
 '<h2>Terms of use</h2><p>Clinical Companion supports, and does not replace, your professional clinical judgment. Use fictional or de-identified information unless your plan states otherwise. Fair use applies; excessive use isn\'t permitted.</p>',
 eyebrow='MEMBERS', extra_css=CC_CSS, with_nav=False)
print('built',[p[0] for p in PAGES]+['clinical-companion'])
