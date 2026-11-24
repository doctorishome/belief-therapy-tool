# Pearls topic cards: the standard to follow

The model card is `pearls/abortion.html`. Every other Pearls topic card should match it.

## 1. Look (do not change)
- Load Google Font Lora in the page head (`Lora` 400, 700, and italic 400).
- Title: `'Lora', Georgia, serif`, bold, 26 px.
- Verses in the beige box (and Synopsis/Guidance text): `'Lora', Georgia, serif`, 20 px, line-height 1.55. Do not use Arial. (Changed Nov 24, 2026 from 23 px / 1.65 so verses read well on a phone.)
- Verse references: bold, underlined in gold, `'Lora', Georgia, serif`, 16 px (smaller than the verses). Wrap the parentheses and the reference link in `<span class="ref-wrap">` so the parentheses are 16 px too. The reference sits on its own line, centered under the verse (`.ref-wrap { display: block; text-align: center; margin-top: 6px; }`). The “Read in context · Commentary” line below it stays left-aligned.
- Section headings (e.g., "God's Guidance"): `'Lora', Georgia, serif`, bold, green #596653, 23 px.
- "Read in context · Commentary" links (`.hub`): system font, 600 weight, 16 px, shown as a block with `margin: 6px 0 34px`. Do not put `<br><br>` after `.hub`; that margin is the gap before the next verse (about 34 px). The last `.hub`, the one before the note, has no bottom margin.
- Copy the whole `<style>` block from `pearls/abortion.html` unchanged. Do not restyle.

## 2. Bible text
- Use the Berean Standard Bible (BSB) wording for every verse (public domain). Not the NIV.
- Check each verse against the BSB exactly (`python3 tools/verse.py "Psalm 139:13"`).
- Keep the same verses and order as the original Pearls topic; only the translation changes.
- If the card's own paragraphs quote a verse word for word, make that quote match the BSB too.

## 3. Links under each verse
- Reference link: `https://biblehub.com/<book>/<chapter>-<verse>.htm`
- "Read in context": `https://biblehub.com/bsb/<book>/<chapter>.htm`
- "Commentary": David Guzik's Enduring Word, chapter page:
  `https://enduringword.com/bible-commentary/<book>-<chapter>/`
  - Book names are lowercase with hyphens: `psalm-139` (singular "psalm"), `1-john-1`, `2-corinthians-5`, `song-of-solomon-2`.
  - Some chapters are grouped on Enduring Word (e.g., `1-chronicles-4-8`). Open each link to make sure it loads before publishing.
- All links open in a new tab (`target="_blank" rel="noopener"`).
- Note under the box: "“Read in context” opens the chapter in the Berean Standard Bible on Bible Hub. “Commentary” opens David Guzik’s Enduring Word commentary on that chapter. Both open in a new tab."

## 4. Working safely
- One AI helper works on Pearls at a time.
- Convert a few cards, have Brian review, then continue in small batches.
