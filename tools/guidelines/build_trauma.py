# Builds counselors/guidelines-trauma.html. Run from repo root: python3 tools/guidelines/build_trauma.py
import sys; sys.path.insert(0, 'tools/guidelines')
from common import page, belief_table, doi, link

P = 'psychological/'
BELIEFS = [
 ('Nowhere is really safe. Danger is about to happen again.', 'What is the actual danger here, today? How is now different from then?', P + 'Psych-051-Nowhere-Is-Really-Safe.html'),
 ('What happened was my fault. I should have seen it coming and stopped it.', 'What did you know at the time, and what choices did you really have in those seconds?', P + 'Psych-053-What-Happened-Was-My-Fault.html'),
 ('I can’t trust anyone. If I let my guard down, I’ll be hurt again.', 'Is it true of everyone? How could you tell a safe person from an unsafe one?', P + 'Psych-052-I-Cant-Trust-Anyone.html'),
 ('I’m permanently damaged, and I will never be myself again.', 'What parts of you came through this? What does God say about who you are?', P + 'Psych-054-Im-Permanently-Damaged.html'),
 ('I have no control. If it happened once, nothing I do can stop it from happening again.', 'What is within your control now that was not then?', P + 'Psych-056-I-Have-No-Control.html'),
 ('When my body reacts, the danger is happening now.', 'Is your body remembering, or is something dangerous happening right now? How can you check?', P + 'Psych-058-When-My-Body-Reacts-the-Danger-Is-Now.html'),
 ('If I talk about it, I will fall apart.', 'Has talking about painful things ever helped before? What would make it safe enough to try a little?', P + 'Psych-059-If-I-Talk-About-It-I-Will-Fall-Apart.html'),
 ('My future holds only more pain.', 'Is that a prediction or a feeling? What would one better day look like?', P + 'Psych-055-My-Future-Holds-Only-More-Pain.html'),
]

G = []
G.append(('resilience', 'Expect Resilience, Offer Early Support Wisely', 'Most people recover; avoid forced debriefing.', ['All steps'],
 'Many people go through terrible events and recover without developing PTSD. Early on, people need safety, calm, connection, and practical help. Research does not support routine single-session “debriefing” that pushes everyone to relive the event right away; it does not prevent PTSD and may make some people worse.',
 ['In the first days and weeks, focus on safety, basic needs, sleep, and connection with supportive people.',
  'Tell clients that fear, jumpiness, bad dreams, and replaying the event are common at first and often ease with time.',
  'Do not require anyone to tell the whole story in detail soon after the event.',
  'Watch who is not recovering after the first month; they may need trauma-focused treatment.'],
 ['What you are feeling is a normal reaction to something that was not normal. What would help you feel a little safer today?'],
 ('The LORD is near to the brokenhearted; He saves the contrite in spirit.', 'Psalm 34:18'), ''))
G.append(('safety', 'Put Safety and Stability First', 'Stabilize before processing.', ['Identify'],
 'Trauma work can stir up strong emotions. Before going into the memories, make sure the client is safe now and has ways to calm themselves.',
 ['Ask whether the danger is still present: an abusive relationship, unsafe housing, ongoing threats.',
  'Ask directly about suicidal thoughts, self-harm, and alcohol or drug use. In a crisis, call 911 or call or text 988.',
  'Teach grounding skills: noticing five things you see, slow breathing, feeling your feet on the floor, holding a comforting object.',
  'Watch for dissociation (spacing out, losing time, feeling unreal). Slow down and bring the client back to the present.',
  'Stabilizing does not mean waiting forever. Once the client is reasonably safe and steady, move toward treatment of the trauma itself.'],
 ['Before we go any further, let’s make sure you have a few ways to calm your body when the memories come up.'],
 None, ''))
G.append(('assess', 'Assess Carefully and Thoroughly', 'Know what you are treating.', ['Identify'],
 'Trauma can lead to PTSD, but also to depression, anxiety, substance misuse, sleep problems, physical health problems, and relationship difficulties. Careful assessment guides the right treatment.',
 ['Ask about trauma history gently and in general terms first; the client does not need to give details to be assessed.',
  'Use brief, free measures such as the PC-PTSD-5 (screen) and the PCL-5 (symptom checklist) from the National Center for PTSD, and repeat the PCL-5 to track progress.',
  'Distinguish Acute Stress Disorder (3 days to 1 month after the event) from PTSD (more than 1 month).',
  'Note repeated, long-term trauma such as childhood abuse or domestic violence, which often brings added problems with emotions, self-worth, and relationships.',
  'Screen for depression, substance use, and suicide risk, which often occur alongside PTSD.'],
 [], None,
 '<div class="crit"><p style="margin:6px 0"><strong>PTSD (DSM-5-TR), in brief:</strong> exposure to actual or threatened death, serious injury, or sexual violence (directly, as a witness, learning it happened to someone close, or repeated exposure to details through work), followed for more than a month by symptoms in four groups:</p>'
 '<ol><li><strong>Intrusion:</strong> unwanted memories, nightmares, flashbacks, distress at reminders</li><li><strong>Avoidance:</strong> of memories, thoughts, people, or places linked to the event</li><li><strong>Negative changes in thinking and mood:</strong> distorted blame, persistent fear, guilt or shame, beliefs like “I am bad” or “The world is completely dangerous,” feeling cut off</li><li><strong>Arousal and reactivity:</strong> irritability, recklessness, being on guard, startling easily, poor concentration and sleep</li></ol>'
 '<p style="margin:6px 0">Notice that group 3 is about <em>beliefs</em>. This is where Belief Counseling fits most directly. For the full teaching overview, see <a href="reviews/ptsd-teaching-overview.html">PTSD</a> and <a href="reviews/acute-stress-teaching-overview.html">Acute Stress Disorder</a> on the Disorders page.</p></div>'))
G.append(('treat', 'Use Trauma-Focused Treatments With the Best Evidence', 'Proven therapies first; get trained.', ['Challenge', 'Replace'],
 'PTSD is very treatable. The VA/Department of Defense guideline (2023) and the American Psychological Association guideline (2025) both recommend trauma-focused psychotherapies such as Cognitive Processing Therapy (CPT) and Prolonged Exposure (PE); the VA/DoD guideline also recommends EMDR. These therapies are recommended over medication when both are available.',
 ['Practice only the methods you are trained in. If you are not trained in a trauma-focused therapy, get training and supervision, or refer.',
  'Explain the options to the client and decide together; client preference matters.',
  'When needed, refer for a medication evaluation; sertraline, paroxetine, and venlafaxine are the medications the VA/DoD guideline recommends.',
  'Track progress with the PCL-5. If the client is not improving, review the plan with your supervisor.',
  'Treat nightmares and sleep problems; they often improve with trauma treatment, and some need specific treatment.'],
 [], None, ''))
G.append(('stuck', 'Target the Beliefs Trauma Leaves Behind', 'Trauma teaches lies; help unlearn them.', ['Identify', 'Challenge', 'Replace'],
 'Cognitive Processing Therapy calls them “stuck points”: beliefs formed by trauma about safety, trust, control, self-worth, and closeness that keep PTSD going. These are false beliefs in the Belief Counseling sense. Identifying them, examining them with Socratic questions, and replacing them with truth is central to recovery.',
 ['Listen for over-accommodated beliefs (“The world is completely dangerous,” “I can never trust anyone”) and self-blame (“It was my fault”).',
  'Use gentle Socratic questions; do not argue. Let the client discover the evidence.',
  'Aim for balanced beliefs, not the opposite extreme: “Some places and people are dangerous, but I can learn to tell the difference.”',
  'When the client is ready and wants it, bring in Scripture that speaks to safety, worth, and God’s presence.',
  'Assign the matching belief card as homework.'],
 [], None, belief_table(BELIEFS)))
G.append(('avoidance', 'Approach Avoidance Gently', 'Avoidance keeps PTSD going.', ['Challenge'],
 'Avoiding memories and reminders brings short-term relief but keeps the fear alive. Recovery usually means approaching what has been avoided, gradually and safely, with the client in control.',
 ['Explain why avoidance keeps symptoms going, in plain words.',
  'Build a step-by-step list of avoided situations together, starting with the easiest.',
  'Separate dangerous situations (which should be avoided) from safe reminders (which can be approached).',
  'The client sets the pace. Never surprise a client with a reminder or force them to talk.'],
 ['Avoiding it has helped you get through. But it may also be keeping the fear alive. Would you like to work on that together, a small step at a time?'],
 ('When you pass through the waters, I will be with you; and when you go through the rivers, they will not overwhelm you. When you walk through the fire, you will not be scorched; the flames will not set you ablaze.', 'Isaiah 43:2'), ''))
G.append(('body', 'Help the Client Understand the Body’s Alarm', 'The alarm is stuck “on,” not broken.', ['Identify', 'Challenge'],
 'After trauma, the body’s alarm system can go off at reminders that are not dangerous: a smell, a sound, a tone of voice. Clients often believe these reactions mean they are in danger now or are “going crazy.”',
 ['Explain triggers and the fight-flight-freeze response in simple terms. Freezing during the trauma was the body’s automatic response, not a choice or a failure.',
  'Help the client identify personal triggers and early warning signs.',
  'Practice grounding and slow breathing in session so they can be used at home.',
  'Encourage regular sleep, exercise, and medical care; trauma often affects physical health.'],
 ['Your body learned to protect you. Right now it is ringing the alarm even when you’re safe. Let’s practice turning it down.'],
 None, ''))
G.append(('guilt', 'Address Guilt, Shame, and Moral Injury', 'Separate real guilt from false guilt.', ['Challenge', 'Replace'],
 'Many survivors carry guilt or shame. Some is false guilt (“I should have stopped it”). Some comes from having done, failed to prevent, or witnessed something that violates their own moral beliefs, called “moral injury,” common among first responders and veterans. Each needs a different response.',
 ['For false guilt, examine what the client knew and could do at the time; hindsight makes everything look clearer.',
  'For real wrongdoing, do not explain it away. Make room for confession, repentance, and God’s forgiveness, and for making amends where possible.',
  'Shame says “I am bad”; guilt says “I did something bad.” Help clients separate who they are from what happened.',
  'With the client’s permission, involve a pastor or chaplain when moral and spiritual questions are central.'],
 ['If your best friend had been in exactly your place, knowing only what you knew then, what would you say to him?'],
 ('Neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.', 'Romans 8:39'), ''))
G.append(('faith', 'Let Faith Be a Resource, Not a Pressure', 'Lament before explanation.', ['Replace'],
 'Faith can be a great source of strength after trauma: meaning, hope, community, and God’s presence. Trauma can also shake faith: “Where was God?” Clients should be free to bring their questions without being rushed to answers.',
 ['Ask how the trauma has affected the client’s faith, for better and for worse.',
  'Make room for lament. The Psalms show God’s people bringing fear, anger, and questions to Him.',
  'Be careful with verses about God bringing good out of evil (Genesis 50:20, Romans 8:28). They are true, but offered too early they can sound as if the suffering did not matter.',
  'Never suggest that trauma symptoms mean weak faith, or that prayer alone should be enough.'],
 ['How has what happened affected your relationship with God?'],
 ('You have taken account of my wanderings. Put my tears in Your bottle— are they not in Your book?', 'Psalm 56:8'), ''))
G.append(('self', 'Care for Yourself as the Counselor', 'Hearing trauma affects the helper.', ['All steps'],
 'Listening to trauma stories week after week can affect counselors too, through secondary traumatic stress and burnout. Caring for yourself protects your clients as well as you.',
 ['Notice your own signs: intrusive images, dread before sessions, numbness, irritability, poor sleep.',
  'Use regular supervision or consultation, especially with severe cases.',
  'Keep a balanced caseload when you can, and protect time for rest, worship, and relationships.',
  'If a client’s story touches your own history, get support, and refer if needed.'],
 [], ('Come to Me, all you who are weary and burdened, and I will give you rest.', 'Matthew 11:28'), ''))

AP = [("“You need to tell me everything that happened.”", "“You can share as much or as little as you want. We’ll go at your pace.”"),
      ("“At least you survived.”", "“You went through something terrible. I’m glad you’re here, and I want to understand what it’s been like.”"),
      ("“You should be over this by now.”", "“Healing from trauma takes time, and there are treatments that really help.”"),
      ("“God has a reason for everything.”", "“Many people ask where God was. Would you like to talk about that?”"),
      ("“Why didn’t you fight back?”", "“Your body did what it could to survive. Freezing is an automatic response, not a choice.”"),
      ("“Just stop thinking about it.”", "“Trying to push memories away often makes them stronger. Let’s find a better way to handle them.”")]

CHECK = ['Is the client safe now, and have I asked about suicide and substance use?',
         'Does the client have grounding skills before we go into the memories?',
         'Have I measured symptoms (for example, the PCL-5) so we can track progress?',
         'Am I trained in the trauma-focused method I’m using, or should I refer?',
         'Which trauma beliefs (stuck points) are keeping this going?',
         'Am I letting the client set the pace?',
         'Am I taking care of myself and using supervision?']

REFS = [
 'American Psychological Association. (2025). <em>Clinical practice guideline for the treatment of posttraumatic stress disorder (PTSD) in adults</em>. ' + link('https://www.apa.org/about/offices/directorates/guidelines/clinical-practice'),
 'Bonanno, G. A. (2004). Loss, trauma, and human resilience: Have we underestimated the human capacity to thrive after extremely aversive events? <em>American Psychologist, 59</em>(1), 20–28. ' + doi('10.1037/0003-066X.59.1.20'),
 'Department of Veterans Affairs &amp; Department of Defense. (2023). <em>VA/DoD clinical practice guideline for the management of posttraumatic stress disorder and acute stress disorder</em>. ' + link('https://www.healthquality.va.gov/guidelines/MH/ptsd/'),
 'Langberg, D. (2015). <em>Suffering and the heart of God: How trauma destroys and Christ restores</em>. New Growth Press.',
 'Litz, B. T., Stein, N., Delaney, E., Lebowitz, L., Nash, W. P., Silva, C., &amp; Maguen, S. (2009). Moral injury and moral repair in war veterans: A preliminary model and intervention strategy. <em>Clinical Psychology Review, 29</em>(8), 695–706. ' + doi('10.1016/j.cpr.2009.07.003'),
 'National Center for PTSD. PTSD Checklist for DSM-5 (PCL-5) and Primary Care PTSD Screen (PC-PTSD-5). ' + link('https://www.ptsd.va.gov/professional/assessment/', 'ptsd.va.gov/professional/assessment'),
 'Resick, P. A., Monson, C. M., &amp; Chard, K. M. (2017). <em>Cognitive processing therapy for PTSD: A comprehensive manual</em>. Guilford Press.',
 'Rose, S. C., Bisson, J., Churchill, R., &amp; Wessely, S. (2002). Psychological debriefing for preventing post traumatic stress disorder (PTSD). <em>Cochrane Database of Systematic Reviews</em>, Issue 2, Art. No. CD000560. ' + doi('10.1002/14651858.CD000560'),
]

page('counselors/guidelines-trauma.html', 'Trauma and PTSD', 'Counseling after frightening and overwhelming events',
 'Belief Counseling guidelines for trauma and PTSD: safety and stabilization, assessment, trauma-focused treatment, trauma beliefs, guilt and moral injury, and faith.',
 'These guidelines apply the general <a href="guidelines.html">Clinical Practice Guidelines</a> to counseling people after trauma: events that involved actual or threatened death, serious injury, or sexual violence, such as accidents, assaults, combat, disasters, and abuse. For abuse in particular, see also the <a href="guidelines-abuse.html">Abuse guidelines</a>.',
 'This is a practice framework, not a substitute for professional judgment, supervision, specialized trauma training, the law, licensing-board rules, informed consent, or your profession’s ethics code. If a client is at risk of suicide, call 911 or call or text 988.',
 'Safety first, then healing.', 'Trauma is very treatable. Our goal is to help the person feel safe, face what they have been avoiding, and replace the lies trauma taught them with the truth, at a pace they can manage.',
 G, AP, 'A Quick Check for Trauma Counseling', CHECK,
 'Trauma work requires specific training. Learn the PTSD criteria and the PCL-5 well, practice grounding skills yourself, and seek supervised training in at least one trauma-focused therapy (such as CPT or PE) before treating PTSD on your own. Notice how trauma stories affect you, and bring that to supervision.',
 '<a href="https://www.beliefcounselor.com/false-belief-finder" target="_top">Search all belief cards (Lie Finder)</a> · <a href="reviews/ptsd-teaching-overview.html">PTSD teaching overview</a> · <a href="guidelines-abuse.html">Abuse guidelines</a> · <a href="guidelines.html">General Clinical Practice Guidelines</a>',
 'He heals the brokenhearted<br>and binds up their wounds.', 'Psalm 147:3', REFS)
