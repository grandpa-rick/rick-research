import json,sys
sys.path.insert(0,'.')
from reduce2 import explore2
from collections import Counter, defaultdict
lines=[json.loads(l) for l in open('out_muxz16.txt')]
byf=defaultdict(list)
for d in lines: byf[d['f']].append(d)
c=Counter(); openlist=[]
for f,ds in byf.items():
    certs=json.load(open('../wake282/'+f))
    for d,cc in zip(ds,certs):
        assert cc['Pz']==d['Pz'] and cc['A']==d['A']
        if d['muxz']=='parity-even': continue
        r=explore2(cc['Px'],cc['Pz'])
        c[(d['muxz'],r[0])]+=1
        if d['muxz']=='exhausted' and r[0]=='OPEN': openlist.append((cc['lam'],cc['A'],d['gap']))
print(dict(c)); print(openlist)
