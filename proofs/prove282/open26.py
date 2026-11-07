import json,sys
sys.path.insert(0,'.')
import tdec
from tdec import dec_tab
from reduce2 import explore2
from collections import Counter
D=json.load(open('pfail.json')); c=Counter(); out=[]
for d in D:
    if explore2(d['Px'],d['Pz'])[0]=='KILL': continue
    tdec.memo.clear()
    r=dec_tab(d['Px'],d['Pz'],budget=300)
    c[None if r is None else r[0]]+=1
    out.append(dict(d,res=r))
    print(d['lam'], None if r is None else (r[0],[t[0] for t in r[1]]),flush=True)
json.dump(out,open('open26.json','w'),default=list); print(c)
