"""Independent replay of c^s_{u,v} via Delta(R_s)=sum_nu R_{lambda/nu} (x) R_{nu/mu} (GLL Prop 2.4.2 / Huang),
ribbon cell poset, order ideals, gap-free expansion R_{a (+) b}=R_{a0b}+R_{a1b}. Compare with shuffle count."""
import itertools
from cap_rank import coeff, subseqs, EPS
def expand(s, cells):
    # cells sorted subset of 0..d-1 (traversal order); return dict word->mult for R_subset
    comps=[]; cur=[cells[0]]
    for c in cells[1:]:
        if c==cur[-1]+1: cur.append(c)
        else: comps.append(cur); cur=[c]
    comps.append(cur)
    words=[''.join(s[c] for c in comp[:-1]) for comp in comps]
    out={}
    for gaps in itertools.product('01',repeat=len(words)-1):
        w=words[0]
        for g,x in zip(gaps,words[1:]): w+=g+x
        out[w]=out.get(w,0)+1
    return out
def leq(s,a,b):  # cell a <= cell b in English order (a,b traversal indices)
    if a==b: return True
    lo,hi=min(a,b),max(a,b)
    seg=s[lo:hi]
    if set(seg)<= {'0'}: return a<b   # same row: later is right => larger
    if set(seg)<= {'1'}: return a>b   # same column: later is above => smaller
    return False
def delta_coeffs(s):
    d=len(s)+1; cells=range(d); res={}
    for k in range(d+1):
        for I in itertools.combinations(cells,k):
            Is=set(I)
            if any((b in Is) and leq(s,a,b) and a not in Is for a in cells for b in cells): continue
            F=[c for c in cells if c not in Is]
            L=expand(s,F) if F else {EPS:1}
            R=expand(s,list(I)) if I else {EPS:1}
            for u,x in L.items():
                for v,y in R.items(): res[(u,v)]=res.get((u,v),0)+x*y
    return res
bad=0;n=0
for Lg in range(0,7):
    for s in (''.join(t) for t in itertools.product('01',repeat=Lg)):
        D=delta_coeffs(s); d=Lg+1
        for (u,v),c in D.items():
            n+=1
            if coeff(u,v,s)!=c: bad+=1; print('MISMATCH',s,u,v,c,coeff(u,v,s))
        # also zero entries: check all pairs
        for i in range(d+1):
            U=[EPS] if i==0 else subseqs(s,i-1); V=[EPS] if i==d else subseqs(s,d-i-1)
            for u in U:
                for v in V:
                    if coeff(u,v,s)!=D.get((u,v),0): bad+=1
print('entries checked',n,'mismatches',bad)
