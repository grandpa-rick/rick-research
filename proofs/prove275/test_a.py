from qc import *
# rule Q (quasi-tensor) : returns 'L','R', or None from (eps,phi) of factors
def ruleQ(su,sv,op):
    (eu,pu),(ev,pv)=su,sv
    if INF in (eu,ev) or (eu>0 and pv>0): return None
    if op=='e': return 'L' if eu>0 else ('R' if ev>0 else None)
    else: return 'R' if pv>0 else ('L' if pu>0 else None)
def ruleK(su,sv,op):   # Kashiwara tensor rule for this bracketing (anti-Kashiwara convention: u before v)
    (eu,pu),(ev,pv)=su,sv
    if op=='e': return 'L' if eu>pv else ('R' if ev>0 else None) if True else None
    else: return 'R' if pv>eu else ('L' if pu>0 else None)
def ruleK_fixed(su,sv,op):
    (eu,pu),(ev,pv)=su,sv
    # word u v: reduced u = i^pu (i+1)^eu ; reduced v = i^pv (i+1)^ev ; (i+1)^eu i^pv brackets min
    if op=='e':
        # unbracketed i+1's: from u: max(eu-pv,0) (they're left), from v: ev. leftmost: u's if eu>pv
        if eu>pv: return 'L'
        return 'R' if ev>0 else None
    else:
        # unbracketed i's: from u: pu, from v: max(pv-eu,0); rightmost: v's if pv>eu
        if pv>eu: return 'R'
        return 'L' if pu>0 else None
def swapped(rule): return lambda su,sv,op: {'L':'R','R':'L',None:None}[rule(sv,su,op)]
def apply(u,v,side,i,op,F):
    if side is None: return None
    if side=='L':
        x=F(u,i,op); return None if x is None else x+v
    x=F(v,i,op); return None if x is None else u+x
def test(F,S,rule,N=6,n=4):
    tot=bad=0;first=None
    for L in range(2,N+1):
      for w in itertools.product(range(1,n+1),repeat=L):
        for m in range(1,L):
          u,v=w[:m],w[m:]
          for i in range(1,n):
            for op in 'ef':
              tot+=1
              if F(w,i,op)!=apply(u,v,rule(S(u,i),S(v,i),op),i,op,F):
                bad+=1
                if first is None: first=(u,v,i,op)
    return tot,bad,first
print('quasi, rule Q        ',test(quasi,qstr,ruleQ))
print('quasi, swapped Q     ',test(quasi,qstr,swapped(ruleQ)))
print('kashiwara, rule K    ',test(kash,kstr,ruleK_fixed))
print('kashiwara, swapped K ',test(kash,kstr,swapped(ruleK_fixed)))
# does quasi follow Kashiwara rule with finite strings? (expected: no, inversion straddle)
print('quasi, rule K w/ qstr',test(quasi,qstr,ruleK_fixed))
# is the choice determined by (eps,phi)? check functional dependence independently of ruleQ:
tab=defaultdict(set)
for L in range(2,7):
  for w in itertools.product(range(1,5),repeat=L):
    for m in range(1,L):
      u,v=w[:m],w[m:]
      for i in range(1,4):
        for op in 'ef':
          r=quasi(w,i,op)
          side=None if r is None else ('L' if r[m:]==v and r[:m]!=u else 'R')
          tab[(qstr(u,i),qstr(v,i),op)].add(side)
print('data-determined keys:',len(tab),' ambiguous:',sum(len(s)>1 for s in tab.values()))
