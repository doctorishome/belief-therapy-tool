import re, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH
sys.path.insert(0, sys.argv[1]); from refs import REFS
OUT = sys.argv[2]
d = Document()
for s in d.sections:
    s.left_margin = s.right_margin = Inches(0.75); s.top_margin = s.bottom_margin = Inches(0.7)
st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
st.paragraph_format.space_after = Pt(4); st.paragraph_format.line_spacing = 1.05
for name in ('Title','Heading 1'):
    s = d.styles[name]; s.font.name='Calibri'
    rf = s.element.rPr.rFonts
    for a in ('w:ascii','w:hAnsi','w:eastAsia','w:cs'): rf.set(qn(a),'Calibri')
    for a in ('w:asciiTheme','w:hAnsiTheme','w:eastAsiaTheme','w:cstheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
d.styles['Title'].font.size = Pt(24)
h1 = d.styles['Heading 1']; h1.font.size = Pt(13); h1.paragraph_format.space_before = Pt(10); h1.paragraph_format.space_after = Pt(2)
lb = d.styles['List Bullet']; lb.paragraph_format.space_after = Pt(2)
ln = d.styles['List Number']; ln.paragraph_format.space_after = Pt(2)

def runs(p, text, size=None):
    # **bold**, *italic*
    for part in re.split(r'(\*\*.+?\*\*|\*[^*]+?\*)', text):
        if not part: continue
        if part.startswith('**'): r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith('*'): r = p.add_run(part[1:-1]); r.italic = True
        else: r = p.add_run(part)
        if size: r.font.size = Pt(size)
    return p
def P(text, style=None, size=None): return runs(d.add_paragraph(style=style), text, size)
def B(text): return P(text, 'List Bullet')
def H(text): return d.add_heading(text, level=1)
def link(p, url, text, size):
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), p.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True))
    r = OxmlElement('w:r'); pr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '1F4E79'); pr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); pr.append(u)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size*2))); pr.append(sz)
    r.append(pr); t = OxmlElement('w:t'); t.text = text; r.append(t); h.append(r); p._p.append(h)

d.add_paragraph('Bipolar Disorders (DSM-5-TR): Teaching Overview', style='Title')
P('*Clinical Companion Knowledge Library: for counselors and counseling students*')

H('1. What it is')
P('Bipolar disorders are mood disorders marked by episodes of mania or hypomania, usually alternating with episodes of depression. In DSM-5-TR they have their own chapter, "Bipolar and Related Disorders," placed between the psychotic and depressive disorders (American Psychiatric Association [APA], 2022).')
P('**How common:** across 61,392 adults in 11 countries, lifetime prevalence was 0.6% for bipolar I, 0.4% for bipolar II, and 2.4% for the whole bipolar spectrum. Three in four had at least one other disorder, most often anxiety, and depressive episodes caused severe role impairment more often than manic ones (about 74% vs. 51%) (Merikangas et al., 2011).')
P('**Often missed:** across 27 studies (9,415 patients), management began a pooled 5.8 years after onset (Dagani et al., 2017). For a typical patient aged 25 to 45, remaining life expectancy is about 8 to 12 years shorter than average (Kessing et al., 2015).')
P('**Counselor framing:** bipolar disorder is a lifelong medical-psychiatric illness. **Medication is the foundation**; counseling works alongside it, and its key jobs are early recognition, adherence, and relapse prevention.')

H('2. Core symptoms to watch for')
P('DSM-5-TR criteria, paraphrased (APA, 2022); use the manual itself for formal diagnosis.')
B('**Manic episode:** abnormally elevated, expansive, or irritable mood *plus* increased activity or energy, most of the day, nearly every day, for **at least 1 week** (any length if hospitalized). Three or more of the following (four if mood is only irritable): grandiosity, **decreased need for sleep**, pressured speech, racing thoughts, distractibility, increased goal-directed activity or agitation, and risky pursuits (spending, sex, business ventures). It causes marked impairment, hospitalization, or psychosis.')
B('**Hypomanic episode:** the same symptoms for **at least 4 days**, a clear change that others notice, but without marked impairment, hospitalization, or psychosis.')
B('**Bipolar I:** at least one manic episode. **Bipolar II:** at least one hypomanic and one major depressive episode, never mania. **Cyclothymic disorder:** 2 years (1 in youth) of frequent hypomanic and depressive symptoms that never meet full episode criteria.')
B('**Specifiers** include anxious distress, mixed features, rapid cycling (4 or more episodes in a year), psychotic features, peripartum onset, and seasonal pattern. A full manic episode that begins during antidepressant treatment and persists beyond the drug’s effect counts toward bipolar I.')
P('**Differential diagnosis (general clinical consensus):** *unipolar depression*: always ask about past mania or hypomania before treating depression; *borderline personality disorder*: mood shifts over hours, tied to relationships, rather than episodes lasting days; *ADHD*: lifelong rather than episodic; *substances and medical causes* (stimulants, steroids, thyroid disease).')
P('**Screening:** on the Mood Disorder Questionnaire, 7 or more "yes" items gave sensitivity of 0.73 and specificity of 0.90 in mood clinics (Hirschfeld et al., 2000). It is a screen, not a diagnosis.')
P('**Suicide risk:** lifetime suicide attempts were reported by 36.3% with bipolar I and 32.4% with bipolar II, not a significant difference, so bipolar II is not "milder" for safety (Novick et al., 2010). Ask directly, especially in depressive and mixed states.')
P('**When counselors must refer (general clinical consensus):** refer for psychiatric evaluation whenever mania, hypomania, psychosis, a mixed state, or suicidality is suspected. Use emergency services for danger to self or others or for severe mania with poor judgment. Counselors do not manage medication; coordinate with the prescriber through a signed release.')

H('3. What works: treatment and the evidence')
P('**Bottom line for class:** medication is the foundation. Skills-based psychotherapy *added to* medication lowers relapse and speeds recovery from bipolar depression. Psychotherapy alone is not a treatment for bipolar I.')
P('**Medication (referral notes).** Lithium has the strongest evidence for long-term prevention (Geddes & Miklowitz, 2013; Yatham et al., 2018). Versus placebo it reduced any mood episode (RR 0.66) and manic episodes (RR 0.52) (Severus et al., 2014) and reduced suicides (OR 0.13) (Cipriani et al., 2013). Adding a standard antidepressant to a mood stabilizer did not improve durable recovery (23.5% vs. 27.3% with placebo) (Sachs et al., 2007), and an antidepressant *without* a mood stabilizer nearly tripled the risk of mania (HR 2.83) (Viktorin et al., 2014). Nonadherence runs 10% to 60% (median 40%) in mood disorders, and attitudes and beliefs predict it at least as much as side effects do (Lingam & Scott, 2002), which makes it a natural CBT target.')
P('**Psychotherapy evidence (honest effect sizes):**')
B('**Overall:** across 39 trials (3,863 people), manualized therapies plus medication lowered recurrence (OR 0.56). Psychoeducation with skills practice worked better in a group or family format than individually (OR 0.12), and CBT helped stabilize depressive symptoms (SMD −0.32) (Miklowitz et al., 2021).')
B('**CBT:** in 19 trials (1,384 patients), CBT lowered relapse (OR 0.51) and improved depression (g = −0.49), mania severity (g = −0.58), and functioning (g = 0.46) (Chiang et al., 2017). In a relapse-prevention trial (n = 103), cognitive therapy brought fewer episodes, fewer days ill, fewer admissions, and better coping with warning signs over 12 months (Lam et al., 2003). **Caution:** in a large pragmatic trial (n = 253), CBT did not reduce recurrence overall; it helped people with fewer than 12 prior episodes but not those with more (Scott et al., 2006). Start early.')
B('**Group psychoeducation** (21 sessions, n = 120) reduced recurrences and hospitalizations over 2 years (Colom et al., 2003).')
B('**Family-focused therapy** (n = 101): relapse 35% vs. 54% with crisis management, with better medication adherence (Miklowitz et al., 2003).')
B('**Interpersonal and social rhythm therapy** (n = 175): longer survival without a new episode, and more regular daily routines predicted fewer recurrences (Frank et al., 2005).')
B('**Bipolar depression** (STEP-BD, n = 293): up to 30 sessions of family-focused therapy, social rhythm therapy, or CBT gave higher 1-year recovery (64.4% vs. 51.5%) and faster recovery than 3 sessions of collaborative care (Miklowitz et al., 2007).')
P('**CBT for bipolar disorder: how it is used** (drawn from the trials above):')
B('**Teach the illness model** and the role of medication; chart mood and sleep daily.')
B('**Map early warning signs** of mania and depression and write a relapse-prevention plan (Lam et al., 2003).')
B('**Protect sleep and daily rhythms**; sleep loss can trigger mania (Frank et al., 2005).')
B('**Challenge the beliefs** that drive relapse: hypomanic thinking ("I don’t need sleep," "nothing can go wrong"), depressive thinking, and beliefs about medication (Lingam & Scott, 2002). Involve family when possible (Miklowitz et al., 2003).')

H('4. Religion, spirituality, and Christian integration: what the evidence shows')
P('**Faith matters to most patients.** Among patients in remission, 78% held strong religious or spiritual beliefs and 81.5% practiced frequently; most linked their faith to managing the illness. Yet faith conflicted with medical illness models for 24% and with medical advice for 19% (Mitchell & Romans, 2003).')
P('**Religious coping.** Among 168 outpatients (88% religiously affiliated), intrinsic religiosity (OR 0.19) and positive religious coping (OR 0.25) were linked to fewer depressive symptoms, and negative religious coping to poorer psychological quality of life (Stroppa & Moreira-Almeida, 2013). Among 334 veterans, more frequent private prayer or meditation was associated with mixed states, while mania and depression were not associated with religious involvement (Cruz et al., 2010); the direction of this link is unknown. A scoping review of 18 studies found intrinsic religiosity and positive coping most consistently tied to better outcomes, and found that patients want clinicians to take their faith into account (Jackson et al., 2022).')
P('**Intervention studies.** We found **no trial of Christian or religiously integrated CBT for bipolar disorder** (PubMed search, October 31, 2026). The nearest evidence comes from other disorders:')
B('Religiously modified CBT (10 studies in depression, anxiety, and schizophrenia) mostly matched standard CBT; not yet well established, but acceptable to strongly religious clients (Lim et al., 2014).')
B('Faith-adapted CBT for depression and anxiety (16 trials) showed benefits, but trials were small and at risk of bias (Anderson et al., 2015).')
B('Religious CBT matched conventional CBT for major depression (n = 132) and was slightly more effective for more religious clients (Koenig et al., 2015).')
P('**Honest summary for teaching:**')
P('Medication plus psychoeducation, CBT, family work, and rhythm regulation is the evidence base. Faith integration supports engagement and coping; it does not replace them.', 'List Number')
P('Intrinsic faith and positive religious coping go with fewer depressive symptoms, but conflict between faith and medical advice is a real threat to adherence.', 'List Number')
P('No bipolar-specific trial of religious CBT exists. Extend findings from depression cautiously, with consent, and in coordination with the prescriber.', 'List Number')

H('5. Practical Christian-integration notes')
P('These apply Dr. Campbell’s identify, challenge, replace-with-Scripture method alongside psychiatric care. Clinical items rest on the research above. Pastoral items are theological application, not research findings.')
B('**Identify (clinical).** Take a spiritual history: does faith help, or does it conflict with treatment ("taking lithium means I don’t trust God") (Mitchell & Romans, 2003)? Tell sincere faith from hypomanic religious grandiosity ("God has chosen me for a mission that can’t wait") by sleep loss, pressured speech, and change from the person’s usual faith, not by content.')
B('**Challenge (clinical).** Test the beliefs that drive relapse: "I feel fine, so I’m healed and can stop my medication," "this energy is God’s anointing," and, when depressed, "God has abandoned me." Use mood charts and shared evidence review, never argument about faith (Lingam & Scott, 2002).')
B('**Replace (pastoral).** Offer Scripture that supports self-control, rest, rhythm, and wise counsel:')
for v in ['“For God has not given us a spirit of fear, but of power, love, and self-control.” (2 Timothy 1:7). Keeping a treatment plan is part of self-control.',
          '“In vain you rise early and stay up late, toiling for bread to eat—for He gives sleep to His beloved.” (Psalm 127:2). Sleep is a gift that protects against relapse.',
          '“To everything there is a season, and a time for every purpose under heaven.” (Ecclesiastes 3:1). Regular daily rhythms honor the way God made us.',
          '“Plans fail for lack of counsel, but with many advisers they succeed.” (Proverbs 15:22). The treatment team, family, and pastor are “many advisers.”']:
    p = P(v, 'List Bullet 2')
B('**Faith community (clinical).** With a signed release, help family and pastor learn the warning signs and support treatment (Miklowitz et al., 2003). Luke, “the beloved physician” (Colossians 4:14), can frame medicine as compatible with faith.')
B('**Ministers:** use this for referral awareness only. Ministers cannot diagnose; refer suspected mania or severe depression promptly.')

H('6. Quick classroom takeaways')
B('Mania lasts at least 1 week, hypomania at least 4 days; always screen for past highs before treating depression.')
B('Medication, especially lithium, is the foundation. CBT, group or family psychoeducation, and social rhythm therapy reduce relapse when added to it.')
B('Faith is often a resource and sometimes a conflict with treatment. Assess it, support positive coping, and watch for religious grandiosity. No Christian-specific CBT trial for bipolar disorder exists yet.')

H('Sources note')
P(f'All {len(REFS)} references were checked against Crossref and PubMed (October 31, 2026), and the figures quoted were checked against each study’s abstract. Each DOI is a live link to the publisher record.')
H('References')
for _, au, yr, ti, jo, vo, iss, pg, doi in REFS:
    p = d.add_paragraph(); pf = p.paragraph_format
    pf.left_indent = Inches(0.35); pf.first_line_indent = Inches(-0.35); pf.space_after = Pt(2); pf.line_spacing = 1.0
    S = 8.5
    r = p.add_run(f'{au} ({yr}). '); r.font.size = Pt(S)
    if jo is None:
        r = p.add_run(ti + '. '); r.italic = True; r.font.size = Pt(S)
    else:
        r = p.add_run(ti + '. '); r.font.size = Pt(S)
        r = p.add_run(jo + ', ' + vo); r.italic = True; r.font.size = Pt(S)
        r = p.add_run((f'({iss})' if iss else '') + f', {pg}. '); r.font.size = Pt(S)
    link(p, 'https://doi.org/' + doi, 'https://doi.org/' + doi, S)
p = P(f'*Prepared for Clinical Companion (Brian Campbell). Teaching overview only. Clinically review before use. Not a substitute for the DSM-5-TR or clinical judgment. All {len(REFS)} references and DOIs verified via Crossref and PubMed (Saturday, Oct 31, 2026). Effect sizes as reported in the cited sources.*', size=8)
# page numbers in footer
for s in d.sections:
    fp = s.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run(); f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'),'begin'); r._r.append(f1)
    it = OxmlElement('w:instrText'); it.text = 'PAGE'; r._r.append(it)
    f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'),'end'); r._r.append(f2); r.font.size = Pt(9)
d.save(OUT)
