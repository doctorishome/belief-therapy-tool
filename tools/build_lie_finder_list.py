"""Builds the Lie Finder master list from the belief cards in this repository.

Run:  python3 tools/build_lie_finder_list.py

Writes:
  lie-finder/master-list.json  - the list the Lie Finder search reads (one entry per false belief)
  lie-finder/master-list.html  - the same list as a readable page for Dr. Campbell to review

Each entry: id, level, topic, belief, origins (short), client_words (what clients typically say), card link.
Sources: the card .json files in tools/<set>/, plus tools/lists/psychological.json for
psychological beliefs (older psychological cards have no .json, so their text is read from the card page).
Re-run after adding cards; nothing here needs editing by hand.
"""
import json, re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://doctorishome.github.io/belief-therapy-tool/'
LEVELS = [  # (code, name), in the order of the six levels, then Core
    ('BIO', 'Biological/Physical'),
    ('PSY', 'Psychological/Cognitive'),
    ('INT', 'Interpersonal'),
    ('SEC', 'Socioeconomic'),
    ('SCU', 'Sociocultural'),
    ('SPR', 'Spiritual/Religious'),
    ('CORE', 'Core False Beliefs'),
]
LEVEL_NAME = dict(LEVELS)


def level_for(folder):
    if folder.startswith('bio-'): return 'BIO'
    if folder.startswith('psych-'): return 'PSY'
    if folder.startswith('inter-') or folder == 'marriage': return 'INT'
    if folder.startswith('socioeconomic'): return 'SEC'
    if folder.startswith('cult-'): return 'SCU'
    if folder == 'cards': return 'SPR'
    if folder == 'core' or folder.startswith('core-'): return 'CORE'
    return None


def clean(s):
    s = re.sub(r'<[^>]+>', '', str(s or ''))
    return re.sub(r'\s+', ' ', html.unescape(s)).strip().strip('“”"')


def short(text, sentences=2, limit=320):
    parts = re.split(r'(?<=[.!?])\s+', clean(text))
    out = ' '.join(parts[:sentences])
    return out if len(out) <= limit else out[:limit].rsplit(' ', 1)[0] + '…'


def pretty(slug):
    return ' '.join(w.capitalize() for w in slug.replace('-', ' ').split())


CARD_PAGES = [p for p in (ROOT / 'belief-cards').rglob('*.html')]


def find_page(file_stem):
    for p in CARD_PAGES:  # page names are "<File>.html" or "<Word>-<number>-<File>.html"
        if p.stem == file_stem or re.sub(r'^([A-Za-z]+-)?\d+-', '', p.stem) == file_stem:
            return p
    return None


def page_sections(page):
    """Read 'Where it often comes from' and 'Common self-statements' from a card page."""
    t = page.read_text(encoding='utf-8')
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    t = re.sub(r'<h[1-4][^>]*>', '\n### ', t)
    t = re.sub(r'<li[^>]*>', '\n- ', t)
    t = html.unescape(re.sub(r'<[^>]+>', '', t))
    origins, words = '', []
    m = re.search(r'### Where it often comes from(.*?)\n###', t, flags=re.S)
    if m: origins = m.group(1)
    m = re.search(r'### Common self-statements(.*?)\n###', t, flags=re.S)
    if m: words = [clean(x) for x in re.findall(r'\n- (.+)', m.group(1))]
    return origins, words


entries, seen = [], set()

# 1. Every card that has a .json file
for f in sorted((ROOT / 'tools').glob('*/*.json')):
    code = level_for(f.parent.name)
    if not code:
        continue
    d = json.loads(f.read_text(encoding='utf-8'))
    if not isinstance(d, dict) or 'belief' not in d:
        continue
    page = find_page(d['file'])
    topic = d.get('group') or d.get('tag') or (pretty(page.parent.name) if page and page.parent.name != 'belief-cards' else '')
    words = d.get('self_statements') or d.get('self') or []
    entries.append({
        'level': code,
        'prefix': 'M' if f.parent.name == 'marriage' else '',
        'num': int(d['num']),
        'topic': clean(topic),
        'belief': clean(d.get('belief_plain') or d['belief']),
        'origins': short(d.get('origins', '')),
        'client_words': [clean(w) for w in words][:6],
        'card': BASE + page.relative_to(ROOT).as_posix() if page else None,
    })
    if page:
        seen.add(page.name)

# 2. Spiritual/Religious cards written before the .json files were used (cards 1-5)
for page in sorted((ROOT / 'belief-cards').glob('Belief-*.html')):
    if page.name in seen:
        continue
    t = page.read_text(encoding='utf-8')
    m = re.search(r'False Belief #(\d+) · ([^·<]+)', t)
    title = re.search(r'<h[12][^>]*>(.*?)</h[12]>', t, flags=re.S)
    origins, words = page_sections(page)
    entries.append({
        'level': 'SPR', 'prefix': '', 'num': int(m.group(1)) if m else int(page.stem.split('-')[1]),
        'topic': clean(m.group(2)) if m else '', 'belief': clean(title.group(1)) if title else '',
        'origins': short(origins), 'client_words': words[:6],
        'card': BASE + page.relative_to(ROOT).as_posix(),
    })
    seen.add(page.name)

# 3. Psychological beliefs listed on the website (older cards have no .json; some have no card yet)
lst = json.loads((ROOT / 'tools/lists/psychological.json').read_text(encoding='utf-8'))
psy_nums = {e['num'] for e in entries if e['level'] == 'PSY'}
next_num = 1000
for g in lst['groups']:
    for b in g['beliefs']:
        link = b[1] if len(b) > 1 else None
        if link and link in seen:
            for e in entries:  # card already added from its .json: use the website's group name as topic
                if e['card'] and e['card'].endswith('/' + link):
                    e['topic'] = g['name']
            continue
        origins, words = '', []
        num = None
        if link:
            page = ROOT / 'belief-cards/psychological' / link
            m = re.match(r'Psych-(\d+)', link)
            num = int(m.group(1)) if m else None
            if page.exists():
                origins, words = page_sections(page)
        if num is None or num in psy_nums:
            next_num += 1
            num = next_num
        psy_nums.add(num)
        entries.append({
            'level': 'PSY', 'prefix': '', 'num': num, 'topic': g['name'], 'belief': clean(b[0]),
            'origins': short(origins), 'client_words': words[:6],
            'card': lst['card_base'] + link if link else None,
        })

# Order and number
order = {c: i for i, (c, _) in enumerate(LEVELS)}
entries.sort(key=lambda e: (order[e['level']], e['prefix'], e['num']))
for e in entries:
    n, pre = e.pop('num'), e.pop('prefix')
    e['id'] = '%s-%s%03d' % (e['level'], pre, n) if n < 1000 else '%s-X%02d' % (e['level'], n - 1000)
    e['level'] = LEVEL_NAME[e['level']]
entries = [{k: e[k] for k in ('id', 'level', 'topic', 'belief', 'origins', 'client_words', 'card')} for e in entries]

out = ROOT / 'lie-finder'
out.mkdir(exist_ok=True)
(out / 'master-list.json').write_text(json.dumps({
    'title': 'Belief Counseling - Lie Finder master list',
    'note': 'Built by tools/build_lie_finder_list.py from the belief cards. Do not edit by hand; re-run the script.',
    'count': len(entries),
    'beliefs': entries,
}, ensure_ascii=False, indent=1), encoding='utf-8')

# Readable review page
e = html.escape
counts = {}
for x in entries:
    counts[x['level']] = counts.get(x['level'], 0) + 1
sections = []
for _, name in LEVELS:
    items = [x for x in entries if x['level'] == name]
    if not items:
        continue
    rows = []
    for x in items:
        link = ('<a href="%s" target="_blank" rel="noopener">Open card</a>' % e(x['card'])) if x['card'] else '<span class="none">No card yet</span>'
        words = ''.join('<li>%s</li>' % e(w) for w in x['client_words'])
        rows.append('<article><div class="meta"><span class="id">%s</span> · %s · %s</div><h3>“%s”</h3>%s%s</article>' % (
            e(x['id']), e(x['topic']), link, e(x['belief']),
            ('<p><b>Where it comes from:</b> %s</p>' % e(x['origins'])) if x['origins'] else '',
            ('<p><b>What clients say:</b></p><ul>%s</ul>' % words) if words else ''))
    sections.append('<details><summary>%s <small>%d beliefs</small></summary>%s</details>' % (e(name), len(items), ''.join(rows)))
css = ('body{margin:0;background:#F7F3EA;color:#1E2430;font:17px/1.55 Georgia,serif}main{max-width:900px;margin:0 auto;padding:24px 16px 64px}'
       'h1{color:#1F3A68;font-size:32px;margin:0 0 8px}details{background:#fff;border:1px solid #E2D9C4;border-radius:10px;margin:12px 0;padding:0 16px}'
       'summary{cursor:pointer;padding:16px 0;font-size:21px;font-weight:700;color:#1F3A68}summary small{font-weight:400;color:#5A6170;font-size:15px;margin-left:8px}'
       'article{border-top:1px solid #EFE7D6;padding:14px 0}h3{margin:4px 0;font-size:19px}.meta{font:14px/1.4 system-ui,sans-serif;color:#5A6170}'
       '.id{font-weight:700;color:#9A6F1E}.none{color:#8A5A00}p{margin:6px 0}ul{margin:4px 0 4px 20px;padding:0}a{color:#1F3A68}')
summary = ' · '.join('%s: %d' % (n, counts[n]) for _, n in LEVELS if n in counts)
page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex"><title>Lie Finder Master List</title><style>%s</style></head><body><main>'
        '<h1>Lie Finder Master List</h1><p>%d false beliefs. %s</p><p>Tap a level to open it.</p>%s</main></body></html>') % (
        css, len(entries), e(summary), ''.join(sections))
(out / 'master-list.html').write_text(page, encoding='utf-8')
print(len(entries), 'beliefs;', summary)
