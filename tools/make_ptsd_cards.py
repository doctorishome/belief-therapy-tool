"""Build PTSD cards 51–60 on the same template as the anxiety cards.
Overcoming Anxiety plays first; Overcoming Depression second.
Run: python3 tools/make_ptsd_cards.py
"""
import importlib.util, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('anx', ROOT/'tools/make_anxiety_cards.py')
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
A.V.update({
 'Psalm 27:1': 'The LORD is my light and my salvation— whom shall I fear? The LORD is the stronghold of my life— whom shall I dread?',
 'Psalm 34:18': 'The LORD is near to the brokenhearted; He saves the contrite in spirit.',
 'Psalm 23:4': 'Even though I walk through the valley of the shadow of death, I will fear no evil, for You are with me; Your rod and Your staff, they comfort me.',
 'Psalm 103:13–14': 'As a father has compassion on his children, so the LORD has compassion on those who fear Him. For He knows our frame; He is mindful that we are dust.',
 'Psalm 118:6': 'The LORD is on my side; I will not be afraid. What can man do to me?',
 'Psalm 147:3': 'He heals the brokenhearted and binds up their wounds.',
 'Romans 8:1': 'Therefore, there is now no condemnation for those who are in Christ Jesus.',
 '2 Corinthians 5:17': 'Therefore if anyone is in Christ, he is a new creation. The old has passed away. Behold, the new has come!',
 'Romans 8:38–39': 'For I am convinced that neither death nor life, neither angels nor principalities, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.',
 'Romans 12:15': 'Rejoice with those who rejoice; weep with those who weep.',
 'Galatians 6:2': 'Carry one another’s burdens, and in this way you will fulfill the law of Christ.',
 '2 Corinthians 1:3–4': 'Blessed be the God and Father of our Lord Jesus Christ, the Father of compassion and the God of all comfort, who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves have received from God.',
 'Isaiah 43:2': 'When you pass through the waters, I will be with you; and when you go through the rivers, they will not overwhelm you. When you walk through the fire, you will not be scorched; the flames will not set you ablaze.',
 'Isaiah 61:1': 'The Spirit of the Lord GOD is on Me, because the LORD has anointed Me to preach good news to the poor. He has sent Me to bind up the brokenhearted, to proclaim liberty to the captives and freedom to the prisoners.',
 'Lamentations 3:22–23': 'Because of the loving devotion of the LORD we are not consumed, for His mercies never fail. They are new every morning; great is Your faithfulness!',
 'Psalm 30:5': 'For His anger is fleeting, but His favor lasts a lifetime. Weeping may stay the night, but joy comes in the morning.',
})
COUNSEL = ' A counselor can help you work with this at a pace that is safe. You do not have to do it alone, or all at once.'
CRISIS = ' If you are thinking about ending your life, call or text 988 in the United States, or tell someone near you right away.'
STEP_TOP = 'Choose steps you can do safely. If you are thinking about ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone.'
C = []
def add(**k):
    C.append(k)

add(num=51, file='Nowhere-Is-Really-Safe', crisis=False,
 key='Psalm 46:1', also=['Psalm 27:1','Isaiah 41:10','Psalm 23:4','Deuteronomy 31:8'],
 pearls=['fear','anxiety-worry','trust','peace','god-present-everywhere'], gc=[5,30,27],
 songs=[('fear','God is a stronghold. The world does not have to feel safe before He is with you.'),('battle','You can hand the fear of the next blow to God.'),('storm','You can tell the truth about danger without deciding the whole world is unsafe.'),('lives','Because Jesus lives, this moment is not the only moment there will ever be.')],
 origins='After something overwhelming, the nervous system often stays on duty. A sudden noise, a crowded room, or a quiet night can all feel like the moment before it happens again. That alarm once made sense. The lie is the conclusion that nowhere is really safe, and that danger is certainly about to return. Safety can be wise. A whole world with no safe place is a belief, not a map.',
 teaches='God does not tell wounded people that the world has no danger in it. He says He is a refuge and strength, an ever-present help in trouble. “The LORD is my light and my salvation— whom shall I fear?” He is with you, and He will not forsake you. Even in the valley, the psalmist says, “You are with me.” These verses do not promise that nothing painful will ever happen again. They promise that you are not left without a refuge, and that “nowhere” is too big a word.',
 replacement='The world is not perfectly safe, and I am not without a refuge. God is with me, and I can look for safety one real place at a time.',
 truths=['I can be careful without deciding that nowhere is safe.','God is a refuge in trouble, not only after trouble is gone.','A trigger is not the same thing as the danger returning.','I can name one place, or one person, that is safe enough for today.','I do not have to prove the whole world is safe before I rest.','My counselor and I can go at a pace that does not overwhelm me.'],
 self=['It is about to happen again.','I cannot let my guard down anywhere.','Safe people do not understand.','If I relax, I am asking for it.','Every reminder is a warning.','There is no point going out.'],
 errors=[('Overgeneralization','Turning one unsafe experience into “nowhere is safe.”'),('Fortune telling','Deciding the danger is about to return because your body expects it.'),('Emotional reasoning','Feeling unsafe and treating the feeling as a fact about every place.'),('Catastrophizing','Reading an ordinary moment as the start of the worst.')],
 questions=['What is actually happening right now, apart from the alarm?','Is there one place, or one person, that has been safe enough?','Am I responding to a memory, or to a present threat?','What would “safe enough for the next hour” look like?','What does God promise about being with me, not about a danger-free world?','What has my counselor suggested I do when this alarm gets loud?'],
 prompt='When nowhere felt safe', moment='the alarm said danger was about to return',
 example='Psalm 46:1 becomes: “<strong>Sarah</strong> can write: “God is my refuge. This feeling is not the whole map.””',
 reading='fear', read_label='Fear',
 actions=[('<strong>Name now versus then.</strong> Write “Then” and “Now” in two words each. Do not add the story. Ask whether the danger is in the room today.','Name now versus then'),
          ('<strong>Use one safe anchor.</strong> With your counselor’s guidance, choose one place or person that is safe enough, and stay there for a short, planned time.','Use one safe anchor'),
          ('<strong>Do not scan the whole world.</strong> When the alarm says “nowhere,” list three ordinary things that are steady right now.','Do not scan the whole world'),
          ('<strong>Tell your counselor</strong> how often this alarm comes, and follow the plan you make together. You do not have to figure the pace out alone.','Tell your counselor')],
 prayer='Lord, my body says nowhere is safe. Be my refuge here. Help me tell the difference between a memory and a present danger, and give me one safe place for today. Amen.',
 tracker='A moment that was safer than the alarm said')

add(num=52, file='I-Cant-Trust-Anyone', crisis=False,
 key='Psalm 118:6', also=['Proverbs 3:5–6','1 Peter 5:7','Isaiah 41:10','Psalm 34:18'],
 pearls=['trust','fear','love-by-god','loneliness','friendship'], gc=[17,5,29],
 songs=[('stays','God stays when people have failed you. That does not mean every person will.'),('alone','You are not left without a companion, even when trust feels impossible.'),('knows','Jesus knows what it is to be hurt, and He does not turn that into “trust no one.”'),('friend','You can bring a guarded heart to God before you hand it to a person.')],
 origins='Trust breaks when someone who should have been safe was not. After that, keeping everyone out can feel like the only wisdom left. The lie stretches a real betrayal into a rule about every person, and often about God too. Caution with unsafe people is not the same thing as “I can’t trust anyone.” A counselor can help you sort who is unsafe from who might be safe, without rushing you.',
 teaches='Scripture does not say every person is trustworthy. It does say the Lord is on your side, and that you can trust Him with all your heart instead of leaning only on a frightened understanding. You can cast anxiety on Him because He cares. He is near the brokenhearted. Being hurt taught a hard lesson. It did not prove that no one, and not God, can ever be trusted again. Trust can be small, specific, and slow.',
 replacement='I was hurt, and that does not mean I can never trust anyone. I can trust God, and I can test trust slowly with safe people.',
 truths=['Not every person is the person who hurt me.','I can trust God even while I am careful with people.','Trust can be one small step, not an open door to everyone.','Caution is wise. Total isolation is the lie.','God is near the brokenhearted.','My counselor can help me decide who is safe.'],
 self=['If I let anyone close, I will be hurt again.','Kindness is a setup.','I can only count on myself.','God let it happen, so He is not safe either.','Needing people is how I got hurt.','I would rather be alone than risk it.'],
 errors=[('Overgeneralization','Turning one betrayal into “no one can be trusted.”'),('Fortune telling','Deciding that closeness will certainly end in harm.'),('Mind reading','Assuming a kind person has a hidden motive.'),('All-or-nothing thinking','Either I trust everyone or I trust no one.')],
 questions=['Who specifically broke my trust, and have I made that person stand for everyone?','What would a small, limited trust look like?','Am I protecting myself, or am I refusing every good person too?','What does God say about His care, separate from what people did?','Who has been safe, even in a small way?','What has my counselor said about going slowly?'],
 prompt='When trust felt impossible', moment='closeness felt like a setup',
 example='Psalm 118:6 becomes: “<strong>Sarah</strong> can write: “The Lord is on my side. I do not have to trust everyone to trust Him.””',
 reading='trust', read_label='Trust',
 actions=[('<strong>Separate one person from everyone.</strong> Write the name of who hurt you. Then write “This is not every person.”','Separate one person from everyone'),
          ('<strong>One limited step.</strong> With your counselor, choose one safe person and one small trust, such as a short conversation. Stop there.','One limited step'),
          ('<strong>Notice kindness without explaining it away.</strong> When someone is decent to you, write what they did before you decide it was fake.','Notice kindness'),
          ('<strong>Pray Psalm 118:6</strong> when the rule “trust no one” shows up.','Pray the Lord-is-on-my-side verse')],
 prayer='Lord, I learned not to trust, and the lesson was costly. Be a safe place for me. Help me not to call every person dangerous, and help me go slowly with the people who are. Amen.',
 tracker='A moment of small, real trust')

add(num=53, file='What-Happened-Was-My-Fault', crisis=False,
 key='Romans 8:1', also=['Psalm 103:13–14','Psalm 34:18','Isaiah 61:1','John 14:27'],
 pearls=['guilt-shame','thinking-healthy','self-esteem-low','forgiveness','depression-symptoms-of'], gc=[29,27,24],
 songs=[('voice','The voice that says it was all your fault is not the voice of truth.'),('east','God does not measure you by a blame you were never meant to carry.'),('name','God names you as His, not as the cause of what was done.'),('amazing','Grace meets you here. You do not have to finish the story by blaming yourself.')],
 origins='People who were hurt often search for a reason they could have controlled. “If it was my fault, then I can make sure it never happens again.” That search feels like safety. It is usually a lie that piles shame on top of harm. You did not have to see it coming. You did not have to stop what someone else chose, or what you had no power to prevent. A counselor can help you lay down a blame that was never yours, without forcing the details.',
 teaches='There is no condemnation for those who are in Christ Jesus. The Lord has compassion and knows our frame. He is near the brokenhearted. He binds up the brokenhearted and proclaims liberty. Jesus tells His friends not to let their hearts be troubled. None of these verses say that suffering is proof you caused it. Self-blame can feel responsible. It is not the same thing as truth, and it is not what God asks of a wounded person.',
 replacement='What happened was not mine to stop just because I wish I had. I am not condemned, and I do not have to carry blame that is not mine.',
 truths=['Wanting to have stopped it does not mean I caused it.','I can grieve without putting myself on trial.','God does not condemn me for what I could not prevent.','Shame is not the same thing as guilt.','I can tell the truth about responsibility with a counselor, slowly.','I am allowed to be a person who was hurt, not the cause of it.'],
 self=['I should have known.','If I had been smarter, braver, or quieter, it would not have happened.','A good person would have stopped it.','God must think it was my fault too.','I do not deserve comfort.','If I blame myself, at least the world makes sense.'],
 errors=[('Personalization','Taking blame for what another person did, or for what you could not control.'),('Hindsight bias','Judging your past self with information you did not have then.'),('Emotional reasoning','Feeling guilty and concluding you are guilty.'),('All-or-nothing thinking','If you did not prevent it perfectly, it was entirely your fault.')],
 questions=['What, exactly, do I believe I should have done, and could I really have done it then?','Whose choice was it, if I set my self-blame aside?','Would I blame a friend who lived through the same thing?','Am I using blame to feel less helpless?','What does “no condemnation” mean for a person who was hurt?','What would my counselor want me to stop saying to myself?'],
 prompt='When you put yourself on trial', moment='you blamed yourself for what happened',
 example='Romans 8:1 becomes: “<strong>Sarah</strong> can write: “I wish I had stopped it. That wish is not a conviction. In Christ I am not condemned.””',
 reading='guilt-shame', read_label='Guilt/Shame',
 actions=[('<strong>Write the charge, then the facts.</strong> One sentence of self-blame. Then one sentence a fair friend would say. Do not add graphic detail.','Write the charge, then the facts'),
          ('<strong>Ask your counselor</strong> to help you sort real responsibility from blame that is not yours. Stop if it becomes too much.','Ask your counselor'),
          ('<strong>Refuse one “I should have.”</strong> When the sentence starts, say, “I did not have to see it coming,” and stop.','Refuse one “I should have”'),
          ('<strong>Read Romans 8:1</strong> each morning before you review the past.','Read the no-condemnation verse')],
 prayer='Lord, I have put myself on trial for something I could not carry. There is no condemnation in Christ. Teach me the difference between grief and guilt, and give me a counselor’s help as I lay this down. Amen.',
 tracker='A moment I did not take the blame')

add(num=54, file='Im-Permanently-Damaged', crisis=True,
 key='Psalm 147:3', also=['Isaiah 61:1','2 Corinthians 12:9','2 Corinthians 5:17','Psalm 34:18'],
 pearls=['self-esteem-low','sorrow','depression-symptoms-of','hopeless','love-by-god'], gc=[12,27,24],
 songs=[('allnew','God makes things new. Damage is not His last word about you.'),('broken','God works with wounded people. He does not discard them.'),('yousay','What God says about you is not “ruined forever.”'),('assurance','You belong to Christ. What happened does not get to name you.')],
 origins='Harm can leave real marks: fear, numbness, shame, a life that does not feel like the one you had. Those marks matter. The lie is the word “permanently,” and the claim that you will never be yourself again. Healing is often slow and incomplete in the way people wish, and it is not the same as being finished as a person. You do not have to describe what happened in order to question this sentence. A counselor can walk with you.',
 teaches='God heals the brokenhearted and binds up their wounds. He sends good news and liberty to the captive, not a label of permanent ruin. His grace is sufficient, and His power is made perfect in weakness. Anyone in Christ is a new creation. He is near the brokenhearted. These promises do not mean you should feel like your old self by Friday. They mean “never” and “permanently” are bigger than the evidence, and bigger than the gospel.',
 replacement='I was hurt, and I am not permanently ruined. God is healing what I cannot rush, and I can still be myself in His hands.',
 truths=['A wound is not a finished identity.','I may not feel like myself yet, and that is not the same as never.','God binds up the brokenhearted.','Grace is enough in weakness.','I can heal slowly, with a counselor, without having to be who I was.','I am more than what happened to me.'],
 self=['I am ruined.','The real me is gone.','People who heal were not hurt like I was.','If I am not better yet, I never will be.','I should not hope. It will only hurt.','God cannot do anything with someone this damaged.'],
 errors=[('Fortune telling','Deciding that because you are not healed yet, you never will be.'),('Labeling','Calling your whole self ruined because you carry wounds.'),('All-or-nothing thinking','If you are not your old self, you are permanently destroyed.'),('Discounting the positive','Ignoring any strength, love, or small change that is still yours.')],
 questions=['What is still true about me that this sentence erases?','Am I asking healing to be finished before I will believe it can happen?','Would I tell a wounded friend they are permanently ruined?','What small sign of life have I noticed, even if I do not trust it yet?','What does God do with the brokenhearted?','What pace has my counselor said is honest for me?'],
 prompt='When you felt permanently ruined', moment='being yourself again felt impossible',
 example='Psalm 147:3 becomes: “<strong>Sarah</strong> can write: “God binds up the brokenhearted. I am wounded, and I am not finished.””',
 reading='hopeless', read_label='Hopeless',
 actions=[('<strong>Name what remains.</strong> Write three things that are still you: a value, a love, a skill. No details of the harm.','Name what remains'),
          ('<strong>Talk with your counselor</strong> about the word “permanently.” Ask what slow healing has looked like for others. Stop if you need to.','Talk with your counselor'),
          ('<strong>Do one ordinary thing that is yours</strong> this week, something you liked before or still like a little.','Do one ordinary thing that is yours'),
          ('<strong>If “never” includes wanting to die,</strong> call or text 988, or tell your counselor or someone near you today.','Get help if you want to die')],
 prayer='Lord, I feel ruined and afraid I will never be myself. Bind up what is broken. Do not let this wound be my name. Give me patience, and a counselor to walk with me. Amen.',
 tracker='A moment I was still myself')

add(num=55, file='My-Future-Holds-Only-More-Pain', crisis=True,
 key='Lamentations 3:22–23', also=['Psalm 30:5','Psalm 147:3','Romans 8:38–39','Isaiah 43:2'],
 pearls=['hopeless','sorrow','depression-symptoms-of','peace','suffering'], gc=[12,27,15],
 songs=[('hope','The future is not only the pain behind you. Christ is a living hope.'),('forever','Resurrection says pain does not own the last chapter.'),('heaven','There is a future with God that this hurt does not get to cancel.'),('faithful','Mercies are new in the morning, even when today still hurts.')],
 origins='When pain has lasted, the mind protects itself by expecting more of the same. “If I do not hope, I cannot be disappointed.” That can feel like realism. It is a closed future: only more pain, never safe, never whole. You do not have to pretend the past was small. You also do not have to sign away every year ahead. A counselor can help you hold both the wound and a future that is not only the wound.',
 teaches='The Lord’s mercies are new every morning. Weeping may stay the night, and joy comes in the morning. God heals the brokenhearted. Nothing in the present or the future can separate His people from His love. When you pass through deep waters, He is with you, and the waters do not get the last word. These verses do not say the pain was good, or that you must feel whole today. They say “only more pain” is a forecast you do not have to believe.',
 replacement='My future is not only more pain. God is with me, His mercy is new, and wholeness can grow even while I still hurt.',
 truths=['I do not know the whole future, and pain does not get to write it.','God’s mercy is new this morning.','I can hurt today and still not be doomed to only hurt.','Nothing in the future can separate me from God’s love.','I can take one day, with a counselor’s help, without settling every year.','Feeling unsafe is not the same as a future with no safety.'],
 self=['The rest of my life will feel like this.','Hoping is a trick.','I will never feel safe or whole, so I should stop wanting that.','Good things are for people who were not hurt.','If God loved me, the future would already look different.','I should not make plans.'],
 errors=[('Fortune telling','Writing every future year from today’s pain.'),('Overgeneralization','Turning a long wound into “only pain from now on.”'),('Emotional reasoning','Feeling hopeless and calling that a fact about the future.'),('Discounting the positive','Refusing any mercy, relationship, or ease that does not fit the forecast.')],
 questions=['What do I actually know about next year, and what am I guessing?','Has any day been even slightly different from the worst day?','Would I tell a friend their whole future is only pain?','What is one small plan that does not require me to feel whole first?','What does “mercies new every morning” allow me to expect besides a perfect life?','Who can help me look at the future without being flooded?'],
 prompt='When the future felt like only pain', moment='hope felt like a trick',
 example='Lamentations 3:22–23 becomes: “<strong>Sarah</strong> can write: “His mercies are new this morning. Today is not the whole future.””',
 reading='hopeless', read_label='Hopeless',
 actions=[('<strong>One small plan.</strong> Schedule one ordinary good thing this week. You do not have to feel whole to keep it.','One small plan'),
          ('<strong>Write “I don’t know yet”</strong> next to a fear about the future. Leave it unknown instead of tragic.','Leave the future unknown'),
          ('<strong>Tell your counselor</strong> that the future feels like only pain. Let them help you go slowly.','Tell your counselor'),
          ('<strong>If this includes wanting to die,</strong> call or text 988, or tell someone near you today. You do not have to carry a closed future alone.','Get help if you want to die')],
 prayer='Lord, I have decided the future is only pain. Your mercies are new this morning. Stay with me, open a little room in the days ahead, and give me people who will walk there with me. Amen.',
 tracker='A moment the future was not only pain')

add(num=56, file='I-Have-No-Control', crisis=False,
 key='Isaiah 43:2', also=['Deuteronomy 31:8','Psalm 46:1','Philippians 4:13','Psalm 121:3–4'],
 pearls=['fear','trust','anxiety-worry','thinking-healthy','god-all-powerful'], gc=[5,30,29],
 songs=[('greater','You do not have to control what already happened in order to be held.'),('power','God’s power is present where yours ran out.'),('conquer','Not being in control of the past is not the same as being defeated now.'),('victory','Christ’s victory does not depend on you having stopped what happened.')],
 origins='Helplessness is one of the hardest parts of being hurt. If you could not stop it, the mind may decide you can never stop anything like it. “I have no control” feels true because, in that moment, you did not. The lie makes that moment the rule for every future moment. You still cannot control other people’s choices. You can have choices now: a boundary, a call, a counselor, a next step. Those are small, and they are real.',
 teaches='God does not say you were in control of the waters or the fire. He says when you pass through them, He is with you, and they will not overwhelm you. He will not leave you. He is a refuge and strength. Christ gives strength. The Protector of Israel does not sleep. None of this gives you a button to rewind what happened. It does mean “nothing I do can ever matter” is larger than the truth. You are not God, and you are not powerless in the life you have now.',
 replacement='I could not control what happened. I am not powerless now. God is with me, and I can take one real step today.',
 truths=['Not controlling the past is not the same as having no choices now.','God is with me in what I cannot steer.','I can choose one safe step without controlling other people.','Strength is given. I do not have to invent it.','A boundary is a form of power.','My counselor can help me see the choices I still have.'],
 self=['If it happened once, it will happen no matter what I do.','Trying is pointless.','I am a passenger in my own life.','Other people have choices. I do not.','Safety depends on me controlling everything, and I cannot.','I should not bother.'],
 errors=[('Overgeneralization','Turning one helpless moment into “I can never affect anything.”'),('Fortune telling','Deciding the next chapter is already fixed because the last one was.'),('All-or-nothing thinking','Either I control everything or I control nothing.'),('Discounting the positive','Ignoring the choices, helps, and boundaries you do have now.')],
 questions=['What was truly outside my control then?','What is one choice I do have today?','Am I trying to control other people so I can feel safe?','What would a small boundary look like?','Where does God promise to be when I cannot steer the outcome?','What step has my counselor said is mine to take, and what is not?'],
 prompt='When you felt you had no choices', moment='everything felt already decided',
 example='Isaiah 43:2 becomes: “<strong>Sarah</strong> can write: “I could not stop the waters. God is with me in them, and I still have a step I can take.””',
 reading='trust', read_label='Trust',
 actions=[('<strong>List two kinds of control.</strong> Write what you cannot control, and one thing you can, such as a boundary or a phone call.','List two kinds of control'),
          ('<strong>Take that one step</strong> this week. Keep it small and safe. Tell your counselor if it stirs you up.','Take that one step'),
          ('<strong>Do not rehearse powerlessness.</strong> When the sentence starts, add, “That was then. Today I can ___.”','Do not rehearse powerlessness'),
          ('<strong>Pray Isaiah 43:2</strong> without asking to become the one who controls everything.','Pray the “I will be with you” verse')],
 prayer='Lord, I could not stop what happened, and I have called myself powerless ever since. Be with me. Show me the one step that is actually mine, and give me strength to take it. Amen.',
 tracker='A choice I still had')

add(num=57, file='Other-People-Can-See-I-Am-Different', crisis=False,
 key='Psalm 34:18', also=['Romans 8:38–39','2 Corinthians 12:9','Isaiah 61:1','John 14:27'],
 pearls=['self-esteem-low','loneliness','friendship','love-by-god','thinking-healthy'], gc=[24,17,29],
 songs=[('truth','You can be honest about being changed without deciding everyone is backing away.'),('body','The people of God are called to come near, not to keep their distance.'),('who','God’s love, not other people’s stare, is what names you.'),('lovesme','Jesus loves you as you are, including the ways you have been changed.')],
 origins='Being hurt can change how you carry yourself. You may feel marked, odd, or easy to spot. Sometimes people really have been clumsy or distant. The lie says they can see that you are different and therefore they will keep away, as if your wound were a sign on your face. Most people cannot read your history. Some who know it can stay. You do not have to explain what happened in order to test this. A counselor can help you sort fear from fact.',
 teaches='The Lord is near the brokenhearted. He does not keep His distance from wounds. Nothing can separate you from the love of God in Christ. Grace is sufficient when you feel exposed. God binds up the brokenhearted rather than stepping back from them. Jesus says not to let your heart be troubled. People are limited and sometimes unkind. Their distance, real or imagined, is not God’s posture toward you, and it is not a law that everyone will leave.',
 replacement='Some people may notice I am struggling, and that does not mean everyone will keep their distance. God is near, and safe people can stay.',
 truths=['My history is not written on my face.','God draws near to the brokenhearted.','One person’s distance is not everyone’s.','I can be changed and still be lovable.','I do not owe anyone the story.','I can let one safe person come closer, at my pace.'],
 self=['They can tell.','If they knew, they would step back.','I should stay away so I do not make people uncomfortable.','I am too different to belong.','Looking fine is the only way to be tolerated.','God is probably keeping His distance too.'],
 errors=[('Mind reading','Deciding you know that people see your past and will leave.'),('Overgeneralization','Turning one awkward reaction into “everyone will keep away.”'),('Labeling','Calling yourself too different to belong.'),('Emotional reasoning','Feeling exposed and concluding that you are exposed to everyone.')],
 questions=['What do people actually see, and what am I sure they know?','Who has come closer instead of stepping back?','Do I pull away first and then call it their distance?','Would I avoid a friend who had been hurt?','What does God do with the brokenhearted?','What would letting one safe person stay look like, without telling more than I want?'],
 prompt='When you felt too different to be near', moment='you were sure people would step back',
 example='Psalm 34:18 becomes: “<strong>Sarah</strong> can write: “The Lord is near the brokenhearted. I do not have to hide to be met.””',
 reading='loneliness', read_label='Loneliness',
 actions=[('<strong>Test one interaction.</strong> Have one ordinary conversation without explaining your history. Write whether the person actually withdrew.','Test one interaction'),
          ('<strong>Ask your counselor</strong> what is fear and what is a real pattern of people leaving. Do not decide alone.','Ask your counselor'),
          ('<strong>Let one safe person know you are having a hard day</strong> without telling the story. Notice if they stay.','Let one safe person know'),
          ('<strong>Read Psalm 34:18</strong> when you want to disappear from a room.','Read the near-the-brokenhearted verse')],
 prayer='Lord, I feel marked and sure that people will back away. You draw near to the brokenhearted. Help me not to hide from every person, and help me trust the ones who are safe. Amen.',
 tracker='A person who did not step back')

add(num=58, file='When-My-Body-Reacts-the-Danger-Is-Now', crisis=False,
 key='Psalm 94:19', also=['Psalm 46:1','Isaiah 43:2','2 Timothy 1:7','John 14:27'],
 pearls=['anxiety-worry','fear','peace','trust','suffering'], gc=[5,27,29],
 songs=[('liar','A body alarm can lie about what time it is.'),('held','You can be held while your body remembers.'),('worn','A worn-out body is not the same thing as a present danger.'),('tender','Christ meets you gently in the alarm. You do not have to be ashamed of it.')],
 origins='The body remembers. A smell, a tone of voice, a posture, or a sudden sensation can bring a wave of fear, numbness, or the urge to flee, even when the room is safe. That reaction is not you being dramatic. The lie is the interpretation: “Because my body reacts, the danger is happening now, and I am not safe even here.” A counselor can help you tell a memory in the body from a threat in the room, without making you relive anything.',
 teaches='When anxiety overwhelms, God’s consolation is for the soul. He is a refuge and strength, an ever-present help. When you pass through deep waters, He is with you and they do not overwhelm you. He has not given a spirit of fear, but of power, love, and self-control. Jesus gives peace and says not to let your heart be troubled. A reacting body is real. It is not, by itself, proof that the danger has returned or that this place is unsafe.',
 replacement='My body can react to a memory without the danger being here now. I can be startled and still be safe, and God is with me.',
 truths=['A body alarm is not a time machine.','I can be triggered and still be in a safe room.','God is a refuge while my body is loud.','I do not have to explain the reaction in order to ride it out.','This wave can peak and pass.','My counselor and I can make a plan for these moments.'],
 self=['It is happening again.','I have to get out or I will not survive this feeling.','If my heart is racing, I am in danger.','I am not safe in my own home, my church, or my car.','I should be over these reactions by now.','God is far away when I feel like this.'],
 errors=[('Emotional reasoning','Treating a body sensation as proof of present danger.'),('Fortune telling','Deciding the feeling will not pass, or that harm is seconds away.'),('Overgeneralization','Because the body reacts here, nowhere in the present is safe.'),('Catastrophizing','Turning a wave of memory into a present emergency.')],
 questions=['What year is it, and who is actually in the room?','Is this sensation familiar from a memory rather than from what I see now?','Has this wave passed before?','What would my counselor tell me to do in the first minute?','What is one thing I can touch or name that belongs to today?','Where is God while this is loud, according to Scripture?'],
 prompt='When your body said the danger was now', moment='a reaction felt like the past had returned',
 example='Psalm 94:19 becomes: “<strong>Sarah</strong> can write: “Anxiety is overwhelming me, and God’s consolation is here. This is not the old danger.””',
 reading='anxiety-worry', read_label='Anxiety/Worry',
 actions=[('<strong>Orient to today.</strong> When a wave comes, name the date, the room, and one safe person, out loud if you can. Do not tell the story.','Orient to today'),
          ('<strong>Ride one wave with a plan</strong> you and your counselor already agreed on. If you do not have a plan, ask for one before you experiment.','Ride one wave with a plan'),
          ('<strong>Note that it passed.</strong> Afterward, write only “It rose and it fell,” not what you remembered.','Note that it passed'),
          ('<strong>Do not face this alone.</strong> Tell your counselor how often the body alarm comes. Follow their pace.','Tell your counselor')],
 prayer='Lord, my body says the danger is here. Console me. Help me know the difference between a memory and this room, and stay with me until the wave falls. Amen.',
 tracker='A body alarm that was not present danger')

add(num=59, file='If-I-Talk-About-It-I-Will-Fall-Apart', crisis=False,
 key='2 Corinthians 1:3–4', also=['Galatians 6:2','Romans 12:15','Psalm 34:18','Isaiah 61:1'],
 pearls=['sorrow','suffering','help','trust','thinking-healthy'], gc=[27,17,22],
 songs=[('speak','Truth can be spoken in pieces. You do not have to say everything.'),('younger','God meets the younger, wounded part of you with kindness, not a demand to spill it all.'),('even','You can bring a little of the truth even if you do not feel ready for all of it.'),('glory','God’s glory includes binding up what is broken, not forcing it into the open.')],
 origins='Silence often kept you going. Talking can feel like opening a door you cannot shut, as if one sentence would undo you in front of someone. That fear deserves respect. The lie says any word will make you fall apart, so the only safe choice is to lock it all inside. Many people find that a small, chosen sentence, with a counselor, does not destroy them. You never have to tell everything. You never have to tell it before you are ready.',
 teaches='God is the Father of compassion and the God of all comfort, and He comforts us so that comfort can be shared. We are told to carry one another’s burdens, and to weep with those who weep. The Lord is near the brokenhearted. He binds up the brokenhearted. None of this is a command to disclose your story on demand. It is a promise that comfort exists outside of silence, and that falling apart is not the certain result of one true, careful sentence with a safe person.',
 replacement='I do not have to tell everything. One careful sentence, with a safe person or my counselor, does not have to make me fall apart.',
 truths=['Silence kept me going, and it does not have to be my only tool.','I choose what to say, and when, and to whom.','God comforts. He does not force my story out of me.','A counselor can help me say a little without being flooded.','Feeling stirred is not the same as falling apart.','I can stop a conversation when I need to.'],
 self=['If I start, I will not be able to stop.','No one can handle hearing it, and neither can I.','Keeping it inside is the only adult thing to do.','Needing to talk means I am weak.','One word will ruin the rest of my day, or my life.','God wants me to pretend I am fine.'],
 errors=[('Fortune telling','Deciding that any word will certainly shatter you.'),('All-or-nothing thinking','Either I tell everything or I tell nothing.'),('Catastrophizing','Treating emotion that rises as proof you will not recover the day.'),('Mind reading','Assuming no one could bear a single careful sentence.')],
 questions=['What am I afraid will happen if I say one sentence, not the whole story?','Have I ever said a little and remained myself afterward?','Who is actually safe enough for a small truth?','Do I have permission, including from myself, to stop?','What kind of comfort does Scripture describe, and does it require a full account?','What pace has my counselor offered?'],
 prompt='When talking felt like it would undo you', moment='a single word felt too dangerous',
 example='2 Corinthians 1:3 becomes: “<strong>Sarah</strong> can write: “God is the God of comfort. I can say a little, and I can stop.””',
 reading='help', read_label='Help',
 actions=[('<strong>Do not start with the story.</strong> With your counselor, practice saying only “This is hard to talk about.” Stop there if you need to.','Practice one safe sentence'),
          ('<strong>Agree on a stop signal</strong> with your counselor or a safe person before any harder conversation.','Agree on a stop signal'),
          ('<strong>Write one sentence you are willing to say,</strong> with no graphic detail, and decide later whether to share it.','Write one sentence you might say'),
          ('<strong>After any conversation, do something ordinary</strong> that reminds you that you did not disappear.','Do something ordinary afterward')],
 prayer='Lord, I am afraid that speaking will undo me. You are the God of comfort. Give me a safe person, a slow pace, and the freedom to say a little and then stop. Amen.',
 tracker='A word I survived saying')

add(num=60, file='If-I-Care-They-Will-Be-Hurt', crisis=False,
 key='1 John 4:18', also=['John 15:9','Romans 8:38–39','Psalm 34:18','Galatians 6:2'],
 pearls=['love-by-god','friendship','fear','trust','sorrow'], gc=[17,15,27],
 songs=[('love','God’s love can take you over without putting the people you love in danger.'),('jesus','Jesus stayed near suffering. Love did not make Him a danger to others.'),('want','You can follow love without controlling every outcome.'),('eyes','Look at Christ’s love, not at the fear that caring will destroy someone.')],
 origins='Some people come to believe that their love is dangerous. If they care, the other person will be hurt, leave, or be taken. Sometimes loss taught that lesson with terrible force. The lie says your affection is the cause, so the safe life is a life without closeness. Love is not a weapon you are carrying. You can care, with wisdom and with help, without deciding that your heart puts people in harm’s way. A counselor can help you untangle grief from this rule.',
 teaches='Perfect love casts out fear. There is a kind of fear that has to do with punishment, and it does not belong in love. Jesus loves His friends and tells them to remain in that love. Nothing can separate you from the love of God. The Lord is near the brokenhearted, including when love and loss have gotten tangled. We are called to carry one another’s burdens, which means closeness is part of how God intends care to move. Your love is not a curse on the people you cherish.',
 replacement='Caring about someone does not put them in danger. I can love, with wisdom, without calling my heart the cause of harm.',
 truths=['My love is not a threat.','Loss is not proof that caring caused it.','I can be close and still be wise.','God’s love is not something I will ruin by receiving it.','Grief and love can exist together.','A counselor can help me stop punishing closeness.'],
 self=['If I love them, something bad will happen to them.','I should keep my distance for their sake.','People are safer when I do not care.','Getting close is selfish.','I destroy what I love.','God’s love is for other people, not for someone like me.'],
 errors=[('Fortune telling','Deciding that your care will cause future harm.'),('Personalization','Making yourself the cause of a loss you could not prevent.'),('Overgeneralization','Turning one loss into a rule that love is dangerous.'),('Emotional reasoning','Feeling afraid of closeness and calling that fear proof.')],
 questions=['What loss am I treating as proof that my love causes harm?','Would I tell a grieving friend to stop loving so their people will be safe?','What is the difference between reasonable care and this fearful rule?','Who has been close to me and has not been harmed by that closeness?','What does Scripture say love does with fear?','What would one ordinary act of care look like this week, without a vow of distance?'],
 prompt='When loving someone felt dangerous', moment='closeness felt like it would cause harm',
 example='1 John 4:18 becomes: “<strong>Sarah</strong> can write: “Love does not have to be mixed with this fear. My care is not a curse.””',
 reading='love-by-god', read_label='Love, By God',
 actions=[('<strong>Separate love from the loss.</strong> Write “I care” and “What I could not prevent” on two lines. Do not make the first line the cause of the second.','Separate love from the loss'),
          ('<strong>One ordinary kindness.</strong> Do one small caring thing for someone safe, with your counselor’s blessing if this belief is very loud.','One ordinary kindness'),
          ('<strong>Notice who is all right.</strong> After you care, write what actually happened to them that day, not what you feared.','Notice who is all right'),
          ('<strong>Talk with your counselor</strong> about where this rule came from, without going into graphic detail.','Talk with your counselor')],
 prayer='Lord, I have treated my love as something dangerous. Your love casts out fear. Teach me that caring is not a curse, and walk with me as I risk ordinary closeness again. Amen.',
 tracker='A moment of care that did not cause harm')

# 1 John 4:18 must be in V
A.V['1 John 4:18'] = 'There is no fear in love, but perfect love drives out fear, because fear involves punishment. The one who fears has not been perfected in love.'
# John 15:9 may already be absent
A.V['John 15:9'] = 'As the Father has loved Me, so have I loved you. Remain in My love.'

def main():
    src = (ROOT/'belief-cards/psychological/Psych-041-Something-Terrible-Is-About-to-Happen.html').read_text()
    head, rest = src.split('<!-- ============ CARD ============ -->', 1)
    script = rest[rest.rfind('\n</div><script>')+1:]
    lst = json.loads((ROOT/'tools/lists/psychological.json').read_text())
    group = next(g for g in lst['sections'][0]['groups'] if g['name']=='PTSD')
    beliefs = [b[0] for b in group['beliefs']]
    if len(beliefs) != len(C):
        raise SystemExit(f'count {len(beliefs)} vs {len(C)}')
    sets=set(); outdir=ROOT/'tools/psych-ptsd'; outdir.mkdir(exist_ok=True)
    for d, belief in zip(C, beliefs):
        d['belief']=belief
        songset=tuple(k for k,_ in d['songs'])
        if songset in sets:
            raise SystemExit('dup '+str(songset))
        sets.add(songset)
        kinds=[]
        blocks=[]
        for key, why in d['songs']:
            kind, html = A.song(key, why)
            kinds.append(kind); blocks.append(html)
        if kinds.count('classic')!=1 or len(kinds)!=4:
            raise SystemExit(f'mix {d["num"]} {kinds}')
        for slug in list(d['pearls'])+[d['reading']]:
            if slug not in A.PEARLS:
                raise SystemExit('pearl '+slug)
        if '988' in d['origins']:
            raise SystemExit('988 baked into origins '+str(d['num']))
        d['origins'] = d['origins'] + COUNSEL + (CRISIS if d['crisis'] else '')
        A.STEP = STEP_TOP if d['crisis'] else A.STEP if False else (
            STEP_TOP if d['crisis'] else 'Choose steps you can do safely. If this belief comes with hopelessness or thoughts of ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone.')
        shown='“'+belief+'”'
        errs='\n'.join(f'<li><strong>{a}: </strong>{b}</li>' for a,b in d['errors'])
        refs=[d['key']]+d['also'][:2]
        scr='<ul class="opts">\n'+'\n'.join(f'<li><span class="ref">{ref}</span><span class="scrip">“{A.V[ref]}”</span></li>' for ref in refs)+'\n</ul>'
        truths=[d['replacement']]+[t for t in d['truths'] if t!=d['replacement']]
        truths=truths[:6]
        acts='<ul class="opts">\n'+'\n'.join(f'<li>{a}</li>' for a,_ in d['actions'])+'\n</ul>'
        page=A.render_page(d, head, script, blocks, shown, belief, errs, scr, truths, acts)
        page=page.replace('· Anxiety</div>', '· PTSD</div>', 1)
        fname=f"Psych-{d['num']:03d}-{d['file']}"
        page=page.replace('Psych-041-Something-Terrible-Is-About-to-Happen-Homework.pdf', fname+'-Homework.pdf')
        page=page.replace('Psych-041-Something-Terrible-Is-About-to-Happen.pdf', fname+'.pdf')
        page=page.replace('Belief Card: Something terrible is about to happen', 'Belief Card: '+belief.rstrip('.'))
        page=page.replace('“Something terrible is about to happen.”', shown)
        if page.find('<h2>Listen: Overcoming Anxiety</h2>') > page.find('<h2>Listen: Overcoming Depression</h2>'):
            raise SystemExit('audio order '+fname)
        (ROOT/'belief-cards/psychological'/f'{fname}.html').write_text(page)
        (outdir/f"{d['num']:03d}.json").write_text(json.dumps({
            'num': d['num'], 'file': d['file'], 'group': 'PTSD',
            'belief': '“'+belief+'”', 'belief_plain': belief.rstrip('.'),
            'origins': d['origins'], 'self': d['self'],
            'songs': [k for k,_ in d['songs']], 'key': d['key'],
            'replacement': d['replacement'], 'crisis': d['crisis'],
        }, ensure_ascii=False, indent=1)+'\n')
        group['beliefs'][d['num']-51][:] = [belief, fname+'.html']
        print(d['num'], d['key'], 'crisis', d['crisis'], 'open988', '988' in d['origins'])
    (ROOT/'tools/lists/psychological.json').write_text(json.dumps(lst, ensure_ascii=False, indent=1)+'\n')
    print('wired', sum(1 for b in group['beliefs'] if len(b)>1))

if __name__=='__main__':
    main()
