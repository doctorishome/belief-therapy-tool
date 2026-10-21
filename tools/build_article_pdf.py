"""Builds a framed article PDF (navy-and-gold frame matching the Belief Cards and Godly Counsel lessons).

Usage: python3 tools/build_article_pdf.py belief-cards/articles/<Name>.html
Output: belief-cards/articles/<Name>.pdf next to the page (letter size)
The .html is also the phone-friendly web page; this script prints it and adds the frame and page numbers.
"""
import io, os, sys, pathlib
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

TOOLS = os.path.dirname(os.path.abspath(__file__))
NAVY, GOLD = HexColor("#1F3A5F"), HexColor("#B08A4B")
W, H = 612, 792
pdfmetrics.registerFont(TTFont("Serif", os.path.join(TOOLS, "gc_fonts", "SourceSerif4-Regular.ttf")))

src = pathlib.Path(sys.argv[1]).resolve()
out = src.with_suffix(".pdf")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto(src.as_uri()); pg.wait_for_timeout(800)
    body = pg.pdf(format="Letter", print_background=True, prefer_css_page_size=True)
    b.close()

reader = PdfReader(io.BytesIO(body)); writer = PdfWriter(); n = len(reader.pages)
for i, page in enumerate(reader.pages, 1):
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(W, H))
    c.setStrokeColor(NAVY); c.setLineWidth(2.2); c.rect(22, 22, W - 44, H - 44)
    c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.rect(28, 28, W - 56, H - 56)
    c.setFillColor(GOLD); c.setFont("Serif", 8)
    c.drawCentredString(W / 2, 38, "%d of %d" % (i, n))
    c.save()
    page.merge_page(PdfReader(io.BytesIO(buf.getvalue())).pages[0])
    writer.add_page(page)
writer.add_metadata({"/Title": src.stem.replace("-", " "), "/Author": "Dr. Brian Campbell"})
with open(out, "wb") as f:
    writer.write(f)
print(out, n, "pages")
