"""Puts the agreements and consent forms on the on-screen New Client Forms page (counselors/new-client-forms.html).

    python3 tools/add_consent_forms.py

The wording is taken from sections 4 to 9 of the New Client Packet (counselors/forms/New-Client-Packet-fillable.pdf).
Edit CONSENT below and run again; the script replaces everything between the CONSENT markers in the page.
Field types: read (text to read: h heading, p paragraphs, l bullet list), check (a statement to agree to),
one / many (choices), text, date. req=1 means it must be answered.
"""
import json
import pathlib
import re

PAGE = pathlib.Path(__file__).resolve().parent.parent / "counselors" / "new-client-forms.html"


def read(h, p=(), l=()):
    return {"type": "read", "h": h, "p": list(p), "l": list(l)}


def check(k, t, req=1):
    return {"k": k, "t": t, "type": "check", "req": req}


def sign(prefix):
    return [{"k": prefix + "_sig", "t": "Printed name", "type": "text", "req": 1},
            {"k": prefix + "_pen", "t": "Signature", "type": "sig", "req": 1},
            {"k": prefix + "_date", "t": "Date", "type": "date", "req": 1}]


CONSENT = [
    {"group": "Agreements and Consent Forms",
     "note": "Please read each one and sign. Your counselor will go over them with you and answer any questions."},

    {"id": "c_treat", "name": "Informed Consent for Treatment", "time": "read and sign", "sections": [
        ["Please read", [
            read("Nature of counseling", ["Counseling is a collaborative process in which you and your counselor work together to understand your concerns and to make changes in thinking, feelings, behavior, relationships, and spiritual life. The first session(s) focus on assessment and setting goals together. Counseling often helps, but results cannot be guaranteed, and talking about painful matters may at times feel uncomfortable before it feels better."]),
            read("Faith-integrated approach", ["[Practice Name] offers Christian Belief Counseling, a cognitive-behavioral approach that helps identify beliefs that shape how you interpret life events and examine them for accuracy. For clients who desire it, biblical truth and Christian faith are integrated into counseling. Faith integration is your choice; you may ask for more, less, or none at any time, and you will be treated with respect whatever your beliefs."]),
            read("Confidentiality and its limits", ["What you share is kept confidential and is not released without your written permission, except in a few situations the law requires or permits (such as a serious risk of harm, suspected abuse or neglect, a court order, and insurance billing). These limits, and your choices about them, are explained in full in the Confidentiality and Limits of Confidentiality Agreement, which you will also sign. The uses for treatment, payment, and health-care operations are described in the Notice of Privacy Practices."]),
            read("Emergencies and after-hours", ["[Practice Name] is not a crisis service and messages are not monitored after hours. In an emergency, call 911 or go to the nearest emergency department. For a mental-health crisis, call or text 988. For non-urgent matters, call [Phone]; messages are returned within [one business day]."]),
            read("Counselor credentials", ["Your counselor's name, state of practice, license, and supervisor (if any) are listed at the start of the Confidentiality Agreement. You may ask about training and approach at any time."]),
            read("Your rights, including the right to stop", ["You have the right to ask questions, to take part in planning your treatment, to refuse any technique, and to stop counseling at any time. If you stop, a referral can be provided on request."]),
            read("Records", ["Records are kept securely and retained as required by law; the Confidentiality Agreement explains how long records are kept and who can see them."]),
        ]],
        ["Your consent", [
            check("c_treat_ok", "I have read this information, have had the opportunity to ask questions, and consent to counseling services with [Practice Name]."),
            *sign("c_treat")]],
    ]},

    {"id": "c_conf", "name": "Confidentiality and Limits of Confidentiality Agreement", "time": "read and sign",
     "intro": "Trust is the cornerstone of counseling. This agreement explains how I protect your privacy, the few times the law or ethics require me to share information, and your rights. We will go over it together, and you can ask questions at any time.",
     "sections": [
        ["Please read", [
            read("Your counselor", ["Counselor name, state of practice, license, and supervisor (if any): [filled in by the practice]."]),
            read("1. What confidentiality means", ["All interactions that take place in counseling are considered confidential. This includes phone calls and messages, scheduling notes, what you say in session, and my records and notes. I will not even confirm that you are my client unless you give me written permission. In almost all cases, I share information about you only when you give me written permission."]),
            read("2. Who can see your records", ["Your records are seen by me [and by office staff who help with scheduling and billing, who are trained in and bound by the same privacy rules]. If I practice under supervision, my supervisor may also see them. No one else sees them unless you give written permission or one of the exceptions in part 3 applies. If I keep separate personal session notes (“psychotherapy notes”), federal law (HIPAA) gives them extra protection, and they are not shared even with your insurance company without your separate written permission."]),
            read("3. When I may have to share information", ["These rules are based on the laws of the state where I provide counseling. I will keep what you share private except in these situations. When I must share, I share only what is truly necessary and, whenever it is safe and possible, I will talk with you first."], [
                "Danger to yourself. If I believe you are in serious and immediate danger of killing or seriously injuring yourself, I may contact your emergency contact, family members, or emergency services, or help arrange hospitalization, to keep you safe.",
                "Danger to others. If you threaten serious harm to another person, I may be required or permitted to warn that person, notify the police, or arrange hospitalization (often called the “duty to warn or protect”). [State] law sets the exact rules.",
                "Abuse or neglect of a child. If I learn of or suspect physical, sexual, or emotional abuse or neglect of anyone under 18, I must report it to child protective services. I do not have to be certain; reasonable suspicion is enough.",
                "Abuse of an elder or dependent adult. If I learn of or suspect abuse, neglect, or exploitation of an elder or a disabled or dependent adult, I must report it to the state agency that handles these reports.",
                "Court orders and subpoenas. If a judge orders me to release records or to testify, I may have to comply. I will ask for your written consent first, or work to limit what is shared as narrowly as possible. I will not hand over records just because an attorney asks; I will talk with you, and with an attorney if needed, before responding to any subpoena.",
                "Insurance billing. If you use insurance, I share only the minimum needed to be paid: usually your name, dates of service, type of service, and diagnosis, and sometimes a treatment summary if your plan requires it. If you pay in full yourself, you may ask me not to bill your insurance at all.",
                "Consultation and supervision. I may consult with other licensed professionals to give you the best care, without using your name or details that would identify you; they must also keep it confidential. If I practice under supervision, my supervisor may review your records and information as part of that supervision and is bound by the same confidentiality rules as I am.",
                "Emergencies. In a medical or mental-health emergency, I may share information that emergency responders need to help you.",
                "Other legal requirements. Rarely, other laws may require disclosure (for example, certain public-health reports, or if you file a complaint or lawsuit against me)."]),
            read("", ["Talking about a past crime, when no one is in ongoing danger, generally does not require a report. If you are an adult being hurt by a partner or family member, I usually cannot report it without your permission, but we will make a safety plan together."]),
            read("4. Faith-integrated counseling", ["Christian Belief Counseling may include prayer, Scripture, or conversation about faith, but only if you want it. You may ask for more, less, or none at any time, and you will be respected whatever your beliefs. I will not share anything about your counseling with your church, pastor, ministry leaders, or faith community, even if they referred you or help pay for counseling, unless you sign a written release."]),
            read("5. Couples and family counseling", ["When I see a couple or family together, the couple or family is “the client.” I cannot promise that other participants will keep what is said private. Records of joint sessions are released only with the written permission of every adult participant."]),
            {"k": "c_conf_couple", "t": "Couples and family counseling: please choose one", "type": "one", "req": 1, "opts": [
                "No-secrets policy: something one person tells me privately may be brought into joint sessions if it is important to our work",
                "Private information shared with me alone stays private unless it falls under part 3",
                "Not applicable: individual counseling"]},
            read("6. Email, text, phone, and video sessions", ["Email and text messages are convenient but not fully secure, and others may see them on your phone or computer. Please use them for scheduling only, not for personal or clinical details. Video sessions use a secure platform, but no technology is free of risk. Join from a private place, use your own device and a password-protected network (not public Wi-Fi), and do not record sessions. I do not provide counseling or crisis help by email or text."]),
            {"k": "c_conf_contact", "t": "You may contact me by", "type": "many", "opts": ["Phone call", "Voicemail", "Text", "Email"]},
            read("7. Technology and AI-assisted tools", ["I keep records in secure electronic software. I may also use secure software that includes AI-assisted tools, for example to help draft notes or paperwork, only under appropriate privacy and security safeguards and written agreements (such as a HIPAA business associate agreement). I will not enter information that identifies you into any tool without those safeguards. I do not use AI to diagnose you or to respond to a crisis, and I review and remain responsible for anything a tool produces. You may ask what tools I use, and you may decline AI-assisted tools without any effect on your care."]),
            {"k": "c_conf_ai", "t": "AI-assisted tools: my choice", "type": "one", "req": 1, "opts": ["AI-assisted note tools may be used as described", "Please do not use AI-assisted tools with my information"]},
            read("8. Records and how long they are kept", ["Your records are stored securely. I keep them for [__] years after our last session, as required by [State] rules, and then destroy them securely. If I become unable to practice, [Records Custodian name and contact] will safeguard your records and help you get a copy."]),
            read("9. Releasing information with your permission", ["Except as described in part 3, I release information only with your signed written authorization (a Release of Information form) that states what will be shared, with whom, why, and when the permission ends. You may cancel it in writing at any time, except for information already shared. I share only the minimum necessary, and I remind the person who receives it that they may not pass it on without your consent."]),
            read("10. Your rights", [], [
                "See and get a copy of your records, usually within 30 days of your request (personal psychotherapy notes are an exception).",
                "Ask me to correct your records, or to contact you only in certain ways or at certain places.",
                "Ask me to limit what I share. If you pay in full yourself, I will not share that care with your insurer unless the law requires it.",
                "Receive a copy of my Notice of Privacy Practices, and be told if your information is ever breached.",
                "Make a complaint to me, to the [State Licensing Board name, phone, website], or to the U.S. Department of Health and Human Services, Office for Civil Rights (www.hhs.gov/ocr/complaints, 1-800-368-1019). You will never be penalized for making a complaint."]),
            read("11. If you are in crisis", ["I am not a crisis service, and messages are not monitored after hours."], [
                "Emergency or immediate danger: call 911 or go to the nearest emergency room.",
                "988 Suicide & Crisis Lifeline: call or text 988, or chat at 988lifeline.org (free, 24/7; Veterans press 1).",
                "National Domestic Violence Hotline: 1-800-799-7233, or text START to 88788.",
                "Childhelp Child Abuse Hotline: 1-800-422-4453."]),
        ]],
        ["Please check each statement to show you understand it", [
            check("c_conf_1", "Safety. My counselor may share information to protect me or someone else from serious harm."),
            check("c_conf_2", "Abuse reporting. My counselor must report suspected abuse or neglect of a child, an elder, or a dependent adult."),
            check("c_conf_3", "Legal. A court order or other law may require my counselor to release information."),
            check("c_conf_4", "Insurance. If I use insurance, the minimum information needed for billing will be shared."),
            check("c_conf_5", "Consultation and supervision. My counselor may consult with professionals without using my name, and a supervisor (if any) may review my information under the same confidentiality rules."),
            check("c_conf_6", "Electronic. Email, text, and video have privacy risks, and I chose my contact methods above."),
            check("c_conf_7", "Technology. I understand how secure software and AI-assisted tools may be used, and I made my choice above."),
            check("c_conf_8", "Faith community. Nothing will be shared with my church or pastor without my written release.")]],
        ["Your signature", [
            check("c_conf_ok", "I have read this agreement, have had the chance to ask questions, and understand the nature and limits of confidentiality. I agree to begin counseling with this understanding."),
            *sign("c_conf")]],
    ]},

    {"id": "c_npp", "name": "Notice of Privacy Practices: Acknowledgment of Receipt", "time": "sign", "sections": [
        ["Acknowledgment", [
            check("c_npp_ok", "I acknowledge that I have received, or have been offered, a copy of the [Practice Name] Notice of Privacy Practices, which describes how my health information may be used and disclosed and how I can get access to it."),
            *sign("c_npp")]],
    ]},

    {"id": "c_fin", "name": "Financial Policy, Assignment of Benefits, and Authorization to Bill Insurance", "time": "read and sign", "sections": [
        ["Fees", [
            read("", [], ["Initial assessment session (90791): $[____]", "Individual session, 53+ minutes (90837): $[____]",
                          "Individual session, 38–52 minutes (90834): $[____]", "Late cancellation / no-show fee: $[____]"])]],
        ["Please check each item", [
            check("c_fin_1", "Payment, copays, coinsurance and deductibles are due at the time of each session. Accepted methods: [________]."),
            check("c_fin_2", "Insurance benefits are verified as a courtesy, but this is not a guarantee of payment. I am responsible for any amount my insurance does not pay, including denied claims and services not covered."),
            check("c_fin_3", "Cancellations need at least [24] hours' notice. Late cancellations and missed appointments (no-shows) are charged the fee above; insurance does not pay this fee."),
            check("c_fin_4", "Assignment of benefits: I authorize my insurance company to pay benefits directly to [Practice Name / counselor] for services provided."),
            check("c_fin_5", "Authorization to bill insurance: I authorize [Practice Name] to release the information needed to process my insurance claims, including diagnosis, dates of service, and treatment information."),
            check("c_fin_6", "Fees for other services (letters, reports, records copies, court-related work) are billed at $[____] per hour and are not covered by insurance.")]],
        ["Your signature", sign("c_fin")],
    ]},

    {"id": "c_tele", "name": "Telehealth Consent", "time": "only if you will have video or phone sessions", "sections": [
        ["Your choice", [
            {"k": "c_tele_use", "t": "Will you use telehealth?", "type": "one", "req": 1,
             "opts": ["I will NOT use telehealth", "I would like the option of telehealth"],
             "help": "If you will not use telehealth, choose that answer, sign at the bottom, and skip the rest."}]],
        ["If you would like the option of telehealth", [
            read("", ["Telehealth means counseling by secure video or phone instead of in person. It uses a HIPAA-compliant platform, but no technology is completely free of risk, such as interruptions or unauthorized access. I agree to:"], [
                "Be located in [State] during each session and tell my counselor my location at the start of each session.",
                "Use a private place where I will not be overheard, and not record sessions without mutual consent.",
                "If the connection fails, wait for the counselor to call me back at the number below.",
                "In an emergency during a session, my counselor may contact local emergency services at my location."]),
            {"k": "c_tele_phone", "t": "Call-back number if the connection fails", "type": "tel"},
            {"k": "c_tele_ec", "t": "Emergency contact near me (name and phone)", "type": "text"},
            read("", ["I understand that I may stop telehealth at any time and request in-person services, and that telehealth may not be right for every situation. Telehealth sessions follow the same fees, confidentiality, and policies as in-person sessions."])]],
        ["Your signature", sign("c_tele")],
    ]},

    {"id": "c_gfe", "name": "Good Faith Estimate Notice", "time": "self-pay or out-of-network clients", "sections": [
        ["Please read", [
            read("", ["Under the federal No Surprises Act, if you do not have health insurance, or you are not using insurance to pay for services, you have the right to receive a Good Faith Estimate of the expected cost of your care. You may ask for one before scheduling, and you will receive it in writing at least 1 business day before your first session. If you receive a bill that is at least $400 more than your Good Faith Estimate, you can dispute the bill. Make sure to save a copy of your Good Faith Estimate. For questions or more information, visit www.cms.gov/nosurprises or call 1-800-985-3059."]),
            {"k": "c_gfe_which", "t": "Which applies to you?", "type": "one", "req": 1,
             "opts": ["I am self-pay / out-of-network and have received a Good Faith Estimate", "Not applicable: I am using in-network insurance"]}]],
        ["Your signature", sign("c_gfe")],
    ]},

    {"id": "c_more", "name": "Release of Information and Client Handbook",
     "soon": "Being prepared. Your counselor will go over these with you."},
]

NEW_JS = r"""
function renderList(){
 let n=0;
 document.getElementById('list').innerHTML=FORMS.map(f=>{
  if(f.group)return `<h3 class="grp">${esc(f.group)}</h3>${f.note?`<p class="status">${esc(f.note)}</p>`:''}`;
  n++;
  if(f.soon)return `<div class="item"><p><b>${n}. ${esc(f.name)}</b></p><p class="soon">${esc(f.soon)}</p></div>`;
  return `<div class="item"><p><b>${n}. ${esc(f.name)}</b> ${done[f.id]?'<span class="done">✓ Done</span>':`<span class="status">(${f.time})</span>`}</p><button class="btn${done[f.id]?' light':''}" onclick="openForm('${f.id}')">${done[f.id]?'Review':'Start'}</button></div>`;}).join('');
 const t=FORMS.filter(f=>f.sections).length,d=Object.keys(done).length;
 document.getElementById('progress').textContent=`${d} of ${t} forms complete.`;
}
function field(q){
 if(q.type==='read')return `<div class="read">${q.h?`<h4>${esc(q.h)}</h4>`:''}${q.p.map(x=>`<p>${esc(x)}</p>`).join('')}${q.l.length?'<ul>'+q.l.map(x=>`<li>${esc(x)}</li>`).join('')+'</ul>':''}</div>`;
 const v=answers[q.k];const r=q.req?' <span class="req">*</span>':'';
 if(q.type==='check')return `<div class="f agree"><label><input type="checkbox" id="${q.k}" ${v?'checked':''}> <span>${esc(q.t)}${r}</span></label></div>`;
 let h=`<div class="f"><label class="t" for="${q.k}">${esc(q.t)}${r}</label>`;
 if(q.type==='long')h+=`<textarea id="${q.k}">${esc(v||'')}</textarea>`;
 else if(q.type==='one'||q.type==='many'){
  const ty=q.type==='one'?'radio':'checkbox';
  h+=`<div class="opts${q.yn?' yn':''}${q.opts.some(o=>o.length>40)?' wide':''}">`+q.opts.map(o=>{const on=q.type==='one'?v===o:(v||[]).includes(o);
   return `<label class="${on?'on':''}"><input type="${ty}" name="${q.k}" value="${esc(o)}" ${on?'checked':''} onchange="mark(this)">${esc(o)}</label>`;}).join('')+'</div>';}
 else h+=`<input type="${q.type}" id="${q.k}" value="${esc(v||'')}">`;
 if(q.help)h+=`<small>${esc(q.help)}</small>`;
 return h+'</div>';
}
"""


SIG_JS = r"""
function sigInit(){
 document.querySelectorAll('canvas.sig').forEach(c=>{
  const x=c.getContext('2d');x.lineWidth=2.2;x.lineCap='round';x.lineJoin='round';x.strokeStyle='#12284c';
  const old=answers[c.id];
  if(old){const im=new Image();im.onload=()=>x.drawImage(im,0,0);im.src=old;c.dataset.signed='1';}
  let down=false;
  const at=e=>{const r=c.getBoundingClientRect();return [(e.clientX-r.left)*c.width/r.width,(e.clientY-r.top)*c.height/r.height];};
  c.addEventListener('pointerdown',e=>{down=true;c.setPointerCapture(e.pointerId);const [a,b]=at(e);x.beginPath();x.moveTo(a,b);x.lineTo(a+.1,b+.1);x.stroke();c.dataset.signed='1';e.preventDefault();});
  c.addEventListener('pointermove',e=>{if(!down)return;const [a,b]=at(e);x.lineTo(a,b);x.stroke();});
  ['pointerup','pointercancel'].forEach(n=>c.addEventListener(n,()=>{down=false;}));
 });
}
function sigClear(id){const c=document.getElementById(id);c.getContext('2d').clearRect(0,0,c.width,c.height);delete c.dataset.signed;}
"""


def add_signature_pad(s):
    """Signature boxes the client signs with a mouse or finger (added Nov 12, 2026). Safe to run again."""
    if "function sigInit" in s:
        return s
    def rep(old, new):
        nonlocal s
        assert old in s, old[:60]
        s = s.replace(old, new, 1)
    rep(" if(q.type==='check')return `<div class=\"f agree\">",
        " if(q.type==='sig')return `<div class=\"f\"><label class=\"t\">${esc(q.t)}${r}</label><canvas class=\"sig\" id=\"${q.k}\" width=\"700\" height=\"170\"></canvas>"
        "<div><button type=\"button\" class=\"btn light\" onclick=\"sigClear('${q.k}')\">Clear signature</button></div>"
        "<small>Sign in the box with your mouse, or with your finger on a phone or tablet.</small></div>`;\n"
        " if(q.type==='check')return `<div class=\"f agree\">")
    rep("document.getElementById('formarea').innerHTML=h;", "document.getElementById('formarea').innerHTML=h;sigInit();")
    rep("  if(q.type==='check')v=document.getElementById(q.k).checked;",
        "  if(q.type==='check')v=document.getElementById(q.k).checked;\n"
        "  else if(q.type==='sig'){const c=document.getElementById(q.k);v=c.dataset.signed?c.toDataURL():'';}")
    rep("if(v)h+=`<tr><td>${esc(q.t)}</td><td>${esc(v)}</td></tr>`;",
        "if(v)h+=`<tr><td>${esc(q.t)}</td><td>${q.type==='sig'?`<img class=\"sigimg\" src=\"${v}\" alt=\"Signature\">`:esc(v)}</td></tr>`;")
    rep("function mark(el)", SIG_JS.strip() + "\nfunction mark(el)")
    rep("</style>", "canvas.sig{display:block;width:100%;max-width:700px;height:auto;aspect-ratio:700/170;background:#fff;border:1.5px solid #999;"
                    "border-bottom:2.5px solid var(--navy);border-radius:6px;touch-action:none;cursor:crosshair}\n"
                    ".sigimg{max-width:260px;height:auto;border-bottom:1px solid #999}\n</style>")
    return s


def main():
    s = PAGE.read_text(encoding="utf-8")
    data = ",\n ".join(json.dumps(f, ensure_ascii=False) for f in CONSENT)
    block = "/*CONSENT*/\n " + data + "\n /*/CONSENT*/"
    if "/*CONSENT*/" in s:
        s = re.sub(r"/\*CONSENT\*/.*?/\*/CONSENT\*/", lambda m: block, s, flags=re.S)
    else:
        old = re.search(r" \{id:'consent',name:'Agreements and Consent Forms',soon:'[^']*'\}", s)
        assert old, "placeholder entry not found"
        s = s.replace(old.group(0), " " + block)
        # list + field renderers
        a, b = s.index("function renderList(){"), s.index("function mark(el)")
        s = s[:a] + NEW_JS.strip() + "\n" + s[b:]
        # saving: skip text blocks, read check boxes
        old = "  let v;\n  if(q.type==='one')"
        assert old in s
        s = s.replace(old, "  if(q.type==='read')return;\n  let v;\n  if(q.type==='check')v=document.getElementById(q.k).checked;\n  else if(q.type==='one')")
        old = "const n=FORMS.filter(f=>!f.soon).length;\n if(Object.keys(done).length===n)"
        assert old in s
        s = s.replace(old, "const n=FORMS.filter(f=>f.sections).length;\n if(Object.keys(done).length===n)")
        old = "FORMS.filter(f=>!f.soon&&done[f.id]).forEach("
        assert old in s
        s = s.replace(old, "FORMS.filter(f=>f.sections&&done[f.id]).forEach(")
        old = "f.sections.flatMap(s=>s[1]).forEach(q=>{let v=answers[q.k];if(Array.isArray(v))v=v.join('; ');"
        assert old in s
        s = s.replace(old, "f.sections.flatMap(s=>s[1]).filter(q=>q.type!=='read').forEach(q=>{let v=answers[q.k];if(Array.isArray(v))v=v.join('; ');if(v===true)v='Agreed';")
        old = "if(q.req&&(!v||!v.length)&&!missing)missing=q.t;"
        assert old in s
        s = s.replace(old, "if(q.req&&(!v||(v!==true&&!v.length))&&!missing)missing=q.t;")
        css = (".grp{margin-top:26px;font-size:20px;color:var(--navy);border-bottom:2px solid var(--gold)}\n"
               ".read h4{margin:16px 0 4px;color:var(--navy);font-size:17px}.read p,.read li{font-size:16px;margin:0 0 8px}.read ul{margin:0 0 8px;padding-left:22px}\n"
               ".agree label{display:flex;gap:10px;align-items:flex-start;cursor:pointer;background:#fbf8ef;border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-size:16px}\n"
               ".agree input{flex:none;width:20px;height:20px;margin-top:3px}\n.opts.wide label{flex:1 1 100%;text-align:left}\n")
        s = s.replace("</style>", css + "</style>", 1)
    s = add_signature_pad(s)
    old = "Altogether they take about 15–20 minutes."
    if old in s:
        s = s.replace(old, "About You and the Brief History take about 15–20 minutes; then please read and sign the agreements.")
    PAGE.write_text(s, encoding="utf-8")
    print("updated", PAGE.name)


if __name__ == "__main__":
    main()
