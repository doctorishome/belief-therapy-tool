/**
 * RSS-5 and Brief RCOPE for the counselor's local case record.
 *
 * Item wording is copied from the open-access source articles and is not paraphrased.
 * RSS-5: Salcone et al., 2025, Journal of Psychopathology and Behavioral Assessment,
 * https://doi.org/10.1007/s10862-024-10182-9 (CC BY 4.0).
 * Brief RCOPE questionnaire: Table 2 of Pargament, Feuille, and Burdzy, 2011, Religions,
 * https://doi.org/10.3390/rel2010051 (CC BY 3.0).
 *
 * Anchor judgments (also shown on each form):
 * RSS-5 is scored 1 = Not at all through 5 = A great deal. The article names
 * Somewhat, Quite a bit, and A great deal as the higher endorsements. The second
 * anchor, "A little bit," is the original RSS label (Exline and colleagues, 2014);
 * Salcone et al. do not print that word. Item wording is unchanged.
 * Brief RCOPE uses the article's 0 ("not at all") to 3 ("a great deal") scale.
 * Somewhat is the interior word the article uses. "Quite a bit" is the customary
 * label for 2; the 2011 article does not print it. Item wording is unchanged.
 * The two Brief RCOPE subscales are summed separately and are not combined.
 */

export const RSS5_ID = "rss5";
export const RCOPE_ID = "brcope";

const RSS_ANCHORS = [
  { value: 1, label: "Not at all" },
  { value: 2, label: "A little bit" },
  { value: 3, label: "Somewhat" },
  { value: 4, label: "Quite a bit" },
  { value: 5, label: "A great deal" },
];

const RCOPE_ANCHORS = [
  { value: 0, label: "Not at all" },
  { value: 1, label: "Somewhat" },
  { value: 2, label: "Quite a bit" },
  { value: 3, label: "A great deal" },
];

export const INSTRUMENTS = {
  [RSS5_ID]: {
    id: RSS5_ID,
    short: "RSS-5",
    title: "Religious and Spiritual Struggles Scale-5",
    blurb: "Five items, one total. A brief optional intake screen for adult clients. No clinical cutoff.",
    needsStressor: false,
    anchors: RSS_ANCHORS,
    groups: [
      {
        heading: "Religious and spiritual struggles",
        note: "One item for each kind of struggle on this short form. The demonic subscale from the original scale is not included.",
        items: [
          { domain: "Divine", sourceItem: 19, text: "Felt as though God had abandoned me" },
          { domain: "Interpersonal", sourceItem: 17, text: "Felt rejected or misunderstood by religious/spiritual people" },
          { domain: "Moral", sourceItem: 14, text: "Worried that my actions were morally or spiritually wrong" },
          { domain: "Doubt", sourceItem: 24, text: "Felt troubled by doubts or questions about spirituality/religion" },
          { domain: "Ultimate meaning", sourceItem: 7, text: "Questioned whether life really matters" },
        ],
      },
    ],
    intro: "It is not uncommon for people to struggle in their spirituality or faith at different points in life. Below you will find questions that ask about different types of ways that people might struggle in this area. In responding to items, please feel free to substitute an alternate word that captures whatever “God” means to you. For example, you may see God as a Higher Power, Divine Being, Great Spirit, Nature, a Positive Energy Providence, Fate, etc.",
    scaleNote: "Items are rated from 1 = Not at all to 5 = A great deal. A higher total means greater religious and spiritual struggle.",
    credit: "Salcone, Currier, McDermott, Davis, Raines, Lee, Exline, and Pargament (2025). Development and evaluation of the Religious and Spiritual Struggles Scale-5 (RSS-5). Journal of Psychopathology and Behavioral Assessment, 47, Article 8. https://doi.org/10.1007/s10862-024-10182-9. Open access under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/). Original Religious and Spiritual Struggles Scale: Exline and colleagues (2014), Psychology of Religion and Spirituality, 6, 208–222. Item wording is unchanged. The article’s sentence for the moral item leaves out a closing quotation mark before the subscale label; the words of the item are printed as quoted. The second anchor, “A little bit,” is the original RSS label; Salcone et al. name 1 = Not at all and 5 = A great deal, and they name Somewhat, Quite a bit, and A great deal as the higher endorsements.",
  },
  [RCOPE_ID]: {
    id: RCOPE_ID,
    short: "Brief RCOPE",
    title: "Brief RCOPE",
    blurb: "Fourteen items. Two scores, positive and negative religious coping, kept separate. Name the stressor first.",
    needsStressor: true,
    anchors: RCOPE_ANCHORS,
    groups: [
      {
        heading: "Positive religious coping",
        note: "Items 1–7. Scored as their own sum.",
        items: [
          { text: "Looked for a stronger connection with God." },
          { text: "Sought God\u2019s love and care." },
          { text: "Sought help from God in letting go of my anger." },
          { text: "Tried to put my plans into action together with God." },
          { text: "Tried to see how God might be trying to strengthen me in this situation." },
          { text: "Asked forgiveness for my sins." },
          { text: "Focused on religion to stop worrying about my problems." },
        ],
      },
      {
        heading: "Negative religious coping",
        note: "Items 8–14. Scored as their own sum. Not added to the positive score.",
        items: [
          { text: "Wondered whether God had abandoned me." },
          { text: "Felt punished by God for my lack of devotion." },
          { text: "Wondered what I did for God to punish me." },
          { text: "Questioned God\u2019s love for me." },
          { text: "Wondered whether my church had abandoned me." },
          { text: "Decided the devil made this happen." },
          { text: "Questioned the power of God." },
        ],
      },
    ],
    intro: "The Brief RCOPE asks how much each way of coping was used with one critical life event. Name that stressor, then rate every item for that same event.",
    scaleNote: "Each item is scored from 0 = not at all to 3 = a great deal. Positive religious coping is the sum of items 1–7 (0–21). Negative religious coping is the sum of items 8–14 (0–21). The article reports and interprets these two scores separately. This form does not add them together.",
    credit: "Pargament, Feuille, and Burdzy (2011). The Brief RCOPE: Current psychometric status of a short measure of religious coping. Religions, 2(1), 51–76. https://doi.org/10.3390/rel2010051. Open access under the Creative Commons Attribution license (http://creativecommons.org/licenses/by/3.0/). The fourteen items are Table 2, unchanged. The article scores extent of use from 0 (“not at all”) to 3 (“a great deal”) and uses “somewhat” for an interior response. “Quite a bit,” scored 2, is the customary label for that point; the 2011 article does not print those two words. Some published studies recode the same items from 1 to 4. This form keeps the 0–3 scoring.",
  },
};

export function instrumentById(id) {
  return INSTRUMENTS[id] || null;
}

export function flatItems(inst) {
  return inst.groups.flatMap((g) => g.items);
}

export function anchorLabel(inst, value) {
  const hit = inst.anchors.find((a) => a.value === value);
  return hit ? hit.label : "";
}

function answersAreComplete(inst, answers) {
  const items = flatItems(inst);
  if (!Array.isArray(answers) || answers.length !== items.length) return false;
  return answers.every((v) => inst.anchors.some((a) => a.value === v));
}

export function scoreRss5(answers) {
  const inst = INSTRUMENTS[RSS5_ID];
  if (!answersAreComplete(inst, answers)) return null;
  const total = answers.reduce((sum, n) => sum + n, 0);
  const explore = flatItems(inst)
    .map((item, i) => ({ ...item, index: i, value: answers[i], label: anchorLabel(inst, answers[i]) }))
    .filter((item) => item.value >= 3);
  return { total, min: 5, max: 25, explore };
}

export function scoreBriefRcope(answers) {
  const inst = INSTRUMENTS[RCOPE_ID];
  if (!answersAreComplete(inst, answers)) return null;
  const positive = answers.slice(0, 7).reduce((sum, n) => sum + n, 0);
  const negative = answers.slice(7, 14).reduce((sum, n) => sum + n, 0);
  return { positive, negative, min: 0, max: 21 };
}

export function scoreInstrument(id, answers) {
  if (id === RSS5_ID) return scoreRss5(answers);
  if (id === RCOPE_ID) return scoreBriefRcope(answers);
  return null;
}

export function missingPieces(id, answers, stressor) {
  const inst = instrumentById(id);
  if (!inst) return ["Unknown screen."];
  const missing = [];
  if (inst.needsStressor && !String(stressor || "").trim()) missing.push("Name the stressor this screen is about.");
  const items = flatItems(inst);
  const list = Array.isArray(answers) ? answers : [];
  items.forEach((_, i) => {
    if (!inst.anchors.some((a) => a.value === list[i])) missing.push("Answer item " + (i + 1) + ".");
  });
  return missing;
}

export function resultCopy(id, answers, stressor) {
  const inst = instrumentById(id);
  const scores = scoreInstrument(id, answers);
  if (!inst || !scores) return null;
  if (id === RSS5_ID) {
    const lines = [
      "Total " + scores.total + " (range 5–25). A higher total means greater religious and spiritual struggle.",
      "No clinical cutoff has been established for the RSS-5. This score is not a diagnosis, a severity band, or a pass/fail result.",
    ];
    if (scores.explore.length) {
      lines.push("Salcone et al. suggest asking more when an item is answered Somewhat, Quite a bit, or A great deal. That is a prompt to explore the kind of struggle, not a cutoff.");
    } else {
      lines.push("No item was answered Somewhat, Quite a bit, or A great deal.");
    }
    lines.push("The demonic subscale from the original scale is not part of this short form.");
    return { scores, lines, explore: scores.explore };
  }
  return {
    scores,
    lines: [
      "Positive religious coping " + scores.positive + " (items 1–7, range 0–21). A higher score means more use of these methods with the named stressor: looking for connection with God, care, help letting go of anger, acting with God, seeing the event as a way God might strengthen the person, asking forgiveness, or turning to religion to stop worrying.",
      "Negative religious coping " + scores.negative + " (items 8–14, range 0–21). A higher score means more spiritual tension about this stressor: wondering about abandonment or punishment, questioning God’s love or power, feeling the church had abandoned the person, or deciding the devil made it happen.",
      "These two scores stay separate. They are not added into one total. The article does not give a clinical cutoff, and it does not treat positive coping as always helpful or negative coping as always harmful.",
      "Stressor: " + String(stressor || "").trim(),
    ],
    explore: [],
  };
}

export function plainSummary(admin) {
  if (!admin) return "";
  const copy = resultCopy(admin.instrument, admin.answers, admin.stressor);
  if (!copy) return "";
  const inst = instrumentById(admin.instrument);
  const head = inst.short + ".";
  if (admin.instrument === RSS5_ID) {
    const flags = copy.explore.map((item) => item.domain + " " + item.value + " (" + item.label + "): " + item.text);
    return [head, ...copy.lines, flags.length ? "Items to explore: " + flags.join("; ") + "." : ""].filter(Boolean).join(" ");
  }
  return [head, ...copy.lines].join(" ");
}
