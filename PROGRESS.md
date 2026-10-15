# Spiritual/Religious Belief Cards — Progress

**Where I left off:** Cards 1–10 are done. Next card to build: **#11** (Holy Spirit group).

## How the cards are made
- Each card's content is in `tools/cards/NNN.json` (NNN = card number).
- `python3 tools/build_cards.py 11 12 13` builds the phone page (.html) and PDF into `belief-cards/`.
- Scripture is pulled automatically from `tools/BSB.txt` (Berean Standard Bible, public domain), so every verse is exact. Only references are stored in the card files.
- Pearls topic links are checked against `tools/pearls-topics.json` (172 topics from the Pearls database).
- Belief wording and numbering come from Brian's file "Belief_Cards_All_120_Plain_Language.html", with these changes:
  - #1 is now "God is punishing me for my many sins."
  - #2 is now "If there is a God, He would not let this happen."
  - #68 is now "I'm going to hell because of my many sins."

## Bible version
- Cards 1–5: NIV (written earlier).
- Cards 6 onward: Berean Standard Bible (BSB). Brian chose CSB first, but CSB text could not be checked word for word, so BSB is used for accuracy.

## Links for the website dropdown items
Base address: `https://doctorishome.github.io/belief-therapy-tool/belief-cards/`

| # | Belief | Phone page |
|---|---|---|
| 1 | God is punishing me for my many sins. | Belief-001-God-Is-Punishing-Me-For-My-Sins.html |
| 2 | If there is a God, He would not let this happen. | Belief-002-If-There-Is-A-God-He-Would-Not-Let-This-Happen.html |
| 3 | God is disappointed in me. | Belief-003-God-Is-Disappointed-In-Me.html |
| 4 | God is too distant to care. | Belief-004-God-Is-Too-Distant-To-Care.html |
| 5 | God loves some people more. | Belief-005-God-Loves-Some-People-More.html |
| 6 | I need a priest, a saint, or Mary to bring my prayers to God. | Belief-006-I-Need-Someone-Else-To-Bring-My-Prayers-To-God.html |
| 7 | Jesus saved me, but now it's up to me to stay acceptable. | Belief-007-Now-Its-Up-To-Me-To-Stay-Acceptable.html |
| 8 | Jesus is one good way to God among many. | Belief-008-Jesus-Is-One-Way-Among-Many.html |
| 9 | Jesus doesn't understand what I'm going through. | Belief-009-Jesus-Doesnt-Understand-What-Im-Going-Through.html |
| 10 | Jesus died for other people's sins, but not ones as bad as mine. | Belief-010-My-Sins-Are-Too-Bad-For-Jesus.html |

## Still to do
- Cards 11–120.
- Link each dropdown item on the Wix page "Spiritual/Religious False Beliefs" to its card (needs the Wix editor).
