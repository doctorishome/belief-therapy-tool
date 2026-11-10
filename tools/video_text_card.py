# On-screen word banners for the Belief Counseling teaching videos (approved style, Nov 9, 2026):
# navy banner, gold top line, lower left, serif 32 / label 18. Overlay with ffmpeg at x=36, y=H-h-36, ~6 s each with 0.5 s fades.
from PIL import Image, ImageDraw, ImageFont
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',32)
L=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
def wrap(text,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if F.getlength(t)<=maxw: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def card(label,text,out,maxw=640):
    lines=wrap(text,maxw)
    w=int(max(max(F.getlength(l) for l in lines),L.getlength(label.upper()))+48)
    h=58+len(lines)*42+20
    im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,w-1,h-1),radius=14,fill=(18,40,76,228))
    d.rounded_rectangle((0,0,w-1,7),radius=3,fill=(201,162,39,255))
    d.text((24,20),label.upper(),font=L,fill=(201,162,39,255))
    y=50
    for ln in lines: d.text((24,y),ln,font=F,fill=(255,255,255,255)); y+=42
    im.save(out)
if __name__=='__main__':
    card('Lesson 1','Introduction to Belief Counseling','c1.png')
    card('The three steps','Identify · Challenge · Replace','c2.png')
