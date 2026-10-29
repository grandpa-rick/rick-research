"""Multivariate check: sum over (rho,lambda,kappa) of prod_d q_d^{#boxes of kappa/rho on diagonal d} == prod_{d=0}^{m-1}(2+q_d)?"""
import sympy as sp
from q50_count import strict_parts, steps, S_of, lam_of, diagram
for m in range(1, 7):
    qs = sp.symbols(f'q0:{m}')
    tot = 0; maxper = 0
    for rho in strict_parts(m):
        for S1, _ in steps(S_of(rho), m, True):
            for S2, _ in steps(S1, m, False):
                th = diagram(lam_of(S2)) - diagram(rho)
                ds = [b - a for a, b in th]
                maxper = max([maxper] + [ds.count(d) for d in set(ds)])
                tot += sp.Mul(*[qs[d] for d in ds])
    target = sp.Mul(*[2 + x for x in qs])
    print(m, "prod(2+q_d) match:", sp.expand(tot - target) == 0, " max boxes per diagonal in theta:", maxper)
