"""Build Anxiety cards 41–50 on the Core-001 / Psych-031 template.
Overcoming Anxiety is the first recording; Overcoming Depression is the second.
Run: python3 tools/make_anxiety_cards.py
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
STEP = 'Choose steps you can do safely. If this belief comes with hopelessness or thoughts of ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone.'
V = {
 'Isaiah 41:10': 'Do not fear, for I am with you; do not be afraid, for I am your God. I will strengthen you; I will surely help you; I will uphold you with My right hand of righteousness.',
 'Psalm 56:3': 'When I am afraid, I put my trust in You.',
 'Psalm 46:1': 'God is our refuge and strength, an ever-present help in times of trouble.',
 'Joshua 1:9': 'Have I not commanded you to be strong and courageous? Do not be afraid; do not be discouraged, for the LORD your God is with you wherever you go.',
 'Matthew 6:34': 'Therefore do not worry about tomorrow, for tomorrow will worry about itself. Today has enough trouble of its own.',
 '2 Timothy 1:7': 'For God has not given us a spirit of fear, but of power, love, and self-control.',
 'Psalm 94:19': 'When anxiety overwhelms me, Your consolation delights my soul.',
 'John 14:27': 'Peace I leave with you; My peace I give to you. I do not give to you as the world gives. Do not let your hearts be troubled; do not be afraid.',
 'Philippians 4:13': 'I can do all things through Christ who gives me strength.',
 '2 Corinthians 12:9': 'But He said to me, ‘My grace is sufficient for you, for My power is perfected in weakness.’ Therefore I will boast all the more gladly in my weaknesses, so that the power of Christ may rest on me.',
 'Deuteronomy 31:8': 'The LORD Himself goes before you; He will be with you. He will never leave you nor forsake you. Do not be afraid or discouraged.',
 'Psalm 121:3–4': 'He will not allow your foot to slip; your Protector will not slumber. Behold, the Protector of Israel will neither slumber nor sleep.',
 'Psalm 4:8': 'I will lie down and sleep in peace, for You alone, O LORD, make me dwell in safety.',
 '1 Peter 5:7': 'Cast all your anxiety on Him, because He cares for you.',
 'Isaiah 26:3': 'You will keep in perfect peace the steadfast of mind, because he trusts in You.',
 'Proverbs 3:5–6': 'Trust in the LORD with all your heart, and lean not on your own understanding; in all your ways acknowledge Him, and He will make your paths straight.',
 'Philippians 4:6–7': 'Be anxious for nothing, but in everything, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.',
 'Matthew 6:27': 'Who of you by worrying can add a single hour to his life?',
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
    html = f'''<a class="song" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener"><span class="thumb" style="background-image:url('https://i.ytimg.com/vi/{vid}/hqdefault.jpg')"></span><span class="txt"><span class="st">{title}</span><span class="sa">{art}</span><span class="sw">{why}</span></span></a>'''
    return kind, html
def gc_link(n):
    title = GC[str(n)][0]
    slug = re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-')
    return f'<li><a href="{GCB}GC-{n:02d}-{slug}.pdf" target="_blank" rel="noopener">{title}</a></li>'
def ul(items):
    return '<ul>\n' + '\n'.join(f'<li>{x}</li>' for x in items) + '\n</ul>'
def opts(items):
    return '<ul class="opts">\n' + '\n'.join(f'<li>{x}</li>' for x in items) + '\n</ul>'

C = []
def add(**k):
    C.append(k)

add(num=41, file='Something-Terrible-Is-About-to-Happen',
 key='Isaiah 41:10', also=['Psalm 56:3','Psalm 46:1','Joshua 1:9','Matthew 6:34'],
 pearls=['anxiety-worry','fear','trust','peace','god-all-powerful'], gc=[5,29,30],
 songs=[('liar','Fear makes up disasters. It is not a reliable reporter.'),('fear','God’s presence is the answer to “what if the worst is next.”'),('battle','You can hand the imagined catastrophe to God instead of rehearsing it.'),('eyes','Look at Christ, who is with you, rather than at the disaster you are inventing.')],
 origins='Anxiety is a body alarm that learned to ring early. A scare, a loss, a parent who always expected the worst, or a season of real danger can teach the mind to treat a quiet moment as the pause before disaster. The alarm feels like information. It is often a habit of predicting the worst before anything has happened.',
 teaches='God does not tell His people that nothing hard will ever happen. He tells them not to live as if disaster is already in the room. “Do not fear, for I am with you.” When the psalmist is afraid, he puts his trust in God. God is a refuge and an ever-present help. Courage is commanded because the Lord is with His people wherever they go. Tomorrow’s trouble is not today’s assignment. A feeling that something terrible is about to happen is not the same thing as it happening.',
 replacement='A feeling that something terrible is coming is not proof that it is. God is with me, and I can live this day without living in the catastrophe.',
 truths=['This alarm is a feeling, not a news report.','God is with me in the day I actually have.','I can be afraid and still put my trust in God.','I do not have to solve tomorrow before tonight.','Most of the disasters I rehearse do not arrive.','I can take one ordinary step while the alarm is ringing.'],
 self=['I can feel it. Something awful is next.','If I relax, that is when it will hit.','My dread has always been right.','Other people are naïve. I see what is coming.','I should cancel the plan so I stay safe.','Peace would be careless.'],
 errors=[('Fortune telling','Treating a dread as a report about the future.'),('Emotional reasoning','Feeling alarmed and concluding that danger is present.'),('Catastrophizing','Jumping from a worry to the worst possible ending.'),('Overgeneralization','Because something bad happened once, it is about to happen again.')],
 questions=['What, exactly, do I think is about to happen?','What evidence do I have, apart from the feeling?','How many times has this same dread been wrong?','What would I tell a friend who felt certain disaster was next?','What does God promise about being with me, not about a trouble-free day?','What is one ordinary thing I can do while I wait to see what is actually true?'],
 prompt='When the “something terrible” feeling came', moment='disaster felt moments away',
 example='Isaiah 41:10 becomes: “<strong>Sarah</strong> can write: “I feel afraid, and God is with me. This feeling is not a disaster.””',
 reading='fear', read_label='Fear',
 actions=[('<strong>Name the prediction.</strong> Write the disaster you expect, then write what you actually know. Cross out anything that is only a feeling.','Name the prediction'),
          ('<strong>Check the record.</strong> List three times this same alarm was loud and the feared event did not happen.','Check the record'),
          ('<strong>Stay for one ordinary plan.</strong> Keep one small commitment you feel like canceling, and write what actually occurred.','Stay for one ordinary plan'),
          ('<strong>Pray Isaiah 41:10</strong> when the alarm starts, before you rearrange your day around it.','Pray the “do not fear” verse')],
 prayer='Lord, my body is sure that disaster is next. Teach me to trust You with this day, and not to bow to a feeling as if it were a fact. Amen.',
 tracker='A dread that did not come true')

add(num=42, file='Feeling-Anxious-Means-I-Am-in-Real-Danger',
 key='2 Timothy 1:7', also=['Psalm 56:3','Psalm 94:19','John 14:27','Isaiah 41:10'],
 pearls=['anxiety-worry','fear','peace','trust','thinking-healthy'], gc=[5,29,31],
 songs=[('voice','An anxious feeling is not the voice you have to obey.'),('truth','Tell the truth about the feeling instead of calling it danger.'),('power','God gives power and self-control, not a command to panic.'),('faithful','God’s steady care does not rise and fall with your heart rate.')],
 origins='The body was made to signal real danger. A racing heart, a tight chest, or a wave of dread once meant “move.” After enough scares, or in a season of anxiety, the same signal fires when the room is safe. The feeling is convincing because it is physical. It is still a feeling. It is not a test that proves danger is in the room.',
 teaches='Scripture separates fear from the God who gives power, love, and self-control. “For God has not given us a spirit of fear, but of power, love, and self-control.” The psalmist says, “When I am afraid, I put my trust in You,” which assumes fear and trust can be in the same person at the same time. Jesus gives His peace and says, “Do not let your hearts be troubled.” Anxiety can overwhelm, and God’s consolation meets it. None of these verses say that a pang of anxiety is proof you are in danger.',
 replacement='Anxiety is a feeling, not a verdict that I am in danger. I can be anxious and still be safe.',
 truths=['A feeling of danger is not the same as danger.','I can be anxious and still be safe.','God did not give me a spirit that must panic.','I can put my trust in God while I still feel afraid.','My body can be loud and wrong at the same time.','I do not have to obey every alarm.'],
 self=['If I feel this scared, something must be wrong.','My body would not lie to me.','Calm people are the ones who are safe. I am not calm, so I am not safe.','I have to get out of here.','This feeling is an emergency.','Trusting God would make the feeling stop, and it has not stopped.'],
 errors=[('Emotional reasoning','Using anxiety itself as the evidence of danger.'),('Catastrophizing','Turning a body sensation into an emergency.'),('All-or-nothing thinking','If I am not calm, I must be in danger.'),('Discounting the positive','Ignoring the signs that I am actually safe right now.')],
 questions=['What is the actual danger in this room, apart from how I feel?','Has this same feeling come when I was safe?','What would “safe enough” look like if I did not require the feeling to leave first?','Am I asking a feeling to do the job of evidence?','What does God give instead of a spirit of fear?','What is one thing I can do while anxious that a person in real danger could not do?'],
 prompt='When anxiety felt like danger', moment='a feeling was treated as an emergency',
 example='2 Timothy 1:7 becomes: “<strong>Sarah</strong> can write: “This fear is not from God’s Spirit. I have power, love, and self-control.””',
 reading='anxiety-worry', read_label='Anxiety/Worry',
 actions=[('<strong>Separate feeling from fact.</strong> Write “I feel ___” and “The facts are ___.” Do not let the first line edit the second.','Separate feeling from fact'),
          ('<strong>Stay two minutes.</strong> When the alarm says “leave” and you are not in real danger, stay for two minutes and notice that you are still safe.','Stay two minutes'),
          ('<strong>Name three signs of safety</strong> in the moment: a locked door, a familiar room, a person you trust, your own steady breath.','Name three signs of safety'),
          ('<strong>Read Psalm 56:3 aloud</strong> the next time anxiety spikes: afraid, and still trusting.','Read the afraid-and-trusting verse')],
 prayer='Lord, my feelings are shouting danger. Give me power, love, and a sound mind. Help me trust You while I am still afraid, and not to call every alarm an emergency. Amen.',
 tracker='A time I was anxious and safe')

add(num=43, file='I-Cant-Cope-If-the-Worst-Happens',
 key='Philippians 4:13', also=['Isaiah 41:10','2 Corinthians 12:9','Deuteronomy 31:8','Psalm 46:1'],
 pearls=['anxiety-worry','fear','help','trust','god-all-powerful'], gc=[5,33,30],
 songs=[('greater','God’s strength is greater than the scene you are rehearsing.'),('ourgod','You are not left to cope with the worst by yourself.'),('conquer','In Christ you are not defined by the fear of being overwhelmed.'),('lives','Because He lives, you can face what actually comes.')],
 origins='People who have been through a real crisis, or who grew up without enough help, often practice the worst in their minds so they will not be surprised. The practice becomes a belief: if the worst arrived, I would not be able to stand it. Anxiety lives in that rehearsal. It spends today’s strength on a day that has not come, and then concludes from the exhaustion that coping is impossible.',
 teaches='God does not ask you to carry a future catastrophe today. He does promise strength, presence, and grace for weakness. “I can do all things through Christ who gives me strength.” His grace is sufficient, and His power is perfected in weakness. He will not leave you or forsake you. He is a refuge and strength, an ever-present help. These verses are not a claim that the worst will never happen. They are a claim that you will not face it alone, and that strength is given for the day you are in.',
 replacement='I do not have to survive the worst before it comes. God gives strength for the day I am actually in.',
 truths=['I do not have to cope with tomorrow’s disaster today.','Christ gives strength for what is real, not for every scene I invent.','God’s grace is sufficient in weakness.','I have coped with hard days before, with help.','Being afraid of the worst is not the same as being unable to face a real day.','I can ask for help if a hard thing actually comes.'],
 self=['I would fall apart.','I cannot even think about it.','Other people could handle it. I could not.','If I imagine it enough, maybe I will be ready, but I never feel ready.','God helps strong people. I am not one of them.','The only safe plan is to make sure the worst never happens.'],
 errors=[('Fortune telling','Living through a disaster that has not happened and grading yourself on it.'),('Catastrophizing','Treating the worst case as the case you must solve now.'),('All-or-nothing thinking','If I cannot picture myself calm in the worst, I cannot cope at all.'),('Discounting the positive','Forgetting the hard days I have already come through.')],
 questions=['What is the worst I am rehearsing, and is it happening today?','When have I coped with something hard that I had dreaded?','Am I asking for strength for a real day, or for a movie in my head?','What help would I actually have if that day came?','What does “Christ gives me strength” mean for today, not for every fear?','What is one present responsibility I can do without solving the worst case?'],
 prompt='When the “I couldn’t cope” feeling came', moment='a future disaster felt unbearable',
 example='Philippians 4:13 becomes: “<strong>Sarah</strong> can write: “I do not have to live the worst today. Christ gives me strength for this day.””',
 reading='help', read_label='Help',
 actions=[('<strong>Park the worst case.</strong> Write it on a card, put the card away, and do one task that belongs to today.','Park the worst case'),
          ('<strong>List survived days.</strong> Write three hard things you got through. Note who helped.','List survived days'),
          ('<strong>Ask what help would exist.</strong> If the feared event is realistic, name one person and one practical help you would use. Then stop rehearsing.','Name the help that would exist'),
          ('<strong>Pray for today’s strength only</strong> each morning, using Isaiah 41:10.','Pray for today’s strength')],
 prayer='Lord, I keep trying to survive days that have not come. Give me strength for this one. Remind me that Your grace is enough if a hard day actually arrives. Amen.',
 tracker='A fear I did not have to live today')

add(num=44, file='I-Have-to-Stay-on-Guard',
 key='Psalm 121:3–4', also=['Psalm 4:8','1 Peter 5:7','Matthew 6:34','Isaiah 26:3'],
 pearls=['anxiety-worry','fear','trust','sleep-problems','peace'], gc=[5,22,29],
 songs=[('held','You can be held. You do not have to hold the whole night yourself.'),('already','God already sees what you are afraid you will miss.'),('soul','A restless soul can be told to hope instead of to keep watch forever.'),('assurance','You belong to Christ. Safety is not something you must manufacture by vigilance.')],
 origins='Some people learned that if they stopped watching, something bad got through: a parent’s mood, a child’s safety, a mistake at work, a health scare. Vigilance worked often enough to become a rule. Anxiety then calls rest dangerous. The lie says that the only thing standing between you and harm is your own attention, so you may never come off duty.',
 teaches='Scripture does not despise watchfulness, and it refuses to make you the one who never sleeps. “Your Protector will not slumber.” The psalmist lies down and sleeps in peace because the Lord makes him dwell in safety. Anxiety can be cast on God because He cares. Tomorrow is not today’s extra shift. Perfect peace is tied to a steadfast mind that trusts, not to a mind that never looks away. You may be careful. You are not the night watchman of the universe.',
 replacement='Staying on guard is not what keeps me safe. God does not slumber, and I am allowed to rest.',
 truths=['God keeps watch when I sleep.','Rest is not the same as carelessness.','I can be responsible and still stop scanning.','My attention is not the only thing holding life together.','I can cast this anxiety on God because He cares.','One evening off duty will not invite disaster.'],
 self=['If I stop watching, that is when it will happen.','Rest is for people whose lives are simpler.','I have to check one more time.','Nobody else will notice the danger.','Sleep is unsafe.','If I relax, I am failing the people I love.'],
 errors=[('Fortune telling','Believing that the moment you rest is the moment harm arrives.'),('Personalization','Making yourself the only one who can prevent every bad outcome.'),('All-or-nothing thinking','Either I am fully on guard or I am reckless.'),('Emotional reasoning','Feeling uneasy when I stop checking, and calling the unease proof I must check again.')],
 questions=['What am I afraid will slip through if I stop watching for an hour?','Who else, including God, is already watching?','Has more checking actually made me safer, or only more tired?','What would a responsible person do, short of never resting?','What does Psalm 121 say about the One who does not slumber?','What is one check I can skip tonight as a test?'],
 prompt='When you could not come off duty', moment='rest felt dangerous',
 example='Psalm 121:4 becomes: “<strong>Sarah</strong> can write: “God does not slumber. I do not have to stay awake for both of us.””',
 reading='trust', read_label='Trust',
 actions=[('<strong>Skip one extra check.</strong> Choose one habitual check that is not truly needed, leave it undone once, and write what happened.','Skip one extra check'),
          ('<strong>Set a watch-ending time.</strong> Decide when today’s vigilance stops, and do not reopen the worries after that time.','Set a watch-ending time'),
          ('<strong>Hand the night to God.</strong> Read Psalm 4:8 aloud at bedtime for seven nights.','Hand the night to God'),
          ('<strong>Tell one person you are tired of watching</strong> and let them carry one concern with you.','Share one concern')],
 prayer='Lord, I have appointed myself the one who never sleeps. You do not slumber. Teach me to rest without calling rest a failure, and to trust You with what I cannot watch. Amen.',
 tracker='A check I was able to skip')

add(num=45, file='Not-Knowing-Means-Something-Is-Wrong',
 key='Proverbs 3:5–6', also=['Matthew 6:34','Isaiah 26:3','Philippians 4:6–7','Psalm 46:1'],
 pearls=['anxiety-worry','trust','peace','thinking-healthy','faith'], gc=[5,29,31],
 songs=[('already','God sees the road you cannot see yet.'),('jesus','Jesus is present in what you do not understand.'),('want','Following God does not require control of every outcome.'),('friend','You can bring the unknown to God in plain prayer.')],
 origins='Some minds treat a blank space as a threat. If the test result is not back, the text is unanswered, or next year is unclear, anxiety fills the blank with “something is wrong.” Uncertainty was often punished in childhood, or a surprise once really was bad news. The lie upgrades “I do not know yet” into “it must be bad.” Not knowing is uncomfortable. It is also ordinary.',
 teaches='God asks for trust precisely where understanding runs out. “Trust in the LORD with all your heart, and lean not on your own understanding.” He keeps in peace the mind that is steadfast because it trusts. Jesus says not to worry about tomorrow. Peace that surpasses understanding guards the heart when we pray instead of demanding a preview. God is a refuge in trouble, including the trouble of not knowing. Uncertainty is not a diagnosis.',
 replacement='Not knowing the future is normal. Uncertainty is not the same as something being wrong. I can trust God with what I cannot see.',
 truths=['A blank space is not bad news.','I can wait for facts without inventing them.','God sees what I do not.','Peace does not require a full preview.','I can pray about the unknown instead of filling it with fear.','Today has enough real information for today.'],
 self=['If I do not know, it is bad.','I cannot rest until I know.','Silence means something is wrong.','Other people can tolerate mystery. I cannot.','I have to keep searching until the feeling stops.','God would not leave me without an answer if things were all right.'],
 errors=[('Fortune telling','Filling an unknown with a bad ending.'),('Emotional reasoning','Feeling unsettled by mystery and calling the mystery a problem.'),('Catastrophizing','Turning “not yet” into “something terrible.”'),('All-or-nothing thinking','Either I know everything or nothing is safe.')],
 questions=['What fact am I missing, and what story have I put in its place?','Has “I don’t know yet” turned out all right before?','What would waiting for the real answer look like?','Am I asking God for peace, or for a preview?','What do I actually need to know today?','Who could help me wait without refreshing the fear?'],
 prompt='When not knowing felt like bad news', moment='a blank felt dangerous',
 example='Proverbs 3:5 becomes: “<strong>Sarah</strong> can write: “I do not have to understand this yet. I can trust the Lord with it.””',
 reading='trust', read_label='Trust',
 actions=[('<strong>Write the unknown and the story.</strong> Two lines: what you do not know, and the ending you invented. Cross out the invented ending until there is news.','Separate the unknown from the story'),
          ('<strong>Delay one check.</strong> Wait a set time before refreshing the email, the portal, or the text that is feeding the fear.','Delay one check'),
          ('<strong>Pray the unknown in one sentence</strong> each morning instead of demanding the outcome.','Pray the unknown'),
          ('<strong>Do today’s task</strong> that does not depend on the answer you are waiting for.','Do today’s task')],
 prayer='Lord, I treat every unknown as bad news. Teach me to trust You where I cannot see, and to wait for facts instead of fearing a story. Amen.',
 tracker='An unknown I did not fill with fear')

add(num=46, file='If-I-Dont-Worry-I-Wont-Be-Prepared',
 key='Philippians 4:6–7', also=['Matthew 6:34','Matthew 6:27','Proverbs 3:5–6','Psalm 94:19'],
 pearls=['anxiety-worry','thinking-healthy','peace','trust','help'], gc=[5,29,22],
 songs=[('speak','God’s Word can shape your thoughts more truly than another hour of worry.'),('thrive','A life with God is more than staying braced for trouble.'),('grace','You were not meant to carry every outcome by worrying.'),('great','God is great enough that your worry is not what holds the world together.')],
 origins='Worry can masquerade as love or responsibility. A person who was surprised by hardship, or praised for always being prepared, may believe that worry is the work that keeps people safe. If they stop worrying, they feel guilty, as if they have stopped caring. Anxiety then calls itself a virtue. Planning is wise. Worry is the spinning that adds no hour to your life and no real protection to the people you love.',
 teaches='Jesus asks who can add a single hour to life by worrying, and He says tomorrow can worry about itself. Paul says, “Be anxious for nothing,” and points to prayer with thanksgiving, and to peace that guards the heart. Trust leans on the Lord rather than on our own understanding. When anxiety overwhelms, God’s consolation is what delights the soul, not another lap of worry. Preparation can be a list, a phone call, a plan. Worry is not that list. It only feels like work.',
 replacement='Worry is not preparation. I can plan wisely and still hand the outcome to God.',
 truths=['A plan is not the same thing as a worry spiral.','Worry has not kept the people I love safe.','I can care without rehearsing disaster.','God invites me to pray instead of to spin.','Peace is allowed while I am still responsible.','I can do the useful thing and then stop.'],
 self=['If I stop worrying, I am being careless.','Somebody has to worry, and it is me.','My worry is how I love people.','The moment I feel calm, I have forgotten something.','Planning is not enough. I have to feel the weight.','God helps those who worry hard enough.'],
 errors=[('Emotional reasoning','Feeling guilty when you stop worrying, and calling the guilt proof you should worry.'),('Magnification','Treating worry as if it were a useful safety tool.'),('All-or-nothing thinking','Either I worry constantly or I am irresponsible.'),('Fortune telling','Believing that calm today causes harm tomorrow.')],
 questions=['What useful action is left, once I have already made a reasonable plan?','Has an extra hour of worry ever prevented the thing I feared?','Who told me that caring has to feel like dread?','What would prayer do here that worry cannot?','What is one worry I can turn into a task, and then set down?','How would I want someone I love to carry a similar concern?'],
 prompt='When worry felt like love or duty', moment='calm felt careless',
 example='Philippians 4:6 becomes: “<strong>Sarah</strong> can write: “I can bring this to God instead of worrying it into shape.””',
 reading='anxiety-worry', read_label='Anxiety/Worry',
 actions=[('<strong>Turn worry into a task or a prayer.</strong> If there is a real step, do it. If not, pray one sentence and close the subject.','Turn worry into a task or a prayer'),
          ('<strong>Time the spiral.</strong> Notice how long you worried and whether anything got safer. Write the result.','Time the spiral'),
          ('<strong>Practice one calm hour</strong> after the useful plan is done. Do not reopen the worry during that hour.','Practice one calm hour'),
          ('<strong>Tell a loved one</strong> you are learning that worry is not how you love them.','Tell someone worry is not love')],
 prayer='Lord, I have called worry faithfulness. It has not made anyone safer. Teach me to plan what I can, pray what I cannot, and then rest. Amen.',
 tracker='A worry I set down')

add(num=47, file='Body-Feelings-Mean-Im-Losing-Control',
 key='Psalm 46:1', also=['2 Timothy 1:7','Psalm 94:19','John 14:27','Isaiah 41:10'],
 pearls=['anxiety-worry','fear','peace','help','thinking-healthy'], gc=[5,33,29],
 songs=[('power','God’s power holds you when your body feels out of control.'),('liar','A pounding heart can lie about what is happening.'),('worn','You can be worn out in your body and still ask God to restore you.'),('tender','Christ’s gentleness meets you in the panic. You do not have to hide it.')],
 origins='Panic teaches the body to fear itself. A racing heart, dizziness, a tight throat, or a sudden heat can feel like the beginning of collapse, fainting, or “going crazy.” Once that interpretation sticks, the sensation becomes the emergency. Anxiety disorders often work this way: the body fires, the mind names it catastrophe, and the name makes the body fire harder. The sensation is real. The meaning “I am losing control” is the belief to test.',
 teaches='God is a refuge and strength, an ever-present help, including when the body is loud. He has not given a spirit of fear, but of power, love, and self-control. The psalmist brings overwhelming anxiety to God and finds consolation. Jesus says not to let your heart be troubled, and He gives His peace. “Do not fear, for I am with you” is spoken to people whose bodies know fear. None of these verses say a pounding heart means you are about to lose your mind or your life. They say God is present and you are not abandoned to the sensation.',
 replacement='A racing body is not the same as losing control. I can feel anxious and still be safe.',
 truths=['This sensation is anxiety. It is not proof I am collapsing.','I have felt this before and I did not lose control.','God is a refuge while my body is loud.','I can breathe, stay, and let the wave pass.','Self-control is something God gives, not something the feeling cancels.','I can get ordinary medical care for my body without treating every symptom as doom.'],
 self=['I am about to faint, die, or lose my mind.','I have to escape or it will get worse forever.','If people see this, I will completely fall apart.','My body is warning me of something terrible.','I cannot trust myself when I feel this way.','Calm is the only proof I am all right.'],
 errors=[('Catastrophizing','Turning a body sensation into collapse, death, or madness.'),('Emotional reasoning','Feeling out of control and concluding that you are.'),('Fortune telling','Predicting the sensation will keep rising until you break.'),('Discounting the positive','Forgetting the many times this same wave passed.')],
 questions=['What is my body doing, in plain words, without the disaster label?','How many times has this feeling peaked and then come down?','What would I do if a friend described these exact sensations?','Am I in a place where I can sit, breathe, and wait ten minutes?','What does “God is our refuge” mean while my heart is racing?','Is there a real medical question to ask a doctor, separate from the panic story?'],
 prompt='When your body felt like an emergency', moment='a sensation felt like losing control',
 example='Psalm 46:1 becomes: “<strong>Sarah</strong> can write: “God is my refuge while my heart races. This feeling can pass.””',
 reading='anxiety-worry', read_label='Anxiety/Worry',
 actions=[('<strong>Describe, do not diagnose.</strong> When the wave comes, write only sensations: heart, breath, heat. Do not add “I am dying” or “I am losing it.”','Describe, do not diagnose'),
          ('<strong>Stay for the peak.</strong> If you are not in medical danger, remain where you are for ten minutes and note that the wave changes.','Stay for the peak'),
          ('<strong>Recall three passed waves.</strong> Write them down and keep the note where you will see it.','Recall three passed waves'),
          ('<strong>Ask a doctor once</strong> if a symptom truly worries you, then stop using new sensations as fresh proof of disaster.','Ask a doctor once')],
 prayer='Lord, my body is loud and I am scared of it. Be my refuge here. Give me a sound mind, and help me let this wave pass without calling it the end. Amen.',
 tracker='A body wave that passed')

add(num=48, file='If-People-See-Me-Anxious-I-Wont-Handle-It',
 key='2 Corinthians 12:9', also=['2 Timothy 1:7','Psalm 56:3','John 14:27','Isaiah 41:10'],
 pearls=['anxiety-worry','fear','self-esteem-low','peace','church'], gc=[5,24,29],
 songs=[('truth','You can be honest about anxiety instead of performing calm.'),('yousay','God’s view of you is not canceled when someone sees you struggle.'),('body','People of faith are meant to welcome a person who is not fine.'),('lovesme','Jesus loves you while you are anxious. Being seen does not erase that.')],
 origins='Many people were taught that anxiety should be hidden: do not cry, do not shake, do not let them see you struggle. A time they were judged, or a time they felt humiliated, sealed the rule. Social fear and anxiety then join. The lie says that if another person notices, you will not be able to cope, and the relationship or the room will be ruined. Being seen is uncomfortable. It is not the same as being destroyed.',
 teaches='God’s grace is sufficient, and His power is made perfect in weakness. Paul even boasts in weakness so that Christ’s power may rest on him. God has not given a spirit of fear, but of power, love, and self-control. The psalmist is afraid and still trusts. Jesus gives peace and says not to let your heart be troubled. “I am with you” does not expire when another person notices you are anxious. You may feel exposed. You are not forsaken, and you are not required to look calm in order to be held by God.',
 replacement='Being seen while I am anxious is uncomfortable, and it is not a disaster. God’s grace is enough for me in front of other people.',
 truths=['Someone can notice my anxiety and I can still cope.','I do not have to look calm for God to be with me.','Grace is sufficient in weakness, including public weakness.','Most people are kinder than the disaster I imagine.','I can be honest with one safe person.','A shaky moment is not a ruined life.'],
 self=['If they see my hands shake, it is over.','I have to look fine or I will fall apart.','Everyone will think I am weak or strange.','I should cancel so no one sees me like this.','I cannot speak if I might cry or blush.','God is disappointed that I cannot hide this better.'],
 errors=[('Mind reading','Deciding what everyone will think if they notice.'),('Catastrophizing','Turning being noticed into social ruin.'),('Fortune telling','Predicting you will be unable to cope once you are seen.'),('All-or-nothing thinking','Either I look perfectly calm or I cannot be there at all.')],
 questions=['What exactly am I afraid people will see, and then what?','When has someone seen me struggle and stayed kind?','Do I require other people to hide their anxiety before I respect them?','What would “coping” look like if it included being visibly nervous?','What does God’s grace cover that my composure does not?','Who is one safe person I can stop performing for?'],
 prompt='When being seen felt unbearable', moment='you wanted to hide your anxiety',
 example='2 Corinthians 12:9 becomes: “<strong>Sarah</strong> can write: “God’s grace is sufficient for me, even if someone sees that I am anxious.””',
 reading='anxiety-worry', read_label='Anxiety/Worry',
 actions=[('<strong>Stay while noticed.</strong> Attend one small gathering or meeting you would skip, and remain even if you feel visibly nervous. Write what people actually did.','Stay while noticed'),
          ('<strong>Tell one safe person</strong> you get anxious, in a single sentence. Notice that the sentence did not ruin you.','Tell one safe person'),
          ('<strong>Drop one disguise.</strong> Skip one behavior you use only to look calm, if it is safe to do so, and see what happens.','Drop one disguise'),
          ('<strong>Read 2 Corinthians 12:9</strong> before a situation where you fear being seen.','Read the grace-in-weakness verse')],
 prayer='Lord, I am afraid of being seen this way. Let Your grace be enough when I cannot look calm. Help me stay, and help me trust that a shaky moment is not the end. Amen.',
 tracker='A time I was seen and still all right')

add(num=49, file='One-Small-Problem-Will-Be-a-Disaster',
 key='Matthew 6:34', also=['Matthew 6:27','Isaiah 41:10','Psalm 46:1','Philippians 4:6–7'],
 pearls=['anxiety-worry','fear','thinking-healthy','peace','trust'], gc=[5,29,30],
 songs=[('even','A hard outcome would not mean God has left, and most small problems never become that.'),('glorious','God’s story is larger than the small trouble in front of you.'),('conquer','You are not at the mercy of every snowballing fear.'),('victory','Christ’s rescue is bigger than a problem that feels like it must ruin everything.')],
 origins='Catastrophizing is anxiety’s shortcut. A strange noise, a mistake at work, a child’s cough, a bill, or a cool tone in someone’s voice is treated as the first step of a chain that ends in ruin. Sometimes a small problem did grow, so the mind now refuses to let any problem stay small. The habit feels like realism. It spends a large fear on a small fact, and then the fear itself becomes the emergency.',
 teaches='Jesus will not let tomorrow’s trouble invade today. “Today has enough trouble of its own.” Worry cannot add an hour to your life. God says do not fear, for He is with you, and He upholds you. He is a refuge and strength, a help in trouble, which means trouble can be met without being crowned as disaster. Prayer is offered instead of anxiety. A small problem may need a small response. It does not need a tragic ending written in advance.',
 replacement='A small problem is still a small problem. I do not have to turn it into a catastrophe. I can take the next step.',
 truths=['I can respond to what is actually here.','Most chains I imagine never happen.','God is with me if a problem grows, and it may not grow.','Worry will not add an hour of safety.','I can fix, wait, or ask for help without calling it ruin.','Today’s trouble is enough. I do not have to import next year’s.'],
 self=['This is how it starts. It always ends badly.','If I do not treat this as serious, I will be sorry.','A small leak means the house is coming down.','I cannot tell the difference anymore.','People who stay calm are not paying attention.','One mistake will cost me everything.'],
 errors=[('Catastrophizing','Building a disaster out of a limited fact.'),('Fortune telling','Writing the tragic ending before the middle of the story.'),('Overgeneralization','Because one problem once grew, every problem will.'),('Magnification','Making a small issue so large it hides the real size.')],
 questions=['What is the fact, in one sentence, with no ending attached?','What are two ordinary explanations besides the disastrous one?','If this stayed the size it is today, what would I do?','Have I predicted ruin from a small start and been wrong?','What would “enough response” look like, short of panic?','What does Jesus say about taking on tomorrow’s trouble today?'],
 prompt='When a small thing felt huge', moment='a small problem turned into a disaster in your mind',
 example='Matthew 6:34 becomes: “<strong>Sarah</strong> can write: “Today’s trouble is enough. I will not borrow a disaster from tomorrow.””',
 reading='thinking-healthy', read_label='Thinking, Healthy',
 actions=[('<strong>Write three endings.</strong> For one current worry, write a mild ending, a medium ending, and the disaster. Circle the one with the most evidence, not the loudest.','Write three endings'),
          ('<strong>Match the response to the size.</strong> Do the small thing the problem actually needs, then stop.','Match the response to the size'),
          ('<strong>Collect false alarms.</strong> Note one small worry this week that did not become a disaster.','Collect false alarms'),
          ('<strong>Pray Matthew 6:34</strong> before you expand a problem in your mind.','Pray about today’s trouble only')],
 prayer='Lord, I turn small things into ruin before they have a chance to stay small. Give me a steady mind. Help me do what today actually requires, and leave tomorrow with You. Amen.',
 tracker='A small problem that stayed small')

add(num=50, file='I-Cant-Relax-Until-Everything-Is-Safe',
 key='Psalm 4:8', also=['Psalm 121:3–4','Isaiah 26:3','Philippians 4:6–7','Matthew 6:34'],
 pearls=['anxiety-worry','peace','trust','sleep-problems','fear'], gc=[5,22,29],
 songs=[('ourgod','God is your safety. Your certainty is not.'),('amen','You can rest in what Christ has done instead of in a finished checklist.'),('held','You are held before every question is answered.'),('tender','Christ invites you to come and rest, not to finish securing the world first.')],
 origins='Safety is good. Anxiety turns it into a condition that can never be met. There is always one more lock, one more test, one more reassurance, one more corner of the future that has not been inspected. People who lived with real unpredictability, or who love people they cannot fully protect, are especially vulnerable to this rule. The lie says rest is allowed only after certainty. Certainty about everything never arrives, so rest never arrives either.',
 teaches='The psalmist sleeps in peace because the Lord, not a completed safety review, makes him dwell in safety. The Protector of Israel does not slumber, which means you may. God keeps in peace the mind that trusts Him. Paul says to be anxious for nothing and to pray, and the peace of God will guard the heart. Jesus refuses to let tomorrow’s unfinished business steal today. You will not reach a moment when every risk is gone. Scripture offers peace before that impossible moment.',
 replacement='I will never be sure of every danger. I can rest before I have certainty, because God is my safety.',
 truths=['Complete certainty is not available, and I can still rest.','God makes me dwell in safety. My checklist does not.','I can be responsible and then stop.','Peace is a gift to receive, not a prize for finishing every fear.','One more check will not create the certainty I am chasing.','I can sleep while God keeps watch.'],
 self=['I will relax when I know everyone is safe.','There is always one more thing to check.','Resting now would be selfish or careless.','If I feel any doubt, I am not allowed to stop.','Other people can live with risk. I cannot.','God wants me to be certain before I am peaceful.'],
 errors=[('All-or-nothing thinking','Either everything is safe or I cannot rest at all.'),('Fortune telling','Believing that the unchecked item is the one that will cause harm.'),('Emotional reasoning','Feeling unfinished and concluding that rest is forbidden.'),('Moving the goalposts','Each time one fear is settled, requiring a new one to be settled before peace is allowed.')],
 questions=['What would “sure enough” be, and have I ever reached it?','Which of my checks actually increase safety, and which only feed the feeling?','What am I refusing to leave in God’s hands?','If I waited for certainty, would I ever sleep?','What does Psalm 4:8 say is the reason for peace?','What is one safety behavior I can lay down tonight?'],
 prompt='When rest felt illegal', moment='you could not relax until everything felt certain',
 example='Psalm 4:8 becomes: “<strong>Sarah</strong> can write: “I can lie down in peace, because the Lord makes me dwell in safety.””',
 reading='peace', read_label='Peace',
 actions=[('<strong>Stop at a set number of checks.</strong> Decide the reasonable checks in advance. When they are done, do not add one more.','Stop at a set number of checks'),
          ('<strong>Rest on purpose for twenty minutes</strong> while one question is still unanswered, if no one is in immediate danger. Write whether harm arrived.','Rest while one question is open'),
          ('<strong>Read Psalm 4:8 at bedtime</strong> and then put the phone away from the worries.','Read the sleep-in-peace verse'),
          ('<strong>Name what only God can secure.</strong> Write one fear you cannot fully control, and pray it instead of checking it.','Pray what you cannot secure')],
 prayer='Lord, I have made certainty the door to rest, and the door never opens. You are the One who makes me dwell in safety. Teach me to lie down before every question is answered. Amen.',
 tracker='A rest I took before I felt certain')

def render(d, head, script):
    kinds, blocks = [], []
    for key, why in d['songs']:
        kind, html = song(key, why)
        kinds.append(kind); blocks.append(html)
    if sorted(kinds) != ['classic','contemporary','contemporary','contemporary'] and kinds.count('classic') != 1:
        raise SystemExit(f"song mix {d['num']} {kinds}")
    if kinds.count('classic') != 1 or len(kinds) != 4:
        raise SystemExit(f"song mix {d['num']} {kinds}")
    for slug in d['pearls']+[d['reading']]:
        if slug not in PEARLS:
            raise SystemExit('pearl '+slug)
    belief = d['belief']
    shown = '“' + belief + '”'
    if '988' in d['origins']:
        raise SystemExit('988 in origins '+str(d['num']))
    errs = '\n'.join(f'<li><strong>{a}: </strong>{b}</li>' for a,b in d['errors'])
    refs = [d['key']] + d['also'][:2]
    scr = '<ul class="opts">\n' + '\n'.join(
        f'<li><span class="ref">{ref}</span><span class="scrip">“{V[ref]}”</span></li>' for ref in refs) + '\n</ul>'
    truths = [d['replacement']] + [t for t in d['truths'] if t != d['replacement']]
    truths = truths[:6]
    acts = '<ul class="opts">\n' + '\n'.join(f'<li>{a}</li>' for a,_ in d['actions']) + '\n</ul>'
    body = f'''<!-- ============ CARD ============ -->
<div class="card belief">
<div class="tag">Psychological/Cognitive False Belief #{d['num']} · Anxiety</div>
<h1>{shown}</h1>
<div class="orn">✦ ✦ ✦</div>

<h2>Where it often comes from</h2>
<p>{d['origins']}</p>

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
{audio('Overcoming Anxiety', ANX, 'about 18 minutes')}

{audio('Overcoming Depression', DEP, 'about 20 minutes')}

<h2>Songs that speak truth to this belief</h2>
<p class="songnote2">Tap a song to play it right here. Three contemporary songs and one classic hymn or older favorite.</p>
<div class="songs">
{chr(10).join(blocks)}
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
{opts(d['questions'])}
<div class="fill"><span>My own question:</span><i></i></div>

<div class="step"><div class="num">3</div><div><h2>My replacement truth</h2><p class="why">The statement I will say to myself instead of the lie.</p></div></div>
{opts(truths)}
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
<li><strong>Reading:</strong> The <a href="{PB}{d['reading']}" target="_blank" rel="noopener">“{d['read_label']}” topic in Pearls</a>.</li>
<li><strong>Listening:</strong> The <a href="{ANX}" target="_blank" rel="noopener">Overcoming Anxiety audio</a> or the <a href="{DEP}" target="_blank" rel="noopener">Overcoming Depression audio</a> by Dr. Brian Campbell. Tap to play.</li>
</ul>

<div class="step"><div class="num">6</div><div><h2>My action step this week</h2><p class="why">Do one thing that tests the lie in real life.</p><p class="why">{STEP}</p></div></div>
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
    # the variables blocks, truths, shown, belief must exist — they are set below before this return is wrong
    return body

def build_page(d, head, script):
    kinds, blocks = [], []
    for key, why in d['songs']:
        kind, html = song(key, why)
        kinds.append(kind); blocks.append(html)
    if kinds.count('classic') != 1 or len(d['songs']) != 4:
        raise SystemExit(f"song mix {d['num']} {kinds}")
    for slug in list(d['pearls'])+[d['reading']]:
        if slug not in PEARLS:
            raise SystemExit('pearl '+slug)
    belief = d['belief']
    shown = '“' + belief + '”'
    if '988' in d['origins']:
        raise SystemExit('opening 988 on '+str(d['num']))
    errs = '\n'.join(f'<li><strong>{a}: </strong>{b}</li>' for a,b in d['errors'])
    refs = [d['key']] + d['also'][:2]
    scr = '<ul class="opts">\n' + '\n'.join(
        f'<li><span class="ref">{ref}</span><span class="scrip">“{V[ref]}”</span></li>' for ref in refs) + '\n</ul>'
    truths = [d['replacement']] + [t for t in d['truths'] if t != d['replacement']]
    truths = truths[:6]
    acts = '<ul class="opts">\n' + '\n'.join(f'<li>{a}</li>' for a,_ in d['actions']) + '\n</ul>'
    # Reuse render's template by calling a cleaned inner function
    page = render_page(d, head, script, blocks, shown, belief, errs, scr, truths, acts)
    fname = f"Psych-{d['num']:03d}-{d['file']}"
    page = page.replace('Psych-032-Things-Will-Never-Get-Better.pdf', fname+'.pdf')
    page = page.replace('Psych-032-Things-Will-Never-Get-Better-Homework.pdf', fname+'-Homework.pdf')
    page = page.replace('Belief Card: Things will never get better', 'Belief Card: ' + belief.rstrip('.'))
    page = page.replace('“Things will never get better.”', shown)
    return page

def render_page(d, head, script, blocks, shown, belief, errs, scr, truths, acts):
    body = f'''<!-- ============ CARD ============ -->
<div class="card belief">
<div class="tag">Psychological/Cognitive False Belief #{d['num']} · Anxiety</div>
<h1>{shown}</h1>
<div class="orn">✦ ✦ ✦</div>

<h2>Where it often comes from</h2>
<p>{d['origins']}</p>

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
{audio('Overcoming Anxiety', ANX, 'about 18 minutes')}

{audio('Overcoming Depression', DEP, 'about 20 minutes')}

<h2>Songs that speak truth to this belief</h2>
<p class="songnote2">Tap a song to play it right here. Three contemporary songs and one classic hymn or older favorite.</p>
<div class="songs">
{chr(10).join(blocks)}
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
{opts(d['questions'])}
<div class="fill"><span>My own question:</span><i></i></div>

<div class="step"><div class="num">3</div><div><h2>My replacement truth</h2><p class="why">The statement I will say to myself instead of the lie.</p></div></div>
{opts(truths)}
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
<li><strong>Reading:</strong> The <a href="{PB}{d['reading']}" target="_blank" rel="noopener">“{d['read_label']}” topic in Pearls</a>.</li>
<li><strong>Listening:</strong> The <a href="{ANX}" target="_blank" rel="noopener">Overcoming Anxiety audio</a> or the <a href="{DEP}" target="_blank" rel="noopener">Overcoming Depression audio</a> by Dr. Brian Campbell. Tap to play.</li>
</ul>

<div class="step"><div class="num">6</div><div><h2>My action step this week</h2><p class="why">Do one thing that tests the lie in real life.</p><p class="why">{STEP}</p></div></div>
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
    return head + body + script

def main():
    src = (ROOT/'belief-cards/psychological/Psych-032-Things-Will-Never-Get-Better.html').read_text()
    head, rest = src.split('<!-- ============ CARD ============ -->', 1)
    script = rest[rest.rfind('\n</div><script>')+1:]
    lst = json.loads((ROOT/'tools/lists/psychological.json').read_text())
    group = next(g for g in lst['sections'][0]['groups'] if g['name']=='Anxiety')
    beliefs = [b[0] for b in group['beliefs']]
    if len(beliefs) != len(C):
        raise SystemExit(f'count {len(beliefs)} vs {len(C)}')
    sets=set()
    outdir = ROOT/'tools/psych-anxiety'
    outdir.mkdir(exist_ok=True)
    for d, belief in zip(C, beliefs):
        d['belief'] = belief
        songset = tuple(k for k,_ in d['songs'])
        if songset in sets:
            raise SystemExit('dup songs '+str(songset))
        sets.add(songset)
        # build_page does filename replace on a string that still has 032 names from head
        page = build_page(d, head, script)
        # build_page's replace looks for 032 names; head still has them. Good.
        fname = f"Psych-{d['num']:03d}-{d['file']}"
        html_path = ROOT/'belief-cards/psychological'/f'{fname}.html'
        html_path.write_text(page)
        if page.find('Listen: Overcoming Anxiety') > page.find('Listen: Overcoming Depression') and page.find('Listen: Overcoming Depression') != -1:
            # Anxiety heading should come first
            if page.find('<h2>Listen: Overcoming Anxiety</h2>') > page.find('<h2>Listen: Overcoming Depression</h2>'):
                raise SystemExit('audio order '+fname)
        meta = {'num': d['num'], 'file': d['file'], 'group': 'Anxiety',
                'belief': '“'+belief+'”', 'belief_plain': belief.rstrip('.'),
                'origins': d['origins'], 'self': d['self'],
                'songs': [k for k,_ in d['songs']], 'key': d['key'],
                'replacement': d['replacement']}
        (outdir/f"{d['num']:03d}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1)+'\n')
        group['beliefs'][d['num']-41][:] = [belief, fname+'.html']
        print(fname, d['key'])
    (ROOT/'tools/lists/psychological.json').write_text(json.dumps(lst, ensure_ascii=False, indent=1)+'\n')
    print('wired', sum(1 for b in group['beliefs'] if len(b)>1))

if __name__ == '__main__':
    main()
