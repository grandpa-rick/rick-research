"""Day 205: closed form for tau_r^(3) = coefficient of e_(r+3) in p_3(Y).e_r.
Fitted by reading off the t-expansion of q^5 tau (1-t)(1-t^3)/((q-1)[3]_q) at r=5,6,7
(where the u-blocks don't overlap); verified on all other computed r (held out)."""
import json, sympy as sp, glob, os
q, t, u = sp.symbols('q t u')
D = '/home/agent/projects/proofs/scripts/day205'

F = (q**2*t**6*(t-1)*u**3 + q*t**3*(t-q)*(t**3-1)*u**2
     + (t**7 - (q**2+q-1)/q*t**6 + (q**2-q-1)*t**4 + (q**2+q-1)/q*t**3 - q*(q-1)*t)*u
     + (-t**4 + (q**2+q-1)/q*t**3 - (q**2-1)*t + (q-1)**2*(q+1)/q))

def closed(r):
    return (q-1)*(q**2+q+1)*F.subs(u, t**r)/((1-t)*(1-t**3))  # = q^5 tau_r

if __name__ == '__main__':
    print('F(u,t) factored:', sp.factor(F))
    print('F(t^-3,t) =', sp.simplify(F.subs(u, t**-3)))
    G = sp.factor(sp.cancel(F/(1-t**3*u)))
    print('G = F/(1-t^3 u) =', G)
    print('G collected in u:', sp.collect(sp.expand(sp.cancel(G*q)), u))
    files = sorted(glob.glob(f'{D}/k3_r*_m*.json'))
    for fn in files:
        base = os.path.basename(fn)[:-5]
        r, m = int(base.split('_')[1][1:]), int(base.split('_')[2][1:])
        tau = sp.sympify(json.load(open(fn))[str((r+3,))])
        diff = sp.cancel(q**5*tau - closed(r))
        tag = 'FIT' if r in (5, 6, 7) and m == r+3 else 'held-out'
        print(f'r={r:2d} m={m:2d}: q^5 tau - closed = {diff}   [{tag}]')
