"""Wake 230: reconcile Day 228 '155/155' with Clio's 85; fibre sizes for the lambda_1-free claim.
Reuses Day 228 tworow.py functions (Xraw, Xclosed) and Day 226 green.py (Kostka-Foulkes x Murnaghan-Nakayama)."""
import sys
sys.path.insert(0,'/home/agent/projects/proofs/scripts/day226'); sys.path.insert(0,'/home/agent/projects/scripts/day228')
import sympy as sp, io, contextlib
from collections import defaultdict
with contextlib.redirect_stdout(io.StringIO()):
    import tworow  # runs the original 155 loop on import; output captured
    orig = sys.stdout
from green import X as Xgreen, t
cap = io.StringIO()
print("Day 228 tworow.py loop (re-run on import) captured output above is suppressed; re-running counts below.")
N=10
ordered=[]; unordered=[]
for n in range(2,N+1):
    for l2 in range(1,n//2+1):
        lam=(n-l2,l2)
        for y in range(1,n):
            ordered.append((lam,(n-y,y)))
            if y<=n-y: unordered.append((lam,(n-y,y)))
print('155-set size', len(ordered), '= sum floor(n/2)(n-1) =', sum((n//2)*(n-1) for n in range(2,N+1)))
print('85-set size', len(unordered), '= sum floor(n/2)^2 =', sum((n//2)**2 for n in range(2,N+1)))
def check(S):
    pr=pc=0; vals={}
    for lam,(x,y) in S:
        cls=tuple(sorted((x,y),reverse=True)); g=sp.expand(Xgreen(lam,cls))
        pr+= sp.expand(g-tworow.Xraw(lam,x,y))==0; pc+= sp.expand(g-tworow.Xclosed(lam,x,y))==0
        vals[(lam,cls)]=g
    return pr,pc,vals
pr,pc,_=check(ordered); print(f'155-set: raw Thm2.5 pass {pr}/{len(ordered)}, closed pass {pc}/{len(ordered)}')
pr,pc,vals=check(unordered); print(f'85-set : raw Thm2.5 pass {pr}/{len(unordered)}, closed pass {pc}/{len(unordered)}')
print('distinct (lam,class) Green values checked:', len(vals), ' distinct polynomials:', len(set(vals.values())))
# fibres at fixed (lambda2, y): points (lambda1, x) with lambda1+lambda2 = x+y = n <= N, lambda1>=lambda2, x>=y
cells=defaultdict(list)
for (lam,(x,y)),g in vals.items(): cells[(lam[1],y)].append((lam[0],x,g))
sizes=defaultdict(int); nonconst=[]
for (l2,y),pts in sorted(cells.items()):
    sizes[len(pts)]+=1
    if len(set(p[2] for p in pts))>1: nonconst.append(((l2,y),[(p[0],p[1],p[2]) for p in pts]))
print('cells (lambda2,y):', len(cells), ' fibre-size histogram {size: #cells}:', dict(sorted(sizes.items())))
print('points in non-singleton fibres:', sum(len(p) for p in cells.values() if len(p)>1))
print('cells where value varies along fibre:')
for c,pts in nonconst:
    print('  ',c, [(l1,x,sp.factor(g)) for l1,x,g in pts])
# y>lambda2 regime: value depends on lambda2 only?
d=defaultdict(set)
for (lam,(x,y)),g in vals.items():
    if y>lam[1]: d[lam[1]].add(g)
print('y>lambda2: distinct values per lambda2:', {k:len(v) for k,v in sorted(d.items())})
# Clio's literal fibre (fixed rho and lambda2, |lambda|=|rho|): always singleton
print("Clio-literal fibre at fixed rho & lambda2: size 1 always (lambda1 = |rho| - lambda2).")
