"""God-topic cards 2–5, same structure as Belief-001.

Every chapter-and-verse citation is written out from the Berean Standard Bible
beside the reference. Run: python3 tools/make_god_cards_2_5.py
"""
import html
import logging
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_cards import load_bible, scripture  # noqa: E402
from add_share_buttons import MARK, share_block, strip_old, write_stub  # noqa: E402

SRC = ROOT / "belief-cards/psychological/Psych-031-My-Situation-Is-Hopeless.html"
CAT = __import__("json").loads((ROOT / "tools/music-catalog.json").read_text())
PEARLS = __import__("json").loads((ROOT / "tools/pearls-topics.json").read_text())
GC = __import__("json").loads((ROOT / "tools/godly-counsel-chapters.json").read_text())
PB = "https://www.beliefcounselor.com/scriptures?topic="
GCB = "https://doctorishome.github.io/belief-therapy-tool/belief-cards/godly-counsel/"
DEP = "https://music.wixstatic.com/mp3/dbdded_149606a27908493da01ac9492fb18ab1.mp3"
ANX = "https://music.wixstatic.com/mp3/dbdded_f67d414544534727acf6973d58189443.mp3"
STEP = (
    "Choose steps you can do safely. If this belief comes with hopelessness or thoughts of ending your life, "
    "call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone."
)
BOOKS = [
    "1 Corinthians", "2 Corinthians", "1 John", "2 John", "3 John", "1 Peter", "2 Peter",
    "Lamentations", "Zephaniah", "Philippians", "Revelation", "Matthew", "Hebrews",
    "Isaiah", "Romans", "Psalms", "Psalm", "Acts", "John",
]
bible = load_bible()


def qref(ref):
    text = scripture(ref, bible)
    if text.endswith("."):
        text = text[:-1]
    return '<q>%s</q> <span class="ref">(%s)</span>.' % (html.escape(text), ref)


def ul(items):
    return "<ul>\n" + "\n".join("<li>%s</li>" % x for x in items) + "\n</ul>"


def opts(items):
    return '<ul class="opts">\n' + "\n".join("<li>%s</li>" % x for x in items) + "\n</ul>"


def verse_text(ref):
    text = scripture(ref, bible).rstrip()
    if text and text[-1] not in ".!?…’”:":
        text += "."
    return text


def cite(ref):
    return '%s (“%s”)' % (ref, html.escape(verse_text(ref)))


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
        '<p class="atitle"><a href="%s" target="_blank" rel="noopener">%s</a> '
        "<span>· Dr. Brian Campbell · %s</span></p>\n"
        '<audio controls preload="none" src="%s">Your browser can’t play this here. '
        '<a href="%s">Open the recording</a>.</audio>\n'
        '<p class="aload" hidden>Starting the recording… it is a long one, so it may take a few seconds to begin.</p>\n'
        '<p class="anote">Press play to listen here, or tap the title to open it on its own.</p>\n</div>'
        % (title, url, title, minutes, url, url)
    )


def gc_link(n):
    title = GC[str(n)][0]
    slug = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")
    return '<li><a href="%sGC-%02d-%s.pdf" target="_blank" rel="noopener">%s</a></li>' % (
        GCB, n, slug, html.escape(title))


def check_scripture(page):
    ref_re = re.compile(r"\b(?:%s) \d+:\d+(?:[–-]\d+)?" % "|".join(re.escape(b) for b in sorted(BOOKS, key=len, reverse=True)))
    plain = html.unescape(re.sub(r"<[^>]+>", " ", page))
    missing = []
    for m in ref_re.finditer(plain):
        ref = m.group(0).replace("-", "–")
        try:
            words = verse_text(ref)
        except Exception as exc:
            missing.append("%s (%s)" % (ref, exc))
            continue
        window = plain[max(0, m.start() - 1600): m.end() + 1600]
        probe = words[:40].rstrip(".,; ")
        if probe not in window and words[:20] not in window:
            missing.append(ref + " missing text near citation")
    if missing:
        raise SystemExit("scripture not written out:\n" + "\n".join(missing))
    return len(ref_re.findall(plain))


def write_card(d):
    for slug in d["pearls"] + [d["reading"]]:
        if slug not in PEARLS:
            raise SystemExit("pearl " + slug)
    kinds = [CAT[k][3] for k, _ in d["songs"]]
    if kinds.count("classic") != 1 or len(d["songs"]) != 4:
        raise SystemExit("songs %s %s" % (d["num"], kinds))
    belief = d["belief"]
    shown = "“%s”" % belief
    page_src = SRC.read_text()
    head = page_src.split("<!-- share-button:start -->", 1)[0]
    script = page_src[page_src.rfind("\n</div><script>") + 1 :]
    fname = "Belief-%03d-%s" % (d["num"], d["file"])
    head = head.replace("Psych-031-My-Situation-Is-Hopeless.pdf", fname + ".pdf")
    head = head.replace("Psych-031-My-Situation-Is-Hopeless-Homework.pdf", fname + "-Homework.pdf")
    head = re.sub(r"<title>.*?</title>", "<title>Belief Card: %s</title>" % html.escape(belief.rstrip(".")), head, count=1)
    head = re.sub(
        r'<meta name="description" content="[^"]*"/>',
        '<meta name="description" content="Christian belief counseling for “%s” with BSB scriptures, questions, songs, and practical homework."/>' % html.escape(belief),
        head,
        count=1,
    )
    refs = [d["key"]] + d["also"]
    scr = opts(['<span class="ref">%s</span><span class="scrip">“%s”</span>' % (r, html.escape(scripture(r, bible).rstrip("."))) for r in refs])
    err_html = "\n".join("<li><strong>%s: </strong>%s</li>" % pair for pair in d["errors"])
    pearl_html = "\n".join(
        '<li><a href="%s%s" target="_blank" rel="noopener">%s</a></li>' % (PB, s, html.escape(PEARLS[s])) for s in d["pearls"]
    )
    song_html = "\n".join(song(k, w) for k, w in d["songs"])
    gc_html = "\n".join(gc_link(n) for n in d["gc"])
    body = f'''<!-- ============ CARD ============ -->
<div class="card belief">
<div class="tag">Spiritual/Religious False Belief #{d["num"]} · {html.escape(d.get("group", "God"))}</div>
<h1>{shown}</h1>
<div class="orn">✦ ✦ ✦</div>

<h2>Where it often comes from</h2>
<p>{d["origins"]}</p>

<h2>What Scripture teaches</h2>
<p>{d["teaches"]}</p>
<div class="key">{qref(d["key"])}</div>

<h2>Also see</h2>
<div class="also">
{chr(10).join("<p>"+qref(r)+"</p>" for r in d["also"])}
</div>

<h2>Common self-statements</h2>
{ul(d["self"])}

<h2>Common logical errors</h2>
<ul>
{err_html}
</ul>

<h2>Challenging questions</h2>
{ul(d["questions"])}

<h2>Truth summary</h2>
<p class="truth">{d["replacement"]}</p>

<h2>Related Pearls topics</h2>
<p>Click a topic to open it in the Pearls Scripture Search:</p>
<ul class="pearls">
{pearl_html}
</ul>
<p class="gc-head"><strong>Godly Counsel Lessons:</strong></p>
<p>From the book <em>Godly Counsel</em> by Dr. Brian Campbell. Click a lesson to open it. You can read it on screen or print it.</p>
<ul class="pearls">
{gc_html}
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
<h1>My Plan for Replacing<br/>{shown}</h1>
<div class="orn">✦ ✦ ✦</div>
<p class="intro">Read through each section and <strong>check the one that fits you best</strong>. If none of them fit, write your own. One choice per section is enough. A truth you choose for yourself will stick better than one handed to you.</p>
<div class="fill"><span>Name:</span><i></i><span>Date started:</span><i></i></div>

<div class="step"><div class="num">1</div><div><h2>How strongly do I believe the lie?</h2><p class="why">Rate it now so you can see your progress later.</p></div></div>
<div class="rate"><span><b>{shown}</b> I believe this <span class="box"></span> % <span style="font-size:14px;color:#5a5348">(0 = not at all, 100 = completely)</span></span></div>

<div class="step"><div class="num">2</div><div><h2>My best question</h2><p class="why">The one question I will ask myself every time the lie shows up.</p></div></div>
{opts(d["questions"])}
<div class="fill"><span>My own question:</span><i></i></div>

<div class="step"><div class="num">3</div><div><h2>My replacement truth</h2><p class="why">The statement I will say to myself instead of the lie.</p></div></div>
{opts(d["truths"])}
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
<li><strong>{html.escape(d["prompt"])}:</strong> Each day, write down one moment when {html.escape(d["moment"])}. Write what happened, what you told yourself, and one more accurate statement.</li>
<li><strong>My name in Scripture:</strong> Write a personal reminder based on my verse and read it aloud. Keep this application separate from the Bible quotation.
  <span class="scrip">For example, {cite(d["key"])} becomes: “<strong>Sarah</strong> can write: “{html.escape(d["example"])}”” Keep that sentence as your own words, not as the Bible verse.</span></li>
<li><strong>Gratitude journal:</strong> Each night, write three things I thank God for.</li>
<li><strong>Truth recording:</strong> Record my own voice reading my Truth Card and verse, and listen in the car or on a walk.</li>
<li><strong>Reading:</strong> The <a href="{PB}{d["reading"]}" target="_blank" rel="noopener">“{html.escape(PEARLS[d["reading"]])}” topic in Pearls</a>.</li>
<li><strong>Listening:</strong> The <a href="{DEP}" target="_blank" rel="noopener">Overcoming Depression audio</a> or the <a href="{ANX}" target="_blank" rel="noopener">Overcoming Anxiety audio</a> by Dr. Brian Campbell. Tap to play.</li>
</ul>

<div class="step"><div class="num">6</div><div><h2>My action step this week</h2><p class="why">Do one thing that tests the lie in real life.</p><p class="why">{STEP}</p></div></div>
{opts(d["actions"])}
<div class="fill"><span>What I will do:</span><i></i></div>
<div class="fill"><span>When:</span><i></i></div>
<div class="fill"><span>What the lie predicts will happen:</span><i></i></div>

<div class="step"><div class="num">7</div><div><h2>End-of-week check-in</h2><p class="why">Bring this page to your next session.</p></div></div>
<div class="fill"><span>What actually happened:</span><i></i></div>
<div class="lines"><i></i></div>
<div class="fill"><span>What I learned:</span><i></i></div>
<div class="rate"><span><b>The lie</b> {shown}: <span class="box"></span> %</span><span><b>My truth:</b> <span class="box"></span> %</span></div>

<h2>Daily practice tracker</h2>
<table class="track">
<tr><th>Day</th><th>Read my card</th><th>Said my verse</th><th>Used my reminder</th><th>{html.escape(d["tracker"])}</th></tr>
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
<div class="lie">{html.escape(belief[:-1] if belief.endswith(".") else belief)}</div>
<div class="lbl">The truth</div>
<div class="lines"><i></i><i></i></div>
<div class="lbl">God’s Word</div>
<div class="lines"><i></i><i></i></div>
</div>
<p class="cutnote">Copy onto a 3×5 card, or cut along the dashed line and carry it with you.</p>

<h2>Prayer</h2>
<p class="prayer">{d["prayer"]}</p>
<div class="foot">✦ ✦ ✦</div>
<p class="bnote">Scripture quotations are from the Berean Standard Bible (BSB), which is in the public domain.</p>
</div>

<p class="back"><a href="#top">Back to top</a> · <a href="https://www.beliefcounselor.com/spiritual-religious-false-beliefs" target="_top">Spiritual/Religious False Beliefs</a></p>

'''
    page = head + body + script
    n = check_scripture(page)
    out = ROOT / "belief-cards" / (fname + ".html")
    out.write_text(page)
    page = strip_old(out.read_text(encoding="utf-8"))
    page = page.replace(MARK, share_block(page, "spiritual-%d" % d["num"]) + MARK, 1)
    out.write_text(page, encoding="utf-8")
    check_scripture(page)
    write_stub("spiritual-%d" % d["num"], out)
    print("wrote", out.name, "citations", n)


def print_pdfs(paths):
    from weasyprint import HTML
    from weasyprint.urls import URLFetcher
    logging.getLogger("weasyprint").setLevel(logging.ERROR)
    F = ROOT / "tools/gc_fonts"
    css = (
        "<style>@font-face{font-family:\"Source Serif 4\";src:url(\"%s\")}"
        "@font-face{font-family:\"Source Serif 4\";font-style:italic;src:url(\"%s\")}"
        "@font-face{font-family:\"Cormorant Garamond\";font-weight:600 700;src:url(\"%s\")}"
        "@page{size:Letter;margin:0.5in;@bottom-center{content:counter(page);font-size:9pt;color:#1F3A5F}}"
        "</style>"
    ) % ((F / "SourceSerif4-Regular.ttf").as_uri(), (F / "SourceSerif4-Italic.ttf").as_uri(), (F / "Cormorant-SemiBold.ttf").as_uri())
    fetch = URLFetcher(allowed_protocols=["file", "data"])
    for p in paths:
        s = re.sub(r"<link[^>]+fonts.googleapis[^>]*>", "", p.read_text())
        s = s.replace("</head>", css + "</head>")
        HTML(string=s, base_url=p.as_uri(), url_fetcher=fetch).write_pdf(str(p.with_suffix(".pdf")))
        HTML(string=s.replace("<body>", '<body class="hw-only">'), base_url=p.as_uri(), url_fetcher=fetch).write_pdf(
            str(p.with_name(p.stem + "-Homework.pdf"))
        )
        print("pdf", p.stem)


C2 = dict(
    num=2, file="If-There-Is-A-God-He-Would-Not-Let-This-Happen",
    belief="If there is a God, he would not let this happen.",
    key="John 16:33",
    also=["Psalm 34:18", "Isaiah 43:2", "Romans 8:28", "Lamentations 3:32–33", "Psalm 46:1"],
    pearls=["suffering", "god-all-loving", "sorrow", "trust", "help"],
    reading="suffering", gc=[27, 30, 15],
    songs=[
        ("storm", "You can praise God in the storm without pretending the storm is small."),
        ("held", "When the pain makes no sense, you are still held."),
        ("even", "Faith can say “even if” when the outcome is not the one you asked for."),
        ("lives", "Because Jesus lives, trouble is not the last word."),
    ],
    origins="A loss, a diagnosis, a betrayal, or a prayer that was not answered the way you asked can make a good God seem impossible. The mind says that a real and kind God would have stopped this. That cry is honest. It is not a proof. We live in a broken world, and love does not mean a life with no pain.",
    self=[
        "A loving God would have stopped this.",
        "This proves He is not there.",
        "If He cared, my prayer would have been answered my way.",
        "Good people do not suffer like this.",
        "I cannot trust a God who lets this happen.",
        "There is no point in talking to Him about it.",
    ],
    errors=[
        ("All-or-nothing thinking", "If God does not prevent this pain, He must not be real or good."),
        ("Emotional reasoning", "Feeling abandoned and treating the feeling as proof God is absent."),
        ("Fortune telling", "Deciding that a God who allowed this will never bring any good from it."),
        ("Discounting the positive", "Ignoring the presence, comfort, and hope Scripture says are still true."),
    ],
    prompt="When I treated pain as proof God is not real",
    moment="a hardship felt like evidence that God would not allow it",
    example="I will have trouble in this world, and Jesus has overcome it. He is still with me.",
    tracker="A hard thing I stopped using as proof God is absent",
)
C2["teaches"] = (
    "Jesus did not promise a life without trouble. "
    + cite("John 16:33") + " "
    + cite("Psalm 34:18") + " "
    + cite("Isaiah 43:2") + " "
    + cite("Romans 8:28") + " "
    + cite("Lamentations 3:32–33") + " "
    + cite("Psalm 46:1") + " "
    "Pain is real. It does not prove that God is absent or unreal."
)
C2["questions"] = [
    "What, exactly, did I expect a loving God to stop?",
    "Does %s say I will have no trouble, or that Jesus has overcome the world?" % cite("John 16:33"),
    "Where is God when I am brokenhearted, according to %s?" % cite("Psalm 34:18"),
    "Am I asking this pain to prove that God is not real?",
    "What would I tell a friend who said the same thing about a grief like mine?",
    "Can I bring God the honest question without deciding the case against Him?",
]
C2["truths"] = [
    "This happened, and God is still God.",
    "Trouble in this world is not proof that Jesus has left me.",
    "The Lord is near when I am brokenhearted.",
    "He is with me in the waters and the fire.",
    "I can grieve and still trust Him.",
    "I do not have to understand this before I talk to Him.",
]
C2["replacement"] = (
    "This happened, and God is still God. Jesus said I would have trouble in this world, and that He has overcome it. "
    "He is near the brokenhearted. I can bring Him my grief without deciding He is absent."
)
C2["actions"] = [
    "<strong>Write the event and the conclusion separately.</strong> One line for what happened. One line for “this means God is not real.” Cross out any word in the second line that is a feeling, not a fact.",
    "<strong>Read %s aloud</strong> and write one sentence about trouble and one sentence about courage." % cite("John 16:33"),
    "<strong>Tell God the honest sentence</strong> “I do not understand why You let this happen,” and then read %s." % cite("Psalm 34:18"),
    "<strong>Name one help that is still here</strong> today: a person, a verse, a meal, a next small step.",
]
C2["prayer"] = (
    "Lord, this pain makes me wonder if You are there. Thank You for what %s says. "
    "Stay near me while I grieve, and teach me not to call my pain a proof that You are gone. Amen."
) % cite("John 16:33")

C3 = dict(
    num=3, file="God-Is-Disappointed-In-Me",
    belief="God is disappointed in me.",
    key="Zephaniah 3:17",
    also=["Romans 8:1", "Psalm 103:13–14", "Romans 5:8", "1 John 3:1", "Psalm 147:11"],
    pearls=["love-by-god", "god-all-loving", "mercy", "forgiveness", "guilt-shame"],
    reading="love-by-god", gc=[17, 24, 14],
    songs=[
        ("yousay", "God’s voice is kinder and truer than the voice that calls you a disappointment."),
        ("who", "Your name is held by the God who knows you, not by your last failure."),
        ("father", "He is a good Father, not a parent who has given up on you."),
        ("lovesme", "The old hymn is simple on purpose: Jesus loves me."),
    ],
    origins="A parent who sighed, a teacher who was never pleased, or a church that noticed failures more than faith can teach the heart to expect disappointment. Real sin adds shame. The thought “I let God down, and He is tired of me” can feel like His voice. It is often an old scorekeeper, not the Father who calls you His child.",
    self=[
        "I am a disappointment to God.",
        "He expected more, and I failed Him.",
        "Other Christians make Him glad. I make Him tired.",
        "If He really knew this week, He would stop loving me.",
        "I should hide until I have improved.",
        "His love is for the people who get it right.",
    ],
    errors=[
        ("Emotional reasoning", "Feeling like a letdown and calling that feeling God’s opinion."),
        ("Mind reading", "Deciding what God thinks of me without asking what He has said."),
        ("All-or-nothing thinking", "If I am not impressive, I must be a disappointment."),
        ("Discounting the positive", "Ignoring the cross, the Father’s compassion, and the name He gives His children."),
    ],
    prompt="When I was sure God was disappointed",
    moment="a failure felt like proof God was tired of me",
    example="In Christ Jesus there is now no condemnation for me. My Father has not given up.",
    tracker="A failure I stopped calling God’s disappointment",
)
C3["teaches"] = (
    "Scripture does not describe the Father as a parent who has given up on His children. "
    + cite("Zephaniah 3:17") + " "
    + cite("Romans 8:1") + " "
    + cite("Psalm 103:13–14") + " "
    + cite("Romans 5:8") + " "
    + cite("1 John 3:1") + " "
    + cite("Psalm 147:11") + " "
    "He knows you are dust, and He still has compassion. Sin is real, and it is not the same thing as being a disappointment He has finished with."
)
C3["questions"] = [
    "Whose disappointed voice am I hearing: God’s, or someone from my past?",
    "What does %s say about condemnation for those in Christ?" % cite("Romans 8:1"),
    "How does %s describe the Lord’s compassion?" % cite("Psalm 103:13–14"),
    "Did God love me only after I improved, or while I was still a sinner, as %s says?" % cite("Romans 5:8"),
    "What would I say to a child who thought a good father was disappointed and done?",
    "What is one true thing God calls me, according to %s?" % cite("1 John 3:1"),
]
C3["truths"] = [
    "In Christ there is now no condemnation for me.",
    "The Lord has compassion on me and knows I am dust.",
    "He loved me while I was still a sinner.",
    "I am called a child of God.",
    "He rejoices over His people with love.",
    "A hard day does not mean He has given up on me.",
]
C3["replacement"] = (
    "God is not disappointed in me as if He has given up. In Christ there is no condemnation. "
    "He has compassion on me, He loved me while I was still a sinner, and He rejoices over His people with love."
)
C3["actions"] = [
    "<strong>Separate the voices.</strong> Write “I feel disappointed in myself” and, beside it, %s." % cite("Romans 8:1"),
    "<strong>Read %s each morning</strong> and say, “This is my Father’s heart toward His people.”" % cite("Zephaniah 3:17"),
    "<strong>Tell one safe believer the failure</strong> you have been hiding, and ask them to read %s with you." % cite("Psalm 103:13–14"),
    "<strong>Do one ordinary faithful thing</strong> today without waiting until you feel impressive.",
]
C3["prayer"] = (
    "Father, I have been sure You are disappointed in me. Thank You for what %s says about Your love. "
    "Quiet me, and teach me to come to You instead of hiding. Amen."
) % cite("Zephaniah 3:17")

C4 = dict(
    num=4, file="God-Is-Too-Distant-To-Care",
    belief="God is too distant or too busy to care about me.",
    key="1 Peter 5:7",
    also=["Psalm 145:18", "Psalm 139:1–3", "Matthew 10:29–31", "Hebrews 4:15–16", "Isaiah 41:10"],
    pearls=["god-present-everywhere", "god-all-knowing", "prayer-how-to", "love-by-god", "fear"],
    reading="god-present-everywhere", gc=[22, 5, 17],
    songs=[
        ("alone", "You are not alone, even when you cannot feel anyone near."),
        ("stays", "God stays. Busyness is not His excuse."),
        ("knows", "He knows the details you think are too small to mention."),
        ("friend", "You have a friend to carry every care to."),
    ],
    origins="Unanswered prayers, a silent season, a busy church, or a parent who was never really there can teach the heart that important people do not have time for one person. God gets pictured as far away, running the universe and skipping you. Silence is not the same as distance. A crowded life is not a picture of God’s attention.",
    self=[
        "God has more important people to watch.",
        "My problem is too small for Him.",
        "He is too far away to notice.",
        "If He cared, I would feel Him.",
        "I should stop bothering Him.",
        "Other people’s prayers get through. Mine do not.",
    ],
    errors=[
        ("Emotional reasoning", "Not feeling God and concluding He is far away."),
        ("Minimizing", "Calling your need too small for the God who numbers hairs."),
        ("Mind reading", "Deciding God is too busy without a word from Him that says so."),
        ("All-or-nothing thinking", "If I cannot feel Him, He must not be near."),
    ],
    prompt="When God felt too far away to care",
    moment="a need felt too small, or God felt too far, for Him to care",
    example="I can cast this care on God, because He cares for me.",
    tracker="A care I brought to God instead of deciding He was too busy",
)
C4["teaches"] = (
    "Scripture does not describe God as too busy for the person who calls on Him. "
    + cite("1 Peter 5:7") + " "
    + cite("Psalm 145:18") + " "
    + cite("Psalm 139:1–3") + " "
    + cite("Matthew 10:29–31") + " "
    + cite("Hebrews 4:15–16") + " "
    + cite("Isaiah 41:10") + " "
    "He knows when you sit and when you rise. He is near to all who call on Him in truth. Not feeling Him is not the same as His being far away."
)
C4["questions"] = [
    "What need have I decided is too small for God?",
    "What does %s say I may do with my anxiety, and why?" % cite("1 Peter 5:7"),
    "Who is the Lord near to, according to %s?" % cite("Psalm 145:18"),
    "Am I using a feeling of silence as if it were a fact about God’s location?",
    "What does %s say God already knows about me?" % cite("Psalm 139:1–3"),
    "What would change today if I believed He cares for me?",
]
C4["truths"] = [
    "God cares for me, so I can cast my anxiety on Him.",
    "The Lord is near to all who call on Him in truth.",
    "He knows my path and my thoughts.",
    "I am worth more than many sparrows to my Father.",
    "I may come to the throne of grace and find help.",
    "Not feeling Him does not mean He has left.",
]
C4["replacement"] = (
    "God is not too distant or too busy to care about me. He is near to all who call on Him. "
    "He knows my ways, and He invites me to cast my anxiety on Him because He cares for me."
)
C4["actions"] = [
    "<strong>Bring one specific care out loud.</strong> Say it to God in a sentence, then read %s." % cite("1 Peter 5:7"),
    "<strong>Write three details God already knows</strong> about today, using %s as your reminder." % cite("Psalm 139:1–3"),
    "<strong>Ask for help from one person</strong> instead of deciding you are too small to matter.",
    "<strong>Read %s when God feels far</strong> and write “near” next to the care you were going to carry alone." % cite("Psalm 145:18"),
]
C4["prayer"] = (
    "Lord, I have pictured You as too far away and too busy for me. Thank You for what %s says. "
    "I cast this care on You, because You care for me. Amen."
) % cite("1 Peter 5:7")

C5 = dict(
    num=5, file="God-Loves-Some-People-More",
    belief="God loves some people more than others.",
    key="John 3:16",
    also=["Romans 2:11", "Acts 10:34–35", "1 John 4:9–10", "Romans 10:12", "2 Peter 3:9"],
    pearls=["love-by-god", "god-all-loving", "mercy", "grace", "salvation"],
    reading="love-by-god", gc=[17, 7, 29],
    songs=[
        ("onegod", "There is one true God, and His love is not a private club."),
        ("wins", "Grace, not a ranking, is how God meets people."),
        ("chains", "The same grace that frees one person is offered to you."),
        ("great", "How great Thou art is a song about His love for the world, not for a short list."),
    ],
    origins="Comparing blessings, health, gifts, families, or how easily someone else seems to hear God can turn love into a ranking. A home or a church that favored some people trains the heart to expect God to do the same. Different gifts and different seasons are not a measurement of who is loved more.",
    self=[
        "God likes them better than He likes me.",
        "I am the extra one, not the loved one.",
        "If He loved me as much, my life would look like theirs.",
        "Blessing is how God shows His favorites.",
        "I have to earn a higher place in His love.",
        "Some people are the real Christians. I am on the edge.",
    ],
    errors=[
        ("Comparing", "Using someone else’s blessings as a scoreboard of God’s love."),
        ("All-or-nothing thinking", "If my life is harder, I must be loved less."),
        ("Fortune telling", "Deciding God has ranked me for good because today looks smaller."),
        ("Discounting the positive", "Ignoring the love He has already shown in giving His Son."),
    ],
    prompt="When I ranked God’s love",
    moment="someone else’s life made me feel less loved by God",
    example="God loved the world, including me, and gave His Son. He does not show favoritism.",
    tracker="A comparison I stopped using as a measure of God’s love",
)
C5["teaches"] = (
    "God’s love is not a contest with winners and leftovers. "
    + cite("John 3:16") + " "
    + cite("Romans 2:11") + " "
    + cite("Acts 10:34–35") + " "
    + cite("1 John 4:9–10") + " "
    + cite("Romans 10:12") + " "
    + cite("2 Peter 3:9") + " "
    "He gives different gifts and allows different stories. A different story is not a smaller love. The same Lord gives richly to all who call on Him."
)
C5["questions"] = [
    "Whose life am I using as the proof that God loves them more?",
    "Who did God love, according to %s?" % cite("John 3:16"),
    "What does %s say about favoritism?" % cite("Romans 2:11"),
    "Am I treating a blessing as a score instead of a gift?",
    "What does %s say the same Lord does for all who call on Him?" % cite("Romans 10:12"),
    "What would I tell a friend who felt second-class in God’s family?",
]
C5["truths"] = [
    "God so loved the world that He gave His Son.",
    "God does not show favoritism.",
    "He loved us and sent His Son before we loved Him.",
    "The same Lord gives richly to all who call on Him.",
    "He is patient, not wanting anyone to perish.",
    "A different life is not a smaller love.",
]
C5["replacement"] = (
    "God does not love some people more than others. He loved the world and gave His Son. "
    "He does not show favoritism. The same Lord gives richly to all who call on Him, including me."
)
C5["actions"] = [
    "<strong>Name the comparison.</strong> Write the person and the blessing, then write %s beside it." % cite("Romans 2:11"),
    "<strong>Read %s aloud</strong> and put your own name in a separate sentence that is your application, not a change to the verse." % cite("John 3:16"),
    "<strong>Thank God for one gift in your life</strong> without measuring it against someone else’s.",
    "<strong>Encourage one person you have ranked above or below yourself,</strong> and tell them God does not show favoritism, as %s says." % cite("Romans 2:11"),
]
C5["prayer"] = (
    "Father, I have been keeping score of Your love. Thank You for what %s says. "
    "Teach me that a different story is not a smaller love, and help me call on You. Amen."
) % cite("John 3:16")

CARDS = [C2, C3, C4, C5]


def main():
    paths = []
    for d in CARDS:
        write_card(d)
        paths.append(ROOT / "belief-cards" / ("Belief-%03d-%s.html" % (d["num"], d["file"])))
    # The God list already opens every belief, including these four, by filename.
    text = (ROOT / "belief-lists/spiritual-religious.html").read_text()
    for d in CARDS:
        slug = "Belief-%03d-%s.html" % (d["num"], d["file"])
        if slug not in text and d["file"] not in text:
            raise SystemExit("list is not wired to " + slug)
        if d["belief"] not in text:
            raise SystemExit("list wording differs: " + d["belief"])
    print_pdfs(paths)
    print("list links confirmed")


if __name__ == "__main__":
    main()
