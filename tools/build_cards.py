#!/usr/bin/env python3
"""Build Spiritual/Religious Belief Cards (HTML + PDF) from JSON data files.

Usage:  python3 tools/build_cards.py 6 7 8 9 10     (or no numbers = build all in tools/cards/)

Each card's content lives in tools/cards/NNN.json. Scripture text is NOT stored there:
only references. Verse text is pulled from tools/BSB.txt (Berean Standard Bible,
public domain) so every quotation is exact. To switch translations later, supply a
new text file in the same format and change TRANSLATION below.
"""
import html, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
OUT = os.path.join(ROOT, "belief-cards")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PEARLS = "https://doctorishome.wixstudio.com/website-6/scriptures?topic="
LIST_PAGE = "https://doctorishome.wixstudio.com/website-6/spiritual-religious-false-beliefs"
TRANSLATION_NOTE = ("Scripture quotations are from the Berean Standard Bible (BSB), "
                    "which is in the public domain.")

PEARLS_TOPICS = {}  # slug -> display name, loaded from tools/pearls-topics.json

BOOK_ALIAS = {"Psalm": "Psalms", "Song of Songs": "Song of Solomon", "Revelation": "Revelation of John"}


def load_bible():
    bible, book = {}, None
    for line in open(os.path.join(TOOLS, "BSB.txt"), encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("### "):
            book = line[4:].strip()
        else:
            m = re.match(r"\[(\d+):(\d+)\] (.*)", line)
            if m and book:
                bible[(book, int(m.group(1)), int(m.group(2)))] = m.group(3).strip()
    return bible


def book_key(name):
    m = re.match(r"^([123]) (.+)$", name)
    if m:
        return "I" * int(m.group(1)) + " " + m.group(2)
    return BOOK_ALIAS.get(name, name)


def verses(ref, bible):
    """'Romans 8:38–39' -> list of (key, text). Supports a,b lists: 'Psalm 34:4, 18'."""
    m = re.match(r"^(.+?) (\d+):(.+)$", ref)
    if not m:
        raise ValueError("Bad reference: " + ref)
    book, ch, rest = book_key(m.group(1)), int(m.group(2)), m.group(3)
    out = []
    for part in rest.split(","):
        part = part.strip()
        if "–" in part or "-" in part:
            a, b = re.split(r"[–-]", part)
            rng = range(int(a), int(b) + 1)
        else:
            rng = [int(part)]
        for v in rng:
            key = (book, ch, v)
            if key not in bible:
                raise KeyError("Verse not found: %s %d:%d (from %s)" % (book, ch, v, ref))
            out.append((key, bible[key]))
    return out


def scripture(ref, bible):
    """Verse text tidied for quoting: balanced inner quotes shown as single quotes,
    first letter capitalized, and a sentence-ending mark in place of a trailing comma/dash."""
    t = " ".join(t for _, t in verses(ref, bible)).strip()
    if "‘" in t and "“" in t:
        raise ValueError("Quote inside a quote in %s; choose a different verse range" % ref)
    depth, out = 0, []
    for ch in t:  # drop closing quotes with no opener (speech began in an earlier verse)
        if ch == "“":
            depth += 1
        elif ch == "”":
            if depth == 0:
                continue
            depth -= 1
        out.append(ch)
    t = "".join(out).rstrip() + "”" * depth  # close speech that continues past the quoted verses
    t = t.replace("“", "‘").replace("”", "’")
    t = re.sub(r"[,;:—–-]+([’]?)$", r".\1", t)
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    return t


def strip_end(t):
    return t[:-1] if t.endswith(".") else t


def e(s):
    return html.escape(s, quote=False)


def li(items):
    return "\n".join("<li>%s</li>" % x for x in items)


def pearls_link(slug):
    if slug not in PEARLS_TOPICS:
        raise KeyError("Unknown Pearls topic slug: " + slug)
    return '<a href="%s%s" target="_blank" rel="noopener">%s</a>' % (PEARLS, slug, PEARLS_TOPICS[slug])


def render(d, bible, style):
    n, belief = d["num"], d["belief"]
    lie = belief.rstrip(".")
    key_ref = d["key"]
    key_txt = scripture(key_ref, bible)
    also = [(r, scripture(r, bible)) for r in d["also"]]
    hw_refs = d.get("hw_scriptures") or [key_ref] + d["also"]
    hw = [(r, scripture(r, bible)) for r in hw_refs]

    also_html = "\n".join('<p><q>%s</q> <span class="ref">(%s)</span>.</p>' % (e(strip_end(t)), r) for r, t in also)
    errors_html = "\n".join("<li><strong>%s: </strong>%s</li>" % (a, b) for a, b in d["errors"])
    pearls_html = "\n".join("<li>%s</li>" % pearls_link(s) for s in d["pearls"])
    hw_scrip = "\n".join('<li><span class="ref">%s</span><span class="scrip">“%s”</span></li>' % (r, e(t)) for r, t in hw)
    actions = "\n".join("<li><strong>%s</strong> %s</li>" % (a, b) for a, b in d["actions"])
    log_t, log_d = d["log"]
    name_ref, name_html = d["name_example"]
    reading = d["reading"]
    listen = d.get("listening", "Depression")
    tracker = d["tracker"]
    file_base = "Belief-%03d-%s" % (n, d["file"])

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Belief Card: {e(lie[0].upper() + lie[1:])}</title>
<meta name="description" content="{html.escape(d['meta'])}"/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&amp;family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet"/>
<style>
{style}
  .bnote{{margin-top:14px;text-align:center;font-size:13px;color:#5a5348;font-style:italic}}
</style></head><body><div class="wrap" id="top">

<div class="printbar">
<p><strong>Print this card and homework</strong> to fill out with a pen. Choose what you’d like to print:</p>
<button type="button" onclick="printPages(false)">Print Card and Homework</button>
<button type="button" class="alt" onclick="printPages(true)">Print Homework Only</button>
</div>
<script>
function printPages(hwOnly){{
  document.body.classList.toggle('hw-only', hwOnly);
  window.print();
}}
window.addEventListener('afterprint', function(){{ document.body.classList.remove('hw-only'); }});
</script>

<!-- ============ CARD ============ -->
<div class="card belief">
<div class="tag">Spiritual/Religious False Belief #{n} · {e(d['group'])}</div>
<h1>“{e(belief)}”</h1>
<div class="orn">✦ ✦ ✦</div>

<h2>Where it often comes from</h2>
<p>{d['origins']}</p>

<h2>What Scripture teaches</h2>
<p>{d['teaches']}</p>
<div class="key"><q>{e(strip_end(key_txt))}</q> <span class="ref">({key_ref})</span>.</div>

<h2>Also see</h2>
<div class="also">
{also_html}
</div>

<h2>Common self-statements</h2>
<ul>
{li(d['self_statements'])}
</ul>

<h2>Common logical errors</h2>
<ul>
{errors_html}
</ul>

<h2>Challenging questions</h2>
<ul>
{li(d['questions'])}
</ul>

<h2>Truth summary</h2>
<p class="truth">{d['truth']}</p>

<h2>Related Pearls topics</h2>
<p>Click a topic to open it in the Pearls Scripture Search:</p>
<ul class="pearls">
{pearls_html}
</ul>

<p class="morning">Each morning ask: “If I truly believed God’s truth instead of this lie, how would I think, speak, and act today?”</p>
<div class="foot">✦ ✦ ✦</div>
</div>

<!-- ============ HOMEWORK, PAGE 1 ============ -->
<div class="card">
<div class="tag">Homework · Replace and Rehearse</div>
<h1>My Plan for Replacing<br/>“{e(lie)}”</h1>
<div class="orn">✦ ✦ ✦</div>
<p class="intro">Read through each section and <strong>check the one that fits you best</strong>. If none of them fit, write your own. One choice per section is enough. A truth you choose for yourself will stick better than one handed to you.</p>
<div class="fill"><span>Name:</span><i></i><span>Date started:</span><i></i></div>

<div class="step"><div class="num">1</div><div><h2>How strongly do I believe the lie?</h2><p class="why">Rate it now so you can see your progress later.</p></div></div>
<div class="rate"><span><b>“{e(belief)}”</b> I believe this <span class="box"></span> % <span style="font-size:14px;color:#5a5348">(0 = not at all, 100 = completely)</span></span></div>

<div class="step"><div class="num">2</div><div><h2>My best question</h2><p class="why">The one question I will ask myself every time the lie shows up.</p></div></div>
<ul class="opts">
{li(d['hw_questions'])}
</ul>
<div class="fill"><span>My own question:</span><i></i></div>

<div class="step"><div class="num">3</div><div><h2>My replacement truth</h2><p class="why">The statement I will say to myself instead of the lie.</p></div></div>
<ul class="opts">
{li(d['hw_truths'])}
</ul>
<div class="fill"><span>In my own words:</span><i></i></div>

<div class="step"><div class="num">4</div><div><h2>My Scripture</h2><p class="why">The verse that speaks most directly to me. This is the one I will memorize.</p></div></div>
<ul class="opts">
{hw_scrip}
</ul>
<div class="fill"><span>A verse I found myself:</span><i></i></div>
<div class="lines"><i></i></div>

<div class="foot">✦ ✦ ✦</div>
</div>

<!-- ============ HOMEWORK, PAGE 2 ============ -->
<div class="card">
<div class="tag">Homework · Replace and Rehearse</div>
<h1>Practicing the Truth</h1>
<div class="orn">✦ ✦ ✦</div>

<div class="step"><div class="num">5</div><div><h2>My practice plan</h2><p class="why">Everyone does the first three. Then pick one or two extra tools.</p></div></div>
<div class="group">Everyone does these</div>
<ul class="opts">
<li><strong>Make my Truth Card</strong> (below). Carry it and read it at least three times a day.</li>
<li><strong>Memorize my Scripture</strong> from Step 4.</li>
<li><strong>Set reminders</strong> to silently repeat my truth. Check one or more:
  <span class="scrip" style="font-style:normal">☐ <strong>A buzz:</strong> my watch or phone vibrates every ______ minutes<br/>☐ <strong>An everyday event:</strong> every time I ______________________________<br/>☐ <strong>A visual reminder:</strong> something I will see often, such as a sticky note on my mirror, my truth as the background picture on my phone, or a note on my car dashboard.</span></li>
</ul>
<div class="group">Pick one or two that fit me</div>
<ul class="opts">
<li><strong>{log_t}:</strong> {log_d}</li>
<li><strong>My name in Scripture:</strong> Rewrite my verse with my name in it and read it aloud each morning.
  <span class="scrip">For example, {name_ref} becomes: “{name_html}”</span></li>
<li><strong>Gratitude journal:</strong> Each night, write three things I thank God for.</li>
<li><strong>Truth recording:</strong> Record my own voice reading my Truth Card and verse, and listen in the car or on a walk.</li>
<li><strong>Reading:</strong> The <a href="{PEARLS}{reading}" target="_blank" rel="noopener">“{PEARLS_TOPICS[reading]}” topic in Pearls</a>.</li>
<li><strong>Listening:</strong> The Overcoming {listen} audio download.</li>
</ul>

<div class="step"><div class="num">6</div><div><h2>My action step this week</h2><p class="why">Do one thing that tests the lie in real life.</p></div></div>
<ul class="opts">
{actions}
</ul>
<div class="fill"><span>What I will do:</span><i></i></div>
<div class="fill"><span>When:</span><i></i></div>
<div class="fill"><span>What the lie predicts will happen:</span><i></i></div>

<div class="step"><div class="num">7</div><div><h2>End-of-week check-in</h2><p class="why">Bring this page to your next session.</p></div></div>
<div class="fill"><span>What actually happened:</span><i></i></div>
<div class="lines"><i></i></div>
<div class="fill"><span>What I learned:</span><i></i></div>
<div class="rate"><span><b>The lie</b> “{e(lie)}”: <span class="box"></span> %</span><span><b>My truth:</b> <span class="box"></span> %</span></div>

<h2>Daily practice tracker</h2>
<table class="track">
<tr><th>Day</th><th>Read my card</th><th>Said my verse</th><th>Used my reminder</th><th>{tracker}</th></tr>
""" + "".join('<tr><td>%s</td><td></td><td></td><td></td><td class="wide"></td></tr>\n' % dname
              for dname in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]) + f"""</table>

<h2>My Truth Card</h2>
<div class="cutcard">
<div class="lbl">The lie</div>
<div class="lie">{e(belief)}</div>
<div class="lbl">The truth</div>
<div class="lines"><i></i><i></i></div>
<div class="lbl">God’s Word</div>
<div class="lines"><i></i><i></i></div>
</div>
<p class="cutnote">Copy onto a 3×5 card, or cut along the dashed line and carry it with you.</p>

<h2>Prayer</h2>
<p class="prayer">{d['prayer']}</p>
<div class="foot">✦ ✦ ✦</div>
<p class="bnote">{TRANSLATION_NOTE}</p>
</div>

<p class="back"><a href="#top">Back to top</a> · <a href="{LIST_PAGE}" target="_top">All Spiritual/Religious False Beliefs</a></p>

</div></body></html>
"""
    return file_base, page, [k for r in hw_refs + [key_ref] + d["also"] for k, _ in verses(r, bible)]


def main():
    global PEARLS_TOPICS
    PEARLS_TOPICS = json.load(open(os.path.join(TOOLS, "pearls-topics.json"), encoding="utf-8"))
    bible = load_bible()
    style = open(os.path.join(TOOLS, "card-style.css"), encoding="utf-8").read().rstrip()
    nums = [int(a) for a in sys.argv[1:]] or sorted(
        int(f[:3]) for f in os.listdir(os.path.join(TOOLS, "cards")) if f.endswith(".json"))
    for n in nums:
        d = json.load(open(os.path.join(TOOLS, "cards", "%03d.json" % n), encoding="utf-8"))
        base, page, used = render(d, bible, style)
        for old in os.listdir(OUT):  # remove an older file name for the same number
            if old.startswith("Belief-%03d-" % n) and not old.startswith(base + "."):
                os.remove(os.path.join(OUT, old))
        hp = os.path.join(OUT, base + ".html")
        open(hp, "w", encoding="utf-8").write(page)
        pp = os.path.join(OUT, base + ".pdf")
        subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=8000", "--print-to-pdf=" + pp, hp],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("built", base, "verses:", len(set(used)))


if __name__ == "__main__":
    main()
