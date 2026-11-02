// Builds "The Mentally Healthy Christian" (from Christlike: Walking the Walk), Berean Standard Bible version.
// Usage (from repo root): NODE_PATH=$(npm root -g) node tools/build_mentally_healthy_christian.js <data.json> <out.docx>
// data.json: [{page, prose:[text with ^n^ note numbers], verses:[{n, ref, text}]}]
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle, Footer, PageNumber,
  Bookmark, InternalHyperlink, Table, TableRow, TableCell, WidthType, ShadingType } = require('docx');
const NAVY = '12284C', GOLD = 'C9A227', CREAM = 'FAF6EC', MUTED = '5B6678', INK = '1F2A3A', LINK = '1D3A6B';
const FONT = 'Georgia';
const data = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const r = (text, o = {}) => new TextRun({ text, font: FONT, size: 23, color: INK, ...o });
const first = (n) => n.split(/[,\-–]/)[0];

function prosePara(t) {
  const kids = [];
  t.split(/(\^[^^]+\^)/).filter(Boolean).forEach((part) => {
    if (part.startsWith('^')) {
      const n = part.slice(1, -1);
      kids.push(new InternalHyperlink({ anchor: 'v' + first(n), children: [new TextRun({ text: n, font: FONT, size: 23, superScript: true, color: LINK })] }));
    } else kids.push(r(part));
  });
  return new Paragraph({ spacing: { after: 140, line: 320 }, children: kids });
}

const W = 10080;
function verseBox(verses) {
  const kids = verses.map((v) => new Paragraph({ spacing: { after: 110 }, children: [
    new Bookmark({ id: 'v' + first(v.n), children: [new TextRun({ text: v.n + '  ', font: FONT, size: 18, bold: true, color: GOLD })] }),
    r('“' + v.text + '”', { italics: true, size: 21 }), r('  (' + v.ref + ')', { bold: true, size: 19, color: NAVY })] }));
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], rows: [new TableRow({ children: [new TableCell({
    width: { size: W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: CREAM },
    margins: { top: 140, bottom: 60, left: 220, right: 220 },
    borders: { top: { style: BorderStyle.SINGLE, size: 4, color: 'E3DCC6' }, bottom: { style: BorderStyle.SINGLE, size: 4, color: 'E3DCC6' },
      right: { style: BorderStyle.SINGLE, size: 4, color: 'E3DCC6' }, left: { style: BorderStyle.SINGLE, size: 24, color: GOLD } },
    children: kids })] })] });
}

const body = [];
data.forEach((pg) => {
  pg.prose.forEach((t) => body.push(prosePara(t)));
  if (pg.verses.length) { body.push(verseBox(pg.verses)); body.push(new Paragraph({ spacing: { after: 200 }, children: [] })); }
});

const logo = fs.readFileSync('belief-counseling-logo.png');
const doc = new Document({
  creator: 'Brian Campbell, Ph.D.', title: 'The Mentally Healthy Christian',
  styles: { default: { document: { run: { font: FONT, size: 23 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, bottom: 900, left: 1080, right: 1080 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 4 } },
      children: [new TextRun({ text: 'The Mentally Healthy Christian  ·  © 2026 Brian Campbell, Ph.D.  ·  Page ', font: FONT, size: 16, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: MUTED })] })] }) },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 68, height: 90 }, altText: { title: 'Belief Counseling logo', description: 'Belief Counseling logo: a cross before a rising sun', name: 'logo' } })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [new TextRun({ text: 'From the book Christlike: Walking the Walk', font: FONT, size: 22, italics: true, color: MUTED })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: 'The Mentally Healthy Christian', font: FONT, size: 44, bold: true, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [r('“But we have the mind of Christ.”', { italics: true })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [r('(1 Corinthians 2:16)', { bold: true, size: 19, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } },
        children: [new TextRun({ text: 'Dr. Brian Campbell, in collaboration with Rev. Jim Angelakos  ·  © 2026 Brian Campbell, Ph.D. All rights reserved.', font: FONT, size: 19, italics: true, color: MUTED })] }),
      ...body,
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 6 } },
        children: [new TextRun({ text: 'Scripture quotations are from the Berean Standard Bible (BSB), public domain. The small numbers in the text link to the Scripture that supports each statement.', font: FONT, size: 18, italics: true, color: MUTED })] }),
    ] }] });
Packer.toBuffer(doc).then((b) => fs.writeFileSync(process.argv[3], b));
