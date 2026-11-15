"""Shared markup for Email this card / Email this page. Run to add it to existing pages:

    python3 tools/email_share.py
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JS = ROOT / "site" / "email-share.js"
ICON = ('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" '
        'aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="1.5" '
        'fill="none" stroke="currentColor" stroke-width="1.7"/>'
        '<path d="M4 7l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>')


def rel_script(directory):
    rel = os.path.relpath(JS, directory)
    return rel.replace("\\", "/")


def card_html(src):
    return ('<p class="emailshare noprint"><a class="emailshare-btn" data-email="card" href="mailto:" '
            'aria-label="Email this false-belief card to someone">%s Email this card</a></p>\n'
            '<script src="%s"></script>\n' % (ICON, src))


def page_html(src):
    return ('<p class="emailshare noprint"><a class="emailshare-btn" data-email="page" href="mailto:" '
            'aria-label="Email this page to a friend">%s Email this page to a friend</a></p>\n'
            '<script src="%s"></script>\n' % (ICON, src))


def insert_card(text, src):
    if 'data-email="card"' in text:
        return text
    block = card_html(src)
    marker = "function printPages"
    i = text.find(marker)
    if i != -1:
        j = text.find("</script>", i)
        if j != -1:
            j += len("</script>")
            return text[:j] + "\n" + block + text[j:]
    m = text.find("<body")
    if m == -1:
        return text
    end = text.find(">", m)
    return text[:end + 1] + "\n" + block + text[end + 1:]


def insert_page(text, src):
    if 'data-email="page"' in text:
        return text
    block = page_html(src)
    foot = text.find('<div class="foot">')
    if foot == -1:
        foot = text.find("<footer")
    if foot != -1:
        return text[:foot] + block + text[foot:]
    end = text.rfind("</body>")
    if end == -1:
        return text + block
    return text[:end] + block + text[end:]


def apply_file(path, kind):
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    src = rel_script(path.parent)
    new = insert_card(text, src) if kind == "card" else insert_page(text, src)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    n = 0
    for p in (ROOT / "belief-cards").rglob("*.html"):
        if apply_file(p, "card"):
            n += 1
    print("cards", n)


if __name__ == "__main__":
    main()
