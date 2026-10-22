"""Adds a "Recommended Books" box to belief cards, from books/recommended-books.md.

Run:  python3 tools/add_book_boxes.py
- Each card listed for a book (by card number, e.g. SPR-106) gets one box listing all its books.
- The box sits just before "Related Pearls topics" (after the Truth summary and any "Read more" box).
- A book whose "Amazon link" line holds a web address gets a "View on Amazon" button, and the box then
  shows Amazon's required notice. Books still marked "(add later)" show without a button.
Safe to run again: boxes are replaced, not duplicated. Run it after editing the book list, and after
rebuilding any card.
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://doctorishome.github.io/belief-therapy-tool/"
DISCLOSURE = "As an Amazon Associate, I earn from qualifying purchases."


def read_books():
    text = (ROOT / "books/recommended-books.md").read_text(encoding="utf-8")
    books = []
    for part in re.split(r"^## ", text, flags=re.M)[1:]:
        title, _, rest = part.partition("\n")
        title = title.strip()
        fields = dict(re.findall(r"^- ([^:\n]+):[ \t]*(.*)$", rest, flags=re.M))
        if title in ("Title", "How to add a book") or title.startswith("Sample") or "Author" not in fields:
            continue
        link = fields.get("Amazon link", "").strip()
        books.append({
            "title": title,
            "author": fields.get("Author", "").strip(),
            "why": fields.get("Why I recommend it", "").strip(),
            "link": link if link.startswith("http") else "",
            "cards": re.findall(r"\b(?:SPR|BIO|PSY|INT|SEC|SCU|CORE)-[A-Z]?\d+\b", fields.get("Cards", "")),
        })
    return books


def box(books):
    items, any_link = [], False
    for b in books:
        btn = ""
        if b["link"]:
            any_link = True
            btn = ('<br><a href="%s" target="_blank" rel="noopener sponsored" style="display:inline-block;'
                   'margin-top:6px;padding:7px 14px;border-radius:6px;background:var(--navy,#1F3A5F);color:#fff;'
                   'font-weight:600;text-decoration:none;font-size:.9em">View on Amazon</a>' % html.escape(b["link"]))
        items.append('<li style="margin:0 0 10px"><b style="color:var(--navy,#1F3A5F)"><i>%s</i></b>, by %s'
                     '%s%s</li>' % (html.escape(b["title"]), html.escape(b["author"]),
                                    ('<br><span style="font-size:.92em">%s</span>' % html.escape(b["why"])) if b["why"] else "",
                                    btn))
    note = ('<p style="margin:4px 0 0;font-size:.78em;color:#777">%s</p>' % DISCLOSURE) if any_link else ""
    return ('<!--books-->'
            '<div class="book-box" style="border:1px solid var(--gold,#B08A4B);border-radius:8px;padding:14px 18px;'
            'margin:18px 0;background:#fff">'
            '<p style="margin:0 0 8px;color:var(--gold,#B08A4B);font-size:.8em;letter-spacing:.12em;'
            'text-transform:uppercase">Recommended Books</p>'
            '<ul style="list-style:none;margin:0;padding:0">%s</ul>%s</div><!--/books-->') % ("".join(items), note)


cards = {b["id"]: b["card"] for b in json.loads((ROOT / "lie-finder/master-list.json").read_text(encoding="utf-8"))["beliefs"]}
per_card = {}
for b in read_books():
    for cid in b["cards"]:
        if not cards.get(cid):
            print("No card page for", cid, "(%s)" % b["title"]); continue
        per_card.setdefault(cards[cid].replace(BASE, ""), []).append(b)

OLD = re.compile(r"<!--books-->.*?<!--/books-->\n*", re.S)
changed = 0
for page in sorted(set(per_card) | {str(p.relative_to(ROOT)) for p in (ROOT / "belief-cards").rglob("*.html")
                                    if "<!--books-->" in p.read_text(encoding="utf-8")}):
    path = ROOT / page
    t = path.read_text(encoding="utf-8")
    new = OLD.sub("", t)
    if page in per_card:
        i = new.find("<h2>Related Pearls topics</h2>")
        if i < 0:
            print("No 'Related Pearls topics' on", page); continue
        new = new[:i] + box(per_card[page]) + "\n\n" + new[i:]
    if new != t:
        path.write_text(new, encoding="utf-8"); changed += 1
print(len(per_card), "card(s) with books;", changed, "file(s) updated")
