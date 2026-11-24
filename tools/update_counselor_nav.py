"""Writes the Counselors' Room menu into every counselors/*.html page that has a <!--nav-->...<!--/nav--> block.

Edit MENU below, then run:  python3 tools/update_counselor_nav.py
"""
import glob, os, re

# The menu matches the Counselors' Room (members/, built by tools/build_members_room.py).
M = "../members/"
MENU = [("index.html", "Welcome"), ("belief-counseling.html", "Belief Counseling"), ("process.html", "The Process"),
        ("assessment.html", "Assessment"), ("disorders.html", "Disorders"),
        ("tips.html", "Professional Tips"), ("library.html", "Library")]
# Which menu item is underlined on each kept page
SECTION = {"core-beliefs.html": "process.html", "reviews.html": "assessment.html",
           "tips.html": "tips.html", "tips-ethics.html": "tips.html", "tip-ethics-treatment-modalities.html": "tips.html",
           "cases.html": "tips.html", "theory.html": "tips.html",
           "books.html": "library.html", "videos.html": "library.html", "articles.html": "library.html"}


# Lie Finder: stands out as a cream button with a gold ring (gold text marks the current page).
LIE_FINDER = '<a class="lf" target="_top" href="https://www.beliefcounselor.com/false-belief-finder" style="display:inline-flex;align-items:center;gap:6px;background:#faf6ec;color:#12284c;font-weight:bold;border:0;text-decoration:none;border-radius:20px;padding:4px 14px;box-shadow:0 0 0 2px #c9a227 inset"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>Lie Finder</a>'


def nav(page):
    h = ['<!--nav--><div class="nav"><div class="brand">Belief Counseling<small>Counselors’ Room</small></div>']
    for f, label in MENU:
        h.append(f'<a class="l{" on" if SECTION.get(page) == f else ""}" href="{M}{f}">{label}</a>')
        if f == "index.html":
            h.append(LIE_FINDER)
    h.append(f'<a class="l" href="../counselors/membership.html">Membership</a>')
    h.append('<span class="acct"><a class="l" target="_top" href="https://www.beliefcounselor.com/my-subscriptions">My Subscriptions</a>'
             '<a class="l" target="_top" href="https://www.beliefcounselor.com/account-settings">My Account</a></span>'
             '<a class="pub" target="_blank" rel="noopener" href="https://www.beliefcounselor.com">Public Site ↗</a>'
             '<a class="needhelp" target="_top" href="https://www.beliefcounselor.com/help">Need Help?</a></div>'
             '<script>/* When moving between pages inside the Wix page, show the new page from its top. */(function(){try{if(window.top!==window&&document.referrer&&new URL(document.referrer).host===location.host){var t=document.body.firstElementChild||document.body;t.scrollIntoView({block:"start"});}}catch(e){}})();</script>'
             '<script>/* Inside the Wix Counselors’ Room, ask the Wix page to open these menu links. The address still works if this file is opened on its own. */(function(){if(!window.parent||window.parent===window)return;var root=document.querySelector(".nav");if(!root)return;root.addEventListener("click",function(e){if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;var a=e.target&&e.target.closest?e.target.closest("a"):null;if(!a||!root.contains(a))return;var href=a.getAttribute("href")||"";if(href.indexOf("https://www.beliefcounselor.com")!==0)return;var u;try{u=new URL(href);}catch(err){return;}e.preventDefault();window.parent.postMessage({type:"navigate",path:(u.pathname||"/")+u.search+u.hash},"*");});})();</script><!--/nav-->')
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
