"""Builds counselors/clinical-companion.html: the Clinical Companion page, laid out by the Flow of Care.

Edit the SECTIONS list below, then run:  python3 tools/build_companion_page.py
Each step is (number, title, one-line summary, [links]).  A link is (label, href) or (label, None) for "coming soon".
Links open in a new tab.
"""
import html, os

PUB = "https://www.beliefcounselor.com"
APP = "https://doctorishome.github.io/belief-therapy-tool/app/"

FOUNDATIONS = [
    ("F1", "Foundations 1: The Basics", "Start with the same pages the public reads, so you and your clients share the same language.", [
        ("What Is a Belief?", PUB + "/beliefs"),
        ("What Is Belief Counseling?", PUB + "/belief-counseling"),
        ("What Is Belief Mining? (including Why Beliefs Matter and the six levels)", PUB + "/belief-mining"),
        ("Videos", "videos.html"),
        ("Dr. Campbell's videos on the basics", None),
    ]),
    ("F2", "Foundations 2: Counselor Reading", "The history, ethics, and theory behind Belief Counseling, including competence and when to refer.", [
        ("From CBT to Christian CBT: A Brief History (PDF)", "theory/From-CBT-to-Christian-CBT.pdf"),
        ("Professional Tip: Ethical Considerations When Choosing Treatment Modalities", "tip-ethics-treatment-modalities.html"),
        ("How Beliefs Influence Personality (PDF)", "theory/How-Beliefs-Influence-Personality.pdf"),
        ("Professional Competencies for Providing Christian CBT (PDF)", "theory/Belief-Counseling-Competencies.pdf"),
        ("Why Belief Counseling?", None),
    ]),
    ("F3", "Foundations 3: Assessment Skills", "Learn these before your first client. They are the skills the steps below depend on.", [
        ("The DSM-5-TR diagnostic process: step-by-step slides (narrated)", "presentations/diagnostic-process/index.html"),
        ("Practice tutorial: DSM-5-TR diagnosis and coding", "presentations/diagnostic-process/tutorial.html"),
        ("The diagnostic process flow chart", "reviews/dsm5tr-flow-chart.html"),
        ("Download the PowerPoint", "reviews/dsm5tr-diagnostic-process.pptx"),
        ("Functional analysis of the presenting problem (tutorial)", None),
        ("Guide to the screening forms: in the Clinical Companion app, Library › Step 9: Follow-up Forms and Screens", APP),
    ]),
]

GROUPS = [
    ("Before the first visit", [
        ("1", "Telephone Intake", "A trained intake person takes the call, screens for fit, explains the faith-integrated approach, schedules the first visit, and asks: online or paper forms?", [
            ("Telephone Intake form", None),
            ("Crisis script and referral list", None),
        ]),
        ("2", "Online (or Paper) Intake", "The client completes About You and a Brief History before the first visit. Paper copies match the online forms.", [
            ("New Client Forms (the link the client receives)", "new-client-forms.html"),
            ("New Client Packet (fill in your practice details)", "practice-forms.html"),
            ("Confidentiality agreement (PDF)", "forms/Confidentiality-Agreement-fillable.pdf"),
            ("Pastoral confidentiality agreement (PDF)", "forms/Pastoral-Confidentiality-Agreement-fillable.pdf"),
            ("Online consent forms (treatment, release of information, Client Handbook)", None),
        ]),
        ("3", "Schedule the First Visit", "Set the first appointment.", []),
        ("4", "Assessment Report Begins", "The intake information goes into the client's file, and the AI starts the Assessment Report.", [
            ("Start Clinical Companion", APP),
        ]),
        ("5", "Review Intake Information", "Before the first interview, review everything, including the AI's report, and form an initial hypothesis about the diagnosis and about toxic beliefs.", []),
    ]),
    ("Sessions", [
        ("6", "Initial Interview", "Belief mining begins: a counselor-led functional analysis of the presenting problem, safety issues, and a review of the intake forms.", [
            ("Presenting Problem Assessment (counselor's interview guide)", None),
            ("Mining Tools for all six levels (table on The Process page)", "process.html"),
            ("Anxious Thoughts & Beliefs Checklist (PDF)", "forms/Belief-Counseling-Anxious-Thoughts-and-Beliefs-Checklist.pdf"),
            ("Depressive Thoughts & Beliefs Checklist (PDF)", "forms/Belief-Counseling-Depressive-Thoughts-and-Beliefs-Checklist.pdf"),
            ("Deeper Issues: A Checklist of Core Beliefs (PDF)", "forms/Belief-Counseling-Deeper-Issues-Checklist-of-Core-Beliefs.pdf"),
            ("Discover the Lies (PDF)", "forms/Belief-Counseling-Discover-the-Lies.pdf"),
            ("Parental Messages Checklist (PDF)", "forms/Belief-Counseling-Parental-Messages-Checklist.pdf"),
            ("Adult History (only when needed)", None),
        ]),
        ("7", "Develop Hypotheses", "Develop hypotheses about the diagnosis and the possible false beliefs.", [
            ("Core False Beliefs", "core-beliefs.html"),
        ]),
        ("8", "Counselor Enters the Case Note", "Dictate your hypotheses and findings into the case note. The AI adds the interview findings and suggests DSM-5-TR and belief questions for the next session. Steps 6 to 8 repeat after every session.", [
            ("Start Clinical Companion", APP),
        ]),
        ("9", "Follow-up Tests or Assessments", "At the end of the session, check off the forms the client should complete, then send one link or print the card.", [
            ("Forms to Complete card (PHQ-9, GAD-7, spiritual screens, and more)", "followup-forms.html"),
            ("Life Events and Beliefs Screening", "../Life_Events_Beliefs_Screening.html"),
            ("Christian Experiences and Beliefs Checklist (PDF)", "forms/Belief-Counseling-Christian-Experiences-and-Beliefs-Checklist.pdf"),
            ("Christian Experiences and Beliefs Checklist (Word)", "forms/Belief-Counseling-Christian-Experiences-and-Beliefs-Checklist.docx"),
        ]),
    ]),
    ("Diagnosis and treatment", [
        ("10", "Diagnosis + Identify", "Make the DSM-5-TR diagnosis while identifying the client's false beliefs.", [
            ("Refresher: the DSM-5-TR diagnostic process (Foundations 3)", "#F3"),
            ("DSM-5-TR Reviews of specific disorders", "reviews.html"),
            ("False Belief Finder", PUB + "/false-belief-finder"),
            ("Core False Beliefs", "core-beliefs.html"),
            ("Personality Belief Questionnaire materials", None),
        ]),
        ("11", "Treatment Plan", "Build the plan from the diagnosis and the false beliefs.", []),
        ("12", "Challenge", "Question the false beliefs with secular and Christian techniques.", [
            ("Questioning False Beliefs worksheet (PDF)", "forms/Belief-Counseling-Questioning-False-Beliefs.pdf"),
            ("Questioning False Beliefs worksheet (Word)", "forms/Belief-Counseling-Questioning-False-Beliefs.docx"),
            ("Cognitive Errors Checklist (PDF)", "forms/Belief-Counseling-Cognitive-Errors-Checklist.pdf"),
            ("Video: Questioning Your Beliefs", "videos.html"),
            ("Questioning Beliefs (public page)", PUB + "/blank-3"),
            ("Behavioral Experiments (public page)", PUB + "/blank-5"),
        ]),
        ("13", "Replace", "Replace the false beliefs with the truth.", [
            ("Pearls Scripture Search", PUB + "/scriptures"),
            ("Books (Recommended): Pearls, Godly Counsel, Christlike, and more", "books.html"),
        ]),
        ("14", "Belief Cards", "Use the public belief cards as homework.", [
            ("Core False Beliefs cards", PUB + "/core-beliefs"),
            ("Spiritual/Religious False Beliefs cards", PUB + "/spiritual-religious-false-beliefs"),
            ("Biological/Physical False Beliefs cards", PUB + "/biological-physical-false-beliefs"),
            ("Psychological/Cognitive False Beliefs cards", PUB + "/blank-7"),
            ("Interpersonal False Beliefs cards", PUB + "/blank-8"),
            ("Socioeconomic False Beliefs cards", PUB + "/blank-9"),
            ("Sociocultural False Beliefs cards", PUB + "/blank-10"),
            ("Clinical background notes for each card", None),
        ]),
    ]),
]

e = html.escape


def links(items):
    if not items:
        return ""
    out = []
    for label, href in items:
        if href is None:
            out.append(f'<li class="soon">{e(label)} <span>Coming soon</span></li>')
        elif href.startswith("#"):
            out.append(f'<li><a href="{href}">{e(label)}</a></li>')
        else:
            out.append(f'<li><a href="{e(href)}" target="_blank" rel="noopener">{e(label)} <span class="nt">↗</span></a></li>')
    return '<ul class="tools">' + "".join(out) + "</ul>"


def block(num, title, summary, items, found=False):
    badge = f'<div class="num{" f" if found else ""}">{e(num)}</div>'
    return (f'<section class="step{" found" if found else ""}" id="{"F" + num[1:] if found else "s" + num}">{badge}'
            f'<div class="body"><h3>{e(title)}</h3><p>{e(summary)}</p>{links(items)}</div></section>')


CSS = """
:root{--navy:#12284c;--navy2:#1d3a6b;--gold:#c9a227;--cream:#faf6ec;--ink:#1f2a3a;--mut:#5b6678;--line:#e3dcc6;--amber:#faeeda;--amberline:#c99a4a}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--ink);background:var(--cream);line-height:1.6}
a{color:var(--navy2)}
.hero{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;padding:40px 22px 34px;text-align:center}
.hero h1{font-size:clamp(1.8rem,4.5vw,2.7rem);margin:0 0 8px;line-height:1.2}
.hero .eyebrow{color:var(--gold);letter-spacing:2px;text-transform:uppercase;font-size:.78rem;margin-bottom:10px}
.hero p.lead{max-width:680px;margin:0 auto 18px;color:#dfe6f2;font-size:1.08rem}
.btn{display:inline-block;background:var(--gold);color:var(--navy);font-weight:bold;text-decoration:none;padding:13px 30px;border-radius:30px;font-size:1.05rem}
a.btn.startcc{padding:16px 38px;font-size:1.25rem;box-shadow:0 6px 18px rgba(0,0,0,.28)}a.btn.startcc:hover{background:#e0b83a}
.hero .startnote{margin:10px auto 0;max-width:640px;color:#f6e7b8;font-size:.98rem}
.hero .backline{margin:16px 0 0}
.hero a.back{color:#fff;font-weight:bold;text-decoration:none;border-bottom:2px solid var(--gold)}
.hero a.needhelp{display:inline-block;margin-top:12px;color:var(--gold);font-size:.95rem}
.wrap{max-width:900px;margin:0 auto;padding:26px 18px 20px}
.jump{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:0 0 10px}
.jump a{background:#fff;border:1px solid var(--line);border-radius:20px;padding:5px 14px;text-decoration:none;font-size:.92rem;color:var(--navy)}
.jump a:hover{border-color:var(--gold)}
h2{color:var(--navy);font-size:1.5rem;margin:30px 0 6px;border-bottom:2px solid var(--gold);padding-bottom:6px}
.intro{color:var(--mut);margin:4px 0 10px}
.step{display:flex;gap:16px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:12px 0;scroll-margin-top:12px}
.step.found{background:var(--amber);border-color:var(--amberline)}
.num{flex:0 0 44px;width:44px;height:44px;border-radius:50%;background:var(--navy);color:var(--gold);font-weight:bold;display:flex;align-items:center;justify-content:center;font-size:1.15rem}
.num.f{background:#854f0b;color:#fff;font-size:1rem}
.body{flex:1;min-width:0}
.body h3{margin:2px 0 2px;color:var(--navy);font-size:1.15rem}
.body p{margin:0;color:var(--ink)}
ul.tools{list-style:none;padding:0;margin:10px 0 0}
ul.tools li{margin:6px 0;padding-left:18px;position:relative}
ul.tools li::before{content:"›";position:absolute;left:2px;color:var(--gold);font-weight:bold}
ul.tools a{font-weight:bold;text-decoration:none;border-bottom:1px solid var(--line)}
ul.tools a:hover{border-color:var(--gold)}
ul.tools .nt{font-weight:normal;color:var(--mut);font-size:.85em}
ul.tools li.soon{color:var(--mut)}
ul.tools li.soon span{font-size:.78rem;background:#eee8d6;border-radius:10px;padding:1px 8px;margin-left:4px;white-space:nowrap}
.card{background:#fff;border:1px solid var(--line);border-top:4px solid var(--gold);border-radius:8px;padding:14px 18px;margin:14px 0}
.card p{margin:0}
.foot{margin:40px 0 0;padding:20px;text-align:center;color:#c8d1e0;background:var(--navy);font-size:.85rem}.foot a{color:var(--gold)}
@media(max-width:560px){.step{flex-direction:column;gap:8px}.wrap{padding:20px 12px}}
"""


def build():
    parts = []
    parts.append('<h2 id="foundations">Foundations</h2><p class="intro">Complete these before you see clients. Each one builds on the one before.</p>')
    for i, (num, title, summary, items) in enumerate(FOUNDATIONS):
        parts.append(block("F" + str(i + 1), title, summary, items, found=True))
    gid = ["before", "sessions", "treatment"]
    for (gname, steps), g in zip(GROUPS, gid):
        parts.append(f'<h2 id="{g}">{e(gname)}</h2>')
        for s in steps:
            parts.append(block(*s))
    jump = ('<nav class="jump"><a href="#foundations">Foundations</a><a href="#before">Steps 1–5: Before the first visit</a>'
            '<a href="#sessions">Steps 6–9: Sessions</a><a href="#treatment">Steps 10–14: Diagnosis and treatment</a>'
            '<a href="forms/Clinical-Companion-Flow-of-Care.pdf" target="_blank" rel="noopener">Flow of Care chart (PDF) ↗</a></nav>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Clinical Companion</title><style>{CSS}</style></head><body><!--standalone-->
<div class="hero"><div class="eyebrow">Members</div><h1>Clinical Companion</h1>
<p class="lead">Everything you need, in the order you use it with a client: from the foundations, through the first phone call, to the belief cards your client takes home.</p>
<a class="btn startcc" href="{APP}" target="_top">Start Clinical Companion</a>
<p class="startnote">Practice mode. Use fictional cases only. This is not yet for real client data.</p>
<p class="backline"><a class="back" href="https://www.beliefcounselor.com/blank-11" target="_top">← Back to the Counselors’ Room</a></p>
<a class="needhelp" href="https://www.beliefcounselor.com/help" target="_top">Need Help?</a></div>
<div class="wrap">{jump}
<div class="card"><p>Clinical Companion supports, and does not replace, your professional clinical judgment. Client information is safeguarded: case files are encrypted, and secure, protected connections are being completed. Until they are finished, please practice with fictional cases. Links open in a new tab.</p></div>
{''.join(parts)}
</div>
<div class="foot">Educational training for counselors. Never enter real client names or details. · © 2026 Brian Campbell, Ph.D. · <a href="https://www.beliefcounselor.com/account-settings" target="_top">My Account</a> · <a href="https://www.beliefcounselor.com/my-subscriptions" target="_top">My Subscriptions</a> · <a href="https://www.beliefcounselor.com/help" target="_top">Help</a></div>
</body></html>
"""
    out = os.path.join(os.path.dirname(__file__), "..", "counselors", "clinical-companion.html")
    open(out, "w").write(page)
    print("wrote", os.path.normpath(out))


if __name__ == "__main__":
    build()
