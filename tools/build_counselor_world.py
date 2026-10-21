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
def nav(active):
    # These pages are shown inside a Wix embed box, which does not allow links to change the whole Wix page.
    # So counselor pages open inside the same box, and the public site opens in a new tab.
    ls=''.join('<a class="l%s" href="%s.html">%s</a>'%(' on' if k==active else '',k,t) for k,t,slug in PAGES)
    return '<div class="nav"><div class="brand">Belief Counseling<small>For Counselors</small></div>%s<a class="pub" target="_blank" rel="noopener" href="%s/false-belief-finder">False Belief Finder ↗</a><a class="pub" target="_blank" rel="noopener" href="%s">Public Site ↗</a></div>'%(ls,SITE,SITE)
FOOT='<div class="foot">Educational training for counselors. Never enter real client names or details. · Scripture quotations: Berean Standard Bible (BSB), public domain. · © Brian Campbell, Ph.D.</div>'
def page(key,title,hero_sub,body,eyebrow='Belief Counseling for Counselors'):
    h='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head><body>'%(html.escape(title),CSS)
    h+=nav(key)+'<div class="hero"><div class="eyebrow">%s</div><h1>%s</h1><p>%s</p></div><div class="wrap">%s</div>%s</body></html>'%(eyebrow,title,hero_sub,body,FOOT)
    (OUT/('%s.html'%key)).write_text(h)
def cards(items): return '<div class="grid">'+''.join('<div class="card"><h3>%s</h3><p>%s</p></div>'%i for i in items)+'</div>'
JOIN='<div class="cta"><span class="btn soon">Join the Counselors’ Room</span><div class="note">Membership opens soon. Monthly membership; your first practice case is free.</div></div>'

# 1 Welcome
page('welcome','Welcome to the Counselors’ Room','Learn Christian cognitive-behavioral Belief Therapy from a psychologist with 35 years of clinical experience, and practice it on guided cases before you meet your next client.',
 '<h2>What you will find inside</h2>'+cards([
 ('Professional Tips','Short, practical teaching from Dr. Campbell’s years in practice, delivered weekly to your inbox and kept in a searchable archive.'),
 ('The Process','The eight steps of Belief Therapy, with the reason behind each one, from Assess through Reinforce.'),
 ('Theory Topics','A framework for understanding the great majority of psychological struggles: beliefs, personality, and the whole person.'),
 ('Case Studies','Practice on composite cases guided by an AI supervisor trained on Dr. Campbell’s method. Your first case is free.'),
 ('The Course','A step-by-step course in Christian Cognitive-Behavioral Therapy, with quizzes and a certificate of completion.'),
 ('Clinical Library','Counselor-only background, assessment tools, and references behind every false-belief card on the public site.')])+
 '<h2>How it works</h2>'
 '<div class="step"><div class="num">1</div><div><strong>Join for a small monthly membership.</strong><p>You get the tips, the library, and the theory topics right away.</p></div></div>'
 '<div class="step"><div class="num">2</div><div><strong>Try your first practice case free.</strong><p>Walk a composite client through the eight steps. Your supervisor pauses for your answer before showing the model approach.</p></div></div>'
 '<div class="step"><div class="num">3</div><div><strong>Keep growing.</strong><p>Add more cases in sets of five, work through the course, and earn your certificate of completion.</p></div></div>'
 '<h2>About Dr. Campbell</h2><p>Brian Campbell, Ph.D., has spent 35 years in private practice, teaching, and writing. Belief Therapy grew from that work: a Christian cognitive-behavioral approach that helps clients name the lies behind their pain and replace them with truth from God’s Word.</p>'
 '<div class="scrip">“Do not be conformed to this world, but be transformed by the renewing of your mind.” <b>Romans 12:2</b></div>'+JOIN)
# 2 Process
steps=[('Assess','Gather the whole story: the presenting problem, family and parental patterns, Christian background, and functioning across the biological, psychological, interpersonal, socioeconomic, sociocultural, and spiritual levels.','You cannot find the right belief until you know the person.'),
('Identify','Surface the specific false beliefs driving the distress, in the client’s own words.','You cannot attack a belief you haven’t named.'),
('Hypothesize','Decide which belief, if changed, would bring the greatest shift.','Not every lie carries equal weight; start where change matters most.'),
('Question','Ask spiritual and general questions that invite the client to examine the belief for themselves.','Questions let clients discover the flaw instead of being told.'),
('Refute','Argue against the false belief with evidence, Scripture, logic, and the client’s own experience.','A belief held for years needs more than a gentle doubt.'),
('Replace','Build a replacement belief grounded in biblical truth, such as “I am imperfect but deeply loved by God.”','Removing a lie leaves a gap; truth must take its place.'),
('Rehearse','Assign homework: Scripture memory, reminder cards, reading, listening, and small behavioral experiments.','Beliefs change through repetition.'),
('Reinforce','Review progress, belief strength, remaining triggers, and spiritual growth.','Gains last when they are reviewed and protected.')]
body='<h2>The eight steps</h2><p>Each step has a purpose. In training, you will learn what to do and why it works.</p>'+''.join('<div class="step"><div class="num">%d</div><div><strong>%s</strong><p>%s</p><p><em>Why: %s</em></p></div></div>'%(i+1,a,b,c) for i,(a,b,c) in enumerate(steps))
body+='<h2>Key Scriptures</h2><div class="scrip">“Do not be conformed to this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what is the good, pleasing, and perfect will of God.” <b>Romans 12:2</b></div><div class="scrip">“We tear down arguments and every presumption set up against the knowledge of God; and we take captive every thought to make it obedient to Christ.” <b>2 Corinthians 10:5</b></div><div class="scrip">“Then you will know the truth, and the truth will set you free.” <b>John 8:32</b></div><div class="scrip">“I have hidden Your word in my heart that I might not sin against You.” <b>Psalm 119:11</b></div><div class="scrip">“All Scripture is God-breathed and is useful for instruction, for conviction, for correction, and for training in righteousness.” <b>2 Timothy 3:16</b></div>'
body+='<div class="cta"><a class="btn" href="cases.html">Practice the process on a case</a></div>'
page('process','The Process','The eight steps of Belief Therapy, and the reason behind each one.',body)
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
page('cases','Case Studies','Practice the eight steps on composite cases, guided by an AI supervisor trained on Dr. Campbell’s method.',
 '<h2>How practice works</h2><div class="step"><div class="num">1</div><div><strong>You choose a case.</strong><p>Pick the type of case that matches your caseload. No random assignments.</p></div></div>'
 '<div class="step"><div class="num">2</div><div><strong>You work each step.</strong><p>The supervisor pauses and asks for your thinking before showing the model approach, and offers a help menu if you are stuck.</p></div></div>'
 '<div class="step"><div class="num">3</div><div><strong>You keep a clean summary.</strong><p>Each case ends with a summary of the model path and a short quiz you can review later.</p></div></div>'
 '<h2>Pricing</h2><div class="grid"><div class="card"><span class="tag free">Free</span><h3>Your first case</h3><p>Included with membership.</p></div><div class="card"><span class="tag">Sets of five</span><h3>More cases</h3><p>Add cases in sets of five whenever you are ready. Pricing to be announced.</p></div></div>'
 '<h2>Case categories</h2><ul class="clean">'+''.join('<li>%s</li>'%c for c in cats)+'</ul>'
 '<p><strong>Important:</strong> all cases are fictional composites. Never enter real client names or details.</p>')
# 6 Course
secs=['Welcome and How This Course Works','The Process: The Eight Steps of Belief Therapy','Levels of Analysis: The Whole Person','Assess and Identify: Finding the Lies','Hypothesize and Question','Refute and Replace','Rehearse and Reinforce','Core Beliefs and Personality Patterns','Safety, Ethics, and Scope of Practice','Practice Cases and Final Review']
page('course','Christian Cognitive-Behavioral Therapy: The Course','A step-by-step course in Belief Therapy, with quizzes, practice cases, and a certificate of completion.',
 '<h2>Course outline</h2>'+''.join('<div class="step"><div class="num">%d</div><div><strong>%s</strong></div></div>'%(i+1,s) for i,s in enumerate(secs))+
 '<div class="card"><span class="tag">Coming soon</span><h3>Certificate of completion</h3><p>Finish the lessons and quizzes to receive a certificate of completion from Dr. Campbell.</p></div>')
# 7 Library
page('library','Clinical Library','Counselor-only background, tools, and references.',
 '<h2>Assessment tools</h2><ul class="clean"><li>Adult History Questionnaire</li><li>Christian Experiences and Beliefs Inventory</li><li>Parental Messages checklist</li><li>Life Events and Beliefs Screening</li><li>Anxious Thoughts and Beliefs checklist</li><li>Depressive Thoughts and Beliefs checklist</li><li>Discover the Lies worksheet</li><li>Questioning Your Beliefs worksheet</li></ul>'
 '<h2>Clinical background for the belief cards</h2><p>Each public false-belief card links to a counselor note on origins, cognitive errors, and treatment approach. Members will find them organized by category: Spiritual/Religious, Psychological/Cognitive, Interpersonal, Socioeconomic, Sociocultural, and Biological/Physical.</p>'
 '<h2>Recommended reading</h2><ul class="clean"><li>Beck, Davis, and Freeman, <em>Cognitive Therapy of Personality Disorders</em></li><li>Beck Institute Personality Belief Questionnaire materials</li></ul>'
 '<div class="card"><span class="tag">Coming soon</span><h3>Library opens with membership</h3><p>Documents will be added here in stages.</p></div>')
print('built',[p[0] for p in PAGES])
