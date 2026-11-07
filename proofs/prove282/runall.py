import json,sys
sys.path.insert(0,'.')
from reduce import explore
from collections import Counter
D=json.load(open('pfail.json')); c=Counter(); hs=Counter()
for d in D:
    r=explore(d['Px'],d['Pz'])
    c[r[0]]+=1
    if r[0]=='KILL': hs[r[1].count(',')]+=1
    else: print('OPEN',d['lam'],d['Px'],d['Pz'],flush=True)
print(c,'reduction depth of kills',dict(hs))
