"""Recursive end-test for filtrations with subquotients L_I x P_I on quotients V/U."""
import sys, json, numpy as np, itertools
import step2 as S2
from lin import *
src = open('step2.py').read()
# re-use run() internals by exec-ing a modified copy that returns its closures
src = src.replace("    res = dict(n=n, N=N, dimJH", "    return locals()\n    res = dict(n=n, N=N, dimJH")
ns = {}; exec(compile(src.replace("if __name__ == '__main__':", "if False:"), 'step2mod', 'exec'), ns)
n, N = int(sys.argv[1]), int(sys.argv[2])
L = ns['run'](n, N)
d = L['d']; JS = L['JS']; socHrho = L['socHrho']; layer_decomp = L['layer_decomp']; wl = L['wl']; rho = L['rho']
chi = L['chi']; subsets = L['subsets']; comp_of = ns['comp_of']
def times(ops, vecs):
    out = []
    for M in ops:
        P = M @ np.array(vecs, dtype=object).T
        out += [list(P[:, c]) for c in range(P.shape[1])]
    return out
def bottom(U):
    SocS = preimage_in(JS, U, d)
    Zb = basis_of(U + times(socHrho, SocS), d)
    return layer_decomp(Zb, U), Zb
def iso_component(Zb, U, Jlab, Hcomp):
    """subspace of Zb (containing U) = U + (S-label Jlab, H-char Hcomp) isotypic part. Only valid when the
    H-char determines it uniquely within the semisimple Zb/U: we take the H-eigenspace and, if other S-labels
    share that H-char, refuse."""
    D = [D for D in subsets if comp_of(D, N) == Hcomp][0]
    annU = nullspace(U, d) if U else [[int(i == j) for j in range(d)] for i in range(d)]
    cols = np.array(Zb, dtype=object).T; rows = []
    for i in range(N-1):
        M = (rho[i] - chi(D, i)*np.eye(d, dtype=object)) @ cols
        for a in annU: rows.append(list(np.array(a, dtype=object) @ M))
    co = nullspace(rows, len(Zb))
    vec = [list(cols @ np.array(c, dtype=object)) for c in co]
    return basis_of(U + vec, d)
U0 = []
b0, Zb0 = bottom(U0)
print('bottom(V):', b0)
results = {'bottom(V)': {str(k): v for k, v in b0.items()}}
# explore: repeatedly peel 1-dim-P pieces (P_I 1-dim => piece = isotypic comp), report bottom sets
frontier = [((), U0)]
seen = {}
while frontier:
    path, U = frontier.pop()
    b, Zb = bottom(U)
    key = str(path); seen[key] = {str(k): v for k, v in b.items()}
    print('after peeling', path, 'dimU', dim_span(U), 'bottom pairs:', b)
    for (J, K), mlt in b.items():
        # candidate piece L_J x P_J requires K = nu(J)
        if K != L['nu_c'][J][0][0] if J in L['nu_c'] else True: continue
        if J in path: continue
        # 1-dim P iff nu(J)=J and J in {(N,), (1,)*N}
        if J in [(N,), (1,)*N]:
            U2 = iso_component(Zb, U, J, K)
            frontier.append((path + (J,), U2))
        else:
            print('  non-1dim candidate', J, '-- needs manual handling')
json.dump(seen, open(f'step3_{n}{N}.json', 'w'), indent=1)
