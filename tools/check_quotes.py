"""Check that every quoted passage of 5+ words in card 'teaches' text appears in the BSB."""
import re,json,sys,glob
t=open('tools/BSB.txt',encoding='utf-8').read()
norm=lambda s:re.sub(r'\s+',' ',re.sub(r"[^a-z0-9' ]+",' ',s.lower().replace('’',"'").replace('‘',"'"))).strip()
B=norm(re.sub(r'\[\d+:\d+\]','',t))
bad=0
for f in sorted(sum([glob.glob(a) for a in sys.argv[1:]],[])):
    d=json.load(open(f));txt=d['teaches']
    for q in re.findall(r'“([^”]+)”',txt):
        for part in re.split(r'…|\.\.\.',q):
            n=norm(part)
            if len(n.split())>=5 and n not in B:
                print(f[-30:],'NOT FOUND:',part.strip()[:90]);bad+=1
print('bad',bad)
