"""Replace the HeyGen iframes on counselors/guidelines.html with Wix-hosted <video> players
plus Back 10 sec / Play-Pause / Stop / Forward 10 sec buttons."""
import json,re
P='counselors/guidelines.html'
heygen2key={'7b3eaa3d32854ff2a6a27363f6255776':'g01','d8982404914d4b5f947e25f25886ac5a':'g02','99ec5681d0634c83a240c3e57232c683':'g03','5c710e149aa149899413665dc629c12e':'g04','a6e78060cc53405ba0b9ac1281ebd823':'g05','ba333f34f5c34d9288247cf3a621324b':'g06a','c496f790c2034d0f9aaeb1b380bf12b9':'g06b','2fcb205031d04271ab76a1cc050fd210':'g07','e02ef46c3705490d8e1ace3621c7fe0e':'g08','0449ee56a6c24be79aaa4e3b47620dd0':'g09','755846f08add4b21aa16c8c5aaa9a4ae':'g10','362de205078c41b684a1aebda9b1d7fe':'g11','1c1d16dbee8c4d64be4f8fbcb3505f98':'g12','61131e264b6548b99519fadcea6a169e':'g13','9b10e3b314134221b4e950b643899c03':'g14','e70ac88e43284c0db41fcc37caaf4e61':'g15','ec23b182fab44a7aa2b24dac9f8cc560':'g16','d599a5446ff74c78b191ed29e3cf13b2':'closing'}
wix=json.load(open('tools/guidelines/wix_videos.json'))
s=open(P).read()
CTL=('<div class="gctl" role="group" aria-label="Video controls">'
 '<button type="button" data-a="rew" aria-label="Back 10 seconds">&#9194; Back 10 sec</button>'
 '<button type="button" data-a="pp" class="pri" aria-label="Play">&#9654; Play</button>'
 '<button type="button" data-a="stop" aria-label="Stop">&#9632; Stop</button>'
 '<button type="button" data-a="fwd" aria-label="Forward 10 seconds">Forward 10 sec &#9193;</button></div>')
def rep(m):
    hid,title=m.group(1),m.group(2)
    url='https://video.wixstatic.com/video/%s/file'%wix[heygen2key[hid]]
    return ('<div class="gvid-f"><video controls playsinline preload="metadata" src="%s" title="%s"></video></div>'%(url,title))+CTL
s,n=re.subn(r'<div class="gvid-f"><iframe src="https://app\.heygen\.com/embeds/([a-f0-9]+)" title="([^"]*)"[^>]*></iframe></div>',rep,s)
assert n==18,n
css=('<style id="gvid-ctl">.gvid-f video{position:absolute;inset:0;width:100%;height:100%;background:#12284c}'
 '.gctl{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin:10px 0 16px}'
 '.gctl button{font:inherit;font-family:system-ui,sans-serif;cursor:pointer;border-radius:22px;border:1px solid var(--navy);background:#fff;color:var(--navy);font-weight:700;padding:7px 14px;font-size:.95rem;line-height:1.2}'
 '.gctl button.pri{background:var(--navy);color:#fff;min-width:7.5em}'
 '.gctl button:hover{border-color:var(--gold)}'
 '@media print{.gctl{display:none}}</style>')
js=('<script id="gvid-js">(function(){var vids=[].slice.call(document.querySelectorAll(".gvid video"));'
 'function setPP(v){var b=v.closest(".gvid").querySelector("[data-a=pp]");if(v.paused){b.innerHTML="&#9654; Play";b.setAttribute("aria-label","Play")}else{b.innerHTML="&#10074;&#10074; Pause";b.setAttribute("aria-label","Pause")}}'
 'vids.forEach(function(v){["play","pause","ended"].forEach(function(e){v.addEventListener(e,function(){setPP(v)})});'
 'v.addEventListener("play",function(){vids.forEach(function(o){if(o!==v&&!o.paused)o.pause()})});'
 'v.closest(".gvid").querySelector(".gctl").addEventListener("click",function(ev){var b=ev.target.closest("button");if(!b)return;var a=b.getAttribute("data-a");'
 'if(a==="pp"){if(v.paused){v.play()}else{v.pause()}}'
 'else if(a==="stop"){v.pause();v.currentTime=0}'
 'else if(a==="rew"){v.currentTime=Math.max(0,v.currentTime-10)}'
 'else if(a==="fwd"){v.currentTime=Math.min((v.duration||v.currentTime+10)-0.1,v.currentTime+10)}})});})();</script>')
if 'id="gvid-ctl"' not in s: s=s.replace('</head>',css+'</head>',1)
if 'id="gvid-js"' not in s: s=s.replace('</body>',js+'</body>',1)
open(P,'w').write(s); print('replaced',n)
