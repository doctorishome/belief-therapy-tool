/** Clearly fictional sample cases. Every fact is invented. */

function daysAgo(n) {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d.toISOString().slice(0, 10);
}

export function sampleCases() {
  const now = new Date().toISOString();
  const stamp = (c) => ({ ...c, createdAt: now, updatedAt: now });
  return [
    stamp({
      id: "sample-case-0001",
      sample: true,
      name: "Jordan Testcase",
      preferredName: "Jordy",
      dob: "1990-04-12",
      phone: "(555) 010-4477",
      email: "jordan.testcase@example.com",
      address: "123 Example Street, Apt 4B, Springfield, ZZ 00000",
      clientId: "CC-000123",
      presentingConcerns:
        "FAKE SAMPLE DATA. Jordan reports low mood, poor sleep (waking at 4am), loss of interest in hobbies, and difficulty concentrating at work for about 3 months. Also reports worry about job performance and occasional chest tightness before meetings.",
      history:
        "FAKE SAMPLE DATA. Jordan Testcase (DOB 04/12/1990) works at Acme Widgets Inc. Partner Riley Example is supportive. One prior depressive episode in 2015 treated with counseling. No hospitalizations. Denies substance use beyond 1-2 drinks per week. No current SI/HI reported. Contact: (555) 010-4477, jordan.testcase@example.com.",
      notes: [
        {
          id: "n1",
          date: daysAgo(21),
          text: "Intake. Jordan presented with flat affect, tearful when discussing work. PHQ-9 = 16, GAD-7 = 11. Jordy (preferred name) says sleep has been poor since a date in March. Discussed safety; denies SI.",
        },
        {
          id: "n2",
          date: daysAgo(14),
          text: "Session 2. Jordan practiced behavioral activation (walks 3x/week). Reports Riley noticed some improvement. Still ruminating at night.",
        },
        {
          id: "n3",
          date: daysAgo(7),
          text: "Session 3. Mood slightly improved (self-rated 4/10 to 5/10). Worry about a performance review at Acme Widgets Inc. Began cognitive restructuring around the belief “If I am not perfect at work I am a failure.”",
        },
      ],
      workingDiagnoses:
        "FAKE SAMPLE: Rule out Major Depressive Disorder, recurrent, moderate (F33.1). Consider Generalized Anxiety Disorder (F41.1).",
      confirmedDiagnoses: "",
      treatmentPlan:
        "FAKE SAMPLE: 1) Reduce depressive symptoms (PHQ-9 under 10 within 12 weeks). 2) Improve sleep to 6+ hours a night. Interventions: CBT, behavioral activation, sleep hygiene.",
      sessionPlan: "",
    }),
    stamp({
      id: "sample-case-0002",
      sample: true,
      name: "Sam Fictional",
      preferredName: "Sam",
      dob: "1998-11-02",
      phone: "(555) 010-2290",
      email: "sam.fictional@example.com",
      address: "456 Sample Avenue, Unit 2, Exampletown, ZZ 00001",
      clientId: "CC-000456",
      presentingConcerns:
        "FAKE SAMPLE DATA. Sam describes months of intrusive doubts about having offended God, repeated confession, and avoidance of church services. Sleep is light. Work as a library aide is harder on days the doubts are loud. Denies wanting to die.",
      history:
        "FAKE SAMPLE DATA. Sam Fictional grew up in a church that stressed rule-keeping. No psychiatric hospital stays. No substance use. A primary-care visit last year was described as normal. Sam calls the fear “scrupulosity” after reading about it, and also says “If I have a bad thought, I have sinned as if I did it.”",
      notes: [
        {
          id: "n1",
          date: daysAgo(10),
          text: "Intake. Cooperative, anxious, seeks reassurance about whether a thought was sinful. Agreed to try noticing the thought without confessing it this week. Safety: no SI, no HI.",
        },
      ],
      workingDiagnoses:
        "FAKE SAMPLE: Consider obsessive-compulsive disorder with religious scrupulosity (F42.2). Rule out a primary depressive disorder and a medical cause of anxiety.",
      confirmedDiagnoses: "",
      treatmentPlan:
        "FAKE SAMPLE: ERP-informed CBT aimed at less reassurance and less repeated confession, plus belief work on thought-action fusion. Coordinate with Sam’s pastor only if Sam asks.",
      sessionPlan: "",
    }),
    stamp({
      id: "sample-case-0003",
      sample: true,
      name: "Riley Sample",
      preferredName: "Riley",
      dob: "1976-06-18",
      phone: "(555) 010-8831",
      email: "riley.sample@example.com",
      address: "78 Practice Road, Fiction City, ZZ 00002",
      clientId: "CC-000789",
      presentingConcerns:
        "FAKE SAMPLE DATA. Riley’s fictional spouse died of a sudden illness 5 months ago. Riley reports waves of sadness, guilt (“I should have noticed sooner”), poor appetite, and withdrawal from a weekly small group. Still goes to work. No alcohol increase. No current plan to self-harm.",
      history:
        "FAKE SAMPLE DATA. Riley Sample has no prior counseling. One adult child lives out of state and phones weekly. Riley says “God is punishing me” and also “I will never feel like myself again.” Medical care is current; the fictional physician knows about the grief.",
      notes: [
        {
          id: "n1",
          date: daysAgo(6),
          text: "Session 1. Tearful, oriented, future-oriented about work. Named the belief “This death is my fault and God’s punishment.” Homework: one short walk and one meal with a neighbor. Safety plan reviewed; denies SI.",
        },
      ],
      workingDiagnoses:
        "FAKE SAMPLE: Grief is prominent. Consider major depressive disorder if symptoms stay past what Riley’s culture and clinician judge to be the course of grief (provisional F32.1). Rule out medical illness and substance use.",
      confirmedDiagnoses: "",
      treatmentPlan:
        "FAKE SAMPLE: Support grief, watch depressive symptoms, and gently examine the punishment belief with Scripture the client already trusts. Reassess in 4 weeks.",
      sessionPlan: "",
    }),
  ];
}
