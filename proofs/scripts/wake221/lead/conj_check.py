"""Wake 221: test conjectured closed forms against symbolic history leads (leads_n8.pkl).
(G) Lead_{lam,(n)} = (1-t^n) K_lam / prod_i (1-t^{lam_i}),  K_lam = sum_{H connected graph on [l]} prod_{ij in H} (t^{lam_i lam_j}-1)
(F) Lead_{lam,mu} = sum_{set partitions pi of [l], sorted block sums = mu} prod_{C in pi} Lead_{lam_C,(|lam_C|)}
(I) Lead_{1^n,(n)} = (-1)^{n-1}[n]_t I_n(t), I_n via Mallows-Riordan: sum I_n (t-1)^{n-1} x^n/n! = log sum t^{C(n,2)} x^n/n!
(T) #H(lam,(n)) = (l-1)!;  (C) Lead_{lam,(n)}(1) = (-1)^{l-1} n^{l-1}."""
import pickle, itertools, functools
from math import factorial
from sympy import symbols, cancel, expand, series, log, exp, Rational, simplify, factor
t, x = symbols('t x')
res = pickle.load(open('leads_n8.pkl', 'rb'))
@functools.lru_cache(None)
def K(lam):
    # connected-graph sum via recursion Conn(S) = Tot(S) - sum_{min S in T, T<S} Conn(T) Tot(S-T),
    # Tot(S) = prod_{i<j in S}(1 + (t^{a_i a_j}-1)) = t^{e2(lam_S)}
    l = len(lam)
    def tot(S): return t**sum(lam[i]*lam[j] for i, j in itertools.combinations(S, 2))
    conn = {}
    for r in range(1, l+1):
        for S in itertools.combinations(range(l), r):
            v = tot(S); rest = S[1:]
            for q in range(0, len(rest)):
                for c in itertools.combinations(rest, q):
                    T = (S[0],)+c; U = tuple(i for i in S if i not in T)
                    v -= conn[T]*tot(U)
            conn[S] = expand(v)
    return conn[tuple(range(l))]
def G(lam):
    n = sum(lam); d = 1
    for a in lam: d *= 1-t**a
    return cancel((1-t**n)*K(tuple(lam))/d)
def setparts(s):
    if not s: yield []; return
    a, rest = s[0], s[1:]
    for r in range(len(rest)+1):
        for c in itertools.combinations(rest, r):
            rem = [y for y in rest if y not in c]
            for p in setparts(rem): yield [(a,)+c]+p
okG = okT = okC = 0; totG = 0; maxl = 0
for (lam, mu), (L, c) in res.items():
    if len(mu) != 1: continue
    totG += 1; l = len(lam)
    okG += cancel(L-G(lam)) == 0
    okT += c == factorial(l-1)
    okC += cancel(L).subs(t, 1) == (-1)**(l-1)*sum(lam)**(l-1)
print(f'(G) full-merge closed form: {okG}/{totG};  (T) #H=(l-1)!: {okT}/{totG};  (C) Lead(1)=(-1)^(l-1) n^(l-1): {okC}/{totG}')
okF = totF = 0
for (lam, mu), (L, c) in res.items():
    if len(mu) == 1 or sum(lam) > 7: continue
    totF += 1; s = 0
    for p in setparts(list(range(len(lam)))):
        if tuple(sorted((sum(lam[i] for i in C) for C in p), reverse=True)) != mu: continue
        term = 1
        for C in p: term *= G(tuple(lam[i] for i in C)) if len(C) > 1 else 1
        s += term
    okF += cancel(L-s) == 0
print(f'(F) coarsening factorization (n<=7, all proper coarsenings mu, l(mu)>=2): {okF}/{totF}')
ser = series(log(sum(t**(m*(m-1)//2)*x**m/factorial(m) for m in range(10))), x, 0, 9).removeO()
okI = 0
for n in range(2, 9):
    In = cancel(ser.coeff(x, n)*factorial(n)/(t-1)**(n-1))
    L = res[((1,)*n, (n,))][0]
    good = cancel(L-(-1)**(n-1)*cancel((1-t**n)/(1-t))*In) == 0; okI += good
    print(f'  n={n}: I_n={expand(In)}  match={good}')
print(f'(I) 1^n inversion-enumerator form: {okI}/7')
