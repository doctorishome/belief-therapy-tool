const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,ShadingType,BorderStyle,AlignmentType,ImageRun,Footer,PageNumber,LevelFormat,PageBreak,HeightRule,VerticalAlign}=require('docx');
const NAVY='12284C',INK='1F2A3A',MUT='5B6678',GOLD='C9A227',CREAM='FAF6EC',LINE='D8CDB7';
const F='Georgia';
const W=10080;
const t=(text,o={})=>new TextRun({text,font:F,size:o.size||20,bold:o.bold,italics:o.it,color:o.color||INK});
const p=(runs,o={})=>new Paragraph({children:Array.isArray(runs)?runs:[t(runs,o)],alignment:o.align,spacing:{before:o.before||0,after:o.after===undefined?100:o.after,line:o.line||276},keepNext:o.keepNext,numbering:o.num?{reference:'b',level:0}:undefined});
const H=(n,title,pb)=>new Paragraph({pageBreakBefore:!!pb,keepNext:true,spacing:{before:220,after:80},border:{bottom:{style:BorderStyle.SINGLE,size:6,color:GOLD,space:2}},children:[new TextRun({text:n?n+'.  ':'',font:F,size:24,bold:true,color:GOLD}),new TextRun({text:title,font:F,size:24,bold:true,color:NAVY})]});
const b={style:BorderStyle.SINGLE,size:4,color:LINE};const borders={top:b,bottom:b,left:b,right:b};
const nob={style:BorderStyle.NONE,size:0,color:'FFFFFF'};const noborders={top:nob,bottom:nob,left:nob,right:nob};
const cell=(children,w,o={})=>new TableCell({width:{size:w,type:WidthType.DXA},borders:o.nob?noborders:borders,shading:o.fill?{type:ShadingType.CLEAR,color:'auto',fill:o.fill}:undefined,margins:{top:60,bottom:60,left:110,right:110},verticalAlign:VerticalAlign.CENTER,children:Array.isArray(children)?children:[children]});
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
  row([cell(lab('Client ID (if applicable)'),2300,{fill:CREAM}),cell(blank(),2740),cell(lab('Counselor/Psychologist'),2300,{fill:CREAM}),cell(blank(),2740)],420),
  row([cell(lab('Agency/Practice name'),2300,{fill:CREAM}),new TableCell({columnSpan:3,width:{size:7780,type:WidthType.DXA},borders,margins:{top:60,bottom:60,left:110,right:110},children:[blank()]})],420)]),
 p([t('Purpose: ',{bold:1,color:NAVY}),t('This form allows [Agency/Practice Name] to release and disclose confidential information about the client named above, in compliance with legal, ethical, and HIPAA requirements.')],{before:140}),
 H('1','Information to Be Released'),
 p('Please check the specific information to be released (check all that apply):'),
 checks(['Assessment reports','Progress notes / treatment summaries','Psychological evaluations','Diagnosis information','Session notes','Treatment plans','Medical records / history','Academic or educational records','Communication with other healthcare providers']),
 other(),
 H('2','Purpose of the Release'),
 p('Please check the reason(s) for releasing this information (check all that apply):'),
 checks(['Continuity of care / coordination with other providers','Insurance or billing','Legal proceedings (for example, court or attorney)','Personal use by the client','Academic or educational purposes','Referral to other providers or services']),
 other(),
 H('3','Authorized Recipients',1),
 p('I authorize the release of the information above to the following individuals, organizations, or agencies:'),
 table([3400,4080,2600],[
  row([cell(lab('Name'),3400,{fill:CREAM}),cell(lab('Address'),4080,{fill:CREAM}),cell(lab('Phone / email'),2600,{fill:CREAM})]),
  row([cell(blank(),3400),cell(blank(),4080),cell(blank(),2600)],480),
  row([cell(blank(),3400),cell(blank(),4080),cell(blank(),2600)],480),
  row([cell(blank(),3400),cell(blank(),4080),cell(blank(),2600)],480)]),
 H('4','Expiration of Authorization'),
 p('This authorization will expire on the following date or event (for example, “one year from the date of signature” or “upon completion of treatment”):'),
 table([2600,W-2600],[row([cell(lab('Expiration date or event'),2600,{fill:CREAM}),cell(blank(),W-2600)],440)]),
 H('5','Revocation of Authorization'),
 p('I understand that I have the right to revoke this authorization at any time by submitting a written request to my counselor/psychologist. I understand that any disclosures made before my revocation will not be affected by it.'),
 H('6','Legal and Ethical Considerations'),
 p('I understand that my counselor/psychologist is bound by professional ethics and federal law (including HIPAA) to maintain confidentiality, except in specific situations where disclosure is legally mandated. These include, but are not limited to:'),
 ...['Risk of harm to myself or others (for example, suicide or homicide)','Known or suspected abuse or neglect of a child, an elder, or a vulnerable person','Legal requirements (for example, court orders or subpoenas)','Reporting of certain communicable diseases (for example, sexually transmitted diseases)','As permitted by HIPAA for treatment, payment, and healthcare operations'].map(x=>p(x,{num:1,after:40})),
 p('I understand that the release of my Protected Health Information (PHI) will be limited to the minimum necessary to achieve the purpose of the disclosure, as required by HIPAA.',{before:80}),
 H('7','Acknowledgment of Understanding'),
 p('I acknowledge that I have been informed of my rights regarding confidentiality and the release of information. I have read and understood the terms of this authorization. By signing this form, I authorize the release of the specified confidential information as outlined above.'),
 table([3000,4380,700,2000],[
  row([cell(lab('Client signature'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],560),
  row([cell(lab('Parent/guardian signature (if applicable)'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],560),
  row([cell(lab('Counselor/Psychologist signature'),3000,{fill:CREAM}),cell(blank(),4380),cell(lab('Date'),700,{fill:CREAM}),cell(blank(),2000)],560)]),
 new Paragraph({spacing:{before:200,after:0},shading:{type:ShadingType.CLEAR,color:'auto',fill:CREAM},border:{left:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:6}},children:[t('Notice to recipient: ',{bold:1,color:NAVY,size:19}),t('The information disclosed to you is confidential and protected under federal and state laws. You are not permitted to redisclose this information without the specific written consent of the client or as required by law.',{size:19})]}),
 new Paragraph({children:[new PageBreak()]}),
 p([new TextRun({text:'For the Counselor',font:F,size:30,bold:true,color:NAVY})],{after:40}),
 p([t('Remove this page before giving the form to a client.',{it:1,color:MUT})],{after:160}),
 H('','Disclaimer'),
 p('This sample is not a legal document. It is presented for educational purposes only. Although an attempt has been made to illustrate a tool that complies with some of the legal requirements for the release of confidential information, the document may not be complete or it may contain errors. It incorporates legal and ethical requirements based on the ACA, APA, and HIPAA guidelines.'),
 H('','Additional Considerations'),
 ...[['HIPAA compliance: ','Make sure the form meets HIPAA’s Privacy Rule requirements, such as specifying the scope of the information being released, the purpose of the release, and the client’s right to revoke consent.'],['State-specific laws: ','Adapt the form as needed to comply with any additional state confidentiality laws or mandates.'],['Expiration of consent: ','Always specify an expiration date or event, so the authorization does not continue indefinitely without the client’s consent.']].map(([a,b])=>p([t(a,{bold:1,color:NAVY}),t(b)],{num:1,after:60})),
 p([t('This form should be reviewed by legal counsel to make sure it complies with all relevant laws in your jurisdiction.',{bold:1})],{before:120}),
];
const doc=new Document({
 numbering:{config:[{reference:'b',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:540,hanging:270}}}}]}]},
 styles:{default:{document:{run:{font:F,size:20,color:INK}}}},
 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:900,right:1080,bottom:900,left:1080}}},
  footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,border:{top:{style:BorderStyle.SINGLE,size:4,color:LINE,space:4}},children:[new TextRun({text:'Belief Counseling · Release of Confidential Information (sample form) · © 2024 Brian Campbell, Ph.D. · Page ',font:F,size:15,color:MUT}),new TextRun({children:[PageNumber.CURRENT],font:F,size:15,color:MUT})]})]})},
  children:kids}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync('Belief-Counseling-Release-of-Confidential-Information.docx',b));
