"""Print the Socioeconomic Scarcity and Security HTML cards and their homework with local licensed fonts."""
from pathlib import Path
import re,logging,sys
from weasyprint import HTML
from weasyprint.urls import URLFetcher
from pypdf import PdfWriter
logging.getLogger('weasyprint').setLevel(logging.ERROR)
ROOT=Path(__file__).resolve().parents[1];SUB=sys.argv[1] if len(sys.argv)>1 else 'scarcity-security';TITLE=sys.argv[2] if len(sys.argv)>2 else 'Scarcity and Security';OUT=ROOT/('belief-cards/sociocultural/'+SUB);F=ROOT/'tools/gc_fonts'
css=f'''<style>@font-face{{font-family:"Source Serif 4";src:url("{(F/'SourceSerif4-Regular.ttf').as_uri()}")}}@font-face{{font-family:"Source Serif 4";font-style:italic;src:url("{(F/'SourceSerif4-Italic.ttf').as_uri()}")}}@font-face{{font-family:"Cormorant Garamond";font-weight:600 700;src:url("{(F/'Cormorant-SemiBold.ttf').as_uri()}")}}@page{{size:Letter;margin:0.5in;@bottom-center{{content:counter(page);font-size:9pt;color:#1F3A5F}}}} @media print{{h2,.step{{break-after:avoid}}p{{orphans:3;widows:3}}.bnote{{font-size:10px}}body{{font-size:12.5px;line-height:1.4}}h1{{font-size:28px}}h2{{font-size:16px;margin:12px 0 5px}}p{{margin-bottom:7px}}.step{{margin:12px 0 6px}}.step h2{{font-size:16px}}.opts li{{margin-bottom:5px}}table.track{{break-inside:auto}}table.track tr{{break-inside:avoid}}table.songj td{{height:34px}}.intro{{font-size:13px}}.song .sw{{font-size:11.5px}}.card{{background:white}}.opts .scrip{{font-size:12px}}.fill span{{font-size:12px}}.group{{font-size:10px}}.step .why{{font-size:12px}}.foot{{display:none}}.songj td{{height:30px}}.opts{{margin:4px 0 7px}}.opts li{{margin-bottom:3px}}.step{{margin:8px 0 4px}}.intro{{padding:8px 12px;font-size:12px}}.fill{{margin:5px 0}}.fill i{{height:18px}}.step .why{{font-size:11px}}.rate{{padding:8px 12px}}h1{{margin:6px 0;font-size:26px}}.num{{height:22px;flex-basis:22px;font-size:12px}}.orn{{margin-bottom:5px}}}}</style>'''
fetch=URLFetcher(allowed_protocols=['file','data'])
combined=PdfWriter()
for p in sorted(OUT.glob('Cult-*.html')):
 s=re.sub(r'<link[^>]+fonts.googleapis[^>]*>','',p.read_text());s=s.replace('</head>',css+'</head>')
 full=p.with_suffix('.pdf');HTML(string=s,base_url=p.as_uri(),url_fetcher=fetch).write_pdf(str(full));combined.append(full)
 hw=s.replace('<body>','<body class="hw-only">');hp=p.with_name(p.stem+'-Homework.pdf');HTML(string=hw,base_url=p.as_uri(),url_fetcher=fetch).write_pdf(str(hp))
 print(full.name,flush=True)
combined.write(OUT/(TITLE.replace(' and ','-').replace(' ','-')+'-All-Five-Cards-and-Homework.pdf'))
