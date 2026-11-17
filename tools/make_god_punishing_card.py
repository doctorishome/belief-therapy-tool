"""One example Spiritual/Religious card: “God is punishing me.”

Same page parts as the psychological cards (Psych-031 and later): origins,
Scripture, also-see, self-statements, logical errors, questions, truth,
Pearls, Godly Counsel, Christlike, both talks, four songs, homework, tracker,
song journal, truth card, prayer, and the share button (added after).

Scripture is taken from tools/BSB.txt through tools/build_cards.py.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_cards import load_bible, scripture  # noqa: E402

OUT = ROOT / "belief-cards/Belief-001-God-Is-Punishing-Me-For-My-Sins.html"
SRC = ROOT / "belief-cards/psychological/Psych-031-My-Situation-Is-Hopeless.html"
CAT = __import__("json").loads((ROOT / "tools/music-catalog.json").read_text())
PEARLS = __import__("json").loads((ROOT / "tools/pearls-topics.json").read_text())
GC = __import__("json").loads((ROOT / "tools/godly-counsel-chapters.json").read_text())
PB = "https://www.beliefcounselor.com/scriptures?topic="
GCB = "https://doctorishome.github.io/belief-therapy-tool/belief-cards/godly-counsel/"
DEP = "https://music.wixstatic.com/mp3/dbdded_149606a27908493da01ac9492fb18ab1.mp3"
ANX = "https://music.wixstatic.com/mp3/dbdded_f67d414544534727acf6973d58189443.mp3"
BELIEF = "God is punishing me."
SHOWN = "“" + BELIEF + "”"

bible = load_bible()


def qref(ref):
    text = scripture(ref, bible)
    if text.endswith("."):
        text = text[:-1]
    return "<q>%s</q> <span class=\"ref\">(%s)</span>." % (html.escape(text), ref)


def ul(items):
    return "<ul>\n" + "\n".join("<li>%s</li>" % x for x in items) + "\n</ul>"


def opts(items):
    return "<ul class=\"opts\">\n" + "\n".join("<li>%s</li>" % x for x in items) + "\n</ul>"


def song(key, why):
    vid, title, art, kind, _ = CAT[key]
    if kind not in ("contemporary", "classic"):
        raise SystemExit(key)
    return (
        '<a class="song" href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">'
        '<span class="thumb" style="background-image:url(\'https://i.ytimg.com/vi/%s/hqdefault.jpg\')"></span>'
        '<span class="txt"><span class="st">%s</span><span class="sa">%s</span><span class="sw">%s</span></span></a>'
        % (vid, vid, html.escape(title), html.escape(art), html.escape(why))
    )


def audio(title, url, minutes):
    return (
        "<h2>Listen: %s</h2>\n<div class=\"audio\">\n"
        "<p class=\"atitle\"><a href=\"%s\" target=\"_blank\" rel=\"noopener\">%s</a> "
        "<span>· Dr. Brian Campbell · %s</span></p>\n"
        "<audio controls preload=\"none\" src=\"%s\">Your browser can’t play this here. "
        "<a href=\"%s\">Open the recording</a>.</audio>\n"
        "<p class=\"aload\" hidden>Starting the recording… it is a long one, so it may take a few seconds to begin.</p>\n"
        "<p class=\"anote\">Press play to listen here, or tap the title to open it on its own.</p>\n</div>"
        % (title, url, title, minutes, url, url)
    )


def gc_link(n):
    title = GC[str(n)][0]
    slug = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")
    return '<li><a href="%sGC-%02d-%s.pdf" target="_blank" rel="noopener">%s</a></li>' % (
        GCB, n, slug, html.escape(title))


KEY = "Romans 8:1"
ALSO = ["Psalm 103:10–12", "Isaiah 53:5", "1 John 1:9", "John 9:1–3"]
PEARL_SLUGS = ["forgiveness", "god-all-loving", "grace", "guilt-shame", "suffering"]
READING = "forgiveness"
for s in PEARL_SLUGS + [READING]:
    if s not in PEARLS:
        raise SystemExit("pearl " + s)

songs = [
    ("east", "God removes sin as far as the east is from the west. He is not keeping a ledger to punish you."),
    ("messiah", "The punishment that brought peace was laid on Jesus, not stored up for you."),
    ("grace", "Grace means the rescue is His work, not a penalty you finish paying."),
    ("amazing", "This hymn locates hope in grace, not in earning your way out of punishment."),
]
kinds = [CAT[k][3] for k, _ in songs]
if kinds.count("classic") != 1 or len(songs) != 4:
    raise SystemExit(kinds)

questions = [
    "What, exactly, do I think God is punishing me for?",
    "If I have confessed that sin, what does 1 John 1:9 say He does?",
    "Is this trouble proof of punishment, or a hard thing that happens in a broken world?",
    "What did Jesus already carry, according to Isaiah 53:5?",
    "How is a Father’s loving discipline different from payback?",
    "What would I tell a friend who said God was punishing them for the same trouble?",
]
truths = [
    "In Christ there is now no condemnation for me.",
    "Jesus took the punishment that brought me peace.",
    "God has not dealt with me according to my sins.",
    "A hard season is not proof that God is paying me back.",
    "When I confess, He forgives and cleanses.",
    "The Lord’s discipline is love, not revenge.",
]
actions = [
    "<strong>Name the charge.</strong> Write the sin you think God is punishing, then write 1 John 1:9 beside it and note whether you have confessed it.",
    "<strong>Separate trouble from a sentence.</strong> List the hardship, then one other explanation Scripture allows: a broken world, someone else’s sin, a natural consequence, or a Father’s training.",
    "<strong>Read Romans 8:1 aloud</strong> each morning for seven days before you interpret the day.",
    "<strong>Say it out loud to one safe believer:</strong> “I have been sure God is punishing me,” and ask them to pray Romans 8:1 with you.",
]
errs = [
    ("Emotional reasoning", "Feeling condemned and treating the feeling as God’s verdict."),
    ("Personalization", "Taking a hardship many people face and reading it as a sentence aimed at me."),
    ("All-or-nothing thinking", "If I am not being blessed, I must be being punished."),
    ("Discounting the positive", "Ignoring the cross, forgiveness, and care that are already true."),
]
self_statements = [
    "This sickness, this loss, or this closed door is God paying me back.",
    "If I were right with God, this would not be happening.",
    "He is finished with me.",
    "I deserve every bad thing that comes.",
    "Other people get mercy. I get punishment.",
    "If I suffer long enough, maybe He will finally be satisfied.",
]

teaches = (
    "Scripture takes sin seriously, and it does not say that God is now punishing "
    "the person who belongs to Christ for sins Jesus already carried. "
    "Romans 8:1 says, “Therefore, there is now no condemnation for those who are in Christ Jesus.” "
    "Psalm 103:10 says, “He has not dealt with us according to our sins or repaid us according to our iniquities.” "
    "Verse 12 says, “As far as the east is from the west, so far has He removed our transgressions from us.” "
    "Isaiah 53:5 says “the punishment that brought us peace was upon Him.” "
    "When we confess, “He is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.” "
    "When the disciples asked who had sinned so that a man was born blind, Jesus answered, "
    "“Neither this man nor his parents sinned, but this happened so that the works of God would be displayed in him.” "
    "God does discipline the children He loves. Hebrews 12:6 says, "
    "“For the Lord disciplines the one He loves, and He chastises every son He receives.” "
    "That discipline is a Father’s training for our good, not payback. "
    "Some trouble is the natural result of a choice. Some trouble comes with living in a broken world. "
    "Neither one means the cross was not enough."
)
# Confirm every quoted sentence is the BSB line, not a paraphrase.
for ref, snippet in [
    ("Romans 8:1", "Therefore, there is now no condemnation for those who are in Christ Jesus."),
    ("Psalm 103:10", "He has not dealt with us according to our sins or repaid us according to our iniquities."),
    ("Psalm 103:12", "As far as the east is from the west, so far has He removed our transgressions from us."),
    ("John 9:3", "Neither this man nor his parents sinned, but this happened so that the works of God would be displayed in him."),
    ("Isaiah 53:5", "the punishment that brought us peace was upon Him"),
    ("1 John 1:9", "He is faithful and just to forgive us our sins and to cleanse us from all unrighteousness."),
    ("Hebrews 12:6", "For the Lord disciplines the one He loves, and He chastises every son He receives."),
]:
    got = scripture(ref, bible)
    if snippet.rstrip(".") not in got and snippet not in got:
        raise SystemExit("BSB mismatch %s\n%s" % (ref, got))

replacement = (
    "God is not punishing me for sins Jesus already bore. In Christ there is no condemnation. "
    "A hard season can be real without being a sentence, and when God corrects me it is a Father’s love, not revenge."
)
prayer = (
    "Lord, I have been reading my pain as Your punishment. Thank You that there is now no condemnation "
    "for those who are in Christ Jesus. When You correct me, let me receive a Father’s love, not a sentence. Amen."
)
STEP = (
    "Choose steps you can do safely. If this belief comes with hopelessness or thoughts of ending your life, "
    "call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone."
)

page_src = SRC.read_text()
head = page_src.split("<!-- share-button:start -->", 1)[0]
script = page_src[page_src.rfind("\n</div><script>") + 1 :]
head = head.replace("Psych-031-My-Situation-Is-Hopeless.pdf", "Belief-001-God-Is-Punishing-Me-For-My-Sins.pdf")
head = head.replace("Psych-031-My-Situation-Is-Hopeless-Homework.pdf", "Belief-001-God-Is-Punishing-Me-For-My-Sins-Homework.pdf")
head = re.sub(r"<title>.*?</title>", "<title>Belief Card: God is punishing me</title>", head, count=1)
head = re.sub(
    r'<meta name="description" content="[^"]*"/>',
    '<meta name="description" content="Christian belief counseling for “God is punishing me.” with BSB scriptures, questions, songs, and practical homework."/>',
    head,
    count=1,
)

refs = [KEY] + ALSO[:2]
scr = opts(
    ['<span class="ref">%s</span><span class="scrip">“%s”</span>' % (r, html.escape(scripture(r, bible).rstrip("."))) for r in refs]
)
err_html = "\n".join("<li><strong>%s: </strong>%s</li>" % pair for pair in errs)
pearl_html = "\n".join(
    '<li><a href="%s%s" target="_blank" rel="noopener">%s</a></li>' % (PB, s, html.escape(PEARLS[s]))
    for s in PEARL_SLUGS
)
song_html = "\n".join(song(k, w) for k, w in songs)

body = f'''<!-- ============ CARD ============ -->
<div class="card belief">
<div class="tag">Spiritual/Religious False Belief #1 · God</div>
<h1>{SHOWN}</h1>
<div class="orn">✦ ✦ ✦</div>

<h2>Where it often comes from</h2>
<p>People often say it in a longer way: “God is punishing me for my many sins.” A sickness, a loss, a closed door, or a season that will not lift starts to feel like a sentence. Some of us grew up with a parent, a teacher, or a church that kept score, so every trouble was treated as proof we had done something wrong. Real sin can leave a heavy conscience, and a sermon about judgment can turn into a private verdict. The thought is understandable. It is still a conclusion. Suffering is not a reliable report of God’s attitude toward you.</p>

<h2>What Scripture teaches</h2>
<p>{teaches}</p>
<div class="key">{qref(KEY)}</div>

<h2>Also see</h2>
<div class="also">
{chr(10).join("<p>"+qref(r)+"</p>" for r in ALSO)}
</div>

<h2>Common self-statements</h2>
{ul(self_statements)}

<h2>Common logical errors</h2>
<ul>
{err_html}
</ul>

<h2>Challenging questions</h2>
{ul(questions)}

<h2>Truth summary</h2>
<p class="truth">{replacement}</p>

<h2>Related Pearls topics</h2>
<p>Click a topic to open it in the Pearls Scripture Search:</p>
<ul class="pearls">
{pearl_html}
</ul>
<p class="gc-head"><strong>Godly Counsel Lessons:</strong></p>
<p>From the book <em>Godly Counsel</em> by Dr. Brian Campbell. Click a lesson to open it. You can read it on screen or print it.</p>
<ul class="pearls">
{gc_link(26)}
{gc_link(14)}
{gc_link(27)}
</ul>

<!--christlike-->
<h2>What does a mentally healthy Christian look like?</h2>
<div style="display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap;background:#f6efe2;border-left:4px solid #b08a4b;border-radius:6px;padding:16px 18px;margin:8px 0 18px">
<a href="https://www.amazon.com/dp/1456309684" target="_blank" rel="noopener" title="Order Christlike: Walking the Walk on Amazon" style="flex:none"><img src="https://doctorishome.github.io/belief-therapy-tool/belief-cards/books/christlike-cover.jpg" alt="Cover of Christlike: Walking the Walk, The Mentally Healthy Christian, by Dr. Brian Campbell with Rev. Jim Angelakos" style="width:120px;height:auto;display:block;border-radius:3px;box-shadow:0 3px 10px rgba(0,0,0,.25)"></a>
<div style="flex:1;min-width:200px">
<p style="margin:0 0 8px">From <em>Christlike: Walking the Walk</em> by Dr. Brian Campbell. A portrait, verse by verse, of how a mentally healthy Christian thinks, feels, and lives.</p>
<p style="margin:0"><a href="https://doctorishome.github.io/belief-therapy-tool/belief-cards/books/the-mentally-healthy-christian.html" target="_blank" rel="noopener" style="color:#1f3a5f;text-decoration-color:#b08a4b;text-underline-offset:3px"><b>Read excerpts from “The Mentally Healthy Christian”</b></a> <span style="font-size:.9em;color:#6b6250">(with every Scripture written out)</span></p>
</div></div>
<!--/christlike-->
{audio("Overcoming Depression", DEP, "about 20 minutes")}

{audio("Overcoming Anxiety", ANX, "about 18 minutes")}

<h2>Songs that speak truth to this belief</h2>
<p class="songnote2">Tap a song to play it right here. Three contemporary songs and one classic hymn or older favorite.</p>
<div class="songs">
{song_html}
</div>
<p class="songnote">Songs play here through YouTube and may start with a short ad. If one will not play, use its “Watch on YouTube” link.</p>

<p class="morning">Each morning ask: “If I truly believed God’s truth instead of this lie, what is one step I could take today?”</p>
<div class="foot">✦ ✦ ✦</div>
</div>

<!-- ============ HOMEWORK, PAGE 1 ============ -->
<div class="card">
<div class="tag">Homework · Replace and Rehearse</div>
<h1>My Plan for Replacing<br/>{SHOWN}</h1>
<div class="orn">✦ ✦ ✦</div>
<p class="intro">Read through each section and <strong>check the one that fits you best</strong>. If none of them fit, write your own. One choice per section is enough. A truth you choose for yourself will stick better than one handed to you.</p>
<div class="fill"><span>Name:</span><i></i><span>Date started:</span><i></i></div>

<div class="step"><div class="num">1</div><div><h2>How strongly do I believe the lie?</h2><p class="why">Rate it now so you can see your progress later.</p></div></div>
<div class="rate"><span><b>{SHOWN}</b> I believe this <span class="box"></span> % <span style="font-size:14px;color:#5a5348">(0 = not at all, 100 = completely)</span></span></div>

<div class="step"><div class="num">2</div><div><h2>My best question</h2><p class="why">The one question I will ask myself every time the lie shows up.</p></div></div>
{opts(questions)}
<div class="fill"><span>My own question:</span><i></i></div>

<div class="step"><div class="num">3</div><div><h2>My replacement truth</h2><p class="why">The statement I will say to myself instead of the lie.</p></div></div>
{opts(truths)}
<div class="fill"><span>In my own words:</span><i></i></div>

<div class="step"><div class="num">4</div><div><h2>My Scripture</h2><p class="why">The verse that speaks most directly to me. This is the one I will memorize.</p></div></div>
{scr}
<div class="fill"><span>A verse I found myself:</span><i></i></div>
<div class="lines"><i></i></div>

<div class="foot">✦ ✦ ✦</div>
</div>

<!-- ============ HOMEWORK, PAGE 2 ============ -->
<div class="card">
<div class="tag">Homework · Replace and Rehearse</div>
<h1>Practicing the Truth</h1>
<div class="orn">✦ ✦ ✦</div>

<div class="step"><div class="num">5</div><div><h2>My practice plan</h2><p class="why">Everyone does the first four. Then pick one or two extra tools.</p></div></div>
<div class="group">Everyone does these</div>
<ul class="opts">
<li><strong>Make my Truth Card</strong> (below). Carry it and read it at least three times a day.</li>
<li><strong>Memorize my Scripture</strong> from Step 4.</li>
<li><strong>Listen to one song each day</strong> from “Songs that speak truth to this belief” on my card, and fill in my song journal (below).</li>
<li><strong>Set reminders</strong> to silently repeat my truth. Check one or more:
  <span class="scrip" style="font-style:normal">☐ <strong>A buzz:</strong> my watch or phone vibrates every ______ minutes<br/>☐ <strong>An everyday event:</strong> every time I ______________________________<br/>☐ <strong>A visual reminder:</strong> something I will see often, such as a sticky note on my mirror, my truth as the background picture on my phone, or a note on my car dashboard.</span></li>
</ul>
<div class="group">Pick one or two that fit me</div>
<ul class="opts">
<li><strong>When the “God is punishing me” thought came:</strong> Each day, write down one moment when a hardship felt like a sentence from God. Write what happened, what you told yourself, and one more accurate statement.</li>
<li><strong>My name in Scripture:</strong> Write a personal reminder based on my verse and read it aloud. Keep this application separate from the Bible quotation.
  <span class="scrip">For example, Romans 8:1 becomes: “<strong>Sarah</strong> can write: “In Christ Jesus there is now no condemnation for me.””</span></li>
<li><strong>Gratitude journal:</strong> Each night, write three things I thank God for.</li>
<li><strong>Truth recording:</strong> Record my own voice reading my Truth Card and verse, and listen in the car or on a walk.</li>
<li><strong>Reading:</strong> The <a href="{PB}{READING}" target="_blank" rel="noopener">“{html.escape(PEARLS[READING])}” topic in Pearls</a>.</li>
<li><strong>Listening:</strong> The <a href="{DEP}" target="_blank" rel="noopener">Overcoming Depression audio</a> or the <a href="{ANX}" target="_blank" rel="noopener">Overcoming Anxiety audio</a> by Dr. Brian Campbell. Tap to play.</li>
</ul>

<div class="step"><div class="num">6</div><div><h2>My action step this week</h2><p class="why">Do one thing that tests the lie in real life.</p><p class="why">{STEP}</p></div></div>
{opts(actions)}
<div class="fill"><span>What I will do:</span><i></i></div>
<div class="fill"><span>When:</span><i></i></div>
<div class="fill"><span>What the lie predicts will happen:</span><i></i></div>

<div class="step"><div class="num">7</div><div><h2>End-of-week check-in</h2><p class="why">Bring this page to your next session.</p></div></div>
<div class="fill"><span>What actually happened:</span><i></i></div>
<div class="lines"><i></i></div>
<div class="fill"><span>What I learned:</span><i></i></div>
<div class="rate"><span><b>The lie</b> {SHOWN}: <span class="box"></span> %</span><span><b>My truth:</b> <span class="box"></span> %</span></div>

<h2>Daily practice tracker</h2>
<table class="track">
<tr><th>Day</th><th>Read my card</th><th>Said my verse</th><th>Used my reminder</th><th>A hardship I stopped calling punishment</th></tr>
<tr><td>Mon</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Tue</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Wed</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Thu</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Fri</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Sat</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Sun</td><td></td><td></td><td></td><td class="wide"></td></tr>
</table>

<h2>My song journal</h2>
<p class="why">After each day's song, write what it told you that challenges the lie.</p>
<table class="track songj">
<tr><th>Day</th><th>Song I listened to</th><th>What it told me that challenges the lie</th></tr>
<tr><td>Mon</td><td></td><td></td></tr>
<tr><td>Tue</td><td></td><td></td></tr>
<tr><td>Wed</td><td></td><td></td></tr>
<tr><td>Thu</td><td></td><td></td></tr>
<tr><td>Fri</td><td></td><td></td></tr>
<tr><td>Sat</td><td></td><td></td></tr>
<tr><td>Sun</td><td></td><td></td></tr>
</table>

<h2>My Truth Card</h2>
<div class="cutcard">
<div class="lbl">The lie</div>
<div class="lie">{BELIEF[:-1]}</div>
<div class="lbl">The truth</div>
<div class="lines"><i></i><i></i></div>
<div class="lbl">God’s Word</div>
<div class="lines"><i></i><i></i></div>
</div>
<p class="cutnote">Copy onto a 3×5 card, or cut along the dashed line and carry it with you.</p>

<h2>Prayer</h2>
<p class="prayer">{prayer}</p>
<div class="foot">✦ ✦ ✦</div>
<p class="bnote">Scripture quotations are from the Berean Standard Bible (BSB), which is in the public domain.</p>
</div>

<p class="back"><a href="#top">Back to top</a> · <a href="https://www.beliefcounselor.com/spiritual-religious-false-beliefs" target="_top">Spiritual/Religious False Beliefs</a></p>

'''

OUT.write_text(head + body + script)
print("wrote", OUT.name)
