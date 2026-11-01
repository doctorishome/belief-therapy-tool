"""Per-review cognitive errors (name, feeds, sounds like[, note]) and disputing questions.
Question numbers refer to questioning_form.json (spiritual list first, then general)."""
CAREGIVER_Q = 'Have the parent (or an older child) choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief.'
PSYCHOSIS_Q = ('Do not use these to argue with a delusion or with the client’s faith. Once trust is built, have the client choose questions from the '
               '[Questioning False Beliefs]({form}) form that “speak to” the distress, fears, and conclusions around the belief.')
ANXIETY_Q = ('Have the client choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief, then test the answers with exposure. '
             'Do not let the questions become a new form of reassurance.')

DATA = {
'acute': dict(label='trauma symptoms', errors=[
    ('Hindsight bias', 'guilt and replaying the event', 'I should have seen it coming.'),
    ('Personalization', 'self-blame', 'It happened because of me.'),
    ('Catastrophizing', 'hypervigilance and startle', 'I’ll never be safe again.'),
    ('Overgeneralization', 'fear and avoidance of reminders', 'Nowhere is safe anymore.'),
    ('Emotional reasoning', 'persistent fear', 'I feel in danger, so I must be in danger.'),
    ('Avoidance', 'avoidance of memories and reminders', 'If I stay away from that road, I won’t have to feel it.'),
    ('Fortune telling', 'negative mood and hopelessness', 'I’ll never be the same.'),
  ], questions=[
    (45, 'hindsight bias'), (48, 'personalization and self-blame'), (41, 'catastrophizing'), (35, 'overgeneralization'),
    (32, 'emotional reasoning'), (46, 'avoidance'), (12, 'fortune telling'), (4, 'the belief that God abandoned or is punishing me'),
  ]),
'adhd': dict(errors=[
    ('Global labeling', 'shame and low self-esteem', 'I’m just lazy.'),
    ('Overgeneralization', 'discouragement after missed deadlines', 'I never finish anything.'),
    ('Comparisons', 'shame', 'Everyone else can sit still and get it done.'),
    ('Should statements', 'guilt about inattention', 'I should be able to focus in prayer like everyone else.'),
    ('Fortune telling', 'procrastination and avoiding tasks', 'I’ll mess it up, so why start?'),
    ('Unrealistic expectations', 'spiritual guilt about treatment', 'If I trusted God, I wouldn’t need medicine.'),
    ('Jumping to conclusions', 'harsh parenting (in parents)', 'He forgot his homework to defy me.'),
  ], questions=[
    (51, 'global labeling'), (50, 'overgeneralization'), (57, 'comparisons'), (39, 'should statements'),
    (47, 'fortune telling'), (1, 'unrealistic expectations about medication'), (35, 'a parent’s jumping to conclusions'),
  ]),
'adjustment': dict(errors=[
    ('Catastrophizing', 'worry and anxiety', 'This divorce will ruin everything.'),
    ('Helplessness', 'low mood and giving up', 'There’s nothing I can do.'),
    ('Fortune telling', 'hopelessness', 'It will never get better.'),
    ('Underestimating myself', 'withdrawal and avoidance', 'I can’t handle this.'),
    ('Personalization', 'sadness and guilt', 'God is punishing me with this.'),
    ('Unrealistic expectations', 'spiritual guilt', 'A real Christian wouldn’t be this upset.'),
  ], questions=[
    ((31, 8), 'catastrophizing'), (64, 'helplessness'), (42, 'fortune telling'), (47, 'underestimating myself'),
    (4, 'personalization'), (21, 'unrealistic expectations'),
  ]),
'antisocial': dict(errors=[
    ('Blaming others', 'aggression and lack of remorse', 'He made me do it.'),
    ('Jumping to conclusions', 'fights and hostility', 'He looked at me wrong, so he wants trouble.'),
    ('Mind reading', 'suspicion and aggression', 'They think I’m weak.'),
    ('Confirmatory bias', 'deceit and self-justification', 'See? Everybody cheats.'),
    ('Unrealistic expectations', 'entitlement and irritability', 'People should give me what I want.'),
    ('Should statements', 'anger when crossed', 'People should respect me or pay for it.'),
  ], questions=[
    ((22, 2), 'blaming others'), (24, 'jumping to conclusions and mind reading'), (40, 'confirmatory bias'),
    (17, 'entitlement'), (53, 'should statements'), (7, '“God forgives, so it doesn’t matter”'),
  ]),
'anxiety': dict(qintro=ANXIETY_Q, errors=[
    ('Catastrophizing', 'worry and panic', 'If my heart races, I’m having a heart attack.'),
    ('Fortune telling', 'anticipatory anxiety and avoidance', 'I’ll freeze up and embarrass myself.'),
    ('Mind reading', 'social anxiety', 'They can tell I’m nervous and think I’m weird.'),
    ('Emotional reasoning', 'panic and fear', 'I feel afraid, so something bad must be happening.'),
    ('Underestimating myself', 'avoidance and safety behaviors', 'I couldn’t handle it if it happened.'),
    ('Avoidance', 'avoidance', 'If I don’t go, I won’t have to feel it.'),
    ('Should statements', 'spiritual guilt about anxiety', 'I should never feel anxious if I trust God.'),
  ], questions=[
    ((41, 43), 'catastrophizing'), (44, 'fortune telling'), (24, 'mind reading'), (32, 'emotional reasoning'),
    (46, 'underestimating myself'), (37, 'avoidance'), (23, 'should statements and spiritual guilt'),
  ]),
'autism': dict(who=' in parents and in autistic clients',
  qintro='Have the parent or client choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief. With autistic clients, ask one concrete question at a time.',
  errors=[
    ('Global labeling', 'shame (in autistic clients)', 'I’m broken.'),
    ('Comparisons', 'low self-worth and withdrawal', 'Everyone else knows how to act at church.'),
    ('Mind reading', 'social anxiety', 'They all think I’m weird.'),
    ('All-or-nothing thinking', 'distress when plans change', 'If the plan changes, the whole day is ruined.'),
    ('Personalization', 'parental guilt', 'God is punishing us.'),
    ('Fortune telling', 'parental hopelessness', 'She’ll never have a good life.'),
    ('Disqualifying the positive', 'parental discouragement', 'Our child is a burden.'),
  ], questions=[
    ((51, 23), 'global labeling and “God made a mistake with me”'), (48, 'comparisons'), (32, 'mind reading'),
    (27, 'all-or-nothing thinking'), (49, 'parental personalization'), (42, 'fortune telling'), (18, 'disqualifying the positive'),
  ]),
'avoidant': dict(errors=[
    ('Mind reading', 'fear of criticism', 'They think I’m boring.'),
    ('Fortune telling', 'avoiding social situations', 'If I speak up in Bible study, I’ll sound stupid.'),
    ('Global labeling', 'feelings of inadequacy', 'I’m socially inept.'),
    ('Selective attention', 'fear of rejection', 'Nobody talked to me after church.'),
    ('Disqualifying the positive', 'low self-worth', 'They only invited me to be polite.'),
    ('Comparisons', 'feeling inferior', 'Everyone else belongs there.'),
    ('Avoidance', 'avoidance and isolation', 'It’s safer to stay home.'),
  ], questions=[
    (32, 'mind reading'), (44, 'fortune telling'), (51, 'global labeling'), (35, 'selective attention'),
    (18, 'disqualifying the positive'), (55, 'comparisons and fear of rejection'), (46, 'avoidance'), (23, '“God puts up with me”'),
  ]),
'bipolar': dict(qintro='Use these mainly between episodes or during depression; during mania, focus on safety, sleep, and medication. Have the client choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief.',
  errors=[
    ('Emotional reasoning', 'stopping medication', 'I feel fine, so I’m healed.'),
    ('Jumping to conclusions', 'grandiose or spiritualized ideas in hypomania', 'This idea came so fast, God must be in it.'),
    ('All-or-nothing thinking', 'swings in self-view', 'Either I’m completely well or completely broken.'),
    ('Global labeling', 'shame after episodes', 'I’m just crazy.'),
    ('Overgeneralization', 'discouragement', 'I’ll always be at the mercy of this illness.'),
    ('Fortune telling', 'hopelessness in depression', 'Another episode will wreck everything.', 'Always ask about suicide when you hear this.'),
    ('Helplessness', 'poor adherence and low energy', 'Nothing I do changes my moods.'),
  ], questions=[
    (32, 'emotional reasoning'), (7, 'jumping to conclusions'), (27, 'all-or-nothing thinking'), (51, 'global labeling'),
    (47, 'overgeneralization'), (12, 'fortune telling'), (64, 'helplessness'),
  ]),
'conduct': dict(who=' in youth and in parents', qintro=CAREGIVER_Q, errors=[
    ('Jumping to conclusions', 'fighting and hostility', 'He bumped me on purpose.'),
    ('Mind reading', 'hostility toward adults', 'The teacher hates me.'),
    ('Blaming others', 'lack of remorse', 'It’s his fault I hit him.'),
    ('Unrealistic expectations', 'stealing and entitlement', 'I deserve what I take.'),
    ('Global labeling', 'hopelessness and more rule-breaking', 'I’m just a bad kid.'),
    ('Fortune telling', 'parents giving up', 'This child is beyond hope.'),
  ], questions=[
    (24, 'jumping to conclusions'), (32, 'mind reading'), (2, 'blaming others'), (60, 'entitlement and weighing the costs'),
    ((51, 12), 'global labeling and “God gave up on me”'), (63, 'a parent’s fortune telling'),
  ]),
'delusional': dict(qintro=PSYCHOSIS_Q, errors=[
    ('Jumping to conclusions', 'the delusion itself', 'My wife was late, so she’s having an affair.'),
    ('Confirmatory bias', 'a delusion that grows stronger', 'The neighbor’s light was on again—more proof.'),
    ('Selective attention', 'suspicion', 'I saw the same car twice today.'),
    ('Mind reading', 'fear and isolation', 'They’re plotting against me.'),
    ('Emotional reasoning', 'fear', 'I feel watched, so I must be watched.'),
    ('Catastrophizing', 'anxiety and safety behaviors', 'They’re going to harm me.'),
  ], questions=[
    (24, 'jumping to conclusions'), (40, 'confirmatory bias'), (35, 'selective attention'), (32, 'mind reading and emotional reasoning'),
    (41, 'catastrophizing'), (1, 'spiritual forms of the belief'), (53, 'the distress the belief causes'),
  ]),
'dependent': dict(errors=[
    ('Underestimating myself', 'needing others to decide', 'I could never handle that on my own.'),
    ('Helplessness', 'handing over responsibility', 'Nothing I decide turns out right.'),
    ('Catastrophizing', 'fear of being alone', 'If he leaves, I’ll fall apart.'),
    ('Fortune telling', 'fear of disagreeing', 'If I say no, they’ll leave me.'),
    ('Mind reading', 'going along to please others', 'She’ll be angry if I don’t go along.'),
    ('Should statements', 'submission framed as spirituality', 'A good Christian never disagrees.'),
  ], questions=[
    ((46, 47), 'underestimating myself'), (22, 'helplessness'), (37, 'catastrophizing'), (41, 'fortune telling'),
    (55, 'mind reading'), (1, 'should statements'),
  ]),
'dsed': dict(who=', mainly in caregivers', label='problems', qintro=CAREGIVER_Q, errors=[
    ('Jumping to conclusions', 'lax supervision', 'Everyone at church is safe.'),
    ('Mind reading', 'parental hurt', 'She doesn’t need me.'),
    ('Personalization', 'parental discouragement', 'He goes to strangers because I’m a bad mother.'),
    ('All-or-nothing thinking', 'parental hurt', 'If he loved us, he’d never go to strangers.'),
    ('Fortune telling', 'giving up on boundary teaching', 'He’ll never learn to stay close.'),
  ], questions=[
    (32, 'jumping to conclusions'), (24, 'mind reading'), ((49, 48), 'personalization'), (27, 'all-or-nothing thinking'),
    (42, 'fortune telling'),
  ]),
'eating': dict(errors=[
    ('All-or-nothing thinking', 'restricting and bingeing', 'I ate one cookie, so the day is ruined.'),
    ('Emotional reasoning', 'body dissatisfaction', 'I feel fat, so I am fat.'),
    ('Global labeling', 'worth tied to weight or shape', 'I’m disgusting.'),
    ('Selective attention', 'body checking', 'All I see is my stomach.'),
    ('Perfectionism', 'drive for thinness and control', 'If I’m not thin enough, I’ve failed.'),
    ('Comparisons', 'body dissatisfaction', 'Everyone at church is thinner than me.'),
    ('Should statements', 'rigid food rules', 'I shouldn’t eat dessert, ever.'),
  ], questions=[
    (27, 'all-or-nothing thinking'), (32, 'emotional reasoning'), (23, 'global labeling and “God is disgusted with me”'),
    (35, 'selective attention'), (39, 'perfectionism'), (54, 'comparisons'), (53, 'should statements'),
  ]),
'grief': dict(errors=[
    ('Hindsight bias', 'guilt', 'I should have known he was sick.'),
    ('Personalization', 'guilt and spiritual distress', 'God took her to punish me.'),
    ('Should statements', 'spiritual guilt', 'A strong Christian wouldn’t still be grieving.'),
    ('All-or-nothing thinking', 'staying stuck', 'Moving on means I didn’t love him.'),
    ('Fortune telling', 'hopelessness', 'I’ll never be happy again.'),
    ('Avoidance', 'avoiding reminders', 'If I go into her room, I’ll fall apart.'),
  ], questions=[
    (45, 'hindsight bias'), (4, 'personalization'), (48, 'should statements'), (24, 'all-or-nothing thinking'),
    (12, 'fortune telling'), (46, 'avoidance'), (58, 'guilt'),
  ]),
'histrionic': dict(errors=[
    ('All-or-nothing thinking', 'attention-seeking', 'If I’m not the center of attention, I’m invisible.'),
    ('Jumping to conclusions', 'seeing relationships as closer than they are', 'We just met, but she’s my best friend.'),
    ('Emotional reasoning', 'rapidly shifting emotions', 'I feel it so strongly, it must be true.'),
    ('Mind reading', 'discomfort when not noticed', 'They’re bored with me.'),
    ('Catastrophizing', 'dramatic expression', 'This is the worst thing that has ever happened.'),
    ('Comparisons', 'envy', 'She gets all the attention at church.'),
  ], questions=[
    ((4, 55), 'all-or-nothing thinking and worth tied to attention'), (24, 'jumping to conclusions'), (32, 'emotional reasoning'),
    (35, 'mind reading'), (28, 'catastrophizing'), (54, 'comparisons'),
  ]),
'narcissistic': dict(errors=[
    ('All-or-nothing thinking', 'fragile self-worth', 'If I’m not the best, I’m nothing.'),
    ('Unrealistic expectations', 'entitlement', 'People should treat me as special.'),
    ('Blaming others', 'lack of accountability', 'It’s their fault, not mine.'),
    ('Comparisons', 'grandiosity and envy', 'I’m more spiritual than the people at my church.'),
    ('Mind reading', 'belief that others are envious', 'They’re just jealous of me.'),
  ], questions=[
    (39, 'all-or-nothing thinking'), (17, 'entitlement'), ((38, 2), 'blaming others'), (21, 'comparisons'),
    (24, 'mind reading'), (0, '“They need to earn my forgiveness”'),
  ]),
'ocd': dict(qintro=('Use them to question the appraisal, not to settle whether a sin or harm occurred; repeated questioning can become a ritual. '
                    'Have the client choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief, then practice ERP.'),
  errors=[
    ('Catastrophizing', 'anxiety and compulsions', 'If I don’t check, the house will burn down.'),
    ('Over-responsibility', 'checking and rituals', 'If someone gets sick, it will be my fault.'),
    ('Emotional reasoning', 'doubt and scrupulosity', 'I feel guilty, so I must have sinned.'),
    ('Jumping to conclusions', 'distress over intrusive thoughts', 'Having this thought means I want it.'),
    ('Perfectionism', 'repeating rituals', 'My prayer has to be said perfectly.'),
    ('Should statements', 'guilt over intrusions', 'I should never have a bad thought.'),
  ], questions=[
    (36, 'catastrophizing'), (49, 'over-responsibility'), (32, 'emotional reasoning'), (6, 'jumping to conclusions about thoughts'),
    (39, 'perfectionism'), (19, 'scrupulosity and should statements'),
  ]),
'ocpd': dict(errors=[
    ('Perfectionism', 'preoccupation with details', 'Anything less than perfect is unacceptable.'),
    ('Should statements', 'rigidity and overwork', 'Rest is laziness; I should always be working.'),
    ('All-or-nothing thinking', 'inflexibility', 'If it’s not done my way, it’s done wrong.'),
    ('Over-responsibility', 'refusing to delegate', 'If I don’t control it, it will fall apart.'),
    ('Unrealistic expectations', 'conflict with others', 'Everyone should meet my standards.'),
    ('Catastrophizing', 'anxiety about mistakes', 'One mistake will ruin everything.'),
  ], questions=[
    (39, 'perfectionism'), (11, 'should statements'), (24, 'all-or-nothing thinking'), (9, 'over-responsibility'),
    (21, 'unrealistic expectations'), (28, 'catastrophizing'),
  ]),
'odd': dict(who=' in children and in parents', qintro=CAREGIVER_Q, errors=[
    ('Blaming others', 'irritability and blaming', 'He made me mad.'),
    ('Overgeneralization', 'resentment', 'Nobody ever listens to me.'),
    ('Jumping to conclusions', 'anger and spitefulness', 'She did that to annoy me.'),
    ('Global labeling', 'defiance and low self-worth', 'I’m the bad kid.'),
    ('All-or-nothing thinking', 'harsh parenting (in parents)', 'Either I break his will or he wins.'),
    ('Personalization', 'parental guilt', 'God will judge me for my child’s behavior.'),
    ('Fortune telling', 'parents giving up on new methods', 'Praise won’t work with this kid.'),
  ], questions=[
    (24, 'blaming others and jumping to conclusions'), (35, 'overgeneralization'), ((51, 4), 'global labeling and “God is angry with me too”'),
    (27, 'all-or-nothing thinking'), (48, 'a parent’s personalization'), (32, 'fortune telling (test it with a chart)'),
  ]),
'paranoid': dict(errors=[
    ('Mind reading', 'suspicion', 'They’re talking about me.'),
    ('Jumping to conclusions', 'grudges and hostility', 'He forgot to call, so he’s against me.'),
    ('Confirmatory bias', 'a growing sense of threat', 'See? They’re against me again.'),
    ('Selective attention', 'reading hidden insults into remarks', 'I noticed how she said “good morning.”'),
    ('Overgeneralization', 'mistrust of everyone', 'I can’t trust anyone.'),
    ('Fortune telling', 'reluctance to confide', 'If I tell her, she’ll use it against me.'),
  ], questions=[
    (32, 'mind reading'), ((24, 58), 'jumping to conclusions'), (40, 'confirmatory bias'), (35, 'selective attention'),
    (4, 'overgeneralization and “I can’t trust anyone, not even God”'), (44, 'fortune telling'),
  ]),
'personality': dict(errors=[
    ('All-or-nothing thinking', 'unstable relationships', 'You’re either for me or against me.'),
    ('Emotional reasoning', 'emptiness and unstable self-image', 'I feel empty, so I am nothing.'),
    ('Fortune telling', 'fear of abandonment', 'He’ll leave me like everyone else.'),
    ('Mind reading', 'anger and suspicion', 'They secretly hate me.'),
    ('Global labeling', 'shame', 'I’m too bad to be loved.'),
    ('Catastrophizing', 'crises and self-harm', 'I can’t survive this feeling.', 'Always ask about self-harm and suicide when you hear this.'),
  ], questions=[
    (27, 'all-or-nothing thinking'), (32, 'emotional reasoning'), ((42, 23), 'fortune telling and “God will leave me”'),
    (24, 'mind reading'), (20, 'global labeling and “I can never be forgiven”'), (46, 'catastrophizing'),
  ]),
'ptsd': dict(label='trauma symptoms', errors=[
    ('Hindsight bias', 'guilt', 'I should have seen it coming.'),
    ('Personalization', 'self-blame', 'It was my fault.'),
    ('Emotional reasoning', 'false guilt', 'I feel guilty, so I must be guilty.'),
    ('Overgeneralization', 'fear and mistrust', 'Nowhere is safe, and no one can be trusted.'),
    ('Catastrophizing', 'hypervigilance', 'Something terrible is about to happen.'),
    ('Global labeling', 'shame and moral injury', 'I’m ruined.'),
    ('Avoidance', 'avoidance of memories and reminders', 'If I don’t talk about it, it can’t hurt me.'),
  ], questions=[
    (45, 'hindsight bias'), ((48, 4), 'personalization and “God was punishing me”'), (32, 'emotional reasoning'),
    (35, 'overgeneralization'), (41, 'catastrophizing'), (20, 'global labeling and moral injury'), (46, 'avoidance'),
  ]),
'rad': dict(who=', mainly in caregivers', label='problems', qintro=CAREGIVER_Q, errors=[
    ('Personalization', 'parental discouragement', 'This child rejects me because I’m failing.'),
    ('Mind reading', 'harsh or withdrawn parenting', 'She’s doing this on purpose to hurt me.'),
    ('Unrealistic expectations', 'exhaustion and guilt', 'If we love him enough, he will bond right away.'),
    ('Fortune telling', 'giving up', 'He’ll never trust us.'),
    ('Disqualifying the positive', 'missing small gains', 'One hug doesn’t mean anything.'),
    ('Overgeneralization', 'withdrawal (in older children)', 'Adults can’t be counted on.'),
  ], questions=[
    ((48, 4), 'personalization and “I must be failing God”'), (24, 'mind reading'), (39, 'unrealistic expectations'),
    (42, 'fortune telling'), (18, 'disqualifying the positive'), (35, 'overgeneralization'),
  ]),
'schizoid': dict(qintro='Use them gently and without pressure; the goal is curiosity, not persuasion. Have the client choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief.',
  errors=[
    ('Overgeneralization', 'detachment', 'People are always more trouble than they’re worth.'),
    ('All-or-nothing thinking', 'avoiding closeness', 'Either I’m completely on my own or I’ll be swallowed up.'),
    ('Fortune telling', 'declining invitations', 'Going to that group would be pointless.'),
    ('Selective attention', 'little pleasure in people', 'All I notice at church is the noise.'),
    ('Disqualifying the positive', 'emotional flatness', 'That visit didn’t really matter to me.'),
  ], questions=[
    (24, 'overgeneralization'), (27, 'all-or-nothing thinking'), (42, 'fortune telling'), (35, 'selective attention'),
    (53, 'the cost of total detachment'), (4, '“God is distant, and that suits me”'),
  ]),
'schizophrenia': dict(qintro=('Do not use these on the religious content of a delusion or on the client’s faith. Have the client choose questions from the '
                              '[Questioning False Beliefs]({form}) form that “speak to” distress-driving beliefs about voices, illness, and the future.'),
  errors=[
    ('Jumping to conclusions', 'delusional ideas', 'That car followed me, so they’re watching me.'),
    ('Emotional reasoning', 'fear of voices', 'The voice feels powerful, so it must be.'),
    ('Helplessness', 'obeying or giving in to voices', 'I have to do what the voice says.'),
    ('Catastrophizing', 'distress and safety behaviors', 'If I don’t obey, something terrible will happen.'),
    ('Global labeling', 'self-stigma and withdrawal', 'I’m crazy; my life is over.'),
    ('Fortune telling', 'hopelessness', 'I’ll never work or have friends.', 'Ask about suicide when you hear hopelessness.'),
  ], questions=[
    (24, 'jumping to conclusions'), ((32, 6), 'emotional reasoning about a voice’s power'), (64, 'helplessness'),
    (41, 'catastrophizing'), (51, 'global labeling'), (63, 'fortune telling'),
  ]),
'schizotypal': dict(qintro='Keep the tone curious, never mocking. Have the client choose questions from the [Questioning False Beliefs]({form}) form that “speak to” the belief.',
  errors=[
    ('Jumping to conclusions', 'ideas of reference', 'The pastor’s sermon was really about me.'),
    ('Confirmatory bias', 'magical thinking', 'Another license plate sign—more proof.'),
    ('Selective attention', 'odd beliefs and perceptions', 'I only notice the signs that are meant for me.'),
    ('Emotional reasoning', 'unusual perceptions', 'I sense evil in him, so it must be there.'),
    ('Mind reading', 'suspicion and social anxiety', 'They think I’m strange.'),
    ('Fortune telling', 'avoiding people', 'If I go, they’ll laugh at me.'),
  ], questions=[
    (24, 'jumping to conclusions'), ((40, 1), 'confirmatory bias and private spiritual ideas'), (35, 'selective attention'),
    (32, 'emotional reasoning and mind reading'), (44, 'fortune telling'),
  ]),
'somatic': dict(qintro=ANXIETY_Q, errors=[
    ('Catastrophizing', 'health anxiety', 'This headache must be a brain tumor.'),
    ('Selective attention', 'focus on the body', 'I notice every twinge.'),
    ('Emotional reasoning', 'distress about symptoms', 'I feel sick, so something must be seriously wrong.'),
    ('Fortune telling', 'checking and reassurance-seeking', 'If I stop checking, something terrible will happen.'),
    ('Disqualifying the positive', 'repeated tests and doctor visits', 'The tests were normal, but they missed something.'),
    ('Personalization', 'spiritual distress', 'God is punishing me with this illness.'),
    ('Unrealistic expectations', 'spiritual guilt', 'If I had enough faith, I would be healed.'),
  ], questions=[
    (41, 'catastrophizing'), (35, 'selective attention'), (32, 'emotional reasoning'), (43, 'fortune telling'),
    (40, 'disqualifying the positive'), (4, 'personalization'), (9, 'unrealistic expectations and demanding certainty'),
  ]),
'substance': dict(errors=[
    ('All-or-nothing thinking', 'lapses turning into relapse', 'I slipped once, so I’ve blown it; I might as well keep using.'),
    ('Emotional reasoning', 'giving in to cravings', 'I need it so badly, I have to have it.'),
    ('Global labeling', 'shame', 'I’m just an addict.'),
    ('Blaming others', 'continued use', 'I only drink because of my wife.'),
    ('Fortune telling', 'hopelessness', 'I’ll never stay clean.'),
    ('Unrealistic expectations', 'refusing treatment', 'If I had enough faith, I wouldn’t need treatment.'),
  ], questions=[
    ((27, 38), 'all-or-nothing thinking'), (37, 'emotional reasoning about cravings'), ((51, 20), 'global labeling and “God could never forgive me”'),
    (22, 'blaming others'), (63, 'fortune telling'), (1, 'unrealistic expectations about treatment'),
  ]),
}
