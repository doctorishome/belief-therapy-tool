"""Writes the Counselors' Room menu into every counselors/*.html page that has a <!--nav-->...<!--/nav--> block.

Edit MENU below, then run:  python3 tools/update_counselor_nav.py
"""
import glob, os, re

CC = "https://www.beliefcounselor.com/clinical-companion"
MENU = [
    ("Learn", [("intro.html", "Introduction (Start here)"), ("process.html", "The Process"), ("theory.html", "Theory"),
               ("core-beliefs.html", "Core False Beliefs"), ("reviews.html", "DSM-5-TR Reviews"), ("videos.html", "Videos")]),
    ("Practice", [("cases.html", "Case Studies"), ("course.html", "The Course")]),
    ("Reading", [("articles.html", "Articles"), ("tips.html", "Professional Tips"), ("tips-ethics.html", "Ethics", "sub"),
                 ("books.html", "Books (Recommended)")]),
]
# Pages that are not in the menu but belong under a section (so that section is underlined)
EXTRA = {"tip-ethics-treatment-modalities.html": "Reading"}


def nav(page):
    h = ['<!--nav--><div class="nav"><div class="brand">Belief Counseling<small>For Counselors</small></div>']
    h.append(f'<a class="l{" on" if page == "welcome.html" else ""}" href="welcome.html">Welcome</a>')
    h.append(f'<a class="l cc" target="_top" href="{CC}" style="color:var(--navy);background:var(--gold);border:0;border-radius:20px;padding:4px 14px;font-weight:bold">Clinical Companion</a>')
    for name, items in MENU:
        on = page in [i[0] for i in items] or EXTRA.get(page) == name
        h.append(f'<div class="dd{" on" if on else ""}"><button type="button" aria-haspopup="true" aria-expanded="false">{name}</button><div class="menu">')
        for it in items:
            cls = ' class="sub"' if len(it) > 2 else ""
            h.append(f'<a{cls} href="{it[0]}">{it[1]}</a>')
        h.append('<button type="button" class="x" aria-label="Close menu">Close &#10005;</button></div></div>')
    h.append('<span class="acct"><a class="l" target="_top" href="https://www.beliefcounselor.com/my-subscriptions">My Subscriptions</a>'
             '<a class="l" target="_top" href="https://www.beliefcounselor.com/account-settings">My Account</a></span>'
             '<a class="pub" target="_blank" rel="noopener" href="https://www.beliefcounselor.com">Public Site ↗</a>'
             '<a class="needhelp" target="_top" href="https://www.beliefcounselor.com/help">Need Help?</a></div><!--/nav-->')
    return "".join(h)


def main():
    d = os.path.join(os.path.dirname(__file__), "..", "counselors")
    for f in sorted(glob.glob(os.path.join(d, "*.html"))):
        s = open(f).read()
        if "<!--nav-->" not in s:
            continue
        page = os.path.basename(f)
        new = re.sub(r"<!--nav-->.*?<!--/nav-->", lambda m: nav(page), s, count=1, flags=re.S)
        if new != s:
            open(f, "w").write(new)
            print("updated", page)


if __name__ == "__main__":
    main()
