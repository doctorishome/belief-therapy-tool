# Builds counselors/guidelines-abuse.html. Run from repo root: python3 tools/guidelines/build_abuse.py
import sys; sys.path.insert(0, 'tools/guidelines')
from common import page, belief_table, doi, link

P = 'psychological/'
BELIEFS = [
 ('What was done to me was my fault. I must have caused it.', 'Who made the choice to hurt you? Who is responsible for that choice?', P + 'Psych-061-What-Was-Done-to-Me-Was-My-Fault.html'),
 ('I should have fought harder or left sooner. Because I didn’t, I must have agreed to it.', 'Does freezing or staying out of fear mean you agreed? What made leaving or fighting so hard?', P + 'Psych-066-I-Should-Have-Fought-or-Left.html'),
 ('I’m damaged and ashamed, as if what was done to me made me worthless.', 'Can what someone else did change your worth to God?', P + 'Psych-062-Im-Damaged-and-Ashamed.html'),
 ('What happened makes me dirty or bad.', 'Whose sin was it? What does God say to those who were sinned against?', 'core/after-painful-experiences/Core-022-What-Happened-Makes-Me-Dirty-Or-Bad.html'),
 ('If I tell someone, they won’t believe me, or they will blame me.', 'Is there one safe person who might believe you? What would help you find out?', P + 'Psych-063-They-Wont-Believe-Me.html'),
 ('I have to keep this secret.', 'Who benefits from the secret? Who would be protected if it were told?', P + 'Psych-065-I-Have-to-Keep-This-Secret.html'),
 ('I have to keep them calm. If they get angry, it is my job to fix it.', 'Who is responsible for their anger? Has keeping them calm ever made you safe for long?', P + 'Psych-068-I-Have-to-Keep-Them-Calm.html'),
 ('I don’t get to decide what happens to my body.', 'What does Scripture say about your body and your worth? Who gave anyone the right to take that choice from you?', P + 'Psych-069-I-Dont-Get-to-Decide-About-My-Body.html'),
 ('Being submissive means accepting mistreatment or abuse.', 'Does any passage on submission tell anyone to accept abuse? How did Jesus treat women and the vulnerable?', 'Belief-096-Being-Submissive-Means-Accepting-Abuse.html'),
 ('Forgiving means I must trust them again.', 'Can you release the debt to God and still keep yourself safe?', 'Belief-038-Forgiving-Means-I-Must-Trust-Them-Again.html'),
]

HOT = ('<div class="hot"><h3>Keep these numbers at hand</h3><ul>'
       '<li><strong>Emergency:</strong> 911</li>'
       '<li><strong>988 Suicide &amp; Crisis Lifeline:</strong> call or text 988</li>'
       '<li><strong>National Domestic Violence Hotline:</strong> 1-800-799-7233 (thehotline.org)</li>'
       '<li><strong>RAINN National Sexual Assault Hotline:</strong> 1-800-656-4673 (rainn.org)</li>'
       '<li><strong>Childhelp National Child Abuse Hotline:</strong> 1-800-422-4453</li>'
       '<li><strong>Elder or vulnerable adult abuse:</strong> your state’s Adult Protective Services (eldercare.acl.gov or 1-800-677-1116 to find it)</li>'
       '</ul></div>')

G = []
G.append(('danger', 'Assess Current Danger First', 'Is the client safe tonight?', ['Identify'],
 'Before anything else, find out whether the abuse is still happening and how dangerous it is. Research on intimate partner homicide has identified warning signs, including the abuser’s access to a gun, earlier threats with a weapon, and the woman leaving or separating. Stalking, forced sex, and abuse during pregnancy also raised the risk.',
 ['Ask privately, never in front of a partner or family member who may be the abuser.',
  'Ask about weapons, threats to kill, choking or strangling, stalking, escalating violence, and whether the client is planning to leave.',
  'Help the client make a safety plan: safe places, important documents, money, a code word with a friend, and the hotline number.',
  'Remember that leaving can be the most dangerous time. Plan carefully, and connect the client with a domestic violence advocate.',
  'If a client is in immediate danger, help them call 911.'],
 ['Do you feel safe going home today? Has he ever threatened to kill you or used a weapon?'],
 ('The prudent see danger and take cover, but the simple keep going and suffer the consequences.', 'Proverbs 22:3'), ''))
G.append(('report', 'Know and Follow Your Duty to Report', 'The law protects the vulnerable.', ['All steps'],
 'Counselors in every state must report suspected abuse or neglect of a child, and in most states of an elder or dependent adult. In many states, clergy are mandated reporters too. Reporting is not a betrayal of the client; it is how the vulnerable are protected.',
 ['Learn your state’s reporting laws, including who must report, what must be reported, and how fast.',
  'Explain the limits of confidentiality at the first session, before anything is disclosed.',
  'Report suspicion; you do not need proof. Do not investigate or interview a child in detail yourself.',
  'Do not let church leaders, family members, or the abuser talk you out of reporting or handle it “internally.”',
  'Document what was said, in the client’s own words, and what you did.'],
 ['Before we start, I want you to know what stays private and the few things I am required by law to report.'],
 ('Open your mouth for those with no voice, for the cause of all the dispossessed.', 'Proverbs 31:8'), ''))
G.append(('disclosure', 'Respond Well When Abuse Is Disclosed', 'Believe, support, do not take control.', ['Identify'],
 'How people respond when a survivor tells them matters. A large review of research found that negative reactions, especially controlling the survivor, distracting them, or treating them differently, were linked to worse mental health. Many survivors have already been doubted or blamed.',
 ['Listen calmly. Thank the client for telling you.',
  'Say plainly that it was not their fault.',
  'Do not ask “why” questions that sound like blame: “Why didn’t you leave?” “Why were you there?”',
  'Do not take over. Offer choices about what happens next, except where you are legally required to report.',
  'Do not push for details the client is not ready to share.'],
 ['Thank you for telling me. What happened was not your fault. You decide what we do with this next.'],
 None, ''))
G.append(('couples', 'Do Not Do Couples Counseling While Abuse Is Ongoing', 'Abuse is not a communication problem.', ['All steps'],
 'Abuse is about one person’s pattern of power and control. Couples counseling can put the victim in danger (what they say in session may be punished at home) and suggests both partners share responsibility for the violence.',
 ['Screen each partner privately for abuse before starting couples or marriage counseling.',
  'If there is ongoing abuse, provide individual counseling and safety planning instead.',
  'Refer the abusive partner to a specialized batterer intervention program, not anger management alone.',
  'Never counsel a victim to submit more, try harder, or return to an unsafe home to save the marriage.'],
 [], ('The LORD tests the righteous and the wicked; His soul hates the lover of violence.', 'Psalm 11:5'), ''))
G.append(('blame', 'Place Responsibility Where It Belongs', 'Self-blame is the most common lie.', ['Identify', 'Challenge', 'Replace'],
 'Abuse often leaves the survivor believing it was their fault, that they are dirty or worthless, or that they must keep it secret. Abusers frequently teach these beliefs on purpose. Belief Counseling helps the survivor identify these lies, examine them, and replace them with the truth about responsibility, worth, and God’s heart for the oppressed.',
 ['Name clearly that the abuser is responsible for the abuse.',
  'Gently examine self-blame: what the survivor knew, what power they had, and what the abuser did to control them.',
  'Address shame directly. What was done to them does not define who they are.',
  'Use the matching belief cards as homework once a belief has been identified together.'],
 [], None, belief_table(BELIEFS)))
G.append(('choices', 'Respect the Survivor’s Choices and Pace', 'Restore the control abuse took away.', ['All steps'],
 'Abuse takes away choice. Healing gives it back. Adult survivors decide whether to leave, whether to press charges, and what to share, even when we wish they would choose differently (except where reporting is required by law).',
 ['Do not pressure an adult to leave, stay, report to police, or confront the abuser.',
  'Explain options and their likely consequences, and support the survivor’s decision.',
  'Understand why people stay: fear, money, children, faith, love, threats, isolation. Returning several times is common.',
  'Offer repeated, patient support. Each conversation can plant a seed.'],
 ['Whatever you decide, I’ll keep working with you. What feels most important to you right now?'],
 None, ''))
G.append(('trauma', 'Treat the Effects of Abuse With Proven Methods', 'Abuse is trauma; treat it as trauma.', ['Challenge', 'Replace'],
 'Survivors of abuse often develop PTSD, depression, anxiety, substance misuse, and relationship difficulties. Long-term childhood abuse can bring added problems with emotions, self-worth, and trust. Trauma-focused treatments work for many survivors.',
 ['Follow the <a href="guidelines-trauma.html">Trauma and PTSD guidelines</a>: safety, stabilization, assessment, and trauma-focused treatment.',
  'Expect trust to be built slowly. The counseling relationship itself can be a healing experience of safe authority.',
  'For children, use child-appropriate trauma treatment, such as trauma-focused CBT, and involve safe caregivers.',
  'Refer for specialized care when needed, and get supervision.'],
 [], ('He heals the brokenhearted and binds up their wounds.', 'Psalm 147:3'), ''))
G.append(('forgive', 'Never Pressure Forgiveness or Reconciliation', 'Forgiveness is not a return to danger.', ['Replace'],
 'Survivors are often told by family or church to “forgive and forget” and to restore the relationship. Forgiveness can be part of healing, but only in its own time, and it never requires trust, reconciliation, silence, or giving up legal protection.',
 ['Do not raise forgiveness early, and never make it a condition for healing.',
  'Separate forgiveness (releasing the debt to God) from reconciliation (which requires real repentance and changed behavior over time) and from trust (which must be earned).',
  'Affirm that a survivor can forgive and still report the crime, keep a protective order, and have no contact.',
  'Use the forgiveness belief cards when false beliefs about forgiveness come up.'],
 ['What have people told you about forgiving him? What does forgiveness mean to you?'],
 ('If it is possible on your part, live at peace with everyone.', 'Romans 12:18'), ''))
G.append(('spiritual', 'Recognize Spiritual Abuse and Misused Scripture', 'Scripture never excuses abuse.', ['Identify', 'Challenge', 'Replace'],
 'Some abusers use Scripture to control: “Wives submit,” “Children obey,” “You must forgive.” Some churches have protected abusers or blamed victims. This can wound a survivor’s faith deeply and make them afraid of God.',
 ['Ask whether Scripture or church leaders were used to keep the client silent or in danger.',
  'Help the client separate God from the people who misused His name.',
  'Read passages in context: the same chapters that call for submission call husbands to love sacrificially and parents not to provoke their children.',
  'Do not involve the client’s pastor or church without the client’s consent, and be aware that some church leaders are themselves mandated reporters.',
  'When appropriate, point to God’s care for the oppressed and Jesus’s protection of the vulnerable.'],
 ['When you think of God after all this, what do you picture? Does that picture fit how Jesus treated hurting people?'],
 ('Have no fellowship with the fruitless deeds of darkness, but rather expose them.', 'Ephesians 5:11'), ''))
G.append(('restore', 'Restore Dignity, Body, and Relationships', 'Abuse damages; God restores.', ['Replace'],
 'Recovery includes regaining a sense of worth, a healthy relationship with one’s own body and sexuality, and the ability to have safe, close relationships. For many Christian survivors, it also includes knowing God as safe.',
 ['Help survivors learn and practice boundaries; saying no is allowed.',
  'For survivors of sexual abuse, address shame about the body and sexuality gently; refer to a specialist when needed.',
  'Encourage connection with safe people and, when the survivor is ready, a supportive church or survivors’ group.',
  'Celebrate growth: speaking up, setting a limit, trusting a safe person.'],
 ['What would it look like to treat yourself the way God sees you?'],
 ('Do not be afraid, for you will not be put to shame; do not be intimidated, for you will not be humiliated.', 'Isaiah 54:4'), ''))

AP = [("“Why didn’t you just leave?”", "“Leaving can be very hard and even dangerous. What has made it hard for you?”"),
      ("“What were you doing to make him so angry?”", "“Nothing you did makes his violence your fault.”"),
      ("“Are you sure that’s what happened?”", "“Thank you for trusting me with this. I believe you.”"),
      ("“You need to forgive him and move on.”", "“Forgiveness can come in its own time. Right now, your safety matters most.”"),
      ("“God hates divorce, so you have to stay.”", "“God cares deeply about your safety. Let’s talk about what keeps you and your children safe.”"),
      ("“Let’s bring your husband in so we can work on this together.”", "“I’d like to keep meeting with you on your own for now.”"),
      ("“I’ll call the police right now.”" + " (for an adult, without asking)", "“Would you like help calling the police or a domestic violence advocate?”")]

CHECK = ['Is the client safe right now? Have I asked about weapons, threats, and strangulation?',
         'Is there a child, elder, or dependent adult I am required to report about?',
         'Did I respond to the disclosure with belief and support, without taking control?',
         'Am I avoiding couples counseling while abuse is ongoing?',
         'Am I placing responsibility on the abuser, not the survivor?',
         'Am I respecting the survivor’s choices and pace?',
         'Have I avoided pressuring forgiveness or reconciliation, or using Scripture to keep someone in danger?']

REFS = [
 'Campbell, J. C., Webster, D., Koziol-McLain, J., Block, C., Campbell, D., Curry, M. A., Gary, F., Glass, N., McFarlane, J., Sachs, C., Sharps, P., Ulrich, Y., Wilt, S. A., Manganello, J., Xu, X., Schollenberger, J., Frye, V., &amp; Laughon, K. (2003). Risk factors for femicide in abusive relationships: Results from a multisite case control study. <em>American Journal of Public Health, 93</em>(7), 1089–1097. ' + doi('10.2105/AJPH.93.7.1089'),
 'Child Welfare Information Gateway. State laws on mandatory reporting of child abuse and neglect. ' + link('https://www.childwelfare.gov/', 'childwelfare.gov'),
 'Dworkin, E. R., Brill, C. D., &amp; Ullman, S. E. (2019). Social reactions to disclosure of interpersonal violence and psychopathology: A systematic review and meta-analysis. <em>Clinical Psychology Review, 72</em>, 101750. ' + doi('10.1016/j.cpr.2019.101750'),
 'Herman, J. L. (2015). <em>Trauma and recovery: The aftermath of violence, from domestic abuse to political terror</em> (Rev. ed.). Basic Books.',
 'Langberg, D. (2020). <em>Redeeming power: Understanding authority and abuse in the church</em>. Brazos Press.',
 'National Domestic Violence Hotline. Safety planning resources. ' + link('https://www.thehotline.org/', 'thehotline.org'),
 'Tracy, S. R. (2005). <em>Mending the soul: Understanding and healing abuse</em>. Zondervan.',
]

page('counselors/guidelines-abuse.html', 'Abuse', 'Counseling survivors of physical and sexual abuse',
 'Belief Counseling guidelines for counseling survivors of physical and sexual abuse: danger assessment, mandatory reporting, disclosure, self-blame, forgiveness, and spiritual abuse.',
 'These guidelines apply the general <a href="guidelines.html">Clinical Practice Guidelines</a> to counseling people who have been physically or sexually abused, whether as children or adults, by a partner, family member, or anyone else. Abuse is a form of trauma, so the <a href="guidelines-trauma.html">Trauma and PTSD guidelines</a> apply as well.',
 'This is a practice framework, not a substitute for professional judgment, supervision, specialized training, the law, licensing-board rules, informed consent, or your profession’s ethics code. Reporting laws differ by state; know yours.',
 'Safety and truth, not silence.', 'Our goal is to protect the vulnerable, place responsibility where it belongs, and help survivors replace the lies abuse taught them with the truth of their worth to God.',
 G, AP, 'A Quick Check for Abuse Counseling', CHECK,
 'Learn your state’s mandatory reporting law before practicum begins, and know your site’s procedure. Practice responding to a disclosure out loud. Never screen couples for abuse together. Bring every abuse case to supervision, and notice how these stories affect you.',
 '<a href="https://www.beliefcounselor.com/false-belief-finder" target="_top">Search all belief cards (Lie Finder)</a> · <a href="guidelines-trauma.html">Trauma and PTSD guidelines</a> · <a href="guidelines.html">General Clinical Practice Guidelines</a>',
 'He has sent Me to proclaim liberty to the captives<br>… to release the oppressed.', 'Luke 4:18', REFS, top_extra=HOT)
