# Pearls topic cards: the standard to follow

The model card is `pearls/abortion.html`. Every other Pearls topic card should match it.

## 1. Look (do not change)
- Load Google Font Lora in the page head (`Lora` 400, 700, and italic 400).
- Title: `'Lora', Georgia, serif`, bold, 26 px.
- Verses in the beige box (and Synopsis/Guidance text): `'Lora', Georgia, serif`, 20 px, line-height 1.55. Do not use Arial. (Changed Nov 24, 2026 from 23 px / 1.65 so verses read well on a phone.)
- Verse references: bold, underlined in gold, `'Lora', Georgia, serif`, 16 px (smaller than the verses). Wrap the parentheses and the reference link in `<span class="ref-wrap">` so the parentheses are 16 px too. (Changed Nov 24, 2026.) The reference sits at the END of the verse, on the same line: one space after the verse's last word, then the reference. Do NOT put `<br>` between the verse and the reference. `.ref-wrap { display: inline; white-space: nowrap; font-size: 16px; }` keeps "(Psalm 139:13)" together; if it does not fit, the whole reference moves to the next line.
  Example: `...in my mother’s womb. <span class="ref-wrap">(<a class="ref" href="https://biblehub.com/psalms/139-13.htm" target="_blank" rel="noopener">Psalm 139:13</a>)</span><span class="hub">...</span>`
- Section headings (e.g., "God's Guidance"): `'Lora', Georgia, serif`, bold, green #596653, 23 px.
- "Context · Commentary" links (`.hub`): the first link's text is "Context" (not "Read in context"). System font, 600 weight, 16 px, shown as a block, CENTERED (`text-align: center`), with `margin: 6px 0 34px`. Do not put `<br><br>` after `.hub`; that margin is the gap before the next verse (about 34 px). The last `.hub`, the one before the note, has no bottom margin.
- Copy the whole `<style>` block from `pearls/abortion.html` unchanged. Do not restyle.

## 2. Bible text
- Use the Berean Standard Bible (BSB) wording for every verse (public domain). Not the NIV.
- Check each verse against the BSB exactly (`python3 tools/verse.py "Psalm 139:13"`).
- Keep the same verses and order as the original Pearls topic; only the translation changes.
- If the card's own paragraphs quote a verse word for word, make that quote match the BSB too.

## 3. Links under each verse
- Reference link: `https://biblehub.com/<book>/<chapter>-<verse>.htm`
- "Context": `https://biblehub.com/bsb/<book>/<chapter>.htm`
- "Commentary": David Guzik's Enduring Word, chapter page:
  `https://enduringword.com/bible-commentary/<book>-<chapter>/`
  - Book names are lowercase with hyphens: `psalm-139` (singular "psalm"), `1-john-1`, `2-corinthians-5`, `song-of-solomon-2`.
  - Some chapters are grouped on Enduring Word (e.g., `1-chronicles-4-8`). Open each link to make sure it loads before publishing.
- All links open in a new tab (`target="_blank" rel="noopener"`).
- Note under the box: "“Context” opens the chapter in the Berean Standard Bible on Bible Hub. “Commentary” opens David Guzik’s Enduring Word commentary on that chapter. Both open in a new tab."

## 4. Working safely
- One AI helper works on Pearls at a time.
- Convert a few cards, have Brian review, then continue in small batches.

## 5. The website shows the same look
- The Counselor Scripture Search page (beliefcounselor.com/counselor-scriptures) builds its own display from the Wix database. Its page code already places the reference at the end of each verse and centers "Context · Commentary" for every converted topic (any topic whose Scripture text has biblehub.com or enduringword.com links). The database text may say either "Read in context" or "Context"; the page shows "Context" either way.
