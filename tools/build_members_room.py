"""Build the Counselors' Room from Brian's "Basic Organization" outline (Nov 12, 2026).

    python3 tools/build_members_room.py

Writes members/*.html, and turns the old room's pages in counselors/ (FORWARD below) into
short forwarders, so the Wix pages that still load them show the new room.
The menu on the kept counselors/ pages comes from tools/update_counselor_nav.py.
To change the room: edit PAGES below and run again. To rename the room: change ROOM.

An item is (title, description, links). links is a list of (label, address); an empty
list shows a "Coming" label instead. Addresses starting with C/ point into counselors/.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "members"
ROOM = "Counselors’ Room"
SITE = "https://www.beliefcounselor.com"
GH = "https://doctorishome.github.io/belief-therapy-tool/"
F = "C/forms/Belief-Counseling-"

# file, menu label, heading, one-line summary
MENU = [
    ("index.html", "Welcome", "Welcome to the " + ROOM,
     "Everything for counselors, in the order you learn it."),
    ("belief-counseling.html", "Belief Counseling", "Belief Counseling",
     "The basics: what a belief is, what Belief Counseling is, and who should practice it."),
    ("process.html", "The Process", "The Process",
     "Three steps: Identify, Challenge, and Replace."),
    ("assessment.html", "Traditional Assessment", "Traditional Assessment",
     "Diagnosis, intake, sample forms, and the first interview."),
    ("tips.html", "Professional Tips", "Professional Tips",
     "Tips, case studies, theory, and insights from 35 years of practice."),
    ("library.html", "Library", "Library",
     "Books, videos, and articles."),
]


def video(n, slug, title):
    return ("video", title, "C/videos/lesson-%d-%s" % (n, slug))


PAGES = {
    "belief-counseling.html": [
        ("", "", [
            ("What Is a Belief?", "What beliefs are and how they shape thinking, feeling, and behavior.",
             [("Open page", SITE + "/beliefs")],
             "https://static.wixstatic.com/media/dbdded_4b31d62e4bab4f13b7c432e198166a64~mv2.png"),
            ("What Is Belief Counseling?", "The approach in plain language: identify, challenge, and replace false beliefs with truth.",
             [("Open page", SITE + "/belief-counseling")],
             "https://static.wixstatic.com/media/dbdded_419fa7003c984920aa0e8c88d113eae1~mv2.png"),
            ("Why Beliefs Matter", "Why Belief Counseling starts with beliefs, one step beneath emotions and behavior.",
             [("Open page", SITE + "/belief-counseling")],
             "https://static.wixstatic.com/media/dbdded_a07d286719a14ae8aa245ae61bc30665~mv2.avif"),
            ("Competence and Training", "Professional competencies for providing Christian cognitive-behavioral therapy.",
             [("Read (PDF)", "C/theory/Belief-Counseling-Competencies.pdf")]),
        ]),
    ],
    "process.html": [
        ("Introduction", "", [video(1, "introduction", "Introduction to the Process")]),
        ("Step 1: Identify", "Belief Mining uncovers the false beliefs. Each level has its own Mining Tool.", [
            video(2, "identify", "Step 1: Identify"),
            ("group", "Belief Mining: Levels"),
            ("1. Biological/Physical", "Mining Tool: Life Events & Beliefs Screening.",
             [("About this level", SITE + "/biological-physical"),
              ("Mining Tool", GH + "Life_Events_Beliefs_Screening.html")]),
            ("2. Psychological/Cognitive", "Mining Tools: five checklists of thoughts and beliefs.",
             [("About this level", SITE + "/psychological-cognitive"),
              ("Anxious Thoughts & Beliefs", F + "Anxious-Thoughts-and-Beliefs-Checklist.pdf"),
              ("Depressive Thoughts & Beliefs", F + "Depressive-Thoughts-and-Beliefs-Checklist.pdf"),
              ("Deeper Issues: Core Beliefs", F + "Deeper-Issues-Checklist-of-Core-Beliefs.pdf"),
              ("Discover the Lies", F + "Discover-the-Lies.pdf"),
              ("Cognitive Errors", F + "Cognitive-Errors-Checklist.pdf")]),
            ("3. Interpersonal", "Mining Tools: messages from parents and from spouses or partners.",
             [("About this level", SITE + "/interpersonal"),
              ("Toxic Beliefs Parents Teach Children", GH + "worksheets/parents.html"),
              ("Parental Messages Checklist", F + "Parental-Messages-Checklist.pdf"),
              ("Toxic Messages from Spouses or Partners", GH + "worksheets/partners.html")]),
            ("4. Socioeconomic", "Mining Tool: messages from money, work, and status.",
             [("About this level", SITE + "/socioeconomic"),
              ("Mining Tool", GH + "worksheets/money.html")]),
            ("5. Sociocultural", "Mining Tools: messages from culture, community, and media.",
             [("About this level", SITE + "/blank"),
              ("Culture & Community", GH + "worksheets/culture.html"),
              ("Media & Culture", GH + "worksheets/media.html")]),
            ("6. Spiritual/Religious", "Mining Tools: messages from church and religious upbringing.",
             [("About this level", SITE + "/blank-4"),
              ("Church setting", GH + "worksheets/church-setting.html"),
              ("Upbringing", GH + "worksheets/church-upbringing.html")]),
            ("group", "Spiritual Assessment Tools (optional)"),
            ("Christian Experiences and Beliefs", "Church background, family faith, and present beliefs. Counselor-guided.",
             [("Open (PDF)", F + "Christian-Experiences-and-Beliefs-Checklist.pdf"),
              ("Word", F + "Christian-Experiences-and-Beliefs-Checklist.docx")]),
            ("RSS-5", "Religious and Spiritual Struggles Scale, five-question short form. Optional.", []),
            ("Brief RCOPE", "A short measure of religious coping, for when a specific stressor is central. Optional.", []),
            ("SAI", "Spiritual Assessment Inventory (Hall & Edwards, 2002), for in-depth work. Optional. "
                    "Waiting for author permission.", []),
            ("group", "Core False Beliefs"),
            ("Core False Beliefs", "The 22 deep-seated beliefs that are especially important to mine.",
             [("Open page", "C/core-beliefs.html")]),
        ]),
        ("Step 2: Challenge", "Question the false belief, refute it, and test it.", [
            video(3, "challenge", "Step 2: Challenge"),
            ("Questions", "The Questioning False Beliefs worksheet, with general and Christian questions.",
             [("Open (PDF)", F + "Questioning-False-Beliefs.pdf"),
              ("Word", F + "Questioning-False-Beliefs.docx")]),
            ("Behavioral Experiments", "Simple experiments a client can do to test a belief in real life.",
             [("Open page", SITE + "/blank-5")]),
            ("Behavioral Interventions", "Article: Behavioral Interventions in Christian Cognitive-Behavioral Therapy.",
             [("Read article", GH + "pages/counselor/behavioral-interventions-ccbt.html"),
              ("PDF", GH + "pages/counselor/behavioral-interventions-ccbt.pdf")]),
            ("Cognitive Restructuring", "", []),
        ]),
        ("Step 3: Replace", "Put biblical truth in the place of the false belief, and practice it.", [
            video(4, "replace", "Step 3: Replace"),
            ("Scriptures", "Pearls Scripture Search: more than 170 topics.",
             [("Open Scripture Search", SITE + "/scriptures")]),
            ("Prayer", "", []),
            ("Reinforce", "", []),
            ("Practice", "", []),
        ]),
    ],
    "assessment.html": [
        ("", "This section shows what the assessment process looks like in private practice, "
             "with sample forms for each step.", [
            ("The Flow: Start Here", "A narrated presentation that walks through the whole process, "
                                     "from the first phone call on. Watch this first.",
             [("Open the slide show", "C/presentations/flow-of-care/index.html")]),
        ]),
        ("DSM-5-TR", "", [
            ("Training", "The DSM-5-TR diagnostic process, step by step (narrated slides).",
             [("Open slides", "C/presentations/diagnostic-process/index.html"),
              ("Flow chart", "C/reviews/dsm5tr-flow-chart.html")]),
            ("Tutorial", "Practice tutorial: DSM-5-TR diagnosis and coding.",
             [("Open tutorial", "C/presentations/diagnostic-process/tutorial.html")]),
        ]),
        # Replaces the Intake Process boxes. The form files stay in counselors/forms/.
        ("LIVE_PRACTICE", "", []),
        ("Online Assessment", "The forms the client completes before the first visit.", [
            ("Client forms", "About You · Brief History · Life Events & Beliefs Screening · "
                             "Agreements and consent forms, signed on screen",
             [("Open the client forms", "C/new-client-forms.html")]),
            ("Life Events & Beliefs Screening", "A one-page checklist of life events that may lie beneath painful beliefs.",
             [("Open", GH + "Life_Events_Beliefs_Screening.html")]),
            ("Schedule First Appointment", "", []),
        ]),
        ("Initial Interview", "", [
            ("Presenting Problem", "", []),
            ("Functional Analysis", "", []),
            ("Dictate Case Note", "", []),
            ("Initial Hypotheses", "", []),
        ]),
        ("DSM-5-TR Disorders", "", [
            ("Disorder reviews", "Teaching reviews of the major disorders: key features, what works, and Christian-integrated care.",
             [("Open the list of disorders", "C/reviews.html")]),
            ("False Beliefs", "Use the Lie Finder to find the false beliefs affecting a client.",
             [("Open Lie Finder", SITE + "/false-belief-finder")]),
            ("Treatment Plan", "", []),
        ]),
    ],
    "tips.html": [
        ("", "", [
            ("Introduction", "How the Professional Tips work and the topics you can expect.",
             [("Open", "C/tips.html")]),
            ("Weekly Professional Tips", "A new tip each week. Start with two free samples: Sex in the Counseling Room, and My Thoughts on Demonic Possession.",
             [("Open the tips", "C/weekly-tips.html")]),
            ("Sample Tips", "Ethics: Ethical Considerations When Choosing Treatment Modalities.",
             [("Read the tip", "C/tip-ethics-treatment-modalities.html"), ("All Ethics tips", "C/tips-ethics.html")]),
            ("Case Studies", "Practice on composite cases with a guided supervisor.",
             [("Open", "C/cases.html")]),
            ("Theory", "From CBT to Christian CBT, and How Beliefs Influence Personality.",
             [("Open", "C/theory.html")]),
            ("Insights", "", []),
        ]),
    ],
    "library.html": [
        ("", "", [
            ("Books", "Books Dr. Campbell recommends for counselors and clients.", [("Open", "C/books.html")]),
            ("Videos", "Teaching videos, with the forms that go with them.", [("Open", "C/videos.html")]),
            ("Articles", "All of Dr. Campbell’s articles for counselors in one place.", [("Open", "C/articles.html")]),
        ]),
    ],
}

CSS = """
:root{--navy:#12284c;--navy2:#1d3a6b;--gold:#c9a227;--cream:#faf6ec;--ink:#1f2a3a;--mut:#5b6678;--line:#e3dcc6}
*{box-sizing:border-box}
body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--ink);background:var(--cream);line-height:1.6}
.nav{position:sticky;top:0;z-index:5;background:var(--navy);border-bottom:3px solid var(--gold);padding:10px 18px;display:flex;flex-wrap:wrap;align-items:center;gap:6px 18px}
.brand{color:#fff;font-weight:bold;font-size:1.05rem;margin-right:auto;letter-spacing:.3px}
.brand small{display:block;color:var(--gold);font-weight:normal;font-size:.72rem;letter-spacing:1.5px;text-transform:uppercase}
.nav a{color:#e9edf5;text-decoration:none;font-size:.92rem;padding:5px 2px;border-bottom:2px solid transparent;white-space:nowrap}
.nav a:hover,.nav a.on{color:#fff;border-color:var(--gold)}
.nav a.on{color:var(--gold);font-weight:bold;border-bottom-width:3px}
.nav a.pub{color:var(--gold);font-size:.85rem;border:1px solid var(--gold);border-radius:20px;padding:3px 12px}
.hero{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;padding:44px 22px 38px;text-align:center}
.hero h1{font-size:clamp(1.8rem,4.5vw,2.7rem);margin:0 0 8px;line-height:1.2}
.hero p{max-width:720px;margin:0 auto;font-size:1.1rem;color:#dfe6f2}
.hero .eyebrow{color:var(--gold);letter-spacing:2px;text-transform:uppercase;font-size:.78rem;margin-bottom:10px}
.wrap{max-width:900px;margin:0 auto;padding:26px 20px 20px}
h2{color:var(--navy);font-size:1.5rem;margin:34px 0 6px;border-bottom:2px solid var(--gold);padding-bottom:6px}
h3.group{color:var(--navy);font-size:1.02rem;letter-spacing:1px;text-transform:uppercase;margin:24px 0 8px}
p.lead{color:var(--mut);margin:6px 0 12px}
.item{background:#fff;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:0 8px 8px 0;padding:12px 16px;margin:10px 0}
.item h4{margin:0;color:var(--navy);font-size:1.08rem}
.item p{margin:2px 0 0;color:var(--mut);font-size:.96rem}
.item.pic{display:flex;gap:18px;align-items:center}
.item.pic .ph{flex:0 0 240px;line-height:0}
.item.pic img{width:240px;height:135px;object-fit:cover;border-radius:6px;display:block}
@media(max-width:620px){.item.pic{flex-direction:column;align-items:flex-start}.item.pic .ph,.item.pic img{width:100%;height:auto}}
.item .links{margin-top:8px;display:flex;flex-wrap:wrap;gap:8px}
.item .links a{font:bold .85rem Arial,Helvetica,sans-serif;text-decoration:none;color:var(--navy);border:1.5px solid var(--navy);border-radius:20px;padding:4px 13px}
.item .links a:first-child{background:var(--navy);color:#fff}
.item .links a:hover{background:var(--gold);border-color:var(--gold);color:var(--navy)}
.item.soon{border-left-color:var(--line);background:#fffdf7}
.chip{display:inline-block;font:bold .68rem Arial,Helvetica,sans-serif;letter-spacing:1px;text-transform:uppercase;color:var(--mut);border:1px solid var(--line);border-radius:12px;padding:1px 9px;margin-left:8px;vertical-align:middle}
.vid{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px;margin:10px 0}
.vid video{display:block;width:100%;max-width:640px;margin:0 auto;border-radius:6px;background:#000}
.vid h4{margin:0 0 8px;color:var(--navy);font-size:1.02rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin:18px 0}
a.card{display:block;text-decoration:none;background:#fff;border:1px solid var(--line);border-top:4px solid var(--gold);border-radius:8px;padding:16px 18px;box-shadow:0 2px 6px rgba(18,40,76,.06)}
a.card:hover{box-shadow:0 6px 16px rgba(18,40,76,.16)}
a.card h3{margin:0 0 4px;color:var(--navy);font-size:1.15rem}
a.card p{margin:0;color:var(--mut);font-size:.96rem}
a.card.cc{background:var(--navy);border-color:var(--gold)}
a.card.cc h3{color:var(--gold)}a.card.cc p{color:#dfe6f2}
.start{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin:6px 0 4px}
.start a{display:block;text-decoration:none;background:var(--navy);border-left:5px solid var(--gold);border-radius:0 8px 8px 0;padding:13px 18px}
.start a b{display:block;color:var(--gold);font-size:1.1rem}.start a span{color:#dfe6f2;font-size:.95rem}
.start a:hover{background:var(--navy2)}
.lock{background:#fff;border:1px solid var(--gold);border-radius:8px;padding:14px 18px;margin:14px 0;color:var(--navy);font-weight:bold}
.foot{margin:40px 0 0;padding:20px;text-align:center;color:#c8d1e0;background:var(--navy);font-size:.85rem}
.foot a{color:var(--gold)}
@media(max-width:1100px){.brand{flex:1 0 100%;margin-right:0}}
@media(max-width:560px){.nav{padding:8px 12px;gap:6px 10px}.nav a{font-size:.82rem}}
"""

# Extra styles for the Live Interactive Diagnosis Practice section only.
PRACTICE_CSS = """
.item ol.steps{margin:8px 0 0;padding-left:1.3em;list-style:decimal}
.item ol.cases{margin:8px 0 0;padding-left:0;list-style:none}
.item ol li{margin:10px 0}
.item ol a{color:var(--navy2)}
.item .fine{margin:12px 0 0;font-size:.92rem}
.chip.keep{text-transform:none;letter-spacing:0;font-size:.75rem}
.chip.free{color:var(--navy);border-color:var(--gold);background:#f8f1d8}
.caserow{display:flex;gap:12px;align-items:center}
.casenum{flex:0 0 1.4em;text-align:right;font-weight:bold;color:var(--navy)}
.portrait{flex:0 0 88px;width:88px;height:88px;border-radius:50%;overflow:hidden;background:#f4efe3;border:2px solid var(--gold)}
@media(max-width:560px){.portrait{flex-basis:72px;width:72px;height:72px}}
.portrait img{width:100%;height:100%;object-fit:cover;display:block}
.casetext{min-width:0}
.banner{margin:8px 0 16px}
.banner img{display:block;width:100%;height:auto;border-radius:12px;box-shadow:0 2px 8px rgba(18,40,76,.12)}
.banner figcaption{margin:6px 0 0;font:13px/1.4 Arial,Helvetica,sans-serif;color:var(--mut)}
"""

e = html.escape

# Old room pages that now only forward to the new room (old page -> new page).
FORWARD = {"welcome.html": "index.html", "intro.html": "index.html", "process.html": "process.html",
           "library.html": "library.html", "course.html": "index.html"}
# counselors/ pages that carry the room menu: these open in the same tab.
IN_ROOM = {"books.html", "articles.html", "cases.html", "core-beliefs.html", "reviews.html", "theory.html",
           "tips.html", "tips-ethics.html", "tip-ethics-treatment-modalities.html", "videos.html"}


def href(a):
    return "../counselors/" + a[2:] if a.startswith("C/") else a


# The Lie Finder stands out in the menu: a cream button with a gold ring and a magnifying glass
# (not gold text, which marks the page you are on).
LIE_FINDER = '<a class="lf" target="_top" href="https://www.beliefcounselor.com/false-belief-finder" style="display:inline-flex;align-items:center;gap:6px;background:#faf6ec;color:#12284c;font-weight:bold;border:0;text-decoration:none;border-radius:20px;padding:4px 14px;box-shadow:0 0 0 2px #c9a227 inset"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>Lie Finder</a>'


def nav(current):
    out = ['<div class="nav"><div class="brand">Belief Counseling<small>%s</small></div>' % e(ROOM)]
    for f, label, _, _ in MENU:
        cls = ["on"] if f == current else []
        out.append('<a%s href="%s">%s</a>' % (' class="%s"' % " ".join(cls) if cls else "", f, e(label)))
        if f == "index.html":
            out.append(LIE_FINDER)
    out.append('<a href="../counselors/membership.html">Membership</a>')
    out.append('<a class="pub" target="_blank" rel="noopener" href="%s">Public Site ↗</a></div>' % SITE)
    return "".join(out)


def live_practice():
    """Section that takes the place of Intake Process on Traditional Assessment."""
    intro = (
        "You interview a fictional client, played by an AI, and practice the work as you would in the room. "
        "You walk through the DSM-5-TR diagnostic process, and you practice Belief Counseling: identify a false belief, "
        "challenge it, and replace it with Scripture. An AI supervisor coaches you along the way, with questions to ask, "
        "feedback, and help with the diagnosis."
    )
    sessions = (
        "There are two sessions. Session 1 is the first interview: a functional analysis, a safety check, a diagnostic "
        "hypothesis, belief mining, the first false beliefs, and the assessment tools. Session 2 finishes the diagnosis, "
        "challenges and replaces the main false belief, and chooses the belief cards that fit. At the end, the AI gives "
        "you the diagnosis, feedback, and a report you can print."
    )
    fiction = "Every client is fictional. This is training, not clinical care."
    page_href = e(href("C/cases/case-01-walt-page.html"))
    file_href = e(href("C/cases/case-01-walt.txt"))
    # target=_blank is the fallback when a sandboxed iframe ignores download.
    save = ('<a href="%s" download="Walt-AI-Case-File.txt" target="_blank" rel="noopener">'
            'Save the AI case file</a>' % file_href)
    steps = [
        ('Open <a target="_blank" rel="noopener" href="%s">Walt’s case page</a> and click Print, '
         'so you have the case in front of you. Have a pen and paper ready for notes.' % page_href),
        ("Click ‘%s.’ It saves to your computer’s Downloads folder (on a phone, to your Files)." % save),
        ('Open <a href="https://grok.com" target="_blank" rel="noopener">Grok</a>, '
         '<a href="https://chatgpt.com" target="_blank" rel="noopener">ChatGPT</a>, or '
         '<a href="https://claude.ai" target="_blank" rel="noopener">Claude</a> and sign in to a free account.'),
        "Start a new chat. Click the paperclip or ‘+’ beside the message box and choose Walt-AI-Case-File.txt from Downloads.",
        ("Type OK and press Enter. The Supervisor welcomes you and the interview begins. "
         "Each reply starts with “Walt says:” or “Supervisor here:”. Type COACH anytime for help. "
         "If your messages run out, copy the “PICK UP HERE FOR SESSION 2” block into a new chat. "
         "You can type or use voice."),
    ]
    lis = ["<li>%s</li>" % step for step in steps]
    photo = e(href("C/cases/case-01-walt.jpg"))
    alt = e("Walt (fictional client, AI-generated image)")
    portrait = '<span class="portrait"><img alt="%s" src="%s"></span>' % (alt, photo)
    blank = '<span class="portrait"></span>'

    def row(n, photo_html, body):
        return ('<li><span class="caserow"><span class="casenum">%d.</span>%s'
                '<span class="casetext">%s</span></span></li>' % (n, photo_html, body))

    walt = ('<strong>Walt</strong> <span class="chip keep free">Free sample case</span>'
            "<p>58-year-old band director, referred by his doctor. He says he is “just tired.”</p>"
            '<div class="links"><a target="_blank" rel="noopener" href="%s">Open case</a>'
            '<a href="%s" download="Walt-AI-Case-File.txt" target="_blank" rel="noopener">Save the AI case file</a></div>' % (page_href, file_href))
    cases = [row(1, portrait, walt)]
    for n in range(2, 11):
        cases.append(row(n, blank, 'Coming soon <span class="chip keep">Members</span>'))
    note = "One case is free for everyone. Members ($14.95) get the full case list."
    banner = e(href("C/cases/diagnosis-practice-banner.jpg"))
    banner_alt = e("A counselor in training takes notes while interviewing a fictional AI client on her laptop.")
    return (
        "<h2>Live Interactive Diagnosis Practice</h2>"
        '<figure class="banner"><img alt="%s" src="%s">'
        '<figcaption>AI-generated image.</figcaption></figure>'
        '<div class="item"><h4>AI-assisted practice cases</h4><p>%s</p><p>%s</p><p>%s</p></div>'
        '<div class="item"><h4>How to start a case</h4><ol class="steps">%s</ol></div>'
        '<div class="item"><h4>Practice Cases</h4><ol class="cases">%s</ol><p class="fine">%s</p></div>'
        % (banner_alt, banner, e(intro), e(sessions), e(fiction), "".join(lis), "".join(cases), e(note))
    )


def item(it):
    if it[0] == "group":
        return '<h3 class="group">%s</h3>' % e(it[1])
    if it[0] == "video":
        base = href(it[2])
        return ('<div class="vid"><h4>▶ Video: %s</h4><video controls preload="none" poster="%s.jpg">'
                '<source src="%s.mp4" type="video/mp4"></video></div>' % (e(it[1]), base, base))
    title, desc, links = it[:3]
    pic = it[3] if len(it) > 3 else ""
    if not links:
        return '<div class="item soon"><h4>%s<span class="chip">Coming</span></h4>%s</div>' % (
            e(title), "<p>%s</p>" % e(desc) if desc else "")
    ls = "".join('<a%s href="%s">%s</a>' % (
        "" if a[2:] in IN_ROOM else ' target="_blank" rel="noopener"', e(href(a)), e(l)) for l, a in links)
    if pic:
        return ('<div class="item pic"><a class="ph" target="_blank" rel="noopener" href="%s"><img src="%s" alt=""></a>'
                '<div><h4>%s</h4>%s<div class="links">%s</div></div></div>' % (
                    e(href(links[0][1])), e(pic), e(title), "<p>%s</p>" % e(desc) if desc else "", ls))
    return '<div class="item"><h4>%s</h4>%s<div class="links">%s</div></div>' % (
        e(title), "<p>%s</p>" % e(desc) if desc else "", ls)


def page(f, label, heading, summary):
    if f == "index.html":
        cards = "".join('<a class="card%s" href="%s"><h3>%s</h3><p>%s</p></a>' % (
            " cc" if g == "clinical-companion.html" else "", g, e(l), e(s)) for g, l, _, s in MENU[1:])
        start = ('<div class="start"><a href="../counselors/landing.html"><b>Start here: Introduction</b>'
                 '<span>What this site is for, an overview, and how to find your way around.</span></a>'
                 '<a href="../counselors/membership.html"><b>Membership</b>'
                 '<span>$14.95 a month. Cancel anytime. How sign-up works and what is included.</span></a></div>')
        body = start + '<div class="grid">%s</div>' % cards
    else:
        parts = []
        for title, lead, items in PAGES[f]:
            if title == "LIVE_PRACTICE":
                parts.append(live_practice())
                continue
            if title:
                parts.append("<h2>%s</h2>" % e(title))
            if lead:
                parts.append('<p class="lead">%s</p>' % e(lead))
            parts.extend(item(i) for i in items)
        body = "".join(parts)
        if f == "clinical-companion.html":
            body = '<div class="lock">🔒 No access until membership is paid for.</div>' + body
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><style>%s</style></head><body>'
            '%s'
            '<div class="hero"><div class="eyebrow">Belief Counseling for Counselors</div><h1>%s</h1><p>%s</p></div>'
            '<div class="wrap">%s</div>'
            '<div class="foot">Educational training for counselors. Never enter real client names or details. · '
            '© Brian Campbell, Ph.D. · <a href="%s/help" target="_top">Help &amp; Support</a></div><script>/* When moving between pages inside the Wix page, show the new page from its top. */(function(){try{if(window.top!==window&&document.referrer&&new URL(document.referrer).host===location.host){var t=document.body.firstElementChild||document.body;t.scrollIntoView({block:\"start\"});}}catch(e){}})();</script></body></html>'
            % (e(heading), CSS + (PRACTICE_CSS if f == "assessment.html" else ""), nav(f), e(heading), e(summary), body, SITE))


def main():
    OUT.mkdir(exist_ok=True)
    for f, label, heading, summary in MENU:
        (OUT / f).write_text(page(f, label, heading, summary), encoding="utf-8")
        print("wrote members/" + f)
    for old, new in FORWARD.items():
        to = "../members/" + new
        (ROOT / "counselors" / old).write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title>'
            '<meta http-equiv="refresh" content="0; url=%s"><script>location.replace("%s")</script></head>'
            '<body><p><a href="%s">Continue to the %s</a></p></body></html>' % (e(ROOM), to, to, to, e(ROOM)),
            encoding="utf-8")
        print("forwarder counselors/" + old)


if __name__ == "__main__":
    main()
