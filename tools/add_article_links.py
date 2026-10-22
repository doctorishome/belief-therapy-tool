"""Adds a "Read more" article box to belief cards, right after the Truth summary.

Run:  python3 tools/add_article_links.py
Safe to run again: a card that already has the box is updated in place, not duplicated.
If a card is rebuilt with its builder, run this script again to put the box back.

To add an article to more cards, add the card's page path to that article's "cards" list below.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://doctorishome.github.io/belief-therapy-tool/belief-cards/articles/"

ARTICLES = {
    "free-will-pain-suffering": {
        "title": "Free Will, Pain, and Suffering",
        "author": "Dr. Brian Campbell",
        "blurb": "Why your pain is not God’s punishment, and where to find hope, including Nick Vujicic’s story.",
        "page": BASE + "Free-Will-Pain-and-Suffering.html",
        "pdf": BASE + "Free-Will-Pain-and-Suffering.pdf",
        "cards": [
            "belief-cards/Belief-002-If-There-Is-A-God-He-Would-Not-Let-This-Happen.html",
            "belief-cards/Belief-073-My-Illness-Disability-Or-Scars-Will-Last-Forever.html",
            "belief-cards/Belief-077-God-Took-My-Loved-One-Because-He-Needed-Them.html",
            "belief-cards/Belief-106-If-I-Am-Suffering-God-Is-Punishing-Me.html",
            "belief-cards/Belief-107-Real-Christians-Dont-Suffer.html",
            "belief-cards/Belief-108-I-Must-Figure-Out-The-Reason-For-Everything-Bad.html",
            "belief-cards/Belief-110-My-Suffering-Means-God-Has-Abandoned-Me.html",
            "belief-cards/Belief-120-Natural-Disasters-Are-God-Punishing-The-People-They-Strike.html",
            "belief-cards/interpersonal/grief-loss/Inter-049-God-Took-Them-From-Me-to-Punish-Me.html",
            "belief-cards/biological/chronic-pain/Bio-006-This-Pain-Will-Never-End.html",
            "belief-cards/biological/chronic-pain/Bio-008-I-Cant-Be-Happy-as-Long-as-I-Hurt.html",
            "belief-cards/biological/serving-god-with-limits/Bio-075-Only-Healthy-Strong-People-Can-Serve-God-Well.html",
            "belief-cards/biological/why-god-allows-suffering/Bio-061-God-Is-Punishing-Me-With-This-Illness.html",
            "belief-cards/biological/why-god-allows-suffering/Bio-062-I-Must-Have-Done-Something-to-Deserve-This.html",
            "belief-cards/biological/why-god-allows-suffering/Bio-063-A-Loving-God-Wouldnt-Let-Me-Suffer-Like-This.html",
            "belief-cards/biological/why-god-allows-suffering/Bio-064-God-Has-Abandoned-Me.html",
            "belief-cards/biological/why-god-allows-suffering/Bio-065-My-Suffering-Is-Meaningless.html",
        ],
    },
}

BTN = ("display:inline-block;padding:9px 16px;border-radius:6px;font-weight:600;text-decoration:none;"
       "font-size:.95em;margin:6px 8px 0 0;")


def box(key, a):
    pdf_name = a["pdf"].rsplit("/", 1)[1]
    return (
        '<!--article:%s-->'
        '<div class="article-box" style="border:1px solid var(--gold,#B08A4B);border-radius:8px;'
        'padding:14px 18px;margin:18px 0;background:#fff">'
        '<p style="margin:0 0 4px;color:var(--gold,#B08A4B);font-size:.8em;letter-spacing:.12em;'
        'text-transform:uppercase">Read more</p>'
        '<p style="margin:0 0 4px"><b style="color:var(--navy,#1F3A5F)"><i>%s</i></b>, by %s</p>'
        '<p style="margin:0 0 4px">%s</p>'
        '<a href="%s" target="_blank" rel="noopener" style="%sbackground:var(--navy,#1F3A5F);color:#fff">Read online</a>'
        '<a href="%s" download="%s" target="_blank" rel="noopener" style="%sborder:1px solid var(--navy,#1F3A5F);'
        'color:var(--navy,#1F3A5F)">Download PDF</a>'
        '</div><!--/article:%s-->'
    ) % (key, a["title"], a["author"], a["blurb"], a["page"], BTN, a["pdf"], pdf_name, BTN, key)


changed = 0
for key, a in ARTICLES.items():
    block = box(key, a)
    old = re.compile(r"<!--article:%s-->.*?<!--/article:%s-->" % (key, key), re.S)
    for rel in a["cards"]:
        path = ROOT / rel
        t = path.read_text(encoding="utf-8")
        if old.search(t):
            new = old.sub(lambda m: block, t)
        else:
            m = re.search(r'(<h2>Truth summary</h2>\s*<p class="truth">.*?</p>)', t, re.S)
            if not m:
                print("NO TRUTH SUMMARY:", rel)
                continue
            new = t[:m.end()] + "\n" + block + t[m.end():]
        if new != t:
            path.write_text(new, encoding="utf-8")
            changed += 1
print(changed, "card(s) updated")
