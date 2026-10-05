"""Day 205: cyclotomic content of q^5 tau_r^(3) vs [r+3]_t, and q=1 check."""
import json, sympy as sp, os
from k3_closed_form_fit import closed
q, t, u = sp.symbols('q t u')
D = '/home/agent/projects/proofs/scripts/day205'

C = q**3*(t*u-1)*(t**2*u-1) + (1+t+t**2)*(q**2*(t*u-1) + q*(t-1) + 1)

def phi(d):
    return sp.cyclotomic_poly(d, t)

print(f"{'r':>2} | {'Phi_d present (d|r+3)':<22} | {'missing':<8} | extra Phi_d (d !| r+3) | other factors")
for r in range(1, 14):
    fn = f'{D}/k3_r{r}_m{r+3}.json'
    if not os.path.exists(fn):
        continue
    tau = sp.sympify(json.load(open(fn))[str((r+3,))])
    N = sp.factor(sp.cancel(q**6*tau))   # q^6 tau is a polynomial
    _, facs = sp.factor_list(N)
    cyc, other = [], []
    for f, e in facs:
        found = None
        if f.free_symbols == {t}:
            for d in range(1, 4*r+20):
                if sp.expand(f - phi(d)) == 0:
                    found = d
                    break
        if found:
            cyc += [found]*e
        else:
            other.append((f, e))
    divs = [d for d in sp.divisors(r+3) if d > 1]
    present = [d for d in divs if d in cyc]
    missing = [d for d in divs if d not in cyc]
    extra = [d for d in cyc if d not in divs]
    oth = [str(f) if f.free_symbols != {t, q} else f'<deg_t {sp.degree(f, t)} bivariate>' for f, e in other]
    # identity check with the closed-form factorization
    ident = sp.cancel(q**5*tau - (q**3-1)*sp.cancel((1-t**(r+3))/(1-t))*C.subs(u, t**r)/(q*(1+t+t**2)))
    # q=1 specialization by direct substitution
    q1 = sp.simplify(tau.subs(q, 1))
    # is C(t^r,t) divisible by Phi_3?
    rem3 = sp.rem(sp.expand(C.subs(u, t**r)), phi(3), t)
    print(f"{r:>2} | {str(present):<22} | {str(missing):<8} | {str(extra):<10} | {oth} | ident={ident} | tau(q=1)={q1} | C(t^r) mod Phi3 = {sp.factor(rem3)}")
