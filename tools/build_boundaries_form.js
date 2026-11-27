const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,ShadingType,BorderStyle,AlignmentType,ImageRun,Footer,PageNumber,LevelFormat,PageBreak,HeightRule,VerticalAlign}=require('docx');
const NAVY='12284C',INK='1F2A3A',MUT='5B6678',GOLD='C9A227',CREAM='FAF6EC',LINE='D8CDB7';
const F='Georgia';
const W=10080;
const t=(text,o={})=>new TextRun({text,font:F,size:o.size||20,bold:o.bold,italics:o.it,color:o.color||INK});
const p=(runs,o={})=>new Paragraph({children:Array.isArray(runs)?runs:[t(runs,o)],alignment:o.align,spacing:{before:o.before||0,after:o.after===undefined?80:o.after,line:o.line||264},keepNext:o.keepNext,numbering:o.num?{reference:'b',level:0}:undefined});
const H=(n,title,pb)=>new Paragraph({pageBreakBefore:!!pb,keepNext:true,spacing:{before:150,after:70},border:{bottom:{style:BorderStyle.SINGLE,size:6,color:GOLD,space:2}},children:[new TextRun({text:n?n+'.  ':'',font:F,size:24,bold:true,color:GOLD}),new TextRun({text:title,font:F,size:24,bold:true,color:NAVY})]});
const b={style:BorderStyle.SINGLE,size:4,color:LINE};const borders={top:b,bottom:b,left:b,right:b};
const nob={style:BorderStyle.NONE,size:0,color:'FFFFFF'};const noborders={top:nob,bottom:nob,left:nob,right:nob};
const cell=(children,w,o={})=>new TableCell({width:{size:w,type:WidthType.DXA},borders:o.nob?noborders:borders,shading:o.fill?{type:ShadingType.CLEAR,color:'auto',fill:o.fill}:undefined,margins:o.nob?{top:15,bottom:15,left:110,right:110}:{top:50,bottom:50,left:110,right:110},verticalAlign:VerticalAlign.CENTER,children:Array.isArray(children)?children:[children]});
const row=(cells,h)=>new TableRow({children:cells,cantSplit:true,height:h?{value:h,rule:HeightRule.ATLEAST}:undefined});
const table=(widths,rows)=>new Table({width:{size:W,type:WidthType.DXA},columnWidths:widths,rows});
const lab=(s)=>p([t(s,{bold:true,color:NAVY,size:19})],{after:0});
const blank=()=>p('',{after:0});
// helpers
function checks(items){const rows=[];for(let i=0;i<items.length;i+=2){rows.push(row([cell(p('☐  '+items[i],{after:0}),W/2,{nob:1}),cell(p(items[i+1]?'☐  '+items[i+1]:'',{after:0}),W/2,{nob:1})]));}return table([W/2,W/2],rows);}
const other=()=>table([2200,W-2200],[row([cell(lab('Other (please specify)'),2200,{fill:CREAM}),cell(blank(),W-2200)],420)]);
const logo=new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[new ImageRun({type:'png',data:fs.readFileSync('logo.png'),transformation:{width:54,height:72}})]});
const kids=[
 logo,
 p([new TextRun({text:'Therapeutic Boundaries Consent',font:F,size:36,bold:true,color:NAVY})],{align:AlignmentType.CENTER,after:40}),
 p([t('Understanding the professional counseling relationship',{it:1,color:MUT,size:19})],{align:AlignmentType.CENTER,after:160}),
 new Paragraph({spacing:{after:120},border:{top:{style:BorderStyle.SINGLE,size:8,color:GOLD,space:4}},children:[]}),
 table([2300,2740,2300,2740],[
  row([cell(lab('Client name'),2300,{fill:CREAM}),cell(blank(),2740),cell(lab('Counselor'),2300,{fill:CREAM}),cell(blank(),2740)],420)]),
 p('As part of our commitment to providing a safe, respectful, and effective therapeutic environment, the following clarifies the boundaries of the professional counseling relationship. Please read each statement and check the box to show that you understand it.',{before:120,after:60}),
 ...[
  ['A professional relationship','The counseling relationship is a professional, not a personal, relationship. All interactions between the counselor and client must remain within the scope of therapy. No additional relationships (for example, friendships, business relationships, or romantic relationships) should be sought or initiated by the counselor or the client.'],
  ['Physical contact','Physical contact beyond a handshake is not part of the therapeutic process. It will not be initiated by the counselor and should not be initiated by the client.'],
  ['Contact outside of sessions','Any communication outside of the counseling session (for example, phone or email) is limited to practical matters such as scheduling. No personal or private conversations should be sought or engaged in by the counselor or the client.'],
  ['Sexual topics and conduct','Although sexual topics may be part of the counseling process, the client and the counselor must completely refrain from any attempt to be sexually provocative or seductive, or to encourage or initiate a romantic or physical relationship.'],
  ['Modest attire','To promote a professional relationship, clients are asked to wear modest attire and to refrain from wearing clothes that may be considered sexually provocative or seductive.'],
  ['Raising concerns','If at any point you feel uncomfortable or unclear about the boundaries of our relationship, you are encouraged to raise this in session.'],
  ['Firm boundaries','Your counselor is ethically obligated to maintain firm professional boundaries. Any behavior by the client that may be perceived as sexually suggestive or provocative may lead to ending the counseling relationship and referral to another counselor, after appropriate discussion with you, the client.'],
 ].map(([h,b2],i)=>table([620,W-620],[row([cell(p([t('☐',{size:26,color:NAVY})],{align:AlignmentType.CENTER,after:0}),620,{nob:1}),cell(p([t((i+1)+'.  '+h+'.  ',{bold:1,color:NAVY}),t(b2)],{after:0}),W-620,{nob:1})])])).flatMap(x=>[x,new Paragraph({spacing:{before:0,after:0,line:120},children:[]})]),
 H('','Signatures'),
 p('I have read this form, or had it read to me, have had the chance to ask questions, and I understand and agree to the boundaries of the counseling relationship described above.'),
 table([3000,4380,700,2000],[
  row([cell(lab('Client signature'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],500),
  row([cell(lab('Client initials'),3000,{fill:CREAM}),new TableCell({columnSpan:3,width:{size:7080,type:WidthType.DXA},borders,margins:{top:60,bottom:60,left:110,right:110},children:[blank()]})],480),
  row([cell(lab('Counselor signature'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],500)]),
 new Paragraph({spacing:{before:200,after:0},shading:{type:ShadingType.CLEAR,color:'auto',fill:CREAM},border:{left:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:6}},children:[t('Sample form. ',{bold:1,color:NAVY,size:18}),t('Add your practice name and adapt the wording to your practice. Have the form reviewed for the laws and ethics code of your state and profession before you use it.',{size:18})]}),
];
const doc=new Document({
 styles:{default:{document:{run:{font:F,size:20,color:INK}}}},
 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:900,right:1080,bottom:900,left:1080}}},
  footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,border:{top:{style:BorderStyle.SINGLE,size:4,color:LINE,space:4}},children:[new TextRun({text:'Belief Counseling · Therapeutic Boundaries Consent (sample form) · © 2026 Brian Campbell, Ph.D. · Page ',font:F,size:15,color:MUT}),new TextRun({children:[PageNumber.CURRENT],font:F,size:15,color:MUT})]})]})},
  children:kids}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync('Belief-Counseling-Therapeutic-Boundaries-Consent.docx',b));
