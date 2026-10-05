"""Wake 223 Task B: tests on wake222 G' leads (n<=6; n=6 excludes lam=1^6). Grade: computed.
(1) v = l - kappa on all pairs. (2) non-coarsening pairs + leads. (3) fit Lead = (t^{lam_recv*k}-1)/(1-t^k) for single-move
pairs (l-kappa=1). (4) (2,2,2)->(5,1) Lead(0)=4. (5) EVERY v=1 pair vs first-order term predicted from the computed B rule:
[(s-1)^1] e*_lam = sum_{i<j} M_{lam_i lam_j} e_{lam minus i,j},  M_{ab} = b e_a e_b + sum_{j=1}^b L(a-b+j,j) e_{a+j}e_{b-j} (a>=b);
and the prediction must vanish when v>=2."""
import os, sys, pickle
from sympy import symbols, cancel, factor, expand
G='/home/agent/projects/proofs/scripts/wake222/gprime'; sys.path.insert(0, G); os.chdir(G)
from analyze import leads, is_coarsening
from kappa import kappa
t = symbols('t')
def L(a, b): return cancel((1-t**(a+b))/((1-t**a)*(1-t**b))*(t**(a*b)-1))
def M(a, b):
    if a < b: a, b = b, a
    out = {(a, b): b}
    for j in range(1, b+1):
        mu = tuple(x for x in (a+j, b-j) if x > 0); out[mu] = out.get(mu, 0) + L(a-b+j, j)
    return out
def first_order(lam):
    out = {}; l = len(lam)
    for i in range(l):
        for j in range(i+1, l):
            rest = [lam[k] for k in range(l) if k not in (i, j)]
            for mu, c in M(lam[i], lam[j]).items():
                key = tuple(sorted(list(mu)+rest, reverse=True)); out[key] = out.get(key, 0) + c
    return out
allL = {}
for n in range(2, 7): allL.update(leads(n))
nv = okv = 0; nfo = okfo = 0; fails = []
print('== non-coarsening pairs ==')
for (lam, mu), (v, Ld) in sorted(allL.items()):
    k = kappa(lam, mu); nv += 1; okv += (v == len(lam)-k)
    fo = cancel(first_order(lam).get(mu, 0))
    if v == 1: good = cancel(fo - Ld) == 0
    else: good = fo == 0
    nfo += 1; okfo += good
    if not good: fails.append((lam, mu, v, factor(Ld), factor(fo)))
    if not is_coarsening(lam, mu):
        # single-move fit: find receiver/sender/k when l-kappa = 1 (two parts change)
        fit = ''
        if len(lam)-k == 1:
            from collections import Counter
            dl = Counter(lam) - Counter(mu); dm = Counter(mu) - Counter(lam)
            if sum(dl.values()) == 2 and sum(dm.values()) == 2:
                old = sorted(dl.elements(), reverse=True); new = sorted(dm.elements(), reverse=True)
                recv, kk = old[0], new[0]-old[0]
                if kk > 0:
                    F = cancel((t**(recv*kk)-1)/(1-t**kk)); fit = f' fit(t^(recv*k)-1)/(1-t^k) [recv={recv},k={kk}] = {factor(F)}: {cancel(F-Ld)==0}'
        print(f'{lam}->{mu}: l-kappa={len(lam)-k} v={v} Lead(0)={Ld.subs(t,0)} Lead={factor(Ld)}{fit}')
print(f'VALUATION LAW v=l-kappa: {okv}/{nv} (n<=6, 1^6 excluded)')
print(f'FIRST-ORDER B-RULE (v=1 lead match, v>=2 vanish): {okfo}/{nfo}')
for f in fails: print('  FAIL', f)
n6 = {k: v for k, v in allL.items() if sum(k[0]) == 6}
print(f'n=6 pairs: {len(n6)}; v=l-kappa at n=6: {sum(1 for (l,m),(v,_) in n6.items() if v==len(l)-kappa(l,m))}/{len(n6)}')
v, Ld = allL[((2,2,2),(5,1))]; print(f'(2,2,2)->(5,1): v={v} Lead(0)={Ld.subs(t,0)} Lead={expand(Ld)} = {factor(Ld)}; Lead(1)={Ld.subs(t,1)}')
