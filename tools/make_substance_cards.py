"""Build Substance Abuse cards 71–80 on the anxiety/PTSD card template.
Compassionate and non-shaming. SAMHSA and a doctor-before-withdrawal note are on every card.
Run: python3 tools/make_substance_cards.py
"""
import importlib.util, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('anx', ROOT/'tools/make_anxiety_cards.py')
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
A.V.update({
 'John 8:36': 'So if the Son sets you free, you will be free indeed.',
 'Matthew 11:28': 'Come to Me, all you who are weary and burdened, and I will give you rest.',
 'Proverbs 27:1': 'Do not boast about tomorrow, for you do not know what a day may bring.',
 'Lamentations 3:22–23': 'Because of the loving devotion of the LORD we are not consumed, for His mercies never fail. They are new every morning; great is Your faithfulness!',
 'Psalm 42:11': 'Why are you downcast, O my soul? Why the unease within me? Put your hope in God, for I will yet praise Him, my Savior and my God.',
 '1 Corinthians 6:12': '‘Everything is permissible for me,’ but not everything is beneficial. ‘Everything is permissible for me,’ but I will not be mastered by anything.',
 'Psalm 121:1–2': 'I lift up my eyes to the hills. From where does my help come? My help comes from the LORD, the Maker of heaven and earth.',
 'Romans 14:7': 'For none of us lives to himself alone, and none of us dies to himself alone.',
 'Isaiah 43:18–19': '‘Do not call to mind the former things; pay no attention to the things of old. Behold, I am about to do something new; even now it is coming. Do you not see it? Indeed, I will make a way in the wilderness and streams in the desert.’',
 'Hebrews 4:16': 'Let us then approach the throne of grace with confidence, so that we may receive mercy and find grace to help us in our time of need.',
 'Psalm 139:14': 'I praise You, for I am fearfully and wonderfully made. Marvelous are Your works, and I know this very well.',
 'Psalm 34:18': 'The LORD is near to the brokenhearted; He saves the contrite in spirit.',
 'Romans 8:1': 'Therefore, there is now no condemnation for those who are in Christ Jesus.',
 'Isaiah 41:10': 'Do not fear, for I am with you; do not be afraid, for I am your God. I will strengthen you; I will surely help you; I will uphold you with My right hand of righteousness.',
})
HELP = ' If you want help, call the SAMHSA National Helpline at 1-800-662-4357. Do not try to stop or withdraw on your own if that could make you sick. A doctor can help you do it safely, and a counselor can walk with you. Needing that help is not a failure.'
CRISIS = ' If you are thinking about ending your life, call or text 988 in the United States, or tell someone near you right away.'
STEP_TOP = 'Choose steps you can do safely. If you are thinking about ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. For help with substance use, call 1-800-662-4357, and talk with a doctor before you stop if withdrawal could make you sick.'
STEP_MILD = 'Choose steps you can do safely. If this belief comes with hopelessness or thoughts of ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. For help with substance use, call 1-800-662-4357, and talk with a doctor before you stop if withdrawal could make you sick.'
C = []
def add(**k):
    C.append(k)

add(num=71, file='I-Can-Control-It', crisis=False,
 key='John 8:36', also=['Hebrews 4:16','2 Corinthians 12:9','Psalm 121:1–2','Proverbs 27:1'],
 pearls=['thinking-healthy','help','trust','self-esteem-low','faith'], gc=[29,22,33],
 songs=[('battle','You do not have to win this by yourself before you are allowed to ask for help.'),('greater','God’s help is greater than the claim that you can handle it alone.'),('ourgod','Needing God is not the same as being out of control as a person.'),('victory','Freedom is something Christ gives. It is not a test you have to pass in private.')],
 origins='“I can stop whenever I want” often protects a person from having to look closely. If you are still in control, you do not have to tell anyone, see a doctor, or feel afraid. Sometimes the sentence is true for a while, and then it becomes the reason you do not ask for help after it stops being true. You are not a weak person if stopping is harder than you expected. Strength here looks like honesty, not like proving you can quit without anyone.',
 teaches='Jesus says that if the Son sets you free, you will be free indeed. That freedom is a gift, not a performance you stage to show you were never stuck. You can approach the throne of grace for help in time of need. Grace is sufficient in weakness. Your help comes from the Lord. Scripture does not mock a person who discovers they cannot stop as easily as they thought. It invites them to a freedom that does not depend on managing it alone.',
 replacement='I do not have to prove I can stop alone. If this is harder than I thought, I can tell the truth and ask for help.',
 truths=['Wanting to be in control is human.','Honesty is stronger than a promise I keep only in my head.','Needing a doctor or a counselor is not failure.','Jesus offers real freedom. I do not have to manufacture it.','I can ask for help before things get worse.','One honest conversation is a real step.'],
 self=['I can quit any time, so this is not a problem.','If I needed help, I would already have asked.','People who need help are the ones who have really lost it. I have not.','I will not tell anyone, because then it becomes real.','God helps people who have already stopped.','Admitting I need help means I am a failure.'],
 errors=[('Denial','Using “I can stop” to avoid looking at what stopping actually takes.'),('All-or-nothing thinking','Either you are fully in control or you are a failure.'),('Emotional reasoning','Feeling capable in a calm moment and calling that proof for every moment.'),('Fortune telling','Deciding you will quit later, so today does not count.')],
 questions=['When did I last stop as easily as this sentence says?','What am I protecting by saying I can control it?','Who would I trust with the truth if I did not have to impress them?','Would I want a friend to keep this secret if they were me?','What would asking for help look like this week, without quitting in a dangerous way on my own?','What does “free indeed” mean if freedom is a gift?'],
 prompt='When you said you could stop any time', moment='you used control to avoid asking for help',
 example='John 8:36 becomes: “<strong>James</strong> can write: “I do not have to prove I can stop alone. Jesus is the one who sets people free.””',
 reading='help', read_label='Help',
 actions=[('<strong>Tell one true sentence</strong> to a doctor, a counselor, or 1-800-662-4357: “Stopping is harder than I say.”','Tell one true sentence'),
          ('<strong>Do not test control by stopping suddenly</strong> if withdrawal could make you sick. Ask a doctor what is safe.','Ask a doctor before you stop'),
          ('<strong>Write the last time</strong> “I can stop whenever I want” was not what happened. No speech to yourself about being a failure.','Write the last time'),
          ('<strong>Pray John 8:36</strong> as a request, not as a claim that you have already handled it.','Pray for real freedom')],
 prayer='Lord, I have said I can stop whenever I want. If that is no longer true, give me honesty and a safe way to get help. Set me free. Do not let me do this alone. Amen.',
 tracker='A moment I told the truth about control')

add(num=72, file='I-Cant-Cope-Without-It', crisis=False,
 key='2 Corinthians 12:9', also=['Isaiah 41:10','Psalm 121:1–2','Matthew 11:28','Hebrews 4:16'],
 pearls=['anxiety-worry','help','peace','god-all-powerful','trust'], gc=[5,33,22],
 songs=[('held','You can be held while you learn another way to get through the day.'),('worn','Being worn down is a reason to ask for help, not a reason this is your only option.'),('power','God’s strength is for the hour you are actually in.'),('faithful','His faithfulness does not run out on a hard day.')],
 origins='Many people start using because a day was too heavy: pain, fear, grief, a mind that would not quiet, a life that asked for more than they had. The relief was real. The lie comes later, when the relief is renamed the only way to cope. “I can’t get through the day without it.” That sentence feels like a fact because the day is hard and the other tools are rusty. It is still a belief, not a life sentence. You are allowed to need help learning another way. You are also allowed to be honest that stopping may need a doctor, not a burst of willpower.',
 teaches='God’s grace is sufficient, and His power is made perfect in weakness. That is not a slogan that says “cope harder.” It says you do not have to be strong enough by yourself. “Do not fear, for I am with you. I will strengthen you and help you.” Help comes from the Lord. Jesus invites the weary to come and rest. You can approach Him for mercy in a time of need. None of these verses shame you for having used something to get through. They say it is not your only help.',
 replacement='I have used this to get through the day, and it is not my only help. God is with me, and I can learn another way with a doctor and a counselor.',
 truths=['The day is hard, and that is not the same as “nothing else will ever help.”','Relief I reached for does not have to be my only plan.','God’s strength shows up in weakness.','I can ask for help before I am out of other ideas.','A doctor can help me change this safely.','One other way to cope is worth learning, even if it feels small.'],
 self=['I cannot get through a normal day without it.','Other people cope. I am the one who cannot.','If I do not use, I will fall apart, so I have no choice.','God expects me to white-knuckle this.','Asking for another way means I am weak.','Nothing a counselor says will work on a real day.'],
 errors=[('All-or-nothing thinking','If this has been your way to cope, no other way can exist.'),('Fortune telling','Deciding a day without it will certainly destroy you.'),('Emotional reasoning','Feeling unable and calling the feeling a permanent fact.'),('Discounting the positive','Ignoring every hour you have gotten through another way.')],
 questions=['What did this help me survive, and what is it costing me now?','Have I ever gotten through a hard hour another way, even a small one?','Am I calling “I have not learned another way yet” the same thing as “no other way exists”?','Who could help me build one other option?','What would be unsafe about stopping on my own?','What does “I will help you” mean on a day I want to use?'],
 prompt='When the day felt impossible without it', moment='using felt like the only way to cope',
 example='2 Corinthians 12:9 becomes: “<strong>James</strong> can write: “God’s grace is enough for this day. This is not my only help.””',
 reading='help', read_label='Help',
 actions=[('<strong>Name one other help</strong> you could try in the next hard hour: a person, a walk, a prayer, a meeting, or a call to 1-800-662-4357.','Name one other help'),
          ('<strong>Talk with a doctor</strong> before you stop if withdrawal could make you sick. Do not turn this card into a plan to quit alone tonight.','Talk with a doctor'),
          ('<strong>Tell your counselor</strong> what the day feels like without it. Let them help you make the next hour smaller.','Tell your counselor'),
          ('<strong>Read Isaiah 41:10</strong> when the sentence “I can’t cope” starts.','Read the help verse')],
 prayer='Lord, I have believed I cannot get through the day without this. Your grace is sufficient in my weakness. Give me a doctor, a counselor, and one other way to cope. Amen.',
 tracker='An hour I got through another way')

add(num=73, file='Ive-Earned-the-Relief', crisis=False,
 key='Matthew 11:28', also=['Psalm 34:18','Hebrews 4:16','Isaiah 41:10','Lamentations 3:22–23'],
 pearls=['suffering','sorrow','joy','help','love-by-god'], gc=[27,12,22],
 songs=[('grace','Grace is real relief. It does not have to come in a bottle or a pill.'),('chains','Mercy can loosen what you reached for when you were hurting.'),('east','God’s kindness runs toward you. You do not have to earn a harmful kind of relief.'),('amazing','Amazing grace is for people who have been through hard things, not only for people who coped well.')],
 origins='If you have suffered, relief can feel like something you are owed. A hard childhood, a loss, a body in pain, a mind that will not rest: of course you want the pain to stop. Wanting relief is not selfish. The lie is narrower. It says this particular use is the relief you have earned, and that you should not question it because of what you have been through. You can honor the pain and still tell the truth that this kind of relief is hurting you. God is not stingy with comfort. He does not say you must keep hurting. He offers rest that does not master you.',
 teaches='Jesus says, “Come to Me, all you who are weary and burdened, and I will give you rest.” The invitation is for tired people, not for people who have already coped correctly. The Lord is near the brokenhearted. You can come for mercy and find grace to help. He will strengthen and help you. His mercies are new every morning. These verses do not scold you for wanting relief. They say the rest He gives is better than a relief that starts to own you.',
 replacement='I am allowed to want relief after what I have been through. Using is not the only comfort God has for me.',
 truths=['Wanting the pain to ease is human and good.','What I have suffered is real.','A harmful relief is not the only kindness available to me.','Jesus invites weary people to rest.','I can seek comfort and still be honest about the cost.','A doctor and a counselor can help me find relief that does not take over.'],
 self=['After what I have been through, I deserve this.','Anyone in my place would use.','If I stop, I am refusing myself the only kindness I get.','God does not understand how tired I am.','Comfort that comes with a cost is still mine to keep.','People who tell me to get help do not know what I have survived.'],
 errors=[('Emotional reasoning','Feeling you have earned it and treating the feeling as the whole truth.'),('All-or-nothing thinking','Either you get this relief or you get no comfort at all.'),('Discounting the positive','Ignoring every other comfort because this one is faster.'),('Justification','Using real pain as a reason not to look at real cost.')],
 questions=['What pain am I trying to quiet, and is it allowed to matter?','Has this relief stayed kind, or has it started to cost me?','What comfort have I decided does not count?','Would I want rest for a friend that begins to master them?','What would Jesus’ “I will give you rest” look like besides this?','Who can help me pursue comfort without shaming the pain?'],
 prompt='When you felt you had earned it', moment='you called using the relief you deserved',
 example='Matthew 11:28 becomes: “<strong>James</strong> can write: “I am weary, and Jesus offers rest. This is not my only comfort.””',
 reading='suffering', read_label='Suffering',
 actions=[('<strong>Name the pain and the cost</strong> on two lines. The pain is allowed to be real. The cost is allowed to be real too.','Name the pain and the cost'),
          ('<strong>Ask for one other comfort</strong> this week: a safe person, a meeting, prayer, or a call to 1-800-662-4357.','Ask for one other comfort'),
          ('<strong>Do not stop suddenly</strong> to prove you do not need the relief. Talk with a doctor about a safe plan.','Talk with a doctor'),
          ('<strong>Pray Matthew 11:28</strong> as a tired person, not as someone who must first deserve rest.','Pray as a tired person')],
 prayer='Lord, I have called this the relief I earned. I am weary. Give me the rest You promised, and a safe way to seek comfort that does not master me. Amen.',
 tracker='A comfort that was not using')

add(num=74, file='One-More-Time-Wont-Matter', crisis=False,
 key='Proverbs 27:1', also=['Hebrews 4:16','Psalm 121:1–2','Matthew 6:34','John 8:36'],
 pearls=['thinking-healthy','faith','help','peace','joy'], gc=[29,22,31],
 songs=[('even','You can take a true step today even if you do not feel ready for forever.'),('again','God’s mercy meets you again. Tomorrow is not the only day He helps.'),('thrive','A real life is allowed to start before you feel impressive.'),('lives','Because He lives, today is a day you can ask for help.')],
 origins='“One more time won’t matter. I’ll quit tomorrow” is a kind sentence people tell themselves so today does not have to change. Tomorrow stays clean because it never arrives. This is not proof that you are a liar or a hopeless case. It is a very common way to lower the fear of stopping. The mercy in it, if you can hear it, is that you already know you want a different day. The lie is that today is too small to matter and that a promise about tomorrow is the same thing as a plan. A plan includes a person who can help, and a doctor if stopping could make you sick.',
 teaches='Proverbs says not to boast about tomorrow, because you do not know what a day may bring. That is not a threat. It is a kindness that brings you back to the day you are actually in. You can approach God today for mercy and help. Your help comes from the Lord. Today has enough trouble of its own, which also means today is the day you are allowed to act, not only to promise. Jesus sets people free. None of this says “shame yourself for every delay.” It says a postponed promise is not the same as help received.',
 replacement='One more time does matter, and tomorrow is not a plan. I can take one honest step today, with help.',
 truths=['A promise about tomorrow is not the same as help today.','Today is small enough to be a real step.','I am not a failure because I have said “tomorrow” before.','I can tell someone the promise instead of keeping it in my head.','A doctor can help me make stopping safe.','God’s help is for this day, not only for a future version of me.'],
 self=['This time does not count.','I will be different tomorrow.','I have said it before, so saying it again is pointless.','Today is already ruined, so I might as well.','If I ask for help today, I have admitted I cannot quit on my own schedule.','God is keeping score of every delay.'],
 errors=[('Minimization','Calling another time “nothing” so you do not have to feel it.'),('Fortune telling','Treating a tomorrow you cannot see as a reliable plan.'),('All-or-nothing thinking','If today is not a perfect quit, today is worthless.'),('Emotional reasoning','Feeling done with the day and deciding the day is allowed to be given up.')],
 questions=['How many tomorrows have I already spent?','What would a plan include that a promise does not?','What is one step that is smaller than quitting forever?','Who needs to know, so this is not only a private bargain?','What would be unsafe about deciding to stop tonight with no medical help?','What help is available today, not next month?'],
 prompt='When you moved it to tomorrow', moment='one more time felt like it would not matter',
 example='Proverbs 27:1 becomes: “<strong>James</strong> can write: “I do not know tomorrow. I can ask for help today.””',
 reading='thinking-healthy', read_label='Thinking, Healthy',
 actions=[('<strong>Trade the promise for a call.</strong> Instead of “tomorrow,” call 1-800-662-4357 or tell your counselor what you were about to delay.','Trade the promise for a call'),
          ('<strong>Do not make “tonight I stop cold” the step</strong> if withdrawal could make you sick. Ask a doctor what a safe step is.','Ask what a safe step is'),
          ('<strong>Write today’s step on paper</strong> before the day is over: one person to tell, or one appointment to request.','Write today’s step'),
          ('<strong>Pray Proverbs 27:1</strong> as a return to today, not as a speech against yourself.','Pray about today')],
 prayer='Lord, I keep moving this to tomorrow. Bring me back to today. Give me one honest step and a safe person to take it with. Amen.',
 tracker='A step I did not postpone')

add(num=75, file='Nothing-Else-Will-Work', crisis=True,
 key='Psalm 42:11', also=['Lamentations 3:22–23','Psalm 34:18','Hebrews 4:16','Isaiah 41:10'],
 pearls=['hopeless','depression-symptoms-of','help','joy','love-by-god'], gc=[12,22,29],
 songs=[('hope','Living hope is for the day when you cannot imagine another way to feel okay.'),('forever','God’s love outlasts the feeling that nothing else will work.'),('heaven','There is more ahead than the relief you can arrange tonight.'),('assurance','You belong to Christ even when you feel unable to feel okay any other way.')],
 origins='When something is the only thing that has made you feel okay, the mind draws a hard line: nothing else will work. Depression, panic, grief, and withdrawal can all make that line feel like a wall. It is a painful belief, and it is also a hopeless one. You are not foolish for having found one thing that numbed the pain. You are also not stuck with the conclusion that God, people, medicine, and time have nothing left for you. If this belief comes with thoughts of dying, that is an emergency, not a private philosophy. Please tell someone today.',
 teaches='The psalm talks to a downcast soul and says, “Put your hope in God, for I will yet praise Him.” “Yet” means the praise is not required before the hope. Mercies are new every morning, even after a night that felt final. The Lord is near the brokenhearted. You can approach Him for grace to help in time of need. He will strengthen and help you. These verses do not say you must feel okay in order to be helped. They say the feeling “nothing else will work” is not the last word.',
 replacement='This is not the only thing that can help me. God is near, other help exists, and I can ask even when I cannot feel that yet.',
 truths=['Feeling like nothing else will work is not proof that nothing will.','I am allowed to want to feel okay.','God is near me in this, not waiting for me to fix it first.','A doctor, a counselor, and other people can help.','I do not have to feel hopeful before I ask.','If I want to die, I can call 988 today.'],
 self=['This is the only thing that works.','I have tried, and nothing else touches it.','If I cannot feel hope, there is no hope.','God has already decided not to help me.','People who talk about other options do not know my pain.','I might as well give up.'],
 errors=[('Fortune telling','Deciding every future help will fail because this one worked fastest.'),('Emotional reasoning','Feeling hopeless and calling the feeling a fact about God and about medicine.'),('All-or-nothing thinking','If this is what works, nothing else is allowed to count.'),('Discounting the positive','Erasing every hour of relief that did not come from using.')],
 questions=['What have I actually tried, and what have I only imagined would fail?','Is “I cannot feel another way” the same as “no other way exists”?','Who is one person or helper I have not given a real chance?','What would I tell a friend who said nothing else will ever work?','Where is God in the sentence “nothing else”?','If I am thinking about dying, who will I tell today?'],
 prompt='When nothing else seemed able to help', moment='you felt this was the only way to feel okay',
 example='Psalm 42:11 becomes: “<strong>James</strong> can write: “My soul is downcast, and I will yet hope in God. This is not my only help.””',
 reading='hopeless', read_label='Hopeless',
 actions=[('<strong>If you want to die, call or text 988</strong> or tell someone near you now. Do that before any other step.','Call or text 988 if you want to die'),
          ('<strong>Tell one helper the sentence</strong> “nothing else will work,” and let them answer. A counselor, a doctor, or 1-800-662-4357.','Tell one helper the sentence'),
          ('<strong>Do not stop suddenly</strong> to force another way to work. Ask a doctor what is safe.','Ask a doctor what is safe'),
          ('<strong>Read Psalm 42:11</strong> out loud, including the word “yet.”','Read the “yet” verse')],
 prayer='Lord, my soul is downcast, and I have believed nothing else will work. You are my Savior and my God. Give me help I cannot feel yet, and keep me alive to receive it. Amen.',
 tracker='A help I did not dismiss')

add(num=76, file='A-Little-Doesnt-Count', crisis=False,
 key='1 Corinthians 6:12', also=['Proverbs 27:1','Hebrews 4:16','John 8:36','Psalm 121:1–2'],
 pearls=['thinking-healthy','self-esteem-low','help','faith','guilt-shame'], gc=[29,31,22],
 songs=[('voice','The voice that says a little does not count is worth testing.'),('truth','You can tell the truth about the little without turning it into a speech of shame.'),('conquer','You do not have to be mastered by something you keep calling small.'),('eyes','Look at Christ, who offers freedom, when you are bargaining about amount.')],
 origins='“A little doesn’t count” is how a lot of people stay out of the conversation. If it is small, it is not a problem, and you are still in control. Sometimes the amount really is small. The lie is the rule that small means harmless, and that you can keep it small forever by deciding to. You do not need a dramatic story to be allowed to get help. You also do not need to call yourself a terrible person because the amount was not huge. Honesty about the little is an act of care, not a confession that you are worthless.',
 teaches='Paul says that not everything is beneficial, and “I will not be mastered by anything.” He is not sorting people into the ruined and the fine. He is telling the truth that a permitted thing can still take the lead. You do not know what tomorrow brings, so “I will keep it small” is a hope, not a guarantee. You can ask God for help before a little becomes the master. Jesus sets people free. Your help comes from the Lord. None of this requires you to exaggerate the problem or to hide it.',
 replacement='A little can still matter. I can be honest about it, and I can get help before I have to prove I lost control.',
 truths=['Small is not the same as harmless.','I do not have to wait for a crisis to tell the truth.','I am not worthless if a little has started to matter.','I can ask whether this is mastering me.','A doctor or a counselor can help me look at this without shaming me.','Keeping it small is not a plan I have to manage alone.'],
 self=['It is only a little. People are overreacting.','I can keep it at this level forever.','If I am not using as much as someone else, I do not need help.','Admitting the little makes me a hypocrite.','I am still in charge because I chose the amount.','God does not care about something this small.'],
 errors=[('Minimization','Shrinking the pattern so you do not have to look at it.'),('Comparison','Using someone else’s larger use as proof that yours does not count.'),('All-or-nothing thinking','If it is not the worst case, it is nothing.'),('Control fallacy','Believing that choosing the amount means the amount cannot start choosing you.')],
 questions=['What do I mean by a little, and has that meaning already changed?','What am I unwilling to give up, even in a small amount?','Would I want a friend to get help at this stage, or only after a crisis?','Am I more interested in keeping it small or in telling the truth?','What would help look like before things grow?','What does “not mastered by anything” invite, without a speech of shame?'],
 prompt='When you said a little did not count', moment='you kept the amount small in order to stay in control',
 example='1 Corinthians 6:12 becomes: “<strong>James</strong> can write: “A little can still master me. I can tell the truth and ask for help.””',
 reading='thinking-healthy', read_label='Thinking, Healthy',
 actions=[('<strong>Write the actual amount</strong> for the last seven days, plainly. No comparing it with someone worse, and no name-calling.','Write the actual amount'),
          ('<strong>Show that note</strong> to a doctor, a counselor, or tell it to 1-800-662-4357.','Show the note to a helper'),
          ('<strong>Do not “prove it is small” by stopping suddenly</strong> if withdrawal could make you sick. Ask what is safe.','Ask what is safe'),
          ('<strong>Pray 1 Corinthians 6:12</strong> as a request not to be mastered, not as a verdict.','Pray not to be mastered')],
 prayer='Lord, I have said a little does not count. Give me honesty without shame, and help before this masters me. Amen.',
 tracker='A time I did not minimize the amount')

add(num=77, file='Other-People-Are-the-Reason', crisis=False,
 key='Psalm 121:1–2', also=['Psalm 34:18','Matthew 11:28','Hebrews 4:16','Isaiah 41:10'],
 pearls=['guilt-shame','thinking-healthy','help','forgiveness','suffering'], gc=[27,29,17],
 songs=[('jesus','Jesus stays with you in the hurt other people caused. He also stays for the next step.'),('want','You can want a different way even if the people who hurt you do not change.'),('alone','You are not alone with their treatment or with the choice in front of you.'),('friend','You can tell God what they did and still ask for help with what you do next.')],
 origins='Other people really can be part of the story. Stress, cruelty, loneliness, a house that was never safe, a loss someone else caused: those things hurt, and using may have been how you got through them. The lie goes one step further. It says you have no next step until they treat you better, and that the using is simply their fault. Their harm can be real and still not be the only thing that gets to decide your tomorrow. You can grieve what they did and still reach for help. You do not have to pretend you caused their treatment in order to get care for yourself.',
 teaches='Help comes from the Lord, the Maker of heaven and earth. That help is not postponed until the people who hurt you apologize. He is near the brokenhearted, which includes hearts broken by other people. Jesus invites the weary. You can approach Him for grace to help in time of need. He will strengthen you. These verses do not deny that people wounded you. They say your help does not have to wait on their change.',
 replacement='People have hurt me, and that is real. Their treatment does not remove my next step. I can get help even if they do not change.',
 truths=['What other people did can be truly wrong.','I do not have to excuse them in order to get help.','I also do not have to wait for them before I ask for help.','God’s help is not on their timetable.','A counselor can help me hold both truths.','I am not a worse person because pain had a reason.'],
 self=['If they were kinder, I would not use.','This is on them, so I do not have to look at it.','Nothing will change until they change.','Getting help means I am letting them off the hook.','I am only doing what they drove me to.','God should fix them first.'],
 errors=[('Blame shifting','Making another person’s wrong the reason you cannot take any step.'),('All-or-nothing thinking','Either they change or you have no choices at all.'),('Emotional reasoning','Feeling powerless around them and deciding you are powerless everywhere.'),('Fortune telling','Deciding you will use for as long as they stay the same.')],
 questions=['What did they actually do, and what have I added by saying I have no choice?','Can their wrong be real and my next step still be mine?','What help is available even if they never apologize?','Who is a safe person who is not the person I am blaming?','What would I want for a friend in this exact spot?','Where does my help come from if it does not come from their reform?'],
 prompt='When you gave them the whole reason', moment='someone else’s treatment felt like the reason you had to use',
 example='Psalm 121:2 becomes: “<strong>James</strong> can write: “My help comes from the Lord. I do not have to wait for them to change.””',
 reading='suffering', read_label='Suffering',
 actions=[('<strong>Write two lines.</strong> “What they did” and “the step I can take anyway.” Do not use the second line to excuse the first.','Write two lines'),
          ('<strong>Tell a helper who is not the person you blame.</strong> A counselor, a doctor, or 1-800-662-4357.','Tell a helper who is not them'),
          ('<strong>Ask a doctor</strong> before you change how you stop. Do not make a sudden stop your way of proving them wrong.','Ask a doctor first'),
          ('<strong>Pray Psalm 121:1–2</strong> when you want to wait for them to become kinder.','Pray for help that does not wait on them')],
 prayer='Lord, people have hurt me, and I have used that as the whole reason. Be near the brokenhearted. Give me help that does not wait on their change. Amen.',
 tracker='A step I took without waiting for them')

add(num=78, file='I-Dont-Hurt-Anybody-Else', crisis=False,
 key='Romans 14:7', also=['Hebrews 4:16','Psalm 139:14','John 8:36','Matthew 11:28'],
 pearls=['love-by-god','friendship','help','self-esteem-low','thinking-healthy'], gc=[17,24,29],
 songs=[('body','You are part of a body of people. Your life is connected, and you are still loved.'),('love','Love can tell the truth and still stay.'),('who','Who you are to God is not “someone whose life does not matter as long as others seem fine.”'),('lovesme','Jesus loves you. That is a reason to get help, not a reason to hide.')],
 origins='“I don’t hurt anybody else, so this is my choice and it is fine” can come from a real desire not to be a burden, or from a wish to keep this private. Sometimes it is also a way to end the conversation. You do not need a list of people you have harmed in order to be worth helping. Your own life matters. And lives are connected: the people who love you are affected even when you are careful, even when you cannot see it, even when you are trying not to hurt them. This is not a speech to make you feel like a destroyer. It is an invitation to let your life count, including to you.',
 teaches='None of us lives to himself alone, and none of us dies to himself alone. That is a word about connection, not a verdict that you have ruined everyone. You can approach God with confidence for mercy. You are fearfully and wonderfully made, which means your life is not a private thing you are allowed to throw away because you think no one else is involved. Jesus sets people free. He invites the weary to rest. Scripture cares about you, not only about the question of whether someone else has caught you.',
 replacement='My life matters, to God and to people who love me. I can get help because I am worth caring for.',
 truths=['I do not have to prove I have hurt someone before I deserve help.','My life is connected to other lives.','I matter even on the days I think I am only affecting myself.','Jesus loves me. That is a reason to reach for help.','I can be honest without calling myself a monster.','A counselor can help me see the people I have been protecting from the truth.'],
 self=['It is my body and my business.','Nobody else is affected.','If they do not know, it does not count.','I am not hurting them, so I should be left alone.','Getting help would worry people, so hiding is kinder.','I do not matter enough for this to be a problem.'],
 errors=[('Minimization','Deciding hidden use has no effect.'),('All-or-nothing thinking','If you are not the worst story you have heard, no one is touched.'),('Mind reading','Assuming the people who love you are fine because they have not said otherwise.'),('Discounting the positive','Treating your own life as too small to be worth help.')],
 questions=['Who loves me, and have I actually asked whether they are unaffected?','Do I hide this because it hurts no one, or because I do not want them to worry?','If a friend said their life did not matter as long as others seemed fine, what would I say?','What would change if I believed I was worth a doctor’s help?','Who is one person I could stop hiding from?','What does “none of us lives to himself alone” invite, without a list of damages?'],
 prompt='When you said it hurt no one', moment='you treated this as a private choice with no cost',
 example='Romans 14:7 becomes: “<strong>James</strong> can write: “I do not live to myself alone. My life matters, and I can ask for help.””',
 reading='love-by-god', read_label='Love, By God',
 actions=[('<strong>Tell one person who loves you</strong> a single true sentence, or tell a counselor first if that person is not safe.','Tell one true sentence'),
          ('<strong>Call 1-800-662-4357</strong> if you do not yet have a person to tell. You do not have to have a crisis story.','Call the helpline'),
          ('<strong>Ask a doctor</strong> for a safe plan before you stop. Your body matters too.','Ask a doctor'),
          ('<strong>Read Romans 14:7</strong> as a word about connection, not as an accusation.','Read the connection verse')],
 prayer='Lord, I have said this hurts no one and so it is fine. Teach me that my life matters, and that the people who love me matter, and give me a safe way to get help. Amen.',
 tracker='A moment I let my life matter')

add(num=79, file='No-Point-in-Stopping-Now', crisis=True,
 key='Lamentations 3:22–23', also=['Romans 8:1','Isaiah 43:18–19','Psalm 42:11','Hebrews 4:16'],
 pearls=['hopeless','forgiveness','guilt-shame','faith','help'], gc=[12,14,22],
 songs=[('allnew','God makes things new. A damaged chapter is not the end of the story.'),('broken','God works with broken things. You do not have to be undamaged before you stop.'),('wins','Grace wins over the sentence that it is too late.'),('glory','To God be the glory for mercy, including mercy that starts today.')],
 origins='“I’ve already messed things up, so there is no point in stopping now” is hopelessness wearing the clothes of realism. The past may be genuinely damaged: trust, health, money, time, relationships. None of that is brushed aside here. The lie is the conclusion that more harm is the logical next step, and that mercy is no longer on offer. Stopping still matters on the worst day. It matters because you are still alive, and because God’s mercies are new in the morning, not only in the years before things went wrong. If this belief includes wanting to die, please reach for help now. You do not have to decide the rest of your life today.',
 teaches='Because of the Lord’s loving devotion we are not consumed, for His mercies never fail. They are new every morning. There is no condemnation in Christ Jesus. God says not to be locked on the former things, because He is doing something new, a way in the wilderness. Put your hope in God. Approach the throne of grace for mercy and help. These verses were written for people with real wreckage behind them. They do not say the past was small. They say it is not a reason to keep going down.',
 replacement='What I have done is not the end of the story. God’s mercy is new today, and stopping still matters.',
 truths=['The past can be really damaged and still not be the last word.','There is a point in stopping today.','I am not condemned and finished.','God’s mercy is new this morning.','I can ask for help without first repairing everything.','If I want to die, I can call 988 and stay.'],
 self=['It is too late.','I have already ruined it, so more does not matter.','Mercy is for people who stopped sooner.','God is done with me.','There is no point in a doctor now.','I might as well disappear.'],
 errors=[('Fortune telling','Deciding the rest of your life is already ruined.'),('All-or-nothing thinking','If you cannot undo the past, the future is pointless.'),('Emotional reasoning','Feeling finished and calling that God’s verdict.'),('Discounting the positive','Refusing any help because it cannot rewrite every consequence.')],
 questions=['What is actually lost, and what am I adding by saying nothing left matters?','Would I tell a friend it was pointless for them to stop today?','What is one thing stopping would still protect?','Where do I see “new every morning” arguing with “no point”?','Who can help me with the next day, not the whole repair?','If I am thinking about dying, who will I contact before today ends?'],
 prompt='When you decided it was too late', moment='you felt there was no point in stopping',
 example='Lamentations 3:22–23 becomes: “<strong>James</strong> can write: “His mercies are new this morning. There is still a point in stopping.””',
 reading='hopeless', read_label='Hopeless',
 actions=[('<strong>If you want to die, call or text 988</strong> or tell someone near you today.','Call or text 988 if you want to die'),
          ('<strong>Make one appointment</strong> or one call to 1-800-662-4357. The point of the call is today, not a repaired past.','Make one call'),
          ('<strong>Ask a doctor</strong> before you stop if withdrawal could make you sick. A safe plan is still worth making.','Ask a doctor'),
          ('<strong>Read Lamentations 3:22–23</strong> in the morning before you review everything you have ruined.','Read the new-mercy verse')],
 prayer='Lord, I have decided it is too late and there is no point. Your mercies are new this morning. There is no condemnation in Christ. Help me stop, and help me stay alive. Amen.',
 tracker='A reason today still mattered')

add(num=80, file='I-Cant-Be-Myself-Unless-I-Use', crisis=False,
 key='Hebrews 4:16', also=['Psalm 139:14','2 Corinthians 12:9','John 8:36','Psalm 34:18'],
 pearls=['self-esteem-low','friendship','fear','love-by-god','help'], gc=[24,17,5],
 songs=[('yousay','What God says about you is enough for you to be in the room.'),('clean','You do not have to arrive altered in order to be received.'),('speak','God’s Word can give you a self to stand in, a little at a time.'),('tender','Christ is gentle with the person who is afraid to be seen without a buffer.')],
 origins='Some people use because being with others feels impossible without a buffer. The room is too bright, the words will not come, or the real self feels like too much or not enough. “I can’t be myself unless I use first.” That can be social fear, old shame, or a habit that now feels like personality. You are not faking a self when you are sober. You are meeting people without a screen. It can be awkward and still be you. God already knows you without it. Safe people can learn to know you too, in small doses, with help.',
 teaches='You can approach the throne of grace with confidence, so that you may receive mercy and find grace to help. You do not have to chemically prepare yourself to come to God, and you do not have to be impressive to come to people. You are fearfully and wonderfully made. Grace is sufficient in weakness, including the weakness of feeling unlike yourself in a room. Jesus sets people free. He is near the brokenhearted. These verses do not demand that you become outgoing. They say the self God made does not require using in order to be real.',
 replacement='I can be myself without using first. God already knows me, and I can practice being with safe people a little at a time.',
 truths=['Needing a buffer is understandable. It is not my identity.','The person I am without it is still me.','God receives me without my having to prepare a different self.','I can start with one safe person and a short time.','Awkward is not the same as fake.','A counselor can help me practice this without shaming the fear.'],
 self=['Nobody wants the sober version of me.','I am boring, or too much, unless I use.','I cannot talk to people without it.','If I do not use first, they will see the real me and leave.','This is just my personality.','God is disappointed by the self I am in a quiet room.'],
 errors=[('Labeling','Calling the buffered self the real you and the other self a failure.'),('Mind reading','Deciding people will reject you before they have met you without it.'),('Fortune telling','Deciding every social hour without using will be unbearable.'),('Emotional reasoning','Feeling unlike yourself and concluding you are not yourself.')],
 questions=['Who told me, or what taught me, that I am not acceptable as I am?','What is one person and one short visit I could try without using first?','Is the fear of being seen the same as being unlovable?','What does God already know about me that I am trying to hide?','What would “a little at a time” look like, with a counselor’s help?','If withdrawal or a sudden stop would make me sick, what should I ask a doctor before I experiment?'],
 prompt='When you used in order to be yourself', moment='you felt you could not be with people unless you used first',
 example='Hebrews 4:16 becomes: “<strong>James</strong> can write: “I can come as I am and find grace to help. I do not have to use first to be real.””',
 reading='self-esteem-low', read_label='Self-Esteem, Low',
 actions=[('<strong>Plan one short time</strong> with a safe person without using first. Tell your counselor the plan. Keep it small.','Plan one short time'),
          ('<strong>If that is not medically safe yet,</strong> do not force it. Ask a doctor how to approach days without using.','Ask a doctor first'),
          ('<strong>Call 1-800-662-4357</strong> if you need help finding that doctor or a counselor.','Call the helpline'),
          ('<strong>Pray Hebrews 4:16</strong> before the next room you are afraid to enter as yourself.','Pray before you walk in')],
 prayer='Lord, I have believed I cannot be myself unless I use first. You already know me. Give me grace to be seen, a safe person, and a doctor’s help so I do not do this in a dangerous way. Amen.',
 tracker='A moment I showed up without using first')

def main():
    src = (ROOT/'belief-cards/psychological/Psych-041-Something-Terrible-Is-About-to-Happen.html').read_text()
    head, rest = src.split('<!-- ============ CARD ============ -->', 1)
    script = rest[rest.rfind('\n</div><script>')+1:]
    lst = json.loads((ROOT/'tools/lists/psychological.json').read_text())
    group = next(g for g in lst['sections'][0]['groups'] if g['name']=='Substance Abuse')
    beliefs = [b[0] for b in group['beliefs']]
    if len(beliefs) != len(C):
        raise SystemExit(f'count {len(beliefs)} vs {len(C)}')
    used=set()
    for p in (ROOT/'tools').glob('psych-*/*.json'):
        d=json.loads(p.read_text())
        songs=d.get('songs')
        if isinstance(songs, list) and songs and isinstance(songs[0], str):
            used.add(tuple(songs))
    outdir=ROOT/'tools/psych-substance'; outdir.mkdir(exist_ok=True)
    for d, belief in zip(C, beliefs):
        d['belief']=belief
        songset=tuple(k for k,_ in d['songs'])
        if songset in used: raise SystemExit('dup '+str(songset))
        used.add(songset)
        kinds=[]; blocks=[]
        for key, why in d['songs']:
            kind, html = A.song(key, why); kinds.append(kind); blocks.append(html)
        if kinds.count('classic')!=1 or len(kinds)!=4: raise SystemExit(f'mix {d["num"]} {kinds}')
        for slug in list(d['pearls'])+[d['reading']]:
            if slug not in A.PEARLS: raise SystemExit('pearl '+slug)
        if '988' in d['origins'] or '662' in d['origins']: raise SystemExit('prebaked '+str(d['num']))
        d['origins'] = d['origins'] + HELP + (CRISIS if d['crisis'] else '')
        A.STEP = STEP_TOP if d['crisis'] else STEP_MILD
        shown='“'+belief+'”'
        errs='\n'.join(f'<li><strong>{a}: </strong>{b}</li>' for a,b in d['errors'])
        refs=[d['key']]+d['also'][:2]
        scr='<ul class="opts">\n'+'\n'.join(f'<li><span class="ref">{ref}</span><span class="scrip">“{A.V[ref]}”</span></li>' for ref in refs)+'\n</ul>'
        truths=[d['replacement']]+[t for t in d['truths'] if t!=d['replacement']]
        truths=truths[:6]
        acts='<ul class="opts">\n'+'\n'.join(f'<li>{a}</li>' for a,_ in d['actions'])+'\n</ul>'
        page=A.render_page(d, head, script, blocks, shown, belief, errs, scr, truths, acts)
        page=page.replace('· Anxiety</div>', '· Substance Abuse</div>', 1)
        fname=f"Psych-{d['num']:03d}-{d['file']}"
        page=page.replace('Psych-041-Something-Terrible-Is-About-to-Happen-Homework.pdf', fname+'-Homework.pdf')
        page=page.replace('Psych-041-Something-Terrible-Is-About-to-Happen.pdf', fname+'.pdf')
        page=page.replace('Belief Card: Something terrible is about to happen', 'Belief Card: '+belief.rstrip('.'))
        page=page.replace('“Something terrible is about to happen.”', shown)
        if page.find('<h2>Listen: Overcoming Anxiety</h2>') > page.find('<h2>Listen: Overcoming Depression</h2>'):
            raise SystemExit('audio '+fname)
        if '1-800-662-4357' not in page or 'doctor' not in page.lower():
            raise SystemExit('helpline missing '+fname)
        if d['crisis'] and page.find('988') > page.find('Where it often comes from') + 2500:
            raise SystemExit('988 not near top '+fname)
        (ROOT/'belief-cards/psychological'/f'{fname}.html').write_text(page)
        (outdir/f"{d['num']:03d}.json").write_text(json.dumps({
            'num': d['num'], 'file': d['file'], 'group': 'Substance Abuse',
            'belief': '“'+belief+'”', 'belief_plain': belief.rstrip('.'),
            'origins': d['origins'], 'self': d['self'],
            'songs': [k for k,_ in d['songs']], 'key': d['key'],
            'replacement': d['replacement'], 'crisis': d['crisis'],
        }, ensure_ascii=False, indent=1)+'\n')
        group['beliefs'][d['num']-71][:] = [belief, fname+'.html']
        print(d['num'], 'crisis', d['crisis'])
    (ROOT/'tools/lists/psychological.json').write_text(json.dumps(lst, ensure_ascii=False, indent=1)+'\n')
    print('wired', sum(1 for b in group['beliefs'] if len(b)>1))

if __name__=='__main__':
    main()
