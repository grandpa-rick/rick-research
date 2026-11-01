# Q55 cominuscule scout (PROVE 269 compute agent, 2026-11-01).
# For (W,J): test (a) [x,y] in W^J Boolean, (b) [x,y]_W subset W^J, (c) y = v x, v = product of distinct pairwise
# commuting simple reflections with lengths adding (the "antichain skew heap"; = antichain in join-irreducible poset when
# W^J is distributive -- also checked), (d) P^{J,q}_{x,y}=1, (d-) P^{J,-1}_{x,y}=1.
# Elements of W are encoded as the vector w(rho) in fundamental-weight coordinates; no enumeration of W is needed except for
# the optional full-KL cross-check on small groups.
import itertools, sys

def cartan(t, n):
    A = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
    def link(i, j, aij=-1, aji=-1): A[i][j] = aij; A[j][i] = aji
    if t in 'ABCD' or t == 'E':
        if t == 'E':   # Bourbaki: 1-3-4-5-6(-7), 2-4
            for i, j in [(0, 2), (2, 3), (3, 4), (1, 3)] + [(k, k+1) for k in range(4, n-1)]: link(i, j)
            return A
        for k in range(n-2): link(k, k+1)
        if t == 'A': link(n-2, n-1)
        if t == 'B': link(n-2, n-1, -1, -2)   # A[i][j]=<a_i^v,a_j>: B_n: a_{n-1} long, a_n short
        if t == 'C': link(n-2, n-1, -2, -1)
        if t == 'D': link(n-3, n-1)  # nodes n-2 and n-1 (0-based) both attached to n-3
        if t == 'D': link(n-3, n-2)
        return A
    if t == 'G': link(0, 1, -1, -3); return A
    if t == 'F': link(0, 1); link(1, 2, -2, -1); link(2, 3); return A
    raise ValueError

class Cox:
    def __init__(s, A):
        s.A = A; s.n = len(A); s.rho = tuple([1]*s.n)
        s.alpha = [tuple(A[i][j] for i in range(s.n)) for j in range(s.n)]  # alpha_j in omega coords = column j
        s.m = {}
        for i in range(s.n):
            for j in range(s.n):
                p = A[i][j]*A[j][i]; s.m[(i, j)] = {0: 2, 1: 3, 2: 4, 3: 6, 4: 1}[p] if i != j else 1
    def refl(s, i, mu):
        c = mu[i]
        return tuple(mu[k] - c*s.alpha[i][k] for k in range(s.n)) if c else mu
    def le(s, a, b):   # Bruhat a <= b, elements as w(rho)
        while b != s.rho:
            i = next(k for k in range(s.n) if b[k] < 0)
            if a[i] < 0: a = s.refl(i, a)
            b = s.refl(i, b)
        return a == s.rho
    def length(s, a):
        l = 0
        while a != s.rho:
            i = next(k for k in range(s.n) if a[k] < 0); a = s.refl(i, a); l += 1
        return l
    def apply_word(s, word, mu):   # element = s_{word[0]} ... s_{word[-1]}
        for i in reversed(word): mu = s.refl(i, mu)
        return mu

def quotient(C, J):
    lam = tuple(0 if k in J else 1 for k in range(C.n))
    els = {lam: (C.rho, [], 0)}  # wlam -> (wrho, word, length)
    frontier = [lam]
    while frontier:
        nf = []
        for mu in frontier:
            wr, wd, l = els[mu]
            for i in range(C.n):
                if mu[i] > 0:
                    nu = C.refl(i, mu)
                    if nu not in els: els[nu] = (C.refl(i, wr), [i]+wd, l+1); nf.append(nu)
        frontier = nf
    return lam, els

# ---- polynomials
def padd(a, b):
    r = [0]*max(len(a), len(b))
    for i, c in enumerate(a): r[i] += c
    for i, c in enumerate(b): r[i] += c
    while r and r[-1] == 0: r.pop()
    return tuple(r)
def pmul(a, b):
    if not a or not b: return ()
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] += x*y
    while r and r[-1] == 0: r.pop()
    return tuple(r)
def psc(a, k, c=1): return tuple([0]*k+[c*x for x in a]) if a else ()
neg = lambda a: tuple(-x for x in a)

def parKL(Wj, leq, lnf, act, gens, xparam):   # copied from prove268/q55.py (Deodhar R-recursion on W^J)
    order = sorted(Wj, key=lnf); R = {}
    fac = (0, 1) if xparam == '-1' else (-1,)
    for tau in order:
        for sig in Wj:
            if not leq(sig, tau): continue
            if sig == tau: R[(sig, tau)] = (1,); continue
            s = next(i for i in gens if act(i, tau)[0] == 'down'); st = act(s, tau)[1]
            k, ss = act(s, sig)
            if k == 'down': R[(sig, tau)] = R.get((ss, st), ())
            elif k == 'up': R[(sig, tau)] = padd(pmul((-1, 1), R.get((sig, st), ())), psc(R.get((ss, st), ()), 1))
            else: R[(sig, tau)] = pmul(fac, R.get((sig, st), ()))
    P = {}
    for tau in order:
        for sig in sorted([s for s in Wj if leq(s, tau)], key=lnf, reverse=True):
            if sig == tau: P[(sig, tau)] = (1,); continue
            F = ()
            for rho in Wj:
                if rho != sig and leq(sig, rho) and leq(rho, tau): F = padd(F, pmul(R[(sig, rho)], P[(rho, tau)]))
            d = lnf(tau)-lnf(sig); p = list(neg(tuple(F[:(d-1)//2+1]))) if F else []
            while p and p[-1] == 0: p.pop()
            P[(sig, tau)] = tuple(p)
    return P

def boolean(elts, leq):
    mn = [x for x in elts if all(leq(x, y) for y in elts)]
    if len(mn) != 1: return False
    mn = mn[0]; others = [x for x in elts if x != mn]
    atoms = [a for a in others if not any(b != a and leq(b, a) for b in others)]
    S = {x: frozenset(i for i, a in enumerate(atoms) if leq(a, x)) for x in elts}
    if len(set(S.values())) != len(elts) or len(elts) != 2**len(atoms): return False
    return all(leq(x, y) == (S[x] <= S[y]) for x in elts for y in elts)

def fullW(C):
    els = {C.rho: []}; fr = [C.rho]
    while fr:
        nf = []
        for a in fr:
            for i in range(C.n):
                b = C.refl(i, a)
                if b not in els: els[b] = [i]+els[a]; nf.append(b)
        fr = nf
    return els

def fullKL(C, els):
    L = list(els); ln = {a: len(els[a]) for a in L}
    order = sorted(L, key=lambda a: ln[a]); P = {}; mu = {}
    below = {w: [x for x in L if C.le(x, w)] for w in L}
    for w in order:
        if w == C.rho: P[(w, w)] = (1,); continue
        s = next(i for i in range(C.n) if w[i] < 0); v = C.refl(s, w)
        zs = [z for z in below[v] if z[s] < 0 and mu.get((z, v), 0)]
        for x in below[w]:
            c = 1 if x[s] < 0 else 0; sx = C.refl(s, x)
            t = padd(psc(P.get((sx, v), ()), 1-c), psc(P.get((x, v), ()), c))
            for z in zs:
                if C.le(x, z): t = padd(t, neg(psc(P[(x, z)], (ln[w]-ln[z])//2, mu[(z, v)])))
            P[(x, w)] = t; d = ln[w]-ln[x]
            if d % 2 == 1 and len(t) == (d-1)//2+1: mu[(x, w)] = t[-1]
    return P

def run(name, t, n, J, label, xcheck=False):
    C = Cox(cartan(t, n)); J = set(J)
    lam, els = quotient(C, J)
    Wj = list(els); ln = lambda a: els[a][2]
    leq = lambda a, b: C.le(els[a][0], els[b][0])
    def act(i, a):
        c = a[i]
        if c == 0: return ('stay', None)
        return ('up' if c > 0 else 'down', C.refl(i, a))
    PJ = {x: parKL(Wj, leq, ln, act, range(C.n), x) for x in ['q', '-1']}
    comm = [S for k in range(C.n+1) for S in itertools.combinations(range(C.n), k)
            if all(C.m[(i, j)] == 2 for i, j in itertools.combinations(S, 2))]
    # distributivity + join-irreducibles
    up = {a: [b for b in Wj if leq(a, b) and ln(b) == ln(a)+1] for a in Wj}
    lowc = {a: [b for b in Wj if leq(b, a) and ln(b) == ln(a)-1] for a in Wj}
    JI = [a for a in Wj if len(lowc[a]) == 1]
    def is_lattice_distributive():
        # distributive iff |{order ideals of JI}| == |W^J| and map a -> {j<=a} is an order iso onto ideals
        img = {a: frozenset(j for j in JI if leq(j, a)) for a in Wj}
        if len(set(img.values())) != len(Wj): return False
        lowJ = {j: frozenset(j2 for j2 in JI if j2 != j and leq(j2, j)) for j in JI}
        seen = {frozenset()}; fr = [frozenset()]
        while fr and len(seen) <= len(Wj):   # BFS over order ideals of JI; abort once more ideals than |W^J|
            nf = []
            for S in fr:
                for j in JI:
                    if j not in S and lowJ[j] <= S:
                        T = S | {j}
                        if T not in seen: seen.add(T); nf.append(T)
            fr = nf
        nid = len(seen)
        return nid == len(Wj) and all(leq(a, b) == (img[a] <= img[b]) for a in Wj for b in Wj)
    dist = is_lattice_distributive()
    stats = {}; fails = {}; cmismatch = 0; pairs = 0
    Pf = None
    if xcheck:
        Wall = fullW(C); Pf = fullKL(C, Wall)
        WJel = [u for u in Wall if all(i in J for i in Wall[u])]
        wJ = max(WJel, key=lambda u: len(Wall[u])); xbad = [0, 0, 0]
    for x in Wj:
        for y in Wj:
            if not leq(x, y): continue
            pairs += 1
            I = [a for a in Wj if leq(x, a) and leq(a, y)]
            A = boolean(I, leq)
            B = not any(C.le(C.apply_word(els[v][1], C.refl(s, C.rho)), els[y][0]) for v in I for s in J)
            # (c) weak-order antichain
            Cc = False
            for S in comm:
                z = x; ok = True
                for i in S:
                    k, z2 = act(i, z)
                    if k != 'up': ok = False; break
                    z = z2
                if ok and z == y: Cc = True; break
            if dist:
                th = [j for j in JI if leq(j, y) and not leq(j, x)]
                Cji = not any(a != b and leq(a, b) for a in th for b in th)
                cmismatch += (Cji != Cc)
            Dq = PJ['q'][(x, y)] == (1,); Dm = PJ['-1'][(x, y)] == (1,)
            key = (A, B, Cc, Dq, Dm); stats[key] = stats.get(key, 0)+1
            if xcheck:
                xr, yr = els[x][0], els[y][0]; ww = lambda r, u: C.apply_word(Wall[r], u)  # r*u as vector
                alt = ()
                for u in WJel: alt = padd(alt, psc(Pf.get((ww(xr, u), yr), ()), 0, (-1)**len(Wall[u])))
                xbad[0] += alt != PJ['q'][(x, y)]
                xbad[1] += Pf.get((ww(xr, wJ), ww(yr, wJ)), ()) != PJ['-1'][(x, y)]
                full = [w for w in Wall if C.le(xr, w) and C.le(w, yr)]
                xbad[2] += all(quot_min(C, w, J) for w in full) != B
    names = ['a', 'b', 'c', 'd', 'd-']
    imp = {}
    for p in range(5):
        for q in range(5):
            if p != q:
                imp[(p, q)] = sum(v for k, v in stats.items() if k[p] and not k[q])
    out = [f"## {name}  [{label}]  |W^J|={len(Wj)}, pairs x<=y: {pairs}, W^J distributive: {dist}"
           + (f", (c) weak-vs-JI mismatches: {cmismatch}" if dist else ", (c) = weak-order version only")]
    out.append("   key (a,b,c,d,d-): count  " + "; ".join(f"{tuple(int(z) for z in k)}:{v}" for k, v in sorted(stats.items())))
    core = [(p, q) for p in range(4) for q in range(4) if p != q]
    out.append("   failures of implication X=>Y among a,b,c,d: " +
               ", ".join(f"{names[p]}=>{names[q]}:{imp[(p,q)]}" for p, q in core))
    out.append("   u=-1 convention: d-=>a fails " + str(imp[(4, 0)]) + ", a=>d- fails " + str(imp[(0, 4)]))
    if xcheck:
        out.append(f"   full-KL cross-check (|W|={len(Wall)}): P^Jq vs alt-sum bad={xbad[0]}, P^J-1 vs P(xw_J,yw_J) bad={xbad[1]}, (b) shortcut vs full interval bad={xbad[2]}")
    print("\n".join(out)); sys.stdout.flush()
    return stats

def quot_min(C, w, J):   # w (as w rho) in W^J iff no right descent in J iff w(alpha_j) > 0; test via length
    lw = C.length(w)
    return all(C.length(C.apply_word_vec(w, j)) > lw for j in J)

def _apply_right(C, w, j):  # w s_j as vector: need a word for w; recover by descent-peeling
    word = []; a = w
    while a != C.rho:
        i = next(k for k in range(C.n) if a[k] < 0); word.append(i); a = C.refl(i, a)
    return C.apply_word(word, C.refl(j, C.rho))
Cox.apply_word_vec = _apply_right

if __name__ == '__main__':
    X = True
    cases = [
        # Bourbaki 0-based node labels; J = nodes KEPT in W_J
        ("A3 Gr(2,4)", 'A', 3, {0, 2}, "minuscule+cominuscule", X),
        ("A4 Gr(2,5)", 'A', 4, {0, 2, 3}, "minuscule+cominuscule", X),
        ("A5 Gr(2,6)", 'A', 5, {0, 2, 3, 4}, "minuscule+cominuscule", False),
        ("A5 Gr(3,6)", 'A', 5, {0, 1, 3, 4}, "minuscule+cominuscule", False),
        ("C3 LG(3,6) (=B3 spinor quotient)", 'C', 3, {0, 1}, "C: cominuscule; B: minuscule (same W,J)", X),
        ("B3 node1 Q^5 (=C3 P^5 quotient)", 'B', 3, {1, 2}, "B: cominuscule; C: minuscule (same W,J)", X),
        ("B4 spinor/LG(4,8)", 'B', 4, {0, 1, 2}, "B: minuscule; C: cominuscule", False),
        ("D4 node1 quadric", 'D', 4, {1, 2, 3}, "minuscule+cominuscule", X),
        ("D4 node4 spinor", 'D', 4, {0, 1, 2}, "minuscule+cominuscule", X),
        ("D5 node1 quadric", 'D', 5, {1, 2, 3, 4}, "minuscule+cominuscule", False),
        ("D5 node5 spinor", 'D', 5, {0, 1, 2, 3}, "minuscule+cominuscule", False),
        ("E6 node1", 'E', 6, {1, 2, 3, 4, 5}, "minuscule+cominuscule", False),
        ("E7 node7", 'E', 7, {0, 1, 2, 3, 4, 5}, "minuscule+cominuscule", False),
        # controls
        ("CONTROL A3 J={s2} (non-maximal)", 'A', 3, {1}, "not maximal", X),
        ("CONTROL A3 J={s1} (non-maximal)", 'A', 3, {0}, "not maximal", X),
        ("CONTROL B3 node2", 'B', 3, {0, 2}, "neither", X),
        ("CONTROL G2 node1", 'G', 2, {1}, "neither", X),
        ("CONTROL G2 node2", 'G', 2, {0}, "neither", X),
        ("CONTROL C4 node2", 'C', 4, {0, 2, 3}, "neither", False),
        ("CONTROL D4 node2", 'D', 4, {0, 2, 3}, "neither (adjoint)", X),
        ("CONTROL F4 node4", 'F', 4, {0, 1, 2}, "neither", False),
        ("CONTROL E6 node2 (adjoint)", 'E', 6, {0, 2, 3, 4, 5}, "neither", False),
    ]
    sel = sys.argv[1:]
    for c in cases:
        if sel and not any(s in c[0] for s in sel): continue
        run(*c)
