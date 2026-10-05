"""
Day 205: exact, dependency-free engine for the level-one AHA polynomial
representation, used to check the reduction  Sub-Lemma Z  ->  (L1)-(L4).

Coefficient ring: Laurent polynomials in t and Q := q^{-1} with integer
coefficients, stored as dict {(t_exp, Q_exp): int}.
Polynomial in X_1..X_m: dict {exponent tuple: coeff}.

Conventions (identical to scripts/day198/p2Y_er.py::build_action; this is
cross-checked in reduction_0_conventions.py):
  T_i F  = t s_i F + (t-1) X_{i+1} (s_i F - F)/(X_i - X_{i+1})
  T_i^{-1} = t^{-1} T_i - (1 - t^{-1})
  pi F   = X_1 F(X_2, ..., X_m, q^{-1} X_1)
  Y_i    = t^{m-i} T_{i-1} ... T_1  pi  T_{m-1}^{-1} ... T_i^{-1}
  sigma_m = sum_{k=0}^{m-1} T_k T_{k-1} ... T_1
"""
from itertools import combinations
from functools import lru_cache

# ---------------- coefficient ring Z[t^{+-1}, Q^{+-1}] ----------------
def c_add(a, b, sb=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + sb * v
        if r[k] == 0:
            del r[k]
    return r

def c_shift(a, dt=0, dQ=0, s=1):
    return {(k[0] + dt, k[1] + dQ): s * v for k, v in a.items()}

def c_mul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = (k1[0] + k2[0], k1[1] + k2[1])
            r[k] = r.get(k, 0) + v1 * v2
    return {k: v for k, v in r.items() if v}

ONE = {(0, 0): 1}
def c_t(n): return {(n, 0): 1}
def c_Q(n): return {(0, n): 1}
def c_int(n): return {(0, 0): n} if n else {}
def tint(n):
    """[n]_t = 1 + ... + t^{n-1} (0 for n <= 0)."""
    return {(i, 0): 1 for i in range(n)} if n > 0 else {}

def c_str(a):
    if not a:
        return "0"
    parts = []
    for (te, Qe), v in sorted(a.items()):
        mon = "*".join(x for x in [f"t^{te}" if te else "", f"q^{-Qe}" if Qe else ""] if x)
        parts.append(f"{v}" + ("*" + mon if mon else ""))
    return " + ".join(parts)

# ---------------- polynomials ----------------
def p_add_term(P, e, c):
    if not c:
        return
    if e in P:
        s = c_add(P[e], c)
        if s:
            P[e] = s
        else:
            del P[e]
    else:
        P[e] = dict(c)

def p_add(P1, P2, s2=1):
    R = {e: dict(c) for e, c in P1.items()}
    for e, c in P2.items():
        p_add_term(R, e, c if s2 == 1 else c_shift(c, s=s2))
    return R

def p_scale(P, c):
    R = {}
    for e, d in P.items():
        p_add_term(R, e, c_mul(d, c))
    return R

def p_mul(P1, P2):
    R = {}
    for e1, c1 in P1.items():
        for e2, c2 in P2.items():
            p_add_term(R, tuple(a + b for a, b in zip(e1, e2)), c_mul(c1, c2))
    return R

def p_is_zero(P):
    return len(P) == 0

def monomial(m, expo, c=ONE):
    return {tuple(expo): dict(c)}

def var(m, i):
    """X_i, 1-indexed."""
    e = [0] * m
    e[i - 1] = 1
    return {tuple(e): dict(ONE)}

@lru_cache(maxsize=None)
def _e_sym(m, k, lo):
    """e_k(X_{lo+1}, ..., X_m) as frozen dict (lo = number of skipped leading vars)."""
    if k < 0 or k > m - lo:
        return ()
    res = []
    for S in combinations(range(lo, m), k):
        e = [0] * m
        for j in S:
            e[j] = 1
        res.append(tuple(e))
    return tuple(res)

def e_sym(m, k, lo=0):
    """e_k in variables X_{lo+1..m}; e_0 = 1; 0 if k<0 or k > #vars."""
    return {e: dict(ONE) for e in _e_sym(m, k, lo)}

def e_tail(m, k):
    return e_sym(m, k, lo=1)

_elam_cache = {}
def e_lam(m, lam):
    key = (m, tuple(lam))
    if key not in _elam_cache:
        P = {tuple([0] * m): dict(ONE)}
        for part in lam:
            P = p_mul(P, e_sym(m, part))
        _elam_cache[key] = P
    return _elam_cache[key]

# ---------------- operators ----------------
def swap(e, i):
    e = list(e)
    e[i - 1], e[i] = e[i], e[i - 1]
    return tuple(e)

def T(P, i):
    """T_i, 1 <= i <= m-1."""
    R = {}
    for e, c in P.items():
        a, b = e[i - 1], e[i]
        # t * s_i
        p_add_term(R, swap(e, i), c_shift(c, dt=1))
        if a == b:
            continue
        # (t-1) X_{i+1} (s_i x^e - x^e)/(X_i - X_{i+1})
        # D := (A^b B^a - A^a B^b)/(A-B)
        if a > b:
            sign, lo, n = -1, b, a - b
        else:
            sign, lo, n = 1, a, b - a
        tm1 = c_add(c_shift(c, dt=1), c, sb=-1)  # (t-1) c
        for p in range(n):
            ne = list(e)
            ne[i - 1] = lo + p
            ne[i] = lo + (n - 1 - p) + 1  # extra X_{i+1}
            p_add_term(R, tuple(ne), c_shift(tm1, s=sign))
    return R

def Tinv(P, i):
    """T_i^{-1} = t^{-1} T_i - (1 - t^{-1})."""
    A = {e: c_shift(c, dt=-1) for e, c in T(P, i).items()}
    B = {e: c_add(c, c_shift(c, dt=-1), sb=-1) for e, c in P.items()}
    return p_add(A, B, -1)

def PI(P):
    """pi F = X_1 F(X_2, ..., X_m, q^{-1} X_1)."""
    R = {}
    for e, c in P.items():
        m = len(e)
        ne = (e[m - 1] + 1,) + tuple(e[: m - 1])
        p_add_term(R, ne, c_shift(c, dQ=e[m - 1]))
    return R

def rho(P, j):
    """rho_j := T_{j-1} ... T_1 (rho_1 = id)."""
    for k in range(1, j):
        P = T(P, k)
    return P

def sigma(P, m):
    """sigma_m = sum_{k=0}^{m-1} T_k ... T_1, computed by the recursion
    rho_{k+1} = T_k rho_k."""
    total = {e: dict(c) for e, c in P.items()}
    cur = P
    for k in range(1, m):
        cur = T(cur, k)
        total = p_add(total, cur)
    return total

def Y(P, i, m):
    G = P
    for j in range(i, m):
        G = Tinv(G, j)
    G = PI(G)
    for j in range(1, i):
        G = T(G, j)
    return {e: c_shift(c, dt=m - i) for e, c in G.items()}

def e1Y(P, m):
    tot = {}
    for i in range(1, m + 1):
        tot = p_add(tot, Y(P, i, m))
    return tot

# ---------------- e-basis decomposition ----------------
def conj(lam):
    return tuple(sum(1 for x in lam if x > j) for j in range(lam[0])) if lam else ()

def e_decompose(P, m):
    """Expand a symmetric polynomial P in {e_mu : mu_1 <= m}.  Leading-term
    algorithm: the lex-leading monomial of e_mu is x^{mu'} with coeff 1.
    Raises if P is not symmetric (leading exponent not a partition).
    Returns {mu: coeff}; the remainder is checked to be exactly 0."""
    P = {e: dict(c) for e, c in P.items()}
    out = {}
    while P:
        lead = max(P)
        if any(lead[j] < lead[j + 1] for j in range(m - 1)):
            raise ValueError(f"not symmetric: leading exponent {lead}")
        lam = tuple(x for x in lead if x > 0)
        mu = conj(lam)  # mu_1 = len(lam) <= m
        c = P[lead]
        out[mu] = c_add(out.get(mu, {}), c)
        P = p_add(P, p_scale(e_lam(m, mu), c), -1)
    return {k: v for k, v in out.items() if v}

def sorted_part(*xs):
    return tuple(sorted((x for x in xs if x > 0), reverse=True))

def from_e_expansion(m, expansion):
    P = {}
    for mu, c in expansion.items():
        P = p_add(P, p_scale(e_lam(m, mu), c))
    return P

def exp_equal(E1, E2):
    keys = set(E1) | set(E2)
    return all(not c_add(E1.get(k, {}), E2.get(k, {}), sb=-1) for k in keys)

def exp_add(E1, E2, w=ONE):
    R = {k: dict(v) for k, v in E1.items()}
    for k, v in E2.items():
        s = c_add(R.get(k, {}), c_mul(v, w))
        if s:
            R[k] = s
        elif k in R:
            del R[k]
    return R

# ---------------- claimed right-hand sides ----------------
def claimed_L(r, which):
    """(L1)-(L4) right-hand sides as {partition: coeff}; e_mu = prod e_{mu_i}."""
    neg = lambda c: c_shift(c, s=-1)
    A, B, two = tint(r + 2), c_shift(tint(r), dt=1), tint(2)   # [r+2], t[r], [2]
    E = {}
    def put(mu, c):
        mu = sorted_part(*mu)
        s = c_add(E.get(mu, {}), c)
        if s:
            E[mu] = s
        elif mu in E:
            del E[mu]
    if which == 1:
        put((r + 2,), A); put((r + 1, 1), B)
    elif which == 2:
        put((r + 2,), neg(A)); put((r + 1, 1), ONE)
    elif which == 3:
        put((r + 2,), neg(A)); put((r + 1, 1), neg(B)); put((r, 2), two)
    elif which == 4:
        put((r + 2,), A); put((r + 1, 1), neg(ONE)); put((r, 2), neg(two)); put((r, 1, 1), ONE)
    return E

def claimed_Z(r):
    """Sub-Lemma Z coefficients (Day 203 table), rewritten in Q = q^{-1}:
       (r,1,1): Q^2 ; (r,2): Q(1-Q)[2]_t ; (r+1,1): (1-Q)(t[r]_t + Q) ;
       (r+2): (1-Q)^2 [r+2]_t .  Colliding partitions (r=1) are summed."""
    one_m_Q = c_add(ONE, c_Q(1), sb=-1)                         # 1 - q^{-1}
    E = {}
    def put(mu, c):
        mu = sorted_part(*mu)
        s = c_add(E.get(mu, {}), c)
        if s:
            E[mu] = s
        elif mu in E:
            del E[mu]
    put((r, 1, 1), c_Q(2))                                           # q^{-2}
    put((r, 2), c_mul(c_mul(c_Q(1), one_m_Q), tint(2)))             # (q-1)[2]_t/q^2
    put((r + 1, 1), c_mul(one_m_Q, c_add(c_shift(tint(r), dt=1), c_Q(1))))  # (1-q^-1)(t[r]_t+q^-1)
    put((r + 2,), c_mul(c_mul(one_m_Q, one_m_Q), tint(r + 2)))      # (q-1)^2[r+2]_t/q^2
    return E

WEIGHTS = {1: c_Q(0), 2: c_Q(1), 3: c_Q(1), 4: c_Q(2)}
