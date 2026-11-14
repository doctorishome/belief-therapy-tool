"""Build Abuse cards 61–70 on the anxiety/PTSD card template.
Survivor wording only. Safety numbers are on every card.
Run: python3 tools/make_abuse_cards.py
"""
import importlib.util, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('anx', ROOT/'tools/make_anxiety_cards.py')
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
A.V.update({
 'Psalm 34:18': 'The LORD is near to the brokenhearted; He saves the contrite in spirit.',
 'Psalm 103:13–14': 'As a father has compassion on his children, so the LORD has compassion on those who fear Him. For He knows our frame; He is mindful that we are dust.',
 'Psalm 118:6': 'The LORD is on my side; I will not be afraid. What can man do to me?',
 'Psalm 139:14': 'I praise You, for I am fearfully and wonderfully made. Marvelous are Your works, and I know this very well.',
 'Psalm 147:3': 'He heals the brokenhearted and binds up their wounds.',
 'Romans 8:1': 'Therefore, there is now no condemnation for those who are in Christ Jesus.',
 'Romans 8:38–39': 'For I am convinced that neither death nor life, neither angels nor principalities, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.',
 'Romans 12:15': 'Rejoice with those who rejoice; weep with those who weep.',
 'Galatians 6:2': 'Carry one another’s burdens, and in this way you will fulfill the law of Christ.',
 '2 Corinthians 1:3–4': 'Blessed be the God and Father of our Lord Jesus Christ, the Father of compassion and the God of all comfort, who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves have received from God.',
 'Isaiah 61:1': 'The Spirit of the Lord GOD is on Me, because the LORD has anointed Me to preach good news to the poor. He has sent Me to bind up the brokenhearted, to proclaim liberty to the captives and freedom to the prisoners.',
 '1 Peter 5:7': 'Cast all your anxiety on Him, because He cares for you.',
 'Isaiah 43:2': 'When you pass through the waters, I will be with you; and when you go through the rivers, they will not overwhelm you. When you walk through the fire, you will not be scorched; the flames will not set you ablaze.',
})
SAFE = ' If you are not safe right now, call 911. You can also call the National Domestic Violence Hotline at 1-800-799-7233. If a child is being hurt, call Childhelp at 1-800-422-4453. A counselor can help you at a pace that is safe. You do not have to do this alone, or all at once.'
CRISIS = ' If you are thinking about ending your life, call or text 988 in the United States, or tell someone near you right away.'
STEP_TOP = 'Choose steps you can do safely. If you are thinking about ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone.'
STEP_MILD = 'Choose steps you can do safely. If this belief comes with hopelessness or thoughts of ending your life, call or text 988 (the Suicide &amp; Crisis Lifeline), or call 911 in an emergency. You do not have to carry this alone. If you are not safe right now, call 911 or 1-800-799-7233.'
C = []
def add(**k):
    C.append(k)

add(num=61, file='What-Was-Done-to-Me-Was-My-Fault', crisis=False,
 key='Romans 8:1', also=['Psalm 103:13–14','Psalm 34:18','Isaiah 61:1','John 14:27'],
 pearls=['guilt-shame','thinking-healthy','self-esteem-low','love-by-god','forgiveness'], gc=[29,27,24],
 songs=[('younger','God meets the younger you with kindness, not with the blame you have been carrying.'),('clean','Shame after harm is not the same thing as being the cause of it.'),('cross','Christ carries guilt that is truly yours. He does not ask you to carry someone else’s.'),('glory','God’s glory is mercy, not a trial of the person who was hurt.')],
 origins='People who were harmed often hunt for a reason they could have controlled. “If it was my fault, I can keep it from happening again.” That search feels like safety. It is a lie that adds shame to harm. What was done to you was someone else’s choice or someone else’s failure to protect you. You did not cause it by existing, by trusting, or by being unable to stop it. You do not have to describe it in order to lay this sentence down.',
 teaches='There is no condemnation in Christ for the person who was hurt and then blamed themselves. The Lord has compassion and knows our frame. He is near the brokenhearted. He binds up the brokenhearted and proclaims liberty. Jesus says not to let your heart be troubled. None of these verses say that suffering proves you caused it. Wanting to have stopped it is grief. It is not a verdict.',
 replacement='What was done to me was not my fault. I did not cause it, and I do not have to carry blame that belongs to someone else.',
 truths=['I did not cause what was done to me.','Wanting to have stopped it is not the same as causing it.','I am not on trial for someone else’s choice.','God is near me. He is not accusing me.','I can grieve without agreeing with the blame.','A counselor can help me sort this without making me tell everything.'],
 self=['I must have done something to make it happen.','If I had been different, it would not have happened.','A better person would have prevented it.','I do not deserve comfort because I let it happen.','God agrees that it was my fault.','If I stop blaming myself, I will not be safe.'],
 errors=[('Personalization','Taking the blame for what another person did.'),('Hindsight bias','Judging your past self with facts you did not have then.'),('Emotional reasoning','Feeling guilty and deciding the feeling is proof.'),('All-or-nothing thinking','If you did not stop it perfectly, it was entirely your fault.')],
 questions=['What do I believe I should have done, and could I really have done it then?','Whose choice was it, if I set my self-blame aside?','Would I say this was a friend’s fault if it had happened to them?','Am I using blame to feel less helpless?','What does “no condemnation” mean for a person who was hurt?','What would my counselor want me to stop saying to myself?'],
 prompt='When you blamed yourself', moment='you took the fault for what was done to you',
 example='Romans 8:1 becomes: “<strong>Sarah</strong> can write: “What was done to me was not my fault. In Christ I am not condemned.””',
 reading='guilt-shame', read_label='Guilt/Shame',
 actions=[('<strong>Write the charge, then a fair sentence.</strong> One line of self-blame. Then one line you would say to a friend. No graphic detail.','Write the charge, then a fair sentence'),
          ('<strong>Ask your counselor</strong> to help you separate grief from blame. Stop if it becomes too much.','Ask your counselor'),
          ('<strong>Refuse one “I caused it.”</strong> When the sentence starts, say, “That was not mine to cause,” and stop.','Refuse one “I caused it”'),
          ('<strong>Read Romans 8:1</strong> each morning before you review the past.','Read the no-condemnation verse')],
 prayer='Lord, I have blamed myself for harm I did not choose. There is no condemnation in Christ. Teach me the difference between grief and guilt, and give me a safe counselor as I lay this down. Amen.',
 tracker='A moment I did not take the blame')

add(num=62, file='Im-Damaged-and-Ashamed', crisis=True,
 key='Psalm 147:3', also=['Isaiah 61:1','Psalm 34:18','Romans 8:38–39','2 Corinthians 12:9'],
 pearls=['self-esteem-low','guilt-shame','love-by-god','hopeless','sorrow'], gc=[24,27,12],
 songs=[('broken','God does not throw away a wounded person.'),('yousay','What God says about you is not “worthless.”'),('allnew','What was done to you is not God’s last word about you.'),('lovesme','Jesus loves you. Harm does not cancel that.')],
 origins='Harm can leave shame that feels like a stain: damaged, ashamed, worthless. That feeling is common, and it is a lie about your worth. What was done to you does not make you less of a person. Shame often shows up because someone treated you as if you did not matter. God’s nearness to the brokenhearted is the opposite of that treatment. You do not have to recount what happened to question this sentence.',
 teaches='God heals the brokenhearted and binds up their wounds. He does not rename them worthless. He is near the brokenhearted. Nothing can separate you from the love of God in Christ. Grace is sufficient in weakness. These verses do not rush you to feel clean. They refuse the conclusion that harm made you damaged goods.',
 replacement='I was hurt, and I am not worthless. What was done to me does not decide what I am worth.',
 truths=['Shame is a feeling, not a measurement of my worth.','I am not damaged goods.','God is near me, not disgusted with me.','Nothing can separate me from the love of God.','I can heal slowly without first proving I am clean.','A counselor can help me carry the shame without making me describe everything.'],
 self=['I am ruined and dirty.','If people knew, they would be disgusted.','I will never be worth kindness.','The shame is proof that I am the problem.','I should hide so I do not contaminate anyone.','God cannot look at me.'],
 errors=[('Labeling','Calling your whole self damaged because you were harmed.'),('Emotional reasoning','Feeling ashamed and deciding the shame is the truth about you.'),('Mind reading','Assuming everyone would reject you if they knew.'),('Fortune telling','Deciding you will always be worthless.')],
 questions=['What was done to me, and what have I decided that makes me?','Would I call a friend worthless because someone harmed them?','Is shame a fact, or a weight someone else put on me?','What is still true and good about me?','What does God do with the brokenhearted?','Who is safe enough to tell that I feel ashamed, without telling the story?'],
 prompt='When shame said you were worthless', moment='you felt damaged beyond help',
 example='Psalm 147:3 becomes: “<strong>Sarah</strong> can write: “God binds up the brokenhearted. I am hurt, and I am not worthless.””',
 reading='self-esteem-low', read_label='Self-Esteem, Low',
 actions=[('<strong>Separate the harm from your name.</strong> Write “What happened” and “Who I am” on two lines. Do not let the first rename the second. No details.','Separate the harm from your name'),
          ('<strong>Tell your counselor</strong> that shame says you are worthless. Let them help you go slowly.','Tell your counselor'),
          ('<strong>Receive one kindness</strong> this week without explaining why you do not deserve it.','Receive one kindness'),
          ('<strong>If the shame includes wanting to die,</strong> call or text 988, or tell someone near you today.','Get help if you want to die')],
 prayer='Lord, I feel damaged and ashamed, as if what was done to me made me worthless. You bind up the brokenhearted. Teach me that I am still loved, and stay near while the shame is loud. Amen.',
 tracker='A moment I was not worthless')

add(num=63, file='They-Wont-Believe-Me', crisis=False,
 key='Psalm 34:18', also=['Galatians 6:2','Romans 12:15','Isaiah 61:1','1 Peter 5:7'],
 pearls=['trust','help','loneliness','love-by-god','friendship'], gc=[17,27,22],
 songs=[('truth','Truth can be told to a safe person. Not every listener is a courtroom.'),('body','God’s people are called to come near, not to cross-examine the wounded.'),('stays','God does not walk out when the story is hard to hear.'),('friend','You can bring the fear of not being believed to God first.')],
 origins='Many people stay quiet because they expect disbelief or blame. Sometimes that fear comes from already having been dismissed. The lie says that telling anyone will fail: they will not believe you, or they will make it your fault. Some people are unsafe to tell. That does not mean there is no one who can hear you. You choose who, and how much. A counselor is one place to start, and you can stop whenever you need to.',
 teaches='The Lord is near the brokenhearted. He does not begin with an interrogation. Believers are told to carry one another’s burdens and to weep with those who weep. God binds up the brokenhearted. You can cast this fear on Him because He cares. These verses do not force you to disclose. They say that being heard is possible, and that disbelief from one person is not the verdict of God or of every person.',
 replacement='Some people may not believe me, and that does not mean no one will. I can choose a safe person, say only what I want, and stop.',
 truths=['One person not believing me is not everyone.','I get to choose who hears me.','I do not have to tell the whole story to be believed about the fact that I was hurt.','God already knows, and He is near.','A counselor can hear me at my pace.','I can stop a conversation that does not feel safe.'],
 self=['No one will believe me.','They will say I caused it.','I should keep quiet so I am not put on trial.','If I cannot prove it, it does not count.','Telling will only make me the problem.','Even God would take their side.'],
 errors=[('Fortune telling','Deciding in advance that every listener will fail you.'),('Overgeneralization','Turning one dismissal into “no one will believe me.”'),('Mind reading','Knowing what a safe person would say before you ask.'),('All-or-nothing thinking','Either everyone believes every detail or telling is pointless.')],
 questions=['Who actually dismissed me, and have I made them stand for everyone?','What would “a safe listener” need to be like?','Do I have to prove the whole story before I am allowed to say I was hurt?','What is the smallest true sentence I would be willing to try, and with whom?','What does God do with the brokenhearted while people argue?','What stop signal do I want with my counselor?'],
 prompt='When you were sure you would not be believed', moment='telling felt like walking into blame',
 example='Psalm 34:18 becomes: “<strong>Sarah</strong> can write: “The Lord is near me. I do not have to convince everyone before I am allowed to speak.””',
 reading='help', read_label='Help',
 actions=[('<strong>Do not start with the hardest listener.</strong> With your counselor, name one person who might be safe, or decide the counselor is the first hearer.','Choose a safe first listener'),
          ('<strong>Agree on a stop.</strong> Before any conversation, decide the sentence you will use to pause.','Agree on a stop'),
          ('<strong>Practice one sentence</strong> that does not include graphic detail: “I was hurt, and I need you to believe that.”','Practice one sentence'),
          ('<strong>If telling is not safe yet,</strong> you do not have to. Call 911 or 1-800-799-7233 if you are in danger now.','You do not have to tell yet')],
 prayer='Lord, I expect disbelief and blame. Be near me. Give me one safe person, a slow pace, and the freedom to speak or to wait. Amen.',
 tracker='A time I was heard')

add(num=64, file='I-Dont-Deserve-to-Be-Safe', crisis=False,
 key='Psalm 46:1', also=['Isaiah 41:10','1 Peter 5:7','Psalm 34:18','Deuteronomy 31:8'],
 pearls=['fear','safety' if False else 'trust','peace','love-by-god','help'], gc=[5,30,17],
 songs=[('held','You are allowed to be held. Safety is not a prize you earn.'),('soul','A hurting soul can hope for safety without having to deserve it first.'),('worn','Being worn down is not a reason you should stay unsafe.'),('assurance','You belong to Christ. Safety and kindness are not rewards for being unharmed.')],
 origins='Harm can teach a person that safety and kindness are for other people. If you were not protected, it is easy to decide you did not deserve protection. That is the lie. Safety is not a wage. Kindness is not something you qualify for by being unhurt or by being perfect. You are allowed to want safety, to ask for it, and to leave what is unsafe. You do not have to explain why you are worth protecting.',
 teaches='God is a refuge and strength, an ever-present help. That help is not issued to the people who earned a safe life. “Do not fear, for I am with you.” He cares for you, and you can cast anxiety on Him. He is near the brokenhearted. He will not forsake you. None of these verses say, “If you had deserved it, you would have been safe.” They say He is a refuge for people in trouble.',
 replacement='I deserve to be safe and treated kindly. Safety is not something I have to earn, and what was done to me did not remove my right to it.',
 truths=['Safety is not a reward.','I am allowed to want kindness.','What was done to me did not make me undeserving.','God is a refuge for people in trouble, including me.','I can ask for protection without making a case for my worth.','Leaving or getting help is not selfish.'],
 self=['I probably deserved it.','Safe homes are for other kinds of people.','If I ask for kindness, I am being greedy.','I should be grateful it was not worse.','Protecting myself would hurt them, so I should not.','God helps people who deserve it. I do not.'],
 errors=[('Personalization','Deciding harm means you were unworthy of safety.'),('Emotional reasoning','Feeling undeserving and calling that God’s view.'),('Discounting the positive','Treating every offer of safety as something you should refuse.'),('All-or-nothing thinking','If life has been unsafe, you are not allowed to seek safety now.')],
 questions=['Who taught me that I had to earn safety?','Would I tell a child they did not deserve to be safe?','What would I do for a friend in my situation?','Is staying a choice, or a rule that says I do not count?','What does “God is our refuge” offer to someone who feels undeserving?','What is one step toward safety I can take with a counselor or a hotline, not alone?'],
 prompt='When you felt you did not deserve safety', moment='kindness or protection felt like too much to ask',
 example='Psalm 46:1 becomes: “<strong>Sarah</strong> can write: “God is a refuge for me. I do not have to earn the right to be safe.””',
 reading='fear', read_label='Fear',
 actions=[('<strong>Say the sentence aloud:</strong> “I am allowed to be safe.” Notice the argument that follows, and do not obey it.','Say you are allowed to be safe'),
          ('<strong>Make one safety contact</strong> if you are not safe: 911, or 1-800-799-7233. If a child is being hurt, call 1-800-422-4453.','Make one safety contact'),
          ('<strong>Accept one kindness</strong> this week without apologizing for needing it.','Accept one kindness'),
          ('<strong>Plan with your counselor</strong> one boundary or exit step. Do not do a dangerous step alone.','Plan one step with your counselor')],
 prayer='Lord, I have believed I do not deserve safety or kindness. You are a refuge. Teach me that protection is not a prize, and give me courage to reach for help. Amen.',
 tracker='A step I took toward safety')

# fix pearls for 64 - I used a bad conditional. Will set properly below.
C[-1]['pearls'] = ['fear','trust','peace','love-by-god','help']

add(num=65, file='I-Have-to-Keep-This-Secret', crisis=False,
 key='Galatians 6:2', also=['2 Corinthians 1:3–4','Psalm 34:18','Romans 12:15','1 Peter 5:7'],
 pearls=['help','trust','fear','loneliness','thinking-healthy'], gc=[17,22,27],
 songs=[('speak','You can speak a little. A secret does not have to be your only safety.'),('even','You can bring a hard truth to God even if you are not ready to tell a person.'),('forgive','The song is about releasing what someone did, not about keeping their secret for them.'),('faithful','God’s faithfulness does not depend on your silence.')],
 origins='Secrets often start as survival. Someone said telling would ruin the family, the church, or you. Or you learned that speaking made things worse. Silence can be wise when a person is not safe to tell. The lie says you must keep the secret forever, and that speaking up will only destroy everything. You are allowed to tell a safe person. You are allowed to tell only what you choose. Telling a counselor, a hotline, or the police is not betrayal. It is a way to get help.',
 teaches='We are told to carry one another’s burdens, which cannot happen if the burden is locked away from every safe person. God is the God of all comfort. He is near the brokenhearted. People who follow Him are told to weep with those who weep. You can cast this fear on Him because He cares. None of this demands a public story. It does say that a secret kept from everyone is not the only faithful choice.',
 replacement='I do not have to keep this secret from every safe person. I can tell a counselor or a helper, say only what I choose, and ask for protection.',
 truths=['Silence kept me going, and it does not have to last forever.','I choose who hears me.','Telling a safe helper is not destroying everything.','God already knows, and He is not shocked.','I can stop if a conversation stops feeling safe.','A hotline or a counselor can hear me without my having to face the person who hurt me.'],
 self=['If I tell, everything will fall apart.','I would be betraying the family or the church.','No one can know.','Speaking up would only make it worse for me.','Good people keep this kind of thing quiet.','God wants me to protect their reputation.'],
 errors=[('Fortune telling','Deciding that any word will certainly ruin everything.'),('All-or-nothing thinking','Either the secret stays with everyone or you tell the world.'),('Emotional reasoning','Feeling panic at the thought of telling, and calling panic a command.'),('Mind reading','Assuming every helper would make it worse.')],
 questions=['Who told me this had to stay a secret, and did they have something to protect?','Is there one person whose job is to help, not to guard the secret?','What am I afraid will happen, and what might happen if I stay silent?','Do I have to tell everything in order to get help?','What would I want a friend to do with a secret like this?','What number can I call if I am not safe today?'],
 prompt='When the secret felt mandatory', moment='speaking up felt like it would destroy everything',
 example='Galatians 6:2 becomes: “<strong>Sarah</strong> can write: “I can let one safe person help carry this. I do not have to keep it alone.””',
 reading='help', read_label='Help',
 actions=[('<strong>Tell one professional first,</strong> a counselor or 1-800-799-7233, not the person who hurt you. You can say as little as “I am not safe” or “I need help with abuse.”','Tell one professional first'),
          ('<strong>Write what you are willing to say</strong> in one sentence, with no graphic detail. You do not have to share it today.','Write one sentence'),
          ('<strong>Name who must not be the first hearer.</strong> The person who hurt you does not get to control the secret.','Name who is not a safe first hearer'),
          ('<strong>If a child is being hurt,</strong> call Childhelp at 1-800-422-4453 or 911. You do not have to investigate it yourself.','Call if a child is being hurt')],
 prayer='Lord, I have carried this secret because I was afraid speaking would ruin everything. You already know. Give me one safe helper, and the courage to tell only what I choose. Amen.',
 tracker='A step out of total silence')

add(num=66, file='I-Should-Have-Fought-or-Left', crisis=False,
 key='Psalm 103:13–14', also=['Romans 8:1','Psalm 34:18','Isaiah 61:1','John 14:27'],
 pearls=['guilt-shame','thinking-healthy','fear','self-esteem-low','help'], gc=[29,24,27],
 songs=[('chains','Grace does not put you on trial for a door you could not open then.'),('wins','Grace wins over the charge that surviving was the same as agreeing.'),('again','You can begin again without first proving you should have left sooner.'),('victory','Christ’s victory is not a prize reserved for the person who fought perfectly.')],
 origins='After harm, people torture themselves with the exit they can see now. “I should have fought harder. I should have left sooner. Because I didn’t, I agreed.” That uses today’s knowledge against the person you were then. Freezing, staying, hoping, having nowhere to go, loving someone, or being afraid are not consent. Not leaving is not the same thing as agreeing. You do not owe anyone a story of why you stayed.',
 teaches='The Lord knows our frame. He has compassion as a father has compassion on his children. There is no condemnation in Christ for the person who survived the way they could. He is near the brokenhearted. He binds up the brokenhearted. Jesus says not to let your heart be troubled. These verses do not scold you for the strategy that kept you alive. Agreement is a free yes. Fear, confusion, and having no safe exit are not a yes.',
 replacement='Not fighting or not leaving was not agreement. I survived the way I could, and that was not consent.',
 truths=['Staying was not the same as agreeing.','I judge my past self with facts I may not have had then.','Freezing or hoping is a human response, not permission.','God knows my frame. He is not cross-examining me.','I can leave or get help now without proving I should have sooner.','My counselor can help me drop this charge.'],
 self=['I agreed because I stayed.','If I had been braver, it would have stopped.','A strong person would have left the first time.','I have no right to complain now.','God wanted me to endure it.','Leaving now would prove I could have left then, so I must not.'],
 errors=[('Hindsight bias','Blaming your past self for not using an exit you can see only now.'),('All-or-nothing thinking','If you did not fight perfectly or leave immediately, you agreed.'),('Emotional reasoning','Feeling ashamed of staying and calling the shame consent.'),('Personalization','Making your survival strategy the cause of their choice.')],
 questions=['What choices did I actually have then, not the ones I can imagine now?','Does staying, freezing, or hoping equal a free yes?','Would I tell a friend that not leaving meant they agreed?','Who benefits if I keep this charge against myself?','What would getting help now look like, without a trial about the past?','What does “He knows our frame” mean for the person I was then?'],
 prompt='When you accused yourself of agreeing', moment='not leaving felt like consent',
 example='Psalm 103:14 becomes: “<strong>Sarah</strong> can write: “God knows my frame. Not leaving was not a yes.””',
 reading='guilt-shame', read_label='Guilt/Shame',
 actions=[('<strong>Retire “I agreed.”</strong> When the sentence comes, answer, “Survival is not consent,” and stop. No replay of events.','Retire “I agreed”'),
          ('<strong>Ask your counselor</strong> to help you look at then versus now. Stop if you feel flooded.','Ask your counselor'),
          ('<strong>One present step,</strong> not a verdict on the past: a call to 1-800-799-7233, a locked door, or a plan with your counselor.','One present step'),
          ('<strong>Read Psalm 103:13–14</strong> when the “I should have” voice starts.','Read the compassion verse')],
 prayer='Lord, I have called my survival a yes. You know my frame. Teach me that not leaving was not agreement, and give me help for the life I have now. Amen.',
 tracker='A moment I did not call survival consent')

add(num=67, file='Kindness-Is-a-Trap', crisis=False,
 key='1 Peter 5:7', also=['Psalm 34:18','John 14:27','Romans 8:38–39','Galatians 6:2'],
 pearls=['trust','fear','love-by-god','friendship','help'], gc=[17,5,29],
 songs=[('knows','Jesus knows harm and still offers kindness that is not a setup.'),('love','Receiving love can be slow. It does not have to be a trap.'),('jesus','Jesus’ gentleness is not the start of harm.'),('eyes','Look at Christ’s kindness when a gentle person feels dangerous.')],
 origins='If gentleness was once the doorway to harm, kindness itself starts to feel like bait. A soft voice, a favor, or patience can make your body brace. That reaction is understandable. The lie says every gentle person is getting ready to hurt you, so you must refuse care. Some people are unsafe, and you are allowed to be careful. Not every kind person is the person who hurt you. A counselor can help you tell the difference without shaming the alarm.',
 teaches='You can cast anxiety on God because He cares for you. His care is not a lure. He is near the brokenhearted. Jesus gives peace and says not to be afraid. Nothing can separate you from the love of God. Believers are told to carry burdens, which is a form of kindness. Scripture does not tell you to trust every smile. It does tell you that real care exists, and that God’s kindness is not the opening move of harm.',
 replacement='Some kindness was misused, and that does not make all kindness a trap. I can go slowly, and I can receive care from safe people and from God.',
 truths=['My alarm can be honored without becoming a law about everyone.','God’s care is not a setup.','I can go slowly with a gentle person.','I am allowed to receive help.','One unsafe person does not equal every kind person.','My counselor can help me test safety without rushing trust.'],
 self=['If they are nice, they want something.','Gentleness is how it starts.','I should reject help before it turns.','No one is kind unless they are planning harm.','I would rather be harsh than fooled.','Even God’s kindness is a trick.'],
 errors=[('Overgeneralization','Turning one betrayal of kindness into “all kindness is a trap.”'),('Fortune telling','Deciding a gentle moment will certainly become harm.'),('Mind reading','Assigning a hidden motive to every kind act.'),('Emotional reasoning','Feeling braced and calling the brace proof of danger.')],
 questions=['Who used kindness badly, and who has not?','What would slow trust look like, short of refusing everyone?','Is this the same person, or a reminder in my body?','What kindness have I received that did not turn into harm?','How is God’s care different from the care that was misused?','What limit can I set while I am still receiving help?'],
 prompt='When kindness felt like a setup', moment='gentleness made you brace for harm',
 example='1 Peter 5:7 becomes: “<strong>Sarah</strong> can write: “I can bring this fear to God, because His care is not a trap.””',
 reading='trust', read_label='Trust',
 actions=[('<strong>Name the old pattern and the present person.</strong> Two lines, no story: who misused kindness, and who is in front of you now.','Name then and now'),
          ('<strong>Receive one small help</strong> from someone you and your counselor consider safe. Write what they did afterward.','Receive one small help'),
          ('<strong>Keep a limit.</strong> You can accept kindness and still say no to more than you want.','Keep a limit'),
          ('<strong>Pray 1 Peter 5:7</strong> when a gentle voice makes you brace.','Pray when kindness feels dangerous')],
 prayer='Lord, kindness makes me brace. Some of that wisdom was earned. Teach me that not every gentle person is a trap, and that Your care is safe. Help me go slowly. Amen.',
 tracker='A kindness that did not turn into harm')

add(num=68, file='I-Have-to-Keep-Them-Calm', crisis=False,
 key='Psalm 118:6', also=['Isaiah 41:10','Galatians 6:2','Psalm 46:1','John 14:27'],
 pearls=['fear','anxiety-worry','trust','help','peace'], gc=[5,17,29],
 songs=[('fear','You do not have to manage another person’s anger in order to be safe with God.'),('battle','Their mood is not a battle you are required to win.'),('power','God’s strength is for you, not for keeping someone else from ever being upset.'),('lives','You can face a hard moment without appointing yourself their emotional guard.')],
 origins='If someone’s anger was dangerous, you may have learned to watch their face and smooth every wave. Keeping them calm felt like keeping yourself, or the children, alive. That skill was survival. The lie says their feelings are your job, and that if they get angry, you failed and you caused the harm. You are not the manager of another adult’s emotions. You are allowed to be a person, not a shock absorber. If their anger is still dangerous, the next step is safety, not better calming.',
 teaches='The Lord is on your side. You do not have to be afraid of a human being as if their mood were your god. “Do not fear, for I am with you.” God is a refuge. Jesus gives peace that is not the same as a house where everyone must stay pleasant. We carry one another’s burdens, which is mutual care, not one person preventing another’s anger at all costs. Their anger is theirs. Your safety matters.',
 replacement='Their feelings are not my job. I am not the cause of their anger, and I am allowed to be safe instead of keeping them calm.',
 truths=['I can care without managing another adult’s emotions.','Their anger is not automatically my fault.','Keeping the peace is not the same as being safe.','God is on my side. I am not alone with their mood.','I can say no without being responsible for their reaction.','If I am not safe, I can call for help instead of trying harder to soothe them.'],
 self=['If I say the wrong thing, it is my fault when they explode.','A good partner, child, or Christian keeps them calm.','I have to read the room or someone gets hurt.','My needs make them angry, so my needs are the problem.','If I were better, they would be peaceful.','Leaving would be cruel because they need me to regulate them.'],
 errors=[('Personalization','Making their emotion your responsibility and your fault.'),('Emotional reasoning','Feeling dread and concluding you must fix their mood.'),('All-or-nothing thinking','Either you keep them calm or you are to blame for harm.'),('Fortune telling','Deciding that any honesty will certainly cause an explosion you must prevent.')],
 questions=['Whose feeling is this, and who is making me carry it?','What happens to me when I spend the day preventing their anger?','Would I tell a friend it was their job to keep someone else calm?','Is soothing them keeping me safe, or only postponing harm?','What would one honest sentence cost, and do I have a safety plan?','What does “the Lord is on my side” free me from managing?'],
 prompt='When you rushed to keep someone calm', moment='their mood felt like your fault to prevent',
 example='Psalm 118:6 becomes: “<strong>Sarah</strong> can write: “The Lord is on my side. I do not have to manage their anger to be safe.””',
 reading='fear', read_label='Fear',
 actions=[('<strong>Pause one fix.</strong> The next time you start to smooth their mood, wait ten seconds if it is safe, and notice that their feeling is still theirs.','Pause one fix'),
          ('<strong>Make a safety plan</strong> with your counselor or with 1-800-799-7233 if their anger is dangerous. Do not experiment with honesty that could put you in danger.','Make a safety plan'),
          ('<strong>Write “not my job”</strong> on a card you can see. Their emotion is on one side. Your safety is on the other.','Write “not my job”'),
          ('<strong>Tell your counselor</strong> how much of the day you spend preventing someone’s anger.','Tell your counselor')],
 prayer='Lord, I have lived as the one who must keep them calm. You are on my side. Free me from carrying their anger, and show me the safe next step. Amen.',
 tracker='A moment their feeling was not my job')

add(num=69, file='I-Dont-Get-to-Decide-About-My-Body', crisis=False,
 key='Psalm 139:14', also=['Isaiah 43:2','Psalm 34:18','1 Peter 5:7','Romans 8:38–39'],
 pearls=['self-esteem-low','fear','love-by-god','guilt-shame','trust'], gc=[24,27,17],
 songs=[('liar','The lie that your no does not count is not the truth about your body.'),('greater','God’s care for you is greater than someone else’s claim on your body.'),('want','What you want for your own body is allowed to matter.'),('tender','Christ is gentle. Gentleness does not override your no.')],
 origins='When someone treats your body as if it belonged to them, you can start to believe the treatment. “I don’t get to decide. Saying no doesn’t count.” That is what harm teaches. It is not the truth. Your body is not a possession of another person. A no counts even if it was ignored. A yes that was forced, frightened, or not free was not a real yes. You do not have to describe what happened in order to hold this truth. A counselor can help you practice choice in ordinary, safe ways.',
 teaches='You are fearfully and wonderfully made. That is not a slogan for people who were never harmed. It means your body is not trash and not someone else’s property. When you pass through what feels like deep water, God is with you. He is near the brokenhearted. He cares for you. Nothing can separate you from His love. These verses do not erase what was done. They say your no still counts, and your body is still yours to steward before God, not to surrender to whoever demands it.',
 replacement='My body is not someone else’s to decide about. My no counts, even if it was ignored.',
 truths=['A no counts even when someone acts as if it does not.','I am fearfully and wonderfully made, not owned.','Forced or frightened agreement is not a real yes.','I can practice small choices now.','God is near me. He does not side with the person who ignored my no.','I can talk with a counselor without giving details.'],
 self=['I do not get a vote about my own body.','Saying no just makes it worse, so it does not count.','If I froze, I agreed.','My body is already ruined, so boundaries are pointless.','Other people’s wants matter more than my no.','God expects me to submit even when I am afraid.'],
 errors=[('All-or-nothing thinking','If your no was ignored once, it never counts.'),('Emotional reasoning','Feeling powerless and concluding you have no right to choose.'),('Personalization','Treating their demand as a duty you failed by refusing.'),('Discounting the positive','Ignoring every choice you do have now.')],
 questions=['Who taught me that my no does not count?','What is one choice about my body or my time that is actually mine today?','Would I tell a friend their no was meaningless?','Does freezing or fear turn a no into a yes?','What does “fearfully and wonderfully made” deny about being owned?','What small boundary can I practice with a safe person or my counselor?'],
 prompt='When your no felt like it did not count', moment='a choice about your body felt impossible',
 example='Psalm 139:14 becomes: “<strong>Sarah</strong> can write: “I am fearfully and wonderfully made. My no counts.””',
 reading='self-esteem-low', read_label='Self-Esteem, Low',
 actions=[('<strong>Practice one small no</strong> with a safe person, about time, touch, or a favor. You do not have to explain.','Practice one small no'),
          ('<strong>Write “my no counts”</strong> where you will see it. Do not add the story underneath.','Write “my no counts”'),
          ('<strong>Tell your counselor</strong> that choice about your body feels gone. Ask for ordinary ways to practice it. Stop if you need to.','Tell your counselor'),
          ('<strong>If someone is overriding your no now,</strong> call 911 or 1-800-799-7233. You do not have to manage that alone.','Call if your no is being overridden')],
 prayer='Lord, I was taught that my body was not mine to decide about. I am fearfully and wonderfully made. Restore the truth that my no counts, and give me safe help as I learn to choose again. Amen.',
 tracker='A no I was allowed to mean')

add(num=70, file='Other-People-Had-It-Worse', crisis=False,
 key='Isaiah 61:1', also=['Psalm 147:3','Psalm 34:18','Romans 12:15','Galatians 6:2'],
 pearls=['sorrow','guilt-shame','thinking-healthy','help','love-by-god'], gc=[27,15,29],
 songs=[('who','God’s care for you does not depend on your pain winning a comparison.'),('grace','Grace meets your actual hurt. It does not ask you to rank it.'),('thrive','You are allowed to heal and live, not only to endure because someone else had more.'),('great','God is great enough to care for your wound and for everyone else’s.')],
 origins='Comparison is a way to keep going: “Other people had it worse, so mine doesn’t count.” Sometimes other people said that to silence you. Minimizing can feel humble or tough. It is still a lie if it means your harm does not matter, you should not need help, and you should not tell. Someone else’s deeper pain does not shrink yours. God does not run a contest before He binds up the brokenhearted. You do not have to prove your story was the worst in order for it to count.',
 teaches='God binds up the brokenhearted. He does not first ask whether someone else was broken more. He is near the brokenhearted, not only the people with the most visible wounds. We weep with those who weep, without a scoreboard. We carry one another’s burdens, including burdens the person has been told are too small. Your pain can be real and still not be the worst pain in the world. Both of those things are true.',
 replacement='What was done to me counts, even if someone else suffered more. I am allowed to get help without winning a comparison.',
 truths=['My pain does not have to be the worst to be real.','God binds up my broken heart without a contest.','Minimizing kept me quiet. It does not have to keep me from help.','I can care about others and still name my own hurt.','I do not owe anyone a graphic comparison.','A counselor can take this seriously at my pace.'],
 self=['I should be over it because others had it worse.','Complaining would be selfish.','It was not that bad.','If I get help, I am taking it from someone who needs it more.','I have no right to call it abuse.','God is busy with bigger suffering.'],
 errors=[('Minimization','Shrinking real harm because it is not the worst imaginable harm.'),('All-or-nothing thinking','If it is not the worst, it does not count at all.'),('Emotional reasoning','Feeling you should be fine, and deciding you are fine.'),('Discounting the positive','Refusing help, comfort, or the name of what happened.')],
 questions=['Who benefits if I decide my harm does not count?','Would I tell a friend their pain was too small to matter?','What do I lose by never naming it?','Can two people need help at the same time?','What does God do with a broken heart that is not the most broken?','What is one help I have refused because I thought I should be grateful?'],
 prompt='When you ranked your pain as too small', moment='you decided your harm did not count',
 example='Isaiah 61:1 becomes: “<strong>Sarah</strong> can write: “God binds up the brokenhearted. That includes me, even if someone else suffered more.””',
 reading='sorrow', read_label='Sorrow',
 actions=[('<strong>Drop the contest.</strong> Write “It counts” under the sentence “others had it worse.” Do not list details or other people’s stories.','Drop the contest'),
          ('<strong>Ask for one help you have postponed</strong> because you thought you should cope: a counselor, a friend, or 1-800-799-7233.','Ask for one postponed help'),
          ('<strong>Tell your counselor</strong> you minimize. Let them help you name the impact without a graphic account.','Tell your counselor'),
          ('<strong>If a child is being minimized or hurt,</strong> call 1-800-422-4453 or 911. Their pain counts too.','Call if a child is being hurt')],
 prayer='Lord, I have treated my harm as if it did not count. You bind up the brokenhearted, including me. Help me receive care without winning a comparison. Amen.',
 tracker='A moment my pain was allowed to count')

def main():
    src = (ROOT/'belief-cards/psychological/Psych-041-Something-Terrible-Is-About-to-Happen.html').read_text()
    head, rest = src.split('<!-- ============ CARD ============ -->', 1)
    script = rest[rest.rfind('\n</div><script>')+1:]
    lst = json.loads((ROOT/'tools/lists/psychological.json').read_text())
    group = next(g for g in lst['sections'][0]['groups'] if g['name']=='Abuse')
    beliefs = [b[0] for b in group['beliefs']]
    if len(beliefs) != len(C):
        raise SystemExit(f'count {len(beliefs)} vs {len(C)}')
    sets=set(); outdir=ROOT/'tools/psych-abuse'; outdir.mkdir(exist_ok=True)
    for d, belief in zip(C, beliefs):
        d['belief']=belief
        songset=tuple(k for k,_ in d['songs'])
        if songset in sets: raise SystemExit('dup '+str(songset))
        sets.add(songset)
        kinds=[]; blocks=[]
        for key, why in d['songs']:
            kind, html = A.song(key, why); kinds.append(kind); blocks.append(html)
        if kinds.count('classic')!=1: raise SystemExit(f'mix {d["num"]} {kinds}')
        for slug in list(d['pearls'])+[d['reading']]:
            if slug not in A.PEARLS: raise SystemExit('pearl '+slug)
        base = d['origins']
        if '988' in base or '1-800' in base: raise SystemExit('numbers prebaked '+str(d['num']))
        d['origins'] = base + SAFE + (CRISIS if d['crisis'] else '')
        A.STEP = STEP_TOP if d['crisis'] else STEP_MILD
        shown='“'+belief+'”'
        errs='\n'.join(f'<li><strong>{a}: </strong>{b}</li>' for a,b in d['errors'])
        refs=[d['key']]+d['also'][:2]
        scr='<ul class="opts">\n'+'\n'.join(f'<li><span class="ref">{ref}</span><span class="scrip">“{A.V[ref]}”</span></li>' for ref in refs)+'\n</ul>'
        truths=[d['replacement']]+[t for t in d['truths'] if t!=d['replacement']]
        truths=truths[:6]
        acts='<ul class="opts">\n'+'\n'.join(f'<li>{a}</li>' for a,_ in d['actions'])+'\n</ul>'
        page=A.render_page(d, head, script, blocks, shown, belief, errs, scr, truths, acts)
        page=page.replace('· Anxiety</div>', '· Abuse</div>', 1)
        fname=f"Psych-{d['num']:03d}-{d['file']}"
        page=page.replace('Psych-041-Something-Terrible-Is-About-to-Happen-Homework.pdf', fname+'-Homework.pdf')
        page=page.replace('Psych-041-Something-Terrible-Is-About-to-Happen.pdf', fname+'.pdf')
        page=page.replace('Belief Card: Something terrible is about to happen', 'Belief Card: '+belief.rstrip('.'))
        page=page.replace('“Something terrible is about to happen.”', shown)
        if page.find('<h2>Listen: Overcoming Anxiety</h2>') > page.find('<h2>Listen: Overcoming Depression</h2>'):
            raise SystemExit('audio '+fname)
        if '1-800-799-7233' not in page or '1-800-422-4453' not in page:
            raise SystemExit('safety numbers missing '+fname)
        (ROOT/'belief-cards/psychological'/f'{fname}.html').write_text(page)
        (outdir/f"{d['num']:03d}.json").write_text(json.dumps({
            'num': d['num'], 'file': d['file'], 'group': 'Abuse',
            'belief': '“'+belief+'”', 'belief_plain': belief.rstrip('.'),
            'origins': d['origins'], 'self': d['self'],
            'songs': [k for k,_ in d['songs']], 'key': d['key'],
            'replacement': d['replacement'], 'crisis': d['crisis'],
        }, ensure_ascii=False, indent=1)+'\n')
        group['beliefs'][d['num']-61][:] = [belief, fname+'.html']
        print(d['num'], 'crisis', d['crisis'], 'top988', CRISIS.strip()[:12] in d['origins'])
    (ROOT/'tools/lists/psychological.json').write_text(json.dumps(lst, ensure_ascii=False, indent=1)+'\n')
    print('wired', sum(1 for b in group['beliefs'] if len(b)>1))

if __name__=='__main__':
    main()
