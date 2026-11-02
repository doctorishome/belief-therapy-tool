// Builds counselors/forms/Belief-Counseling-Christian-Experiences-and-Beliefs-Checklist.docx
// Run from the repo root: NODE_PATH=$(npm root -g) node tools/build_christian_experiences.js
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType, Footer, PageNumber, TabStopType, SectionType } = require('docx');
const NAVY = '12284C', GOLD = 'C9A227', CREAM = 'FAF6EC', MUTED = '5B6678', INK = '1F2A3A';
const FONT = 'Georgia', SZ = 24; // 12 pt

// Pairs of sections, shown side by side: [left, right]
const S = [
  [['Childhood Church Experience', [
    'I attended church regularly as a child (approximately weekly).',
    'I liked going to church as a child.',
    'As a child, my church was very conservative and legalistic (focused on rules).',
    'I went to Vacation Bible School as a child.',
    'As a child, I took confirmation classes or studied for my first communion.',
    'As a child, I never really understood what church was about.']],
   ['Family and Parental Faith', [
    'One or both of my parents claimed to be a Christian.',
    'One or both of my parents worked in part-time or full-time Christian ministry.',
    'My parents were both devout Christians.',
    'As a child, although my parents went to church, they did not really live Christian lives.',
    'My parents were openly hostile toward church and God.',
    'I am a preacher’s kid (PK).',
    'I am a missionary kid (MK).',
    'Although my parents never went to church, someone else took me.',
    'My parents prayed with me as a child and taught me to pray.']]],
  [['Youth Experience', [
    'As a youth, I regularly participated in my church youth group.',
    'As a youth, I went on mission trips with my youth group.',
    'As a youth, my parents had to force me to go to church.',
    'As a youth, I wasn’t allowed to go to dances or listen to non-Christian music.']],
   ['Prayer and the Holy Spirit', [
    'As an adult, I pray on a regular daily basis.',
    'I believe in the power of prayer and that God can perform miracles when we pray.',
    'I don’t know much about the “Holy Spirit.”',
    'I feel the presence of the Holy Spirit in my life.',
    'I believe in the power of prayer.',
    'I believe that God answers our prayers.',
    'I have an active and ongoing prayer life.']]],
  [['Confession, Forgiveness, and Sin', [
    'I believe that you should regularly confess your sins to a priest.',
    'I believe that communion bread and wine actually turn into the body and blood of Christ.',
    'I believe that Jesus can forgive all sins, no matter how “bad” they are.',
    'I believe that once Jesus forgives my sins, God is not even aware of them.',
    'I believe that some sins are worse than other sins.',
    'I believe that all human beings sin, even “born again” Christians.']],
   ['Doubt, Suffering, and God’s Justice', [
    'I am having a crisis of faith. I don’t know what I believe anymore.',
    'If God is “all loving,” I don’t understand why good people suffer.',
    'I believe that pain and suffering can be good for human beings.',
    'I believe that if I follow God, I will be rewarded with money and prosperity.']]],
  [['Childhood Relationship with God', [
    'When I look back on my childhood, I feel that Christianity was forced on me as a child.',
    'As a child, no one ever taught me about God.',
    'Since my earliest childhood memories, I have loved the Lord.',
    'As a child, I felt God’s love at church.',
    'I gave my life to God as a child and had a “born again” experience.',
    'I studied the Bible and learned Bible verses as a child.',
    'As a child, I cried out to God, but He didn’t answer me.',
    'I feel I was abused by Christians as a child.',
    'As a child, I never really believed in God.',
    'As a child, I thought of God as someone who would punish you if you were bad.']],
   ['Core Doctrine and Scripture', [
    'I believe that the Bible is flawless (inerrant), the perfect Word of God.',
    'I have my doubts about the Old Testament, but I believe in the New Testament.',
    'I believe that Jesus Christ was God, and not just a wise man.',
    'I believe in the teachings of Christ, but deep down I don’t really think He was God.',
    'I believe that God is omnipotent (all powerful) and omniscient (all knowing).',
    'I believe in the life, death, and resurrection of Jesus Christ.',
    'I believe that Jesus Christ died for my sins.',
    'I believe that if children die without knowing Jesus, they will still go to heaven.',
    'I believe that there is an actual place called hell.',
    'I believe I will see my family again once I die and go to heaven.']]],
  [['Salvation and Assurance', [
    'I consider myself to be a “born again” Christian.',
    'I have my doubts that heaven really exists.',
    'I have doubts about whether I am really saved.',
    'I believe “once saved, always saved.” You can’t lose your salvation once you are saved.',
    'I believe that God has chosen certain people to be saved and not others.',
    'I believe you can “backslide” and lose your salvation (even if you were once saved).',
    'I really don’t have to worry about anything I do, because I am “saved.”']],
   ['Miracles', [
    'I believe in miracles.',
    'I believe that miracles only happened in the times of Jesus and His apostles.',
    'God has performed miracles in my life.']]],
  [['Guilt, Judgment, and Self-Forgiveness', [
    'I believe that all mental illness is a result of the person’s sin.',
    'I believe that there are always consequences for sin.',
    'I believe that God is punishing me for my sins.',
    'Although I know that God forgives sins, I can’t seem to forgive myself.']],
   ['Present Relationship with God', [
    'I feel close to God and His presence.',
    'I feel I have drifted away from God and His influence on my life.',
    'I used to feel close to God, but now I feel He is very far away.',
    'I have almost given up hope that God will rescue me.']]],
];

const r = (text, o = {}) => new TextRun({ text, font: FONT, size: SZ, color: INK, ...o });
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const NB = { top: none, bottom: none, left: none, right: none };
const W = 10080, GAP = 360, CW = (W - GAP) / 2;

const section = ([title, items]) => [
  new Paragraph({ keepNext: true, spacing: { before: 220, after: 100 }, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD, space: 3 } },
    children: [new TextRun({ text: title, font: FONT, size: 25, bold: true, color: NAVY })] }),
  ...items.map(t => new Paragraph({ spacing: { after: 60 }, indent: { left: 400, hanging: 400 }, tabStops: [{ type: TabStopType.LEFT, position: 400 }],
    keepLines: true, children: [r('☐', { color: NAVY, font: 'Segoe UI Symbol' }), r('\t' + t)] })),
];
const body = S.flat().flatMap(section);

const instr = new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], rows: [new TableRow({ children: [new TableCell({
  width: { size: W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: CREAM }, margins: { top: 140, bottom: 140, left: 220, right: 220 },
  borders: { top: { style: BorderStyle.SINGLE, size: 18, color: GOLD }, bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD }, left: { style: BorderStyle.SINGLE, size: 6, color: GOLD }, right: { style: BorderStyle.SINGLE, size: 6, color: GOLD } },
  children: [new Paragraph({ children: [r('Instructions: ', { bold: true, color: NAVY }), r('Read each statement and check all that apply to you. If a statement does not apply, leave it blank.')] })] })] })] });

const PAGE = { size: { width: 12240, height: 15840 }, margin: { top: 900, bottom: 900, left: 1080, right: 1080 } };
let FOOT;
const logo = fs.readFileSync('belief-counseling-logo.png');
const doc = new Document({
  creator: 'Brian Campbell, Ph.D.', title: 'Christian Experiences and Beliefs Checklist',
  styles: { default: { document: { run: { font: FONT, size: SZ } } } },
  sections: [{
    properties: { page: PAGE },
    footers: FOOT = { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 4 } },
      children: [new TextRun({ text: 'Belief Counseling  ·  © 2026 Brian Campbell, Ph.D.  ·  Page ', font: FONT, size: 16, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: MUTED })] })] }) },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 68, height: 90 }, altText: { title: 'Belief Counseling logo', description: 'Belief Counseling logo: a cross before a rising sun', name: 'logo' } })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [new TextRun({ text: 'Christian Experiences and Beliefs', font: FONT, size: 40, bold: true, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: 'A Checklist', font: FONT, size: 26, italics: true, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 220 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } },
        children: [new TextRun({ text: 'By Brian Campbell, Ph.D.  ·  © 2026 Brian Campbell, Ph.D. All rights reserved.', font: FONT, size: 20, italics: true, color: MUTED })] }),
      new Paragraph({ spacing: { after: 200 }, tabStops: [{ type: TabStopType.LEFT, position: 6600 }], children: [r('Name: ______________________________________', { bold: true, color: NAVY }), r('\tDate: ________________', { bold: true, color: NAVY })] }),
      instr,
      new Paragraph({ spacing: { after: 120 }, children: [] }),
    ] },
    { properties: { type: SectionType.CONTINUOUS, page: PAGE, column: { count: 2, space: 400 } }, footers: FOOT,
      children: body },
    { properties: { type: SectionType.CONTINUOUS, page: PAGE }, footers: FOOT, children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 6 } },
        children: [new TextRun({ text: 'For use in counseling and training. Not a diagnostic instrument.', font: FONT, size: 18, italics: true, color: MUTED })] }),
    ] }] });
Packer.toBuffer(doc).then(b => fs.writeFileSync(process.argv[2] || 'counselors/forms/Belief-Counseling-Christian-Experiences-and-Beliefs-Checklist.docx', b));
