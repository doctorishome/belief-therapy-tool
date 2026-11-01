import json, pathlib
TITLE = 'Delusional Disorder (DSM-5-TR): Teaching Overview'
FILE = 'delusional-disorder-teaching-overview'
VERIFIED = 'Sunday, Nov 1, 2026'
SOURCES = 'Crossref, OpenAlex, and PubMed/Europe PMC records'

_REUSED = json.loads((pathlib.Path(__file__).parent / 'reused_refs.json').read_text())
_NEW = [
 ('Freeman, D., Dunn, G., Startup, H., Pugh, K., Cordwell, J., Mander, H., Černis, E., Wingham, G., Shirvell, K., & Kingdon, D. (2015). Effects of cognitive behaviour therapy for worry on persecutory delusions in patients with psychosis (WIT): A parallel, single-blind, randomised controlled trial with a mediation analysis. *The Lancet Psychiatry, 2*(4), 305–313.', '10.1016/S2215-0366(15)00039-5'),
 ('Freeman, D., Emsley, R., Diamond, R., Collett, N., Bold, E., Chadwick, E., Isham, L., Bird, J. C., Edwards, D., Kingdon, D., Fitzpatrick, R., Kabir, T., Waite, F., Carr, L., Causier, C., Černis, E., Kirkham, M., Lambe, S., Lister, R., . . . Twivy, E. (2021). Comparison of a theoretically driven cognitive therapy (the Feeling Safe Programme) with befriending for the treatment of persistent persecutory delusions: A parallel, single-blind, randomised controlled trial. *The Lancet Psychiatry, 8*(8), 696–707.', '10.1016/S2215-0366(21)00158-9'),
 ('Marneros, A., Pillmann, F., & Wustmann, T. (2012). Delusional disorders—are they simply paranoid schizophrenia? *Schizophrenia Bulletin, 38*(3), 561–568.', '10.1093/schbul/sbq125'),
 ('Muñoz-Negro, J. E., & Cervilla, J. A. (2016). A systematic review on the pharmacological treatment of delusional disorder. *Journal of Clinical Psychopharmacology, 36*(6), 684–690.', '10.1097/JCP.0000000000000595'),
 ('O’Connor, K., Stip, E., Pélissier, M.-C., Aardema, F., Guay, S., Gaudette, G., Van Haaster, I., Robillard, S., Grenier, S., Careau, Y., Doucet, P., & Leblanc, V. (2007). Treating delusional disorder: A comparison of cognitive-behavioural therapy and attention placebo control. *The Canadian Journal of Psychiatry, 52*(3), 182–190.', '10.1177/070674370705200310'),
 ('Perälä, J., Suvisaari, J., Saarni, S. I., Kuoppasalmi, K., Isometsä, E., Pirkola, S., Partonen, T., Tuulio-Henriksson, A., Hintikka, J., Kieseppä, T., Härkänen, T., Koskinen, S., & Lönnqvist, J. (2007). Lifetime prevalence of psychotic and bipolar I disorders in a general population. *Archives of General Psychiatry, 64*(1), 19–28.', '10.1001/archpsyc.64.1.19'),
 ('Skelton, M., Khokhar, W. A., & Thacker, S. P. (2015). Treatments for delusional disorder. *Cochrane Database of Systematic Reviews, 2015*(5), CD009785.', '10.1002/14651858.CD009785.pub2'),
]
RAW_REFS = sorted([tuple(r) for r in _REUSED] + _NEW, key=lambda r: r[0].replace('O’', 'O').lower())

BODY = [
('H', '1. What it is'),
('P', 'Delusional disorder is the presence of one or more **delusions** (fixed false beliefs that are not changed by clear evidence) lasting **at least 1 month**, in a person who has never met the full criteria for schizophrenia. Apart from the delusion and its effects, the person often functions fairly well and does not seem obviously odd (American Psychiatric Association [APA], 2022). It is listed in DSM-5-TR’s schizophrenia spectrum chapter.'),
('P', '**How common:** in a nationally representative Finnish sample of 8,028 adults aged 30 and older, lifetime prevalence was 0.18%, compared with 0.87% for schizophrenia (Perälä et al., 2007).'),
('P', '**Not simply mild schizophrenia.** Followed for about 11 years, inpatients with delusional disorder had a later onset, no first-rank or significant negative symptoms, fewer and shorter hospital stays, and better outcomes in work, relationships, and self-sufficiency than patients with paranoid schizophrenia. The diagnosis was very stable and only rarely turned into schizophrenia (Marneros et al., 2012).'),
('P', '**Counselor framing:** most people with delusional disorder do not think they are ill. They come because of the consequences: conflict with neighbors, a broken marriage, lawsuits, repeated medical visits, or pressure from family. The belief feels like plain fact to them, so arguing about it usually backfires.'),
('H', '2. Core symptoms to watch for'),
('P', 'DSM-5-TR criteria, paraphrased (APA, 2022); use the manual itself for formal diagnosis.'),
('B', 'One or more **delusions** lasting **1 month or longer**.'),
('B', 'The person has **never met Criterion A for schizophrenia**. Hallucinations, if present, are not prominent and fit the delusional theme (for example, sensing insects in the skin with a delusion of infestation).'),
('B', 'Apart from the delusion, **functioning is not markedly impaired** and behavior is not obviously bizarre.'),
('B', 'Any mood episodes have been **brief** compared with the delusional periods, and the condition is not due to a substance, a medical condition, or another mental disorder such as body dysmorphic disorder or OCD.'),
('B', '**Types:** **persecutory** (being conspired against, spied on, poisoned, harassed; the most common type), **jealous** (partner is unfaithful), **erotomanic** (another person, often of higher status, is in love with them), **grandiose** (great talent, insight, or a special identity or mission), **somatic** (bodily functions or sensations, such as infestation or a foul odor), **mixed**, and **unspecified**. A specifier notes **bizarre content** (clearly implausible, such as organs replaced without a scar).'),
('P', '**Rule out:** schizophrenia and other psychotic disorders; depression or bipolar disorder with psychotic features; OCD or body dysmorphic disorder with absent insight; substance use (especially stimulants and cannabis); and medical or neurological causes, including **dementia in older adults**. Paranoid personality disorder involves suspicion, not a fixed delusion. Beliefs shared by the person’s religious or cultural community are **not** delusions (APA, 2022).'),
('P', '**Safety (general clinical consensus):** ask about plans to confront, follow, or harm the supposed persecutor, partner, or object of love. **Jealous and persecutory types carry a real risk of violence**, and erotomanic types of stalking. Follow duty-to-warn laws, assess suicide risk, and refer for psychiatric evaluation in every case.'),
('H', '3. What works: treatment and the evidence'),
('P', '**Bottom line for class:** trial evidence specific to delusional disorder is very thin. Antipsychotic medication helps some patients, and cognitive therapy developed for persecutory delusions in psychosis is the most promising psychological approach. Engagement comes first.'),
('P', '**Evidence overview (honest effect sizes):**'),
('B', '**Cochrane review:** of 141 citations, only **one small trial** (17 completers) qualified: CBT versus supportive therapy. It showed a benefit on social self-esteem, but the evidence was very low quality. The reviewers concluded there was not enough evidence for firm recommendations and that offering treatments proven for other psychotic disorders is reasonable (Skelton et al., 2015).'),
('B', '**CBT trial:** in 24 people with delusional disorder randomized to 24 weeks of CBT or an attention-control therapy, both groups improved, but CBT had more effect on the emotion linked to the belief and on how the belief drove actions (O’Connor et al., 2007).'),
('B', '**Cognitive therapy for persecutory delusions (mixed psychosis samples):** in 130 adults with persistent persecutory delusions, the **Feeling Safe Programme** reduced delusional conviction (d = −0.86) and delusion severity (d = −1.20) at 6 months more than befriending (Freeman et al., 2021). In 150 patients, just six sessions of CBT targeting **worry** reduced persecutory delusions, and reduced worry accounted for about 66% of the change (Freeman et al., 2015).'),
('B', '**Medication (referral notes):** a review of 385 published cases (no randomized trials) found that about one-third of patients responded well to antipsychotics, somewhat more often with older (first-generation) drugs (39%) than newer ones (28%) (Muñoz-Negro & Cervilla, 2016). Getting a suspicious patient to accept medication is often the main obstacle.'),
('P', '**Cognitive work with delusional disorder: how it is used** (Garety et al., 2001; Freeman et al., 2021):'),
('B', '**Engage around the person’s own goals:** "You’ve been under terrible strain. Let’s work on sleep, stress, and getting your life back." Do not argue about the belief or pretend to agree with it.'),
('B', '**Reduce what keeps the belief going:** worry, poor sleep, low self-esteem, avoidance, and safety behaviors such as constant checking or hiding, which prevent the person from learning that they are safe.'),
('B', '**Gently examine the evidence:** consider other explanations, notice "jumping to conclusions," and run small behavioral experiments ("What happens if you go to the store without checking for followers?").'),
('H', '4. Religion, spirituality, and Christian integration: what the evidence shows'),
('P', '**Disorder-specific research.** We found **no study of religion or faith-integrated treatment specifically in delusional disorder** (literature search, November 1, 2026). The findings below come from broader samples of people with psychosis.'),
('P', '**Religious delusions.** They appeared in 24% of 193 inpatients, who were more severely ill than patients with other delusions (Siddle et al., 2002). Rates vary by time, place, and probably personal religiosity (Cook, 2015). A second study found them no more severe, but these patients adhered less to treatment and got less support from their faith communities (Mohr et al., 2010).'),
('P', '**Spiritual experience versus delusion.** Members of new religious movements endorsed as many unusual beliefs as deluded inpatients but were far less distressed and preoccupied; Christian and nonreligious controls did not differ (Peters et al., 1999). Weigh conviction, preoccupation, distress, and whether the person’s faith community shares the belief, not the content alone (Pierre, 2001).'),
('P', '**Faith as help or hindrance.** Among 115 outpatients with psychosis, religion gave hope and meaning for 71% but spiritual despair for 14% (Mohr et al., 2006). Nonadherent patients more often saw a conflict between their religion and medication: 31% versus 8% of adherent patients (Borras et al., 2007). In 47 patients with psychosis, spiritual struggle was linked to more suicidal ideation (Rosmarin et al., 2013).'),
('P', '**Clergy.** One-quarter of U.S. adults who ever sought help for a mental disorder went to clergy, and most of those seeing clergy saw no other professional (Wang et al., 2003). Pastors may be the first to hear a delusion.'),
('P', '**Honest summary for teaching:**'),
('N', 'Medication and cognitive therapy for persecutory delusions are the best available evidence. Faith integration supports them; it does not replace them.'),
('N', 'No faith-integrated trial exists for delusional disorder. Ordinary faith is not a symptom; judge beliefs by their fixity, distress, and whether the person’s own church shares them.'),
('N', 'A respected pastor or faith community can help engage a suspicious person in care, or can unintentionally confirm the delusion. Work together carefully.'),
('H', '5. Practical Christian-integration notes'),
('P', 'These apply Dr. Campbell’s identify, challenge, replace-with-Scripture method gently, within psychiatric and cognitive care. Clinical items rest on the research above. Pastoral items are theological application, not research findings.'),
('B', '**Identify (clinical).** Listen for the delusion and the fears beneath it, including spiritual forms: "My neighbors are working with the devil against me," "God told me my wife is unfaithful," "I have a special mission no one else understands." Notice the distress, isolation, and loss the belief has caused (Mohr et al., 2010).'),
('B', '**Challenge (clinical).** Do not debate the delusion head-on. Focus on distress, safety, sleep, and worry, and gently test predictions and consider other explanations over time (Freeman et al., 2021). Ask whether the person’s church or Scripture actually teaches what they believe (Pierre, 2001).'),
('B', '**Replace (pastoral).** Offer Scripture that steadies fear and honors careful testing of beliefs:'),
('B2', '“He who dwells in the shelter of the Most High will rest in the shadow of the Almighty. I will say to the LORD, ‘You are my refuge and my fortress, my God, in whom I trust.’” (Psalm 91:1–2). Safety rooted in God, not in constant vigilance.'),
('B2', '“There is no fear in love, but perfect love drives out fear…” (1 John 4:18)'),
('B2', '“The first to state his case seems right until another comes and cross-examines him.” (Proverbs 18:17). Considering other explanations is wise, not disloyal.'),
('B2', '“Be anxious for nothing, but in everything, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.” (Philippians 4:6–7). For the worry that feeds persecutory fears.'),
('B', '**Faith community (clinical).** Offer calm, consistent friendship without confirming or ridiculing the belief. Protect anyone the person believes is a persecutor or secret lover, and do not carry messages between them.'),
('B', '**Ministers:** avoid interpreting the belief as demonic attack or special revelation, encourage evaluation as care for the whole person, take any threat seriously, and refer promptly.'),
('H', '6. Quick classroom takeaways'),
('B', 'Delusional disorder means one or more fixed false beliefs for at least 1 month without schizophrenia, with fairly preserved functioning. Types: persecutory, jealous, erotomanic, grandiose, somatic, mixed. Assess violence and suicide risk.'),
('B', 'Evidence is thin: antipsychotics help about one-third; cognitive therapy targeting worry, sleep, and safety behaviors reduces persecutory delusions. Engage first; never argue.'),
('B', 'Replace fear with the security of God’s love, and gently weigh beliefs as "another comes and cross-examines."'),
]

from instruments import add_assessment
BODY = add_assessment(BODY, ['APA_PSY', 'PSYRATS', 'PDI', 'BABS', 'GPTS', 'BPRS', 'PANSS', 'CSSRS'], about='delusional disorder',
                      use={'GPTS': 'Measuring persecutory ideas and ideas of reference.'},
                      takeaway='Rate the belief’s conviction, preoccupation, and distress with the PSYRATS or PDI, and its fixity with the BABS; track change over time rather than arguing about content.')

from dispute import add_dispute
BODY = add_dispute(BODY, 'delusional')

from treatment_links import link_treatments
from treatment_pairs import PAIRS
BODY = link_treatments(BODY, PAIRS['delusional'])
