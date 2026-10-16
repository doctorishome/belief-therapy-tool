# Spiritual/Religious Belief Cards — Progress

**Where I left off:** Cards 1–25 are done. Next card to build: **#26**.

## How the cards are made
- Each card's content is in `tools/cards/NNN.json` (NNN = card number).
- `python3 tools/build_cards.py 11 12 13` builds the phone page (.html) and PDF into `belief-cards/`.
- Scripture is pulled automatically from `tools/BSB.txt` (Berean Standard Bible, public domain), so every verse is exact. Only references are stored in the card files.
- Fonts: before building, install Cormorant Garamond and Source Serif 4 locally (from github.com/google/fonts, folders ofl/cormorantgaramond and ofl/sourceserif4) so the PDFs match cards 1–5.
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
| 4 | God is too distant or too busy to care about me. | Belief-004-God-Is-Too-Distant-To-Care.html |
| 5 | God loves some people more than others. | Belief-005-God-Loves-Some-People-More.html |
| 6 | I need a priest, a saint, or Mary to bring my prayers to God. | Belief-006-I-Need-Someone-Else-To-Bring-My-Prayers-To-God.html |
| 7 | Jesus saved me, but now it’s up to me to stay acceptable. | Belief-007-Now-Its-Up-To-Me-To-Stay-Acceptable.html |
| 8 | Jesus is one good way to God among many. | Belief-008-Jesus-Is-One-Way-Among-Many.html |
| 9 | Jesus doesn’t understand what I’m going through. | Belief-009-Jesus-Doesnt-Understand-What-Im-Going-Through.html |
| 10 | Jesus died for other people’s sins, but not ones as bad as mine. | Belief-010-My-Sins-Are-Too-Bad-For-Jesus.html |
| 11 | If I don’t speak in tongues, I don’t have the Holy Spirit. | Belief-011-No-Tongues-Means-No-Holy-Spirit.html |
| 12 | If the Spirit were in me, I would never struggle. | Belief-012-If-The-Spirit-Were-In-Me-I-Would-Never-Struggle.html |
| 13 | I have committed the unpardonable sin. | Belief-013-I-Have-Committed-The-Unpardonable-Sin.html |
| 14 | The Spirit’s leading always comes as a strong feeling. | Belief-014-The-Spirits-Leading-Is-Always-A-Strong-Feeling.html |
| 15 | My spiritual gifts don’t matter as much as other people’s. | Belief-015-My-Spiritual-Gifts-Dont-Matter.html |
| 16 | Every problem I have is a spiritual attack. | Belief-016-Every-Problem-Is-A-Spiritual-Attack.html |
| 17 | Satan has power over me, and I am helpless. | Belief-017-Satan-Has-Power-Over-Me.html |
| 18 | I am under a generational curse. | Belief-018-I-Am-Under-A-Generational-Curse.html |
| 19 | My loved one has become an angel watching over me. | Belief-019-My-Loved-One-Has-Become-An-Angel.html |
| 20 | I should pray to angels for help. | Belief-020-I-Should-Pray-To-Angels.html |
| 21 | Strong emotions mean my faith is weak. | Belief-021-Strong-Emotions-Mean-My-Faith-Is-Weak.html |
| 22 | Depression and anxiety are always caused by sin. | Belief-022-Depression-And-Anxiety-Are-Always-Caused-By-Sin.html |
| 23 | Counseling or medication shows a lack of faith. | Belief-023-Counseling-Or-Medication-Shows-A-Lack-Of-Faith.html |
| 24 | My body and its desires are shameful. | Belief-024-My-Body-And-Its-Desires-Are-Shameful.html |
| 25 | Feeling angry is always a sin. | Belief-025-Feeling-Angry-Is-Always-A-Sin.html |

## Still to do
- Cards 26–120.
- Link each dropdown item on the Wix page "Spiritual/Religious False Beliefs" to its card (needs the Wix editor).
