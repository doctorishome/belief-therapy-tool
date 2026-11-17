"""Restyle God cards 1–5 and Christ cards 7–10 like card 6.

What Scripture teaches becomes beige boxes with one-sentence connectors.
Every other direct quotation is a beige box. Teaching verses are not repeated.
No verse appears more than twice. Card 6 is not touched.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_cards import load_bible, scripture  # noqa: E402

bible = load_bible()
CITE = re.compile(r"((?:[1-3] )?[A-Za-z]+ \d+:\d+(?:[–-]\d+)?) \(“(.*?)”\)")
REF = re.compile(r"(?:[1-3] )?[A-Za-z]+ \d+:\d+(?:[–-]\d+)?")
CSS = (
    "\n  .sv{margin:0 0 8px;padding:12px 16px;background:var(--soft);border-left:4px solid var(--gold)}"
    "\n  .sv b{display:block;color:var(--navy);font-style:normal;margin:0 0 4px}"
    "\n  .sv q{font-style:italic;color:var(--navy)}"
    "\n  .opts li .sv{margin:6px 0 2px}"
    "\n  .teach .bridge{margin:4px 0 14px}"
)


def norm(ref):
    return ref.replace("-", "–")


def verse_text(ref):
    text = scripture(norm(ref), bible).rstrip()
    if text and text[-1] not in ".!?…’”:":
        text += "."
    return text


def box(ref):
    ref = norm(ref)
    return '<p class="sv"><b>%s</b><q>%s</q></p>' % (ref, html.escape(verse_text(ref)))


def teach_html(paragraph):
    parts = []
    pos = 0
    plain = html.unescape(paragraph)
    for m in CITE.finditer(plain):
        bridge = re.sub(r"\s+", " ", plain[pos:m.start()]).strip()
        if bridge:
            parts.append('<p class="bridge">%s</p>' % html.escape(bridge))
        parts.append(box(m.group(1)))
        pos = m.end()
    tail = re.sub(r"\s+", " ", plain[pos:]).strip()
    if tail:
        parts.append('<p class="bridge">%s</p>' % html.escape(tail))
    if not parts:
        raise SystemExit("no citations in teaching")
    return '<div class="teach">\n' + "\n".join(parts) + "\n</div>"


def rewrite_cited(inner, items, kind):
    bits = re.split(r"(<li>.*?</li>)", inner, flags=re.S)
    cited = [i for i, b in enumerate(bits) if b.startswith("<li>") and REF.search(re.sub(r"<[^>]+>", "", b))]
    if len(cited) != len(items):
        raise SystemExit("%s cited %d vs %d" % (kind, len(cited), len(items)))
    for i, item in zip(cited, items):
        if kind == "q":
            q, ref = item
            bits[i] = "<li>%s%s</li>" % (html.escape(q), box(ref))
        else:
            lead, ref = item
            bits[i] = "<li>%s%s</li>" % (lead, box(ref))
    return "".join(bits)


def sub_ul(text, heading, items, kind, ul_class=None):
    pat = r"(<h2>%s</h2>.*?)(<ul(?: class=\"opts\")?>)(.*?)(</ul>)" % re.escape(heading)
    m = re.search(pat, text, re.S)
    if not m:
        raise SystemExit("missing ul " + heading)
    if ul_class and 'class="opts"' not in m.group(2) and heading != "Challenging questions":
        pass
    new_inner = rewrite_cited(m.group(3), items, kind)
    return text[: m.start()] + m.group(1) + m.group(2) + new_inner + m.group(4) + text[m.end() :]


# also, card questions (q,ref), homework questions, scripture refs,
# (name_ref, sarah), action (html, ref) list, prayer_ref
D = {}

D[1] = dict(
    also=["Micah 7:18-19", "Romans 8:33", "Isaiah 43:25", "2 Corinthians 5:21", "Colossians 2:13-14"],
    cq=[
        ("What does God do with the sin I confess?", "Psalm 32:5"),
        ("Who carried my sins in His own body?", "1 Peter 2:24"),
        ("What has Christ’s blood done for those He justifies?", "Romans 5:9"),
    ],
    hq=[
        ("In whom do I have redemption and forgiveness?", "Ephesians 1:7"),
        ("What does this verse say is proclaimed through Jesus?", "Acts 13:38-39"),
        ("What will God remember no more?", "Hebrews 8:12"),
    ],
    scripture=["John 3:17", "Isaiah 1:18", "Psalm 130:3-4", "Hebrews 10:17", "Titus 3:4-5", "1 John 2:2"],
    name=("John 3:17", "God sent His Son to save me, not to condemn me."),
    actions=[
        ("<strong>Write the sin you think God is punishing,</strong> then read this beside it.", "Isaiah 1:18"),
        ("<strong>Read this aloud</strong> each morning before you interpret the day.", "Psalm 130:3-4"),
        ("<strong>Ask one safe believer to read this with you</strong> when you say, “I have been sure God is punishing me.”", "Hebrews 10:17"),
    ],
    prayer="Titus 3:4-5",
)
D[2] = dict(
    also=["2 Corinthians 1:3-4", "Psalm 23:4", "Romans 8:18", "1 Peter 5:10", "Nahum 1:7"],
    cq=[
        ("Does this verse say the world will be trouble-free, or that Jesus gives peace in it?", "John 14:27"),
        ("What does God keep, according to this verse, when I tell Him my pain?", "Psalm 56:8"),
    ],
    hq=[
        ("Who goes before me and will not forsake me?", "Deuteronomy 31:8"),
        ("What is God for the oppressed?", "Psalm 9:9"),
    ],
    scripture=["Revelation 21:4", "Psalm 121:1-2", "Joshua 1:9", "2 Corinthians 4:8-9", "Psalm 42:11", "Romans 15:13"],
    name=("Psalm 42:11", "I can be downcast and still put my hope in God."),
    actions=[
        ("<strong>Read this aloud</strong> when the pain makes you ask why God allowed it.", "2 Corinthians 4:8-9"),
        ("<strong>Tell God the honest sentence,</strong> “I do not understand why You let this happen,” and then read this.", "Romans 15:13"),
    ],
    prayer="Revelation 21:4",
)
D[3] = dict(
    also=["Romans 8:15-16", "Galatians 4:6-7", "John 1:12", "Isaiah 49:15-16", "Lamentations 3:22-23"],
    cq=[
        ("If God is for me, who can condemn me?", "Romans 8:31-32"),
        ("What does the Lord do for the people who fear Him here?", "Psalm 149:4"),
        ("How does Jesus describe the love He has for His own?", "John 15:9"),
        ("Did God love me before I loved Him?", "1 John 4:10"),
    ],
    hq=[
        ("How long has the Lord loved His people?", "Jeremiah 31:3"),
        ("Why does this psalm say to give thanks?", "Psalm 136:1"),
        ("What can separate me from the love of God?", "Romans 8:39"),
        ("What will I be, and what will I see?", "1 John 3:2"),
    ],
    scripture=["Luke 15:20", "Psalm 27:10", "Ephesians 2:4-5", "Titus 3:4", "Romans 8:32", "1 John 4:16"],
    name=("Luke 15:20", "The Father runs to meet me. He has not given up."),
    actions=[
        ("<strong>Read this when you feel like a disappointment,</strong> and write one way God has already loved you.", "Psalm 27:10"),
        ("<strong>Say this verse aloud</strong> before you review a failure.", "Ephesians 2:4-5"),
        ("<strong>Tell one safe believer,</strong> “I think God is disappointed in me,” and ask them to read this with you.", "Titus 3:4"),
    ],
    prayer="Romans 8:32",
)
D[4] = dict(
    also=["Psalm 139:7-10", "Deuteronomy 31:6", "Genesis 16:13", "Psalm 23:4", "Matthew 6:8"],
    cq=[
        ("Does the Protector of Israel sleep?", "Psalm 121:3-4"),
        ("How near is God to each of us?", "Acts 17:27"),
        ("Can I hide from God in a secret place?", "Jeremiah 23:23-24"),
    ],
    hq=[
        ("What has God promised never to do?", "Hebrews 13:5"),
        ("Does Jesus leave His disciples as orphans?", "John 14:18"),
        ("Who holds my right hand?", "Psalm 73:23-24"),
    ],
    scripture=["Matthew 28:20", "Psalm 16:11", "Deuteronomy 31:8", "Isaiah 30:18", "Psalm 27:10", "Romans 8:38-39"],
    name=("Matthew 28:20", "Jesus is with me always, even when I cannot feel Him."),
    actions=[
        ("<strong>Bring one care to God out loud,</strong> then read this.", "Deuteronomy 31:8"),
        ("<strong>Write three details of today</strong> and read this as a reminder that God knows them.", "Psalm 16:11"),
        ("<strong>When God feels far, read this</strong> and write “with me” next to the need.", "Isaiah 30:18"),
    ],
    prayer="Romans 8:38-39",
)
D[5] = dict(
    also=["Romans 8:32", "Galatians 3:28", "Ephesians 2:4-5", "1 John 4:16", "Titus 3:4"],
    cq=[
        ("Does God show partiality?", "Deuteronomy 10:17"),
        ("What does James say about favoritism?", "James 2:1"),
        ("Does God treat people differently because of their status?", "Galatians 2:6"),
    ],
    hq=[
        ("Who did Jesus come to seek?", "Luke 19:10"),
        ("Who may call on the name of the Lord?", "Romans 10:13"),
        ("Whom does God want to be saved?", "1 Timothy 2:4"),
    ],
    scripture=["Isaiah 55:1", "Revelation 22:17", "Matthew 11:28", "John 7:37", "Colossians 3:11", "John 6:37"],
    name=("Isaiah 55:1", "God’s invitation is for the thirsty, including me."),
    actions=[
        ("<strong>Write the person you are comparing yourself with,</strong> then read this beside their name.", "Colossians 3:11"),
        ("<strong>Read this aloud</strong> and thank God for one gift without measuring it.", "Matthew 11:28"),
        ("<strong>Pray for someone you have ranked above or below yourself,</strong> using this verse.", "John 7:37"),
    ],
    prayer="Revelation 22:17",
)
D[7] = dict(
    also=["Romans 8:33-34", "Colossians 2:13-14", "Titus 3:5", "2 Timothy 1:9", "Romans 6:14"],
    cq=[
        ("Are we justified by works, or through faith in Christ?", "Galatians 2:16"),
        ("What does this verse say we are justified by?", "Romans 3:28"),
        ("Can anyone snatch Jesus’ sheep out of His hand?", "John 10:28-29"),
        ("What has one offering done for those who are being sanctified?", "Hebrews 10:14"),
    ],
    hq=[
        ("Who keeps me from stumbling?", "Jude 1:24"),
        ("Who is faithful to finish what He calls me to?", "1 Thessalonians 5:24"),
        ("What is Christ to me if I am in Him?", "2 Corinthians 5:17"),
        ("For freedom, what has Christ done?", "Galatians 5:1"),
    ],
    scripture=["Ephesians 1:6", "Philippians 2:13", "Romans 8:15", "Colossians 3:3", "1 John 5:11-12", "Romans 5:8"],
    name=("Ephesians 1:6", "I am accepted in the Beloved. I do not keep that acceptance by myself."),
    actions=[
        ("<strong>Write “Jesus saved me” and “I must keep myself acceptable.”</strong> Cross out the second if it disagrees with this.", "Romans 5:8"),
        ("<strong>Read this each morning</strong> before you review yesterday’s failures.", "Philippians 2:13"),
    ],
    prayer="1 John 5:11-12",
)
D[8] = dict(
    also=["John 10:9", "1 John 5:11-12", "John 8:12", "Acts 16:31", "1 Corinthians 8:6"],
    cq=[
        ("What does the one who believes in the Son have?", "John 3:36"),
        ("Who did Jesus say He is, regarding resurrection and life?", "John 11:25-26"),
        ("What is the will of the Father for everyone who looks to the Son?", "John 6:40"),
        ("What confession does this verse join to being saved?", "Romans 10:9"),
    ],
    hq=[
        ("What is eternal life, according to Jesus?", "John 17:3"),
        ("Who is the true God and eternal life?", "1 John 5:20"),
        ("Who has made the Father known?", "John 1:18"),
        ("Whom does God tell to turn to Him and be saved?", "Isaiah 45:22"),
    ],
    scripture=["Matthew 11:27", "John 5:24", "1 John 2:23", "Acts 17:30-31", "John 6:47", "John 12:44-46"],
    name=("John 5:24", "Whoever hears Jesus and believes has crossed from death to life."),
    actions=[
        ("<strong>Copy Jesus’ words from this passage</strong> into a notebook without softening them.", "John 6:47"),
        ("<strong>Pray for one friend of another faith by name,</strong> then read this.", "Acts 17:30-31"),
    ],
    prayer="John 12:44-46",
)
D[9] = dict(
    also=["Isaiah 53:4", "Hebrews 5:7-8", "Matthew 8:17", "Psalm 22:24", "John 1:14"],
    cq=[
        ("What did Jesus say His soul felt in Gethsemane?", "Matthew 26:38"),
        ("Why did the Son share flesh and blood?", "Hebrews 2:14"),
        ("Whose affliction did the Lord share?", "Isaiah 63:9"),
        ("What did Jesus say from the cross about His thirst?", "John 19:28"),
    ],
    hq=[
        ("Who helps us when we do not know what to pray?", "Romans 8:26"),
        ("What did Jesus feel when He saw the crowds?", "Matthew 9:36"),
        ("How did Jesus love His own?", "John 13:1"),
        ("Whom does Jesus invite to come to Him?", "Matthew 11:28-29"),
    ],
    scripture=["1 Peter 2:21", "Psalm 69:20", "Luke 22:44", "Hebrews 12:2-3", "2 Corinthians 1:5", "Psalm 56:8"],
    name=("Matthew 11:28-29", "I can come to Jesus with this burden. He is gentle, and He understands."),
    actions=[
        ("<strong>Name the pain in one sentence,</strong> then read this over it.", "Psalm 69:20"),
        ("<strong>Read this</strong> and write “He is able to help” under the sorrow you have been hiding.", "1 Peter 2:21"),
        ("<strong>Tell one safe believer,</strong> “I have thought Jesus does not understand this,” and read this together.", "Psalm 56:8"),
    ],
    prayer="Luke 22:44",
)
D[10] = dict(
    also=["Isaiah 1:18", "Micah 7:19", "Psalm 51:7", "Ephesians 1:7", "Hebrews 10:17"],
    cq=[
        ("What kind of person is forgiven much?", "Luke 7:47"),
        ("Where did sin increase, and what overflowed even more?", "Romans 5:20"),
        ("What cleanses us from all sin?", "1 John 1:7"),
        ("What did Jesus say to the woman accused of adultery?", "John 8:11"),
    ],
    hq=[
        ("What does God say about sins that are like scarlet?", "Isaiah 1:18"),
        ("How far does God remove our transgressions?", "Psalm 103:12"),
        ("Is there condemnation for those who are in Christ Jesus?", "Romans 8:1"),
        ("What did Jesus say God sent Him to do, rather than to condemn?", "John 3:17"),
    ],
    scripture=["Isaiah 44:22", "Psalm 32:1", "Revelation 1:5", "Titus 3:5", "Romans 10:13", "Colossians 1:13-14"],
    name=("Isaiah 44:22", "God blots out my transgressions and calls me back."),
    actions=[
        ("<strong>Write the sin you think is too bad,</strong> then read this underneath it.", "Psalm 32:1"),
        ("<strong>Read this aloud</strong> and put your initials beside it as your own application, not as a change to the verse.", "Revelation 1:5"),
        ("<strong>Tell one safe believer the exception you have believed,</strong> and read this together.", "Romans 10:13"),
    ],
    prayer="Titus 3:5",
)

# Card 10 homework questions reuse teaching verses (2nd appearance). Also-see verses stay once.
# Isaiah 43:25, John 6:37, Isaiah 53:6, 1 Timothy 1:15 are teaching verses — that would be a 2nd use. Allowed.
# But user said ideally once. Using them again in homework is the one allowed repeat.
# Do not also put them in scripture. The lists above don't. Good.

FILES = {
    1: "Belief-001-God-Is-Punishing-Me-For-My-Sins.html",
    2: "Belief-002-If-There-Is-A-God-He-Would-Not-Let-This-Happen.html",
    3: "Belief-003-God-Is-Disappointed-In-Me.html",
    4: "Belief-004-God-Is-Too-Distant-To-Care.html",
    5: "Belief-005-God-Loves-Some-People-More.html",
    7: "Belief-007-Now-Its-Up-To-Me-To-Stay-Acceptable.html",
    8: "Belief-008-Jesus-Is-One-Way-Among-Many.html",
    9: "Belief-009-Jesus-Doesnt-Understand-What-Im-Going-Through.html",
    10: "Belief-010-My-Sins-Are-Too-Bad-For-Jesus.html",
}


def prayer_html(old_inner, ref):
    text = html.unescape(re.sub(r"<[^>]+>", "", old_inner))
    text = CITE.sub("this verse", text)
    text = re.sub(r"\s+", " ", text).strip()
    m = re.search(r"^(.*?\bwhat )this verse (?:declares|says)\.?\s*(.*)$", text, re.I)
    if not m:
        raise SystemExit("prayer shape: " + text[:160])
    lead = m.group(1) + "this verse says."
    tail = m.group(2).strip()
    return "<p class=\"prayer\">%s</p>\n%s\n<p class=\"prayer\">%s</p>" % (html.escape(lead), box(ref), html.escape(tail))


def apply_one(num):
    spec = D[num]
    path = ROOT / "belief-cards" / FILES[num]
    t = path.read_text()
    if ".sv{" not in t:
        t = t.replace("  .also p{margin:0 0 12px;padding-left:18px;border-left:3px solid var(--line)}",
                      "  .also p{margin:0 0 12px;padding-left:18px;border-left:3px solid var(--line)}" + CSS, 1)
    m = re.search(r"<h2>What Scripture teaches</h2>\s*<p>(.*?)</p>\s*<div class=\"key\">.*?</div>", t, re.S)
    if not m:
        raise SystemExit("teach block " + path.name)
    t = t[: m.start()] + "<h2>What Scripture teaches</h2>\n" + teach_html(m.group(1)) + t[m.end() :]
    also = "<h2>Also see</h2>\n<div class=\"teach\">\n" + "\n".join(box(r) for r in spec["also"]) + "\n</div>"
    t2, n = re.subn(r"<h2>Also see</h2>\s*<div class=\"also\">.*?</div>", also, t, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("also " + path.name)
    t = t2
    t = sub_ul(t, "Challenging questions", spec["cq"], "q")
    t = sub_ul(t, "My best question", spec["hq"], "q")
    scr = "<ul class=\"opts\">\n" + "\n".join("<li>%s</li>" % box(r) for r in spec["scripture"]) + "\n</ul>"
    t2, n = re.subn(r"(<h2>My Scripture</h2>.*?)(<ul class=\"opts\">)(.*?)(</ul>)",
                    lambda m: m.group(1) + scr, t, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("scripture " + path.name)
    t = t2
    name_ref, sarah = spec["name"]
    name = box(name_ref) + (
        '<span class="scrip">For example, this becomes: “<strong>Sarah</strong> can write: “%s”” '
        "Keep that sentence as your own words, not as the Bible verse.</span>"
    ) % html.escape(sarah)
    t2, n = re.subn(r'<span class="scrip">For example, .*?not as the Bible verse\.</span>', name, t, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("name " + path.name)
    t = t2
    t = sub_ul(t, "My action step this week", spec["actions"], "a")
    m = re.search(r"<p class=\"prayer\">.*?</p>", t, re.S)
    if not m:
        raise SystemExit("prayer " + path.name)
    t = t[: m.start()] + prayer_html(m.group(0), spec["prayer"]) + t[m.end() :]
    check(path.name, t, spec)
    path.write_text(t)
    print("wrote", path.name)


def check(name, text, spec):
    body = text.split("<!-- share-button:end -->", 1)[-1]
    refs = re.findall(r"<b>((?:[1-3] )?[A-Za-z]+ \d+:\d+(?:[–-]\d+)?)</b><q>(.*?)</q>", body)
    from collections import Counter
    c = Counter(r for r, _ in refs)
    over = [k for k, v in c.items() if v > 2]
    if over:
        raise SystemExit(name + " repeats " + str(over) + " " + str({k: c[k] for k in over}))
    bad = []
    for ref, quote in refs:
        got = verse_text(ref)
        q = html.unescape(quote)
        if q != got and q.rstrip(".") != got.rstrip("."):
            bad.append(ref)
    if bad:
        raise SystemExit(name + " text mismatch " + ", ".join(bad[:8]))
    teach = re.search(r"<h2>What Scripture teaches</h2>(.*?)<h2>Also see</h2>", body, re.S).group(1)
    teach_refs = set(re.findall(r"<b>(.*?)</b>", teach))
    later = body.split("<h2>Also see</h2>", 1)[1]
    reused = [r for r in teach_refs if "<b>%s</b>" % r in later]
    if reused:
        raise SystemExit(name + " teaching verse reused: " + ", ".join(reused))


def main():
    for num in D:
        apply_one(num)
    six = (ROOT / "belief-cards/Belief-006-I-Need-Someone-Else-To-Bring-My-Prayers-To-God.html").read_text()
    if "Hebrews 10:19" not in six:
        raise SystemExit("card 6 was damaged")
    print("card 6 untouched check ok")


if __name__ == "__main__":
    main()
