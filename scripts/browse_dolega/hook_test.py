"""Check: <kappa(H~_(l1),...,H~_(lr)), e_n> (= [s_{1^n}], computed from actual Htilde in p-basis)
   == q^{sum C(l_i,2)} K_lam(q), K_lam = Rick's connected-graph sum; hence Rick Lead(t) = (1-t^n)/prod(1-t^l_i) * t^{-sum C} <kappa,e_n>|_{q=t}."""
from dict_test import *
def C2(k): return k*(k-1)//2
ok=0;tot=0
for n in range(2,6):
    for lam in parts(n):
        if len(lam)<2: continue
        K=cumulant([(k,) for k in lam]); val=inner(K,e(n))
        target=q**sum(C2(k) for k in lam)*conn_graph_sum(lam,q)
        good=sp.simplify(val-target)==0; tot+=1; ok+=good
        lead=sp.factor((1-t**n)/sp.prod([1-t**k for k in lam])*t**(-sum(C2(k) for k in lam))*val.subs(q,t))
        print(lam,good, sp.factor(val), '| Rick Lead via Dolega:',lead,'| Thm G:',RickLead(lam), sp.simplify(lead-RickLead(lam))==0)
print(ok,'/',tot)
