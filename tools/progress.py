#!/usr/bin/env python3
"""Rewrite the link table in PROGRESS.md from the cards that exist in belief-cards/."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EARLY = {1: "God is punishing me for my many sins.", 2: "If there is a God, He would not let this happen.",
         3: "God is disappointed in me.", 4: "God is too distant or too busy to care about me.",
         5: "God loves some people more than others."}

rows, last = [], 0
for f in sorted(os.listdir(os.path.join(ROOT, "belief-cards"))):
    m = re.match(r"Belief-(\d{3})-.*\.html$", f)
    if not m:
        continue
    n = int(m.group(1))
    jp = os.path.join(ROOT, "tools", "cards", "%03d.json" % n)
    belief = json.load(open(jp, encoding="utf-8"))["belief"] if os.path.exists(jp) else EARLY.get(n, "")
    rows.append("| %d | %s | %s |" % (n, belief, f))
    last = max(last, n)

p = os.path.join(ROOT, "PROGRESS.md")
t = open(p, encoding="utf-8").read()
t = re.sub(r"\*\*Where I left off:\*\*.*", "**Where I left off:** Cards 1–%d are done. Next card to build: **#%d**." % (last, last + 1), t)
t = re.sub(r"(\| # \| Belief \| Phone page \|\n\|---\|---\|---\|\n)(?:\|.*\n)*", lambda m: m.group(1) + "\n".join(rows) + "\n", t)
t = re.sub(r"- Cards \d+–120\.", "- Cards %d–120." % (last + 1), t)
open(p, "w", encoding="utf-8").write(t)
print("PROGRESS.md updated through #%d" % last)
