"""Wake 223: independent check that D_a(e_b) (bfull.py, symbolic t) equals B(e_a,e_b) := d/ds (e_a * e_b)|_{s=1}
computed with the full s-dependent subset-formula star engine of day220/biderivation.py, at t=3/5, n=a+b<=6. Grade: computed."""
import sys, pickle
from sympy import Rational, symbols
src = open('../day220/biderivation.py').read().split("log(f't = {T}")[0]
sys.argv = ['x', 'crosscheck_star_engine.log', '3/5', '6']
exec(src)
t = symbols('t'); res = pickle.load(open('bfull_n7.pkl', 'rb'))
ok = tot = 0
for (a, b), E in sorted(res.items()):
    if a+b > 6: continue
    Bs = Bf({(a,): 1}, {(b,): 1})
    Es = {mu: c.subs(t, Rational(3, 5)) for mu, c in E.items()}
    keys = set(Bs) | set(Es); good = all(Bs.get(k, 0) - Es.get(k, 0) == 0 for k in keys)
    tot += 1; ok += good
    log(f'B(e{a},e{b}) star-engine={Bs}  D_a(e_b)@t=3/5={Es}  {"OK" if good else "FAIL"}')
log(f'CROSSCHECK {ok}/{tot}')
