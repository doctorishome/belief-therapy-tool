"""Shared library of assessment instruments for the DSM-5-TR teaching reviews.

Every link and purchase/qualification level here was checked on the publisher's or
distributor's site, or (for "Original article" links) the DOI was checked on Crossref (Nov 1, 2026).

Use from a review's content.py:
    from instruments import add_assessment
    BODY = add_assessment(BODY, ['PHQ9', 'CSSRS', ...], about='depression', use={'PHQ9': 'custom text'})
add_assessment inserts "3. Frequently used assessment instruments" after section 2 and renumbers
the later numbered headings.
"""
import re

PEARSON_Q = 'https://www.pearsonassessments.com/professional-assessments/ordering/how-to-order/qualifications/qualifications-policy.html'
APA = 'https://www.psychiatry.org/psychiatrists/practice/dsm/educational-resources/assessment-measures'
FREE_GEN = 'None beyond general clinical training'


def doi(d):
    return f'[Original article](https://doi.org/{d})'


# key: (name, best used for, format, purchase, training, where)
I = {
 # --- broad / cross-cutting ---
 'PHQ9': ('**PHQ-9** (Patient Health Questionnaire-9)', 'Screening and tracking depression; item 9 screens for suicidal thoughts.', 'Self-report, 9 items, about 2 minutes', 'No (free)', FREE_GEN, '[PHQ Screeners site](https://www.phqscreeners.com/)'),
 'GAD7': ('**GAD-7** (Generalized Anxiety Disorder-7)', 'Screening and tracking generalized anxiety.', 'Self-report, 7 items, about 2 minutes', 'No (free)', FREE_GEN, '[PHQ Screeners site](https://www.phqscreeners.com/)'),
 'PHQ15': ('**PHQ-15** (Patient Health Questionnaire-15)', 'Physical symptom burden; also an APA DSM-5 Level 2 measure.', 'Self-report, 15 items', 'No (free)', FREE_GEN, '[PHQ Screeners site](https://www.phqscreeners.com/)'),
 'CSSRS': ('**C-SSRS** (Columbia Suicide Severity Rating Scale)', 'Screening and assessing suicide risk; brief screener and full versions.', 'Clinician- or staff-asked questions, a few minutes', 'No (free)', 'Free online training offered and recommended', '[Columbia Lighthouse Project](https://cssrs.columbia.edu/)'),
 'BHS': ('**BHS** (Beck Hopelessness Scale)', 'Hopelessness, a strong warning sign for suicide; ages 17 to 80.', 'Self-report, 20 true/false items', 'Yes', '★ Level B', '[Pearson](https://www.pearsonassessments.com/store/usd/p/100000105)'),
 'BDI2': ('**BDI-II** (Beck Depression Inventory-II)', 'Measuring depression severity in teens and adults.', 'Self-report, 21 items, 5 to 10 minutes', 'Yes', '★ Level B', '[Pearson](https://www.pearsonassessments.com/store/usd/p/100000159)'),
 'MMPI3': ('**MMPI-3** (Minnesota Multiphasic Personality Inventory-3)', 'Broad personality and psychopathology assessment, with validity scales for over- and under-reporting.', 'Self-report, 335 true/false items, about 25 to 50 minutes', 'Yes', '★ Level C', '[Pearson](https://www.pearsonassessments.com/store/usd/p/P100000004)'),
 'MCMI4': ('**MCMI-IV** (Millon Clinical Multiaxial Inventory-IV)', 'Adults in treatment; personality patterns alongside clinical syndromes.', 'Self-report, 195 true/false items, about 25 to 30 minutes', 'Yes', '★ Level C', '[Pearson](https://www.pearsonassessments.com/store/usd/p/100001362)'),
 'PAI': ('**PAI** (Personality Assessment Inventory)', 'Broad clinical and personality assessment for adults, including scales for borderline and antisocial features.', 'Self-report, 344 items, about 50 to 60 minutes', 'Yes', '★ Level C', '[PAR](https://www.parinc.com/product/groups/pai)'),
 'PID5': ('**PID-5** (Personality Inventory for DSM-5)', 'Dimensional personality trait profile (negative affect, detachment, antagonism, disinhibition, psychoticism); brief and informant forms.', 'Self-report; 220-item full or 25-item brief form', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'SCIDPD': ('**SCID-5-PD** (Structured Clinical Interview for DSM-5 Personality Disorders)', 'Diagnosing all ten DSM-5 personality disorders, with an optional self-report screener.', 'Semistructured clinician interview', 'Yes', '★ Clinical interviewing skill; training recommended', '[APA Publishing](https://appi.org/Products/Interviewing/Structured-Clinical-Interview-for-DSM-5-Personalit)'),
 'WHODAS': ('**WHODAS 2.0** (WHO Disability Assessment Schedule)', 'How much symptoms interfere with daily life and functioning.', 'Self- or proxy-report, 36 items', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'K10': ('**K10** (Kessler Psychological Distress Scale)', 'General psychological distress; quick screen in any setting.', 'Self-report, 10 items', 'No (free)', FREE_GEN, doi('10.1017/S0033291702006074')),
 'PSS': ('**PSS** (Perceived Stress Scale)', 'How stressful and overwhelming life feels.', 'Self-report, 10 or 14 items', 'No (free for non-commercial use)', FREE_GEN, doi('10.2307/2136404')),
 # --- anxiety ---
 'APA_ANX': ('**APA DSM-5 anxiety severity measures**', 'Separate brief scales for panic, social anxiety, specific phobia, agoraphobia, separation anxiety, and generalized anxiety (adult and age 11 to 17 versions).', 'Self-report, 10 items each', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'BAI': ('**BAI** (Beck Anxiety Inventory)', 'Anxiety severity, especially physical symptoms; ages 17 to 80.', 'Self-report, 21 items, 5 to 10 minutes', 'Yes', '★ Level B', '[Pearson](https://www.pearsonassessments.com/store/usd/p/100000251)'),
 'PSWQ': ('**PSWQ** (Penn State Worry Questionnaire)', 'Severity of chronic, hard-to-control worry (generalized anxiety).', 'Self-report, 16 items', 'No (free)', FREE_GEN, doi('10.1016/0005-7967(90)90135-6')),
 'STAI': ('**STAI** (State-Trait Anxiety Inventory)', 'Separates current (state) anxiety from long-standing (trait) anxiety.', 'Self-report, 40 items', 'Yes (license per use)', 'No special level listed by the publisher', '[Mind Garden](https://mindgarden.com/state-trait-anxiety-inventory-for-adults/29-staiad-manual.html)'),
 'SCARED': ('**SCARED** (Screen for Child Anxiety Related Disorders)', 'Children and teens; screens panic, generalized, separation, social, and school anxiety.', 'Child and parent forms, 41 items', 'No (free)', FREE_GEN, '[University of Pittsburgh (PDF)](https://pediatricbipolar.pitt.edu/sites/default/files/assets/SCAREDChildVersion_1.19.18.pdf)'),
 'MASC2': ('**MASC 2** (Multidimensional Anxiety Scale for Children, 2nd ed.)', 'Children and teens ages 8 to 19; self and parent forms.', 'Self- and parent-report, 50 items', 'Yes', '★ Level B', '[MHS](https://storefront.mhs.com/collections/masc-2)'),
 # --- OCD ---
 'YBOCS': ('**Y-BOCS** (Yale-Brown Obsessive Compulsive Scale)', 'The standard measure of OCD severity, with a symptom checklist.', 'Clinician interview, 10 severity items', 'No (free)', '★ Clinical interviewing skill; training recommended', doi('10.1001/archpsyc.1989.01810110048007')),
 'CYBOCS': ('**CY-BOCS** (Children’s Yale-Brown Obsessive Compulsive Scale)', 'OCD severity in children and teens.', 'Clinician interview with child and parent', 'No (free)', '★ Clinical interviewing skill; training recommended', doi('10.1097/00004583-199706000-00023')),
 'OCIR': ('**OCI-R** (Obsessive-Compulsive Inventory-Revised)', 'Quick self-report of OCD symptom types (washing, checking, ordering, obsessing, hoarding, neutralizing).', 'Self-report, 18 items', 'No (free)', FREE_GEN, doi('10.1037/1040-3590.14.4.485')),
 'DOCS': ('**DOCS** (Dimensional Obsessive-Compulsive Scale)', 'Severity across four OCD themes, including unacceptable (taboo, religious) thoughts.', 'Self-report, 20 items', 'No (free)', FREE_GEN, '[DOCS website (UNC)](https://docs.web.unc.edu)'),
 'PIOS': ('**PIOS** (Penn Inventory of Scrupulosity)', 'Religious and moral obsessions (scrupulosity), such as fear of sin and of God’s punishment.', 'Self-report, 19 items (revised version 15)', 'No (free)', FREE_GEN, doi('10.1016/S0005-7967(01)00070-5')),
 'FOCI': ('**APA Level 2 Repetitive Thoughts and Behaviors** (adapted from FOCI)', 'Brief follow-up when obsessive or repetitive symptoms are suspected.', 'Self-report, 5 items', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 # --- trauma / grief ---
 'PCPTSD5': ('**PC-PTSD-5** (Primary Care PTSD Screen)', 'Quick screen for probable PTSD.', 'Self-report, 5 items', 'No (free)', FREE_GEN, '[National Center for PTSD](https://www.ptsd.va.gov/professional/assessment/screens/pc-ptsd.asp)'),
 'LEC5': ('**LEC-5** (Life Events Checklist)', 'Which potentially traumatic events a person has experienced.', 'Self-report, 17 items', 'No (free)', FREE_GEN, '[National Center for PTSD](https://www.ptsd.va.gov/professional/assessment/te-measures/life_events_checklist.asp)'),
 'PCL5': ('**PCL-5** (PTSD Checklist for DSM-5)', 'Measuring and tracking the 20 DSM-5 PTSD symptoms.', 'Self-report, 20 items, 5 to 10 minutes', 'No (free)', FREE_GEN, '[National Center for PTSD](https://www.ptsd.va.gov/professional/assessment/adult-sr/ptsd-checklist.asp)'),
 'CAPS5': ('**CAPS-5** (Clinician-Administered PTSD Scale)', 'The gold-standard diagnostic interview for PTSD.', 'Clinician interview, 45 to 60 minutes', 'No (free on request)', '★ Master’s-level clinical or assessment training required to request; training strongly encouraged', '[National Center for PTSD](https://www.ptsd.va.gov/professional/assessment/adult-int/caps.asp)'),
 'CAPSCA': ('**CAPS-CA-5** (CAPS for Children and Adolescents)', 'Diagnostic PTSD interview for ages 7 and older.', 'Clinician interview', 'No (free on request)', '★ Master’s-level clinical or assessment training required to request; training recommended', '[National Center for PTSD](https://www.ptsd.va.gov/professional/assessment/child/caps-ca.asp)'),
 'TSCC': ('**TSCC** (Trauma Symptom Checklist for Children)', 'Trauma symptoms in children ages 8 to 16.', 'Self-report, 54 items (screening form 20)', 'Yes', '★ Level B', '[PAR](https://www.parinc.com/TSCC)'),
 'TSI2': ('**TSI-2** (Trauma Symptom Inventory-2)', 'Broad trauma-related symptoms in adults ages 18 to 88.', 'Self-report, 136 items, about 20 minutes', 'Yes', '★ Level B', '[PAR](https://www.parinc.com/products/TSI-2)'),
 'PG13R': ('**PG-13-R** (Prolonged Grief-13-Revised)', 'Screening for DSM-5-TR prolonged grief disorder.', 'Self-report, 13 items', 'No (free)', FREE_GEN, doi('10.1002/wps.20823')),
 'ICG': ('**ICG** (Inventory of Complicated Grief)', 'Severity of maladaptive grief symptoms; widely used in research.', 'Self-report, 19 items', 'No (free)', FREE_GEN, doi('10.1016/0165-1781(95)02757-2')),
 # --- bipolar ---
 'MDQ': ('**MDQ** (Mood Disorder Questionnaire)', 'Screening for a history of mania or hypomania (bipolar spectrum).', 'Self-report, 13 yes/no items plus 2 questions', 'No (free)', FREE_GEN, doi('10.1176/appi.ajp.157.11.1873')),
 'ASRM': ('**ASRM** (Altman Self-Rating Mania Scale)', 'Current manic or hypomanic symptoms; an APA DSM-5 Level 2 measure.', 'Self-report, 5 items', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'YMRS': ('**YMRS** (Young Mania Rating Scale)', 'Clinician rating of manic symptom severity; standard in treatment research.', 'Clinician interview, 11 items', 'No (free)', '★ Clinical interviewing skill; training recommended', doi('10.1192/bjp.133.5.429')),
 # --- substance ---
 'AUDIT': ('**AUDIT** (Alcohol Use Disorders Identification Test)', 'Screening for hazardous and harmful drinking; first 3 items form the brief AUDIT-C.', 'Self-report or interview, 10 items', 'No (free)', FREE_GEN, '[World Health Organization](https://www.who.int/publications/i/item/who-msd-msb-01.6a)'),
 'ASSIST': ('**ASSIST** (Alcohol, Smoking and Substance Involvement Screening Test)', 'Screening risk across alcohol, tobacco, and other drugs.', 'Interview, 8 questions', 'No (free)', FREE_GEN, '[World Health Organization](https://www.who.int/publications/i/item/978924159938-2)'),
 'DAST': ('**DAST-10** (Drug Abuse Screening Test)', 'Screening for problems from drug use (other than alcohol).', 'Self-report, 10 yes/no items', 'No (free)', FREE_GEN, doi('10.1016/0306-4603(82)90005-3')),
 'CRAFFT': ('**CRAFFT 2.1**', 'Substance use screening for teens and young adults ages 12 to 21.', 'Self-report or interview, a few minutes', 'No (free)', FREE_GEN, '[CRAFFT website](https://crafft.org/)'),
 'SASSI': ('**SASSI-4 / SASSI-A3** (Substance Abuse Subtle Screening Inventory)', 'Likelihood of a substance use disorder, including in people who minimize use; adult and adolescent versions.', 'Self-report, about 15 minutes', 'Yes', '★ Level B', '[Pearson](https://www.pearsonassessments.com/store/usd/p/100001916)'),
 'APA_SUB': ('**APA Level 2 Substance Use** (adapted from NIDA-modified ASSIST)', 'Brief follow-up of substance use found on screening; adult and youth versions.', 'Self-report, brief', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 # --- eating ---
 'SCOFF': ('**SCOFF**', 'Very quick screen for anorexia and bulimia.', 'Self-report or interview, 5 yes/no questions', 'No (free)', FREE_GEN, doi('10.1136/bmj.319.7223.1467')),
 'EAT26': ('**EAT-26** (Eating Attitudes Test)', 'Screening for eating disorder risk.', 'Self-report, 26 items, about 2 minutes', 'No (free; see permission terms)', FREE_GEN, '[EAT-26 website](https://www.eat-26.com/)'),
 'EDEQ': ('**EDE-Q** (Eating Disorder Examination Questionnaire)', 'Eating disorder attitudes and behaviors over the past 28 days.', 'Self-report, 28 items', 'No (free for non-commercial use)', FREE_GEN, '[CREDO, University of Oxford](https://credo-oxford.com/7.2.html)'),
 'EDE': ('**EDE** (Eating Disorder Examination)', 'The gold-standard eating disorder interview.', 'Clinician interview, about 60 minutes', 'No', '★ Training required for reliable use', '[CREDO, University of Oxford](https://credo-oxford.com/7.2.html)'),
 'EDI3': ('**EDI-3** (Eating Disorder Inventory-3)', 'Eating disorder symptoms and related psychological traits, ages 13 to 53.', 'Self-report, 91 items, about 20 minutes', 'Yes', '★ Level B', '[PAR](https://parinc.com/products/EDI-3)'),
 'BES': ('**BES** (Binge Eating Scale)', 'Severity of binge eating.', 'Self-report, 16 items', 'No (free)', FREE_GEN, doi('10.1016/0306-4603(82)90024-7')),
 # --- ADHD ---
 'ASRS': ('**ASRS v1.1** (Adult ADHD Self-Report Scale, 6-item screener)', 'Screening adults for ADHD.', 'Self-report, 6 items', 'No (free; the 18-item version needs permission)', FREE_GEN, '[Harvard NCS site](https://www.hcp.med.harvard.edu/ncs/asrs.php)'),
 'VAND': ('**NICHQ Vanderbilt Assessment Scales**', 'Parent and teacher ratings of ADHD, ODD, conduct, anxiety, and depression symptoms, ages 6 to 12.', 'Parent and teacher forms, initial and follow-up', 'No (free)', FREE_GEN, '[NICHQ (PDF)](https://nichq.org/wp-content/uploads/2024/09/NICHQ-Vanderbilt-Assessment-Scales.pdf)'),
 'SNAP': ('**SNAP-IV** (APA Level 2 Inattention, parent version)', 'Parent rating of inattention and hyperactivity, ages 6 to 17.', 'Parent-report, brief', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'CONN4': ('**Conners 4**', 'ADHD and related problems, ages 6 to 18.', 'Parent, teacher, and self-report forms (full, short, 12-item index)', 'Yes', '★ Level B', '[MHS](https://storefront.mhs.com/collections/conners-4)'),
 'CAARS2': ('**CAARS 2** (Conners Adult ADHD Rating Scales)', 'ADHD in adults 18 and older, with self and observer forms.', 'Self- and observer-report, 97 items (short and index forms available)', 'Yes', '★ Level B', '[MHS](https://storefront.mhs.com/collections/CAARS-2)'),
 'BRIEF2': ('**BRIEF2** (Behavior Rating Inventory of Executive Function)', 'Everyday executive function (planning, self-control, working memory), ages 5 to 18.', 'Parent, teacher, and self-report forms, 55 to 63 items', 'Yes', '★ Level B', '[PAR](https://parinc.com/BRIEF2)'),
 'BASC3': ('**BASC-3** (Behavior Assessment System for Children)', 'Broad behavioral and emotional problems and strengths, ages 2 to 21 (college self-report to 25).', 'Parent, teacher, and self-report forms', 'Yes', '★ Level B', '[Pearson](https://www.pearsonassessments.com/store/usd/p/100001402)'),
 # --- autism ---
 'MCHAT': ('**M-CHAT-R/F** (Modified Checklist for Autism in Toddlers)', 'Screening toddlers for autism, with a follow-up interview.', 'Parent-report, 20 items, plus follow-up', 'No (free for clinical use)', FREE_GEN, '[M-CHAT website](https://www.mchatscreen.com/)'),
 'AQ': ('**AQ / AQ-10** (Autism Spectrum Quotient)', 'Screening for autistic traits in adults, teens, and children.', 'Self- or parent-report, 50 items (10-item short form)', 'No (free for clinicians and research)', FREE_GEN, '[Autism Research Centre, Cambridge](https://www.autismresearchcentre.com/tests/)'),
 'APA_ASD': ('**APA Clinician-Rated Severity of Autism Spectrum and Social Communication Disorders**', 'Rating the DSM-5 level of support needed.', 'Clinician-rated, brief', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'SCQ': ('**SCQ** (Social Communication Questionnaire)', 'Screening for autism in anyone over age 4.', 'Parent-report, 40 yes/no items', 'Yes', '★ Level C', '[WPS](https://www.wpspublish.com/scq-social-communication-questionnaire)'),
 'SRS2': ('**SRS-2** (Social Responsiveness Scale, 2nd ed.)', 'Severity of social impairment, age 2½ through adulthood.', 'Parent, teacher, relative, or self-report, 65 items', 'Yes', '★ Level C', '[WPS](https://www.wpspublish.com/srs-2-social-responsiveness-scale-second-edition)'),
 'CARS2': ('**CARS-2** (Childhood Autism Rating Scale, 2nd ed.)', 'Clinician rating of autism features, ages 2 and up.', 'Clinician-rated after observation and interview', 'Yes', '★ Level C', '[WPS](https://www.wpspublish.com/cars-2-childhood-autism-rating-scale-second-edition)'),
 'ADOS2': ('**ADOS-2** (Autism Diagnostic Observation Schedule)', 'The standard observational assessment for autism, 12 months to adulthood.', 'Structured clinician observation, 40 to 60 minutes', 'Yes', '★ Level C plus specialized training', '[WPS](https://www.wpspublish.com/ados-2-autism-diagnostic-observation-schedule-second-edition)'),
 # --- adjustment / somatic ---
 'SSS8': ('**SSS-8** (Somatic Symptom Scale-8)', 'Brief measure of physical symptom burden.', 'Self-report, 8 items', 'No (free)', FREE_GEN, doi('10.1001/jamainternmed.2013.12179')),
 'HAI': ('**HAI / SHAI** (Health Anxiety Inventory, short form)', 'Severity of health anxiety (illness anxiety).', 'Self-report, 18 items (short form)', 'No (free)', FREE_GEN, doi('10.1017/S0033291702005822')),
 'APA_SSD': ('**APA Clinician-Rated Severity of Somatic Symptom Disorder**', 'Rating the excessive thoughts, feelings, and behaviors that define the disorder.', 'Clinician-rated, brief', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 # --- psychosis ---
 'APA_PSY': ('**APA Clinician-Rated Dimensions of Psychosis Symptom Severity**', 'Rating hallucinations, delusions, disorganization, negative symptoms, cognition, depression, and mania.', 'Clinician-rated, 8 items', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'PANSS': ('**PANSS** (Positive and Negative Syndrome Scale)', 'The standard rating of positive, negative, and general symptoms in schizophrenia.', 'Clinician interview, 30 items, 45 to 50 minutes', 'Yes (licensed by MHS)', '★ Specialized training required', doi('10.1093/schbul/13.2.261')),
 'BPRS': ('**BPRS** (Brief Psychiatric Rating Scale)', 'Quick clinician rating of overall psychiatric symptoms, including psychosis.', 'Clinician interview, 18 items', 'No (free)', '★ Clinical interviewing skill; training recommended', doi('10.2466/pr0.1962.10.3.799')),
 'CDSS': ('**CDSS** (Calgary Depression Scale for Schizophrenia)', 'Depression in schizophrenia, separated from negative symptoms.', 'Clinician interview, 9 items', 'No (free for clinical use)', '★ Clinical interviewing skill; training recommended', doi('10.1016/0920-9964(90)90005-R')),
 'PQB': ('**PQ-B** (Prodromal Questionnaire-Brief)', 'Screening for early psychosis risk.', 'Self-report, 21 items', 'No (free)', FREE_GEN, doi('10.1016/j.schres.2011.03.029')),
 # --- disruptive behavior ---
 'APA_ODD': ('**APA Clinician-Rated Severity of Oppositional Defiant Disorder**', 'Rating ODD severity across settings.', 'Clinician-rated, brief', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'APA_CD': ('**APA Clinician-Rated Severity of Conduct Disorder**', 'Rating conduct disorder severity.', 'Clinician-rated, brief', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'ARI': ('**ARI** (Affective Reactivity Index)', 'Irritability in children and teens ages 6 to 17; an APA DSM-5 Level 2 measure.', 'Parent- and self-report, 7 items', 'No (free from the APA for clinical use)', FREE_GEN, '[APA assessment measures](' + APA + ')'),
 'SDQ': ('**SDQ** (Strengths and Difficulties Questionnaire)', 'Brief screen of conduct, emotional, attention, and peer problems plus strengths.', 'Parent, teacher, and self-report, 25 items', 'No (free paper version)', FREE_GEN, '[SDQ website](https://www.sdqinfo.org/)'),
 'ECBI': ('**ECBI / SESBI-R** (Eyberg Child Behavior Inventory)', 'Frequency of disruptive behavior at home and school, ages 2 to 16; tracks progress in parent training.', 'Parent form 36 items; teacher form 38 items', 'Yes', '★ Level B', '[PAR](https://parinc.com/products/ECBI)'),
 'ICU': ('**ICU** (Inventory of Callous-Unemotional Traits)', 'Callous-unemotional traits (the "limited prosocial emotions" specifier).', 'Parent, teacher, and self-report, 24 items', 'No (free)', FREE_GEN, '[Frick lab, LSU](https://faculty.lsu.edu/pfricklab/icu.php)'),
 'PCLYV': ('**Hare PCL:YV** (Psychopathy Checklist: Youth Version)', 'Psychopathic traits in youth ages 12 to 18, usually in forensic settings.', 'Clinician rating from interview and records', 'Yes', '★ Level C plus specialized training', '[MHS](https://storefront.mhs.com/collections/pcl-yv)'),
 'PCLR': ('**Hare PCL-R** (Psychopathy Checklist-Revised, 2nd ed.)', 'Psychopathy in adults, usually in forensic settings.', 'Clinician rating from interview and records, 20 items', 'Yes', '★ Level C plus specialized training', '[MHS](https://storefront.mhs.com/collections/pcl-r-2nd-ed)'),
 # --- personality-specific ---
 'MSI': ('**MSI-BPD** (McLean Screening Instrument for BPD)', 'Quick screen for borderline personality disorder.', 'Self-report, 10 yes/no items', 'No (free)', FREE_GEN, doi('10.1521/pedi.17.6.568.25355')),
 'BSL23': ('**BSL-23** (Borderline Symptom List-23)', 'Tracking the severity of borderline symptoms during treatment.', 'Self-report, 23 items', 'No (free)', FREE_GEN, doi('10.1159/000173701')),
 'ZAN': ('**ZAN-BPD** (Zanarini Rating Scale for BPD)', 'Clinician rating of change in borderline symptoms.', 'Clinician interview, 9 items', 'No (free)', '★ Clinical interviewing skill; training recommended', doi('10.1521/pedi.17.3.233.22147')),
 'GPTS': ('**GPTS** (Green Paranoid Thought Scales)', 'Ideas of reference and persecution (suspiciousness).', 'Self-report, 32 items', 'No (free)', FREE_GEN, doi('10.1017/S0033291707001638')),
 'SPQ': ('**SPQ** (Schizotypal Personality Questionnaire)', 'Schizotypal traits (odd beliefs, unusual experiences, social anxiety).', 'Self-report, 74 yes/no items', 'No (free)', FREE_GEN, doi('10.1093/schbul/17.4.555')),
 'PNI': ('**PNI** (Pathological Narcissism Inventory)', 'Both grandiose and vulnerable narcissism.', 'Self-report, 52 items', 'No (free)', FREE_GEN, doi('10.1037/a0016530')),
 'NPI16': ('**NPI-16** (Narcissistic Personality Inventory, short form)', 'Grandiose narcissistic traits.', 'Self-report, 16 forced-choice items', 'No (free)', FREE_GEN, doi('10.1016/j.jrp.2005.03.002')),
 'PSYRATS': ('**PSYRATS** (Psychotic Symptom Rating Scales)', 'Rating delusions on conviction, preoccupation, distress, and disruption; the outcome measure in major delusion trials.', 'Clinician interview; delusions scale 6 items', 'No (free)', '★ Clinical interviewing skill; training recommended', doi('10.1017/S0033291799008661')),
 'PDI': ('**PDI-21** (Peters et al. Delusions Inventory)', 'Delusional ideas plus how distressing, preoccupying, and convincing they are.', 'Self-report, 21 items', 'No (free)', FREE_GEN, doi('10.1093/oxfordjournals.schbul.a007116')),
 'BABS': ('**BABS** (Brown Assessment of Beliefs Scale)', 'How fixed a belief is and how much insight the person has.', 'Clinician interview, 7 items', 'No (free)', '★ Clinical interviewing skill; training recommended', doi('10.1176/ajp.155.1.102')),
 'FMPS': ('**FMPS** (Frost Multidimensional Perfectionism Scale)', 'Perfectionism (concern over mistakes, doubts, high standards, organization).', 'Self-report, 35 items', 'No (free)', FREE_GEN, doi('10.1007/BF01172967')),
}

COLS = ['Instrument', 'Best used for', 'Format', 'Purchase required?', 'Training or qualification', 'Where to find it']
WIDTHS = [1.35, 1.6, 1.2, 0.85, 1.05, 0.95]
NOTE = ('**★ = requires professional qualification to purchase or specialized training.** Publishers sell these tests only to qualified users. '
        'At Pearson, **Level B** generally means a master’s degree in a related field with formal assessment training, or a health care license; '
        '**Level C** means a doctorate in psychology or a related field with formal assessment training, or state licensure in a related field '
        f'([Pearson qualifications policy]({PEARSON_Q})). MHS, PAR, and WPS use similar levels. Check each publisher’s page before ordering. '
        '"Original article" links go to the published study that introduced a free scale that has no official website; the scale can usually be obtained there or from its authors.')


def table(keys, use=None):
    use = use or {}
    rows = []
    for k in keys:
        n, u, f, p, t, w = I[k]
        rows.append([n, use.get(k, u), f, p, t, w])
    return ('T', {'cols': COLS, 'widths': WIDTHS, 'rows': rows, 'notes': [NOTE]})


def add_assessment(body, keys, about, use=None, extra=None, takeaway=None):
    out, done = [], False
    for kind, text in body:
        if kind == 'H':
            m = re.match(r'(\d+)\. (.*)', text)
            if m and int(m.group(1)) >= 3:
                if not done:
                    out.append(('H', '3. Frequently used assessment instruments'))
                    out.append(('P', f'These are among the most widely used measures for screening, rating severity, and tracking progress in {about}. '
                                     '**Screening tools do not diagnose;** a positive screen calls for a clinical interview against DSM-5-TR criteria. '
                                     'Click an instrument’s website to find it.' + (' ' + extra if extra else '')))
                    out.append(table(keys, use))
                    done = True
                text = f'{int(m.group(1)) + 1}. {m.group(2)}'
        out.append((kind, text))
    assert done, 'section 3 heading not found'
    if takeaway:
        out.append(('B', takeaway))
    return out
