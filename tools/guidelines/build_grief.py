# Builds counselors/guidelines-grief.html (Grief and Loss guidelines) for the Counselors' Room.
# Reuses the head, styles and menu of counselors/guidelines.html so the pages match.
# Run from the repo root: python3 tools/guidelines/build_grief.py
import re

SRC = 'counselors/guidelines.html'
OUT = 'counselors/guidelines-grief.html'
src = open(SRC).read()
head = src[:src.index('<div class="hero"')]
head = re.sub(r'<title>.*?</title>', '<title>Grief and Loss Guidelines | Belief Counseling</title>', head, 1)
head = re.sub(r'<meta name="description" content="[^"]*">',
              '<meta name="description" content="Belief Counseling guidelines for grief counseling after the death of a loved one: assessment, prolonged grief, false beliefs about loss, lament, and Scripture used with care.">', head, 1)
assert 'class="l on" href="../counselors/guidelines.html">Guidelines' in head

EXTRA = """<style>
table.bt{width:100%;border-collapse:collapse;margin:12px 0;background:#fff;font-size:.97rem}
table.bt th{background:var(--navy);color:#fff;text-align:left;padding:9px 12px}
table.bt td{border:1px solid var(--line);padding:9px 12px;vertical-align:top}
table.bt td:first-child{font-weight:bold;color:#7a1f1f}
table.bt a{color:var(--navy);font-size:.9rem}
.crit{background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px 18px;margin:10px 0}
.crit ol{margin:4px 0 4px 4px}
.also{background:#eef1f6;border-radius:8px;padding:10px 16px;margin:16px 0;font-size:.97rem}
.also a{color:var(--navy);font-weight:bold}
@media(max-width:560px){table.bt{font-size:.9rem}table.bt td,table.bt th{padding:7px 8px}}
</style>"""
head = head.replace('</head>', EXTRA + '</head>', 1)

def say(t): return f'<p class="say">“{t}”</p>'
def scrip(text, ref): return f'<p class="scrip">“{text}” <b>({ref}, BSB)</b></p>'

CARD = '../belief-cards/interpersonal/grief-loss/'
G = []  # (id, title, glance, steps, why, practice, sayings, scripture, extra_html)
G.append(('normal', 'Treat Grief as Normal, Not as a Disorder', 'Most grief needs support, not treatment.', ['All steps'],
 'Grief is the natural response of love to loss. Research following people from before a spouse’s death to a year and a half after shows that most bereaved people are resilient: they hurt deeply, yet keep functioning and slowly recover. Grief also does not move through fixed “stages” in order; it comes in waves.',
 ['Tell clients that strong feelings, waves of sorrow, poor sleep, trouble concentrating, and even briefly sensing the loved one’s presence are common after a death.',
  'Do not push every grieving person into formal therapy. Routine counseling for ordinary grief has shown little benefit; targeted help for people who are struggling works much better.',
  'Do not tell a client which “stage” they should be in, or that they are grieving “wrong.”',
  'Expect hard days around anniversaries, birthdays, holidays, and first events without the loved one.'],
 ['There is no right way or right timetable to grieve. Tell me what it has been like for you.'],
 ('A time to weep and a time to laugh, a time to mourn and a time to dance.', 'Ecclesiastes 3:4'), ''))
G.append(('presence', 'Be Present Before You Counsel', 'Listen first; explain later.', ['Identify'],
 'In the early weeks, the most helpful thing a counselor can offer is steady, unhurried presence. Grieving people need their story heard, often more than once, before they can use advice or teaching.',
 ['Invite the client to tell the story of the person and of the death, in their own words and at their own pace.',
  'Ask about the person who died, not just about the death: who they were and what they meant.',
  'Allow silence and tears. You do not need to fill every pause.',
  'Avoid clichés (see “What to Say Instead” below). They usually comfort the speaker more than the listener.'],
 ['Would you tell me about him? What was he like?', 'What has been the hardest part since she died?'],
 ('Then they sat on the ground with him for seven days and seven nights, but no one spoke a word to him because they saw how intense his suffering was.', 'Job 2:13'), ''))
G.append(('risk', 'Assess Risk and Complications', 'Grief can hide depression, trauma, or risk.', ['Identify'],
 'Bereavement, especially after a suicide or other sudden or violent death, raises the risk of depression, substance misuse, health problems, and suicidal thoughts. A small but important group develops Prolonged Grief Disorder.',
 ['Ask directly about suicidal thoughts, including wishes to “be with” the person who died. In a crisis, call 911 or call or text 988.',
  'Ask about sleep, eating, alcohol and medication use, and physical health; encourage a medical checkup when needed.',
  'Watch for Major Depressive Disorder (pervasive low mood, worthlessness, loss of interest in everything) and for PTSD after a traumatic death (intrusive images of the death, nightmares, avoidance).',
  'Know the risk factors for prolonged grief: sudden or violent death, the death of a child, very close or dependent relationships, earlier losses or mental health problems, and little support.',
  'Do not diagnose Prolonged Grief Disorder before 12 months after the death in adults (6 months in children and adolescents).'],
 [], None,
 '<div class="crit"><p style="margin:6px 0"><strong>Prolonged Grief Disorder (DSM-5-TR), in brief:</strong> at least 12 months since the death (6 months for children and adolescents), and for at least the last month, nearly every day, <em>intense yearning</em> for the person or <em>preoccupation</em> with thoughts or memories of them, plus at least three of these:</p>'
 '<ol><li>Feeling that part of oneself has died (identity disruption)</li><li>Marked disbelief about the death</li><li>Avoiding reminders that the person is dead</li><li>Intense emotional pain (anger, bitterness, sorrow)</li><li>Difficulty moving on with life (friends, interests, plans)</li><li>Emotional numbness</li><li>Feeling that life is meaningless</li><li>Intense loneliness</li></ol>'
 '<p style="margin:6px 0">The grief must cause real distress or impairment and clearly exceed the person’s cultural and religious norms. The <strong>PG-13-Revised</strong> is a short, free questionnaire that matches these criteria. For the full teaching overview, see <a href="reviews/prolonged-grief-teaching-overview.html">Prolonged Grief Disorder</a> on the Disorders page.</p></div>'))
G.append(('treat', 'Use Targeted Methods for Prolonged Grief', 'Help them face the loss and rebuild.', ['Challenge', 'Replace'],
 'When grief is stuck, general supportive counseling is usually not enough. Grief-focused cognitive-behavioral approaches, such as Complicated Grief Treatment, have the strongest research support. They help the person accept the reality of the death and build a meaningful life again.',
 ['Gently help the client retell the story of the death and face painful reminders they have been avoiding (places, photos, belongings), one manageable step at a time.',
  'Identify and examine the beliefs that keep grief stuck (see the next guideline).',
  'Set restoration goals: small steps back into relationships, routines, interests, and purpose.',
  'Help the client keep a healthy bond with the person who died (memories, legacy, gratitude) while accepting that the person is gone.',
  'Refer for a medication evaluation when there is co-occurring depression; medication alone does not resolve prolonged grief.',
  'Get supervision or training before using grief-focused exposure methods, especially after traumatic deaths.'],
 ['What have you been avoiding since he died? What would be one small step toward it?'],
 ('He heals the brokenhearted and binds up their wounds.', 'Psalm 147:3'), ''))

BELIEFS = [
 ('“If I had done something different, they would still be alive.”', 'What did you know at the time? Are you judging yourself with information you only have now?', 'Inter-047-If-I-Had-Done-Something-Different-They-Would-Still-Be-Alive.html'),
 ('“Moving on means forgetting them.”', 'Can you go on living and still love and remember them? What would they want for you?', 'Inter-048-Moving-On-Means-Forgetting-Them.html'),
 ('“I’ll never get over losing them.”', 'Is the goal to “get over” them, or to carry the loss and still live a full life?', 'Inter-046-Ill-Never-Get-Over-Losing-Them.html'),
 ('“God took them from me to punish me.”', 'What does Scripture say about why people die? Does this fit what you know of God’s character in Christ?', 'Inter-049-God-Took-Them-From-Me-to-Punish-Me.html'),
 ('“Grieving shows a lack of faith.”', 'Jesus wept at Lazarus’s tomb. Did that show a lack of faith?', 'Inter-050-Grieving-Shows-a-Lack-of-Faith.html'),
 ('“My loved one died because I didn’t pray enough.”', 'Does Scripture teach that someone’s death depends on how much we prayed?', '../../Belief-080-My-Loved-One-Died-Because-I-Didnt-Pray-Enough.html'),
 ('“My loved one who died by suicide can never be with God.”', 'What does Scripture actually say about salvation, and who decides it?', '../../Belief-079-My-Loved-One-Who-Died-By-Suicide-Can-Never-Be-With-God.html'),
]
btable = ('<table class="bt"><tr><th>False belief</th><th>A question to examine it</th></tr>'
          + ''.join(f'<tr><td>{b}<br><a href="{CARD}{c}">Open the belief card →</a></td><td>{q}</td></tr>' for b, q, c in BELIEFS)
          + '</table>')
G.append(('beliefs', 'Identify the Beliefs That Keep Grief Stuck', 'Guilt and false beliefs drive prolonged grief.', ['Identify', 'Challenge', 'Replace'],
 'Research on grief-focused CBT shows that certain beliefs about the death, oneself, and the future keep grief from easing. These are exactly what Belief Counseling is designed to address: identify the belief, challenge it gently, and replace it with truth.',
 ['Listen for guilt (“I should have…”), self-blame, beliefs that moving on is disloyal, hopelessness about the future, and distorted beliefs about God.',
  'Separate real responsibility from false guilt. Where there is real wrongdoing, point to confession and forgiveness; where there is not, help the client see what they could and could not have known.',
  'Remember that some guilt reflects a realistic regret (a harsh last conversation). Regret can be grieved and forgiven; it does not need to be argued away.',
  'Use the site’s belief cards as homework once a belief has been identified together.'],
 [], None, btable))
G.append(('balance', 'Balance Facing the Loss and Rebuilding Life', 'Grieve, then rest; rest, then grieve.', ['Replace'],
 'Healthy grieving moves back and forth between two kinds of work: facing the loss (remembering, crying, visiting the grave) and rebuilding life (new routines, roles, and relationships). Taking breaks from grief is not denial; it is part of healthy coping.',
 ['Explain this back-and-forth so clients do not feel guilty on a good day or frightened on a hard one.',
  'Watch for clients stuck at one end: constantly immersed in grief, or avoiding it altogether through busyness, alcohol, or refusing to talk about the person.',
  'Help with practical changes the death has brought (finances, single parenting, living alone, new decisions).',
  'Encourage ways to keep a healthy connection with the loved one: telling their story, keeping meaningful items, honoring their values.'],
 ['What helps you remember her? And what has helped you get through the day?'],
 None, ''))
G.append(('lament', 'Make Room for Lament and Hard Questions', 'Honest prayer is biblical.', ['Challenge', 'Replace'],
 'Many grieving Christians feel angry at God, abandoned, or confused, and then feel guilty for feeling that way. Scripture gives us lament: honest, even raw, prayer that brings pain to God instead of hiding it. Some clients develop “complicated spiritual grief,” a painful break in their relationship with God after the loss.',
 ['Let clients voice anger, doubt, and questions without correcting them right away.',
  'Show that the Psalms model honest complaint to God; a client may find it helpful to write their own lament.',
  'Do not rush to explain why God allowed the death. Unanswered questions can be carried with God, not only answered.',
  'When appropriate, invite the client’s pastor or church community into support, with the client’s permission.'],
 ['Many people of deep faith have asked God “why?” Would it help to look at how the Psalms bring that question to Him?'],
 ('How long, O LORD? Will You forget me forever? How long will You hide Your face from me?', 'Psalm 13:1'), ''))
G.append(('hope', 'Offer Christian Hope Without Silencing Sorrow', 'Hope and tears belong together.', ['Replace'],
 'Christians do grieve, but not “like the rest, who are without hope.” Paul did not say not to grieve; he said to grieve with hope. Jesus Himself wept at Lazarus’s tomb, even knowing He would raise him. Hope in the resurrection is real comfort, but it should never be used to hurry a client past their pain.',
 ['Ask permission before sharing Scripture, and choose passages that comfort rather than correct.',
  'Do not tell a client their loved one is “in a better place” as a reason to stop being sad.',
  'Do not make pronouncements about the eternal destiny of the person who died. Point to God’s character and mercy, and refer theological questions to the client’s pastor when needed.',
  'Watch for theology that hurts: “God needed another angel,” “Everything happens for a reason,” or “Your faith should make this easier.” Gently examine these as beliefs.'],
 ['Jesus wept at His friend’s grave, even knowing what He was about to do. What does it mean to you that He grieved too?'],
 ('Brothers, we do not want you to be uninformed about those who sleep in death, so that you will not grieve like the rest, who are without hope.', '1 Thessalonians 4:13'), ''))
G.append(('differences', 'Respect Different Losses and Ways of Grieving', 'Every loss is different.', ['All steps'],
 'Grief is shaped by the relationship, the kind of death, the family, culture, and faith tradition. Some losses are not openly recognized by others, and these can be especially lonely.',
 ['Give special care to the death of a child, suicide loss, homicide, overdose, and sudden accidents; these carry higher risk of prolonged grief and trauma.',
  'Recognize losses others may overlook: miscarriage and stillbirth, the death of an ex-spouse, a friend, a pet, or someone the client had a difficult relationship with.',
  'Remember that grief over a hurtful or abusive person can be mixed with relief, anger, or guilt. All of these are allowed.',
  'Ask about family and cultural customs for mourning, and respect them.',
  'With children, use honest, age-appropriate words (“died,” not “went to sleep”), and involve parents or caregivers.'],
 ['Some people tell me they feel relief mixed in with their grief, and then feel guilty about it. Has anything like that been true for you?'],
 None, ''))
G.append(('support', 'Strengthen Support Around the Grieving Person', 'Grief is not meant to be carried alone.', ['Replace'],
 'Social support is one of the strongest protections in bereavement. Over time, the support that surrounded the funeral often fades, just when loneliness sets in.',
 ['Ask who the client can lean on, and who has pulled away.',
  'Encourage connection with family, friends, church, and, when appropriate, a grief support group.',
  'Help the client tell others what helps (“Please say his name. I like hearing it.”).',
  'Plan ahead for anniversaries and holidays: who will be with them, and how they want to remember the person.'],
 ['Who has been there for you since the funeral? Is there anyone you wish would reach out more?'],
 ('Who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves have received from God.', '2 Corinthians 1:4'), ''))

def section(i, g):
    gid, title, glance, steps, why, practice, sayings, sc, extra = g
    h = f'<div class="g" id="{gid}"><h2><span class="n">{i}</span>{title}</h2>'
    h += ''.join(f'<span class="step">{s}</span>' for s in steps)
    h += f'<p class="why">{why}</p><h3>In practice</h3><ul>' + ''.join(f'<li>{p}</li>' for p in practice) + '</ul>'
    h += extra
    if sayings:
        h += '<h3>Try saying</h3>' + ''.join(say(s) for s in sayings)
    if sc:
        h += scrip(*sc)
    h += '<p class="toplink"><a href="#top">Back to top ↑</a></p></div>'
    return h

glance = '<ol class="glance">' + ''.join(f'<li><a href="#{g[0]}">{g[1]}</a><span>{g[2]}</span></li>' for g in G) + '</ol>'

AP = [("“I know how you feel.”", "“I can’t know exactly what this is like for you, but I want to understand. Will you tell me?”"),
      ("“She’s in a better place, so you shouldn’t be so sad.”", "“You can trust she is with the Lord and still miss her terribly. Both can be true.”"),
      ("“Everything happens for a reason.”", "“I don’t understand why this happened either. I’m here with you in it.”"),
      ("“At least you had him for 40 years.”", "“Forty years together. That’s a lot of life to miss.”"),
      ("“God needed another angel.”", "“What has this loss made you wonder about God?”"),
      ("“It’s been a year; it’s time to move on.”", "“Grief doesn’t keep a calendar. What has this year been like?”"),
      ("“Be strong for the children.”", "“It’s all right for your children to see you grieve. It can teach them how.”")]
aptable = '<table class="ap"><tr><th>Avoid</th><th class="p">Try instead</th></tr>' + ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in AP) + '</table>'

CHECK = ['Have I listened to the story of the person and the death before offering anything?',
         'Have I asked about suicidal thoughts, substance use, and health?',
         'Is this ordinary grief that needs support, or prolonged grief, depression, or trauma that needs treatment?',
         'Which beliefs are making this grief heavier than it needs to be?',
         'Am I offering Scripture to comfort, or to hurry the client past their pain?',
         'Does the client have people around them, especially for the coming anniversaries and holidays?']

body = f"""<div class="hero" id="top"><div class="eyebrow">Belief Counseling · Clinical Practice Guidelines</div><h1>Grief and Loss</h1><p>Counseling after the death of a loved one</p><p style="font-size:.95rem;margin-top:10px">Dr. Brian Campbell</p></div>
<div class="gwrap">
<div class="back"><a href="guidelines.html">&larr; All Guidelines</a><button class="printbtn" onclick="window.print()">Print these guidelines</button></div>
<p>These guidelines apply the general <a href="guidelines.html">Clinical Practice Guidelines</a> to counseling people after the death of someone they love. They draw on bereavement research and grief-focused cognitive-behavioral treatment, with guidance for integrating Christian faith when the client wants it.</p>
<p class="scope"><strong>Please note:</strong> This is a practice framework, not a substitute for professional judgment, supervision, the law, licensing-board rules, informed consent, or your profession’s ethics code. If a client is at risk of suicide, call 911 or call or text 988.</p>

<div class="core"><div class="k">The central principle</div><div class="big">Grief is the price of love.</div><p>Our goal is not to make grief go away. It is to help the person carry the loss, release false beliefs that make it heavier, and live again with hope, while still loving the one who died.</p></div>

<h2>The Guidelines at a Glance</h2>
<p class="small">Click any guideline to jump to it. The tags (Identify, Challenge, Replace) show where each one matters most in the Belief Counseling process.</p>
{glance}
{''.join(section(i + 1, g) for i, g in enumerate(G))}

<h2 id="phrases">Common Missteps: What to Say Instead</h2>
{aptable}

<div class="check" id="check"><h3 style="margin-top:0">A Quick Check for Grief Counseling</h3>
<ul>{''.join(f'<li>{c}</li>' for c in CHECK)}</ul></div>

<div class="stud"><h3 style="margin-top:0">For Students</h3>
<p style="margin:4px 0">Before counseling grieving clients, reflect on your own losses and how they may affect what you say. Practice the “Try instead” lines out loud, and learn the Prolonged Grief Disorder criteria well enough to tell ordinary grief from grief that needs treatment. Bring grief cases involving suicide, a child’s death, or traumatic loss to supervision.</p></div>

<div class="also">Related: <a href="{CARD}index.html">Grief and Loss belief cards and homework</a> · <a href="reviews/prolonged-grief-teaching-overview.html">Prolonged Grief Disorder teaching overview</a> · <a href="guidelines.html">General Clinical Practice Guidelines</a></div>

<p class="motto">Blessed are those who mourn,<br>for they will be comforted.</p>
<p style="text-align:center;margin:0 0 20px;color:var(--mut)">Matthew 5:4 (BSB)</p>

<h2 id="reading">References and Further Reading</h2>
<ul class="refs">
<li>American Psychiatric Association. (2022). <em>Diagnostic and statistical manual of mental disorders</em> (5th ed., text rev.). Prolonged Grief Disorder.</li>
<li>Boelen, P. A., de Keijser, J., van den Hout, M. A., &amp; van den Bout, J. (2007). Treatment of complicated grief: A comparison between cognitive-behavioral therapy and supportive counseling. <em>Journal of Consulting and Clinical Psychology, 75</em>(2), 277–284. <a href="https://doi.org/10.1037/0022-006X.75.2.277" target="_blank" rel="noopener">https://doi.org/10.1037/0022-006X.75.2.277</a></li>
<li>Bonanno, G. A., Wortman, C. B., Lehman, D. R., Tweed, R. G., Haring, M., Sonnega, J., Carr, D., &amp; Nesse, R. M. (2002). Resilience to loss and chronic grief: A prospective study from preloss to 18-months postloss. <em>Journal of Personality and Social Psychology, 83</em>(5), 1150–1164. <a href="https://doi.org/10.1037/0022-3514.83.5.1150" target="_blank" rel="noopener">https://doi.org/10.1037/0022-3514.83.5.1150</a></li>
<li>Currier, J. M., Neimeyer, R. A., &amp; Berman, J. S. (2008). The effectiveness of psychotherapeutic interventions for bereaved persons: A comprehensive quantitative review. <em>Psychological Bulletin, 134</em>(5), 648–661. <a href="https://doi.org/10.1037/0033-2909.134.5.648" target="_blank" rel="noopener">https://doi.org/10.1037/0033-2909.134.5.648</a></li>
<li>Prigerson, H. G., Boelen, P. A., Xu, J., Smith, K. V., &amp; Maciejewski, P. K. (2021). Validation of the new DSM-5-TR criteria for prolonged grief disorder and the PG-13-Revised (PG-13-R) scale. <em>World Psychiatry, 20</em>(1), 96–106. <a href="https://doi.org/10.1002/wps.20823" target="_blank" rel="noopener">https://doi.org/10.1002/wps.20823</a></li>
<li>Shear, M. K., Reynolds, C. F., Simon, N. M., Zisook, S., Wang, Y., Mauro, C., Duan, N., Lebowitz, B., &amp; Skritskaya, N. (2016). Optimizing treatment of complicated grief: A randomized clinical trial. <em>JAMA Psychiatry, 73</em>(7), 685–694. <a href="https://doi.org/10.1001/jamapsychiatry.2016.0892" target="_blank" rel="noopener">https://doi.org/10.1001/jamapsychiatry.2016.0892</a></li>
<li>Stroebe, M., &amp; Schut, H. (1999). The dual process model of coping with bereavement: Rationale and description. <em>Death Studies, 23</em>(3), 197–224. <a href="https://doi.org/10.1080/074811899201046" target="_blank" rel="noopener">https://doi.org/10.1080/074811899201046</a></li>
<li>Wortmann, J. H., &amp; Park, C. L. (2008). Religion and spirituality in adjustment following bereavement: An integrative review. <em>Death Studies, 32</em>(8), 703–736. <a href="https://doi.org/10.1080/07481180802289507" target="_blank" rel="noopener">https://doi.org/10.1080/07481180802289507</a></li>
</ul>
<p class="small">Scripture quotations are from the Berean Standard Bible.</p>
<p class="small">© 2026 Brian Campbell, Ph.D. All rights reserved.</p>
</div>
<div class="foot">Educational training for counselors. Never enter real client names or details. · © Brian Campbell, Ph.D. · <a href="https://www.beliefcounselor.com/help" target="_top">Help &amp; Support</a></div>
</body></html>"""

open(OUT, 'w').write(head + body)
print('ok', OUT)
