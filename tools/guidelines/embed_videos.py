"""Replace the "Training video N (coming soon)" notes on counselors/guidelines.html
with HeyGen players. Usage: python3 tools/guidelines/embed_videos.py ids.txt
ids.txt lines: "V02 <heygen id> <m:ss> <title>"  (title optional)."""
import re, sys

PAGE = 'counselors/guidelines.html'
TITLES = {
    2: 'Guidelines 3 and 4: Curiosity, Not Confrontation',
    3: 'Guideline 6: Ask Before Introducing Scripture',
    4: 'Guideline 6: When Scripture Feels Dismissive',
    5: 'Guideline 7: Forgiveness Is Not Reconciliation',
    6: 'Guideline 9: Respect Readiness and Pace',
    7: 'Guideline 5: Collaborative Behavioral Experiments',
    8: 'Guideline 10: Measure Progress Beyond Agreement',
    9: 'Guideline 12: Grief and Loss',
    10: 'Guideline 13: Trauma and PTSD',
    11: 'Guideline 14: Abuse',
    12: 'Closing Message: Belief Counseling at Its Best',
}


def player(n, vid, dur, label=None):
    m, s = dur.split(':')
    k = label or f'Guideline video {n}'
    return (f'<div class="gvid"><div class="gvid-k">{k} · {int(m)} min {int(s)} sec</div>'
            f'<div class="gvid-f"><iframe src="https://app.heygen.com/embeds/{vid}" '
            f'title="{TITLES[n]} (training video)" allow="encrypted-media; fullscreen" '
            f'allowfullscreen loading="lazy"></iframe></div></div>')


def main(idfile):
    ids = {}
    for line in open(idfile):
        p = line.split()
        if len(p) >= 3 and p[0].startswith('V'):
            ids[int(p[0][1:])] = (p[1], p[2])
    s = open(PAGE).read()
    for n, (vid, dur) in sorted(ids.items()):
        if n < 2:
            continue
        note = f'<p class="vidsoon">Guideline video {n} (coming soon) covers this guideline.</p>'
        if n == 2:
            if note in s:
                s = s.replace(note, player(2, vid, dur), 1)
                s = s.replace(note, '<p class="vidsoon">Training video 2, under Guideline 3 above, also covers this guideline.</p>', 1)
        elif n == 4:
            v3 = re.search(r'<div class="gvid"><div class="gvid-k">Training video 3 [^<]*</div>.*?</div></div>', s)
            if v3 and 'embeds/' + vid not in s:
                s = s[:v3.end()] + player(4, vid, dur) + s[v3.end():]
        elif n == 12:
            if 'embeds/' + vid not in s:
                i = s.find('<p class="motto">')
                s = s[:i] + player(12, vid, dur, 'Closing message') + '\n' + s[i:]
        elif note in s:
            s = s.replace(note, player(n, vid, dur), 1)
    open(PAGE, 'w').write(s)
    print('left:', re.findall(r'Training video \d+ \(coming soon\)', s))


if __name__ == '__main__':
    main(sys.argv[1])
