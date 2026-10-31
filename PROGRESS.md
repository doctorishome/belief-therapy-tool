# Spiritual/Religious Belief Cards — Progress

**Where I left off:** All 120 cards are done (HTML + PDF). Remaining: link each card from the website dropdowns, and Brian’s review of cards 6–120.

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
| 26 | I have sinned too much to be forgiven. | Belief-026-I-Have-Sinned-Too-Much-To-Be-Forgiven.html |
| 27 | If I feel guilty, I must be guilty. | Belief-027-If-I-Feel-Guilty-I-Must-Be-Guilty.html |
| 28 | A good Christian always feels guilty. | Belief-028-A-Good-Christian-Always-Feels-Guilty.html |
| 29 | Being tempted is the same as sinning. | Belief-029-Being-Tempted-Is-The-Same-As-Sinning.html |
| 30 | Some sins can’t be forgiven until I confess them to a priest. | Belief-030-Some-Sins-Need-A-Priest-To-Be-Forgiven.html |
| 31 | Whatever my church teaches must be biblical. | Belief-031-Whatever-My-Church-Teaches-Must-Be-Biblical.html |
| 32 | Truth is whatever feels right to me. | Belief-032-Truth-Is-Whatever-Feels-Right-To-Me.html |
| 33 | If a teaching makes me feel good, it must be from God. | Belief-033-If-A-Teaching-Feels-Good-It-Must-Be-From-God.html |
| 34 | If a leader quotes Scripture, what he says must be true. | Belief-034-If-A-Leader-Quotes-Scripture-It-Must-Be-True.html |
| 35 | Church tradition carries the same authority as Scripture. | Belief-035-Church-Tradition-Has-The-Same-Authority-As-Scripture.html |
| 36 | God forgives, but He never forgets. | Belief-036-God-Forgives-But-He-Never-Forgets.html |
| 37 | I must pay for my sins through suffering. | Belief-037-I-Must-Pay-For-My-Sins-Through-Suffering.html |
| 38 | Forgiving means I must trust them again. | Belief-038-Forgiving-Means-I-Must-Trust-Them-Again.html |
| 39 | God has forgiven me, but I can never forgive myself. | Belief-039-I-Can-Never-Forgive-Myself.html |
| 40 | Forgiving means pretending it didn’t hurt. | Belief-040-Forgiving-Means-Pretending-It-Didnt-Hurt.html |
| 41 | I am saved by my good works. | Belief-041-I-Am-Saved-By-My-Good-Works.html |
| 42 | I can never really know whether I am saved. | Belief-042-I-Can-Never-Know-Whether-I-Am-Saved.html |
| 43 | One more sin and God will give up on me. | Belief-043-One-More-Sin-And-God-Will-Give-Up-On-Me.html |
| 44 | I must suffer in purgatory before I can be with God. | Belief-044-I-Must-Suffer-In-Purgatory.html |
| 45 | Being raised in a Christian family makes me a Christian. | Belief-045-Being-Raised-In-A-Christian-Family-Makes-Me-A-Christian.html |
| 46 | If I had enough faith, God would have healed me. | Belief-046-If-I-Had-Enough-Faith-God-Would-Have-Healed-Me.html |
| 47 | If I give more, God must give me more. | Belief-047-If-I-Give-More-God-Must-Give-Me-More.html |
| 48 | My words create my reality, so I must ‘name it and claim it.’ | Belief-048-My-Words-Create-My-Reality.html |
| 49 | If God doesn’t do a miracle, He doesn’t care. | Belief-049-If-God-Doesnt-Do-A-Miracle-He-Doesnt-Care.html |
| 50 | God’s blessing always shows up as health and wealth. | Belief-050-Gods-Blessing-Always-Shows-Up-As-Health-And-Wealth.html |
| 51 | Good Christians don’t have problems. | Belief-051-Good-Christians-Dont-Have-Problems.html |
| 52 | My worth depends on how much I serve. | Belief-052-My-Worth-Depends-On-How-Much-I-Serve.html |
| 53 | My needs and feelings never count. | Belief-053-My-Needs-And-Feelings-Never-Count.html |
| 54 | God is like my father (or mother). | Belief-054-God-Is-Like-My-Father-Or-Mother.html |
| 55 | Enjoying life is worldly or sinful. | Belief-055-Enjoying-Life-Is-Worldly-Or-Sinful.html |
| 56 | Doubt means I am not a real Christian. | Belief-056-Doubt-Means-I-Am-Not-A-Real-Christian.html |
| 57 | If I don’t feel close to God, He has left me. | Belief-057-If-I-Dont-Feel-Close-To-God-He-Has-Left-Me.html |
| 58 | Faith means never asking questions. | Belief-058-Faith-Means-Never-Asking-Questions.html |
| 59 | My faith is only as strong as my feelings. | Belief-059-My-Faith-Is-Only-As-Strong-As-My-Feelings.html |
| 60 | Real faith means never feeling afraid. | Belief-060-Real-Faith-Means-Never-Feeling-Afraid.html |
| 61 | I’m not good enough to go to heaven. | Belief-061-Im-Not-Good-Enough-To-Go-To-Heaven.html |
| 62 | My loved one in heaven is watching me and is disappointed in me. | Belief-062-My-Loved-One-In-Heaven-Is-Disappointed-In-Me.html |
| 63 | Heaven will be an endless, boring church service. | Belief-063-Heaven-Will-Be-An-Endless-Boring-Church-Service.html |
| 64 | In heaven I’ll be grieving for the people who aren’t there. | Belief-064-In-Heaven-Ill-Be-Grieving-For-Those-Not-There.html |
| 65 | In heaven every mistake I made will be shown to everyone. | Belief-065-In-Heaven-Every-Mistake-Will-Be-Shown.html |
| 66 | Every sinful thought puts me in danger of hell. | Belief-066-Every-Sinful-Thought-Puts-Me-In-Danger-Of-Hell.html |
| 67 | If I die with an unconfessed sin, I will go to hell. | Belief-067-If-I-Die-With-Unconfessed-Sin-I-Will-Go-To-Hell.html |
| 68 | I’m going to hell because of my many sins. | Belief-068-Im-Going-To-Hell-Because-Of-My-Many-Sins.html |
| 69 | My loved one is in hell because I didn’t share my faith enough. | Belief-069-My-Loved-One-Is-In-Hell-Because-Of-Me.html |
| 70 | Fear of hell is the main reason to follow God. | Belief-070-Fear-Of-Hell-Is-The-Main-Reason-To-Follow-God.html |
| 71 | My body doesn’t matter to God; only my soul counts. | Belief-071-My-Body-Doesnt-Matter-To-God.html |
| 72 | After death we become spirits floating forever. | Belief-072-After-Death-We-Become-Spirits-Floating-Forever.html |
| 73 | My illness, disability, or scars will last forever. | Belief-073-My-Illness-Disability-Or-Scars-Will-Last-Forever.html |
| 74 | If my body is cremated, God can’t raise it. | Belief-074-If-My-Body-Is-Cremated-God-Cant-Raise-It.html |
| 75 | I won’t know my loved ones after the resurrection. | Belief-075-I-Wont-Know-My-Loved-Ones-After-The-Resurrection.html |
| 76 | If I grieve deeply, I don’t trust God. | Belief-076-If-I-Grieve-Deeply-I-Dont-Trust-God.html |
| 77 | God took my loved one because He needed them more than I did. | Belief-077-God-Took-My-Loved-One-Because-He-Needed-Them.html |
| 78 | Being afraid of death means my faith is weak. | Belief-078-Being-Afraid-Of-Death-Means-My-Faith-Is-Weak.html |
| 79 | My loved one who died by suicide can never be with God. | Belief-079-My-Loved-One-Who-Died-By-Suicide-Can-Never-Be-With-God.html |
| 80 | My loved one died because I didn’t pray enough. | Belief-080-My-Loved-One-Died-Because-I-Didnt-Pray-Enough.html |
| 81 | If my prayer isn’t answered, I prayed the wrong way. | Belief-081-If-My-Prayer-Isnt-Answered-I-Prayed-The-Wrong-Way.html |
| 82 | God only listens if I use the right words. | Belief-082-God-Only-Listens-If-I-Use-The-Right-Words.html |
| 83 | Asking God more than once shows a lack of faith. | Belief-083-Asking-God-More-Than-Once-Shows-A-Lack-Of-Faith.html |
| 84 | If I pray enough, I shouldn’t need a doctor or counselor. | Belief-084-If-I-Pray-Enough-I-Shouldnt-Need-A-Doctor.html |
| 85 | God only hears the prayers of good people. | Belief-085-God-Only-Hears-The-Prayers-Of-Good-People.html |
| 86 | If I don’t read my Bible every day, God is displeased with me. | Belief-086-If-I-Dont-Read-My-Bible-Every-Day-God-Is-Displeased.html |
| 87 | Every verse applies directly to me, whatever its context. | Belief-087-Every-Verse-Applies-Directly-To-Me.html |
| 88 | I must never question or wrestle with hard passages. | Belief-088-I-Must-Never-Question-Hard-Passages.html |
| 89 | Any verse is a promise I can claim for whatever I want. | Belief-089-Any-Verse-Is-A-Promise-I-Can-Claim.html |
| 90 | Only pastors or scholars can understand the Bible. | Belief-090-Only-Pastors-Or-Scholars-Can-Understand-The-Bible.html |
| 91 | Questioning my pastor is questioning God. | Belief-091-Questioning-My-Pastor-Is-Questioning-God.html |
| 92 | Pastors and leaders are closer to God than I am. | Belief-092-Pastors-And-Leaders-Are-Closer-To-God.html |
| 93 | Leaving a church means leaving God. | Belief-093-Leaving-A-Church-Means-Leaving-God.html |
| 94 | Family problems must be kept secret to protect the church. | Belief-094-Family-Problems-Must-Be-Kept-Secret.html |
| 95 | Being busy at church means being spiritual. | Belief-095-Being-Busy-At-Church-Means-Being-Spiritual.html |
| 96 | Being submissive means accepting mistreatment or abuse. | Belief-096-Being-Submissive-Means-Accepting-Abuse.html |
| 97 | Because I am divorced, God can’t use me. | Belief-097-Because-I-Am-Divorced-God-Cant-Use-Me.html |
| 98 | Sex is dirty, even in marriage. | Belief-098-Sex-Is-Dirty-Even-In-Marriage.html |
| 99 | If my children turn away from God, I failed as a parent. | Belief-099-If-My-Children-Turn-Away-I-Failed-As-A-Parent.html |
| 100 | Single people are less complete in God’s eyes. | Belief-100-Single-People-Are-Less-Complete-In-Gods-Eyes.html |
| 101 | If I miss God’s perfect will, my life is ruined. | Belief-101-If-I-Miss-Gods-Perfect-Will-My-Life-Is-Ruined.html |
| 102 | God’s will is always the thing I least want. | Belief-102-Gods-Will-Is-Always-The-Thing-I-Least-Want.html |
| 103 | I need a clear sign from God before I can decide anything. | Belief-103-I-Need-A-Clear-Sign-Before-I-Can-Decide.html |
| 104 | Every decision has one right answer, and I must find it. | Belief-104-Every-Decision-Has-One-Right-Answer.html |
| 105 | If something is hard, it can’t be God’s will. | Belief-105-If-Something-Is-Hard-It-Cant-Be-Gods-Will.html |
| 106 | If I am suffering, God is punishing me. | Belief-106-If-I-Am-Suffering-God-Is-Punishing-Me.html |
| 107 | Real Christians don’t suffer. | Belief-107-Real-Christians-Dont-Suffer.html |
| 108 | I must figure out the reason for everything bad that happens. | Belief-108-I-Must-Figure-Out-The-Reason-For-Everything-Bad.html |
| 109 | Complaining to God is a sin. | Belief-109-Complaining-To-God-Is-A-Sin.html |
| 110 | My suffering means God has abandoned me. | Belief-110-My-Suffering-Means-God-Has-Abandoned-Me.html |
| 111 | I must keep the rules to stay in God’s favor. | Belief-111-I-Must-Keep-The-Rules-To-Stay-In-Gods-Favor.html |
| 112 | The more I do for God, the more He loves me. | Belief-112-The-More-I-Do-For-God-The-More-He-Loves-Me.html |
| 113 | Because of grace, my choices don’t matter. | Belief-113-Because-Of-Grace-My-Choices-Dont-Matter.html |
| 114 | Resting or receiving help means I’m spiritually lazy. | Belief-114-Resting-Or-Receiving-Help-Means-Im-Lazy.html |
| 115 | I have to clean up my life before I can come to God. | Belief-115-I-Have-To-Clean-Up-My-Life-Before-I-Can-Come-To-God.html |
| 116 | I should live in constant fear of the end times. | Belief-116-I-Should-Live-In-Constant-Fear-Of-The-End-Times.html |
| 117 | Current events tell me exactly when the end is coming. | Belief-117-Current-Events-Tell-Me-When-The-End-Is-Coming.html |
| 118 | I could be left behind because I’m not good enough. | Belief-118-I-Could-Be-Left-Behind-Because-Im-Not-Good-Enough.html |
| 119 | Since the world is ending, planning for the future doesn’t matter. | Belief-119-Since-The-World-Is-Ending-Planning-Doesnt-Matter.html |
| 120 | Natural disasters are God punishing the people they strike. | Belief-120-Natural-Disasters-Are-God-Punishing-The-People-They-Strike.html |

## Song players (rule for all cards)
- Cards are opened from the Wix page inside a restricted box, so links to youtube.com from a card are blocked ("refused to connect").
- Fix: each song plays inside the card using the youtube-nocookie.com embed player (tap the picture to play), with a small "Watch on YouTube" link as backup. Card 43 is the model (see its script at the bottom of the file).
- Use official LYRIC videos (words on screen) from the artist's own channel. Brian wants users to read the words to reinforce the truth, and some sounds are hard for him to hear. Avoid music videos and live videos without words.
- Test every new song's embed before using it; some music-label videos refuse embedding.
- Every card (1–120) now has its Overcoming Anxiety or Depression recording player (from its "listening" value) and a linked homework Listening item; recordings are in the Wix Media Manager of "Pearls Working 5", folder Audio (addresses in tools/add_songs.py). Cards 1–5 have no JSON, so their HTML was updated directly with add_songs().
- Songs live in each card's JSON ("songs": [[videoID, title, artist, one-line why], ...]); tools/add_songs.py adds the audio, songs, journal and player script when the cards are built. Cards 26, 41–45 and 52 done (26 and 52 embeds not yet tested); the rest of the 120 still need songs.

## Still to do
- Link each dropdown item on the Wix page "Spiritual/Religious False Beliefs" to its card (needs the Wix editor).
- Brian to review cards 6–120 (written by Claude from his 120-belief list in the style of cards 1–5).
- Cards 1–5 quote the NIV; cards 6–120 quote the Berean Standard Bible.

## Godly Counsel Lessons (added Oct 16, 2026)
- Under "Related Pearls topics," a card can list Godly Counsel Lessons. Add `"godly_counsel": [26, 14, 6, 7]` (lesson numbers) to the card's JSON file and rebuild.
- Links go to the framed lessons in `belief-cards/godly-counsel/` (navy-and-gold frame, letter size, printable).
- To re-make the framed lessons: `python3 tools/frame_godly_counsel.py <folder with the 33 chapter PDFs>` (Brian's file Godly_Counsel_33_Chapters_5.zip). Lesson list: `tools/godly-counsel-chapters.json`.
- Done: all 120 cards have Godly Counsel Lessons (Brian approved the list Oct 16, 2026; list in `tools/godly-counsel-plan.json`). Cards 1–5 have no JSON file, so their lesson section was added directly to the HTML (via `godly_counsel_html` in build_cards.py) and their PDFs re-printed.
- The first page of Self-Esteem, Low (#24) says "Lesson 23" in the book (typo). The framed copy shows "Lesson 24" (see FIXES in tools/frame_godly_counsel.py). The book file and Wix copy still say 23.
- Cards 1, 26, 41, 42, 45, 52 use slightly tighter print spacing on the belief page (`"print_tight": true`, style in `tools/print-tight.css`; card 1 has it in its HTML) so their PDFs keep their original page count. Phone view is unchanged.

## Psychological/Cognitive belief cards (started Oct 17, 2026)
- Wix page: https://doctorishome.wixstudio.com/website-6/blank-7 ("Psychological/Cognitive False Beliefs", not yet in the menu). Its content is an HTML embed (#html1): 10 personality-disorder boxes, 5 beliefs each.
- Cards live in `belief-cards/psychological/` as hand-made HTML (no builder yet). Card #1: Psych-001-If-I-Let-My-Guard-Down.html (+ PDF), linked from the Paranoid belief "Relaxing my guard leaves me defenseless." via `<a class="cardlink">` in the embed code.
- Next cards are drafted by ChatGPT from Brian's desktop file "Instructions for ChatGPT - Next Psych Card" (template = card #1); Brian uploads them here, then each is linked from its belief in the embed and the site republished.
- To do: add page to menu + rename its address; make the page's belief wording match card titles.

## Counselors' Room addresses (Wix test site)
Welcome blank-11, Process blank-12, Tips blank-13, Theory blank-14, Cases blank-15, Course blank-16, Library blank-17 (under /website-6/). masterPage.js lock uses blank-12..17; REQUIRE_PAID still false until payments are set up.

## Core False Beliefs cards (started Oct 20, 2026)
- 22 core beliefs, in six groups (My Worth, My Strength, Other People, The World & the Future, Rules I Live By, After Painful Experiences). Wording comes from the Wix page "Core False Beliefs" (/website-6/core-beliefs).
- Same format as the other cards. Content in `tools/core/NNN.json`. Build: `python3 tools/build_core_cards.py core <group-folder> "<Group Title>"`, then `python3 tools/print_core_cards.py <group-folder> "<Group Title>"`. Cards go to `belief-cards/core/<group-folder>/` as Core-NNN-....
- Songs: 3 contemporary + 1 classic (Brian's request).
- No link to the separate "I Am Worthless" Counseling Companion; core cards stand on their own (Brian, Oct 20, 2026).
- Website list: `belief-lists/core.html` (same look as the Wix box). To make a belief clickable, fill in its `link:`. The Wix page "Core False Beliefs" now shows this GitHub list (embed #html3 set to its web address, Oct 20, 2026), so no Wix edits are needed for new cards. The old table embed (#html2) is still on the page in a hidden section.
- Done (Oct 20, 2026): all 22 cards built and linked on the list. Brian approved card 1; cards 2-22 await his review. Card content for 2-22 is generated by tools/make_core_cards.py (edit there, rerun it, then rebuild the group). Group folders: my-worth, my-strength, other-people, world-future, rules-i-live-by, after-painful-experiences.

## Lie Finder (Counselor's Room search) — started Oct 21, 2026
- Master list of false beliefs for the Lie Finder search: `lie-finder/master-list.json` (for the search) and `lie-finder/master-list.html` (readable review page).
- Built automatically from the cards by `python3 tools/build_lie_finder_list.py`. Re-run it after adding cards, then push.
- Each entry: id, level, topic, belief, where it comes from (short), what clients say (up to 6), card link.
- Oct 21: 447 beliefs (Bio 75, Psych 55, Interpersonal 60, Socioeconomic 55, Sociocultural 60, Spiritual 120, Core 22); 25 psychological beliefs have no card yet.
- Search instructions: `lie-finder/search-instructions.md` (safety and real needs first, 5–7 lies in Strong fit / Likely / Worth checking, why it fits, confirming questions, ask for missing client words). Test 1 (single mother, can't feed five children) approved by Brian Oct 21.
- Next: one or two more test cases, then the members-only search page on Pearls Working 5.
- Oct 21: Lie Finder page built: `lie-finder/app.html` (shown on the Wix page inside an "Embed a site" element). Wix code to paste once: `lie-finder/wix-code/lieFinder.web.js` (backend, file `backend/lieFinder.web.js`) and `lie-finder/wix-code/page-code.js` (page code; element must be `#html1`). Needs secret `ANTHROPIC_API_KEY` in the Wix Secrets Manager. Search is owner-only (Permissions.Admin) until the Counselor's Room has members; then change to Permissions.SiteMember. Model: claude-sonnet-5-5. Instructions and master list are read from GitHub, so updates need no Wix editing.
- Oct 21: Lie Finder is live at https://doctorishome.wixstudio.com/website-6/lie-finder (page "Lie Finder", not in the menu; backend file backend/lieFinder.web.js and page code are in place; embed element #html1, 1100 x 2400). Tested: page and backend connect; search waits only for the ANTHROPIC_API_KEY secret.
- Oct 21: Renamed the tool to **False Belief Finder** (Brian's choice). Wix page address: /false-belief-finder. Repository folder stays `lie-finder/`.

## Articles
- `belief-cards/articles/` holds framed articles: each `.html` is the phone page (shared style `article.css`) and `python3 tools/build_article_pdf.py belief-cards/articles/<Name>.html` makes the matching framed PDF.
- Oct 21: "Free Will, Pain, and Suffering" in two versions: `Free-Will-Pain-and-Suffering` (written to clients, for the pain and suffering cards) and `Free-Will-Pain-and-Suffering-For-Counselors` (for the Counselor's Room). Both include Nick Vujicic's story (60 Minutes Australia video, youtube.com/watch?v=tJnJ_fTYofQ; picture from Brian's original document in `images/nick-story.jpg`). Not yet linked from any card.
- Oct 21: "Read more" box (Read online + Download PDF) for "Free Will, Pain, and Suffering" added after the Truth summary on 17 cards: SPR 002, 073, 077, 106, 107, 108, 110, 120; INT 049; BIO 006, 008, 061–065, 075. Added by `python3 tools/add_article_links.py` (list of cards is inside the script). If any of these cards is rebuilt, run that script again to put the box back. Not added to homework pages (they are printed).

## Recommended Books (planned)
- `books/recommended-books.md`: Brian's list of books to recommend on cards (author, Amazon Associates link, why, which cards). Started Oct 21 with *The Problem of Pain* (C.S. Lewis) and *When God Doesn't Make Sense* (James Dobson) for the 17 pain and suffering cards. Oct 21: "Recommended Books" boxes are on the cards listed for each book (17 cards so far), placed just before Related Pearls topics, without Amazon buttons yet. When Brian adds Amazon Associates links to the list, run `python3 tools/add_book_boxes.py`: it adds the "View on Amazon" buttons and Amazon's required notice to every card automatically. Also run it after editing the list or rebuilding a card.
- Oct 21: A library-style Recommended Books page was drafted (branch `library-preview`, never made live). Brian set it aside: he prefers showing the real, colorful book covers the way Amazon presents them. Revisit when his Amazon Associates links (and Amazon-provided cover images) are ready.

## Public and counselor pages (Oct 22, 2026)
- `pages/behavioral-experiments.html`: public "Behavioral Experiments" page, shown on Wix page /blank-5 through an "Embed Site" element (#html1; desktop 840x2450, tablet 720x2700, phone 370x3400). Edit the file here to change wording; make the Wix box taller if the text grows.
- `pages/counselor/behavioral-interventions-ccbt.html` (+ PDF): "Behavioral Interventions in Christian Cognitive-Behavioral Therapy". Listed on the Counselors' Room Articles page. Original Word file saved beside it. Full height: about 4600px at 840 wide, 7700px on phones.
- Psychological/Cognitive page heading: page code (#text5) puts "Cognitive" on its own line at 75% size so the word doesn't split.

## Counselors' Room Articles (Oct 22, 2026)
- New tab "Articles" in the Counselors' Room menu (added to all 8 pages in `counselors/`). Page: `counselors/articles.html` — one card per article (topic tag, title, summary, Read article [new tab] + Download PDF).
- Articles so far: Behavioral Interventions in CCBT (`pages/counselor/`), Free Will, Pain, and Suffering — counselor version (`belief-cards/articles/`).
- To add an article: put the HTML (+ PDF) on GitHub, then add one entry to the list in `counselors/articles.html`. No Wix editing needed (the tab opens inside the existing Counselors' Room embeds).

## Counselors' Room: drop-down menu and 3-step Process (Oct 22, 2026)
- Top menu now uses drop-downs: Welcome · Learn (The Process, Theory Topics, Professional Tips) · Practice (Case Studies, The Course) · Resources (Clinical Library, Articles) · False Belief Finder ↗ · Public Site ↗. Built by `python3 tools/counselor_nav.py` (edit GROUPS there to add a page, then run it; it updates all counselors/*.html).
- `counselors/process.html` rewritten for the simplified model: flow diagram Presenting Problem → Belief Mining → 1 Identify → 2 Challenge → 3 Replace → The Truth Sets You Free, with a loop note, then a section per part. The 8 steps are gone. PDF: `counselors/Belief-Counseling-Flow.pdf`. Page height now ~2500px at 1000 wide, ~4300px on phones.
- "Eight steps" wording also changed on welcome, cases and course pages. The Course lesson list still follows the old 8 steps (lessons 5 and 7) and needs Brian's new outline.

## Home page split + public landing page (Oct 23, 2026)
- Home (`site/home.html`): the single blue Counselor's Room button is replaced by two side-by-side buttons: "I'm seeking help for myself or my family" (left) and "I'm a counselor or ministry leader" (right, to the Counselor's Room /blank-11).
- New public landing page `pages/help-for-you.html`: empathetic opening, why beliefs matter, Identify/Challenge/Replace, short example (Romans 8:38-39 written out, links to Core cards 001 and 003), "Is this for me?", 988 crisis note, two next-step buttons (Core False Beliefs, Belief Counseling?), John 8:32 closing, educational note. No contact button (Brian's choice). Scripture in BSB.
- Wix page "Help for You" (/help-for-you, not in the menu) shows this file in an Embed Site element (#html1; desktop 840x3300 (section 3340), tablet 720x3700 (3720), phone 370x4900 (4920); Brian added a picture section above it; made by duplicating Behavioral Experiments). The left Home button opens it.
- Wix "Embed a site" boxes do not allow target="_top" links (no allow-top-navigation); links to other Wix pages must use target="_blank" (Oct 23, 2026).
- Oct 23: Home button style options preview: `pages/home-button-options.html` (A text links, B outlined, C slim bar, D small gold). Brian wants quieter buttons; Brian chose D (small gold buttons, no subtitles); applied to site/home.html. Standing request: build new pages as GitHub files (easier to change, fewer tokens).
- Oct 23: Public belief search `pages/belief-search.html` (searches lie-finder/master-list.json; ?embed=1 hides its title). On Help for You, the left button "Search for a False Belief" opens it in a panel right under the buttons (and hides the closing banner while open, so it fits the Wix box); right button "Learn More About Beliefs" opens the Wix /beliefs page. The Identify/Challenge/Replace list on Help for You is replaced by the Model diagram from the Home page (without the chips). Heights now: 840w 3059 closed / 3229 open; 720w 3238/3378; 370w 4769/4782 — keep under the Wix box sizes.
- Oct 23: Wix page "Search False Beliefs" (/search-false-beliefs, not in the menu) shows `pages/belief-search.html` (plain word search, no AI) in an Embed Site box (made by duplicating Behavioral Experiments; sizes 840x2450 / 720x2700 / 370x3400). The Help for You left button opens it in a new tab; the inline search panel was removed.
- Oct 23: "Beliefs?" page moved to GitHub: `pages/beliefs.html` (same wording as the Wix page; hero picture and book cover from Wix media; verses in a side column; gold Next button to /belief-counseling).
- Oct 23: Wix "Beliefs?" page (/beliefs) now shows only `pages/beliefs.html` in an Embed Site box (#html1 in section8; heights 3450 desktop / 4300 tablet / 4600 phone). The old Wix text sections were deleted. Edit the GitHub file to change this page.
- Oct 23: "Belief Counseling?" page moved to GitHub: `pages/belief-counseling.html` (picture beside intro, four principle cards, gold Next button to /belief-mining; fixed "provide"→"provides" and "Belief Therapy"→"Belief Counseling").
- Oct 23: Wix "Belief Counseling?" page (/belief-counseling) now shows only `pages/belief-counseling.html` (Embed Site #html1 in section8, top margin 20; heights 1150 desktop / 1750 tablet / 1950 phone). Old Wix sections deleted. Pattern for moving a Wix page to GitHub: copy section8 (embed) from the Beliefs? page, paste it on the target page, delete the old sections, change the embed address, set heights, publish.
- Oct 23: `level-pages/level-nav.js` = Belief Mining progress meter (6 levels, current one dark, earlier ones gold, each clickable) + dark bar (← Back to Level #N / gold "Forward to Level #N+1: name →"; level 6 forwards to Core False Beliefs). Added at the bottom of the five GitHub false-belief lists (biological-physical, interpersonal, socioeconomic, sociocultural, spiritual-religious). Not on the Psychological list (its Wix page uses its own embed code, not a GitHub file) and not yet on the level pages (tools.html boxes have fixed heights; check sizes first).

## Home page: explanation before the choice (Oct 31, 2026)
- Brian approved Oct 31; now live in `site/home.html` (preview file removed). Order: hero (buttons removed) → "What Is Belief Counseling?" (plain explanation, three example false beliefs, "Often helpful for" chips) → The Model → "Where Would You Like to Begin?" (two cards with one-line descriptions + small gold buttons: Begin here → /help-for-you, Enter the Counselor's Room → /blank-11) → Foundation → Resources. John 8:32 label changed NIV → BSB.
- Heights of the new page: 1300w 5241, 980w 5328, 840w 5471, 720w 5627, 370w 7511 (old: 3517 / 3610 / 3733 / 3809 / 4938). Wix Home embed box is 3556 tall on desktop, so it must be made taller (≈5300 desktop, ≈5700 tablet, ≈7600 phone) when the preview goes live: copy home-preview.html over home.html, push, then resize the box.
- Oct 31: Wix Home embed #html1 resized: desktop 1280 x 5300 (Scale proportionally, as before), tablet 762 x 5580 and phone 380 x 7650, both now "Relative width" (fixed height) instead of Scale proportionally. If the home page text grows, raise these heights.

## DSM-5-TR Reviews page (Oct 31, 2026)
- New Counselors' Room page `counselors/reviews.html` (menu: Resources > DSM-5-TR Reviews). Grouped list: Mood; Anxiety and Trauma; Other Common Concerns; More Serious or Complex. Live: Depression, Anxiety, OCD, Schizophrenia. "Coming soon": Bipolar, PTSD, Prolonged Grief, Substance Use, Eating Disorders, ADHD, Adjustment, Somatic Symptom/Illness Anxiety, Borderline/Personality, Autism.
- To publish a review: add the PDF to `counselors/reviews/`, then in reviews.html replace that row's `<span class="soon">Coming soon</span>` with an `<a class="open" ...>Open PDF</a>` link (see the comment at the top of the list).
- Welcome page box now shows only the description and "See all reviews →".
