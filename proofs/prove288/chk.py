"""PROVE 288 check: operator identities used in the Q71-U0 proof. Conventions = wake287/u0filt/core.py."""
import sys; sys.path.insert(0, '../wake287/u0filt')
from core import setup, T_ops, U0_ops
from flint import fmpz_mat
def col(M, j): return [int(M[r, j]) for r in range(M.nrows())]
for n in (2, 3):
    for N in range(3, 8 if n == 2 else 6):
        W, idx, d = setup(n, N); ops = U0_ops(n, N); Ts = T_ops(n, N)
        I = fmpz_mat([[int(r == c) for c in range(d)] for r in range(d)])
        p = (I - ops['k0']) * (I - ops['k1'])
        for i in range(2, n): p = p * ops['k%d' % i]
        # p_S = projector onto words with support exactly {0,1}
        assert all(int(p[r, c]) == int(r == c and set(W[r]) == {0, 1}) for r in range(d) for c in range(d))
        f = p * ops['f0'] * p; e = p * ops['e0'] * p
        F = I; E = I
        for _ in range(N - 2): F = f * F; E = e * E
        u = lambda q: idx[tuple(1 if t == q else 0 for t in range(1, N+1))]   # 1 at position q
        v = lambda q: idx[tuple(0 if t == q else 1 for t in range(1, N+1))]   # 0 at position q
        # (A) f^{N-2} u_{N-1} = v_N ; kills u_k (k<N-1) and every {0,1}-word with >=2 ones
        assert col(F, u(N-1)) == col(I, v(N))
        for w in W:
            if set(w) == {0, 1} and (w.count(1) >= 2 or (w.count(1) == 1 and w.index(1) < N-2)):
                assert not any(col(F, idx[w])), w
        # (B) e^{N-2} v_2 = u_1 ; kills v_p (p>=3) and every {0,1}-word with <= N-2 ones
        assert col(E, v(2)) == col(I, u(1))
        for w in W:
            if set(w) == {0, 1} and (w.count(1) <= N-2 or (w.count(1) == N-1 and w.index(0) >= 2)):
                assert not any(col(E, idx[w])), w
        # f^{N-2}, e^{N-2} commute with H
        for T in Ts: assert F*T == T*F and E*T == T*E
        print('ok', n, N)
