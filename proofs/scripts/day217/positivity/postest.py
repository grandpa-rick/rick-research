import sys, pickle
from sympy import symbols, Poly, factor_list, expand, div, together, fraction, Mul
s, t, a = symbols('s t a')
def strip(v, fac):
    """v = sign * fac^m * R ; returns (m, R) with R having fac removed"""
    num, den = fraction(together(v)); m = 0
    num = expand(num)
    while True:
        q, r = div(num, fac, s, t)
        if r != 0: break
        num, m = expand(q), m+1
    return m, num, den
def pos(p, vars_=(s, t)):
    cs = Poly(p, *vars_).coeffs(); return all(c > 0 for c in cs) or all(c < 0 for c in cs)
if __name__ == '__main__':
    basis, MAXN = sys.argv[1], int(sys.argv[2])
    G = pickle.load(open(f'g_{basis}_{MAXN}.pkl', 'rb'))
    tests = {
      'plain': lambda v: pos(fraction(together(v))[0]),
      'strip(1-s)': lambda v: pos(strip(v, 1-s)[1]),
      'strip(1-s),(1-st)': lambda v: pos(strip(strip(v, 1-s)[1], 1-s*t)[1]),
      's=1-a in (a,t)': lambda v: pos(expand(fraction(together(v))[0].subs(s, 1-a)), (a, t)),
      't=1-a': lambda v: pos(expand(fraction(together(v))[0].subs(t, 1-a)), (s, a)),
      's=1+a': lambda v: pos(expand(fraction(together(v))[0].subs(s, 1+a)), (a, t)),
      'st=q (t=q/s) num': lambda v: pos(expand(fraction(together(v.subs(t, a/s)))[0]), (s, a)),
      's=-s': lambda v: pos(expand(fraction(together(v))[0].subs(s, -s))),
      't=-t': lambda v: pos(expand(fraction(together(v))[0].subs(t, -t))),
    }
    for name, f in tests.items():
        bad = [k for k, v in G.items() if not f(v)]
        print(f'{basis} n<={MAXN} test {name}: {len(G)-len(bad)}/{len(G)} pass', ('e.g. fail '+str(bad[0])+' : '+str(G[bad[0]])) if bad else '')
