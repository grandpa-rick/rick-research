"""Probe: for (i)-elements y=s.x of parity-OK pairs, does a tableau predicate predict mu(y,z)? (exploratory, 1 free choice each)"""
import json,sys
from collections import Counter
for n in (15,16):
    S=json.load(open('sieve%d.json'%n))
    def intr(A): return {i for i in A if (i-1 in A or i==1) and (i+1 in A or i==n-1)}
    preds={'Lz<=int(Ly)':lambda Lz,Ly:Lz<=intr(Ly),'Lz<=Ly':lambda Lz,Ly:Lz<=Ly}
    for name,p in preds.items():
        c=Counter()
        for r in S:
            if not r['parity_ok']: continue
            Lz=set()
            row={v:k for k,R in enumerate(r['Pz']) for v in R}; Lz={i for i in range(1,n) if row[i+1]>row[i]}
            for e in r['elems']:
                if e['kind']!='i' or e['muyz'] is None: continue
                c[(p(Lz,set(e['DesPy'])),e['muyz'])]+=1
        print(n,name,'(pred,mu):',dict(c))
