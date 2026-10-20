# How to build Belief Counseling cards (guide for any AI helper)

Repository: https://github.com/doctorishome/belief-therapy-tool  
Live files: https://doctorishome.github.io/belief-therapy-tool/

## What a card is
One false belief gets one card: an HTML page, a Card + Homework PDF, and a Homework-only PDF.
Each card has: where the belief comes from, what Scripture teaches, a key verse (BSB text), "also see" verses,
common self-statements, common logical errors, questions, a truth statement, homework truths, a log, four actions,
a prayer, four song videos (3 modern + 1 classic), related Pearls topics, and Godly Counsel chapters.

## The model to copy
Look at the five finished examples in `tools/socioeconomic/` (001–005) and `tools/socioeconomic-wealth/` (006–010).
Each `.json` file is one card. Copy the field names exactly. Write in plain, warm, non-clinical language.
Public pages avoid clinical terms.

## Rules
- Scripture text is the Berean Standard Bible. Check any reference with `python3 tools/verse.py "John 3:16"`.
  Any verse quoted in the card text must match the BSB wording.
- `pearls` and `reading` must be keys in `tools/pearls-topics.json`.
- `songs` must be keys in `tools/music-catalog.json`.
- `godly_counsel` numbers must be chapters in `tools/godly-counsel-chapters.json`.
- Money cards include a note that the card is educational, not financial or legal advice.

## Steps
1. Write the card JSON files in a new folder `tools/<set-name>/` (numbering continues from the last card).
2. Build the HTML: `python3 tools/build_socio_cards.py <set-folder> <output-subfolder> "<Group Title>"`
3. Build the PDFs: `python3 tools/print_socio_cards.py <output-subfolder> "<Group Title>"`
4. Link each belief on its page list. The list files are in `belief-lists/` (for example `belief-lists/socioeconomic.html`).
   Add the card URLs to the card-link map in that file. Beliefs without a card stay plain text.
5. Commit and push. The Wix pages show the new GitHub files automatically. No Wix edit is needed.

Other card families (Psychological, Marriage) use their own builders in `tools/` (`build_cards.py`, `build_marriage_cards.py`).
