"""Links named treatments, once each, at their first mention from the "What works" section on.
Every URL below was opened and checked on Nov 1, 2026 (official program sites or professional-society pages)."""
import re

U = {
    'CBT': 'https://www.apa.org/ptsd-guideline/treatments/cognitive-behavioral-therapy',
    'CPT': 'https://www.apa.org/ptsd-guideline/treatments/cognitive-processing-therapy',
    'PE': 'https://www.apa.org/ptsd-guideline/treatments/prolonged-exposure',
    'CT_PTSD': 'https://www.apa.org/ptsd-guideline/treatments/cognitive-therapy',
    'EMDR': 'https://www.apa.org/ptsd-guideline/treatments/eye-movement-reprocessing',
    'ERP': 'https://societyofclinicalpsychology.org/psychological-treatments/exposure-and-response-prevention-for-obsessive-compulsive-disorder/',
    'CM': 'https://societyofclinicalpsychology.org/psychological-treatments/contingency-management-for-substance-use-disorder/',
    'CBT_SUD': 'https://societyofclinicalpsychology.org/psychological-treatments/cognitive-behavioral-therapy-for-substance-use-disorders/',
    'IPT': 'https://interpersonalpsychotherapy.org/ipt-basics/overview-of-ipt/',
    'MBCT': 'https://www.mbct.com/about-mbct/',
    'SCHEMA': 'https://schematherapysociety.org/Schema-Therapy',
    'DBT': 'https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/',
    'MI': 'https://motivationalinterviewing.org/',
    'CBTE': 'https://www.cbte.co/',
    'PGT': 'https://prolongedgrief.columbia.edu/',
    'RAISE': 'https://www.nimh.nih.gov/research/research-funded-by-nimh/research-initiatives/recovery-after-an-initial-schizophrenia-episode-raise',
    'IPS': 'https://ipsworks.org/index.php/what-is-ips/',
    'IPSRT': 'https://www.ipsrt.org/',
    'ACT': 'https://contextualscience.org/act',
    'BPT_ADHD': 'https://www.cdc.gov/adhd/treatment/behavior-therapy.html',
    'BPT_DBD': 'https://effectivechildtherapy.org/concerns-symptoms-disorders/disorders/rule-breaking-defiance-and-acting-out/',
    'FEELSAFE': 'https://www.psy.ox.ac.uk/research/oxford-cognitive-approaches-to-psychosis/projects-1/the-feeling-safe-programme',
    'FBT': 'https://train2treat4ed.com/about',
    'ABC': 'https://www.cebc4cw.org/program/attachment-and-biobehavioral-catch-up/',
    'MOUD': 'https://www.fda.gov/drugs/information-drug-class/information-about-medications-opioid-use-disorder-moud',
    'AA': 'https://www.aa.org/',
    'PCIT': 'https://www.pcit.org/about',
    'TRIPLEP': 'https://triplep.net/glo-en/find-out-about-triple-p',
    'IY': 'https://www.incredibleyears.com/early-intervention-programs/parents',
    'MST': 'https://www.mstservices.com/what-is-mst',
}

LINK = re.compile(r'\[[^\]]+\]\([^)]+\)')
BOLD = re.compile(r'\*\*.+?\*\*')


def _link_in(text, phrase, url):
    """Return text with the first plain or bold occurrence of phrase linked, or None."""
    blocked = [m.span() for m in LINK.finditer(text)]
    bolds = [m.span() for m in BOLD.finditer(text)]
    start = 0
    while True:
        i = text.find(phrase, start)
        if i < 0:
            return None
        j = i + len(phrase)
        start = j
        if (i and (text[i - 1].isalnum() or text[i - 1] == '-')) or (j < len(text) and (text[j].isalnum() or text[j] == '-')):
            continue
        if any(a <= i < b for a, b in blocked):
            continue
        b = next(((a, z) for a, z in bolds if a <= i and j <= z), None)
        if b is None:
            if any(a < j and i < z for a, z in bolds):
                continue  # straddles a bold boundary
            return text[:i] + f'[{phrase}]({url})' + text[j:]
        a, z = b
        inner_pre, inner_post = text[a + 2:i], text[j:z - 2]
        out = text[:a]
        if inner_pre:
            out += f'**{inner_pre}**'
        out += f'[**{phrase}**]({url})'
        if inner_post:
            out += f'**{inner_post}**'
        return out + text[z:]


def link_treatments(body, pairs):
    start = next(n for n, (k, t) in enumerate(body) if k == 'H' and 'What works' in t)
    missing = []
    for phrase, key in pairs:
        for n in range(start, len(body)):
            k, t = body[n]
            if k not in ('P', 'B', 'B2', 'N', 'NI'):
                continue
            new = _link_in(t, phrase, U[key])
            if new:
                body[n] = (k, new)
                break
        else:
            missing.append(phrase)
    if missing:
        raise SystemExit(f'treatment link phrase not found: {missing}')
    return body
