"""Adds the "What does a mentally healthy Christian look like?" book box to every belief card.
The box is copied from the sample card (Inter-060) and placed just before the card's "Listen:" section.
Safe to run again: a card that already has the box gets it replaced, not duplicated.
Run from the repo root after rebuilding any cards:  python3 tools/add_christlike_box.py"""
import glob, re
SAMPLE = 'belief-cards/interpersonal/boundaries-conflict/Inter-060-A-Good-Christian-Never-Gets-Angry.html'
box = re.search(r'<!--christlike-->.*?<!--/christlike-->\n', open(SAMPLE, encoding='utf-8').read(), re.S).group(0)
files = [f for f in glob.glob('belief-cards/**/*.html', recursive=True)
         if not f.endswith('/index.html') and '/books/' not in f and '/articles/' not in f and '/godly-counsel/' not in f]
added = replaced = skipped = 0
for f in sorted(files):
    s = open(f, encoding='utf-8').read()
    if '<!--christlike-->' in s:
        new = re.sub(r'<!--christlike-->.*?<!--/christlike-->\n?', lambda m: box, s, flags=re.S)
        replaced += new != s
    elif '<h2>Listen' in s:
        new = s.replace('<h2>Listen', box + '<h2>Listen', 1); added += 1
    else:
        skipped += 1; print('no Listen section:', f); continue
    if new != s: open(f, 'w', encoding='utf-8').write(new)
print(f'added {added}, updated {replaced}, skipped {skipped}, cards checked {len(files)}')
