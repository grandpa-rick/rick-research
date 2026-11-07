"""Skew test: for skew std tableaux S of lam/mu (|S|=m), eject letters from T by reverse bumping boxes of S in decreasing label order.
x<=z in cell Q  <=>  for all k: E_Tx(Q_{>k}) >=_Gale E_Tz(Q_{>k}).  Kill(m): exists S with |S|<=m violating."""
import sys,json
sys.path.insert(0,'.')
from corner import rbump, rowof, evac
from collections import Counter
def ejects(T,S):  # S: list of rows (row indices) of boxes in decreasing label order
    T=[list(R) for R in T]; out=[]
    for r in S:
        a=T[r].pop()
        for rr in range(r-1,-1,-1):
            row=T[rr]; j=max(j for j,b in enumerate(row) if b<a); row[j],a=a,row[j]
        out.append(a)
        T=[R for R in T]
    return sorted(out)
def strips(lam,m):
    # sequences of removable-row choices of length m (removing outer corners successively)
    lam=list(lam); res=[]
    def rec(sh,seq):
        if len(seq)==m: res.append(seq[:]); return
        for r in range(len(sh)):
            if sh[r]>0 and (r==len(sh)-1 or sh[r]>sh[r+1]):
                sh[r]-=1; seq.append(r); rec(sh,seq); seq.pop(); sh[r]+=1
    rec(lam,[]); return res
def gale_ge(a,b): return all(x>=y for x,y in zip(a,b))
def minkill(Tx,Tz,lam,M=4):
    for m in range(1,M+1):
        for S in strips(lam,m):
            if not gale_ge(ejects(Tx,S),ejects(Tz,S)): return m,S
    return None,None
if __name__=='__main__':
    D=json.load(open('pfail.json')); c=Counter(); ce=Counter()
    for d in D:
        lam=d['lam']; m,S=minkill(d['Px'],d['Pz'],lam)
        m2,S2=minkill(evac(d['Px']),evac(d['Pz']),lam)
        c[(m,m2)]+=1
    print(c)
