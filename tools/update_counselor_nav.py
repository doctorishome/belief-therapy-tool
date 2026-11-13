"""Writes the Counselors' Room menu into every counselors/*.html page that has a <!--nav-->...<!--/nav--> block.

Edit MENU below, then run:  python3 tools/update_counselor_nav.py
"""
import glob, os, re

# The menu matches the Counselors' Room (members/, built by tools/build_members_room.py).
M = "../members/"
MENU = [("index.html", "Welcome"), ("belief-counseling.html", "Belief Counseling"), ("process.html", "The Process"),
        ("assessment.html", "Traditional Assessment"), ("tips.html", "Professional Tips"), ("library.html", "Library")]
# Which menu item is underlined on each kept page
SECTION = {"core-beliefs.html": "process.html", "reviews.html": "assessment.html",
           "tips.html": "tips.html", "tips-ethics.html": "tips.html", "tip-ethics-treatment-modalities.html": "tips.html",
           "cases.html": "tips.html", "theory.html": "tips.html",
           "books.html": "library.html", "videos.html": "library.html", "articles.html": "library.html"}


def nav(page):
    h = ['<!--nav--><div class="nav"><div class="brand">Belief Counseling<small>Counselors’ Room</small></div>']
    for f, label in MENU:
        h.append(f'<a class="l{" on" if SECTION.get(page) == f else ""}" href="{M}{f}">{label}</a>')
    h.append(f'<a class="l" href="{M}clinical-companion.html">Clinical Companion</a>')
    h.append(f'<a class="l" href="../counselors/membership.html">Membership</a>')
    h.append('<span class="acct"><a class="l" target="_top" href="https://www.beliefcounselor.com/my-subscriptions">My Subscriptions</a>'
             '<a class="l" target="_top" href="https://www.beliefcounselor.com/account-settings">My Account</a></span>'
             '<a class="pub" target="_blank" rel="noopener" href="https://www.beliefcounselor.com">Public Site ↗</a>'
             '<a class="needhelp" target="_top" href="https://www.beliefcounselor.com/help">Need Help?</a></div><script>/* When moving between pages inside the Wix page, show the new page from its top. */(function(){try{if(window.top!==window&&document.referrer&&new URL(document.referrer).host===location.host){var t=document.body.firstElementChild||document.body;t.scrollIntoView({block:"start"});}}catch(e){}})();</script><!--/nav-->')
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
