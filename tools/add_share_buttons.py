"""Add the "Share this information" email button to every belief card page.

Run after building or rebuilding cards:
    python3 tools/add_share_buttons.py            (all cards)
    python3 tools/add_share_buttons.py --list     (print short path -> card URL, for Wix redirects)

The button is a plain mailto link written straight into the page (no script), so the
visitor's own email program opens with the lie, the truth, the key verse, a short
beliefcounselor.com link back to the card, and a link to The Process page.

Each short link (for example https://www.beliefcounselor.com/card/psych-61) works like this:
one Wix group redirect sends every beliefcounselor.com/card/... address to the same name
under this repository's card/ folder, and this script writes a small forwarding page there
(card/psych-61.html) that opens the real card. New cards need nothing in Wix: just run this
script and push.

Safe to run again: it replaces the block it added before.
"""
import html
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "belief-cards"
SITE = "https://www.beliefcounselor.com"
PAGES = "https://doctorishome.github.io/belief-therapy-tool/"
PROCESS = SITE + "/the-process"
DISCLAIMER = "This educational resource is not a diagnosis or a substitute for professional care."
SUBJECT = "Belief Counseling information you may find helpful"
MARK = "<!-- ============ CARD ============ -->"
OLD_MARK = '<div class="card belief">'  # older Psychological cards (1-30) have no CARD comment
START = "<!-- share-button:start -->"
END = "<!-- share-button:end -->"
MAX_HREF = 1900

PREFIX = {
    "Belief": "spiritual",
    "Psych": "psych",
    "Bio": "bio",
    "Core": "core",
    "Inter": "inter",
    "Marriage": "marriage",
    "Socio": "socio",
    "Cult": "culture",
}
NAME = re.compile(r"^(%s)-(\d+)-.*\.html$" % "|".join(PREFIX))

STYLE = (
    "<style>.emailshare{margin:10px 0 14px;font:14px/1.3 Arial,Helvetica,sans-serif}"
    ".emailshare-btn{display:inline-flex;align-items:center;gap:6px;color:#1e3556;text-decoration:none;"
    "border:1px solid #c4b48a;background:#fffdf8;border-radius:999px;padding:5px 12px}"
    ".emailshare-btn:hover{border-color:#a8864f;color:#a8864f}.emailshare-btn svg{display:block}"
    "@media print{.emailshare{display:none !important}}</style>"
)
ICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" '
    'focusable="false"><rect x="3" y="5" width="18" height="14" rx="1.5" fill="none" stroke="currentColor" '
    'stroke-width="1.7"/><path d="M4 7l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>'
)


def plain(fragment):
    text = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def first(pattern, text):
    m = re.search(pattern, text, re.S)
    return plain(m.group(1)) if m else ""


def card_files():
    for path in sorted(CARDS.rglob("*.html")):
        m = NAME.match(path.name)
        if m and "Homework" not in path.name:
            yield path, PREFIX[m.group(1)] + "-" + str(int(m.group(2)))


def build_body(lie, truth, verse, link):
    body = "I pray that this Belief Counseling information might be helpful:"
    body += '\n\nThe lie: "' + lie + '"'
    if truth:
        body += "\n\nThe truth: " + truth
    if verse:
        body += "\n\nScripture: " + verse
    body += "\n\nRead more here:\n" + link
    body += "\n\nFor a general overview of Belief Counseling, see:\n" + PROCESS
    body += "\n\n" + DISCLAIMER
    return body


def mailto(body):
    return "mailto:?subject=" + quote(SUBJECT, safe="") + "&body=" + quote(body, safe="")


def share_block(page, short):
    anchor = MARK if MARK in page else OLD_MARK
    card = page.split(anchor, 1)[1] if anchor in page else page
    lie = first(r"<h1[^>]*>(.*?)</h1>", card).strip("“”\"' ")
    truth = first(r'<p class="truth">(.*?)</p>', card)
    keybox = re.search(r'<div class="key">(.*?)</div>', card, re.S)
    keybox = keybox.group(1) if keybox else ""
    ref = first(r'<span class="ref">(.*?)</span>', keybox)
    words = plain(re.sub(r'<span class="ref">.*?</span>', "", keybox, flags=re.S))
    words = words.strip(" .").strip("\u201c\u201d\" ").rstrip(".")
    verse = ("“" + words + "”" + (" " + ref if ref else "")) if words else ""
    link = SITE + "/card/" + short
    href = mailto(build_body(lie, truth, verse, link))
    if len(href) > MAX_HREF:
        href = mailto(build_body(lie, truth, "", link))
    if not lie:
        raise ValueError("no belief heading found")
    return (
        START + STYLE
        + '<p class="emailshare noprint"><a class="emailshare-btn" target="_top" href="'
        + html.escape(href, quote=True)
        + '" aria-label="Share this information by email">' + ICON + " Share this information</a></p>"
        + END + "\n"
    )


STUB = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Belief Counseling card</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={url}">
<link rel="canonical" href="{url}">
<script>location.replace("{url}");</script>
</head><body><p>Opening the card&hellip; If it does not open, <a href="{url}">click here</a>.</p></body></html>
"""


def write_stub(short, path):
    url = PAGES + path.relative_to(ROOT).as_posix()
    out = ROOT / "card" / (short + ".html")
    out.parent.mkdir(exist_ok=True)
    out.write_text(STUB.format(url=url), encoding="utf-8")
    # Folder copy too, so the address works with or without ".html" on every web host.
    folder = ROOT / "card" / short
    folder.mkdir(exist_ok=True)
    (folder / "index.html").write_text(STUB.format(url=url), encoding="utf-8")


def strip_old(page):
    page = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", page, flags=re.S)
    page = re.sub(r'<p class="emailshare noprint">.*?</p>\n?', "", page, flags=re.S)
    page = re.sub(r'<script src="[^"]*site/email-share\.js[^"]*"></script>\n?', "", page)
    return page


def main():
    if "--list" in sys.argv:
        for path, short in card_files():
            print("/card/" + short + "\t" + PAGES + path.relative_to(ROOT).as_posix())
        return
    done = 0
    for path, short in card_files():
        page = strip_old(path.read_text(encoding="utf-8"))
        anchor = MARK if MARK in page else OLD_MARK
        if anchor not in page:
            print("skipped (no card marker):", path)
            continue
        page = page.replace(anchor, share_block(page, short) + anchor, 1)
        path.write_text(page, encoding="utf-8")
        write_stub(short, path)
        done += 1
    print("share button written to", done, "cards")


if __name__ == "__main__":
    main()
