"""Build Depression cards 32–40 on the Core-001 / Psych-031 template, and add the
Overcoming Anxiety player to card 31. Run from the repo root:
    python3 tools/make_depression_cards.py
"""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT/'tools/music-catalog.json').read_text())
GC = json.loads((ROOT/'tools/godly-counsel-chapters.json').read_text())
PEARLS = json.loads((ROOT/'tools/pearls-topics.json').read_text())
DEP = 'https://music.wixstatic.com/mp3/dbdded_149606a27908493da01ac9492fb18ab1.mp3'
ANX = 'https://music.wixstatic.com/mp3/dbdded_f67d414544534727acf6973d58189443.mp3'
GCB = 'https://doctorishome.github.io/belief-therapy-tool/belief-cards/godly-counsel/'
PB = 'https://www.beliefcounselor.com/scriptures?topic='
CRISIS = ' If you are thinking about ending your life, call or text 988 in the United States, or tell someone near you right away.'
STEP_CRISIS = 'Choose steps you can do safely. If you are thinking about ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone.'
STEP_MILD = 'Choose steps you can do safely. If this belief comes with hopelessness or thoughts of ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone.'

V = {
 'Psalm 30:5': 'For His anger is fleeting, but His favor lasts a lifetime. Weeping may stay the night, but joy comes in the morning.',
 'Lamentations 3:22–23': 'Because of the loving devotion of the LORD we are not consumed, for His mercies never fail. They are new every morning; great is Your faithfulness!',
 'Psalm 147:3': 'He heals the brokenhearted and binds up their wounds.',
 'Isaiah 41:10': 'Do not fear, for I am with you; do not be afraid, for I am your God. I will strengthen you; I will surely help you; I will uphold you with My right hand of righteousness.',
 'Romans 15:13': 'Now may the God of hope fill you with all joy and peace as you believe in Him, so that you may overflow with hope by the power of the Holy Spirit.',
 'Romans 8:28': 'And we know that God works all things together for the good of those who love Him, who are called according to His purpose.',
 'Galatians 6:9': 'Let us not grow weary in well-doing, for in due time we will reap a harvest if we do not give up.',
 'Proverbs 24:16': 'For though a righteous man may fall seven times, he still gets up; but the wicked stumble in bad times.',
 'Philippians 1:6': 'Being confident of this, that He who began a good work in you will carry it on to completion until the day of Christ Jesus.',
 '1 Peter 5:7': 'Cast all your anxiety on Him, because He cares for you.',
 'Isaiah 49:15–16': '‘Can a woman forget her nursing child, or lack compassion for the son of her womb? Even if she could forget, I will not forget you! Behold, I have inscribed you on the palms of My hands; your walls are ever before Me.’',
 'Zephaniah 3:17': 'The LORD your God is among you; He is mighty to save. He will rejoice over you with gladness; He will quiet you with His love; He will rejoice over you with singing.',
 'Psalm 34:18': 'The LORD is near to the brokenhearted; He saves the contrite in spirit.',
 'Romans 8:38–39': 'For I am convinced that neither death nor life, neither angels nor principalities, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.',
 'Romans 8:1': 'Therefore, there is now no condemnation for those who are in Christ Jesus.',
 '2 Corinthians 5:17': 'Therefore if anyone is in Christ, he is a new creation. The old has passed away. Behold, the new has come!',
 'Psalm 139:14': 'I praise You, for I am fearfully and wonderfully made. Marvelous are Your works, and I know this very well.',
 'Ephesians 2:10': 'For we are God’s workmanship, created in Christ Jesus to do good works, which God prepared in advance as our way of life.',
 'Romans 5:8': 'But God proves His love for us in this: While we were still sinners, Christ died for us.',
 'John 15:9': 'As the Father has loved Me, so have I loved you. Remain in My love.',
 '2 Corinthians 1:3–4': 'Blessed be the God and Father of our Lord Jesus Christ, the Father of compassion and the God of all comfort, who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves have received from God.',
 '1 John 1:9': 'If we confess our sins, He is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.',
 'Psalm 103:12': 'As far as the east is from the west, so far has He removed our transgressions from us.',
 'Micah 7:18': 'Who is a God like You, who pardons iniquity and passes over the transgression of the remnant of His inheritance— who does not retain His anger forever, because He delights in loving devotion?',
 'Deuteronomy 31:8': 'The LORD Himself goes before you; He will be with you. He will never leave you nor forsake you. Do not be afraid or discouraged.',
 'Matthew 28:20': 'And teaching them to obey all that I have commanded you. And surely I am with you always, even to the end of the age.',
 'Psalm 23:4': 'Even though I walk through the valley of the shadow of death, I will fear no evil, for You are with me; Your rod and Your staff, they comfort me.',
}

def qv(ref):
    text = V[ref]
    if text.endswith('.'):
        text = text[:-1]
    return f'<q>{text}</q> <span class="ref">({ref})</span>.'

def audio(title, url, minutes):
    return f'''<h2>Listen: {title}</h2>
<div class="audio">
<p class="atitle"><a href="{url}" target="_blank" rel="noopener">{title}</a> <span>· Dr. Brian Campbell · {minutes}</span></p>
<audio controls preload="none" src="{url}">Your browser can’t play this here. <a href="{url}">Open the recording</a>.</audio>
<p class="aload" hidden>Starting the recording… it is a long one, so it may take a few seconds to begin.</p>
<p class="anote">Press play to listen here, or tap the title to open it on its own.</p>
</div>'''

def song(key, why):
    vid, title, art, kind, _ = CAT[key]
    return kind, f'''<a class="song" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener"><span class="thumb" style="background-image:url('https://i.ytimg.com/vi/{vid}/hqdefault.jpg')"></span><span class="txt"><span class="st">{title}</span><span class="sa">{art}</span><span class="sw">{why}</span></span></a>'''

def gc_link(n):
    title = GC[str(n)][0]
    slug = re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-')
    return f'<li><a href="{GCB}GC-{n:02d}-{slug}.pdf" target="_blank" rel="noopener">{title}</a></li>'

def ul(items):
    return '<ul>\n' + '\n'.join(f'<li>{x}</li>' for x in items) + '\n</ul>'

def patch_31():
    p = ROOT/'belief-cards/psychological/Psych-031-My-Situation-Is-Hopeless.html'
    t = p.read_text()
    if 'Overcoming Anxiety' not in t:
        block = '\n' + audio('Overcoming Anxiety', ANX, 'about 18 minutes') + '\n'
        old = '<p class="anote">Press play to listen here, or tap the title to open it on its own.</p>\n</div>\n\n<h2>Songs that speak truth to this belief</h2>'
        new = old.replace('<h2>Songs', block + '<h2>Songs', 1)
        if old not in t:
            raise SystemExit('card 31 audio anchor not found')
        t = t.replace(old, new, 1)
    old_li = f'<li><strong>Listening:</strong> The <a href="{DEP}" target="_blank" rel="noopener">Overcoming Depression audio</a> by Dr. Brian Campbell. Tap to play.</li>'
    new_li = f'<li><strong>Listening:</strong> The <a href="{DEP}" target="_blank" rel="noopener">Overcoming Depression audio</a> or the <a href="{ANX}" target="_blank" rel="noopener">Overcoming Anxiety audio</a> by Dr. Brian Campbell. Tap to play.</li>'
    if old_li not in t and 'Overcoming Anxiety audio' not in t:
        raise SystemExit('card 31 listening line not found')
    if old_li in t:
        t = t.replace(old_li, new_li, 1)
    p.write_text(t)
    print('patched 31')

# Each card: belief must match the list wording. songs are (catalog key, why).
CARDS = []

def add(**k):
    CARDS.append(k)

add(
 num=32, file='Things-Will-Never-Get-Better', belief='Things will never get better.', crisis=True,
 tagline='A moment that was not the whole future',
 origins='When a hard season goes on and on, the mind starts to treat today as a forecast. Illness that does not lift, grief that stays heavy, money that does not ease, or prayers that seem unanswered can teach a person to say, “It will always be like this.” Depression darkens that forecast, so the future looks closed before another day has been lived. The pain can be real. The prediction that nothing can ever improve is still a prediction.',
 teaches='Scripture does not call pain a small thing. It does say that a night of weeping is not the last word. The psalmist said weeping may stay the night, but joy comes in the morning. Looking at ruin, Jeremiah remembered that the Lord’s mercies never fail and are new every morning. These verses do not promise that tomorrow will be easy, or that every loss will be reversed on our timetable. They do say that God is not finished, and that a dark day is not proof the rest of life is dark.',
 key='Psalm 30:5', also=['Lamentations 3:22–23','Psalm 147:3','Isaiah 41:10','Romans 15:13'],
 self=['This is never going to change.','I have already seen the future, and it is more of the same.','Good days are over for me.','If it were going to get better, it would have by now.','There is no point in looking ahead.','Other people get relief. I will not.'],
 errors=[('Fortune telling','Deciding the rest of life will be like this hard day.'),('Overgeneralization','Turning one long problem into “nothing ever improves.”'),('Emotional reasoning','Feeling stuck and treating the feeling as a forecast.'),('Discounting the positive','Overlooking any mercy, help, or small change that has already come.')],
 questions=['What, exactly, do I believe can never change?','Has a hard season ever shifted later, even a little?','Am I reading the whole future from how I feel today?','What help or mercy am I leaving out of the picture?','What would I tell a friend who said their situation could never improve?','What is one day I can live without settling the whole future?'],
 replacement='A hard season is not the whole story. God can bring change I cannot see yet, and I can take the next day as it comes.',
 truths=['God can bring change I cannot see yet.','Weeping may last the night, and joy can still come.','I do not have to solve the whole future today.','Mercy has met me before.','I can ask for help while I wait.','A dark day is not a life sentence.'],
 pearls=['hopeless','depression-symptoms-of','troubles','joy','god-all-loving'], gc=[12,30,29],
 songs=[('storm','You can tell God the truth in a storm without pretending the storm is already over.'),('again','God has brought new mercy before, and He can do it again.'),('worn','Weariness can be said out loud while you ask God to restore you.'),('lives','Because Jesus lives, tomorrow is not already ruined.')],
 prompt='When the “it will never change” feeling came', moment='the future felt closed',
 example='Psalm 30:5 becomes: “<strong>Sarah</strong> can write: “This night is hard, and joy can still come in the morning.””',
 reading='hopeless', read_label='Hopeless',
 actions=[('<strong>Name the forecast.</strong> Write the sentence “Things will never get better,” then write what you actually know and what you do not know yet.','Name the forecast'),
          ('<strong>Remember one shift.</strong> Write two hard seasons that later eased, even partly. Read them when the forecast feels final.','Remember one shift'),
          ('<strong>Ask for one practical help.</strong> Tell one safe person what feels stuck, and ask for one specific kind of help this week.','Ask for one practical help'),
          ('<strong>Get help if the darkness includes wanting to die.</strong> If you are thinking about ending your life, call or text 988, or tell someone near you today.','Get help if you want to die')],
 prayer='Lord, this season feels endless. Remind me that a hard night is not the end of Your mercy. Help me live this day, and to ask for the help I need. Amen.',
 tracker='A moment that was not the whole future')

add(
 num=33, file='No-Use-Trying-Ill-Only-Fail-Again', belief='There’s no use trying. I’ll only fail again.', crisis=True,
 origins='Failure leaves a mark. A test, a job, a relationship, a habit, or a spiritual effort that collapsed can teach the next try to feel pointless before it starts. Depression adds a heavy voice: “You already know how this ends.” Quitting then feels like wisdom. It is often the lie protecting you from another disappointment, and it also keeps you from the very step that could go differently.',
 teaches='Scripture does not say that God’s people never fall. It says they do not have to stay down. “Let us not grow weary in well-doing, for in due time we will reap a harvest if we do not give up.” A righteous person may fall seven times and still get up. God, who began a good work, carries it on. These verses do not promise that the next try will be easy or that effort earns God’s love. They do say that one failure is not an order to stop.',
 key='Galatians 6:9', also=['Proverbs 24:16','Isaiah 41:10','Philippians 1:6','Psalm 147:3'],
 self=['I already know I will fail.','Trying just sets me up.','People like me do not get back up.','Effort is a waste.','If I do not try, at least I cannot fail.','I should quit before I am embarrassed again.'],
 errors=[('Fortune telling','Predicting the next try from the last failure.'),('Overgeneralization','Turning some failures into “I always fail.”'),('All-or-nothing thinking','Treating anything short of success as proof that trying is useless.'),('Emotional reasoning','Feeling defeated and concluding that effort cannot matter.')],
 questions=['What, exactly, am I afraid will happen if I try once more?','Have I ever tried again and had a different result, even a small one?','Is “I will only fail” a fact, or a way to avoid disappointment?','What would a smaller, safer try look like?','What does God say about falling and getting up?','Who could take one step with me?'],
 replacement='One failure is not a reason to stop. I can take the next small step, and God gives strength to get up again.',
 truths=['I can take one small step without guaranteeing the outcome.','Falling does not mean I cannot get up.','God strengthens me; I do not have to supply all the strength.','A past failure is information, not a verdict.','Quitting is not the same thing as wisdom.','I can ask someone to try with me.'],
 pearls=['depression-symptoms-of','thinking-healthy','help','hopeless','faith'], gc=[12,33,29],
 songs=[('voice','The voice that says you will only fail is not the voice of truth.'),('greater','God’s strength is greater than the failure in front of you.'),('battle','You can bring the next step to God instead of carrying the outcome alone.'),('victory','Getting up again belongs in the story. It is not proof you should quit.')],
 prompt='When the “why try” feeling came', moment='trying felt pointless',
 example='Galatians 6:9 becomes: “<strong>Sarah</strong> can write: “I do not have to grow weary and quit. God can bring a harvest if I do not give up.””',
 reading='thinking-healthy', read_label='Thinking, Healthy',
 actions=[('<strong>Shrink the try.</strong> Pick one step so small it can be finished today. Do it, and write what happened, not what you feared.','Shrink the try'),
          ('<strong>Separate one failure from “always.”</strong> List three things you have done that were not failures. Read the list when the lie speaks.','Separate one failure from always'),
          ('<strong>Borrow a little courage.</strong> Tell one safe person the step you are avoiding, and ask them to check on you after you take it.','Borrow a little courage'),
          ('<strong>Get help if giving up includes wanting to die.</strong> If you are thinking about ending your life, call or text 988, or tell someone near you today.','Get help if you want to die')],
 prayer='Lord, I am tired of failing, and I am tempted to stop. Give me strength for one honest step, and remind me that falling is not the end of Your work in me. Amen.',
 tracker='A step I took anyway')

add(
 num=34, file='Nobody-Really-Cares-About-Me', belief='Nobody really cares about me.', crisis=False,
 origins='People who were overlooked, criticized, or left to manage pain alone often decide that care is something other people receive. A busy family, a cold church, friends who drifted, or a depression that makes every face look indifferent can all feed the conclusion. Sometimes care was truly missing. The lie is the leap from “I have been missed” to “nobody, including God, really cares.”',
 teaches='Scripture says God’s care is not a mood and not a rumor. “Cast all your anxiety on Him, because He cares for you.” He says a mother may forget her child, and He will not forget you; your name is inscribed on His hands. He is near the brokenhearted. Nothing in creation can separate His people from His love in Christ. These verses do not deny lonely days. They deny that loneliness is the same thing as being uncared for.',
 key='1 Peter 5:7', also=['Isaiah 49:15–16','Zephaniah 3:17','Psalm 34:18','Romans 8:38–39'],
 self=['If anyone cared, I would be able to tell.','People only stay until they know me.','I am on my own. That is just how it is.','God has more important people to look after.','Asking for care would only bother someone.','No one would notice if I disappeared.'],
 errors=[('Mind reading','Deciding what others feel without asking them.'),('Overgeneralization','Turning some neglect into “nobody cares.”'),('Emotional reasoning','Feeling alone and concluding that I am unloved.'),('Discounting the positive','Setting aside the people and the mercies that have already shown care.')],
 questions=['Who has shown me care, even if it was imperfect?','Am I reading indifference into people who have not been told what I need?','What would “someone cares” have to look like before I could see it?','Have I let anyone close enough to care for me lately?','What does God say about His care for me?','Who is one safe person I could tell the truth to this week?'],
 replacement='Feeling uncared for is not the same as being forgotten. God cares for me, and I can let a safe person care for me too.',
 truths=['God cares for me, even when I cannot feel it.','Some people have cared, and some still can.','I can ask for care instead of assuming it will never come.','Loneliness is real, and it is not a verdict on my worth.','My name is not forgotten by God.','I do not have to carry this alone.'],
 pearls=['love-by-god','loneliness','god-all-loving','help','depression-symptoms-of'], gc=[17,12,24],
 songs=[('alone','God’s presence remains when you feel unseen.'),('stays','God does not leave when other people have.'),('who','Being cared for rests on God’s love, not on being impressive.'),('lovesme','Jesus’ love is not something you have to earn before it counts.')],
 prompt='When the “nobody cares” feeling came', moment='you felt unseen',
 example='1 Peter 5:7 becomes: “<strong>Sarah</strong> can write: “I can bring this worry to God, because He cares for me.””',
 reading='loneliness', read_label='Loneliness',
 actions=[('<strong>List the evidence of care.</strong> Write three times someone showed up, prayed, listened, or helped. Read the list when the lie says nobody.','List the evidence of care'),
          ('<strong>Tell one person what you need.</strong> Ask a safe friend, family member, or pastor for one specific thing, such as a call or a meal. Notice what they do.','Tell one person what you need'),
          ('<strong>Receive a small kindness.</strong> When someone offers help this week, say yes once, and write how it felt.','Receive a small kindness'),
          ('<strong>Bring the loneliness to God in a sentence.</strong> Each morning, pray 1 Peter 5:7 in your own words.','Pray the care verse')],
 prayer='Lord, I feel unseen. Teach me that You care for me, and give me courage to let one safe person care for me too. Amen.',
 tracker='A moment I was cared for')

add(
 num=35, file='Im-a-Complete-Failure', belief='I’m a complete failure.', crisis=False,
 origins='A harsh parent, a public mistake, a lost job, a broken marriage, or a faith that measured love by performance can turn one collapse into a name: failure. Depression then gathers every shortcoming into a single sentence about the whole person. The events may be real. Calling your entire self a complete failure erases what is still good, still growing, and still held by God.',
 teaches='Scripture tells the truth about sin and failure, and it refuses the final label. “There is now no condemnation for those who are in Christ Jesus.” Anyone in Christ is a new creation. God, who began a good work, carries it on to completion. A person may fall seven times and still get up. Failure at a task is not the same thing as being a failed person. God heals the brokenhearted. He does not introduce His children as complete failures.',
 key='Romans 8:1', also=['Philippians 1:6','2 Corinthians 5:17','Proverbs 24:16','Psalm 147:3'],
 self=['Everything I touch falls apart.','I am the reason things go wrong.','There is no point describing me any other way.','Successful people are a different kind of person.','God must be disappointed every time He looks at me.','I should stop pretending I can do anything well.'],
 errors=[('Labeling','Naming my whole self by my worst moment.'),('Overgeneralization','Turning some failures into failure at everything.'),('Mental filter','Counting what went wrong and ignoring what I have done well.'),('All-or-nothing thinking','If I am not a success in every area, I am a complete failure.')],
 questions=['What specific thing failed, and what did not?','Would I call a friend a complete failure for the same events?','What good work has God already begun in me?','Whose voice first called me a failure?','What would “a person who sometimes fails” sound like instead?','What is one area where I am still learning rather than finished?'],
 replacement='I have failed at things, and that does not make me a complete failure. In Christ I am not condemned, and I can begin again.',
 truths=['A failed task is not a failed person.','In Christ there is no condemnation for me.','God’s work in me is not finished.','I can get up after I fall.','I can be honest about mistakes without wearing them as my name.','I am still able to take a next step.'],
 pearls=['self-esteem-low','guilt-shame','thinking-healthy','depression-symptoms-of','love-by-god'], gc=[24,12,29],
 songs=[('wins','Grace, not your worst day, gets the last word.'),('name','God names you as His, not as your failure.'),('broken','God works through imperfect people. He does not wait for a flawless record.'),('amazing','Grace saves and keeps you. Merit was never the foundation.')],
 prompt='When the “complete failure” feeling came', moment='one mistake felt like your whole name',
 example='Romans 8:1 becomes: “<strong>Sarah</strong> can write: “I have failed, and in Christ I am not condemned.””',
 reading='self-esteem-low', read_label='Self-Esteem, Low',
 actions=[('<strong>Split the label.</strong> Write “I failed at ____.” Then cross out “I am a complete failure.” Notice the difference.','Split the label'),
          ('<strong>Ask for two true things.</strong> Ask one trusted person to name two ways you are not a failure. Write their words down.','Ask for two true things'),
          ('<strong>Repair one small thing.</strong> If a real mistake needs an apology or a fix, do that one thing this week. A repair is not a verdict.','Repair one small thing'),
          ('<strong>Read Romans 8:1 aloud</strong> each morning before you review what went wrong yesterday.','Read the no-condemnation verse')],
 prayer='Lord, I have failed, and I have turned the failure into my name. Remind me that there is no condemnation in Christ, and help me get up and take the next step. Amen.',
 tracker='A moment I was more than a failure')

add(
 num=36, file='Im-No-Good-I-Never-Have-Been', belief='I’m no good. I never have been.', crisis=False,
 origins='Some people hear “you are no good” so early that they cannot remember a time before it. Criticism, comparison, abuse, shame, or a home where love had to be earned can plant the sentence in childhood. Later mistakes seem only to confirm an old verdict. Depression treats the verdict as history: not “I did wrong,” but “I have never been any good.” That is a story about the whole past, and it leaves out how God made you and how He loves you.',
 teaches='The Bible is honest about sin, and it is also clear about creation and redemption. “I praise You, for I am fearfully and wonderfully made.” We are God’s workmanship, created in Christ Jesus. He is among His people, and He quiets them with His love. Christ died for us while we were still sinners, which means His love did not wait until we were “good enough.” Being no good in your own eyes is not the same thing as being worthless to God.',
 key='Psalm 139:14', also=['Ephesians 2:10','Zephaniah 3:17','Romans 5:8','Psalm 34:18'],
 self=['There has never been anything good in me.','I was a mistake from the start.','Other people were born worthwhile. I was not.','Any good I do is fake.','God regrets making me.','I should not take up anyone’s time.'],
 errors=[('Labeling','Calling my whole life “no good” because of shame or sin.'),('Overgeneralization','Erasing every good thing across every year.'),('Emotional reasoning','Feeling worthless and treating the feeling as my history.'),('Discounting the positive','Refusing to count love, effort, or gifts that do not fit the verdict.')],
 questions=['Who first told me I was no good, and were they right about all of me?','What good has been present in me that this sentence leaves out?','Is “never” something I can actually know about my whole life?','Would I say “you have never been any good” to a child I love?','What does God say about how I was made and how Christ loves me?','What is one good thing I can acknowledge without calling it fake?'],
 replacement='I am not worthless. God made me and calls me His workmanship, even with my failures and wounds.',
 truths=['I am fearfully and wonderfully made.','A hard history does not make me no good.','God’s love reached me before I was impressive.','I can admit sin without erasing my whole life.','I am God’s workmanship, not a regret.','Shame is a feeling, not my biography.'],
 pearls=['self-esteem-low','god-creator','love-by-god','thinking-healthy','guilt-shame'], gc=[24,17,12],
 songs=[('yousay','God’s loving word challenges a name built only on weakness.'),('father','The Father’s love is deeper than the verdict you grew up with.'),('clean','Shame does not put you beyond God’s restoring grace.'),('great','The God who made you is great, and you are among His works.')],
 prompt='When the “no good” feeling came', moment='the old verdict felt true',
 example='Psalm 139:14 becomes: “<strong>Sarah</strong> can write: “I am fearfully and wonderfully made. I am not no good.””',
 reading='self-esteem-low', read_label='Self-Esteem, Low',
 actions=[('<strong>Write a truer history.</strong> List five moments of goodness, courage, or love in your life, however small. The lie says there are none.','Write a truer history'),
          ('<strong>Retire the old sentence.</strong> When you hear “I’m no good,” answer aloud with Psalm 139:14.','Retire the old sentence'),
          ('<strong>Tell a safe person the verdict.</strong> Say the sentence you grew up with, and ask what they see instead. Write their answer.','Tell a safe person the verdict'),
          ('<strong>Do one good thing on purpose</strong> this week, a kindness or a faithful task, and let it count.','Do one good thing on purpose')],
 prayer='Lord, I have called myself no good for a long time. Teach me the truth about how You made me and how You love me, and heal the old verdict. Amen.',
 tracker='A moment I was not “no good”')

add(
 num=37, file='Nobody-Could-Possibly-Like-Me', belief='Nobody could possibly like me.', crisis=False,
 origins='Rejection, teasing, betrayal, or the sense of being odd can harden into a rule: if people really knew me, liking me would be impossible. Depression makes that rule feel obvious. It confuses “some people have not liked me” with “no one could.” It also forgets that being liked is not the same thing as being loved by God, who already knows you and has not turned away.',
 teaches='God’s love is not a guess about whether people find us pleasant. “While we were still sinners, Christ died for us.” Jesus tells His friends to remain in His love, the same love the Father has for Him. The Lord is among His people and quiets them with His love. He cares for you. People are free to like or not like, and their opinions are not a law. The lie says liking you is impossible. Scripture says you are already loved.',
 key='Romans 5:8', also=['John 15:9','Zephaniah 3:17','1 Peter 5:7','Isaiah 49:15–16'],
 self=['If they knew the real me, they would leave.','I am too much, or not enough, for anyone to enjoy.','People are only being polite.','I should stay quiet so no one has a reason to dislike me.','Love is for other personalities.','Even God merely puts up with me.'],
 errors=[('Mind reading','Knowing in advance that everyone would reject me.'),('Overgeneralization','Turning some rejection into “nobody could like me.”'),('Labeling','Treating my personality as something impossible to love.'),('Emotional reasoning','Feeling unlikable and calling the feeling a fact about everyone.')],
 questions=['Who has liked me, even a little, when they knew something true about me?','Am I asking people to like a performance, or letting them know me?','What am I sure they would hate, and is that the whole of me?','Would I tell a quiet or awkward friend that nobody could like them?','How is God’s love different from being popular?','What is one safe relationship where I could be a little more honest?'],
 replacement='Not everyone will like me, and that is not the same as nobody could. God loves me, and there are people who can know me and stay.',
 truths=['God loves me and already knows me.','Some rejection is not universal rejection.','I can be known a little more and still be liked.','Being liked is pleasant. Being loved by God is certain.','I do not have to perform to be worth knowing.','One safe person is enough to test this lie.'],
 pearls=['love-by-god','friendship','loneliness','self-esteem-low','church'], gc=[17,24,12],
 songs=[('body','The church is called to welcome people, not to leave them unknown.'),('knows','Jesus knows suffering and still invites you to come.'),('love','Receiving God’s love can loosen the fear of being disliked.'),('friend','You can bring the fear of people to the Friend who carries burdens.')],
 prompt='When the “nobody could like me” feeling came', moment='being known felt dangerous',
 example='Romans 5:8 becomes: “<strong>Sarah</strong> can write: “Christ loved me before I was impressive. Somebody already does.””',
 reading='friendship', read_label='Friendship',
 actions=[('<strong>Stay for one real conversation.</strong> With a safe person, share one honest thing you usually hide. Notice whether they leave.','Stay for one real conversation'),
          ('<strong>Count the exceptions.</strong> Write the names of people who have enjoyed you. The word “nobody” has to survive that list.','Count the exceptions'),
          ('<strong>Receive a compliment without arguing.</strong> When someone says something kind, say “thank you” and write it down.','Receive a compliment'),
          ('<strong>Pray John 15:9</strong> each morning: ask to remain in the love you did not earn.','Pray the love verse')],
 prayer='Lord, I expect dislike before anyone has a chance to know me. Root me in Your love, and help me risk being known by one safe person. Amen.',
 tracker='A moment I was liked or loved')

add(
 num=38, file='Ill-Never-Get-Over-This', belief='I’ll never get over this.', crisis=True,
 origins='Some wounds are so large that “getting over it” sounds like an insult. A death, a betrayal, an illness, a public shame, or a depression that has lasted for years can make recovery seem like a fairy tale. The hurt is real, and it may leave a mark. The lie is the word “never”: the claim that comfort, strength, and a life that is more than this pain are permanently impossible.',
 teaches='God does not tell wounded people to pretend they were never hurt. He heals the brokenhearted and binds up their wounds. He is the Father of compassion and the God of all comfort, who comforts us in all our troubles. Weeping may stay the night, and joy comes in the morning. Mercies are new every morning. These promises do not mean the loss was small or that grief has a deadline. They mean the pain does not get to say “forever.”',
 key='Psalm 147:3', also=['2 Corinthians 1:3–4','Psalm 30:5','Lamentations 3:22–23','Romans 8:28'],
 self=['This will always feel exactly like it does today.','If I were going to heal, I would have by now.','People who say it gets better do not understand.','I am not allowed to feel any relief.','My life stopped, and it cannot start again.','Comfort is for milder problems than mine.'],
 errors=[('Fortune telling','Declaring that healing can never begin.'),('All-or-nothing thinking','If I am not completely over it, I am not healing at all.'),('Emotional reasoning','Feeling raw today and concluding I always will.'),('Discounting the positive','Ignoring any hour that hurt a little less.')],
 questions=['What would “a little better” look like, short of forgetting?','Has any part of this already become more bearable than it was at first?','Am I asking myself to be finished, when God is asking me to be comforted?','Who has walked with someone through a pain that once seemed final?','What comfort has God already given, even if the loss remains?','What is one kindness I can receive this week while I am still hurting?'],
 replacement='I may not be over this today, and that does not mean I never will. God comforts me, and healing can come one day at a time.',
 truths=['Not being over it today is not the same as never healing.','God comforts me inside the trouble, not only after it.','I can hurt and still be held.','A smaller pain than yesterday can count as mercy.','I do not have to heal on someone else’s schedule.','I can ask for help while this is still hard.'],
 pearls=['sorrow','suffering','depression-symptoms-of','hopeless','peace'], gc=[12,27,29],
 songs=[('allnew','God makes things new. The present pain is not His last word.'),('forever','Christ’s resurrection is a hope beyond what feels permanent.'),('heaven','Christian hope looks past this wound to a restored life with God.'),('assurance','You belong to Christ. This pain is not your only story.')],
 prompt='When the “I’ll never get over this” feeling came', moment='healing felt impossible',
 example='Psalm 147:3 becomes: “<strong>Sarah</strong> can write: “God heals the brokenhearted. I am not finished, and I am not abandoned in this.””',
 reading='sorrow', read_label='Sorrow',
 actions=[('<strong>Mark one smaller moment.</strong> Each day, note one minute that hurt less, or one comfort you received. “Never” has to argue with that note.','Mark one smaller moment'),
          ('<strong>Let someone sit with you.</strong> Tell one safe person you are not over it, and let them stay. You do not have to perform recovery.','Let someone sit with you'),
          ('<strong>Receive one comfort on purpose.</strong> A meal, a walk, a prayer, or a song. Write what you received.','Receive one comfort'),
          ('<strong>Get help if “never” includes wanting to die.</strong> If you are thinking about ending your life, call or text 988, or tell someone near you today.','Get help if you want to die')],
 prayer='Lord, I cannot see a way past this pain. Be the God of comfort here, not only later. Heal what I cannot rush, and keep me from calling this the end. Amen.',
 tracker='A moment of comfort')

add(
 num=39, file='My-Sins-Are-Unforgivable', belief='My sins are unforgivable.', crisis=True,
 origins='A shameful act, a repeated habit, a cruel word, or a religious voice that used guilt as a weapon can convince a person they have crossed a line God will not cross back. Depression turns proper sorrow into a closed case: not “I need forgiveness,” but “forgiveness cannot apply to me.” Sin is real. The lie is that Christ’s forgiveness has a limit you have passed, so confession is useless and God is finished with you.',
 teaches='Scripture takes sin seriously, and it speaks clearly about pardon. “If we confess our sins, He is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.” As far as the east is from the west, so far has He removed our transgressions. He pardons iniquity and does not retain His anger forever, because He delights in loving devotion. There is no condemnation for those in Christ. These words are not permission to take sin lightly. They are God’s answer to the claim that your sin is beyond Him.',
 key='1 John 1:9', also=['Psalm 103:12','Micah 7:18','Romans 8:1','Romans 5:8'],
 self=['God might forgive others, but not this.','I have asked too many times.','If people knew, they would agree I am past hope.','Confession will not reach what I did.','I have to pay for this myself.','I should stay away from God so I do not insult Him.'],
 errors=[('All-or-nothing thinking','If this sin was serious, forgiveness is impossible.'),('Emotional reasoning','Feeling unforgivable and calling the feeling God’s decision.'),('Discounting the positive','Ignoring the promise of cleansing because I do not feel clean.'),('Magnification','Making my sin bigger than the cross.')],
 questions=['What exactly am I calling unforgivable, and who told me God stops there?','Have I confused the seriousness of sin with a limit on God’s mercy?','What does 1 John 1:9 say God does when we confess?','Am I trying to pay for what Christ already carried?','Would I tell a repentant friend that God could not forgive them?','What would trusting forgiveness look like this week, even before I feel it?'],
 replacement='My sin is real, and it is not beyond God’s forgiveness. If I confess it, He is faithful to forgive and cleanse me.',
 truths=['God forgives the sins I confess. He is faithful.','Serious sin is not the same thing as unforgivable sin.','I do not have to punish myself to finish Christ’s work.','Feeling guilty is not the same as being unforgiven.','God’s mercy is larger than my worst act.','I can come back instead of hiding.'],
 pearls=['forgiveness','guilt-shame','love-by-god','faith','depression-symptoms-of'], gc=[26,14,12],
 songs=[('east','God removes confessed sin as far as east is from west.'),('chains','Grace, not self-punishment, breaks the chain.'),('cross','Christ’s cross answers guilt. You do not have to pay it yourself.'),('glory','Redemption and forgiveness are the reason to give God glory.')],
 prompt='When the “unforgivable” feeling came', moment='mercy felt out of reach',
 example='1 John 1:9 becomes: “<strong>Sarah</strong> can write: “I confess this sin, and God is faithful to forgive and cleanse me.””',
 reading='forgiveness', read_label='Forgiveness',
 actions=[('<strong>Confess it in plain words.</strong> Write the sin to God in one honest sentence, then read 1 John 1:9 aloud as His answer. Destroy the paper if you need to.','Confess it in plain words'),
          ('<strong>Stop the extra sentence.</strong> When you confess, do not add “but not me.” Stop at God’s promise.','Stop the extra sentence'),
          ('<strong>Tell a pastor or wise believer</strong> if the shame is too heavy to carry alone. Ask them to pray the promise with you.','Tell a pastor'),
          ('<strong>Get help if shame includes wanting to die.</strong> If you are thinking about ending your life, call or text 988, or tell someone near you today.','Get help if you want to die')],
 prayer='Lord, I have sinned, and I have called it beyond You. You are faithful and just. Forgive me, cleanse me, and teach me to come to You instead of hiding. Amen.',
 tracker='A moment I trusted forgiveness')

add(
 num=40, file='God-Has-Forsaken-Me', belief='God has forsaken me.', crisis=True,
 origins='Unanswered prayer, a long depression, a loss, injustice, or a season when worship feels empty can make the soul say what the psalms also said: God has turned away. The feeling of absence is real and is not a sin by itself. The lie is the conclusion that God has broken His promise and left you for good. Depression is very good at mistaking silence for abandonment.',
 teaches='God’s own words answer this belief directly. “He will never leave you nor forsake you.” Jesus said, “Surely I am with you always, even to the end of the age.” Nothing in death or life, present or future, can separate His people from the love of God in Christ. Even in the valley of the shadow of death, the psalmist said, “You are with me.” These verses do not claim you will always feel God’s nearness. They claim that His presence does not depend on the feeling.',
 key='Deuteronomy 31:8', also=['Matthew 28:20','Romans 8:38–39','Psalm 23:4','Isaiah 41:10'],
 self=['If God were with me, I would feel Him.','He answers other people and has given up on me.','My prayers hit the ceiling because He left.','This darkness means I am abandoned.','I must have driven Him away.','There is no point praying to someone who is gone.'],
 errors=[('Emotional reasoning','Feeling abandoned and concluding that God has left.'),('Fortune telling','Deciding a quiet season is a permanent forsaking.'),('Mind reading','Claiming to know that God has rejected me.'),('Discounting the positive','Ignoring the promises, and the helps, that say He is still here.')],
 questions=['Am I equating God’s presence with a feeling?','What has God promised about leaving His people?','Have I felt forsaken before and later found He was still with me?','What help, Scripture, or person has He already placed near me?','Is silence the same thing as abandonment?','What is one way I can pray honestly without deciding He is gone?'],
 replacement='Feeling abandoned is not the same as being forsaken. God has promised not to leave me, and He is with me in this.',
 truths=['God will not forsake me.','A quiet season is not the same as abandonment.','Jesus is with me to the end of the age.','Nothing can separate me from the love of God in Christ.','I can pray honestly while I wait to feel Him.','He is with me in the valley, not only on the far side of it.'],
 pearls=['god-all-loving','god-present-everywhere','faith','depression-symptoms-of','loneliness'], gc=[12,27,22],
 songs=[('even','Trust does not require the feeling you wanted before God counts as present.'),('fear','God’s presence gives courage without requiring a life with no darkness.'),('messiah','Jesus entered suffering. He does not stand far off from yours.'),('eyes','When fear says God is gone, turn your eyes to Christ, who is with you.')],
 prompt='When the “God has left” feeling came', moment='God felt absent',
 example='Deuteronomy 31:8 becomes: “<strong>Sarah</strong> can write: “The Lord goes before me. He will not leave me or forsake me.””',
 reading='god-present-everywhere', read_label='God, Present Everywhere',
 actions=[('<strong>Pray the promise back.</strong> Each morning, read Deuteronomy 31:8 aloud and add one honest sentence about how you feel.','Pray the promise back'),
          ('<strong>Separate feeling from promise.</strong> Write two columns: “What I feel” and “What God promised.” Do not make the first column cross out the second.','Separate feeling from promise'),
          ('<strong>Ask one believer to pray with you</strong> once this week, especially if praying alone feels pointless.','Ask one believer to pray with you'),
          ('<strong>Get help if abandonment includes wanting to die.</strong> If you are thinking about ending your life, call or text 988, or tell someone near you today.','Get help if you want to die')],
 prayer='Lord, I feel forsaken, and Your word says You will not leave me. Hold me to that promise. Be with me in this darkness, and give me courage to keep praying. Amen.',
 tracker='A moment I was not forsaken')

def render(d, head, script):
    kinds = []
    song_html = []
    for key, why in d['songs']:
        kind, html = song(key, why)
        kinds.append(kind)
        song_html.append(html)
    if kinds.count('classic') != 1 or kinds.count('contemporary') != 3:
        raise SystemExit(f"song mix {d['num']} {kinds}")
    origins = d['origins'] + (CRISIS if d['crisis'] else '')
    step = STEP_CRISIS if d['crisis'] else STEP_MILD
    read = d['reading']
    if read not in PEARLS:
        raise SystemExit('bad pearl '+read)
    for slug in d['pearls']:
        if slug not in PEARLS:
            raise SystemExit('bad pearl '+slug)
    belief = d['belief']
    h1 = f'“{belief}”' if belief.endswith('.') else f'“{belief}.”'
    # belief strings already end with a period
    shown = f'“{belief[:-1]}.”' if belief.endswith('.') else f'“{belief}.”'
    # Keep the period inside the quotes, matching card 31: “My situation is hopeless.”
    shown = '“' + belief + '”' if belief.endswith('.') else '“' + belief + '.”'
    errs = '\n'.join(f'<li><strong>{a}: </strong>{b}</li>' for a,b in d['errors'])
    opts = lambda xs: '<ul class="opts">\n' + '\n'.join(f'<li>{x}</li>' for x in xs) + '\n</ul>'
    hw_q = opts(d['questions'])
    hw_t = opts(d['truths'][:1] and [d['replacement']] + d['truths'][1:6] if False else [d['replacement']] + [t for t in d['truths'] if t != d['replacement']][:5])
    # ensure 6 truths: replacement + up to 5
    truth_items = [d['replacement']] + [t for t in d['truths'] if t != d['replacement']]
    truth_items = truth_items[:6]
    hw_t = opts(truth_items)
    scr_refs = [d['key']] + d['also'][:2]
    scr = '<ul class="opts">\n' + '\n'.join(
        f'<li><span class="ref">{ref}</span><span class="scrip">“{V[ref] if V[ref].endswith(("!","?")) else V[ref]}”</span></li>'
        for ref in scr_refs) + '\n</ul>'
    # scripture lines should include final punctuation inside the homework quote, full BSB
    acts = '<ul class="opts">\n' + '\n'.join(f'<li>{a}</li>' for a,_ in d['actions']) + '\n</ul>'
    body = f'''<!-- ============ CARD ============ -->
<div class="card belief">
<div class="tag">Psychological/Cognitive False Belief #{d['num']} · Depression</div>
<h1>{shown}</h1>
<div class="orn">✦ ✦ ✦</div>

<h2>Where it often comes from</h2>
<p>{origins}</p>

<h2>What Scripture teaches</h2>
<p>{d['teaches']}</p>
<div class="key">{qv(d['key'])}</div>

<h2>Also see</h2>
<div class="also">
{chr(10).join('<p>'+qv(r)+'</p>' for r in d['also'])}
</div>

<h2>Common self-statements</h2>
{ul(d['self'])}

<h2>Common logical errors</h2>
<ul>
{errs}
</ul>

<h2>Challenging questions</h2>
{ul(d['questions'])}

<h2>Truth summary</h2>
<p class="truth">{d['replacement']}</p>

<h2>Related Pearls topics</h2>
<p>Click a topic to open it in the Pearls Scripture Search:</p>
<ul class="pearls">
{chr(10).join(f'<li><a href="{PB}{s}" target="_blank" rel="noopener">{PEARLS[s]}</a></li>' for s in d['pearls'])}
</ul>
<p class="gc-head"><strong>Godly Counsel Lessons:</strong></p>
<p>From the book <em>Godly Counsel</em> by Dr. Brian Campbell. Click a lesson to open it. You can read it on screen or print it.</p>
<ul class="pearls">
{chr(10).join(gc_link(n) for n in d['gc'])}
</ul>

<!--christlike-->
<h2>What does a mentally healthy Christian look like?</h2>
<div style="display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap;background:#f6efe2;border-left:4px solid #b08a4b;border-radius:6px;padding:16px 18px;margin:8px 0 18px">
<a href="https://www.amazon.com/dp/1456309684" target="_blank" rel="noopener" title="Order Christlike: Walking the Walk on Amazon" style="flex:none"><img src="https://doctorishome.github.io/belief-therapy-tool/belief-cards/books/christlike-cover.jpg" alt="Cover of Christlike: Walking the Walk, The Mentally Healthy Christian, by Dr. Brian Campbell with Rev. Jim Angelakos" style="width:120px;height:auto;display:block;border-radius:3px;box-shadow:0 3px 10px rgba(0,0,0,.25)"></a>
<div style="flex:1;min-width:200px">
<p style="margin:0 0 8px">From <em>Christlike: Walking the Walk</em> by Dr. Brian Campbell. A portrait, verse by verse, of how a mentally healthy Christian thinks, feels, and lives.</p>
<p style="margin:0"><a href="https://doctorishome.github.io/belief-therapy-tool/belief-cards/books/the-mentally-healthy-christian.html" target="_blank" rel="noopener" style="color:#1f3a5f;text-decoration-color:#b08a4b;text-underline-offset:3px"><b>Read excerpts from “The Mentally Healthy Christian”</b></a> <span style="font-size:.9em;color:#6b6250">(with every Scripture written out)</span></p>
</div></div>
<!--/christlike-->
{audio('Overcoming Depression', DEP, 'about 20 minutes')}

{audio('Overcoming Anxiety', ANX, 'about 18 minutes')}

<h2>Songs that speak truth to this belief</h2>
<p class="songnote2">Tap a song to play it right here. Three contemporary songs and one classic hymn or older favorite.</p>
<div class="songs">
{chr(10).join(song_html)}
</div>
<p class="songnote">Songs play here through YouTube and may start with a short ad. If one will not play, use its “Watch on YouTube” link.</p>

<p class="morning">Each morning ask: “If I truly believed God’s truth instead of this lie, what is one step I could take today?”</p>
<div class="foot">✦ ✦ ✦</div>
</div>

<!-- ============ HOMEWORK, PAGE 1 ============ -->
<div class="card">
<div class="tag">Homework · Replace and Rehearse</div>
<h1>My Plan for Replacing<br/>{shown}</h1>
<div class="orn">✦ ✦ ✦</div>
<p class="intro">Read through each section and <strong>check the one that fits you best</strong>. If none of them fit, write your own. One choice per section is enough. A truth you choose for yourself will stick better than one handed to you.</p>
<div class="fill"><span>Name:</span><i></i><span>Date started:</span><i></i></div>

<div class="step"><div class="num">1</div><div><h2>How strongly do I believe the lie?</h2><p class="why">Rate it now so you can see your progress later.</p></div></div>
<div class="rate"><span><b>{shown}</b> I believe this <span class="box"></span> % <span style="font-size:14px;color:#5a5348">(0 = not at all, 100 = completely)</span></span></div>

<div class="step"><div class="num">2</div><div><h2>My best question</h2><p class="why">The one question I will ask myself every time the lie shows up.</p></div></div>
{hw_q}
<div class="fill"><span>My own question:</span><i></i></div>

<div class="step"><div class="num">3</div><div><h2>My replacement truth</h2><p class="why">The statement I will say to myself instead of the lie.</p></div></div>
{hw_t}
<div class="fill"><span>In my own words:</span><i></i></div>

<div class="step"><div class="num">4</div><div><h2>My Scripture</h2><p class="why">The verse that speaks most directly to me. This is the one I will memorize.</p></div></div>
{scr}
<div class="fill"><span>A verse I found myself:</span><i></i></div>
<div class="lines"><i></i></div>

<div class="foot">✦ ✦ ✦</div>
</div>

<!-- ============ HOMEWORK, PAGE 2 ============ -->
<div class="card">
<div class="tag">Homework · Replace and Rehearse</div>
<h1>Practicing the Truth</h1>
<div class="orn">✦ ✦ ✦</div>

<div class="step"><div class="num">5</div><div><h2>My practice plan</h2><p class="why">Everyone does the first four. Then pick one or two extra tools.</p></div></div>
<div class="group">Everyone does these</div>
<ul class="opts">
<li><strong>Make my Truth Card</strong> (below). Carry it and read it at least three times a day.</li>
<li><strong>Memorize my Scripture</strong> from Step 4.</li>
<li><strong>Listen to one song each day</strong> from “Songs that speak truth to this belief” on my card, and fill in my song journal (below).</li>
<li><strong>Set reminders</strong> to silently repeat my truth. Check one or more:
  <span class="scrip" style="font-style:normal">☐ <strong>A buzz:</strong> my watch or phone vibrates every ______ minutes<br/>☐ <strong>An everyday event:</strong> every time I ______________________________<br/>☐ <strong>A visual reminder:</strong> something I will see often, such as a sticky note on my mirror, my truth as the background picture on my phone, or a note on my car dashboard.</span></li>
</ul>
<div class="group">Pick one or two that fit me</div>
<ul class="opts">
<li><strong>{d['prompt']}:</strong> Each day, write down one moment when {d['moment']}. Write what happened, what you told yourself, and one more accurate statement.</li>
<li><strong>My name in Scripture:</strong> Write a personal reminder based on my verse and read it aloud. Keep this application separate from the Bible quotation.
  <span class="scrip">For example, {d['example']}</span></li>
<li><strong>Gratitude journal:</strong> Each night, write three things I thank God for.</li>
<li><strong>Truth recording:</strong> Record my own voice reading my Truth Card and verse, and listen in the car or on a walk.</li>
<li><strong>Reading:</strong> The <a href="{PB}{read}" target="_blank" rel="noopener">“{d['read_label']}” topic in Pearls</a>.</li>
<li><strong>Listening:</strong> The <a href="{DEP}" target="_blank" rel="noopener">Overcoming Depression audio</a> or the <a href="{ANX}" target="_blank" rel="noopener">Overcoming Anxiety audio</a> by Dr. Brian Campbell. Tap to play.</li>
</ul>

<div class="step"><div class="num">6</div><div><h2>My action step this week</h2><p class="why">Do one thing that tests the lie in real life.</p><p class="why">{step}</p></div></div>
{acts}
<div class="fill"><span>What I will do:</span><i></i></div>
<div class="fill"><span>When:</span><i></i></div>
<div class="fill"><span>What the lie predicts will happen:</span><i></i></div>

<div class="step"><div class="num">7</div><div><h2>End-of-week check-in</h2><p class="why">Bring this page to your next session.</p></div></div>
<div class="fill"><span>What actually happened:</span><i></i></div>
<div class="lines"><i></i></div>
<div class="fill"><span>What I learned:</span><i></i></div>
<div class="rate"><span><b>The lie</b> {shown}: <span class="box"></span> %</span><span><b>My truth:</b> <span class="box"></span> %</span></div>

<h2>Daily practice tracker</h2>
<table class="track">
<tr><th>Day</th><th>Read my card</th><th>Said my verse</th><th>Used my reminder</th><th>{d['tracker']}</th></tr>
<tr><td>Mon</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Tue</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Wed</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Thu</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Fri</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Sat</td><td></td><td></td><td></td><td class="wide"></td></tr>
<tr><td>Sun</td><td></td><td></td><td></td><td class="wide"></td></tr>
</table>

<h2>My song journal</h2>
<p class="why">After each day's song, write what it told you that challenges the lie.</p>
<table class="track songj">
<tr><th>Day</th><th>Song I listened to</th><th>What it told me that challenges the lie</th></tr>
<tr><td>Mon</td><td></td><td></td></tr>
<tr><td>Tue</td><td></td><td></td></tr>
<tr><td>Wed</td><td></td><td></td></tr>
<tr><td>Thu</td><td></td><td></td></tr>
<tr><td>Fri</td><td></td><td></td></tr>
<tr><td>Sat</td><td></td><td></td></tr>
<tr><td>Sun</td><td></td><td></td></tr>
</table>

<h2>My Truth Card</h2>
<div class="cutcard">
<div class="lbl">The lie</div>
<div class="lie">{belief[:-1] if belief.endswith('.') else belief}</div>
<div class="lbl">The truth</div>
<div class="lines"><i></i><i></i></div>
<div class="lbl">God’s Word</div>
<div class="lines"><i></i><i></i></div>
</div>
<p class="cutnote">Copy onto a 3×5 card, or cut along the dashed line and carry it with you.</p>

<h2>Prayer</h2>
<p class="prayer">{d['prayer']}</p>
<div class="foot">✦ ✦ ✦</div>
<p class="bnote">Scripture quotations are from the Berean Standard Bible (BSB), which is in the public domain.</p>
</div>

<p class="back"><a href="#top">Back to top</a> · <a href="https://doctorishome.github.io/belief-therapy-tool/belief-lists/psychological.html" target="_top">Psychological/Cognitive Beliefs</a></p>

'''
    # fix the accidental double assignment above by using shown consistently
    page_head = head.replace('Psych-031-My-Situation-Is-Hopeless.pdf', f"Psych-{d['num']:03d}-{d['file']}.pdf")
    page_head = page_head.replace('Psych-031-My-Situation-Is-Hopeless-Homework.pdf', f"Psych-{d['num']:03d}-{d['file']}-Homework.pdf")
    page_head = page_head.replace('Belief Card: My situation is hopeless', 'Belief Card: ' + belief.rstrip('.'))
    page_head = page_head.replace('“My situation is hopeless.”', shown)
    return page_head + body + script, truth_items

def main():
    patch_31()
    src = (ROOT/'belief-cards/psychological/Psych-031-My-Situation-Is-Hopeless.html').read_text()
    head, rest = src.split('<!-- ============ CARD ============ -->', 1)
    script_at = rest.rfind('\n</div><script>')
    script = rest[script_at+1:]
    global head_g, script_g
    # bind for render via default args closed over
    sets=set()
    for d in CARDS:
        page, truths = render_with(d, head, script)
        songset=tuple(k for k,_ in d['songs'])
        if songset in sets:
            raise SystemExit('duplicate song set '+str(songset))
        sets.add(songset)
        out = ROOT/f"belief-cards/psychological/Psych-{d['num']:03d}-{d['file']}.html"
        out.write_text(page)
        meta = {
            'num': d['num'], 'file': d['file'], 'group': 'Depression',
            'belief': '“'+d['belief']+'”' if d['belief'].endswith('.') else '“'+d['belief']+'.”',
            'belief_plain': d['belief'].rstrip('.'),
            'origins': d['origins'],
            'self': d['self'],
            'songs': [k for k,_ in d['songs']],
            'key': d['key'],
            'replacement': d['replacement'],
        }
        (ROOT/f"tools/psych-depression/{d['num']:03d}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1)+'\n')
        print(out.name, 'truths', len(truths), 'crisis', d['crisis'])
    # wire the list
    lst_path = ROOT/'tools/lists/psychological.json'
    lst = json.loads(lst_path.read_text())
    group = next(g for g in lst['sections'][0]['groups'] if g['name']=='Depression')
    by_belief = {c['belief']: f"Psych-{c['num']:03d}-{c['file']}.html" for c in CARDS}
    for b in group['beliefs']:
        if b[0] in by_belief:
            b[:] = [b[0], by_belief[b[0]]]
    lst_path.write_text(json.dumps(lst, ensure_ascii=False, indent=1)+'\n')
    print('list wired', sum(1 for b in group['beliefs'] if len(b)>1))

def render_with(d, head, script):
    # local wrapper so render can use head/script
    return render(d, head, script)

if __name__ == '__main__':
    main()
