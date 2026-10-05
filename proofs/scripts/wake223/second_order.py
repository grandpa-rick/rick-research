"""Wake 223: direct computation of E_a^{(2)}(e_b e_c) = sum_{|A|=a} c_A X_A binom(Delta_A,2)(e_b e_c), symbolic t,
full e-expansion; test e_n-coefficient == pref*w_ab*w_ac (the remainder of Lead_{(a,b,c),(n)} after the iterated-B part
L(b,c)L(a,b+c)). Also test e_n-coeff of D_a(D_b e_c) == L(b,c)L(a,b+c) directly. Grade: computed."""
import sys, itertools, time
from sympy.polys.rings import ring
from sympy import ZZ, symbols, factor, cancel
from bfull import to_e, parts
t = symbols('t')
def apply_op(a, Fdict_fn, N, order):
    Rg, *g = ring(['t']+[f'x{i}' for i in range(N)], ZZ); T, xs = g[0], g[1:]
    V = Rg(1)
    for i in range(N):
        for j in range(i+1, N): V *= xs[i]-xs[j]
    F = Fdict_fn(Rg, xs); Fd = F.to_dict(); tot = Rg(0)
    for A in itertools.combinations(range(N), a):
        Bc = [j for j in range(N) if j not in A]
        sign = (-1)**sum(1 for i in A for j in Bc if i > j); term = Rg(sign)
        for i in range(N):
            for j in range(i+1, N):
                if (i in A) == (j in A): term *= xs[i]-xs[j]
        for i in A:
            term *= xs[i]
            for j in Bc: term *= xs[i]-T*xs[j]
        def w(m):
            d = sum(m[1+i] for i in A)
            return d*(d-1)//2 if order == 2 else d
        G = Rg.from_dict({m: c*w(m) for m, c in Fd.items() if w(m)})
        tot += term*G
    q, r = tot.div(V); assert r == 0
    return q
def esym(Rg, xs, k):
    s = Rg(0)
    for S in itertools.combinations(range(len(xs)), k):
        m = Rg(1)
        for i in S: m *= xs[i]
        s += m
    return s
def L(a, b): return cancel((1-t**(a+b))/((1-t**a)*(1-t**b))*(t**(a*b)-1))
nmax = int(sys.argv[1]); ok = okD = cnt = 0
for n in range(3, nmax+1):
    for lam in parts(n):
        if len(lam) != 3: continue
        a, b, c = lam; t0 = time.time()
        q = apply_op(a, lambda Rg, xs: esym(Rg, xs, b)*esym(Rg, xs, c), n, 2); E = to_e(q, n)
        X = E.get((n,), 0)
        pref = (1-t**n)/((1-t**a)*(1-t**b)*(1-t**c))
        good = cancel(X - pref*(t**(a*b)-1)*(t**(a*c)-1)) == 0
        # D_a(D_b e_c) e_n-coefficient, computed via bfull D_b(e_c) expansion is not polynomial-direct; do it directly:
        q1 = apply_op(b, lambda Rg, xs: esym(Rg, xs, c), n, 1)   # D_b e_c (in n vars)
        q2 = apply_op(a, lambda Rg, xs: q1.parent.from_dict(q1.to_dict()) if False else Rg.from_dict(q1.to_dict()), n, 1)
        E2 = to_e(q2, n); Y = E2.get((n,), 0)
        goodD = cancel(Y - L(b, c)*L(a, b+c)) == 0
        cnt += 1; ok += good; okD += goodD
        print(f'{lam} [{time.time()-t0:.1f}s]: [e_n]E_a^(2)(e_b e_c) = {factor(X)}  == pref*w_ab*w_ac: {good};  [e_n]D_aD_b e_c == L(b,c)L(a,b+c): {goodD}', flush=True)
        print(f'     full E_a^(2)(e_b e_c) = { {k: factor(v) for k, v in E.items()} }', flush=True)
print(f'SECOND-ORDER REMAINDER {ok}/{cnt}; ITERATED-B DIRECT {okD}/{cnt}')
