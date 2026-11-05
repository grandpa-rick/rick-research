# PROVE 278 Q67: independent re-implementation from the printed defs (expository Def wordqc, Thm B).
import itertools
from collections import defaultdict, Counter
def inv(w,i):
    seen=False
    for c in w:
        if c==i+1: seen=True
        elif c==i and seen: return True
    return False
def ff(w,i):
    if inv(w,i) or i not in w: return None
    p=max(t for t,c in enumerate(w) if c==i); return w[:p]+(i+1,)+w[p+1:]
def ee(w,i):
    if inv(w,i) or i+1 not in w: return None
    p=min(t for t,c in enumerate(w) if c==i+1); return w[:p]+(i,)+w[p+1:]
def std(w):
    o=sorted(range(len(w)),key=lambda p:(w[p],p)); s=[0]*len(w)
    for r,p in enumerate(o): s[p]=r+1
    return tuple(s)
def ides(s): return frozenset(k for k in range(1,len(s)) if s.index(k+1)<s.index(k))
def sw(w,j): w=list(w); w[j],w[j+1]=w[j+1],w[j]; return tuple(w)
def bco(w):  # Gessel b-coordinates
    s=std(w); return tuple(w[s.index(k)] for k in range(1,len(w)+1))
# linear ops as dicts
def add(d,w,c):
    d[w]=d.get(w,0)+c
    if d[w]==0: del d[w]
def ap(op,v):
    o={}
    for w,c in v.items():
        for x,y in op(w).items(): add(o,x,c*y)
    return o
L=lambda x: {} if x is None else {x:1}
def T(j): return lambda w: {sw(w,j):1} if w[j]<w[j+1] else ({} if w[j]==w[j+1] else {w:-1})
def fU(i):   # KT V p.19: i's with no earlier i+1
    def op(w):
        o={}
        for p,c in enumerate(w):
            if c==i+1: break
            if c==i: add(o,w[:p]+(i+1,)+w[p+1:],1)
        return o
    return op
def eU(i):   # guessed dual: i+1's with no later i
    def op(w):
        o={}
        for p in range(len(w)-1,-1,-1):
            c=w[p]
            if c==i: break
            if c==i+1: add(o,w[:p]+(i,)+w[p+1:],1)
        return o
    return op
R=Counter()
for n in range(2,5):
  for k in range(2,6):
    W=list(itertools.product(range(1,n+1),repeat=k))
    for w in W:
      s=std(w)
      for j in range(k-1):
        cons=abs(s[j]-s[j+1])==1
        for i in range(1,n):
          for nm,op in (('f',ff),('e',ee)):
            ok = (lambda x: None if x is None else sw(x,j))(op(w,i)) == op(sw(w,j),i)
            R[('a-swap',nm,cons,ok)]+=1
          # (c) linear commutation and defect formula
          for nm,lop,qop in (('f',fU,ff),('e',eU,ee)):
            R[('KTcomm',nm,ap(T(j),lop(i)(w))==ap(lop(i),T(j)(w)))]+=1
            q=qop(w,i); lhs=ap(T(j),L(q)); 
            for x,c in ap(lambda u:L(qop(u,i)),T(j)(w)).items(): add(lhs,x,-c)
            a,b=(i,i+1) if nm=='f' else (i,i+1)
            pred = {sw(q,j):1} if (q is not None and q[j]==i and q[j+1]==i+1) else {}
            R[('defect',nm,lhs==pred)]+=1
            R[('defect-in-cons',nm, (not lhs) or cons)]+=1
      # b-coords equal under non-consecutive swap
      for j in range(k-1):
        if abs(s[j]-s[j+1])>1:
          R[('bco',bco(w)==bco(sw(w,j)) and ides(std(sw(w,j)))==ides(s))]+=1
    # (b)/(d): components vs std classes, iso via b-coords, LinExt connectivity
    comp={}
    for w in W:
      if w in comp: continue
      st=[w]; comp[w]=w
      while st:
        x=st.pop()
        for i in range(1,n):
          for op in (ff,ee):
            y=op(x,i)
            if y is not None and y not in comp: comp[y]=w; st.append(y)
    cl=defaultdict(set)
    for w in W: cl[comp[w]].add(std(w))
    R[('comp=std',all(len(v)==1 for v in cl.values()) and len(cl)==len({std(w) for w in W}))]+=1
    # S_k side graph on {sigma: ides fixed}: connected under nonconsecutive swaps?
    if n>=k:
      byD=defaultdict(list)
      for s in itertools.permutations(range(1,k+1)): byD[ides(s)].append(s)
      for D,ss in byD.items():
        S=set(ss); seen={ss[0]}; st=[ss[0]]
        while st:
          x=st.pop()
          for j in range(k-1):
            if abs(x[j]-x[j+1])>1:
              y=sw(x,j)
              if y not in seen: seen.add(y); st.append(y)
        R[('linext-conn',seen==S)]+=1
# negative control for (a): swap at consecutive must FAIL somewhere
for key in sorted(R,key=str): print(key,R[key])
