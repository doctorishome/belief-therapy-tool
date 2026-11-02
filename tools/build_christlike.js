// Builds the "Christlike Characteristics of a Mentally Healthy Christian" reference (Word).
// Data: characteristics, expressions and Berean Standard Bible verse text in a JSON file.
// Usage (from repo root): NODE_PATH=$(npm root -g) node tools/build_christlike.js <data.json> <out.docx>
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle, Table, TableRow, TableCell,
  WidthType, ShadingType, Footer, PageNumber, Bookmark, InternalHyperlink, HeadingLevel } = require('docx');
const NAVY = '12284C', GOLD = 'C9A227', CREAM = 'FAF6EC', MUTED = '5B6678', INK = '1F2A3A', LINK = '1D3A6B';
const FONT = 'Georgia';
const data = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3];
const slug = (s) => 'c_' + s.toLowerCase().replace(/[^a-z]+/g, '_');
const r = (text, o = {}) => new TextRun({ text, font: FONT, size: 22, color: INK, ...o });
const link = (anchor, text, o = {}) => new InternalHyperlink({ anchor, children: [new TextRun({ text, font: FONT, size: 20, color: LINK, underline: {}, ...o })] });
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const thin = { style: BorderStyle.SINGLE, size: 4, color: 'E3DCC6' };
const W = 10080, C1 = 2600, C2 = W - C1;

// Index table: characteristic -> its Scriptures, all linking down to the section
const head = new TableRow({ tableHeader: true, children: ['Characteristic', 'Scriptures (click to go to the characteristic)'].map((t, i) => new TableCell({
  width: { size: i ? C2 : C1, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: NAVY },
  margins: { top: 60, bottom: 60, left: 100, right: 100 },
  children: [new Paragraph({ children: [new TextRun({ text: t, font: FONT, size: 20, bold: true, color: 'FFFFFF' })] })] })) });
const idxRows = data.rows.map((row, k) => {
  const a = slug(row.name);
  const refs = [];
  row.verses.forEach((v, i) => { if (i) refs.push(new TextRun({ text: '  ·  ', font: FONT, size: 20, color: GOLD })); refs.push(link(a, v.ref)); });
  const fill = k % 2 ? 'FFFFFF' : CREAM;
  return new TableRow({ cantSplit: true, children: [
    new TableCell({ width: { size: C1, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill }, margins: { top: 50, bottom: 50, left: 100, right: 100 },
      borders: { top: thin, bottom: thin, left: thin, right: thin }, children: [new Paragraph({ children: [link(a, row.name, { bold: true, color: NAVY })] })] }),
    new TableCell({ width: { size: C2, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill }, margins: { top: 50, bottom: 50, left: 100, right: 100 },
      borders: { top: thin, bottom: thin, left: thin, right: thin }, children: [new Paragraph({ children: refs })] }),
  ] });
});
const index = new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [C1, C2], rows: [head, ...idxRows] });

// One section per characteristic
const sections = [];
data.rows.forEach((row) => {
  sections.push(new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, spacing: { before: 320, after: 80 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD, space: 3 } },
    children: [new Bookmark({ id: slug(row.name), children: [new TextRun({ text: row.name, font: FONT, size: 30, bold: true, color: NAVY })] })] }));
  sections.push(new Paragraph({ keepNext: true, spacing: { after: 60 }, children: [r('Christlike expression: ', { bold: true, color: NAVY }), r(row.christ)] }));
  sections.push(new Paragraph({ keepNext: true, spacing: { after: 120 }, children: [r('Mental-health expression: ', { bold: true, color: NAVY }), r(row.mh)] }));
  row.verses.forEach((v) => sections.push(new Paragraph({ spacing: { after: 90 }, indent: { left: 280 },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 8 } },
    children: [r(v.ref + '  ', { bold: true, color: NAVY }), r('“' + v.text + '”', { italics: true })] })));
  sections.push(new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { before: 40, after: 60 }, children: [link('top', '↑ Back to top')] }));
});

const logo = fs.readFileSync('belief-counseling-logo.png');
const doc = new Document({
  creator: 'Brian Campbell, Ph.D.', title: 'Christlike Characteristics of a Mentally Healthy Christian',
  styles: { default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 30, bold: true, color: NAVY }, paragraph: { spacing: { before: 300, after: 120 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 28, bold: true, color: NAVY }, paragraph: { outlineLevel: 1 } }] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, bottom: 900, left: 1080, right: 1080 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 4 } },
      children: [new TextRun({ text: 'Belief Counseling  ·  © 2026 Brian Campbell, Ph.D.  ·  Page ', font: FONT, size: 16, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: MUTED })] })] }) },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [new Bookmark({ id: 'top', children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 68, height: 90 }, altText: { title: 'Belief Counseling logo', description: 'Belief Counseling logo: a cross before a rising sun', name: 'logo' } })] })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: 'Christlike Characteristics of a Mentally Healthy Christian', font: FONT, size: 38, bold: true, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: 'An alphabetical reference with five supporting Scriptures for each characteristic', font: FONT, size: 24, italics: true, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 220 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } },
        children: [new TextRun({ text: 'From Christlike: Walking the Walk  ·  By Brian Campbell, Ph.D.  ·  © 2026 Brian Campbell, Ph.D. All rights reserved.', font: FONT, size: 19, italics: true, color: MUTED })] }),
      new Paragraph({ spacing: { after: 100 }, children: [r('Purpose. ', { bold: true, color: NAVY }), r(data.purpose.replace(/^Purpose\.\s*/, '').replace('quoted from the source book', 'from Scripture'))] }),
      new Paragraph({ spacing: { after: 100 }, children: [r('Scripture note. ', { bold: true, color: NAVY }), r('Scripture quotations are from the Berean Standard Bible (BSB), public domain. Each passage is quoted in full.')] }),
      new Paragraph({ spacing: { after: 160 }, children: [r('How to use this index. ', { bold: true, color: NAVY }), r('Click a characteristic or any of its Scriptures to go to that characteristic. Each one ends with a “Back to top” link that returns here.')] }),
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: 'Scripture Index', font: FONT, size: 30, bold: true, color: NAVY })] }),
      index,
      new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun({ text: 'The Characteristics', font: FONT, size: 30, bold: true, color: NAVY })] }),
      ...sections,
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: 'Concluding Synthesis', font: FONT, size: 30, bold: true, color: NAVY })] }),
      ...data.concl.map((t) => new Paragraph({ spacing: { after: 120 }, children: [r(t)] })),
      new Paragraph({ alignment: AlignmentType.RIGHT, children: [link('top', '↑ Back to top')] }),
    ] }] });
Packer.toBuffer(doc).then((b) => fs.writeFileSync(out, b));
