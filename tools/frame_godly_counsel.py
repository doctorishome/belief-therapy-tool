"""Puts each Godly Counsel chapter PDF into a navy-and-gold frame that matches the Belief Cards.

Usage: python3 tools/frame_godly_counsel.py <folder with the 33 chapter PDFs> [chapter numbers...]
       (no chapter numbers = all 33)
Output: belief-cards/godly-counsel/GC-NN-<Title>.pdf  (letter size, prints well at home)
"""
import io, json, os, re, sys
from pypdf import PdfReader, PdfWriter, PageObject, Transformation
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

TOOLS = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(TOOLS, "..", "belief-cards", "godly-counsel")
NAVY, GOLD, LINE = HexColor("#1F3A5F"), HexColor("#B08A4B"), HexColor("#E4D9C6")
W, H = 612, 792  # US letter
TRIM_TOP, TRIM_SIDE, TRIM_BOTTOM = 26, 40, 40  # blank book margin to trim, in points

F = os.path.join(TOOLS, "gc_fonts")
pdfmetrics.registerFont(TTFont("Corm", os.path.join(F, "Cormorant-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Serif", os.path.join(F, "SourceSerif4-Regular.ttf")))
pdfmetrics.registerFont(TTFont("SerifI", os.path.join(F, "SourceSerif4-Italic.ttf")))


def slug(title):
    return re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-")


def frame(num, title, page_no, pages):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    # outer navy border and inner gold rule
    c.setStrokeColor(NAVY); c.setLineWidth(2.2); c.rect(22, 22, W - 44, H - 44)
    c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.rect(28, 28, W - 56, H - 56)
    # header
    c.setFillColor(GOLD); c.setFont("Serif", 8.5)
    c.drawCentredString(W / 2, H - 52, "G O D L Y   C O U N S E L")
    if page_no > 1:  # page 1 already shows the book's own "Lesson NN / TITLE"
        c.setFillColor(NAVY); c.setFont("Corm", 19)
        c.drawCentredString(W / 2, H - 74, "Lesson %d · %s" % (num, title))
        c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.line(W / 2 - 60, H - 84, W / 2 + 60, H - 84)
    # footer
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(60, 58, W - 60, 58)
    c.setFillColor(NAVY); c.setFont("SerifI", 8.5)
    c.drawString(60, 44, "From Godly Counsel by Dr. Brian Campbell")
    c.setFont("Serif", 8.5)
    c.drawRightString(W - 60, 44, "Page %d of %d" % (page_no, pages))
    c.save()
    return PdfReader(io.BytesIO(buf.getvalue())).pages[0]


def build(src_dir, num, chapters):
    title = chapters[str(num)][0]
    src = [f for f in os.listdir(src_dir) if f.startswith("%02d - " % num) and f.endswith(".pdf")][0]
    reader = PdfReader(os.path.join(src_dir, src))
    out = PdfWriter()
    n = len(reader.pages)
    for i, p in enumerate(reader.pages, 1):
        # trim the book's own blank margins (same amount on every page, so pages line up)
        x0, y0 = float(p.mediabox.left) + TRIM_SIDE, float(p.mediabox.bottom) + TRIM_BOTTOM
        pw = float(p.mediabox.width) - 2 * TRIM_SIDE
        ph = float(p.mediabox.height) - TRIM_TOP - TRIM_BOTTOM
        box_top = H - 94 if i > 1 else H - 62     # page 1 has no lesson heading, so text starts higher
        box_bottom = 66
        s = min((W - 120) / pw, (box_top - box_bottom) / ph, 1.1)
        x = (W - pw * s) / 2
        y = box_top - ph * s                       # text starts just under the heading
        p.cropbox.lower_left = (x0, y0)
        p.cropbox.upper_right = (x0 + pw, y0 + ph)
        page = PageObject.create_blank_page(width=W, height=H)
        page.merge_transformed_page(p, Transformation().translate(-x0, -y0).scale(s).translate(x, y))
        page.merge_page(frame(num, title, i, n))
        out.add_page(page)
    out.add_metadata({"/Title": "Godly Counsel – Lesson %d: %s" % (num, title), "/Author": "Dr. Brian Campbell"})
    os.makedirs(OUT, exist_ok=True)
    name = "GC-%02d-%s.pdf" % (num, slug(title))
    with open(os.path.join(OUT, name), "wb") as fh:
        out.write(fh)
    print("framed", name, n, "pages")


if __name__ == "__main__":
    chapters = json.load(open(os.path.join(TOOLS, "godly-counsel-chapters.json"), encoding="utf-8"))
    nums = [int(a) for a in sys.argv[2:]] or list(range(1, 34))
    for k in nums:
        build(sys.argv[1], k, chapters)
