"""Adds the optional media sections to a built card page: Overcoming Anxiety audio,
"Songs that speak truth to this belief" (in-card YouTube players), and the song journal.

A card gets songs when its JSON file has a "songs" list:
  "songs": [["YouTubeVideoID", "Song title", "Artist", "One sentence on how it speaks truth to this lie."], ...]

Why in-card players: cards are opened from the Wix page inside a restricted box, so a plain
link to youtube.com is refused. The youtube-nocookie.com embed plays inside the card instead.
Test each new video's embed before using it (some music-label videos refuse embedding).
"""
import html, os

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "songs_assets")


def _read(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()


def add_songs(page, d):
    songs = d.get("songs")
    if not songs:
        return page
    e = html.escape
    cards = []
    for vid, title, artist, why in songs:
        cards.append(
            '<a class="song" href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">'
            '<span class="thumb" style="background-image:url(\'https://i.ytimg.com/vi/%s/hqdefault.jpg\')"></span>'
            '<span class="txt"><span class="st">%s</span><span class="sa">%s</span><span class="sw">%s</span></span></a>'
            % (vid, vid, e(title), e(artist), e(why)))
    audio = _read("audio.html") if d.get("listening", "Depression") == "Anxiety" else ""
    block = (audio + '<h2>Songs that speak truth to this belief</h2>\n'
             '<p class="songnote2">Tap a song to play it right here.</p>\n<div class="songs">\n'
             + "\n".join(cards) + '\n</div>\n'
             '<p class="songnote">Songs play here through YouTube and may start with a short ad. '
             'If one will not play, use its “Watch on YouTube” link.</p>\n\n')

    def swap(old, new):
        nonlocal page
        assert page.count(old) == 1, "anchor not found once: " + old[:50]
        page = page.replace(old, new)

    if audio:
        swap("<li><strong>Listening:</strong> The Overcoming Anxiety audio download.</li>",
             '<li><strong>Listening:</strong> The <a href="https://music.wixstatic.com/mp3/dbdded_f67d414544534727acf6973d58189443.mp3" '
             'target="_blank" rel="noopener">Overcoming Anxiety audio</a> by Dr. Brian Campbell. Tap to play.</li>')
    swap("</style>", _read("songs.css") + "</style>")
    swap('<p class="morning">', block + '<p class="morning">')
    swap("Everyone does the first three.", "Everyone does the first four.")
    swap("<li><strong>Set reminders</strong>",
         "<li><strong>Listen to one song each day</strong> from “Songs that speak truth to this belief” on my card, "
         "and fill in my song journal (below).</li>\n<li><strong>Set reminders</strong>")
    journal = ('<h2>My song journal</h2>\n<p class="why">After each day\'s song, write what it told you that challenges the lie.</p>\n'
               '<table class="track songj">\n<tr><th>Day</th><th>Song I listened to</th><th>What it told me that challenges the lie</th></tr>\n'
               + "".join('<tr><td>%s</td><td></td><td></td></tr>\n' % x for x in "Mon Tue Wed Thu Fri Sat Sun".split())
               + '</table>\n\n')
    swap("<h2>My Truth Card</h2>", journal + "<h2>My Truth Card</h2>")
    swap("</body>", _read("songs.js.html") + "</body>")
    return page
