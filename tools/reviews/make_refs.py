"""Turn verified Crossref/PubMed metadata (meta.json in a review folder) into APA references (refs.py).

meta.json maps DOI -> {"a": ["Family|Given", ...] or "#Group name", "y": year, "t": title,
                       "j": journal, "v": volume, "i": issue, "p": pages}
Optional overrides.json maps DOI -> {"t": "exact title", "j": ..., "v": ..., "i": ..., "p": ...}
Run:  python3 tools/reviews/make_refs.py tools/reviews/<topic>
"""
import json, re, sys, pathlib

KEEP = {"WHO", "World", "Mental", "Health", "Survey", "Surveys", "Initiative", "U.S.", "US", "American",
        "Christian", "Christians", "God", "Bible", "Biblical", "Scripture", "Veterans", "Veteran",
        "Building", "Spiritual", "Strength", "Mood", "Disorder", "Questionnaire", "Primary", "Care",
        "Screen", "Checklist", "Systematic", "Treatment", "Enhancement", "Program", "Alcoholics",
        "Anonymous", "Twelve", "Step", "Islamic", "Muslim", "Muslims", "Catholic", "Protestant",
        "English", "Europe", "European", "Canadian", "Australian", "National", "Comorbidity",
        "Replication", "Prolonged", "Grief", "Inventory", "Scale", "Network", "Anxiety",
        "Treatments", "Bipolar", "Disorders", "International", "Society", "Canada", "Ghana",
        "Nigeria", "India", "Pakistan", "Iran", "Malaysia", "Brazil", "Spain", "Sweden", "Swedish",
        "Danish", "Denmark", "Norway", "Norwegian", "Finland", "Finnish", "Dutch", "German",
        "Germany", "Japan", "Japanese", "Chinese", "China", "Korea", "Korean", "Israel", "Jewish",
        "Africa", "African", "Latino", "Hispanic", "Black", "Asian"}
PROPER_PHRASES = ["Primary Care PTSD Screen", "Posttraumatic Stress Disorder Checklist",
                  "Mood Disorder Questionnaire", "World Mental Health", "Building Spiritual Strength",
                  "Spiritually Integrated Cognitive Processing Therapy", "Alcoholics Anonymous",
                  "Prolonged Grief Disorder", "Inventory of Complicated Grief", "National Comorbidity Survey"]


def sentence_case(t):
    t = t.strip().rstrip(".")
    protected = {}
    for i, ph in enumerate(PROPER_PHRASES):
        if ph in t:
            key = f"\x00{i}\x00"; protected[key] = ph; t = t.replace(ph, key)
    out, start = [], True
    for w in re.split(r"(\s+)", t):
        if not w.strip():
            out.append(w); continue
        core = re.sub(r"^[\"'(\[]+|[\"'),.;:\]?!]+$", "", w)
        keep = (core in KEEP or any(c.isupper() for c in core[1:]) or any(c.isdigit() for c in core)
                or "\x00" in core or len(core) <= 1 and core.isupper() and not start)
        if start:
            w2 = w[:1].upper() + w[1:] if not keep else w
            # capitalize first letter after an opening quote/paren
            w2 = re.sub(r"^([\"'(\[]*)([a-z])", lambda m: m.group(1) + m.group(2).upper(), w2)
        elif keep:
            w2 = w
        else:
            w2 = w.lower()
        out.append(w2)
        start = bool(re.search(r"[:?!]$", w))
    s = "".join(out)
    for k, v in protected.items():
        s = s.replace(k, v)
    return s


def initials(given):
    parts = []
    for chunk in given.replace(".", ". ").split():
        if "-" in chunk:
            parts.append("-".join(p[0] + "." for p in chunk.split("-") if p))
        elif chunk.endswith(".") and len(chunk) <= 3:
            parts.append(chunk[0] + ".")
        elif chunk[0].isalpha():
            parts.append(chunk[0].upper() + "." if chunk[0].isupper() else None)
    return " ".join(p for p in parts if p)


def name(a):
    if a.startswith("#"):
        return a[1:]
    fam, giv = a.split("|", 1)
    fam = fam.replace("‐", "-")
    particle = ""
    for p in ("de ", "van ", "von ", "ten ", "Ten "):
        if giv.endswith(" " + p.strip()) or giv.endswith(" " + p.strip().lower()):
            particle = p.strip().lower() + " "; giv = giv[: -len(p.strip()) - 1]
    if fam.startswith("Ten "):
        fam = "ten " + fam[4:]
    ini = initials(giv)
    return f"{particle}{fam}, {ini}" if ini else f"{particle}{fam}"


def authors(lst):
    ns = [name(a) for a in lst]
    if len(ns) == 1:
        return ns[0] if ns[0].endswith(".") else ns[0] + "."
    if len(ns) <= 20:
        s = ", ".join(ns[:-1]) + ", & " + ns[-1]
    else:
        s = ", ".join(ns[:19]) + ", . . . " + ns[-1]
    return s


def pages(p):
    if not p:
        return p
    m = re.match(r"^(\d+)-(\d+)$", p)
    if m:
        a, b = m.groups()
        if len(b) < len(a):
            b = a[: len(a) - len(b)] + b
        return f"{a}–{b}"
    return p.replace("-", "–") if re.match(r"^\d+-\d+$", p) else p


def main(folder):
    f = pathlib.Path(folder)
    meta = json.loads((f / "meta.json").read_text())
    ov = json.loads((f / "overrides.json").read_text()) if (f / "overrides.json").exists() else {}
    refs = []
    for doi, m in meta.items():
        m = {**m, **ov.get(doi, {})}
        if m.get("book"):
            refs.append((m["a"][0].lstrip("#"), authors(m["a"]), str(m["y"]), m["t"], None, None, None, None, doi))
            continue
        t = m["t"] if doi in ov and "t" in ov[doi] else sentence_case(m["t"])
        j = m["j"].replace("&amp;", "and").replace(" & ", " and ")
        refs.append((m["a"][0].split("|")[0].lstrip("#"), authors(m["a"]), str(m["y"]), t, j,
                     m.get("v"), m.get("i"), pages(m.get("p")), doi))
    refs.sort(key=lambda r: (r[0].lower().replace("de ", ""), r[2], r[3]))
    with open(f / "refs.py", "w") as o:
        o.write("REFS = [\n")
        for r in refs:
            o.write("    " + repr(r) + ",\n")
        o.write("]\n")
    for r in refs:
        print(f"{r[1]} ({r[2]}). {r[3]}. {r[4]}, {r[5]}({r[6]}), {r[7]}. https://doi.org/{r[8]}")


if __name__ == "__main__":
    main(sys.argv[1])
