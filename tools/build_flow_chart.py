"""Builds the printable Flow of Care chart: counselors/forms/Clinical-Companion-Flow-of-Care.pdf

    python3 tools/build_flow_chart.py        (needs: pip install cairosvg)

The chart starts at step 1, Telephone Intake (Brian, Nov 12, 2026: no Foundations boxes).
Edit STEPS below and run again. A step is (title, subtitle, bullets, built_by_ai).
"""
import pathlib
from xml.sax.saxutils import escape

import cairosvg

OUT = pathlib.Path(__file__).resolve().parent.parent / "counselors" / "forms" / "Clinical-Companion-Flow-of-Care.pdf"
DATE = "November 12, 2026"
STEPS = [
    ("1. Telephone Intake", "First contact with the client", ["Ask: online or paper forms?"], False),
    ("2. Online (or Paper) Intake", "The client completes the forms before the first visit",
     ["About You and Brief History", "Agreements and consent forms, signed on screen"], False),
    ("3. Schedule First Visit", "Set the first appointment", [], False),
    ("4. Assessment Report Begins", "AI starts the report from the intake information", [], True),
    ("5. Review Intake Information", "Before the first interview",
     ["Initial hypothesis about diagnosis", "Initial hypothesis about toxic beliefs"], False),
    ("6. Initial Interview", "Belief mining begins",
     ["Functional analysis of presenting problem (counselor-led)", "Consider safety issues",
      "Review Mining levels form and Adult History"], False),
    ("7. Develop Hypotheses", "Diagnosis and possible false beliefs", [], False),
    ("8. Counselor Enters First Case Note", "AI adds the Interview Findings",
     ["Functional analysis findings dictated into the note",
      "AI suggests DSM-5-TR and belief questions for next session", "Steps 6-8 repeat after each session"], True),
    ("9. Follow-up Tests or Assessments", "Level checklists, diagnostic forms",
     ["Check off forms on the “Forms to Complete” card", "Short screens: PHQ-9 (depression), GAD-7 (anxiety)",
      "Optional spiritual screens (if faith is included):", "    – RSS-5, routinely (about 2 minutes)",
      "    – Brief RCOPE, when a specific stressor is central",
      "    – SAI, for in-depth work (author permission needed)",
      "    – Christian Experiences and Beliefs (counselor-guided)"], False),
    ("10. Diagnosis + Identify", "DSM-5-TR and false beliefs",
     ["Refresher: the DSM-5-TR diagnostic process"], False),
    ("11. Treatment Plan", "Built from the diagnosis and false beliefs", [], False),
    ("12. Challenge", "Secular and Christian techniques", [], False),
    ("13. Replace", "False beliefs replaced with the truth", [], False),
    ("14. Belief Cards", "Public belief cards used as homework", [], False),
]
W, X, BW = 510, 112, 286
GREEN = ("#e1f3ea", "#1f6b52", "#0f5340")
PURPLE = ("#eceafb", "#5b4fc0", "#3f3690")
FONT = "Liberation Sans, Arial, Helvetica, sans-serif"


def main():
    y, parts = 96, []
    for i, (title, sub, bullets, ai) in enumerate(STEPS):
        fill, stroke, ink = PURPLE if ai else GREEN
        h = 44 + (8 + 15 * len(bullets) if bullets else 0)
        parts.append('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="%s" stroke="%s" stroke-width="1"/>'
                     % (X, y, BW, h, fill, stroke))
        parts.append('<text x="%d" y="%d" text-anchor="middle" font-size="11.5" font-weight="bold" fill="%s">%s</text>'
                     % (W / 2, y + 18, ink, escape(title)))
        parts.append('<text x="%d" y="%d" text-anchor="middle" font-size="9" fill="%s">%s</text>'
                     % (W / 2, y + 33, ink, escape(sub)))
        for k, b in enumerate(bullets):
            indent = len(b) - len(b.lstrip())
            text = b.strip() if indent else "• " + b
            parts.append('<text x="%d" y="%d" font-size="9" fill="#1f2a3a">%s</text>'
                         % (X + 20 + indent * 3, y + 52 + 15 * k, escape(text)))
        y += h
        if i < len(STEPS) - 1:
            parts.append('<path d="M%d %d V%d M%d %d l4 -6 M%d %d l-4 -6" stroke="#444" stroke-width="1" fill="none"/>'
                         % (W / 2, y + 2, y + 18, W / 2, y + 18, W / 2, y + 18))
            y += 21
    y += 26
    for lx, color, label in ((150, GREEN[1], "With the client"), (290, PURPLE[1], "Built by the AI")):
        parts.append('<rect x="%d" y="%d" width="9" height="9" rx="2" fill="%s"/>' % (lx, y - 8, color))
        parts.append('<text x="%d" y="%d" font-size="8.5" fill="#444">%s</text>' % (lx + 14, y, label))
    y += 22
    parts.append('<text x="%d" y="%d" text-anchor="middle" font-size="7.5" fill="#5b6678">Working draft · %s · '
                 '© 2026 Brian Campbell, Ph.D. All rights reserved.</text>' % (W / 2, y, DATE))
    H = y + 24
    head = ('<text x="%d" y="44" text-anchor="middle" font-size="17" font-weight="bold" fill="#12284c">'
            'The Clinical Companion: Flow of Care</text><text x="%d" y="64" text-anchor="middle" font-size="10" '
            'fill="#444">Belief Counseling · Counselors’ Room</text>' % (W / 2, W / 2))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="%s">'
           '<rect width="100%%" height="100%%" fill="#fff"/>%s%s</svg>' % (W, H, W, H, FONT, head, "".join(parts)))
    cairosvg.svg2pdf(bytestring=svg.encode("utf-8"), write_to=str(OUT))
    print("wrote", OUT, "height", H)


if __name__ == "__main__":
    main()
