"""Classify the n=16 false positives of rule R1 (parity OK, no (ii)-element, but verdict NO)."""
import json,glob,sys
sys.path.insert(0,'../prove281')
from common import *
from collections import Counter
C=[c for f in sorted(glob.glob('certs16_*.json')) for c in json.load(open(f))]
S=json.load(open('sieve16.json'))
cnt=Counter(); shp=Counter(); dz=Counter(); ex=[]
for c,r in zip(C,S):
    assert c['Px']==r['Px'] and c['Pz']==r['Pz']
    if not(r['parity_ok'] and r['verdict']=='NO' and not any(e['kind']=='ii' for e in r['elems'])): continue
    shp[''.join(map(str,r['lam']))]+=1
    z=c['z']; Lz=L(z)
    kinds=[]
    for e,ce in zip(r['elems'],c['certs']):
        if ce['verdict'].startswith('kill'):
            y=e['y']; Ly=L(y)
            f1=(inv(y)<inv(z) and not Lz<=Ly)
            kinds.append((ce['verdict'],len(ce['path']),'Lz<=Ly' if Lz<=Ly else 'Lz!<=Ly','sup' if e['sup'] else '-','candX' if e['cand_x'] else '-'))
    for k in kinds: cnt[k]+=1
    # does a tableau-level F1 test (some boundary star image y with L(z) not<= L(y)) explain it?
    dz[any(k[2]=='Lz!<=Ly' and k[1]==0 for k in kinds)]+=1
print('FP by shape',dict(shp)); print('kill kinds (verdict,pathlen,Lz<=Ly?,Des>A?,candX?) counts:')
for k,v in cnt.most_common(): print('  ',k,v)
print('FP pairs explained by an immediate (path 0) kill with L(z) not<= L(sx):',dict(dz))
