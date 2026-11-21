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
// two-column checkbox list
function checks(items){const rows=[];for(let i=0;i<items.length;i+=2){rows.push(row([cell(p('☐  '+items[i],{after:0}),W/2,{nob:1}),cell(p(items[i+1]?'☐  '+items[i+1]:'',{after:0}),W/2,{nob:1})]));}return table([W/2,W/2],rows);}
const other=()=>table([2200,W-2200],[row([cell(lab('Other (please specify)'),2200,{fill:CREAM}),cell(blank(),W-2200)],420)]);
const logo=new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[new ImageRun({type:'png',data:fs.readFileSync('logo.png'),transformation:{width:54,height:72}})]});
const kids=[
 logo,
 p([new TextRun({text:'Release of Confidential Information',font:F,size:36,bold:true,color:NAVY})],{align:AlignmentType.CENTER,after:40}),
 p([t('Authorization for the release of confidential information',{it:1,color:MUT,size:19})],{align:AlignmentType.CENTER,after:160}),
 new Paragraph({spacing:{after:120},border:{top:{style:BorderStyle.SINGLE,size:8,color:GOLD,space:4}},children:[]}),
 table([2300,2740,2300,2740],[
  row([cell(lab('Client name'),2300,{fill:CREAM}),cell(blank(),2740),cell(lab('Date of birth'),2300,{fill:CREAM}),cell(blank(),2740)],420),
  row([cell(lab('Other names used (if any)'),2300,{fill:CREAM}),cell(blank(),2740),cell(lab('Client ID (if applicable)'),2300,{fill:CREAM}),cell(blank(),2740)],420)]),
 H('1','Who May Release the Information'),
 p('I authorize the following practice and counselor to release my information:'),
 table([2300,2740,2300,2740],[
  row([cell(lab('Practice name'),2300,{fill:CREAM}),cell(blank(),2740),cell(lab('Counselor'),2300,{fill:CREAM}),cell(blank(),2740)],420),
  row([cell(lab('Address'),2300,{fill:CREAM}),new TableCell({columnSpan:3,width:{size:7780,type:WidthType.DXA},borders,margins:{top:60,bottom:60,left:110,right:110},children:[blank()]})],420)]),
 H('2','Who May Receive the Information'),
 p('The information may be released to:'),
 table([3400,4080,2600],[
  row([cell(lab('Name or organization'),3400,{fill:CREAM}),cell(lab('Address'),4080,{fill:CREAM}),cell(lab('Phone / fax / email'),2600,{fill:CREAM})]),
  row([cell(blank(),3400),cell(blank(),4080),cell(blank(),2600)],480),
  row([cell(blank(),3400),cell(blank(),4080),cell(blank(),2600)],480)]),
 p([t('This is a ',{}),t('one-way',{bold:1}),t(' release (my counselor may send information) unless I check here:  ☐  ',{}),t('Two-way',{bold:1}),t(' (my counselor and the person above may share information with each other).')],{before:100}),
 H('3','Information to Be Released'),
 p('Please check the specific information to be released (check all that apply):'),
 checks(['Dates of attendance','Diagnosis','Assessment reports / test results','Psychological evaluations','Treatment plan','Treatment summary / discharge summary','Progress notes (general)','Medication information','Academic or educational records','Verbal discussion with the person named above']),
 other(),
 table([3000,W-3000],[row([cell(lab('Records dated (if limited)'),3000,{fill:CREAM}),cell(p('From  ______________________   to  ______________________',{after:0}),W-3000)],420)]),
 p([t('Specially protected information. ',{bold:1,color:NAVY}),t('Federal or state law gives some information extra protection. It is released only if I check the box and initial it here:')],{before:140}),
 table([7080,3000],[
  row([cell(p('☐  Alcohol or drug use treatment records',{after:0}),7080,{nob:1}),cell(p('Initials  ________',{after:0}),3000,{nob:1})]),
  row([cell(p('☐  HIV/AIDS-related information',{after:0}),7080,{nob:1}),cell(p('Initials  ________',{after:0}),3000,{nob:1})]),
  row([cell(p('☐  Genetic testing information',{after:0}),7080,{nob:1}),cell(p('Initials  ________',{after:0}),3000,{nob:1})])]),
 new Paragraph({spacing:{before:140,after:0},shading:{type:ShadingType.CLEAR,color:'auto',fill:CREAM},border:{left:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:6}},children:[t('Psychotherapy notes ',{bold:1,color:NAVY,size:19}),t('(a counselor’s private notes about what was said in sessions, kept apart from the rest of the record) are not released with this form. Releasing them requires a separate authorization.',{size:19})]}),
 H('4','Purpose of the Release'),
 p('Please check the reason(s) for releasing this information (check all that apply):'),
 checks(['Coordination of care with other providers','Referral to other providers or services','Insurance or billing','At my own request','School or educational planning','Legal proceedings (for example, court or attorney)']),
 other(),
 H('5','How the Information May Be Shared'),
 table([W/4,W/4,W/4,W/4],[row(['Mail','Fax','Secure email or portal','Phone or in person'].map(x=>cell(p('☐  '+x,{after:0}),W/4,{nob:1})))]),
 H('6','When This Authorization Ends'),
 p('This authorization ends on the date or event written below (for example, “one year from the date I sign” or “when my treatment ends”). If nothing is written, it ends one year from the date I sign.'),
 table([2600,W-2600],[row([cell(lab('End date or event'),2600,{fill:CREAM}),cell(blank(),W-2600)],440)]),
 H('7','My Rights'),
 ...[['I may revoke (cancel) this authorization at any time ','by giving a written request to the practice named in Section 1. Revoking it does not undo information already released while it was in effect.'],['My treatment does not depend on signing. ','My counselor will not refuse treatment, payment, or eligibility for services because I decline to sign this form.'],['Information may be passed on. ','Once information is released, the person who receives it may share it again, and federal privacy law (HIPAA) may no longer protect it. Some state laws and federal rules for alcohol and drug treatment records still limit sharing it again.'],['I may have a copy ','of this signed form, and I may ask to see or receive a copy of the information that is released.']].map(([a,b])=>p([t(a,{bold:1,color:NAVY}),t(b)],{num:1,after:60})),
 H('8','Signatures'),
 p('I have read this form, or had it read to me, and I understand it. I authorize the release of the information described above.'),
 table([3000,4380,700,2000],[
  row([cell(lab('Client signature'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],500),
  row([cell(lab('Parent, guardian, or legal representative (if the client cannot sign)'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],500),
  row([cell(lab('Printed name and relationship to client'),3000,{fill:CREAM}),new TableCell({columnSpan:3,width:{size:7080,type:WidthType.DXA},borders,margins:{top:60,bottom:60,left:110,right:110},children:[blank()]})],480),
  row([cell(lab('Witness / counselor signature'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],500)]),
 p([t('Revoked on: ',{bold:1,color:NAVY,size:18}),t('______________________     Staff initials: __________',{size:18})],{before:120}),
 new Paragraph({spacing:{before:160,after:0},shading:{type:ShadingType.CLEAR,color:'auto',fill:CREAM},border:{left:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:6}},children:[t('Notice to recipient: ',{bold:1,color:NAVY,size:19}),t('This information is confidential. It is released to you only for the purpose stated above. Please do not share it further unless the client gives written permission or the law requires it.',{size:19})]}),
 new Paragraph({children:[new PageBreak()]}),
 p([new TextRun({text:'For the Counselor',font:F,size:30,bold:true,color:NAVY})],{after:40}),
 p([t('Remove this page before giving the form to a client.',{it:1,color:MUT})],{after:160}),
 H('','Disclaimer'),
 p('This sample is not a legal document. It is presented for educational purposes only. Although an attempt has been made to illustrate a tool that complies with some of the legal requirements for the release of confidential information, the document may not be complete or it may contain errors. It incorporates legal and ethical requirements based on the ACA, APA, and HIPAA guidelines.'),
 H('','Additional Considerations'),
 ...[['HIPAA authorization: ','Under 45 CFR 164.508, a valid release must describe the information, name who may release it and who may receive it, state the purpose, give an end date or event, and be signed and dated. It must also tell the client about the right to revoke, that treatment does not depend on signing, and that released information may be shared again. A form missing any of these is not valid.'],['Psychotherapy notes: ','A counselor’s separate private session notes need their own authorization and cannot be combined with this form. Most requests (insurers, other providers, schools) are met with a treatment summary instead.'],['Alcohol and drug treatment records: ','Records from a federally assisted substance use program are covered by 42 CFR Part 2, which has its own consent and redisclosure-notice rules. Use a Part 2 consent form for those records.'],['Minors and representatives: ','State law decides who signs for a minor or for an adult with a guardian. Write the signer’s relationship and keep a copy of any guardianship or court papers.'],['Limits of confidentiality: ','Duty-to-warn, abuse reporting, and court-order exceptions belong in the Confidentiality Agreement in the New Client Packet, not on this release.'],['Keep the record: ','Give the client a copy, keep the signed original in the chart for at least six years (HIPAA), and note any revocation on the form.'],['State laws: ','Adapt the form for any additional state confidentiality rules (for example, rules for HIV, mental health, or school records).']].map(([a,b])=>p([t(a,{bold:1,color:NAVY}),t(b)],{num:1,after:60})),
 p([t('This form should be reviewed by legal counsel to make sure it complies with all relevant laws in your jurisdiction.',{bold:1})],{before:120}),
];
const doc=new Document({
 numbering:{config:[{reference:'b',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:540,hanging:270}}}}]}]},
 styles:{default:{document:{run:{font:F,size:20,color:INK}}}},
 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:900,right:1080,bottom:900,left:1080}}},
  footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,border:{top:{style:BorderStyle.SINGLE,size:4,color:LINE,space:4}},children:[new TextRun({text:'Belief Counseling · Release of Confidential Information (sample form) · © 2024 Brian Campbell, Ph.D. · Page ',font:F,size:15,color:MUT}),new TextRun({children:[PageNumber.CURRENT],font:F,size:15,color:MUT})]})]})},
  children:kids}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync('Belief-Counseling-Release-of-Confidential-Information.docx',b));
