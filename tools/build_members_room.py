"""Build the Member's Room from Brian's "Basic Organization" outline (Nov 12, 2026).

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
ROOM = "Member’s Room"
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
     "Diagnosis, intake, the forms your client completes, and the first interview."),
    ("tips.html", "Professional Tips", "Professional Tips",
     "Tips, case studies, theory, and insights from 35 years of practice."),
    ("library.html", "Library", "Library",
     "Books, videos, and articles."),
    ("clinical-companion.html", "Clinical Companion", "Clinical Companion",
     "The working tool for your own cases, from the first phone call on. For paid members."),
]


def video(n, slug, title):
    return ("video", title, "C/videos/lesson-%d-%s" % (n, slug))


PAGES = {
    "belief-counseling.html": [
        ("", "", [
            ("What Is a Belief?", "What beliefs are and how they shape thinking, feeling, and behavior.",
             [("Open page", SITE + "/beliefs")]),
            ("What Is Belief Counseling?", "The approach in plain language: identify, challenge, and replace false beliefs with truth.",
             [("Open page", SITE + "/belief-counseling")]),
            ("Why Beliefs Matter", "Why Belief Counseling starts with beliefs, one step beneath emotions and behavior.",
             [("Open page", SITE + "/belief-counseling")]),
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
            ("group", "Spiritual Assessment Tools"),
            ("Christian Experiences and Beliefs", "Church background, family faith, and present beliefs. Counselor-guided.",
             [("Open (PDF)", F + "Christian-Experiences-and-Beliefs-Checklist.pdf"),
              ("Word", F + "Christian-Experiences-and-Beliefs-Checklist.docx")]),
            ("RSS-5", "Religious and Spiritual Struggles Scale, five-question short form.", []),
            ("Brief RCOPE", "A short measure of religious coping, for when a specific stressor is central.", []),
            ("SAI", "Spiritual Assessment Inventory, for in-depth work.", []),
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
        ("", "This section shows what the assessment process looks like, including the forms your client "
             "will see and complete online. You carry it out with your own clients in the Clinical Companion.", [
            ("The Flow: Start Here", "A narrated presentation that walks through the whole process, "
                                     "from the first phone call to the treatment plan. Watch this first.", []),
        ]),
        ("DSM-5-TR", "", [
            ("Training", "The DSM-5-TR diagnostic process, step by step (narrated slides).",
             [("Open slides", "C/presentations/diagnostic-process/index.html"),
              ("Flow chart", "C/reviews/dsm5tr-flow-chart.html")]),
            ("Tutorial", "Practice tutorial: DSM-5-TR diagnosis and coding.",
             [("Open tutorial", "C/presentations/diagnostic-process/tutorial.html")]),
        ]),
        ("Intake Process", "", [
            ("Telephone Intake Form", "", []),
            ("Screen & Refer", "", []),
            ("Provide Link to Online Assessment", "The link the client receives after the call.",
             [("See what the client sees", "C/new-client-forms.html")]),
        ]),
        ("Online Assessment", "The forms the client completes before the first visit.", [
            ("Client forms", "Client Basic Information · Consent for Treatment · Insurance Information · "
                             "Confidentiality · Release of Records · Adult History",
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
            ("False Beliefs", "Use the False Belief Finder to find the false beliefs affecting a client.",
             [("Open False Belief Finder", SITE + "/false-belief-finder")]),
            ("Treatment Plan", "", []),
        ]),
    ],
    "tips.html": [
        ("", "", [
            ("Introduction", "How the Professional Tips work and the topics you can expect.",
             [("Open", "C/tips.html")]),
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
    "clinical-companion.html": [
        ("", "The Clinical Companion is where you work your own cases. It opens once your membership is paid.", [
            ("Introduction", "", []),
            ("Watch the Flow Again", "A refresher before your first case: the same narrated presentation "
                                     "shown under Traditional Assessment.", []),
            ("Start: Telephone Intake", "The Companion begins at step 1, the telephone intake.",
             [("Open the Clinical Companion", SITE + "/clinical-companion")]),
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
.nav a.cc{color:var(--navy);background:var(--gold);border:0;border-radius:20px;padding:4px 14px;font-weight:bold}
.nav a.cc.on{box-shadow:0 0 0 2px #fff}
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
.lock{background:#fff;border:1px solid var(--gold);border-radius:8px;padding:14px 18px;margin:14px 0;color:var(--navy);font-weight:bold}
.foot{margin:40px 0 0;padding:20px;text-align:center;color:#c8d1e0;background:var(--navy);font-size:.85rem}
.foot a{color:var(--gold)}
@media(max-width:1100px){.brand{flex:1 0 100%;margin-right:0}}
@media(max-width:560px){.nav{padding:8px 12px;gap:6px 10px}.nav a{font-size:.82rem}}
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


def nav(current):
    out = ['<div class="nav"><div class="brand">Belief Counseling<small>%s</small></div>' % e(ROOM)]
    for f, label, _, _ in MENU:
        cls = [c for c in ("cc" if f == "clinical-companion.html" else "", "on" if f == current else "") if c]
        out.append('<a%s href="%s">%s</a>' % (' class="%s"' % " ".join(cls) if cls else "", f, e(label)))
    out.append('<a class="pub" target="_blank" rel="noopener" href="%s">Public Site ↗</a></div>' % SITE)
    return "".join(out)


def item(it):
    if it[0] == "group":
        return '<h3 class="group">%s</h3>' % e(it[1])
    if it[0] == "video":
        base = href(it[2])
        return ('<div class="vid"><h4>▶ Video: %s</h4><video controls preload="none" poster="%s.jpg">'
                '<source src="%s.mp4" type="video/mp4"></video></div>' % (e(it[1]), base, base))
    title, desc, links = it
    if not links:
        return '<div class="item soon"><h4>%s<span class="chip">Coming</span></h4>%s</div>' % (
            e(title), "<p>%s</p>" % e(desc) if desc else "")
    ls = "".join('<a%s href="%s">%s</a>' % (
        "" if a[2:] in IN_ROOM else ' target="_blank" rel="noopener"', e(href(a)), e(l)) for l, a in links)
    return '<div class="item"><h4>%s</h4>%s<div class="links">%s</div></div>' % (
        e(title), "<p>%s</p>" % e(desc) if desc else "", ls)


def page(f, label, heading, summary):
    if f == "index.html":
        cards = "".join('<a class="card%s" href="%s"><h3>%s</h3><p>%s</p></a>' % (
            " cc" if g == "clinical-companion.html" else "", g, e(l), e(s)) for g, l, _, s in MENU[1:])
        body = '<div class="grid">%s</div>' % cards
    else:
        parts = []
        for title, lead, items in PAGES[f]:
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
            '© Brian Campbell, Ph.D. · <a href="%s/help" target="_top">Help &amp; Support</a></div></body></html>'
            % (e(heading), CSS, nav(f), e(heading), e(summary), body, SITE))


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
