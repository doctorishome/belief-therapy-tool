const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType, Footer, PageNumber, VerticalAlign, TabStopType } = require('docx');
const NAVY = '12284C', GOLD = 'C9A227', CREAM = 'FAF6EC', MUTED = '5B6678', INK = '1F2A3A';
const FONT = 'Georgia';
const items = [
'Told me I was bad or worthless.','Made me feel that I wasn’t good enough.','Never really accepted me.','Made me feel that I didn’t belong in the family.',
'Made me feel unwanted.','Were never around very much when I was young.','Were unreliable.',
'Were too preoccupied with their own lives to pay much attention to me.','Called me insulting names.','Constantly criticized me.',
'Beat me with belts, brushes, or other objects.','Neglected me physically.','Abused me physically.','Neglected me emotionally.','Got drunk or used drugs.',
'Frightened me a lot.','Made me feel ashamed of *them.*','Made me feel ashamed of *myself.*','Made fun of me or laughed at me in a cruel way.',
'Were severely depressed or unavailable because of emotional, mental, or physical illness.','Behaved in odd, unusual, or bizarre ways.',
'Made me feel that I had to take care of them because of their problems.','Tried to make me think they were perfect.','Pressured me and expected too much of me.',
'Rarely hugged or kissed me.','Rarely told me they loved me.','Blamed me for their problems.','Fought a lot.',
'Sexually molested me.','Were extremely controlling.','Used money to control me.','Used guilt to control me.','Used threats to control me.',
'Seemed to like my brother or sister better than me.','Told me they wished I’d never been born.','Told me I’d never make anything of myself.',
'Were inconsistent when disciplining me.','Lied a lot, both to me and to others.','Frequently broke the law.','Cheated or took advantage of others.',
'Were overly concerned about grades.','Told me I was dumb or stupid.','Did not provide a safe home for me.',
'Were extremely conservative and legalistic.','Were overprotective.','Taught me that the world is a scary place.','Often fought about money.',
'Gave me the feeling that they didn’t have enough money to live on.','Taught me not to trust anyone.','Taught me to expect that the worst will happen.',
'Rarely said they were sorry.','Rarely admitted mistakes.','Made me keep family secrets.',
'Tried to pretend everything was fine when it wasn’t.','Isolated me and kept me away from other children.','Constantly compared me to my brothers or sisters.',
'Never laughed much.','Died when I was young.','Divorced when I was a child.','Abandoned me when I was young.','Couldn’t stand it if I disagreed with them.',
'Spoiled me.','Constantly bragged about me to others.','Tended to let me do whatever I wanted.','Worshiped the ground I walked on.',
'Made me feel “special” or “unique.”','Were very concerned about money and “status.”','Were very concerned about how I looked and how I dressed.',
'“Put me down” in front of others.','Didn’t allow me to express my feelings.','Didn’t care how I felt about things.',
'Tended to make all of my decisions for me when I was growing up.',
'Tended to be very negative and pessimistic.','Made me feel helpless to do anything for myself.',
];
const r = (text, o = {}) => new TextRun({ text, font: FONT, size: 19, color: INK, ...o });
const rich = (t, o = {}) => t.split(/(\*[^*]+\*)/).filter(Boolean).map(s => s.startsWith('*') ? r(s.slice(1, -1), { italics: true, ...o }) : r(s, o));
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const NB = { top: none, bottom: none, left: none, right: none };
const W = 10080, CW = W / 2;
const cell = (n, t) => new TableCell({ width: { size: CW, type: WidthType.DXA }, margins: { top: 50, bottom: 50, left: 0, right: 200 }, borders: NB,
  children: t ? [new Paragraph({ indent: { left: 1180, hanging: 1180 }, tabStops: [{ type: TabStopType.LEFT, position: 780 }, { type: TabStopType.LEFT, position: 1180 }],
    children: [r('________', { color: MUTED }), r(`\t${n}.`, { color: GOLD, bold: true, size: 17 }), r('\t'), ...rich(t)] })] : [new Paragraph('')] });
const half = Math.ceil(items.length / 2);
const rows = [];
for (let i = 0; i < items.length; i += 2) {
  rows.push(new TableRow({ cantSplit: true, children: [cell(i + 1, items[i]), cell(i + 2, items[i + 1])] }));
}
const list = new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [CW, CW], borders: { ...NB, insideHorizontal: none, insideVertical: none }, rows });
const chip = (code, label) => [r(code, { bold: true, color: NAVY }), r(` = ${label}`)];
const sep = () => r('      ');
const sep2 = () => r('   ');
const instr = new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], rows: [new TableRow({ children: [new TableCell({
  width: { size: W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: CREAM }, margins: { top: 160, bottom: 160, left: 220, right: 220 },
  borders: { top: { style: BorderStyle.SINGLE, size: 18, color: GOLD }, bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD }, left: { style: BorderStyle.SINGLE, size: 6, color: GOLD }, right: { style: BorderStyle.SINGLE, size: 6, color: GOLD } },
  children: [
    new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: 'Instructions', font: FONT, size: 22, bold: true, color: NAVY })] }),
    new Paragraph({ spacing: { after: 100 }, children: [r('Parents, caretakers, or close relatives can have a significant influence on children. Please read the items listed below and mark all that apply by writing the appropriate letter or letters in the space provided, using the key below. If an item does not apply, please just leave it blank.')] }),
    new Paragraph({ spacing: { before: 60, after: 80 }, children: [...chip('M', 'Mother'), sep(), ...chip('F', 'Father'), sep(), ...chip('B', 'Both')] }),
    new Paragraph({ spacing: { after: 60 }, children: [r('If someone other than your biological mother or father served as your caretaker or influenced you greatly, please use the following letters:', { italics: true })] }),
    new Paragraph({ spacing: { after: 40 }, children: [...chip('SM', 'Stepmother'), sep(), ...chip('SF', 'Stepfather'), sep(), ...chip('BR', 'Brother'), sep(), ...chip('S', 'Sister')] }),
    new Paragraph({ children: [...chip('A', 'Aunt'), sep(), ...chip('U', 'Uncle'), sep(), ...chip('GM', 'Grandmother'), sep(), ...chip('GF', 'Grandfather')] }),
  ] })] })] });
const logo = fs.readFileSync('logo.png');
const doc = new Document({
  styles: { default: { document: { run: { font: FONT } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, bottom: 900, left: 1080, right: 1080 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 4 } },
      children: [new TextRun({ text: 'Belief Counseling  ·  © 2026 Brian Campbell, Ph.D.  ·  Page ', font: FONT, size: 16, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: MUTED })] })] }) },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 68, height: 90 }, altText: { title: 'Belief Counseling logo', description: 'Belief Counseling logo: a cross before a rising sun', name: 'logo' } })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: 'Parental Messages Checklist', font: FONT, size: 40, bold: true, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 220 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } },
        children: [new TextRun({ text: 'By Brian Campbell, Ph.D.  ·  © 2026 Brian Campbell, Ph.D. All rights reserved.', font: FONT, size: 20, italics: true, color: MUTED })] }),
      new Paragraph({ spacing: { after: 200 }, tabStops: [{ type: TabStopType.LEFT, position: 6600 }], children: [r('Name: ________________________________________', { bold: true, color: NAVY }), r('\tDate: ________________', { bold: true, color: NAVY })] }),
      instr,
      new Paragraph({ spacing: { before: 200, after: 100 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 4 } }, children: [new TextRun({ text: 'My parents or caretakers…', font: FONT, size: 26, bold: true, color: NAVY })] }),
      list,
    ] }] });
Packer.toBuffer(doc).then(b => fs.writeFileSync('Parental_Messages_Checklist.docx', b));
