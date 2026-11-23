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
- Wix page: https://www.beliefcounselor.com/blank-7 ("Psychological/Cognitive False Beliefs", not yet in the menu). Its content is an HTML embed (#html1): 10 personality-disorder boxes, 5 beliefs each.
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
- Oct 21: Lie Finder is live at https://www.beliefcounselor.com/lie-finder (page "Lie Finder", not in the menu; backend file backend/lieFinder.web.js and page code are in place; embed element #html1, 1100 x 2400). Tested: page and backend connect; search waits only for the ANTHROPIC_API_KEY secret.
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

- Nov 1, 2026: False Belief Finder backend (`lie-finder/wix-code/lieFinder.web.js`) now works with Claude or Grok (set PROVIDER at the top; secret ANTHROPIC_API_KEY or XAI_API_KEY) and uses prompt caching (full master list always sent first in fixed order; Claude cache_control 5-min; Grok automatic + x-grok-conv-id). Wix Secrets Manager had 0 secrets as of Nov 1, so searches cannot run until a key is added.

## Counselors' Introduction page for visitors (Nov 11, 2026)
- `counselors/landing.html` is now Brian's Introduction page (who the site is for, why Belief Counseling, what is inside, Clinical Companion, about Dr. Campbell, short Membership section). The Wix "For Counselors" page still shows landing.html to visitors, so no Wix change was needed.
- The old "Join the Counselors' Room" page (price box, sign-up steps, what membership includes) is kept as `counselors/membership.html`, not linked yet. It is meant for the future "Membership" menu item inside the Counselors' Room.
- "See what's inside" (top and bottom) links to welcome.html, so visitors can enter the Counselors' Room. There is no visitor limit yet: every reading page is open until Brian chooses which pages visitors may see. To build then: visitor view with locked pages, plus the Membership menu item.
- Nov 11: temporary gold "Under construction" strip added at the top of `counselors/landing.html` (class `construct`). Remove it when the Counselors' Room structure is finished.
- Nov 11: temporary gold "Under construction" strip also added to the home page (`site/home.html`, class `construct`). It sits on top of the hero picture (position:absolute), so the page height and the Wix embed box heights are unchanged. Remove both strips when the Counselors' Room structure is finished.

## New Counselors' Room replaces the old one (Nov 12, 2026)
- Built from Brian's "Basic Organization" outline; he approved the preview and asked for the old room to be removed, keeping only the new room and the Clinical Companion.
- The room is `members/` (start at `members/index.html`): Belief Counseling · The Process · Traditional Assessment · Professional Tips · Library · Clinical Companion (gold, paid members). Built by `python3 tools/build_members_room.py`: edit PAGES there and run it again. Items with no link show a "Coming" label. Room name is the ROOM line at the top.
- Old room pages removed: `counselors/welcome.html`, `intro.html`, `process.html`, `library.html`, `course.html` are now one-line forwarders to the new room (written by the same script), because the Wix pages still load those addresses. No Wix edit was needed. Their old content is in the Git history before Nov 12, 2026.
- Kept in `counselors/` because the new room or the Clinical Companion uses them: forms, reviews, videos, presentations, theory, articles, books, tips, cases, core-beliefs, help, clinical-companion, new-client-forms, practice-forms, followup-forms, landing (visitor Introduction), membership. The pages with a menu now carry the Member's Room menu: `python3 tools/update_counselor_nav.py`.
- Do not run `tools/build_counselor_world.py`: it would write the old room pages back. The old `tools/counselor_nav.py` was removed.
- "The Flow": a narrated presentation of the whole process (Brian will make it). Listed at the top of Traditional Assessment ("The Flow: Start Here") and as a refresher on the Clinical Companion page ("Watch the Flow Again"), both "Coming". One presentation, two links. It replaces the flow chart inside the Companion.
- Still to do: `counselors/clinical-companion.html` still shows Foundations 1 to 3 and the Flow of Care chart link; Brian wants the Companion to start at step 1, Telephone Intake. Headings inside kept pages and the landing page still say "Counselors' Room".
- Nov 12 (later): Brian chose to keep the name "Counselors' Room" (ROOM in the build script; the folder is still `members/`). The visitor Introduction page (`counselors/landing.html`) stays.
- Flow of Care slide show, DRAFT for Brian's review: `counselors/presentations/flow-of-care/index.html`. 16 slides (overview, the 14 steps starting at Telephone Intake, summary). Each slide shows the flow with the current step lit, on-screen points, the narration script as text, and clickable documents for that step ("coming" where a document does not exist yet). No voice-over yet, at Brian's request: after he approves the script, add `audio/slide-00.mp3` ... and set AUDIO = true in the file, then remove the gold draft strip. Linked from "The Flow: Start Here" (Traditional Assessment) and "Watch the Flow Again" (Clinical Companion page).
- Step 2 on the slides follows Brian's Nov 12 outline (basic information, consent, insurance, confidentiality, release of records, Adult History, Life Events screening before the first visit). This differs from the Nov 9 note in `app/library/flow-of-care.md` (About You and Brief History only; Life Events after the first session). Ask Brian which is right.
- Telephone Intake Form (revised from Brian's 2014 form, approved Nov 12): `counselors/forms/Belief-Counseling-Telephone-Intake-Form.docx` and `.pdf`. Linked from the Telephone Intake slide and from Traditional Assessment (Telephone Intake Form; Screen & Refer is Section 4 of the form).
- On-screen Telephone Intake Form: `counselors/forms/telephone-intake.html` (type in, tick boxes, Hold this form = kept in the browser on that computer only, Print or save as PDF, Clear for a new caller; the counselor's referral list stays on the computer). Two boxes of national numbers at the top, checked Nov 12, 2026: Safety Numbers, and Other National Help Lines (not emergencies). National numbers only, at Brian's request. The Word/PDF copies carry the same numbers on page 3 (built by a script kept outside the repo; ask Claude to regenerate). Later, in the Clinical Companion, the form should save into the client's file instead of the browser.
- Telephone intake hand-off: Brian's counselors will have the intake person and the counselor on different computers, so the form must reach the Clinical Companion through the secure connection (not built yet). What the form sends and what the connection must do is written up in `app/TELEPHONE-INTAKE-HANDOFF.md`. Until then the intake person prints or saves the PDF.
- The Telephone Intake slide carries a reminder button for Brian, "hand-off to the Clinical Companion" (`counselors/forms/telephone-intake-handoff.html`, a web copy of the write-up). Remove that button before the slide show is shown to counselors.
- Nov 12 (later): Brian does not want the national numbers on printed copies. They show only on screen at the top of the on-screen form (hidden when printing); the Word/PDF copies are back to two pages without them.
- Telephone Intake referral list is 14 spaces (was 16), at Brian's request; the on-screen form now prints on two pages.
- Nov 12 (later): on the on-screen Telephone Intake Form the two boxes of national numbers are at the bottom (Brian's request), with a one-line 911/988 notice at the top that jumps down to them.
- Printable Flow of Care chart (`counselors/forms/Clinical-Companion-Flow-of-Care.pdf`) now starts at step 1, Telephone Intake: the three Foundations boxes are gone (Brian, Nov 12). Rebuilt by `python3 tools/build_flow_chart.py` (needs cairosvg); edit STEPS there. Step 2 still reads "About You and Brief History" pending Brian's answer on the intake forms.
- On-screen consent forms (Nov 12): `counselors/new-client-forms.html` now has an "Agreements and Consent Forms" group with six forms to read and sign on screen (Informed Consent, Confidentiality Agreement, Notice of Privacy Practices acknowledgment, Financial Policy, Telehealth Consent, Good Faith Estimate), worded from sections 4 to 9 of the New Client Packet. Adults only, so the packet's children/teens part and guardian signature lines are left out; the drafting notes in brackets ("check your state board rules") are left out; practice placeholders like [Practice Name] stay. Still a practice sample: nothing is saved or sent. Edit the wording in `tools/add_consent_forms.py` and run it. Still to add: Release of Information and the Client Handbook (Brian has his own on his PC).
- Consent forms: each one now has a signature box the client signs with a mouse or finger (required), plus a printed name and date. The signature shows in the counselor view. Added by `add_signature_pad` in `tools/add_consent_forms.py`.
- Flow chart step 2 updated (Nov 12): About You and Brief History, plus the agreements and consent forms signed on screen.
- Brian decided (Nov 12): before the first visit the client completes About You, the Brief History (not the full Adult History), and the Life Events & Beliefs Screening, then signs the consent forms. The screening is now form 3 on `counselors/new-client-forms.html`. The flow chart, the slide show, the Traditional Assessment page and `app/library/flow-of-care.md` all say this.
- Nov 12 (evening): another helper (Cursor Agent, merged as pull request #19) added the RSS-5 and Brief RCOPE to the Clinical Companion's client record as optional spiritual screens (`app/js/spiritual-screens.js`; its 5 checks pass with `node --test app/test/spiritual-screens.test.js`). The SAI is not included. Claude then updated the Counselors' Room Process page, the flow chart (step 9) and the slide show so none of them say "coming" for these any more. Brian wants the spiritual assessment tools to be optional.
- SAI (Spiritual Assessment Inventory) is listed again on the Process page, flow chart and slide as "waiting for author permission" so it is not forgotten; Brian plans to ask the author.
- Nov 12 (evening): the Counselors' Room now links to the visitor Introduction (`counselors/landing.html`, "Start here: Introduction" on the Welcome page) and to Membership (`counselors/membership.html`, on the Welcome page and in the menu). The Introduction gained a "How to find your way around" section; the Membership page's "What membership includes" list now matches the six sections. Flow: public menu "Counselors" -> Wix page /blank-11 -> visitors (not logged in) see the Introduction with Start your free week / See what's inside / Log in; logged-in members go straight to the room's Welcome page. Brian did not see the Introduction or sign-up because he is logged in.
- Clinical Companion unlock screen: "Forgot your passphrase?" (Nov 12). A passphrase cannot be recovered; the option erases the encrypted records in that browser after a ticked confirmation, then shows Create a passphrase again (`eraseVault` in `app/js/vault.js`). Added because Brian forgot his.
- Clinical Companion: recovery key and backup reminder (Nov 12, 2026, at Brian's request after he lost his passphrase). NOTE FOR ANY OTHER HELPER WORKING IN `app/`: the stored envelope is now version 3. Records are encrypted under a random data key; that key is stored wrapped twice, under the passphrase and under a 25-character recovery key shown once at setup (`app/js/vault.js`, see the comment at the top). New functions: `recoverVault`, `renewRecoveryCode`, `takeNewRecoveryCode`, `hasRecoveryKey`, `sealV3`, `openV3`, `eraseVault`. `session.salt` no longer exists. Version 2 vaults are upgraded on first unlock and version 2 backups still restore. Changing the passphrase keeps the recovery key; using the recovery key issues a new one. Unlock screen: "Forgot your passphrase?" offers the reset form, with erase-and-start-over as the last resort. Settings has "Create a new recovery key". Home shows a backup reminder when no backup was downloaded in 14 days (`lastBackupAt` in the browser's prefs). Checks: `node --test app/test/recovery.test.js` plus a 29-step browser run (all passed). When records move to the secure server, email reset can replace this.
- Nov 13: visitor Introduction (`counselors/landing.html`): "Back to the Public Site" is now a button at the top left of the page; the line under the two main buttons is just "Already a member? Log in", centered (Brian looks at the top for a way back).
- Nov 13: Brian asked to try the menu without the gold "Clinical Companion" button (he kept reading gold as "the page I am on"). It is now a plain menu item on every page. In the room's own pages the current section is shown in bold gold text with a thicker gold underline. The Clinical Companion box on the Welcome page is unchanged.
- Nov 13: pages in the Counselors' Room (the room's six pages, the kept counselors/ pages with the menu, and the Introduction) now bring the Wix page back to the top of the embed when reached from another of our pages (a short script using scrollIntoView; it does nothing on the first load from Wix). Fixes "See what's inside" landing at the bottom of an empty-looking page. Tested in a simulated Wix page. The Introduction's "See what's inside" now links straight to members/index.html.

- Nov 16 (4:50 PM): Home page had lost the shared Wix header (menu) and footer (they were removed from the Home page between site revisions 448 and 449); re-added via the header/footer "Add to More Pages" > Home. Beliefs? page had lost its embed section; re-added by copying section8 from Belief Counseling? and setting it to pages/beliefs.html (heights 3450 / 4300 / 4600). Published.

## Weekly Professional Tips (Nov 17, 2026)
- List page: `counselors/weekly-tips.html` (linked from the room's Professional Tips page, `members/tips.html`, edited by hand because `tools/build_members_room.py` no longer matches the live menu, e.g. it lacks Scripture Lookup; the script got the same item). Tips are in the TIPS list at the bottom of the page: n, title, desc, file, show (date it appears), free.
- Tip pages: `counselors/tip-sex-in-counseling-room.html` (Tip 1) and `counselors/tip-demonic-possession.html` (Tip 2). Both are free samples, open to everyone.
- Lock: the page asks the Wix page (postMessage `{type:'cc-member-status?'}`) whether the visitor is a logged-in member; the For Counselors page code answers `{type:'cc-member-status', member:true/false}`. No answer = visitor view. Members-only tips are locked in the list, but a members-only tip's own page must NOT be put on GitHub (public); store its text in a members-only Wix collection when Tip 3 comes.
- Emails: one Wix Email Marketing draft per tip (free plan: Brian opens the next draft each week and clicks Send). The email shows the opening, a short list, and a "Read the full tip" button.
- Nov 17 (later): Professional Tips simplified at Brian's request. The menu's Professional Tips (`members/tips.html`) now forwards straight to the list, `counselors/weekly-tips.html` (titled "Professional Tips"). The list has topic buttons (All + every topic used) and a topic label on each tip ("topics" in the TIPS list). The ethics tip ("Ethical Considerations When Choosing Treatment Modalities") is now Tip 3, members-only (Brian's choice); the old hub, `counselors/tips.html` (Introduction) and `counselors/tips-ethics.html` are no longer linked. Case Studies and Theory are linked under "More from Dr. Campbell" at the bottom of the list. Next emailed tip is Tip 4.
- NOT YET SECURE: members-only tips are locked in the list only. Their pages (e.g. `counselors/tip-ethics-treatment-modalities.html` and its PDF) are still public files on GitHub that anyone with the exact address could open. To do: keep members-only tip text in a Wix collection that only paying members can read (backend web method checking the plan), and remove those files from GitHub.
- Nov 17 (later): MEMBERS-ONLY TIPS ARE NOW PRIVATE. Their pages live in the Wix CMS collection `ProTips` (read/write: Admin only; item id = tip name, fields title + html), NOT on GitHub. Backend `backend/cc-membership.web.js` has `getMembersTip(slug)`: returns the HTML only to an admin or a member with an ACTIVE Clinical Companion plan. The For Counselors page code answers `cc-tip?` with `{type:'cc-tip', slug, ok, html}`. Viewer: `counselors/members-tip.html?t=<name>` (shows a lock + join/log-in if refused). Email link: /blank-11?tip=members-tip&t=<name>. In ProTips now: tip-ethics-treatment-modalities (Tip 3; PDF removed), tip-dont-believe-everything (Tip 4), tip-insurance-company-dilemma (Tip 5, now titled "The Insurance Company Nightmare!", office video embedded from YouTube qj7N0l-07zs because counseling4christians.com will close). `counselors/tip-ethics-treatment-modalities.html`, `tips.html` and `tips-ethics.html` are now forwarders. Older copies remain in the git history.
- To add a members-only tip: insert an item in ProTips (Wix data items API, or the CMS in the dashboard), add its line to TIPS in weekly-tips.html with file "members-tip.html?t=<name>", and make its email draft.
- Nov 17 (later): The Process page (`members/process.html`): the Introduction video stays public; lessons 2-4 (Identify, Challenge, Replace) are members-only. Their MP4s were moved to the Wix media library and removed from GitHub; their players are stored in ProTips as video-lesson-2-identify, video-lesson-3-challenge, video-lesson-4-replace. The page shows a lock with Start your free week / Log in, and for members asks the For Counselors page code (cc-member-status?, then cc-tip?) for each player. NOTE: the script and lock CSS were added to members/process.html by hand; `tools/build_members_room.py` writes the locked placeholders but NOT the script, so re-add it if the page is rebuilt.
- Nov 17: Tips 6 (tip-pastors-daughter) and 7 (tip-stripper-and-keys) added to ProTips, members-only, topics Case Study + Trauma & Dissociation. Brian wants provocative tip titles.
- Nov 17: Tip 8 "The Narcissistic Pastor and the Myth of Non-Directive Therapy" (ProTips id tip-narcissistic-pastor), members-only, topics Case Study + Personality Disorders. Scripture written out (BSB) instead of counseling4christians links.
- Tip 8 email draft: 414d8226-4742-4390-bccb-85b28775c851
- Nov 17: Tip 9 "Non-Directive Therapy Killed John" (ProTips id tip-nondirective-therapy-killed-john), members-only, topics Case Study + Counseling Approach. Includes a safety box for the domestic-violence question.
- Email drafts: Tip 9 f879cdef-8d0d-4e15-a260-a3394a10f17c; Tip 3 ce404a6b-914a-41a8-8205-4f935b82f101 (all 9 tips now have a draft).
- Nov 17: Tip 10 "Did God Do This to Me? Free Will, Pain, and Suffering" (ProTips id tip-free-will-pain-suffering), members-only, topic Faith & Suffering. Email draft 666b7056-7831-42a4-ac26-024746637dcf.
- Nov 17: Tip 11 "The Bible Is the Best Mental Health Textbook Ever Written" (ProTips id tip-bible-mental-health-textbook), members-only, topic Christian CBT. Email draft 2529aa1b-2d50-4cf4-93cd-9f2f4561e499. Brian may send a link for his "Power of Truth" video/chapter.
- Nov 17: Tip 12 "Did We Teach Her This? A Case of Gender Dysphoria" (ProTips id tip-did-we-teach-her-this), members-only, topics Case Study + Children & Families. Church references removed at Brian’s request. Email draft 90d6f493-c2d7-43ad-b2ac-c9b6dfc8e09d.
- Nov 17: Tip 13 "The Lies Your Clients Tell Themselves" (ProTips id tip-lies-clients-tell-themselves), members-only, printable worksheet, topics Tools & Worksheets + Christian CBT. Email draft 75811adb-26a5-4431-b43b-a48301e8a288. Brian may send a permanent link for his "Self-Esteem" chapter.

## Sign-up switched off before launch (Nov 17, 2026)
- Brian is not ready to launch. Visitors may look around the Counselors' Room, but cannot sign up.
- Every sign-up button now reads "Membership opens soon" (a non-clickable `span.btn.soon`): membership.html (2, plus a gold "Membership is not open yet" note), landing.html (2, now "Membership Opens Soon", still linking to membership.html), weekly-tips.html, members-tip.html, members/process.html. "Log in" links still work.
- The Wix page code still handles cc-start-free-week, but no page sends it now. TO REOPEN: revert this commit (git revert) or put the old buttons back.
- Tip release schedule: decided Option B (members see upcoming titles, locked, with dates) and Tuesday mornings, but the start date waits until Brian launches. When set: give each tip a `show` date (Tip 3 first, weekly), show future tips locked with "Coming <date>", and make getMembersTip refuse tips before their date. Tips 1-2 stay free and are not emailed (delete their drafts ea772a90..., 933f0781... at that time).
- Nov 17: Price confirmed: plan e3d1c25e "Clinical Companion" is $14.95/month, no free trial (Brian scrapped the 7-day trial). Old plan 573fa67c ($29.95, 7-day trial) was deleted at Brian's request; only the $14.95 plan remains.
- Nov 17: Membership page now has a "Why join" list (unlimited Lie Finder searches, use with clients, practice the DSM-5-TR, weekly tip, teaching videos); duplicate Lie Finder card removed; Introduction membership paragraph lists the same highlights.
- Nov 17: Lie Finder uses Wix's built-in AI (PROVIDER = "wix" in lie-finder/wix-code/lieFinder.web.js), no API key or per-search charge. The Nov 1 note about missing secrets is out of date.
- Nov 18: Tip 14 "The Secret Thought Life of Christians" (Brian's title "Thinking About Thinking" is the subtitle; ProTips id tip-secret-thought-life), members-only, topic Christian CBT. Clickable verse numbers (popups), two YouTube videos embedded (mPnCuN6RpyA, Kdh1ZUMVh0I); old Drive, counseling4christians, CreateSpace links removed. Email draft 7d69bcbf-ee85-4ef0-9861-df2ced015916. Brian will join Amazon Associates; then add book links (Godly Counsel, Pearls) site-wide with the Amazon Associate disclosure.
- Nov 18: Tip 15 "Mr. and Mrs. Pitchfork" (Brian's Professional Tip #42, The Biological Basis of ADHD; ProTips id tip-mr-mrs-pitchfork), members-only, topics Biology & the Brain + The Counselor (both new). ADHD video embedded from YouTube iZduZXOvhOE (was on counseling4christians.com). American Gothic image replaced by a link to the Art Institute of Chicago (artwork 6565). Added "For counselors: what the story teaches" box. Email draft 0eb22c65-6d3f-4727-8b47-3964e068eecc.
- Nov 18: Tip 16 "Two “Harmless” Beliefs That Caused Me Great Pain" (Brian's Tip #2.5, personal testimony; ProTips id tip-two-harmless-beliefs), topics The Counselor + Christian CBT. Videos: testimony Typu1V29wyg, song "I Need a Savior" KXjS4ZmsKg8 (old counseling4christians MP3 replaced). Email draft d68bd2d9-edbb-4d27-b9b7-c1d0036def10.
- Nov 18: Tip 17 "The Man Who Talked Backwards" (Brian's Tip #10.1, Keep Things in Perspective; ProTips id tip-man-who-talked-backwards), topics The Counselor + Assessment. Course wording (COUN 667, Liberty, grades in this class) removed; "John" is a pseudonym and Dr. Robert Hickey is deceased (Brian OK'd both names). Email draft 66bde116-e16d-4e34-a95c-2e5dfe45b931.
- Nov 18: Tip 18 "Don’t Start with the Checklist!" (Brian's Tip #12.4, Assessment Caveats; ProTips id tip-dont-start-with-checklist), topics Assessment + Private Practice. Disclaimer adds the Joint Commission NPSG 15.01.01 suicide-screening note (Brian approved). Email draft f43ddeb2-96b6-4c9e-9580-8f9e01cda65b.
- Building members-only tips via API: build the page from Tip 15's stored head (keep the nav after </head>), and create email drafts with campaignEditorType {value:"MJML"} (an object, not a string).
- Nov 18: Lie Finder free trial (Brian's choice): visitors must log in free (Wix site member) and then get 3 free searches; site owner/admins and members with an ACTIVE "Clinical Companion" plan (e3d1c25e) search without limit. Live backend `backend/lieFinder.web.js` (which also holds findHelp, appended) now has `whoIsAsking()`, `lieFinderAccess()` and `findLies` = Permissions.Anyone with the checks; only searches that return results are counted. Counts live in the private CMS collection `LieFinderTrials` (_id = member ID, field count; all permissions Admin). False Belief Finder page code is public/pages/cfveb.js (copy: lie-finder/wix-code/page-code.js): sends `access` on load/login, opens Wix sign-up on `login`, goes to /blank-11 on `join`. app.html shows the trial notice (#trial). To change the number, edit FREE_SEARCHES in the backend (and the "3" fallback in app.html).
- Nov 18: Explained the belief cards' "Share this information" button (emails the lie, truth, Scripture and card link with its homework) on the Counselors' Introduction (About the Lie Finder), the membership "Why join" list, and under the Lie Finder plan buttons. Membership list also mentions the 3 free searches.
- Nov 18: Welcome page (members/index.html, edited by hand) has a 6th box, highlighted navy/gold (class "card cc"): "Scripture Lookup — Members get unlimited lookup of 2,500 counseling Scriptures, indexed in 170 topics." Links to /scriptures (target _top). Note: the Scripture Lookup page itself is not yet limited for non-members.
- Nov 18: Scripture Lookup free trial (Brian chose "limit it completely", 5 free): page /scriptures (Pearls Scripture Search, page code public/pages/ys820.js, edited in Wix only) calls `useScriptureLookup(topicId)` from backend/lieFinder.web.js in openTopic(). Not logged in -> topic shows a lock box and #learnMoreButton reads "Log in or sign up free" (promptLogin signup, then reopens the topic); limit reached -> "About membership" (/blank-11). Logged-in non-members see "Free trial: you have N of 5 free topic lookups left" above the topic. Distinct topics are counted in the private collection `ScriptureTrials`. Brian accepted that clients following "Related Pearls topics" links on the belief cards will also need a free login and hit the limit. NOTE: the PearlsTopics collection is still readable by anyone, so this is a page-level limit, not airtight. Wix code edits save through the editor's code models (Monaco) and were confirmed against the files API; Publish must be clicked by Brian.
- Nov 18: Free hidden "Reviewer (2 weeks, free)" pricing plan 5bc05d5f-005d-49ad-88b3-91cd1de583e7 (single payment $0 for 2 weeks, public:false, 1 per buyer) for people Brian invites to review the site. Reviewer link: https://www.beliefcounselor.com/blank-11?reviewer=bc-review-2026 (For Counselors page code ceafa.js: sign up/log in, then checkout.startOnlinePurchase of the Reviewer plan). The Reviewer plan counts as membership everywhere the paid plan does: masterPage.js, ceafa.js isMember, cc-membership.web.js getMembersTip, lieFinder.web.js whoIsAsking (Lie Finder + Scripture Lookup unlimited). Separate from Wix "Client Feedback" links (manage.wix.com/studio/client-feedback; visitor view, 2-week link). Saving Wix code edits needs the Claude browser pane displayed (hidden/background tab did not save).
- Nov 18: Traditional Assessment page (members/assessment.html, edited by hand): The Flow, Training and Tutorial boxes now use the picture layout (item pic). Pictures: members/img/assessment-flow.jpg and assessment-tutorial.jpg (navy title cards made to match the Training slide; sources in work files, not kept) and the Training slide counselors/presentations/diagnostic-process/slides/slide-01.jpg. Pictures are clickable.
- Nov 18: Brian does not want clients filling forms on the site (no client data collection). The on-screen release form was reverted. Instead: downloadable sample counselors/forms/Belief-Counseling-Release-of-Confidential-Information.docx + .pdf (Telephone Intake style: logo, Georgia, navy/gold, cream labels; page 3 = "For the Counselor" disclaimer + considerations; builder tools/build_release_form.js, needs logo.png beside it), listed on members/assessment.html under Online Assessment after Client forms. Open question for Brian: the Online Assessment section and "Open the client forms" still describe on-screen client forms.
- Nov 18: Traditional Assessment "Online Assessment" section replaced by "Sample Intake Forms" (downloads only): Telephone Intake Form (PDF/Word), New Client Packet (9-page fillable PDF), Life Events & Beliefs Screening (PDF + on screen), Confidentiality Agreement, Pastoral Confidentiality Agreement, Release of Confidential Information (PDF/Word); Schedule First Appointment still "Coming". The on-screen counselors/new-client-forms.html is no longer linked from the room (file kept). Flow of Care slide 2 documents now list the New Client Packet PDF and the release form instead of the on-screen forms (slide text/narration unchanged).
- Nov 18: Brian wants downloads only, not fillable. New counselors/forms/New-Client-Packet.pdf = the fillable packet flattened (no form fields), with the page-1 welcome text changed to "Please print it, fill it in, and bring it with you" and the page-2 photo note changed to "Please bring your insurance card(s) and photo ID to your first session so they can be copied." Links switched from New-Client-Packet-fillable.pdf (file kept).
- Nov 18: Confidentiality-Agreement.pdf and Pastoral-Confidentiality-Agreement.pdf = plain (flattened) copies of the fillable versions; all links switched (assessment, practice-forms, Flow of Care). Only counselors/new-client-forms.html (no longer linked) still refers to fillable files.
- Nov 19: Flow of Care step 13 "Search the belief cards" now opens /false-belief-finder (Counselors' Room Lie Finder), not the public /search-false-beliefs. lie-finder/app.html now carries the Counselors' Room menu at the top (copied by hand from counselors/help.html; Lie Finder pill is the current page). tools/update_counselor_nav.py does NOT update it; if the room menu changes, copy the <!--nav--> block into app.html too.
- Nov 19: Removed the shared Wix header from the False Belief Finder page only (header ... menu > Remove from Page) and published, so the Lie Finder looks like it is inside the Counselors' Room (like /blank-11). To bring it back: select the header on another page > Add to More Pages.
- Nov 19: Brian's choice: on the site only the 2 free sample tips can be read (by everyone, members too); all other tips show title + short description only (locked; members see 'Sent by email', visitors 'Members only'). Full tips go to members by weekly email. New intro wording for visitors: 'A new tip from Dr. Campbell each week. Members receive each tip by email and can read the topics that will be sent in upcoming weeks.' Removed 'every past tip' wording from membership.html and members-tip.html. members-tip.html still opens a tip for a member who has its direct link (e.g., from an email).
- Nov 19: New Wix page "Counselor Scripture Search" at /counselor-scriptures = duplicate of Pearls Scripture Search (/scriptures, page code copied with it) with the shared header removed and a fixed-height (116px) top section holding iFrame #html2 = counselors/room-nav.html (the Counselors' Room menu by itself; links open the whole window via /blank-11?tip=room-<page>, stubs counselors/room-*.html redirect to members/*.html). All room "Scripture Lookup" links (counselors/*.html, members/*.html, lie-finder/app.html, build_members_room.py) now go to /counselor-scriptures (target _top). Public /scriptures unchanged. If the scripture page is edited, edit BOTH Wix pages. NOTE: tools/update_counselor_nav.py's MENU lacks Scripture Lookup; running it would drop that link.
- Nov 19: Each DSM-5-TR review now also has a web page counselors/reviews/<file>.html (room menu, navy/gold site style, ← Back = browser back or Traditional Assessment, link to the PDF). Built from each topic's .docx by python3 tools/reviews/build_review_html.py [topic] (run after build_review.py). Traditional Assessment list and reviews.html 'Open review' buttons go to the HTML pages (same frame, so Back works); the PDF stays for printing.

## Nov 19, 2026 — Counselor Scripture Search: description, phone layout, Email to Client (trial)
- /counselor-scriptures description rewritten (approved text). Font 18px desktop, 17px mobile; on the
  mobile layout the two book pictures were moved below the text (Y 910, section height 1160).
- "Email to Client" button (now on every topic; was a trial on ABORTION): Wix embed #html4 in the stack under #detailBox shows
  counselors/email-client-button.html; page code sends a mailto (subject "Scriptures from our session",
  body = topic Scriptures). Wix text links can't carry an email body, hence the embed.
  Page code copy: tools/wix/counselor-scriptures-page.js. To turn on for all topics: EMAIL_ALL = true.

## Nov 21, 2026 — Library Forms page
- The Counselors' Room Library has a fourth card, Forms, opening counselors/forms-library.html. It lists practice forms and belief worksheets already in the repo, with print and download links. Books, Videos, and Articles were not changed.

## Nov 21, 2026 — Life Events & Beliefs Screening is a print form
- Life_Events_Beliefs_Screening.html is now a blank form for counselors to print or download (Life_Events_Beliefs_Screening.pdf) and give to a client. The clickable boxes, typed notes, and Clear button are gone. Other worksheets are unchanged.

## Nov 20, 2026 — SEO plan Jobs 1–4
- Job 1: The Wix site display name is now "Belief Counseling", so page titles end in "| Belief Counseling".
- Job 3 and indexing: The site-wide noindex was removed and sitemap.xml now works. Members-only and unused pages are hidden from Google (page-level noindex on /blank-11, /false-belief-finder, /counselor-scriptures, /blank-12 through /blank-17, /clinical-companion, /challenges, Adult History, four online-program pages, and Plans & Pricing).
- Job 2: Google Search Console is connected and verified, and the sitemap was submitted.
- Job 4: Eight public addresses were renamed and published, with a 301 redirect from each old address. /blank-3 is /questioning-beliefs. /blank-4 is /spiritual-religious. /blank-5 is /behavioral-experiments. /blank-7 is /psychological-cognitive-false-beliefs. /blank-8 is /interpersonal-false-beliefs. /blank-9 is /socioeconomic-false-beliefs. /blank-10 is /sociocultural-false-beliefs. /blank is /sociocultural. Links in this repository were updated to the new addresses. /blank-6 and /blank-11 through /blank-17 were left as they are. The Sociocultural embed still accepts /blank as a fallback.

## Nov 20, 2026 — Counselors' Room: Assessment label and Disorders tab
- The room menu item "Traditional Assessment" is now "Assessment". The page, the link, and ?tip=room-assessment are unchanged. The Welcome card uses the same shorter title.
- A new menu item, Disorders, sits right after Assessment. It opens ?tip=room-disorders (counselors/room-disorders.html), which shows members/disorders.html. The page heading is "DSM-5-TR Disorders". The reviews list is the same Major DSM-5-TR Disorders card that stays on the Assessment tab; members/disorders.html is built from that card (members/dsm-reviews-card.html) so the two lists match. Review links work the same way. Back on a review uses the browser's back button when you opened it from Disorders, and otherwise returns to Assessment.
- The Assessment tab still shows the reviews card, unchanged apart from the menu.

## Nov 20, 2026 — SEO plan Jobs 5–6
- Job 5: Custom search titles and descriptions were put on 23 public Wix pages. Those titles and descriptions are live.
- Job 6: Picture descriptions (alt text) were added to 12 images in the Wix editor and 3 in this repo. The leftover “This is a Custom Element” placeholder was removed on /questioning-beliefs. Decorative images were skipped.
## Nov 21, 2026 — Release of Confidential Information revised (HIPAA 45 CFR 164.508)
- Brian re-sent his 2024 sample release and asked for it revised for the website. Rebuilt the Word + PDF
  (same file names, same links on Traditional Assessment and the Flow of Care slide): added who may release,
  other names, two-way option, records date range, specially protected info (alcohol/drug, HIV, genetic) with
  initials, psychotherapy-notes exclusion, how shared, default end of one year, required statements
  (revoke, treatment not conditioned, redisclosure, copy), representative's relationship, revoked-on line.
  Removed "Session notes" and the limits-of-confidentiality section (belongs in the Confidentiality Agreement;
  "minimum necessary" doesn't apply to authorized releases). Counselor page notes expanded.
  2 pages + counselor page. Builder: tools/build_release_form.js (logo.png beside it).

## Nov 21, 2026 — Professional Tips 19 and 20 (members-only, ProTips)
- Tip 19 "The Woman Who Was Locked in a Box" (Brian's Tip #15, Schizophrenia; ProTips id tip-woman-locked-in-box), topics Case Study + Psychosis (new). Cuba is Brian's deliberate disguise (doc also said Costa Rica). counseling4christians and schizophrenia.com links replaced with NIMH. Added "For counselors" command-hallucination safety box (988) and link to Tip 2. Email draft 21a3083f-5b3c-4b9f-8379-c287981c987b.
- Tip 20 "The Man Who Thought He Caused Pearl Harbor" (Brian's Tip #16, catatonia + freeze commentary; ProTips id tip-man-pearl-harbor), topics Case Study + Psychosis + Biology & the Brain. 1944 -> 1941 (Brian OK'd), 36 years to 1977; "carrier" -> "Navy ship"; antelope video YouTube sYEQQeCZ0O4 (Brian's link); Psychology Today freeze article linked; DSM-5 "with catatonia" note. Email draft 97daf9ea-f0d9-4151-bbe2-a4d198dcdc49.
- Built from the current weekly-tips.html head + nav (Assessment/Disorders/counselor-scriptures), not the older Tip 15 head. Local builder (not in repo, members-only): /home/claude/tips/build.py.

## Nov 23, 2026 — Clinical Practice Guidelines page
- Brian sent "Belief Counseling Clinical Practice Guidelines" + 8 avatar training scripts. Guidelines built as counselors/guidelines.html (builder /home/claude/tips/build_guidelines.py): central principle, 11 guidelines at a glance (jump links), each with Identify/Challenge/Replace tag, In practice, Try saying, one BSB verse (checked with tools/verse.py), "Training video N (coming soon)"; Avoid/Try-instead table, Quick Check, For Students box, further reading (added Norcross & Lambert 2019, Bennett-Levy 2004, Worthington 2006, Pargament 2007). Added 988/duty-to-report to risk, PHQ-9/GAD-7 example.
- Card added on members/belief-counseling.html (picture members/img/clinical-guidelines.jpg). Not in the top menu yet (Brian may want a "Guidelines" menu item).
- Nov 23: RSS-5 and Brief RCOPE are now printable forms on The Process page (`members/process.html`, Spiritual Assessment Tools): `counselors/forms/Belief-Counseling-RSS-5.html|pdf` and `Belief-Counseling-Brief-RCOPE.html|pdf`, built by `node tools/build_spiritual_forms.mjs` from the verbatim items in `app/js/spiritual-screens.js` (items re-checked against both open-access articles; CC BY credit kept on each form). SAI stays "Coming" (author permission pending). Brian was given a free counselor membership (offline paid order eacbe9fa on plan e3d1c25e) so he can see the members-only Process videos.

## Nov 23, 2026 — Guidelines in the Counselors' Room menu
- New menu item "Guidelines" between The Process and Assessment, on all 52 pages that carry the room menu (and counselors/room-nav.html, used by /counselor-scriptures). It opens counselors/guidelines.html; ?tip=room-guidelines goes there through counselors/room-guidelines.html. On the guidelines page, Guidelines (not Belief Counseling) is now the highlighted menu item. The card on the Belief Counseling page stays.
- Members-only tips stored in the Wix ProTips collection still carry the older menu (no Guidelines) until they are rebuilt.

## Nov 23, 2026 — Grief and Loss guidelines (draft for Brian's review)
- Brian wants specialty guidelines for Grief (loss of a loved one), Trauma (incl. PTSD), and Abuse (sexual or physical). Doing Grief first for his review, then Trauma and Abuse in the same format.
- counselors/guidelines-grief.html, built by tools/guidelines/build_grief.py (reuses head/styles/menu of counselors/guidelines.html). 10 guidelines, PGD DSM-5-TR criteria box, false-belief table linked to the Grief and Loss belief cards (Inter-046–050) and Belief-079/080, missteps table, Quick Check, For Students, 8 APA references with DOIs (checked). Verses checked with tools/verse.py.
- NOT yet linked from the menu or the general guidelines page. Review link: beliefcounselor.com/blank-11?tip=guidelines-grief. Plan once approved: a "Specialty guidelines" box on counselors/guidelines.html linking Grief, Trauma, Abuse.
- Nov 23 (later): Brian approved the Grief page. counselors/guidelines.html now has a "Specialty Guidelines" box (id="specialty", cards in div.spec, edited by hand; the general page's builder is not in the repo) linking guidelines-grief.html.
- Trauma and Abuse pages (now listed in the Specialty box too, Nov 23, so Brian can find them; still awaiting his review): counselors/guidelines-trauma.html (tools/guidelines/build_trauma.py) and counselors/guidelines-abuse.html (tools/guidelines/build_abuse.py), both using tools/guidelines/common.py. They link to the PTSD cards Psych-050–060 and abuse cards Psych-061–069, Core-022, Belief-096, Belief-038. Abuse page has a hotline box (911, 988, NDVH, RAINN, Childhelp, Eldercare Locator). Review links: ?tip=guidelines-trauma and ?tip=guidelines-abuse. When approved, add two cards to div.spec on guidelines.html.
- Nov 23 (2:10 PM): Brian asked for the specialty guidelines to go BELOW the general ones, numbered 12–14. The Specialty box was removed from counselors/guidelines.html; Grief (12), Trauma and PTSD (13), Abuse (14) are now cards 12–14 in the "Guidelines at a Glance" grid (jumping to #sp-grief, #sp-trauma, #sp-abuse) and numbered sections after guideline 11, each with a summary, the list of its 10 guidelines, and an "Open the full … guidelines" button to its own page. Edited by hand.
- Nov 23: avatar scripts Presentations 9–11 (Grief, Trauma, Abuse) added to the scripts doc (claude.ai/artifact/H2SNaKuYaNEvbWNx6zcCjL); sections 12–14 on guidelines.html now say 'Training video 9/10/11 (coming soon)'.

## Nov 23, 2026 — Training video 1 (Guideline 1) live
- Made in HeyGen AI Studio, project/video id 7b3eaa3d32854ff2a6a27363f6255776 ("Guideline 1 - Relationship Before Challenge", 2:14). Scene 1 = Julian (Julian Office 8, Turbo/Avatar 6) speaking the opening; scenes 2-9 = no avatar, picture set as background ("Set as BG"), same voice Paul - Serious. Cost about 3 credits (Creator plan, ~100 left).
- Pictures: counselors/videos/g1/P1-0*.png (built in /home/claude/avatar/p1.py + make_slides.py). HeyGen's page cannot fetch from github.io (CSP), so the same pictures were drawn in-page with canvas JS and pushed into HeyGen's My Media file input (input[type=file] index 3 on the Media > My Media panel).
- The built-in Claude browser cannot save downloads to Brian's computer; that is why the video is embedded from HeyGen rather than hosted here.
- On counselors/guidelines.html, guideline 1's "Training video 1 (coming soon)" is replaced by an embedded player (div.gvid, iframe https://app.heygen.com/embeds/7b3eaa3d32854ff2a6a27363f6255776). Share setting: anyone with the link.
- For videos 12-14 use Julian Living Room 4 look (softer setting).
- Nov 23: Pearls abortion card (pearls/abortion.html) set as the model for all Pearls cards: verses back in Georgia 17px (Arial removed), "Commentary" links now go to David Guzik's Enduring Word chapter pages (all 10 checked), note under the box updated. Rules for converting the other Pearls cards are in PEARLS-CARD-STYLE.md (for Grok or any helper).
