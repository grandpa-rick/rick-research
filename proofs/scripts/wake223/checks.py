"""Wake 223 Task A checks on bfull_n7.pkl (symbolic t) and wake221 leads_n8.pkl. Grade: computed."""
import pickle
from sympy import symbols, cancel, factor, expand
t = symbols('t')
res = pickle.load(open('bfull_n7.pkl', 'rb'))
def br(m): return (1-t**m)/(1-t)
def L(a, b): return cancel((1-t**(a+b))/((1-t**a)*(1-t**b))*(t**(a*b)-1))
p1 = p2 = p3 = 0; N = 0
print('== e_{a+b} coefficient of B(e_a,e_b), a>=b, a+b<=7 ==')
for (a, b), E in sorted(res.items()):
    n = a+b; c = E.get((n,), 0); N += 1
    ok1 = cancel(c - L(a, b)) == 0
    ok2 = cancel(c + br(n)*br(a*b)/(br(a)*br(b))) == 0
    # full support formula: B(e_a,e_b) = b e_a e_b + sum_{j=1}^b L(a-b+j, j) e_{a+j} e_{b-j}
    pred = {tuple(sorted((a, b), reverse=True)): b}
    for j in range(1, b+1):
        mu = tuple(sorted([x for x in (a+j, b-j) if x > 0], reverse=True)); pred[mu] = pred.get(mu, 0) + L(a-b+j, j)
    ok3 = set(pred) == set(E) and all(cancel(pred[k]-E[k]) == 0 for k in E)
    p1 += ok1; p2 += ok2; p3 += ok3
    print(f'({a},{b}): coeff = {factor(c)} | pred (1-t^n)(t^ab-1)/((1-t^a)(1-t^b)): {ok1} | -[n][ab]/([a][b]): {ok2} | full-support formula: {ok3} | support {sorted(E)}')
print(f'PREDICTION {p1}/{N}; q-INTEGER FORM {p2}/{N}; FULL-SUPPORT FORMULA {p3}/{N}')
print('== ps multiplicativity: ps(p_k)=1/(1-t^k) => prod ps(p_{lam_i})/ps(p_n) == (1-t^n)/prod(1-t^{lam_i}) (identity, checked symbolically n<=8) ==')
from itertools import combinations
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
okp = cnt = 0
for n in range(2, 9):
    for lam in parts(n):
        ps = lambda k: 1/(1-t**k)
        lhs = 1
        for x in lam: lhs *= ps(x)
        lhs /= ps(n); rhs = (1-t**n)
        for x in lam: rhs /= (1-t**x)
        cnt += 1; okp += cancel(lhs-rhs) == 0
print(f'PS {okp}/{cnt}')
print('== l=3: Lead_{(a,b,c),(n)} vs prefactor * connected-graph sum, and split into iterated-B part + remainder ==')
leads = pickle.load(open('../wake221/lead/leads_n8.pkl', 'rb'))
g = gB = gR = 0; cnt = 0
for (lam, mu), (e, _) in sorted(leads.items()):
    if len(lam) != 3 or mu != (sum(lam),): continue
    a, b, c = lam; n = a+b+c
    pref = (1-t**n)/((1-t**a)*(1-t**b)*(1-t**c))
    wab, wac, wbc = t**(a*b)-1, t**(a*c)-1, t**(b*c)-1
    K = wab*wac + wab*wbc + wac*wbc + wab*wac*wbc
    okG = cancel(e - pref*K) == 0
    # e_a*(e_b*e_c): (s-1)^2 coefficient at e_n = D_a D_b e_c part + E_a^{(2)}(e_b e_c) part
    iterB = L(b, c)*L(a, b+c)                              # = pref*wbc*(wab+wac+wab*wac)
    okB = cancel(iterB - pref*wbc*(wab+wac+wab*wac)) == 0
    rem = cancel(e - iterB); okR = cancel(rem - pref*wab*wac) == 0
    cnt += 1; g += okG; gB += okB; gR += okR
    print(f'{lam}: G {okG}; L(b,c)L(a,b+c)=pref*w_bc(w_ab+w_ac+w_ab w_ac) {okB}; remainder = pref*w_ab*w_ac {okR}')
print(f'G(l=3) {g}/{cnt}; ITERATED-B IDENTITY {gB}/{cnt}; REMAINDER = pref*w_ab*w_ac {gR}/{cnt}')
